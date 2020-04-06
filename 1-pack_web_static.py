#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import local
from datetime import datetime
from os import path


def do_pack():
    """Function to compress directory

    Return: path to archive on success; None on fail
    """
    # Get current time
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = '~/AirBnB_clone_v2/versions/web_static_' + now + '.tgz'

    # Create archive
    local('mkdir -p ~/AirBnB_clone_v2/versions/')
    local('tar -czf {} ~/AirBnB_clone_v2/web_static/'.format(archive_path))

    # Check if archiving was successful
    if path.isfile(archive_path):
        return archive_path
    return None