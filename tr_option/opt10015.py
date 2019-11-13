from tr_option.base import KWTR

# [ opt10015 : 일별거래상세요청 ]
class Opt10015(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10015'
        self.record_name = '일별거래상세'
        self.header = [
            '일자', '종가', '전일대비기호', '전일대비', '등락율', '거래량', '거래대금',
            '장전거래량', '장전거래비중', '장중거래량', '장중거래비중', '장후거래량', '장후거래비중', '합계3',
            '기간중거래량', '체결강도', '외인보유', '외인비중', '외인순매수', '기관순매수', '개인순매수', '외국계', '신용잔고율', '프로그램',
            '장전거래대금', '장전거래대금비중', '장중거래대금', '장중거래대금비중', '장후거래대금', '장후거래대금비중',
        ]


    def tr_opt(self, code, date, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('일자', date)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        return self.core.receive_tr_data_handler


    def tr_opt_data(self, tr_code, rq_name, index):
        ret = {
            'header' : self.header,
            'rows' : [
                [ self.core.get_comm_data(tr_code, rq_name, index, column) for column in self.header ]
            ]
        }

        return ret


    def tr_opt_data_ex(self, tr_code, rq_name):
        ret = {
            'header' : self.header,
            'rows' : self.core.get_comm_data_ex(tr_code, rq_name)
        }

        return ret
