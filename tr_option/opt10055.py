from tr_option.base import KWTR
from copy import deepcopy

# [ opt10055 : 당일전일체결대량요청 ]
class Opt10055(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10055'

        self.record_name_multiple = '당일전일체결대량'
        self.header_multiple = [
            '체결시간', '체결가', '전일대비기호', '전일대비', '등락율', '체결량', '누적거래량', '누적거래대금',
        ]


    def tr_opt(self, code, input1, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 당일전일 = 1:당일,	2:전일

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('당일전일', input1)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
