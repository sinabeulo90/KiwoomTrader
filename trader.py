from core import KWCore
from constants import KWErrorCode

from importer import *

class KWTrader(KWCore):

    def initialize(self):
        self.tr_list['opt10001'] = Opt10001(self)
        self.tr_list['opt10002'] = Opt10002(self)
        self.tr_list['opt10003'] = Opt10003(self)

    def connection(self):
        self.comm_connect()


    # [ opt10001 : 주식기본정보요청 ]
    def opt10001(self, code, prev_next, screen_no):
        return self.tr_list['opt10001'].tr_opt(code, prev_next, screen_no)


    #  [ opt10002 : 주식거래원요청 ]
    def opt10002(self, code, prev_next, screen_no):
        return self.tr_list['opt10002'].tr_opt(code, prev_next, screen_no)


    #  [ opt10003 : 체결정보요청 ]
    def opt10003(self, code, prev_next, screen_no):
        return self.tr_list['opt10003'].tr_opt(code, prev_next, screen_no)
