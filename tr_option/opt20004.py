from tr_option.base import KWTR
from copy import deepcopy

# [ opt20004 : 업종틱차트조회요청 ]
class Opt20004(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt20004'

        self.record_name_single = '업종틱차트'
        self.header_single = [
            '업종코드',
        ]

        self.record_name_multiple = '업종틱차트조회'
        self.header_multiple = [
            '현재가', '거래량', '체결시간', '시가', '고가', '저가', '대업종구분', '소업종구분', '종목정보', '전일종가',
        ]


    def tr_opt(self, input0, tick_range, prev_next, screen_no):
        # 업종코드 = 001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고
        # 틱범위 = 1:1틱, 3:3틱, 5:5틱, 10:10틱, 30:30틱

        self.core.set_input_value('업종코드', input0)
        self.core.set_input_value('틱범위', tick_range)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
