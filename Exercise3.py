import numpy as np


p = 218882428718392752222464057452572775088548364400416032436982041865

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
    


def interpolate(I, Y):
    n = len(I)
    f = np.poly1d([0])
    for i in range(n):
        term = np.poly1d([Y[i]])
        for j in range(n):
            if i != j:
                term = np.polymul(term, np.poly1d([1, -I[j]])) / (I[i] - I[j])
        f = np.polyadd(f, term)
    return f

# Define the points and data for LI, RI, O
I = np.array([1, 2, 3, 4], dtype=int)
LI_values = np.array([0, 1, 1, 3], dtype=int)
RI_values = np.array([1, 1, 2, 3], dtype=int)
O_values = np.array([1, 2, 3, 9], dtype=int)  # Assuming O(4) = 9 for the sake of example

# Interpolate LI, RI, O
qL = interpolate(I, LI_values)
qR = interpolate(I, RI_values)
qO = interpolate(I, O_values)

# Define SL, SR, SM
SL = {i: (i-1) % p for i in I}
SR = {i: (i+1) % p for i in I}
SM = {i: (i*i) % p for i in I}

# Interpolate SL, SR, SM
qSL = interpolate(list(SL.values()), list(SL.keys()))
qSR = interpolate(list(SR.values()), list(SR.keys()))
qSM = interpolate(list(SM.values()), list(SM.keys()))

# Print the results
print("=================")
print("qL =", qL)
print("qR =", qR)
print("qO =", qO)
print("qSL =", qSL)
print("qSR =", qSR)
print("qSM =", qSM)
print("=====================")

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
