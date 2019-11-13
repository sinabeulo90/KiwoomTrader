from tr_option.base import KWTR

# [ opt10013 : 신용매매동향요청 ]
class Opt10013(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = "opt10013"
        self.record_name = '신용매매동향'
        self.header = [
            '일자', '현재가', '전일대비기호', '전일대비기호거래량', '신규', '상환', '잔고', '금액', '대비', '공여율', '잔고율', 
        ]


    def tr_opt(self, code, date, type_flag, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 조회구분 = 1:융자, 2:대주

        self.core.set_input_value("종목코드", code)
        self.core.set_input_value("일자", date)
        self.core.set_input_value("조회구분", type_flag)
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
