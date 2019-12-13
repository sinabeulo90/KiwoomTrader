from tr_option.base import KWTR
from copy import deepcopy

# [ opt10077 : 당일실현손익상세요청 ]
class Opt10077(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10077'

        self.record_name_single = '당일실현손익'
        self.header_single = [
            '당일실현손익',
        ]

        self.record_name_multiple = '당일실현손익상세'
        self.header_multiple = [
            '종목명', '체결량', '매입단가', '체결가', '당일매도손익', '손익율', '당일매매수수료', '당일매매세금', '종목코드',
        ]


    def tr_opt(self, input0, input1, code, prev_next, screen_no):
        # 계좌번호 = 전문 조회할 보유계좌번호
        # 비밀번호 = 사용안함(공백)
        # 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value('계좌번호', input0)
        self.core.set_input_value('비밀번호', input1)
        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
