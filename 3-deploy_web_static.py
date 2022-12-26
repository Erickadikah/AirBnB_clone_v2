#!/usr/bin/env bash
# distributing archiveuploading and deplyoying on servers
from fabric.api import*
from datetime import datetime


env.hosts = ['54.89.21.208',"35.153.194.6"]


def do_pack():
     """generating a .tgz archive from the contents of the web_static"""
     local('mkdir -p versions')
     time = datetime.now().strftime("%Y%m%d%H%M%S")
     name = "web_static_{}.tgz".format(time)
     file_name = "versions/{}".format(name)
     location = local("tar -cvzf {} web_static/".format(file_name))
     if location:
         return (location)
     else:
         return None


def do_deploy(archive_path):
     if not archive_path:
         return False

     #uploading to /tmp/ in the server
     with cd ("/tmp/"):
         res = put(archive_path, "/tmp/")
         print(res)

     #creating a directory for the file extraction
     run("mkdir -p /data/web_static/releases/")

     #getting the file
     file_name =archive_path.split("/")[-1]

     #Extracting the file from archive
     remote_name = file_name.split(".")[0]
     run("mkdir -p /data/web_static/releases/{}".format(remote_name))
     run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
         .format(file_name, remote_name))

     # Delete the archive from the web serve
     run("rm /tmp/{}".format(file_name))

     #moving file out of web_static
     run("mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/".format(remote_name, remote_name))

     # Deleting the symbolic link
     run("rm -rf /data/web_static/current")

     #creating new symbolic link
     run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
         .format(remote_name))
     return True

def deploy():
     """distributing archie to web server"""
     path = do_pack()
     if not path:
         return False
     f = do_deploy(path)
     return (f)

