from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10069 : 대차거래상위10종목요청 ]
class Opt10069(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10069'

        self.record_name_single = '대차거래상위10종목합계'
        self.header_single = [
            '대차거래체결주수합', '대차거래상환주수합', '잔고주수합', '잔고금액합', '대차거래체결주수비율', '대차거래상환주수비율', '잔고주수비율', '잔고금액비율',
        ]

        self.record_name_multiple = '대차거래상위10종목'
        self.header_multiple = [
            '종목명', '종목코드', '대차거래체결주수', '대차거래상환주수', '잔고주수', '잔고금액',
        ]


    def tr_opt(self, date_from, date_to, market_type, prev_next, screen_no):
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 종료일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 시장구분 = 001:코스피, 101:코스닥

        self.core.set_input_value('시작일자', date_from)
        self.core.set_input_value('종료일자', date_to)
        self.core.set_input_value('시장구분', market_type)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
