#!/usr/bin/env python
import shlex
import sys

from context_managers import ssh_context 


with ssh_context(_out=sys.stdout, _err=sys.stdout) as shell:
    shell(shlex.split('cat /etc/resolv.conf'))
    shell(shlex.split('pwd'))

