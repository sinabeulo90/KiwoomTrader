from tr_option.base import KWTR

class Opt10001(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.header = [
            '종목코드', '종목명', '결산월', '액면가', '자본금', '상장주식', '신용비율',
            '연중최고', '연중최저', '시가총액', '시가총액비중', '외인소진률', '대용가',
            'PER', 'EPS', 'ROE', 'PBR', 'EV', 'BPS', '매출액', '영업이익', '당기순이익',
            '250최고', '250최저', '시가', '고가', '저가', '상한가', '하한가', '기준가',
            '예상체결가', '예상체결수량', '250최고가일', '250최고가대비율', '250최저가일', '250최저가대비율',
            '현재가', '대비기호', '전일대비', '등락율', '거래량', '거래대비', '액면가단위', '유통주식', '유통비율'
        ]


    def tr_opt(self, code, prev_next, screen_no):
        rq_name = tr_code = "opt10001"

        self.core.set_input_value("종목코드", code)
        self.core.comm_rq_data(rq_name, tr_code, prev_next, screen_no)

        return self.core.receive_tr_data_handler


    def tr_opt_data(self, tr_code, rq_name, index):
        ret = {
            'header' : self.header,
            'rows' : [[
                self.core.get_comm_data(tr_code, rq_name, index, '종목코드'),
                self.core.get_comm_data(tr_code, rq_name, index, '종목명'),
                self.core.get_comm_data(tr_code, rq_name, index, '결산월'),
                self.core.get_comm_data(tr_code, rq_name, index, '액면가'),
                self.core.get_comm_data(tr_code, rq_name, index, '자본금'),
                self.core.get_comm_data(tr_code, rq_name, index, '상장주식'),
                self.core.get_comm_data(tr_code, rq_name, index, '신용비율'),
                self.core.get_comm_data(tr_code, rq_name, index, '연중최고'),
                self.core.get_comm_data(tr_code, rq_name, index, '연중최저'),
                self.core.get_comm_data(tr_code, rq_name, index, '시가총액'),
                self.core.get_comm_data(tr_code, rq_name, index, '시가총액비중'),
                self.core.get_comm_data(tr_code, rq_name, index, '외인소진률'),
                self.core.get_comm_data(tr_code, rq_name, index, '대용가'),
                self.core.get_comm_data(tr_code, rq_name, index, 'PER'),
                self.core.get_comm_data(tr_code, rq_name, index, 'EPS'),
                self.core.get_comm_data(tr_code, rq_name, index, 'ROE'),
                self.core.get_comm_data(tr_code, rq_name, index, 'PBR'),
                self.core.get_comm_data(tr_code, rq_name, index, 'EV'),
                self.core.get_comm_data(tr_code, rq_name, index, 'BPS'),
                self.core.get_comm_data(tr_code, rq_name, index, '매출액'),
                self.core.get_comm_data(tr_code, rq_name, index, '영업이익'),
                self.core.get_comm_data(tr_code, rq_name, index, '당기순이익'),
                self.core.get_comm_data(tr_code, rq_name, index, '250최고'),
                self.core.get_comm_data(tr_code, rq_name, index, '250최저'),
                self.core.get_comm_data(tr_code, rq_name, index, '시가'),
                self.core.get_comm_data(tr_code, rq_name, index, '고가'),
                self.core.get_comm_data(tr_code, rq_name, index, '저가'),
                self.core.get_comm_data(tr_code, rq_name, index, '상한가'),
                self.core.get_comm_data(tr_code, rq_name, index, '하한가'),
                self.core.get_comm_data(tr_code, rq_name, index, '기준가'),
                self.core.get_comm_data(tr_code, rq_name, index, '예상체결가'),
                self.core.get_comm_data(tr_code, rq_name, index, '예상체결수량'),
                self.core.get_comm_data(tr_code, rq_name, index, '250최고가일'),
                self.core.get_comm_data(tr_code, rq_name, index, '250최고가대비율'),
                self.core.get_comm_data(tr_code, rq_name, index, '250최저가일'),
                self.core.get_comm_data(tr_code, rq_name, index, '250최저가대비율'),
                self.core.get_comm_data(tr_code, rq_name, index, '현재가'),
                self.core.get_comm_data(tr_code, rq_name, index, '대비기호'),
                self.core.get_comm_data(tr_code, rq_name, index, '전일대비'),
                self.core.get_comm_data(tr_code, rq_name, index, '등락율'),
                self.core.get_comm_data(tr_code, rq_name, index, '거래량'),
                self.core.get_comm_data(tr_code, rq_name, index, '거래대비'),
                self.core.get_comm_data(tr_code, rq_name, index, '액면가단위'),
                self.core.get_comm_data(tr_code, rq_name, index, '유통주식'),
                self.core.get_comm_data(tr_code, rq_name, index, '유통비율')
            ]]
        }

        return ret


    def tr_opt_data_ex(self, tr_code, rq_name):
        pass
