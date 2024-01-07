def hello(name: str):
    return "Hello " + name

def raiseMe():
    try:
        raise KeyError
    except KeyError:
        print('Error')

class BasicThing:
    TYPE = 'Basic'

class MyBasic(BasicThing):

    def __init__(self) -> None:
        super().__init__()
        self.name = 'MyBasic'

    def whatIsYourType(self):
        print(self.TYPE , ':' , self.name)

basic = MyBasic()

basic.whatIsYourType()