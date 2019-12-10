from tr_option.base import KWTR
from copy import deepcopy

# [ opt10074 : 일자별실현손익요청 ]
class Opt10074(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10074'

        self.record_name_single = '일자별실현손익단일'
        self.header_single = [
            '총매수금액', '총매도금액', '실현손익', '매매수수료', '매매세금',
        ]
        self.record_name_multiple = '일자별실현손익'
        self.header_multiple = [
            '일자', '매수금액', '매도금액', '당일매도손익', '당일매매수수료', '당일매매세금',
        ]


    def tr_opt(self, input0, date_from, date_to, prev_next, screen_no):
        # 계좌번호 = 전문 조회할 보유계좌번호
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 종료일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)

        self.core.set_input_value('계좌번호', input0)
        self.core.set_input_value('시작일자', date_from)
        self.core.set_input_value('종료일자', date_to)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
