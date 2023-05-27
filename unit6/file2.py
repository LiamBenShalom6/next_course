import file1

class BirthdayCard(file1.GreetingCard):

    def __init__(self, recipient, sender, sender_age):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        print("Happy birthday %d" %(self._sender_age))
        super().greeting_msg()