n = int(input('Tabuada do numero: '))
for count in range(10):
    print('%d x %d = %d' % (n, count + 1, n*(count+1)))