#!/usr/bin/python3
""" compress files """
from fabric.api import *
import time
import subprocess
import os


def do_pack():
    """ compress files """
    try:
        now = time.strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_" + now + ".tgz"
        if not os.path.isdir("versions"):
            os.makedirs("versions")
        bash_cmd = local("tar -cvzf {} web_static".format(filename))
        return ("$filename")
    except:
        return None

env.hosts = ['34.75.53.84', '3.89.225.162']

def do_deploy(archive_path):
    """ decompress files after sending """

    try:        
        if not os.path.exists(archive_path):
            return False
        put(archive_path, "/tmp/")
        filename = archive_path[9:-4]
        arch_dest = "/data/web_static/releases/" + filename + "/"
        run("sudo mkdir -p {}".format(arch_dest))
        run("sudo tar -xvzf {} {}".format(archive_path, arch_dest))
        run("sudo rm -R {}".format(archive_path))
        run("sudo ln -sf /data/web_static/releases/{}/ /data/web_static/current".format(filename))
        return True
    except:
        return False
