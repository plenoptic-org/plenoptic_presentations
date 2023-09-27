#!/usr/bin/env python3

import click
from tqdm import tqdm
import math
import requests
import os
import os.path as op
import subprocess
import tarfile


OSF_DOWNLOAD = "https://osf.io/{}/download"
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
        extract_tar('tmp.tar.gz')


cli.add_command(package_assets)
cli.add_command(upload)
cli.add_command(download)

if __name__ == '__main__':
    cli()
