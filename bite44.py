import random
import string

def gen_key(parts = 4, chars_per_part = 8):
    key = ""
    for i in range(parts):
        key += ("".join(random.choices(string.ascii_uppercase + string.digits, k = chars_per_part))+"-")
    return key.rstrip("-")

k = gen_key()