class Balloon:
    def __init__ (self,Colour,DefenceItem):
        self.__Health = 100 #INTEGER
        self.__Colour = Colour #STRING
        self.__DefenceItem = DefenceItem #STRING

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self,DeltaHealth):
        self.__Health = self.__Health + DeltaHealth

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False

def Defend(MyBalloon,Strength):
    MyBalloon.ChangeHealth(Strength)
    print(MyBalloon.GetDefenceItem())
    if MyBalloon.CheckHealth():
        print("Balloon is popped")
    else:
        print("Balloon successfully defended")
    return MyBalloon


DefenceItem = input("Enter your Defence Item")
Colour = input("Enter your Colour")
Balloon1 = Balloon(DefenceItem,Colour)
Balloon1 = Defend(Balloon1,-50)

    