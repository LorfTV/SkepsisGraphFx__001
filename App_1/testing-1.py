import matplotlib.pyplot as plt  
from matplotlib.animation import FuncAnimation 
import numpy as np 
from hello_keta_lib_002.keta_eq import convert_equation 
from hello_keta_lib_002.default_setup_I import default_setup 

def input_eq(): 
    global x, y, con_input_Eq, x_max, x_min
    input_Eq = input("Write an equation in terms of x: ")  
    con_input_Eq = convert_equation(input_Eq)
    x_min = float(input("Enter the minimum value of x (default: -10): ") or -10)
    x_max = float(input("Enter the maximum value of x (default: 10): ") or 10)
    x = np.linspace(x_min, x_max, 1000)
    try:
        y = eval(con_input_Eq)  
    except Exception as e: #error handling by ChatGPT
        print(f"Error evaluating the equation: {e}")
        y = np.zeros_like(x)  
    
    return x, y, con_input_Eq  

def build_eq(): 
    x, y, con_input_Eq = input_eq()
    plt.plot(x, y)
    plt.title(f"Graph Plot of: {con_input_Eq}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

build_eq()
