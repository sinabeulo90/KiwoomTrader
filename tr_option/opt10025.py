from tr_option.base import KWTR

# [ OPT10025 : 매물대집중요청 ]
class Opt10025(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10025'
        self.record_name = '거래량갱신'
        self.header = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '등락률', '현재거래량', '가격대시작', '가격대끝', '매물량', '매물비',
        ]


    def tr_opt(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 매물집중비율 = 0~100 입력
        # 현재가진입 = 0:현재가 매물대 집입 포함안함, 1:현재가 매물대 집입포함
        # 매물대수 = 숫자입력
        # 주기구분 = 50:50일, 100:100일, 150:150일, 200:200일, 250:250일, 300:300일

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('매물집중비율', input1)
        self.core.set_input_value('현재가진입', input2)
        self.core.set_input_value('매물대수', input3)
        self.core.set_input_value('주기구분', input4)
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
