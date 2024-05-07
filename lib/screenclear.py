from json import loads;
from lib.output import os_output;

with (open("config/colors/colors.json")) as fl:
  colors = loads(fl.read());

os_output(colors, "\n"*100);

