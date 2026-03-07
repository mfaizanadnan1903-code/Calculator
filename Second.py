import math as m
import cmath as cm
import numpy as np
import First as f
from fractions import Fraction

def inch():
    p = (input("Enter 1 for again execution or enter any character to exit program:"))
    if(p=="1"):
        f.calculator()

def single_input_list_observations(n):
    l = [float(input(f"Enter {i+1} observation:")) for i in range(n)]     
    return l
    
def single_input_integer():
    n = int(input("Enter a number:"))
    return n

def single_input_float():
    n = float(input("Enter a number:")) 
    return n
    
def single_input_integer_obs():
    n = int(input("Enter the number of obs:"))
    return n    
    
def fibonacci():
    try:
        n = int(input("How much fibonacci series numbers you want to diaplay:"))
        if(n<0):
            print("You entered wrong number") 
            inch()
        a,b,c = 0,1,0
        for i in range(n):
            print(a)
            c = a+b
            a = b
            b = c          
    except ValueError:
         print("You entered wrong number") 
         inch()     

def matrix_operations_2():
    try:
        print("Square matrix is needed for options1,2,4,5,8.It means these operations need square matrix.It's rows and columns should be equal.\n")
        print("1.Determinant")
        print("2.Inverse of a matrix")
        print("3.Transpose of a matrix")
        print("4.Addition of matrix and transpose of it.")
        print("5.Subtraction of matrix and transpose of it.")
        print("6.Multiplication of matrix and transpose of it.")
        print("7.Multiplication of transpose and matrix of it.")
        print("8.Division of matrix and transpose of it.")
        print("9.All operations")
        c1 = int(input("Choice:"))
        m = int(input("Enter no. of rows:"))
        n = int(input("Enter no. of columns:"))
        l1 = np.array([float(input(f"Enter no{i+1}:")) for i in range(m*n)]).reshape(m,n)
        if c1==1:
            if m==n:
                print("Determinant:\n",np.linalg.det(l1))
            else:
                print("Determinant is not possible.")
        elif c1==2:
            if m==n:
                print("Inverse matrix:\n",np.linalg.inv(l1))
            else:
                print("Inverse matrix is not possible.")
        elif c1==3:
            print("Transpose:\n",l1.transpose())
        elif c1==4:
            if m==n:
                print("Result:\n",l1+(l1.transpose()))
            else:
                print("Result is not possible.")
        elif c1==5:
            if m==n:
                print("Result:\n",l1-(l1.transpose()))
            else:
                print("Result is not possible.")
        elif c1==6:
            print("Result:\n",np.dot(l1,(l1.transpose())))
        elif c1==7:
            print("Result:\n",np.dot((l1.transpose()),l1))
        elif c1==8:
            if m==n:
                print("Result:\n",l1/(l1.transpose()))
            else:
                print("Result is not possible.")
        elif c1==9:
            if m==n:
                print("Determinant:\n",np.linalg.det(l1))
                if(np.linalg.det(l1)!=0):
                    print("Inverse matrix:\n",np.linalg.inv(l1))
                else:
                    print("Option 2 (inverse of a matrix) is not possible.")
                print("Transpose:\n",l1.transpose())
                print("Addition:\n",l1+(l1.transpose()))
                print("Subtraction:\n",l1-(l1.transpose()))
                print("Multiply:\n",np.dot(l1,(l1.transpose())))
                print("Multiply:\n",np.dot((l1.transpose()),l1))
                print("Division:\n",l1/(l1.transpose()))
            else:
                print("Transpose:\n",l1.transpose())
                print("Multiply:\n",np.dot(l1,(l1.transpose())))
                print("Mutiply:\n",np.dot((l1.transpose()),l1))
        else:
            print("Invalid choice")
            inch()
                
    except ValueError:
        print("Error occured")
        inch()
                    
def matrix_operations():
    try:
        ops = int(input("Enter operation you want to conduct:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Dot multiplication\n5.Division\n6.Modulus\n7.All\nChoice:"))
        m = int(input("Enter no. of rows:"))
        n = int(input("Enter no. of columns:"))
        print("Matrix1")
        l1 = np.array([float(input(f"Enter no{i+1}:")) for i in range(m*n)]).reshape(m,n)
        print("Matrix2")
        l2  = np.array([float(input(f"Enter no{i+1}:")) for i in range(m*n)]).reshape(m,n)
        if ops==1:
            print("Addition:\n",l1+l2)
        elif ops==2:
            print("Subtraction:\n",l1-l2)
        elif ops==3:
            print("Multiplication:\n",l1*l2)
        elif ops==4:
            print("Dot multiply:\n",l1.dot(l2))
        elif ops==5:
            print("Division:\n",l1/l2)
        elif ops==6:
            print("Modulus:\n",l1%l2)
        elif ops==7:
            print("Addition:\n",l1+l2)
            print("Subtraction:\n",l1-l2)
            print("Multiplication:\n",l1*l2)
            print("Dot multiply:\n",l1.dot(l2))
            print("Division:\n",l1/l2)
            print("Modulus:\n",l1%l2)
        else:
            print("Invalid choice")
            inch()
    except ValueError:
        print("Error occured")   
        inch()         
               
def linear_equation_solver():
    try:
        num = int(input("Enter no. of system linear equations:"))
        print("No. of values to input:",num*(num+1))
        print("Enter values row-wise")
        rows = num
        columns = num+1
        l1 = []
        for i in range(rows*columns):
            l1.append(float(input(f"Enter no{i+1}:")))
        l2 = []
        for i in range(1,num+1):
                l2.append(l1[i*num])
                l1.pop(i*num)

        l1 = np.array(l1).reshape(rows,rows)
        l2 = np.array(l2)
        if(np.linalg.det(l1)==0):
            print("The equations are singular and no solution is possible.")
            inch()
        inv = np.linalg.inv(l1)
        ans = np.dot(inv,l2)
        for i in range(len(ans)):
            print(f"Answer {i+1} : {Fraction(ans[i]).limit_denominator(100)}")
    except ValueError:
        print("Error occured")
        inch()        
        
def prime(): 
    try:
        n = int(input("Enter a number to check whether the number is prime or not:"))    
        if(n<0):
             print("You entered wrong number") 
             inch()
        flag = 1
        for i in range(2,n):
            if(n%i==0):
                flag=0
        if(flag==1):
            print("Prime number")   
        else:
            print("Not a prime number")    
    except ValueError:
         print("You entered wrong number") 
         inch()       
            
def roots_of_quadratic():
    try:
        a = int(input("Enter first co-efficient:"))
        b = int(input("Enter second co-efficient:"))
        c = int(input("Enter third co-efficient:"))
        ans1 = (-b+((b*b)-4*a*c)**(1/2))/(2*a)
        ans2 = (-b-((b*b)-4*a*c)**(1/2))/(2*a)
        print(f"Root 1:{ans1}")
        print(f"Root 2:{ans2}")
    except:
        print("Error occured")
        inch()
  
def linear_equation_3():
    try:
        a1 = int(input("Enter a1:"))
        b1 = int(input("Enter b1:"))
        c1 = int(input("Enter c1:"))
        d1 = int(input("Enter d1:"))
        a2 = int(input("Enter a2:"))
        b2 = int(input("Enter b2:"))
        c2 = int(input("Enter c2:"))
        d2 = int(input("Enter d2:"))
        a3 = int(input("Enter a3:"))
        b3 = int(input("Enter b3:"))
        c3 = int(input("Enter c3:"))
        d3 = int(input("Enter d3:"))
        arr1 = np.array([[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]])
        arr2 = np.array([[d1],[d2],[d3]])
        arr4 = np.array([["x"],["y"],["z"]])
        print("AX = B")
        print("X = A**(-1) B")
        print(f"X:\n{arr4}\n")
        if(np.linalg.det(arr1)==0):
            print("The matrix is singular.So, it,s solution is not possible.")
            inch()
        arr1 = np.linalg.inv(arr1)
        arr3 = np.dot(arr1,arr2)
        x = Fraction(arr3[0][0]).limit_denominator(100)
        y = Fraction(arr3[1][0]).limit_denominator(100)
        z = Fraction(arr3[2][0]).limit_denominator(100)
        print(f"x={x} , y={y} , z={z}")
    except:
        print("Error occured")
        inch()  
        
def linear_equation_2():
    try:
        a1 = int(input("Enter a1:"))
        b1 = int(input("Enter b1:"))
        c1 = int(input("Enter c1:"))
        a2 = int(input("Enter a2:"))
        b2 = int(input("Enter b2:"))
        c2 = int(input("Enter c2:"))
        arr1 = np.array([[a1,b1],[a2,b2]])
        arr2 = np.array([[c1],[c2]])
        arr4 = np.array([["x"],["y"]])
        print("AX = B")
        print("X = A**(-1) B")
        print(f"X:\n{arr4}\n")
        if(np.linalg.det(arr1)==0):
            print("The matrix is singular.So, it,s solution is not possible.")
            inch()
        arr1 = np.linalg.inv(arr1)
        arr3 = np.dot(arr1,arr2)
        x = Fraction(arr3[0][0]).limit_denominator(100)
        y = Fraction(arr3[1][0]).limit_denominator(100)
        print(f"x={x} , y={y}")
    except:
        print("Error occured")
        inch()    
                                    
if __name__ == "__main__":
    inch()
    roots_of_quadratic()
    linear_equation_2()
    linear_equation_3()
    fibonacci()
    linear_equation_solver()
    prime()
    matrix_operations()
    matrix_operations_2()