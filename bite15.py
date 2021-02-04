names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()

combine = list(zip(names, countries))

for i, item in enumerate(combine, start = 1):
    print(f"{i}. {item[0].ljust(10)} {item[1]}")