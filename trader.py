from core import KWCore
from constants import KWErrorCode

from importer import *

class KWTrader(KWCore):

    def initialize(self):
        self.tr_list['opt10001'] = Opt10001(self)
        self.tr_list['opt10002'] = Opt10002(self)
        self.tr_list['opt10003'] = Opt10003(self)
        self.tr_list['opt10004'] = Opt10004(self)
        self.tr_list['opt10005'] = Opt10005(self)
        self.tr_list['opt10006'] = Opt10006(self)
        self.tr_list['opt10007'] = Opt10007(self)
        self.tr_list['opt10008'] = Opt10008(self)
        self.tr_list['opt10009'] = Opt10009(self)
        self.tr_list['opt10010'] = Opt10010(self)
        # self.tr_list['opt10011'] = Opt10011(self)     # opt10011 : Does not exist.
        self.tr_list['opt10012'] = Opt10012(self)
        self.tr_list['opt10013'] = Opt10013(self)
        self.tr_list['opt10014'] = Opt10014(self)
        self.tr_list['opt10015'] = Opt10015(self)


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


    # [ opt10004 : 주식호가요청 ]
    def opt10004(self, code, prev_next, screen_no):
        return self.tr_list['opt10004'].tr_opt(code, prev_next, screen_no)


    # [ opt10005 : 주식일주월시분요청 ]
    def opt10005(self, code, prev_next, screen_no):
        return self.tr_list['opt10005'].tr_opt(code, prev_next, screen_no)


    # [ OPT10006 : 주식시분요청 ]
    def opt10006(self, code, prev_next, screen_no):
        return self.tr_list['opt10006'].tr_opt(code, prev_next, screen_no)


    # [ opt10007 : 시세표성정보요청 ]
    def opt10007(self, code, prev_next, screen_no):
        return self.tr_list['opt10007'].tr_opt(code, prev_next, screen_no)


    # [ opt10008 : 시세표성정보요청 ]
    def opt10008(self, code, prev_next, screen_no):
        return self.tr_list['opt10008'].tr_opt(code, prev_next, screen_no)


    # [ OPT10009 : 주식기관요청 ]
    def opt10009(self, code, prev_next, screen_no):
        return self.tr_list['opt10009'].tr_opt(code, prev_next, screen_no)


    # [ OPT10010 : 업종프로그램요청 ]
    def opt10010(self, code, prev_next, screen_no):
        return self.tr_list['opt10010'].tr_opt(code, prev_next, screen_no)


    # [ opt10012 : 주문체결요청 ]
    def opt10012(self, code, prev_next, screen_no):
        return self.tr_list['opt10012'].tr_opt(code, prev_next, screen_no)


    # [ opt10013 : 신용매매동향요청 ]
    def opt10013(self, code, date, type_flag, prev_next, screen_no):
        return self.tr_list['opt10013'].tr_opt(code, date, type_flag, prev_next, screen_no)


    # [ opt10014 : 공매도추이요청 ]
    def opt10014(self, code, date_type, date_from, date_to, prev_next, screen_no):
        return self.tr_list['opt10014'].tr_opt(code, date_type, date_from, date_to, prev_next, screen_no)


    # [ opt10015 : 일별거래상세요청 ]
    def opt10015(self, code, date, prev_next, screen_no):
        return self.tr_list['opt10015'].tr_opt(code, date, prev_next, screen_no)
