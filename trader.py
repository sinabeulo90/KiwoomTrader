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
        self.tr_list['opt10016'] = Opt10016(self)
        self.tr_list['opt10017'] = Opt10017(self)
        self.tr_list['opt10018'] = Opt10018(self)
        self.tr_list['opt10019'] = Opt10019(self)
        self.tr_list['opt10020'] = Opt10020(self)
        self.tr_list['opt10021'] = Opt10021(self)
        self.tr_list['opt10022'] = Opt10022(self)
        self.tr_list['opt10023'] = Opt10023(self)
        self.tr_list['opt10024'] = Opt10024(self)
        self.tr_list['opt10025'] = Opt10025(self)
        self.tr_list['opt10026'] = Opt10026(self)
        self.tr_list['opt10027'] = Opt10027(self)
        self.tr_list['opt10028'] = Opt10028(self)
        self.tr_list['opt10029'] = Opt10029(self)
        self.tr_list['opt10030'] = Opt10030(self)
        self.tr_list['opt10031'] = Opt10031(self)
        self.tr_list['opt10032'] = Opt10032(self)
        self.tr_list['opt10033'] = Opt10033(self)
        self.tr_list['opt10034'] = Opt10034(self)
        self.tr_list['opt10035'] = Opt10035(self)
        self.tr_list['opt10036'] = Opt10036(self)
        self.tr_list['opt10037'] = Opt10037(self)


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


    # [ OPT10016 : 신고저가요청 ]
    def opt10016(self, market_type, input1, input2, input3, input4, input5, input6, date, prev_next, screen_no):
        return self.tr_list['opt10016'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, date, prev_next, screen_no)


    # [ opt10017 : 상하한가요청 ]
    def opt10017(self, market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        return self.tr_list['opt10017'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no)


    # [ OPT10018 : 고저가근접요청 ]
    def opt10018(self, input0, input1, input2, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10018'].tr_opt(input0, input1, input2, input3, input4, input5, prev_next, screen_no)


    # [ opt10019 : 가격급등락요청 ]
    def opt10019(self, market_type, input1, date_type, date, input4, input5, input6, input7, input8, prev_next, screen_no):
        return self.tr_list['opt10019'].tr_opt(market_type, input1, date_type, date, input4, input5, input6, input7, input8, prev_next, screen_no)


    # [ OPT10020 : 호가잔량상위요청 ]
    def opt10020(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10020'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT10021 : 호가잔량급증요청 ]
    def opt10021(self, market_type, input1, input2, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10021'].tr_opt(market_type, input1, input2, input3, input4, input5, prev_next, screen_no)


    # [ OPT10022 : 잔량율급증요청 ]
    def opt10022(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10022'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT10023 : 거래량급증요청 ]
    def opt10023(self, market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        return self.tr_list['opt10023'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no)


    # [ OPT10024 : 거래량갱신요청 ]
    def opt10024(self, market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10024'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10025 : 매물대집중요청 ]
    def opt10025(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10025'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ opt10026 : 고저PER요청 ]
    def opt10026(self, per_type, prev_next, screen_no):
        return self.tr_list['opt10026'].tr_opt(per_type, prev_next, screen_no)


    # [ opt10027 : 전일대비등락률상위요청 ]
    def opt10027(self, market_type, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no):
        return self.tr_list['opt10027'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no)


    # [ opt10028 : 시가대비등락률요청 ]
    def opt10028(self, input0, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no):
        return self.tr_list['opt10028'].tr_opt(input0, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no)


    # [ OPT10029 : 예상체결등락률상위요청 ]
    def opt10029(self, market_type, input1, input2, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10029'].tr_opt(market_type, input1, input2, input3, input4, input5, prev_next, screen_no)


    # [ OPT10030 : 당일거래량상위요청 ]
    def opt10030(self, market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10030'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10031 : 전일거래량상위요청 ]
    def opt10031(self, market_type, input1, input2, input3, prev_next, screen_no):
        return self.tr_list['opt10031'].tr_opt(market_type, input1, input2, input3, prev_next, screen_no)


    # [ OPT10032 : 거래대금상위요청 ]
    def opt10032(self, market_type, input1, prev_next, screen_no):
        return self.tr_list['opt10032'].tr_opt(market_type, input1, prev_next, screen_no)


    # [ opt10033 : 신용비율상위요청 ]
    def opt10033(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10033'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT10034 : 외인기간별매매상위요청 ]
    def opt10034(self,  market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10034'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10035 : 외인연속순매매상위요청 ]
    def opt10035(self, market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10035'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10036 : 매매상위요청 ]
    def opt10036(self, market_type, input1, prev_next, screen_no):
        return self.tr_list['opt10036'].tr_opt(market_type, input1, prev_next, screen_no)


    # [ opt10037 : 외국계창구매매상위요청 ]
    def opt10037(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10037'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)
