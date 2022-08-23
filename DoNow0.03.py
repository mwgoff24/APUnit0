'''
###############
# Do Now 0.03 #
###############

In your Console
---------------
Type the following:

class Time(object):
  def __init__(self, hour, minute, second):
    self.hour = hour
    self.minute = minute
    self.second = second

time1 = Time(5, 32, 0)
time2 = Time(23, 11, 11)

print(time1)
print(time2)

In your Notebook
----------------
Respond to the following:

1.  Based on what is output, how can you tell the difference between time1 and time2?
Where it is at in memory.

2.  What happens if you try to add time1 and time2?
An error pops up saying we can't add two time types.
'''

class Time(object):
  def __init__(self, hour, minute, second):
    self.hour = hour
    self.minute = minute
    self.second = second

  def __str__(self):
    return f"{self.hour}:{self.minute}:{self.second}"

  def __add__(self, other):
    new_time = Time(self.hour + other.hour, self.minute + other.minute, self.second + other.second)
    return new_time
    
time1 = Time(5, 32, 0)
time2 = Time(23, 11, 11)
time3 = Time(4, 25, 56)

print(time1)
print(time2)

print(time1 + time2 + time3)