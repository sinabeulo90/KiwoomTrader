from tr_option.base import KWTR
from copy import deepcopy

# [ opt10033 : 신용비율상위요청 ]
class Opt10033(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10033'

        self.record_name_multiple = '신용비율상위'
        self.header_multiple = [
            '종목정보', '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '등락률', '신용비율', '매도잔량', '매수잔량', '현재거래량',
        ]


    def tr_opt(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 거래량구분 = 0:전체조회, 10:만주이상, 50:5만주이상, 100:10만주이상, 200:20만주이상, 300:30만주이상, 500:50만주이상, 1000:백만주이상
        # 종목조건 = 0:전체조회, 1:관리종목제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기
        # 상하한포함 = 0:상하한 미포함, 1:상하한포함
        # 신용조건 = 0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('거래량구분', input1)
        self.core.set_input_value('종목조건', input2)
        self.core.set_input_value('상하한포함', input3)
        self.core.set_input_value('신용조건', input4)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
