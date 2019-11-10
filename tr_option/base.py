from core import KWCore
from abc import abstractmethod

class KWTR(object):

    def __init__(self, core):
        assert(isinstance(core, KWCore))
        self.core = core

    @abstractmethod
    def tr_opt(self, code, prev_next, screen_no):
        pass

    @abstractmethod
    def tr_opt_data(self, tr_code, rq_name, index):
        pass

    @abstractmethod
    def tr_opt_data_ex(self, tr_code, rq_name, index):
        pass
