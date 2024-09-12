# used own repository since link given in test is for COMSC140 instead of COMSC240
def main():
    number = int(input("Enter a number: "))
    pnumber = number + 1
    primeFound = False
    
    while(not primeFound):
        primeFound = True
        for n in range(2, pnumber):
            if pnumber % n == 0: # checks if input value is divisable by n, not prime
                pnumber += 1
                primeFound = False
                break
        
    
    print(pnumber)
    return pnumber
##


if __name__ == '__main__':
    main()
