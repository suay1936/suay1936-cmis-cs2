def countup(n):
    if n >= 10:
        print "Blast off"
    else:
        print n
        countup(n + 1)

def main():
    countup(0)

    return


main()
