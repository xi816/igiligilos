import sys;
import time;

class Clock:
  def __init__(self, tm, tmzone):
    self.tm = tm;
    self.tmzone = tmzone;

  def calculateHeximalTime(self):
    secs = round(self.tm % 60);
    mins = round(self.tm % 3600 // 60);
    hrs = round((self.tm % 86400 // 3600 + self.tmzone) % 24);
    return hrs, mins, secs, "", "";

  def calculateDecimalTime(self):
    secs = round(self.tm % 100);
    mins = round(self.tm % 10000 // 100);
    hrs = round(self.tm % 1000000 // 10000);
    days = round(self.tm % 10000000 // 1000000);
    mths = round(self.tm % 100000000 // 10000000);
    return hrs, mins, secs, mths, days;

def clock():
  e_824083 = 3; # Timezone GMT+3
  e_902835 = time.time();
  e_490237 = Clock(e_902835, e_824083);
  e_923171 = e_490237.calculateHeximalTime();

  a = f"{e_923171[3]:0>2}.{e_923171[4]:0>2}";
  b = f"{e_923171[0]:0>2}:{e_923171[1]:0>2}:{e_923171[2]:0>2}";
  return b, a;

def clockDec():
  e_902835 = time.time();
  e_490237 = Clock(e_902835, 0);
  e_923171 = e_490237.calculateDecimalTime();

  a = f"{e_923171[3]:0>2}.{e_923171[4]:0>2}";
  b = f"{e_923171[0]:0>2}:{e_923171[1]:0>2}:{e_923171[2]:0>2}";
  return b, a;

