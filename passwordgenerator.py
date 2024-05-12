import random

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET2 = 'ABCDEFGHIJKLMNOPQRTSUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '#*%&.?@$-+'

PASSWORD = ALPHABET + ALPHABET2 + NUMBERS + SYMBOLS

PASSWORD_GENERATOR = "".join(random.sample(PASSWORD, 8))

print("Password Created: " + PASSWORD_GENERATOR)

