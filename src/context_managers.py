from contextlib import contextmanager
import os
import subprocess
import sys
import shlex

import sh

TARGET_ADDRESS = os.environ['TARGET_ADDRESS']
TARGET_USER = os.environ.get('TARGET_USER') or os.environ.get('USER')
SOCKET_FILE = os.environ.get('TMP_SSH_SOCKET_FILE', '/tmp/example.sock')


@contextmanager
def ssh_context(target_address: str=None, target_user: str=None, **kwargs):
    # config
    target_address = target_address or TARGET_ADDRESS
    target_user = target_user or TARGET_USER
    socket_file = SOCKET_FILE

    ssh_cmd_base = f'{target_user}@{target_address} -S {socket_file}'
    ssh_shell = sh.ssh.bake(shlex.split(ssh_cmd_base), **kwargs)

    # create master tunnel
    ssh_shell('-MfnNT')

    yield ssh_shell

    # cleanup the master tunnel
    ssh_shell(shlex.split('-O exit'), _bg=True)

