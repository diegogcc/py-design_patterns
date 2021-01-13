from .abs_cust import AbsCust

class NullCust(AbsCust):
    def __init__(self, cust_type):
        self.cust_type = cust_type

    def send_invoice(self):
        print('Customer type %s not found' % self.cust_type)