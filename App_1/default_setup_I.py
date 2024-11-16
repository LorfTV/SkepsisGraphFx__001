import matplotlib.pyplot as plt
import numpy as np

#inspired by manim by Nachiketa Vellikad for Matplotlib
def default_setup(): 
    plt.grid(True, which='major', axis='both', color='#01A79D', linewidth=0.5) #Grid on both the axis that is white 
    plt.gcf().set_facecolor('Black')  #outer bg
    plt.gca().set_facecolor('Black')  #inner bg
    plt.minorticks_on() #info of the axes  
    plt.tick_params(axis='both', which='both', color='white', labelcolor='white') #styling of the info axes 
    plt.xlabel('x-axis', c='w') #labeling the axes
    plt.ylabel('y-axis', c='w') #labeling the axes
    plt.title('Graph', fontname='serif',color='white',fontsize=15) 
