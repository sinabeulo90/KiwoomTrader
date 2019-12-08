from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10068 : 대차거래추이요청 ]
class Opt10068(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10068'

        self.record_name_multiple = '대차거래추이'
        self.header_multiple = [
            '일자', '대차거래체결주수', '대차거래상환주수', '대차거래증감', '잔고주수', '잔고금액',
        ]


    def tr_opt(self, date_from, date_to, input2, code, prev_next, screen_no):
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 종료일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 전체구분 = 1: 전체표시,
        #           0:종목코드 (지원안함. OPT20068사용).
        # 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value('시작일자', date_from)
        self.core.set_input_value('종료일자', date_to)
        self.core.set_input_value('전체구분', input2)
        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
