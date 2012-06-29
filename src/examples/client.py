#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyptlib.easy.client import init, reportSucess, reportFailure, \
    reportEnd


class TransportLaunchException(Exception):

    pass


def launchClient(self, name, port):
    if name != 'dummy':
        raise TransportLaunchException('Tried to launch unsupported transport %s'
                 % name)


if __name__ == '__main__':
    supportedTransports = ['dummy', 'rot13']

    matchedTransports = init(supportedTransports)
    for transport in matchedTransports:
        try:
            launchClient(transport, 8182)
            reportSuccess(transport, 5, ('127.0.0.1', 8182), None, None)
        except TransportLaunchException:
            reportFailure(transport, 'Failed to launch')
    reportEnd()
