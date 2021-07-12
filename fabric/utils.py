import random


def create_unique_number():
      return random.randint(100000000000, 999999999999)


def create_six_digits_unique_number():
      return random.randint(100000, 999999)


def unique_code_generator(instance):
    not_unique = True
    while not_unique:
        code = create_unique_number()
        Klass = instance.__class__
        qs_exists = Klass.objects.filter(code=code).exists()
        if not qs_exists:
            not_unique = False
    return str(code)