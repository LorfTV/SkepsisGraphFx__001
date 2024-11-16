import matplotlib.pyplot as plt  
import numpy as np
import streamlit as st
from keta_eq import convert_equation
from default_setup_I import default_setup
import io
from PIL import Image

def input_eq(): 
    global x, y, con_input_Eq, x_max, x_min, input_Eq
    
    input_Eq = st.text_input("Write an equation in terms of x:")

    # Allow users to either use a slider or enter values manually
    x_min_slider = st.slider("Enter the minimum value of x (default: -10):", -100.0, 0.0, -10.0)
    x_min_manual = st.text_input("Or manually input the minimum value of x:", str(x_min_slider))
    x_min = float(x_min_manual) if x_min_manual else x_min_slider  # Use the manual input if provided

    x_max_slider = st.slider("Enter the maximum value of x (default: 10):", 0.0, 100.0, 10.0)
    x_max_manual = st.text_input("Or manually input the maximum value of x:", str(x_max_slider))
    x_max = float(x_max_manual) if x_max_manual else x_max_slider  # Use the manual input if provided
    
    x = np.linspace(x_min, x_max, 100)  # Generates x values from x_min to x_max
    
    if input_Eq:
        con_input_Eq = convert_equation(input_Eq)  # Convert input equation to a usable format
    else:
        con_input_Eq = ""
    
    try:
        # Evaluate the equation only if con_input_Eq is valid
        if con_input_Eq:  
            y = eval(con_input_Eq, {"np": np, "x": x})
        else:
            y = np.zeros_like(x)  # Default to zero if no equation is provided
    except Exception as e:
        st.error(f"Error evaluating the equation: {e}")
        y = np.zeros_like(x)
    
    return x, y, con_input_Eq  # Return the x values, y values, and the equation string

def build_eq(): 
    x, y, con_input_Eq = input_eq()

    # If the equation is valid, plot the graph
    if con_input_Eq:
        st.subheader(f"Equation: {con_input_Eq}")
        
        # Set the graph style
        plt.figure(figsize=(10, 6))
        
        plt.plot(x, y, label=f"{input_Eq}", color='b', linewidth=2)
        plt.xlabel('x', fontsize=14)
        plt.ylabel('y', fontsize=14)
        plt.title(f"Graph of {input_Eq}", fontsize=16)
        plt.legend()

        default_setup()
        
        # Display the plot with Streamlit
        st.pyplot(plt)
    else:
        st.warning("Please enter an equation to plot.")

def save_plot():
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Streamlit app starts here
st.set_page_config(page_title="Graph.F(X)", layout="wide")
st.title("Graph.F(X)")  

# Sidebar content with better styling and information
st.sidebar.image("skepsis_f(x).png", use_column_width=True)
st.sidebar.title("**Graph.F[X]**")  
st.sidebar.write("*Skepsis Foundation's*") 
st.sidebar.write("### **Developed By Nachiketa Vellikad**") 
st.sidebar.write("*Beta_ve--0.1*") 
st.sidebar.write("***Write any equation in terms of x and with numerical data, and have fun!***") 

build_eq()

# Download button
if con_input_Eq:
    buf = save_plot()
    st.download_button("Download Graphed plot", buf, "skepsisFX_Graph.png", "image/png")
