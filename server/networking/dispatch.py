# -*- coding: iso-8859-1 -*-

import os
if os.name == 'posix':
  from twisted.internet import epollreactor
  epollreactor.install()
elif os.name == 'nt':
  from twisted.internet import selectreactor
  selectreactor.install()
else:
  raise Exception("Unrecognized OS: {}".format(os.name))

from sexpr.sexpr import sexpr2str, str2sexpr

from twisted.internet import protocol, reactor
from twisted.protocols.basic import Int32StringReceiver

class SexpProtocol(Int32StringReceiver):
  app = None
  sessions = 0

  def connectionMade(self):
    self.session_num = SexpProtocol.sessions
    SexpProtocol.sessions += 1

    self.app = self.__class__.app(self)

  def connectionLost(self, reason):
    self.app.disconnect(reason)
      
  def stringReceived(self, string):
    expr = str2sexpr(string)
    for command in expr:
      result = self.app.run(command)
      if result:
        self.sendString(sexpr2str(result))

  @classmethod
  def main(cls, port=19000):
    f = protocol.ServerFactory()
    f.protocol = cls
    reactor.listenTCP(port, f)
    reactor.run()
