from tr_option.base import KWTR
from copy import deepcopy

# [ opt10079 : 주식틱차트조회요청 ]
class Opt10079(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10079'

        self.record_name_single = '주식틱차트'
        self.header_single = [
            '종목코드', '마지막틱갯수',
        ]

        self.record_name_multiple = '주식틱차트조회'
        self.header_multiple = [
            '현재가', '거래량', '체결시간', '시가', '고가', '저가', '수정주가구분', '수정비율', '대업종구분', '소업종구분', '종목정보', '수정주가이벤트', '전일종가',
        ]


    def tr_opt(self, code, input1, input2, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 틱범위 = 1:1틱, 3:3틱, 5:5틱, 10:10틱, 30:30틱
        # 수정주가구분 = 0 or 1, 수신데이터 1:유상증자, 2:무상증자, 4:배당락, 8:액면분할, 16:액면병합, 32:기업합병, 64:감자, 256:권리락

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('시작일자', input1)
        self.core.set_input_value('종료일자', input2)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
