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
