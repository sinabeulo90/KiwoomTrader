from tr_option.base import KWTR
from copy import deepcopy

# [ opt10008 : 주식외국인요청 ]
class Opt10008(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10008'

        self.record_name_multiple = '주식외국인'
        self.header_multiple = [
            '일자', '종가', '전일대비', '거래량', '변동수량', '보유주식수', '비중',
            '취득가능주식수', '외국인한도', '외국인한도증감', '한도소진률',
        ]


    def tr_opt(self, code, prev_next, screen_no):
        # 종목코드 = 000:전체, 001:코스피, 101:코스닥

        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
