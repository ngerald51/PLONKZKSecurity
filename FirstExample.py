# Defining main function
def main():
    
    
    I = [1, 2, 3, 4]
    LI = {1: 0, 2: 1, 3: 1, 4: 3}
    RI = {1:1,2:1,3:2,4:3}
    O = [LI[i] + RI.get(i, 0) for i in I[:3]]
    O.append(LI[4] * RI.get(4, 0))

    print("LI =", LI)
    print("RI =", RI)
    print("O =", O)




# Using the special variable 
# __name__
if __name__=="__main__":
    main()
