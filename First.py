import math as m
import statistics as d
import cmath as cm
import numpy as np
import Second as se         
import Third as th 
from fractions import Fraction

def calculator():
    print("\nThis is calculator.\nThis calculator is for test purpose and then we deploy it.")
    print("Enter the operations you want to conduct:")
    print("1.Arithmetic operations")
    print("2.Areas and volumes of shapes")
    print("3.Trignometric functions")
    print("4.Statistics")
    print("5.Other mathematical functions")
    print("6.Complex mathematical operation")
    print("7.Equation solving")
    print("8.Matrix operations")
    try:
        choice = int(input("Choice:"))
        if(choice==1):
            try:
                print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
                print("6.All")
                c1 = int(input("Choice:"))
                a = float(input("Enter first number:"))
                b = float(input("Enter second number:"))
                if(c1==1):
                    print(f"Addition:{a+b}")
                elif(c1==2):
                    print(f"Subtraction:{a-b}")
                elif(c1==3):
                    print(f"Multiplication:{a*b}")
                elif(c1==4):
                    print(f"Division:{a/b}")
                elif(c1==5):
                    print(f"Modulus:{a%b}") 
                elif(c1==6):
                    print(f"Addition:{a+b}")
                    print(f"Subtraction:{a-b}")
                    print(f"Multiplication:{a*b}")
                    print(f"Division:{a/b}")
                    print(f"Modulus:{a%b}")
                else:
                    print("Invalid choice")  
                    se.inch()
                se.inch()
                    
            except ValueError as e:
                print(f"Error:{e}")   
                se.inch()
            except ZeroDivisionError as e:
                print(f"Error:{e}") 
                se.inch()
            except:
                print("Error 404")
                se.inch()
                
        elif(choice==2):
            try:
                print("1.Area and perimeter of square\n2.Area and perimeter of rectangle")
                print("3.Area of parallelogram")  
                print("4.Area of rhombus")
                print("5.Area of triangle")
                print("6.Area of trapezium") 
                print("7.Volume of cube")
                print("8.Volume of cylinder") 
                print("9.Volume of sphere")
                print("10.Area and circumference of a circle") 
                c1 = int(input("Choice:"))
                if(c1==1):
                    n = float(input("Enter side:"))
                    print(f"Area:{n*n}\nPerimeter:{4*n}")
                elif(c1==2):
                    a = float(input("Enter length:")) 
                    b = float(input("Enter width:")) 
                    print(f"Area:{a*b}\nPerimeter:{2*(a+b)}")
                elif(c1==3):
                    a = float(input("Enter base:"))  
                    b = float(input("Enter height:"))
                    print(f"Area:{a*b}") 
                elif(c1==4):
                    a = float(input("Enter first diagonal:")) 
                    b = float(input("Enter second diagonal:")) 
                    print(f"Area:{(a*b)/2}")  
                elif(c1==5):
                    print("1.Two sides")
                    print("2.Three sides")
                    c2 = int(input("Choice:"))
                    if(c2==1):
                        a = float(input("Enter length:"))
                        b = float(input("Enter height:"))
                        print(f"Area:{(a*b)/2}")
                    elif(c2==2):
                        a = float(input("Enter first side:"))
                        b = float(input("Enter second side:")) 
                        c = float(input("Enter third side:"))
                        s = (a+b+c)/2
                        print(f"Area:{(s*(s-a)*(s-b)*(s-c))**(1/2)}")
                    else:
                        print("Invalid choice")
                        se.inch()
                elif(c1==6):
                    a = float(input("Enter first base:")) 
                    b = float(input("Enter second base:"))
                    c = float(input("Enter height:")) 
                    print(f"Area:{((a+b)*c)/2}")  
                elif(c1==7):
                    a = float(input("Enter radius:"))  
                    print(f"Volume:{a*a*a}")  
                elif(c1==8):
                    a = float(input("Enter radius:")) 
                    b = float(input("Enter height:"))
                    print(f"Area:{(22/7)*a*a*b}") 
                elif(c1==9):
                    a = float(input("Enter radius:"))
                    print(f"Area:{(3/4)*(22/7)*a*a*a}") 
                elif(c1==10):
                    a = float(input("Enter radius:")) 
                    print(f"Area:{(22/7)*a*a}\nCircumference:{2*(22/7)*a}") 
                else:
                    print("Invalid choice")  
                    se.inch()
                se.inch()
                    
            except ValueError as e:
                print(f"Error:{e}")   
                se.inch()
            except:
                print("Error 404")
                se.inch()
                
        elif(choice==3):
            try:
                print("1.Sine\n2.Cosine\n3.Tangent") 
                print("4.Arc sine\n5.Arc cosine\n6.Arc tangent")
                print("7.Hyperbolic sine\n8.Hyperbolic cosine")
                print("9.Hyperbolic tangent\n10.Hyperbolic arc sine")
                print("11.Hyperbolic arc cosine\n12.Hyperbolic arc tangent")  
                c1 = int(input("Choice:"))
                if(c1>=0 and c1<=12):
                    n = se.single_input_float()
                if(c1==1):
                    print(f"sine:{(m.sin(n))}")
                elif(c1==2):
                    print(f"Cosine:{(m.cos(n))}") 
                elif(c1==3):
                    print(f"Tangent:{(m.tan(n))}") 
                elif(c1==4):
                    print(f"Arc sine:{(m.asin(n))}")
                elif(c1==5):
                    print(f"Arc cosine:{(m.acos(n))}")
                elif(c1==6):
                    print(f"Arc tangent:{(m.atan(n))}")
                elif(c1==7):
                    print(f"Hyperbolic sine:{(m.sinh(n))}") 
                elif(c1==8):
                    print(f"Hyperbolic Cosine:{(m.cosh(n))}")
                elif(c1==9):
                    print(f"Hyperbolic Tangent:{(m.tanh(n))}")
                elif(c1==10):
                    print(f"Hyperbolic arc sine:{(m.asinh(n))}")
                elif(c1==11):
                    print(f"Hyperbolic arc cosine:{(m.acosh(n))}") 
                elif(c1==12):
                    print(f"Hyperbolic arc tangent:{(m.atanh(n))}") 
                else:
                    print("Invalid choice")
                    se.inch()
                se.inch()
                    
            except AttributeError as e:
                print(f"Error:{e}")       
                se.inch()                             
            except ValueError as e:
                print(f"Error:{e}")  
                se.inch()
            except:
                print("Error 404")
                se.inch()
                
        elif(choice==4):
            try:
                print("\nUngrouped data\n1.Mean")
                print("2.Median\n3.Mode\n4.Harmonic mean\n5.Geometric mean")
                print("6.Standard deviation\n7.Variance")
                print("8.Moment")
                print("9.Quartile,Decile,Percentile")
                print("10.Mean deviation")
                print("\nGrouped data\n11.Mean\n12.Standard deviation")
                print("13.Variance")
                print("14.Harmonic mean")
                print("15.Geometric mean")
                print("16.Median")
                print("17.Mode")
                print("18.Quartile,Decile,Percentile")
                print("19.Mean deviation")
                print("20.Moment")
                print("\nDiscrete data")
                print("21.Median\n22.Mode")
                print("23.Quartile")
                print("24.Decile")
                print("25.Percentile")
                print("\n26.All ungrouped")
                print("27.All grouped")
                c1 = int(input("Choice:"))
                if(c1 >= 1 and c1<=7):
                    n = se.single_input_integer_obs()
                    l = se.single_input_list_observations(n)
                    if(c1==1):
                        print(f"Mean:{d.mean(l)}") 
                    elif(c1==2):
                        print(f"Median:{d.median(l)}")
                    elif(c1==3):
                        print(f"Mode:{d.mode(l)}")
                    elif(c1==4):
                        print(f"Harmonic mean:{d.harmonic_mean(l)}") 
                    elif(c1==5):
                        print(f"Geometric mean:{d.geometric_mean(l)}")
                    elif(c1==6):
                        print(f"Standard deviation:{d.stdev(l)}") 
                    elif(c1==7):
                        print(f"Variance:{d.variance(l)}")    
                elif(c1==8):
                    th.moment_ungroup()
                elif(c1==9):
                    th.tiles_ungroup()
                elif(c1==10):
                    th.mean_deviation_ungroup()
                elif(c1>=11 and c1<=18):
                    if(c1==11):
                        print(f"Mean:{th.mean_grouped()}")
                    elif(c1==12):
                        print(f"Standard deviation:{(th.variance_grouped())**(1/2)}")
                    elif(c1==13):
                        print(f"Variance:{th.variance_grouped()}")
                    elif(c1==14):
                        print(f"Harmonic mean:{th.harmonic_mean_grouped()}")
                    elif(c1==15):
                        print(f"Geometric mean:{th.geometric_mean_grouped()}")
                    elif(c1==16):
                        print(f"Median:{th.median_grouped()}")
                    elif(c1==17):
                        print(f"Mode:{th.mode_grouped()}")
                    elif(c1==18):
                        th.tiles()
                elif(c1==19):
                    th.mean_deviation_group()
                elif(c1==20):
                    th.moment_group()
                elif(c1==21):
                    th.median_discrete()
                elif(c1==22):
                    th.mode_discrete()
                elif(c1==23):
                    th.quartile_discrete()
                elif(c1==24):
                    th.decile_discrete()
                elif(c1==25):
                    th.percentile_discrete()
                elif(c1==26):
                    th.all_ungroup()
                elif(c1==27):
                    th.all_grouped()
                else:
                    print("Invalid choice")  
                    se.inch()
                se.inch()
                    
            except AttributeError as e:
                print(f"Error:{e}")   
                se.inch()                 
            except ValueError as e:
                print(f"Error:{e}")
                se.inch()
            except:
                print("Error 404")
                se.inch()
            
                
        elif(choice==5):
            try:
                print("1.log with base e")
                print("2.log with base 10")
                print("3.log with base 2")
                print("4.Factorial\n5.Power\n6.Radians to degrees\n7.Degrees to radians")
                print("8.Square of a number") 
                print("9.Square root of a number")
                print("10.Permutations") 
                print("11.Combinations")
                print("12.Cube\n13.Cube root")
                print("14.Fibonacci number generator")
                print("15.Prime number cbecker")
                print("16.GCD (Greatest Common Divisor)")
                c1 = int(input("Choice:"))
                if(c1==1):
                    n = se.single_input_float()
                    print(f"log with base e:{m.log(n)}")
                elif(c1==2):
                    n = se.single_input_float()
                    print(f"log with base 10:{m.log10(n)}") 
                elif(c1==3):
                    n = se.single_input_float()
                    print(f"log with base 2:{m.log2(n)}")
                elif(c1==4):
                    n = int(input("Enter a positive number:"))
                    print(f"Factorial:{m.factorial(n)}") 
                elif(c1==5):
                    n = se.single_input_float()
                    p = int(input("Enter power:")) 
                    print(f"Answer:{n**p}")
                elif(c1==6):
                    n = float(input("Enter radians:"))
                    print(f"Degrees:{Fraction(m.degrees(n)).limit_denominator(10)}") 
                elif(c1==7):
                    n = float(input("Enter degrees:"))
                    print(f"Radians:{Fraction(m.radians(n)).limit_denominator(10)}")
                elif(c1==8):
                    n = se.single_input_float()
                    print(f"Square:{n*n}")
                elif(c1==9):
                    n = se.single_input_float()
                    print(f"Square root:{(n)**(1/2)}")
                elif(c1==10):
                    n = se.single_input_integer()
                    r = se.single_input_integer()
                    per = m.factorial(n)/m.factorial(n-r)
                    print(f"Permutations:{per}")
                elif(c1==11):
                    n = se.single_input_integer()
                    r = se.single_input_integer()
                    com = m.factorial(n)/(m.factorial(r)*m.factorial(n-r))
                    print(f"Combinations:{com}")
                elif(c1==12):
                    n = se.single_input_float()
                    print(f"Cube:{n**3}")
                elif(c1==13):
                    n = se.single_input_float()
                    print(f"Cube root:{n**(1/3)}")
                elif(c1==14):
                    se.fibonacci()
                elif(c1==15):
                    se.prime()
                elif(c1==16):
                    n1 = int(input("Enter first number:"))
                    n2 = int(input("Enter second number:"))
                    print(f"GCD:{m.gcd(n1,n2)}")
                else:
                    print(f"Invalid choice")
                    se.inch()
                se.inch()
                    
            except ValueError as e:
                print(f"Error:{e}")   
                se.inch()
            except:
                print("Error 404")     
                se.inch()
                
        elif(choice==6):
            try:
                print("1.Sine\n2.Cosine\n3.Tangent") 
                print("4.Arc sine\n5.Arc cosine\n6.Arc tangent")
                print("7.Hyperbolic sine\n8.Hyperbolic cosine")
                print("9.Hyperbolic tangent\n10.Hyperbolic arc sine")
                print("11.Hyperbolic arc cosine\n12.Hyperbolic arc tangent")  
                print("13.Addition\n14.Subtraction\n15.Multiplication\n16.Division")
                print("17.Square root")
                print("18.Mod")
                print("19.Inverse")
                c1 = int(input("Choice:"))
                print("Type the complex number in the form: a + bj")
                n = input("Enter a number:")
                n = complex(n)
                if(c1==1):
                    a = cm.sin(n)
                    print(f"sine:{a}")
                elif(c1==2):
                    a = cm.cos(n)
                    print(f"Cosine:{a}") 
                elif(c1==3):
                    a = cm.tan(n)
                    print(f"Tangent:{a}") 
                elif(c1==4):
                    a = cm.asin(n)
                    print(f"Arc sine:{a}")
                elif(c1==5):
                    a = cm.acos(n)
                    print(f"Arc cosine:{a}")
                elif(c1==6):
                    a = cm.atan(n)
                    print(f"Arc tangent:{a}")
                elif(c1==7):
                    a = cm.sinh(n)
                    print(f"Hyperbolic sine:{a}") 
                elif(c1==8):
                    a = cm.cosh(n)
                    print(f"Hyperbolic Cosine:{a}")
                elif(c1==9):
                    a = cm.tanh(n)
                    print(f"Hyperbolic tangent:{a}")
                elif(c1==10):
                    a = cm.asinh(n)
                    print(f"Hyperbolic arc sine:{a}") 
                elif(c1==11):
                    a = cm.acosh(n)
                    print(f"Hyperbolic arc cosine:{a}") 
                elif(c1==12):
                    a = cm.atanh(n)
                    print(f"Hyperbolic arc tangent:{a}") 
                elif(c1==13):
                    n2 = input("Enter second number:")
                    n2 = complex(n2)
                    print(f"Addition:{n+n2}")
                elif(c1==14):
                    n2 = input("Enter second number:")
                    n2 = complex(n2)
                    print(f"Subtraction:{n-n2}")
                elif(c1==15):
                    n2 = input("Enter second number:")
                    n2 = complex(n2)
                    print(f"Multiplication:{n*n2}")
                elif(c1==16):
                    n2 = input("Enter second number:")
                    n2 = complex(n2)
                    print(f"Division:{n/n2}")
                elif(c1==17):
                    ans = n**(1/2)
                    ans2 = 0-ans
                    print(f"Square root:{ans},{ans2}")
                elif(c1==18):
                    n3 = np.array(n)
                    real = np.real(n3)
                    img = np.imag(n3)
                    ans = ((real**2)+(img**2))**(1/2)
                    print(f"Mod:{ans}")
                elif(c1==19):
                    print(f"Inverse:{1/n}")
                else:
                    print("Invalid choice")
                    se.inch()
                se.inch()
                    
            except ValueError as e:
                print(f"Error:{e}")  
                se.inch()
            except AttributeError as e:
                print(f"Error:{e}")
                se.inch()
            except:
                print("Error 404")
                se.inch()
                
        elif(choice==7):
            try:
                print("1. System of 2 linear equations")
                print("2. Roots of a qudratic equation")
                print("3. System of 3 linear equations")
                print("4. System of given linear equations")
                c1 = int(input("Choice:"))
                if(c1==1):
                   se.linear_equation_2()
                elif(c1==2):
                    se.roots_of_quadratic()
                elif(c1==3):
                    se.linear_equation_3()
                elif(c1==4):
                    se.linear_equation_solver()
                else:
                    print("Invalid choice")
                    se.inch()
                se.inch()
                    
            except ValueError as e:
                print(f"Error:{e}")
                se.inch()
            except:
                print("Error 404")
                se.inch()
                
        elif(choice==8):
                try:
                    c1 = int(input("1.Arithmetic operations\n2.Single matrix operations\nChoice:"))
                    if(c1==1):
                        se.matrix_operations()
                    elif(c1==2):
                        se.matrix_operations_2()
                    else:
                        print("Invalid choice")
                        se.inch()
                    
                except ValueError as e