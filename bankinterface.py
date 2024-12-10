class Bank:
    bname='swis'
    roi=0.01
    def __init__(self,name,phone,gender,adhar,pan,bal,pin):
        self.name=name
        self.phone=phone
        self.gender=gender
        self.adhar=adhar
        self.pan=pan
        self.bal=bal
        self.pin=pin
    @staticmethod
    def checkpin():
        passcode=int(input('enter the 4-digit pincode:'))
        return passcode
    def checkbal(self):
        count=0
        print('you have 3 attempt')
        while count<3:
            if self.checkpin()==self.pin:
                print(f'The Avilable Balance is {self.bal}')
                break
            else:
                print('incorrect password')
                print('try again!!')
                print(f'you have left {2-count}')
                count+=1
        else:
            print('Try from first')
    def withdrawal(self):
        count=0
        print('You Have 3 attempt')
        while count<3:
            amount=int(input('enter the amount to withdrwal'))
            if amount<=20000 and self.bal>amount:
                self.bal-=amount
                print('amount withdrwal successful')
                break
            else:
                print('incorrect password')
                print('try again!!')
                print(f'you have left {2-count}')
                count+=1
        else:
            print('Try After sometime')
    def deposite(self):
        count=0
        print('You Have 3 attempt')
        while count<3:
            amount=int(input('enter the amount to withdrwal'))
            if amount<=20000:
                self.bal+=amount
                print('amount withdrwal successful')
                break
            else:
                print('incorrect password')
                print('try again!!')
                print(f'you have left {2-count}')
                count+=1
        else:
            print('Try After sometime')
    @classmethod
    def changename(cls):
        cls.bname='PNG'
obj1=Bank('sujit',6372734447,'male',5412365412,789654123,50000,2001)
obj2=Bank('kiran',6372738754,'female',5412365852,789654784,40000,1999)
obj1.changename()
obj1.checkbal()