#!/usr/bin/env python3

import click
from datetime import datetime
from tqdm import tqdm
import re
import math
import requests
import os
import shutil
import os.path as op
import subprocess
import tarfile
import json


OSF_DOWNLOAD = "https://osf.io/{}/download"
OSF_METADATA = "https://osf.io/{}/metadata?format=datacite-json"
OSF_URL = {'2023-10-02_Winawer-lab-mtg': 'spu5e'}


@click.group()
def cli():
    pass

@click.command()
@click.argument('dir')
def package_assets(dir: str):
    """Package assets directory into a tar ball.

    DIR is the path to the assets directory (e.g.,
    2023-10-02_Winawer-lab-mtg/assets/)

    """
    if dir[-1] == op.sep:
        dir = dir[:-1]
    output_dir = dir + '.tar.gz'
    print(f"Packaging {dir} into {output_dir}")
    with tarfile.open(output_dir, 'w:gz') as tar:
        tar.add(dir)


@click.command()
@click.argument('tar_path')
def upload(tar_path: str):
    """Upload assets tarball to OSF

    TAR_PATH is the path to the assets tarball (e.g.,
    2023-10-02_Winawer-lab-mtg/assets.tar.gz)

    Note that this requires the osf command line tool to be set up (see README
    for details)

    """
    tar_name = tar_path.replace(op.sep, '_')
    subprocess.run(['osf', 'upload', '-f', tar_path, f"osfstorage/{tar_name}"])


def download_url(url: str, destination_path: str):
    """Helper function to download `url` to `destination_path`
    """
    # Streaming, so we can iterate over the response.
    r = requests.get(url, stream=True)
    # Total size in bytes.
    total_size = int(r.headers.get('content-length', 0))
    block_size = 1024*1024
    wrote = 0
    with open(destination_path, 'wb') as f:
        for data in tqdm(r.iter_content(block_size), unit='MB',
                         unit_scale=True,
                         total=math.ceil(total_size//block_size)):
            wrote += len(data)
            f.write(data)
    if total_size != 0 and wrote != total_size:
        raise Exception(f"Error downloading from {url}!")


def extract_tar(path: str):
    """Helper function to extract tarballs
    """
    with tarfile.open(path) as f:
        f.extractall(op.dirname(path))
    os.remove(path)


def _get_date_modified(dir_path: str):
    """Gets date modified for OSF object
    """
    url = OSF_URL[dir_path]
    r = requests.get(OSF_METADATA.format(url))
    meta = json.loads(r.text)
    mod = [d for d in meta['dates'] if d['dateType'] == 'Updated']
    if len(mod) != 1:
        raise Exception(f"Unable to find date modified for {dir_path}!")
    return mod[0]['date']


@click.command()
@click.argument('dir_path')
def get_date_modified(dir_path: str):
    """Gets date modified for OSF object
    """
    # can't call the CLI command from within the script, so need to do this
    date = _get_date_modified(dir_path)
    click.echo(f"{dir_path} modified: {date}")


@click.command()
@click.argument('dir_path')
def download(dir_path: str):
    """Download assets tarball from OSF then extract and arrange files.

    DIR_PATH is the path of the directory whose associated files you want to
    download from the OSF (e.g., 2023-10-02_Winawer-lab-mtg/) or `all` (to
    download all of them)

    Note that this DOES NOT requires the osf command line tool to be set up.

    """
    if dir_path != 'all':
        urls = {dir_path: OSF_URL[dir_path]}
    else:
        urls = OSF_URL
    for k, v in urls.items():
        print(f"Downloading {k}")
        download_url(OSF_DOWNLOAD.format(v), 'tmp.tar.gz')
        remote_modified = _get_date_modified(k)
        remote_modified = datetime.strptime(remote_modified, '%Y-%m-%d').timestamp()
        if op.exists(op.join(k, 'assets')):
            local_modified = op.getmtime(op.join(k, 'assets'))
            if remote_modified < local_modified:
                click.echo("You have local changes more recent than the remote tarball, do you wish to continue extracting?")
                choice = input('y/n: ')
                while choice not in ['y', 'n']:
                    click.echo("Please enter y or n")
                if choice == 'n':
                    shutil.move('tmp.tar.gz', k + '.tar.gz')
                    click.echo(f"Tarball is located at {op.abspath(k + '.tar.gz')}, check its contents with "
                               "tar tvf PATH to see modification times and extract it yourself")
                    continue
        extract_tar('tmp.tar.gz')


@click.command()
@click.argument('dir_path')
def check_assets(dir_path: str):
    """Check to make sure DIR_PATH contains all necessary assets

    DIR_PATH is the path of the directory whose associated files you want to
    check (e.g., 2023-10-02_Winawer-lab-mtg/) or `all` (to check all of them)

    """
    if dir_path != 'all':
        dir_path = [dir_path]
    else:
        dir_path = list(OSF_URL.keys())
    for dir_p in dir_path:
        with open(op.join(dir_p, 'slides.md')) as f:
            slides = f.read()
        slides_assets = re.findall('assets/[A-Za-z0-9_.-]+', slides)
        slides_assets = [a.replace('assets/', '') for a in slides_assets]
        local_assets = os.listdir(op.join(dir_p, 'assets'))
        only_slides = [a for a in slides_assets if a not in local_assets]
        if len(only_slides):
            print('\n'.join(only_slides))
            raise Exception(f"The above assets are only in slides file (not in assets folder)!")
        only_local = [a for a in local_assets if a not in slides_assets]
        if len(only_local):
            print('\n'.join(only_local))
            raise Exception(f"The above assets are only in assets folder (not in slides file)!")


cli.add_command(package_assets)
cli.add_command(upload)
cli.add_command(download)
cli.add_command(get_date_modified)
cli.add_command(check_assets)

if __name__ == '__main__':
    cli()
