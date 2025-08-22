


# Defining main function
def main():
    
        
    I = [1, 2, 3, 4]
    LI = {1: 0, 2: 1, 3: 1, 4: 3}
    
    # Define RI based on Constraint 1 and other constraints
    RI = {1: 1, 2: 1, 3: 2, 4: 3}
    
    # Initialize O with the same length as I
    O = [0] * len(I)
    
    # Constraint 2: Calculate O for i != 4
    for i in I:
        if i != 4:
            O[i-1] = LI[i] + RI[i]
    
    # Constraint 4: LI(4) = RI(4) = O(3)
    O[2] = LI[4] = RI[4] = 3
    
    # Constraint 5: LI(4) * RI(4) = O(4)
    O[3] = LI[4] * RI[4]  # O[3] corresponds to the 4th element
    
    # Print the results to verify
    print("LI =", LI)
    print("RI =", RI)
    print("O =", O)
    
      # Constraints
    assert LI[1] == 0 and RI[1] == 1  # Constraint 1
    
    for i in I:
        if i != 4:
            assert LI[i] + RI[i] == O[i-1]  # Constraint 2
    
    for i in I:
        if i !=4 and i!=3:
            assert LI[i+1] == RI[i] and RI[i+1] == O[i-1]  # Constraint 3
    
    assert LI[4] == RI[4] == O[2]  # Constraint 4
    
    assert LI[4] * RI[4] == O[3]  # Constraint 5
    
    print("All constraints are satisfied.")
    



# Using the special variable 
# __name__
if __name__=="__main__":
    main()
