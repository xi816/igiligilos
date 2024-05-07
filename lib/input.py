# IgiligilOS input system.

def os_input(colors: dict, input_text: str):
  com = input(f"\x1B[{colors['bg-color']}m\x1B[{colors['fg-color']}m{input_text}\x1B[J");
  print("\x1B[0m", end="");
  return com;

