from .abs_cust import AbsCust

class EntCust(AbsCust):

    def send_invoice(self):
        print('Sending invoice for %s customer' % self.name)