# Igiligilo output system.

def os_output(colors: dict, output_text: str):
  print(f"\x1B[{colors['bg-color']}m\x1B[{colors['fg-color']}m{output_text}\x1B[B\r\x1B[0m");

