from tr_option.base import KWTR

# [ OPT10009 : 주식기관요청 ]
class Opt10009(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = "opt10009"
        self.record_name = '주식기관'
        self.header = [
            '날짜', '종가', '대비', '기관기간누적', '기관일변순매매', '외국인일변순매매', '외국인지분율',
        ]


    def tr_opt(self, code, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드

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
        ret = {
            'header' : self.header,
            'rows' : self.core.get_comm_data_ex(tr_code, rq_name)
        }

        return ret
