import sympy as sp
from sympy import *
import numpy as np
from sympy.plotting import plot
from sympy import fourier_series, pi, plot
import matplotlib.pyplot as plt
print("\t\t\tFOURIER SERIES for PERIODIC funtions\n")
c='y'
while(c=='y' or c=='Y'):
    print("enter the equations in terms of x-->f(x)")
    x=symbols('x')
    
    print("\nEnter the choice\n1.Periodic function\n2.Piecewise function with 2 pieces\n3.Piecewise function with 3 pieces\n : ")
    n=int(input())
    
    if(n==1):
        e1=eval(input("Enter the periodic equation : "))
        
        
        
        a=eval(input("enter the lower limit: "))
        b=eval(input("enter the upper limit: "))
        num=int(input("Enter the number of terms to display : ") )
        s = fourier_series(e1,(x,a,b))
        s1 = s.truncate(n=num)
        s2=s.truncate(n=5)
        s3=s.truncate(n=25)
        print("The given fourier seriesof function ",e1," is : ")
        print(s1)
        ch=input("\nDo you wish to plot the fn (y/n): ")
        if(ch=='y' or ch=='Y'):
            p=plot(e1,s2,s3,(x,a,b),legend=True)
            p[0].line_color = 'red'
            p[0].label = 'x'
            p[1].line_color = 'green'
            p[1].label = 'n=5'
            p[2].line_color = 'blue'
            p[2].label = 'n=25'
            p.show()
            
    
    elif(n==2):
        e1=eval(input("Enter the 1st eq : "))  
        l1=eval(input("enter the 1st lower limit: "))
        u1=eval(input("enter the 1st upper limit: "))
        e2=eval(input("Enter the 2nd eq : "))
        l2=eval(input("enter the 2nd lower limit: "))
        u2=eval(input("enter the 2nd upper limit: "))
        f = sp.Piecewise(
            (e1, (x > l1)&(x<u1)),
            (e2, (x > l2)&(x<u2)),
            
            (0, True))

        # Define the period of the function
        T = 2

        # Define the Fourier series coefficients
        a0 = (1/T) * sp.integrate(f, (x, 0, T))
        an = (2/T) * sp.integrate(f*sp.cos(n*sp.pi*x/T), (x, 0, T))
        bn = (2/T) * sp.integrate(f*sp.sin(n*sp.pi*x/T), (x, 0, T))
        num=int(input("Enter the number of terms to display : ") )
        fourier_series = a0/2
        fourier_s = a0/2
        for i in range(1, num+1):
            fourier_s += an.subs(n, i)*sp.cos(i*sp.pi*x/T) + bn.subs(n, i)*sp.sin(i*sp.pi*x/T)
        print(fourier_s)
        ch=input("\nDo you wish to plot the fn (y/n): ")
        if(ch=='y' or ch=='Y'):
            for i in range(1, 50):
                fourier_series += an.subs(n, i)*sp.cos(i*sp.pi*x/T) + bn.subs(n, i)*sp.sin(i*sp.pi*x/T)
                f_np = sp.lambdify(x, fourier_series, 'numpy')
               
            # Plot the function and its Fourier series approximation
            x_vals = np.linspace(0, T, 1000)
            f_vals = f_np(x_vals)
            plt.plot(x_vals, f_vals, label='Fourier series')
            
            plt.legend()
            plt.show()
    elif(n==3):
        e1=eval(input("Enter the 1st eq : "))  
        l1=eval(input("enter the 1st lower limit: "))
        u1=eval(input("enter the 1st upper limit: "))
        e2=eval(input("Enter the 2nd eq : "))
        l2=eval(input("enter the 2nd lower limit: "))
        u2=eval(input("enter the 2nd upper limit: "))
        e3=eval(input("Enter the 3rd eq : "))  
        l3=eval(input("enter the 3rd lower limit: "))
        u3=eval(input("enter the 3rd upper limit: "))
        f = sp.Piecewise(
            (e1, (x > l1)&(x<u1)),
            (e2, (x > l2)&(x<u2)),
            (e3, (x > l3)&(x<u3)),
            (0, True))

        # Define the period of the function
        T = 2

        # Define the Fourier series coefficients
        a0 = (1/T) * sp.integrate(f, (x, 0, T))
        an = (2/T) * sp.integrate(f*sp.cos(n*sp.pi*x/T), (x, 0, T))
        bn = (2/T) * sp.integrate(f*sp.sin(n*sp.pi*x/T), (x, 0, T))
        num=int(input("Enter the number of terms to display : ") )
        fourier_series = a0/2
        fourier_s = a0/2
        for i in range(1, num+1):
            fourier_s += an.subs(n, i)*sp.cos(i*sp.pi*x/T) + bn.subs(n, i)*sp.sin(i*sp.pi*x/T)
        print(fourier_s)
        ch=input("\nDo you wish to plot the fn (y/n): ")
        if(ch=='y' or ch=='Y'):
            for i in range(1, 50):
                fourier_series += an.subs(n, i)*sp.cos(i*sp.pi*x/T) + bn.subs(n, i)*sp.sin(i*sp.pi*x/T)
                f_np = sp.lambdify(x, fourier_series, 'numpy')
                
            # Plot the function and its Fourier series approximation
            x_vals = np.linspace(0, T, 1000)
            f_vals = f_np(x_vals)
            plt.plot(x_vals, f_vals, label='Fourier series')
            
            plt.legend()
            plt.show()
    c=input("\nDo you want to continue for another function (y/n) ? ")