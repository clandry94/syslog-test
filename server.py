#!/usr/bin/env python

from __future__ import print_function

import argparse
import socket
import os
import sys
import json

from syslog_rfc5424_parser import SyslogMessage, ParseError


def main():
    messages = [
            '<6> 2023-08-11T20:37:32.029385Z felt web-aaaaa 1 {"foo": "bar"}',
            '<6>1 2023-08-11T20:37:32.029385Z felt web-aaaaa 1 - - {"foo": "bar"}',
            ]
    
    for m in messages:
        try:
            message = SyslogMessage.parse(m)
            print(json.dumps(message.as_dict()))
        except ParseError as e:
            print(e, file=sys.stderr)


if __name__ == '__main__':
    sys.exit(main())
