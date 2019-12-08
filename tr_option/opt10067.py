from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10067 : 대차거래내역요청 ]
class Opt10067(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10067'

        self.record_name_multiple = '대차거래내역'
        self.header_multiple = [
            '종목명', '종목코드', '대차거래체결주수', '대차거래상환주수', '잔고주수', '잔고금액',
        ]


    def tr_opt(self, date, market_type, prev_next, screen_no):
        # 기준일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 시장구분 = 001:코스피, 101:코스닥

        self.core.set_input_value('기준일자', date)
        self.core.set_input_value('시장구분', market_type)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
