def mul(x, y):
    z = x * y
    return z

def sentence(food, x, y, z):
    return """
I have a, {}. 
Did you know:
{} + {} = {}
""".format(food, x, y, z)

def main():
    food = raw_input("What's your favorite food?: ")
    x = raw_input("Type in a number: ")
    y = raw_input("Type in a new number: ")
    z = mul(int(x), int(y))
    print sentence(food, x, y, z)

main()
