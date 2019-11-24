from tr_option.base import KWTR
from copy import deepcopy

# [ opt10002 : 주식거래원요청 ]
class Opt10002(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10002'

        self.record_name_multiple = '주식거래원'
        self.header_multiple = [
            '종목코드', '종목명', '현재가', '등락부호', '기준가', '전일대비', '등락율',
            '매도거래원명1', '매도거래원1', '매도거래량1', '매수거래원명1', '매수거래원1', '매수거래량1',
            '매도거래원명2', '매도거래원2', '매도거래량2', '매수거래원명2', '매수거래원2', '매수거래량2',
            '매도거래원명3', '매도거래원3', '매도거래량3', '매수거래원명3', '매수거래원3', '매수거래량3',
            '매도거래원명4', '매도거래원4', '매도거래량4', '매수거래원명4', '매수거래원4', '매수거래량4',
            '매도거래원명5', '매도거래원5', '매도거래량5', '매수거래원명5', '매수거래원5', '매수거래량5',
        ]


    def tr_opt(self, code, prev_next, screen_no):
	    # 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
