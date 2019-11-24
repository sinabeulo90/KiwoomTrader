from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10010 : 업종프로그램요청 ]
class Opt10010(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10010'

        self.record_name_multiple = '업종프로그램'
        self.header_multiple = [
            '차익위탁매도수량', '차익위탁매도금액', '차익위탁매수수량', '차익위탁매수금액', '차익위탁순매수수량', '차익위탁순매수금액',
            '비차익위탁매도수량', '비차익위탁매도금액', '비차익위탁매수수량', '비차익위탁매수금액', '비차익위탁순매수수량', '비차익위탁순매수금액',
            '전체차익위탁매도수량', '전체차익위탁매도금액', '전체차익위탁매수수량', '전체차익위탁매수금액', '전체차익위탁순매수수량', '전체차익위탁순매수금액',
        ]


    def tr_opt(self, code, prev_next, screen_no):
        # 종목코드 = 000:전체, 001:코스피, 101:코스닥

        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
