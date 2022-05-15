with open('sample.txt', 'a') as table:
    for item in range(2, 13):
        for item2 in range(1, 13):
            print("{1:>2} times {0} is {2}".format(item, item2, item * item2), file=table)
        print("-" * 20, file=table)
