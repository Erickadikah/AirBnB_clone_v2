#!/usr/bin/python3
from fabric.api import *

def deploy():
    local('web_static')
