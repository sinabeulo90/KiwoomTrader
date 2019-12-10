from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10072 : 일자별종목별실현손익요청 ]
class Opt10072(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10072'

        self.record_name_multiple = '일자별종목별실현손익'
        self.header_multiple = [
            '일자', '당일hts매도수수료', '종목명', '체결량', '매입단가', '체결가', '당일매도손익', '손익율', '종목코드', '당일매매수수료', '당일매매세금', '인출가능금액', '대출일', '신용구분', '종목코드1', '당일매도손익1',
        ]


    def tr_opt(self, input0, code, date_from, prev_next, screen_no):
        # 계좌번호 = 전문 조회할 보유계좌번호
        # 종목코드 = 전문 조회할 종목코드
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)

        self.core.set_input_value('계좌번호', input0)
        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('시작일자', date_from)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
