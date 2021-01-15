import ascii_magic
output = ascii_magic.from_image_file("fun.jpeg",columns=80,char="$*")
ascii_magic.Modes.ascii(output)