class clockTime:

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def setHours(self, hours):
        self.hours = hours

    def setMinutes(self, minutes):
        self.minutes = minutes

    def setSeconds(self, seconds):
        self.seconds = seconds

    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def showTime(self):
        print(str(self.hours), ":", str(self.minutes), ":", str(self.seconds))


c = clockTime()

hours = input("Please enter the hour: ")
minutes = input("Please enter the minute: ")
seconds = input("Please enter the second: ")

c.setHours(hours)
c.setMinutes(minutes)
c.setSeconds(seconds)
c.setTime(hours, minutes, seconds)

print("The time is: ")
c.showTime()
