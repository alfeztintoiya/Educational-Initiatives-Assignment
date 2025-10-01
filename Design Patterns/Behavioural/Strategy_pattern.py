class PaymentStrategy:
    def pay(self,amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self,amount):
        print(f"Paid {amount} using Credit Card")
    
class GPayPayment(PaymentStrategy):
    def pay(self,amount):
        print(f"Paid {amount} using Google Pay")

class UpiPayment(PaymentStrategy):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")
    
class PaymentProcessor:
    def __init__(self,strategy: PaymentStrategy):
        self.strategy = strategy
    
    def process_payment(self,amount):
        self.strategy.pay(amount)

processor = PaymentProcessor(GPayPayment())
processor.process_payment(1000)
processor.strategy = UpiPayment()
processor.process_payment(1500)