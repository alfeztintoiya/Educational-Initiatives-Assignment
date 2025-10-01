class OldPaymentSystem:
    def make_payment(self,amount):
        print(f"Paid {amount} via old system")

class PaymentAdapter:
    def __init__(self,old_payment_system):
        self.old_payment_system = old_payment_system
    
    def pay(self,amount):
        self.old_payment_system.make_payment(amount)

old_system = OldPaymentSystem()
adapter = PaymentAdapter(old_system)
adapter.pay(2100)