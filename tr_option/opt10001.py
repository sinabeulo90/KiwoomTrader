from tr_option.base import KWTR

# [ opt10001 : 주식기본정보요청 ]
class Opt10001(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = "opt10001"
        self.record_name = '주식기본정보'
        self.header = [
            '종목코드', '종목명', '결산월', '액면가', '자본금', '상장주식', '신용비율',
            '연중최고', '연중최저', '시가총액', '시가총액비중', '외인소진률', '대용가',
            'PER', 'EPS', 'ROE', 'PBR', 'EV', 'BPS', '매출액', '영업이익', '당기순이익',
            '250최고', '250최저', '시가', '고가', '저가', '상한가', '하한가', '기준가',
            '예상체결가', '예상체결수량', '250최고가일', '250최고가대비율', '250최저가일', '250최저가대비율',
            '현재가', '대비기호', '전일대비', '등락율', '거래량', '거래대비', '액면가단위', '유통주식', '유통비율',
        ]


    def tr_opt(self, code, prev_next, screen_no):

        self.core.set_input_value("종목코드", code)
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
        pass