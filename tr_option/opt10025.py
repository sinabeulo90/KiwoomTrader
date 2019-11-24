from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10025 : 매물대집중요청 ]
class Opt10025(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10025'

        self.record_name_multiple = '매물대집중'
        self.header_multiple = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '등락률', '현재거래량', '가격대시작', '가격대끝', '매물량', '매물비',
        ]


    def tr_opt(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 매물집중비율 = 0~100 입력
        # 현재가진입 = 0:현재가 매물대 집입 포함안함, 1:현재가 매물대 집입포함
        # 매물대수 = 숫자입력
        # 주기구분 = 50:50일, 100:100일, 150:150일, 200:200일, 250:250일, 300:300일

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('매물집중비율', input1)
        self.core.set_input_value('현재가진입', input2)
        self.core.set_input_value('매물대수', input3)
        self.core.set_input_value('주기구분', input4)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
