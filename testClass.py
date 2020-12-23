class TestT:
    def __init__(self, message="", flag=0, i1="", i2=""):
        """
        flag:
            0 = the system needs additional info
            1 = complete request
            -1 = input error
        :param message:
        :param flag:
        :param i1:
        :param i2:
        """
        self.message = message
        self.flag = flag
        self.i1 = i1
        self.i2 = i2

    def getInfo(self):
        return [self.message, self.flag, self.i1, self.i2]

    def setMessage(self, message):
        self.message = message

    def setFlag(self, flag):
        self.flag = flag

    def setI1(self, i1):
        self.i1 = i1

    def setI2(self, i2):
        self.i2 = i2


# testing
# chat = TestT()
# print(chat.getInfo())
# chat.setMessage('Hi')
# print(chat.getInfo())
