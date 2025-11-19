
def toCelsius(temp, u):
    match u:
        case "C":
            return temp
        case "F":
            return (temp-32) * 5/9
        case "K":
            return (temp - 273.15)

def toKelvin(temp, u):
    match u:
        case "C":
            return temp + 273

        case "F": 
            return 5/9*(temp -32)+273.15

        case "K":
            return temp
    
def toFarenheit(temp, u):
    match u:
        case "C":
            return temp * 9/5 +32 

        case "F":
            return temp

        case "K":
            return 9/5 * (temp - 273.15) + 32
    

def main():
    print(toCelsius(285, "F"))


if __name__ == "__main__":
    main()