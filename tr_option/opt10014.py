from tr_option.base import KWTR

# [ opt10014 : 공매도추이요청 ]
class Opt10014(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10014'
        self.record_name = '공매도추이'
        self.header = [
            '일자', '종가', '전일대비기호', '전일대비', '등락율', '거래량', '공매도량', '매매비중', '공매도거래대금', '공매도평균가', 
        ]


    def tr_opt(self, code, date_type, date_from, date_to, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
	    # 시간구분 = 0:시작일, 1:기간 => 0: 연속 조회, 1: 구간조회
	    # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
	    # 종료일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('시간구분', date_type)
        self.core.set_input_value('시작일자', date_from)
        self.core.set_input_value('종료일자', date_to)
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
