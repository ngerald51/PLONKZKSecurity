
def main():
    y1 = 42
    y2 = 74102
    y3 = 987654321987654321
    
    Q = lambda x: x*x + x + 1
    Z = lambda x: x*x + 1
    Q1 = lambda x: x + 1
    Z1 = lambda x: (x + 1)**2
    Q2 = lambda x: x*x + x
    
    t_gamma1 = Q(y1) * Z(y1)
    f1_gamma2 = Q1(y2) * Z1(y2)
    f2_gamma3 = Q2(y3) * Z1(y3)
    
    print("t(γ1) =", t_gamma1)
    print("f1(γ2) =", f1_gamma2)
    print("f2(γ3) =", f2_gamma3)
    

if __name__=="__main__":
    main()
