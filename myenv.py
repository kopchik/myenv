#!/usr/bin/env python3
import argparse
import shlex
import sys
import os

VERSION = 2
def log(*args):
  print(*args, file=sys.stderr)


def main():
  epilog = "Version: {}.".format(VERSION)
  parser = argparse.ArgumentParser(epilog=epilog)
  parser.add_argument('-d', '--debug', default=False,
                      action='store_const', const=True)
  parser.add_argument('cmd', nargs="+")

  # PARSE CMD
  myfile = os.path.basename(__file__)
  if os.environ['_'].endswith('/'+myfile):
    # normal invocation
    args = parser.parse_args()
  else:
    # if invoked from shabang we need to split args
    rawcmd = " ".join(sys.argv[1:])
    cmd = shlex.split(rawcmd)
    args = parser.parse_args(cmd)

  # PROCESS EXTRA FLAGS
  if args.debug:
    log("env:", os.environ)
    log("now invoking", args.cmd)

  # RUN
  try:
    executable = args.cmd[0]
    cmd = args.cmd
    os.execvp(executable, cmd)
  except FileNotFoundError as err:
    log("{script}: failed to exec: {path}: {err}".format(
          script=__file__,
          path=executable, err=err))
    return 127


if __name__ == '__main__':
  sys.exit(main())