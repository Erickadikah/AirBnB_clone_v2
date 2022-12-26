#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_static folder"""
from fabric.api import *
from datetime import datetime
from fabric.api import put, run, env
import os


env.hosts = ['54.89.21.208', "35.153.194.6"]


def do_deploy(archive_path):
    """deploy function gerates a .tgz archive from the contents of webstatic"""
    if not os.path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    temp = archive_path.split('.')[0]
    file_name = temp.split('/')[1]
    dest = data_path + file_name

    try:
        put(archive_path, '/tmp')
        run('sudo mkdir -p {}'.format(dest))
        run('sudo tar -xzf /tmp/{}.tgz -C {}'.format(file_name, dest))
        run('sudo rm -f /tmp/{}.tgz'.format(file_name))
        run('sudo mv {}/web_static/* {}/'.format(dest, dest))
        run('sudo rm -rf {}/web_static/'.format(dest))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(dest))
        return True
    except RuntimeError:
        return False

