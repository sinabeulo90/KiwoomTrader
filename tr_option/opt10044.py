from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10044 : 일별기관매매종목요청 ]
class Opt10044(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10044'

        self.record_name_multiple = '일별기관매매종목'
        self.header_multiple = [
            '종목코드', '종목명', '순매수수량', '순매수금액', '추정평균가', '현재가', '평균가대비', '대비율',
        ]


    def tr_opt(self, input0, input1, input2, input3, prev_next, screen_no):
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 종료일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 매매구분 = 0:전체, 1:순매도, 2:순매수
        # 시장구분 = 001:코스피, 101:코스닥

        self.core.set_input_value('시작일자', input0)
        self.core.set_input_value('종료일자', input1)
        self.core.set_input_value('매매구분', input2)
        self.core.set_input_value('시장구분', input3)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
