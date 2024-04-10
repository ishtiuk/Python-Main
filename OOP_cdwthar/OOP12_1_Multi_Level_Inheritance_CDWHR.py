
class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    basketball = 8

    # def __init__(self):
    #     self.algo = 4
        
    def is_dance(self):
        self.algo = 4
        return f"I danced for {self.dance} times"


class Grand_son(Son):
    dance = 5

    def is_dance(self):
        return f"And I danced awosomely for {self.dance} times"


dadek = Dad() 
sonek = Son()
grandk = Grand_son()

print(grandk.is_dance())
