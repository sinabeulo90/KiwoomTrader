from tr_option.base import KWTR
from copy import deepcopy

# [ opt10070 : 당일주요거래원요청 ]
class Opt10070(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10070'

        self.record_name_multiple = '당일주요거래원'
        self.header_multiple = [
            '매도거래원별증감1', '매도거래원수량1', '매도거래원1', '매도거래원코드1', '매수거래원1', '매수거래원코드1', '매수거래원별증감1',
            '매도거래원별증감2', '매도거래원수량2', '매도거래원2', '매도거래원코드2', '매수거래원2', '매수거래원코드2', '매수거래원별증감2',
            '매도거래원별증감3', '매도거래원수량3', '매도거래원3', '매도거래원코드3', '매수거래원3', '매수거래원코드3', '매수거래원별증감3',
            '매도거래원별증감4', '매도거래원수량4', '매도거래원4', '매도거래원코드4', '매수거래원4', '매수거래원코드4', '매수거래원별증감4',
            '매도거래원별증감5', '매도거래원수량5', '매도거래원5', '매도거래원코드5', '매수거래원5', '매수거래원코드5', '매수거래원별증감5',
            '외국계매도추정합변동', '외국계매도추정합', '외국계매수추정합', '외국계매수추정합변동',
        ]


    def tr_opt(self, code, prev_next, screen_no):
	    # 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
