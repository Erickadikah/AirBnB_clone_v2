#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_static folder"""
from fabric.api import *
from datetime import datetime

env.hosts = ['54.89.21.208', "35.153.194.6"]


def do_deploy(archive_path):
    """A fabric script that distributes archive to your web servers"""
    if not archive_path:
        return False
    try:
        with cd('/tmp'):
            res = put(archive_path, "/tmp")
            print(res)
        archive = archive_path.split('/')[-1]
        free = archive.split('.')[0]
        sudo('mkdir -p /data/web_static/releases/{}/'.format(free))
        sudo('tar -xzf /tmp/{} -C /data/web_static/releases\
/{}/'.format(archive, free))
        sudo('rm /tmp/{}'.format(archive))
        sudo('mv /data/web_static/releases\
/{}/web_static/* /data/web_static/releases/{}'.format(free, free))
        sudo('rm -rf /data/web_static/releases/{}/web_static'.format(free))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s /data/web_static/releases\
/{}/ /data/web_static/current'.format(free))
        return True
    except:
        return False
