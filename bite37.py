def countdown_recursive(start=10):
    print(start)
    if start < 1:
        print('time is up')
    else:
        countdown_recursive(start-1)

countdown_recursive(10)