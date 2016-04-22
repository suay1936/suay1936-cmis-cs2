def countup(n):
    if n >= 10:
        print "Blast off"
    else:
        print n
        countup(n + 1)

def main():
    countup(0)
    countup(1)
    countup(-20)

    return


main()


