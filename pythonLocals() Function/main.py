def localsPython():
    Python = True
    print(Python)
    locals()['python'] = False;
    print(Python)

localsPython()