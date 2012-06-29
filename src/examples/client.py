#!/usr/bin/env python -u

import os
import sys

import argparse

from struct import unpack
from socket import inet_ntoa

from pyptlib.config import EnvException
from pyptlib.client import ClientConfig

class UnsupportedManagedTransportVersionException(Exception):
  pass

class NoSupportedTransportsException(Exception):
  pass

class TransportLaunchException(Exception):
  def __init__(self, message):
    message=message

def launchClient(self, name, port):
  if name!=supportedTransport:
    raise TransportLaunchException('Tried to launch unsupported transport %s' % (name))

if __name__=='__main__':
    supportedTransportVersion='1'
    supportedTransport='dummy'
    config=ClientConfig()

  if config.checkManagedTransportVersion(supportedTransportVersion):
    config.writeVersion(supportedTransportVersion)
  else:
    config.writeVersionError()
    raise UnsupportedManagedTransportVersionException()

  if not config.checkTransportEnabled(supportedTransport):
    raise NoSupportedTransportsException()
  except EnvException:
    print('error 0')
    return
  except UnsupportedManagedTransportVersionException:
    print('error 1')
    return
  except NoSupportedTransportsException:
    print('error 2')
    return

  try:
    launchClient(supportedTransport, 8182)
    config.writeMethod(supportedTransport, 5, ('127.0.0.1', 8182), None, None)
  except TransportLaunchException as e:
    print('error 3')
    config.writeMethodError(supportedTransport, e.message)

  config.writeMethodEnd()

  run()
