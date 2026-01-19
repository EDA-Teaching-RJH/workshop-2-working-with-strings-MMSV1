import math  

def main():
    A = int(input ("Enter side A: "))  
    B = int(input ("Enter side B: "))
    pythag(A,B) 
    

def pythag(A,B):
    C = math.hypot(A,B)
    print(C)

main()
