from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10071 : 시간대별전일비거래비중요청 ]
class Opt10071(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10071'

        self.record_name_multiple = '시간대별전일비거래비중'
        self.header_multiple = [
            '시간', '현재가', '대비기호', '전일대비', '대비율', '체결거래량', '누적거래량', '순간비율', '누적비율',
        ]


    def tr_opt(self, code, date_type, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 시간구분 = 1:1분,3:3분,5:5분,10:10분,15:15분,30:30분,60:60분

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('시간구분', date_type)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
