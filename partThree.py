def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    x = (d.replace("£", ""))
    return float(x)

def percent_to_float(p):
    y = (p.replace("%", ""))
    return float(y) / 100
    


main()
