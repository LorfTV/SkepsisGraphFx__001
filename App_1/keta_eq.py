import re
import numpy as np

def convert_equation(equation):
    # Replace ^ with ** for exponentiation
    equation = equation.replace('^', '**')
    
    # Add multiplication where needed (between numbers and variables like 4x)
    equation = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation)
    
    # Replace sin, cos, log, etc., with their numpy equivalents
    equation = re.sub(r'\bsin\(', 'np.sin(', equation)
    equation = re.sub(r'\bcos\(', 'np.cos(', equation)
    equation = re.sub(r'\btan\(', 'np.tan(', equation)
    equation = re.sub(r'\blog\(', 'np.log(', equation)
    equation = re.sub(r'\bsqrt\(', 'np.sqrt(', equation)
    equation = re.sub(r'\be\^', 'np.exp', equation)
    
    # If the equation contains 'x' or other variables, make sure it is recognized
    equation = equation.replace('x', 'x')  # Just a placeholder for consistency

    return equation

# Example usage:
user_input = "x^2 + 4x - sin(x) + log(x)"
converted_equation = convert_equation(user_input)
print("Converted equation:", converted_equation)
