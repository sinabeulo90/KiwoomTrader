from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10030 : 당일거래량상위요청 ]
class Opt10030(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10030'

        self.record_name_multiple = '당일거래량상위'
        self.header_multiple = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '등락률', '거래량', '전일비', '거래회전율', '거래금액',
        ]


    def tr_opt(self, market_type, input1, input2, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 정렬구분 = 1:거래량, 2:거래회전율, 3:거래대금
        # 관리종목포함 = 0:관리종목 포함, 1:관리종목 미포함

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('정렬구분', input1)
        self.core.set_input_value('관리종목포함', input2)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
