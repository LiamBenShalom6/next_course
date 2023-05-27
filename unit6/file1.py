class GreetingCard:

    def __init__(self, recipient, sender):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print("The recipient is: %s, the sender is: %s" % (self._recipient, self._sender))