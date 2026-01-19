import math  

def main():
    A = int(input ("Enter side A: "))  
    B = int(input ("Enter side B: "))
    pythag(A,B) 
    

def pythag(A,B):
    C1 = A**2
    C2 = B**2
    C3 = C1 + C2
    C = math.sqrt(C3)
    print(C)

main()
