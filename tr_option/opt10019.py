from tr_option.base import KWTR
from copy import deepcopy

# [ opt10019 : 가격급등락요청 ]
class Opt10019(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10019'

        self.record_name_multiple = '가격급등락'
        self.header_multiple = [
            '종목코드', '종목분류', '종목명', '전일대비기호', '전일대비', '등락률', '기준가', '현재가', '기준대비', '거래량', '급등률',
        ]


    def tr_opt(self, market_type, input1, date_type, date, input4, input5, input6, input7, input8, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥, 201:코스피200
        # 등락구분 = 1:급등, 2:급락
        # 시간구분 = 1:분전, 2:일전
        # 시간 = 분 혹은 일입력
        # 거래량구분 = 00000:전체조회, 00010:만주이상, 00050:5만주이상, 00100:10만주이상, 00150:15만주이상, 00200:20만주이상, 00300:30만주이상, 00500:50만주이상, 01000:백만주이상
        # 종목조건 = 0:전체조회,1:관리종목제외, 3:우선주제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기
        # 신용조건 = 0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체
        # 가격조건 = 0:전체조회, 1:1천원미만, 2:1천원~2천원, 3:2천원~3천원, 4:5천원~1만원, 5:1만원이상, 8:1천원이상
        # 상하한포함 = 0:미포함, 1:포함

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('등락구분', input1)
        self.core.set_input_value('시간구분', date_type)
        self.core.set_input_value('시간', date)
        self.core.set_input_value('거래량구분', input4)
        self.core.set_input_value('종목조건', input5)
        self.core.set_input_value('신용조건', input6)
        self.core.set_input_value('가격조건', input7)
        self.core.set_input_value('상하한포함', input8)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
