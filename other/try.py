import random
p = lambda:random.choice('7♪♫♣♠♦♥◄☼☽')
[print('|'.join([p(),p(),p()]),end='\r') for i in range(8 ** 5)]