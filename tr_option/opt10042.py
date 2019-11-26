from tr_option.base import KWTR
from copy import deepcopy

# [ opt10042 : 순매수거래원순위요청 ]
class Opt10042(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10042'

        self.record_name_multiple = '순매수거래원순위'
        self.header_multiple = [
            '순위', '회원사코드', '회원사명',
        ]


    def tr_opt(self, code, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 종료일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 조회기간구분 = 0:기간으로 조회, 1:시작일자, 종료일자로 조회
        # 시점구분 = 0:당일, 1:전일
        # 기간 = 5:5일, 10:10일, 20:20일, 40:40일, 60:60일, 120:120일
        # 정렬기준 = 1:종가순, 2:날짜순

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('시작일자', input1)
        self.core.set_input_value('종료일자', input2)
        self.core.set_input_value('조회기간구분', input3)
        self.core.set_input_value('시점구분', input4)
        self.core.set_input_value('기간', input5)
        self.core.set_input_value('정렬기준', input6)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
