# Help message for a `help` command.
from json import loads;
from lib.output import os_output;

with (open("config/colors/colors.json")) as fl:
  colors = loads(fl.read());

def help_msg():
  os_output(colors, "This is a help message.\n\nCommands:\n  - help -- Show this help menu.\n  exit -- Exit the OS.");

