#!/usr/bin/python3
"""fab script that delets out-of-date archives """
from fabric.api import *
from datetime import datetime
import os
env.hosts = ['54.89.21.208', "35.153.194.6"]


def do_clean(number=0):
    files_ = os.listdir("versions")
    files_.sort(reverse=True)
    present = len(files_)
    number = int(number)
    # keep only the most recent version of your archive
    if number >= present:
        return
    if number == 0:
        number = 1
    else:
        number = number
    num_del = present - number
    point = -1
    for i in range(num_del):
        local("rm versions/{}".format(files_[point]))
        point -= 1
    """
    Deleting all unnecessary archives (all archives
    minus the number to keep) in the /data/web_static/releases
    """
    with cd("/tmt"):
        run("ls -t -r | head -n -{} | sudo xargs rm".format(number))
