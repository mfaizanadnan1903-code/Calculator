import math as m
import numpy as np
import statistics as s
import First as f
import Second as se

def inch():
    p = (input("Enter 1 for again execution or enter any character to exit program:"))
    if(p=="1"):
        f.calculator()
        
def all_ungroup():
    try:
        print(f"Mean:{s.mean(l:=se.single_input_list_observations(n:=se.single_input_integer_obs()))}\nMedian:{s.median(l)}\nMode:{s.mode(l)}\nGeometric mean:{s.geometric_mean(l)}\nHarmonic mean:{s.harmonic_mean(l)}\nStandard deviation:{s.stdev(l)}\nVariance:{s.variance(l)}")
    except ValueError:
        inch()
        
def mean_deviation_ungroup():
    n = int(input("Enter no. of observations:"))
    l = np.array([float(input(f"Enter {i+1} observation:")) for i in range(n)])
    mean = l.mean()
    l = l-mean
    l = np.abs(l)
    ans = (l.sum())/n
    print("Mean deviation:",ans)

def mean_deviation_group():
    n = int(input("Enter no. of observations:"))
    lower = np.array([float(input(f"Enter {i+1} lower class boundary:")) for i in range(n)])
    upper = np.array([float(input(f"Enter {i+1} upper class boundary:")) for i in range(n)])
    freq = np.array([int(input(f"Enter {i+1} frequency:")) for i in range(n)])
    x = (upper+lower)/2
    mean = x.mean()
    x = x-mean
    x = np.abs(x)
    fx = freq*x
    sum = freq.sum()
    ans = (fx.sum())/sum
    print("Mean deviation:",ans)
        
def moment_group():
    try:
        choice = int(input("1.Moment about mean\n2.Moment about arbitrary constant\n3.Moment about zero\nChoice:"))
        n = int(input("Enter no. of observations:"))
        lower,upper,freq = [],[],[]
        for i in range(n):
            lower.append(float(input(f"Enter {i+1} lower class limit:")))
            upper.append(float(input(f"Enter {i+1} upper class limit:")))
            freq.append(float(input(f"Enter {i+1} frequency:")))
        lower,upper,freq = np.array(lower),np.array(upper),np.array(freq)
        l = (lower+upper)/2
        num = int(input("Enter moment number:"))
        if choice==1:
            print(f"Moment about mean:{(freq*((l-(((freq*l).sum())/freq.sum()))**num)).sum()/freq.sum()}")
        elif choice==2:
            g = float(input("Enter constant:"))
            print("Moment about {g} : {(freq*((l-g)**num)).sum()/freq.sum()}")
        elif choice==3:
            print(f"Moment about zero: {(freq*(l**num)).sum()/freq.sum()}")
    except:
        print('Error occured')
        se.inch()      
          
def moment_ungroup():
    try:
        choice = int(input("1.Moment about mean\n2.Moment about arbitrary constant\n3.Moment about zero\nChoice:"))
        n = int(input("Enter no. of observations:"))
        l = np.array([float(input(f"Enter {i+1} observation:")) for i in range(n)])
        num = int(input("Enter moment number:"))
        if choice==1:
            print(f"Moment about mean:{(((l-(l.mean()))**num).sum())/n}")
        elif choice==2:
            g = float(input("Enter constant:"))
            print(f"Moment about {g}:{(((l-g)**num).sum())/n}")
        elif choice==3:
            print(f"Moment about origin:{((l**num).sum())/n}")
        else:
            print("Invalid choice")
            se.inch()
    except:
        print("Error occured")
        se.inch()       
        
def median_discrete():
    try:
        import numpy as np
        n = int(input("Enter no. of observations:"))
        l = [float(input(f"Enter {i+1} observation:")) for i in range(n)]
        f = [float(input(f"Enter {i+1} frequency:")) for i in range(n)]

        l2 = []
        a,b = 0,f[0]
        for i in range(1,len(f)):
            l2.append(b)
            a = f[i]
            b = a+b
        l2.append(b)

        f = np.array(f)
        sum = (f.sum())/2
        gh = 0
        for i in range(1,len(f)-1):
            if sum > l2[i-1] and sum<=l2[i]:
                gh = i
        median = l[gh]
        print("Median:",median)
    except ValueError:
        print("Error occured")
        inch()      

def quartile_discrete():
    try:
        import numpy as np
        n = int(input("Enter no. of observations:"))
        l = [float(input(f"Enter {i+1} observation:")) for i in range(n)]
        f = [float(input(f"Enter {i+1} frequency:")) for i in range(n)]
        
        n = int(input("Enter quartile number:"))
        
        l2 = []
        a,b = 0,f[0]
        for i in range(1,len(f)):
            l2.append(b)
            a = f[i]
            b = a+b
        l2.append(b)

        f = np.array(f)
        sum = (n*f.sum())/4
        gh = 0
        for i in range(1,len(f)-1):
            if sum > l2[i-1] and sum<=l2[i]:
                gh = i
        quartile = l[gh]
        print("Quartile {n}:",quartile)
    except ValueError:
        print("Error occured")
        inch()
        
def decile_discrete():
    try:
        import numpy as np
        n = int(input("Enter no. of observations:"))
        l = [float(input(f"Enter {i+1} observation:")) for i in range(n)]
        f = [float(input(f"Enter {i+1} frequency:")) for i in range(n)]
        
        n = int(input("Enter decile number:"))
        
        l2 = []
        a,b = 0,f[0]
        for i in range(1,len(f)):
            l2.append(b)
            a = f[i]
            b = a+b
        l2.append(b)

        f = np.array(f)
        sum = (n*f.sum())/4
        gh = 0
        for i in range(1,len(f)-1):
            if sum > l2[i-1] and sum<=l2[i]:
                gh = i
        decile = l[gh]
        print("Decile {n}:",decile)
    except ValueError:
        print("Error occured")
        inch()
        
def mode_discrete():
    try:
        import numpy as np
        n = int(input("Enter no. of observations:"))
        l = [float(input(f"Enter {i+1} observation:")) for i in range(n)]
        f = np.array([float(input(f"Enter {i+1} frequency:")) for i in range(n)])
        
        max = f.max()
        gh = 0
        for i in range(len(f)-1):
            if max==f[i]:
                gh = i
        
        mode = l[gh]
        print("Mode:",mode)
    except ValueError:
        print("Error occured")
        inch()
        
def percentile_discrete():
    try:
        import numpy as np
        n = int(input("Enter no. of observations:"))
        l = [float(input(f"Enter {i+1} observation:")) for i in range(n)]
        f = [float(input(f"Enter {i+1} frequency:")) for i in range(n)]
        
        n = int(input("Enter percentile number:"))
        
        l2 = []
        a,b = 0,f[0]
        for i in range(1,len(f)):
            l2.append(b)
            a = f[i]
            b = a+b
        l2.append(b)

        f = np.array(f)
        sum = (n*f.sum())/4
        gh = 0
        for i in range(1,len(f)-1):
            if sum > l2[i-1] and sum<=l2[i]:
                gh = i
        percentile = l[gh]
        print(f"Percentile {n}:",percentile)
    except ValueError:
        print("Error occured")
        inch()      
                       
def tiles():
    try:
        option = int(input('1.Quartile\n2.Decile\n3.Percentile\nChoice:'))
        if option==1:
            text="quartile"
        elif option==2:
            text="decile"
        elif option==3:
            text="percentile"
            
        n = int(input("Enter no. of observations"))
        upper_class = []
        lower_class = []
        frequency = []
        num = int(input(f"Enter {text} number:"))
        
        for i in range(n):
            lower_class.append(float(input(f"Enter {i+1} lower class limit:")))
            upper_class.append(float(input(f"Enter {i+1} upper class limit:")))
            frequency.append(float(input(f"Enter {i+1} frequency:")))
    
        lower_class = np.array(lower_class)
        upper_class = np.array(upper_class)
        cum_freq = []
        
        a,b = 0,frequency[0]
        for i in range(len(frequency)-1):
            cum_freq.append(b)
            a = frequency[i+1]
            b = a+b
        cum_freq.append(b)
        
        g = (lower_class[1]-upper_class[0])/2
        lower_bound = lower_class-g
        upper_bound = upper_class+g
        frequency = np.array(frequency)

        if option == 1:
            if num > 0 and num <= 3:
                sum = (num*frequency.sum())/4
            else:
                print("You can't find {text}")
                inch()
        elif option == 2:
            if num > 0 and num <= 9:
                sum = (num*frequency.sum())/10
            else:
                print("You can't find {text}")
                inch()
        elif option == 3:
            if num > 0 and num <= 99:
                sum = (num*frequency.sum())/100
            else:
                print("You can't find {text}")
                inch()
            
        gh = 0
        for i in range(1,len(cum_freq)-1):
            if sum > cum_freq[i-1] and sum<=cum_freq[i]:
                gh = i
                
        h = upper_class[gh]-upper_class[gh-1]
        l = lower_bound[gh]
        f = frequency[gh]
        
        c = 0
        if(gh!=0):
            c = cum_freq[gh-1]
            
        ans = l+((h/f)*(sum-c))
        ans = np.round(ans,4)
        print(f"{text} {num} : {ans}")
    except:
        print("Error occured")
        inch()

        
def tiles_ungroup():
    try:
        n = int(input("Enter no. of observations:"))
        l = [float(input(f"Enter {i+1} observation:")) for i in range(n)]
        l.sort()
        option = int(input("1.Quartile\n2.Decile\n3.Percentile\nChoice:"))
        
        if option==1:
            text = "Quartile"
        elif option==2:
            text = "Decile"
        elif option==3:
            text = "Percentile"
        else:
            print("Invalid choice")
            inch()

        num = int(input(f"Enter {text} number:"))
        if option==1:
            if num > 0 and num <=3:
                sum = (num*(len(l)+1))/4
                sum2 = (num*(len(l)+1))//4
            else:
                print(f"You can't find {text.lowercase()}")
                inch()
        elif option==2:
            if num > 0 and num <=9:
                sum = (num*(len(l)+1))/10
                sum2 = (num*(len(l)+1))//10
            else:
                print(f"You can't find {text.lowercase()}")  
                inch()
        elif option==3:
            if num > 0 and num <=99:
                sum = (num*(len(l)+1))/100
                sum2 = (num*(len(l)+1))//100
            else:
                print(f"You can't find {text.lowercase()}")
                inch()
                
        n1 = sum-sum2
        ans = l[sum2-1] + n1*(l[sum2] - l[sum2-1])
        print(f"{text} {num} : {ans}")
    except:
        print("Error occured")
        inch()        
        
def mode_grouped():
    try:
        n = int(input("Enter no. of observations"))
        upper_class = []
        lower_class = []
        frequency = []

        for i in range(n):
            lower_class.append(float(input(f"Enter {i+1} lower class limit:")))
            upper_class.append(float(input(f"Enter {i+1} upper class limit:")))
            frequency.append(float(input(f"Enter {i+1} frequency:")))
    
        lower_class = np.array(lower_class)
        upper_class = np.array(upper_class)
        g = (lower_class[1]-upper_class[0])/2
        lower_bound = lower_class-g
        upper_bound = upper_class+g
        frequency = np.array(frequency)
        
        gh = 0
        max = frequency.max()
        for i in range(1,len(frequency)-1):
            if max==frequency[i]:
                gh = i
        
        h = upper_class[gh]-upper_class[gh-1]
        l = lower_bound[gh]
        fm = frequency[gh]
        
        f1 = 0
        if(gh!=0):
            f1 = frequency[gh-1]
            
        f2 = 0   
        if(gh!=len(frequency)-1):
            f2 = frequency[gh+1]

        ans = l + (((fm-f1)/((2*fm)-f1-f2))*h)
        return np.round(ans,4)
    except:
        print("Error occured")
        inch()
                  
def median_grouped():
    try:
        n = int(input("Enter no. of observations"))
        upper_class = []
        lower_class = []
        frequency = []

        for i in range(n):
            lower_class.append(float(input(f"Enter {i+1} lower class limit:")))
            upper_class.append(float(input(f"Enter {i+1} upper class limit:")))
            frequency.append(float(input(f"Enter {i+1} frequency:")))
    
        lower_class = np.array(lower_class)
        upper_class = np.array(upper_class)
        cum_freq = []
        
        a,b = 0,frequency[0]
        for i in range(len(frequency)-1):
            cum_freq.append(b)
            a = frequency[i+1]
            b = a+b
        cum_freq.append(b)
        
        g = (lower_class[1]-upper_class[0])/2
        lower_bound = lower_class-g
        upper_bound = upper_class+g
        frequency = np.array(frequency)
        sum = (frequency.sum())/2
        gh = 0
        for i in range(1,len(cum_freq)-1):
            if sum > cum_freq[i-1] and sum<=cum_freq[i]:
                gh = i
                
        h = upper_class[gh]-upper_class[gh-1]
        l = lower_bound[gh]
        f = frequency[gh]
        if(gh!=0):
            c = cum_freq[gh-1]
        ans = l+((h/f)*(sum-c))
        return np.round(ans,4)
    except:
        print("Error occured") 
        inch()
    
def geometric_mean_grouped():
    try:
        n = int(input("Enter no. of obseravtions:"))
        l1 = np.array([float(input(f"Enter {i+1} observation:")) for i in range(n)])
        l2 = np.array([float(input(f"Enter {i+1} frequency:")) for i in range(n)])
        l1 = np.log(l1)
        l3 = l1*l2
        a = l2.sum()
        b = l3.sum()
        return m.exp(b/a)
    except ValueError:
            print("Error occured")      
            inch()        
            
def harmonic_mean_grouped():
    try:
        n = int(input("Enter no. of obseravtions:"))
        l1 = np.array([float(input(f"Enter {i+1} observation:")) for i in range(n)])
        l2 = np.array([float(input(f"Enter {i+1} frequency:")) for i in range(n)])
        l1 = 1/l1
        l3 = l1*l2
        a = l2.sum()
        b = l3.sum()
        return np.round(a/b,4)
    except ValueError:
            print("Error occured")      
            inch()
            
def mean_grouped():
    try:
        n = int(input("Enter no. of obseravtions:"))
        lower = [float(input(f"Enter {i+1} lower class limit:")) for i in range(n)]
        upper = [float(input(f"Enter {i+1} upper class limit:")) for i in range(n)]
        freq = [float(input(f"Enter {i+1} frequency:")) for i in range(n)]
        lower = np.array(lower)
        upper = np.array(upper)
        freq = np.array(freq)
        l1 = (upper+lower)/2
        l2 = l1*freq
        a = freq.sum()
        b = l2.sum()
        return np.round(b/a,4)
    except ValueError:
            print("Error occured")      
            inch()
           
def variance_grouped():
        try:
            n = int(input("Enter no. of obseravtions:"))
            l1 = np.array([float(input(f"Enter {i+1} observation:")) for i in range(n)])
            l2 = np.array([float(input(f"Enter {i+1} frequency:")) for i in range(n)])     
            l3 = l1*l2
            l4 = l2*(l1**2)
            a = l2.sum()
            b = l3.sum()
            c = l4.sum()
            return np.round((c/a)-(b/a)**2,4)
        except ValueError:
            print("Error occured")        
            inch()
                
def all_grouped():
    import math as m
    import numpy as np
    try:
        n = int(input("Enter no. of observations"))
        upper_class = []
        lower_class = []
        frequency = []

        for i in range(n):
            lower_class.append(float(input(f"Enter {i+1} lower class limit:")))
            upper_class.append(float(input(f"Enter {i+1} upper class limit:")))
            frequency.append(float(input(f"Enter {i+1} frequency:")))
            
        #making lower,upper class boundaries and midpoint lists
        lower_class = np.array(lower_class)
        upper_class = np.array(upper_class)
        g = (lower_class[1]-upper_class[0])/2
        lower_bound = lower_class-g
        upper_bound = upper_class+g
        l1 = (lower_class+upper_class)/2
        
        #making cumulative frequency column
        cum_freq = []
        a,b = 0,frequency[0]
        for i in range(len(frequency)-1):
            cum_freq.append(b)
            a = frequency[i+1]
            b = a+b
        cum_freq.append(b)
        frequency = np.array(frequency)
        l2 = frequency*l1
        a = l2.sum()
        b = frequency.sum()
        
        #finding class interval
        h = upper_class[gh]-upper_class[gh-1]
             
        #finding index for mode     
        gh = 0
        max = frequency.max()
        for i in range(1,len(frequency)-1):
            if max==frequency[i]:
                gh = i
                
        #finding index for median
        idx = 0
        sum = (frequency.sum())/2
        for i in range(1,len(cum_freq)-1):
            if sum > cum_freq[i-1] and sum<=cum_freq[i]:
                idx = i
                
         #making geometric mean logic
        l7 = np.log(l1)       
        l3 = l7*frequency
        c = l3.sum()
        d = frequency.sum()
        ans3 = m.exp(c/d)
         
         #making harmonic mean logic
        l4 = 1/l1
        l5 = frequency*l4
        h = l5.sum()
        ans4 = d/h
         
        #making formula variables
        if(idx!=0):
            c = cum_freq[idx-1]      
              
        l = lower_bound[gh]
        fm = frequency[gh]
        f = frequency[idx]
        lower2 = lower_bound[idx]
        
        f1 = 0
        if(gh!=0):
            f1 = frequency[gh-1] 
            
        f2 = 0
        if(gh!=len(frequency)-1):
            f2 = frequency[gh+1]

        ans = l + (((fm-f1)*h/((2*fm)-f1-f2)))
        ans2 = lower2+((h/f)*(sum-c))
        
        #making variance logic
        l6 = l1**2
        e = l6.sum()
        m = l1.sum()
        ans5 = (e/d)-(m/d)**2
        
        print("Mean:",np.round(a/b,4))
        print("Geometric mean:",np.round(ans3,4))
        print("Harmoinc mean",np.round(ans4,4))
        print("Median:",np.round(ans2,4))
        print("Mode:",np.round(ans,4))
        print("Variance:",np.round(ans5,4))
        print("Standard deviation:",np.round(ans5**(1/2)),4)
        
    except ValueError:
        print("Error occured")
        inch() 
        
if __name__ == "__main__":
    all_ungroup()
    all_grouped()
    moment_ungroup()
    moment_group()
    tiles()
    mean_deviation()
    harmonic_mean_grouped()
    geometric_mean_grouped()
    mean_grouped()
    median_grouped()
    mode_grouped()
    variance_grouped()