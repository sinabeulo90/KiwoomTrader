from tr_option.base import KWTR
from copy import deepcopy

# [ opt10045 : 종목별기관매매추이요청 ]
class Opt10045(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10045'

        self.record_name_single = '기관추정평균가'
        self.header_single = [
            '기관추정평균가', '외인추정평균가',
        ]

        self.record_name_multiple = '종목별기관매매추이'
        self.header_multiple = [
            '일자', '종가', '대비기호', '전일대비', '등락율', '거래량', '기관기간누적', '기관일별순매매수량', '외인기간누적', '외인일별순매매수량', '한도소진율',
        ]


    def tr_opt(self, code, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 종료일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 기관추정단가구분 = 1:매수단가, 2:매도단가
        # 외인추정단가구분 = 1:매수단가, 2:매도단가
        # 누적기간 = 사용안함
        # 기간구분 = 사용안함

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('시작일자', input1)
        self.core.set_input_value('종료일자', input2)
        self.core.set_input_value('기관추정단가구분', input3)
        self.core.set_input_value('외인추정단가구분', input4)
        self.core.set_input_value('누적기간', input5)
        self.core.set_input_value('기간구분', input6)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
