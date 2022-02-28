class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Creates a "MyTime" object initialization. """
        self.hours   = (((secs//60) + mins) // 60) + hrs 
        self.minutes = ((secs//60) + mins) % 60
        self.seconds = secs % 60

    def __str__(self):
        """ Print the time object in a readibly format. """
        hrs, mins, secs = self.hours, self.minutes, self.seconds
        if len(str(self.seconds)) < 2: secs = f'0{self.seconds}'
        if len(str(self.minutes)) < 2: mins = f'0{self.minutes}'
        if len(str(self.hours)) < 2: hrs = f'0{self.hours}'

        return f'{hrs}:{mins}:{secs}'
    
    def __add__(self, other):
        return MyTime.secs_to_time(self.total_secs() + other.total_secs())
    
    def __sub__(self, other): 
        return MyTime.secs_to_time(self.total_secs() - other.total_secs())
    
    def __gt__(self, other):
        """ Returns True is the invoking object occurred after the given one. """
        return self.total_secs() > other.total_secs()
    
    def __lt__(self, other):
        """ Returns True is the invoking object occurred before the given one. """
        return self.total_secs() < other.total_secs()
     
    def __eq__(self, other):
        """ Returns True if the invoking oject's value is equal to given object's value. """
        return self.total_secs() == other.total_secs()

    def increment(self, seconds):
        """ Increments time object by the given seconds. """ 
        temp_time = MyTime.secs_to_time(self.total_secs() + seconds)
        self.hours = temp_time.hours
        self.minutes = temp_time.minutes
        self.seconds = temp_time.seconds
    
    def total_secs(self):
        """ Returns the total seconds of a given time object. """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def secs_to_time(seconds):
        return MyTime(0, 0, seconds)
    
    def between(self, time0, time1):
        """ Returns True if the invoking object is between the two given objects. """
        return time0.total_secs() <= self.total_secs() < time2.total_secs()


if __name__ == '__main__':
    timeNeg = MyTime(-2, -5, -6)
    time0 = MyTime(8, 30, 30)
    time1 = MyTime(10, 11, 10)
    time2 = MyTime.secs_to_time(time1.total_secs())
    print(timeNeg < time0)
    print(time1 == time2)
