while True:
    a = input('gi meg et tall\n')
    passed = False
    while(not passed):
        try:
            a = float(a)
            passed = True
        except ValueError:
            a = input('Gi meg et TALL takk\n')
    b = input('gi meg enda ett tall\n')
    
    passed = False
    while(not passed):
        try:
            b = float(b)
            passed = True
        except ValueError:
            b = input('Gi meg et TALL takk\n')
    op = input('+, - eller * ?\n')
    while op not in ('+', '-', '*'):
        op = input('+, - eller * TAKK\n')
    if(op == '+'): print(a+b)
    if(op == '-'): print(a-b)
    if(op == '*'): print(a*b)
