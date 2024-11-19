class Device:
    def __init__(self, heigth, width, name):
        self.height = heigth
        self.width = width
        self.name = name
    
    def power(self):
        print(self.name + " power is on")


class Computer(Device):
    def power(self):
        print(self.name + " power is off")

    def playVideo(self):
        print(self.name + "is playing a video")

    def playMusic(self):
        print(self.name + "is playing music")

