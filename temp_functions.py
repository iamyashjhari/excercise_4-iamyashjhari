#fahr_to_celsius

def fahr_to_celsius(fahrenheit): #describes the one parameter of the function, namely Fahrenheit.
    
    #I used docstring to explain the purpose of the parameters and what their return will be.
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Parameters:
    -fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
    - float: Equivalent temperature in Celsius.
    """
    celsius= (fahrenheit -32)/ 1.8
    return celsius
    (print)= (f"{temp_fahrenheit} degrees Fahrenheit is equal to {temp_celsius: 2f} degrees Celsius.")
    
    
def temp_classifier(temp_celsius):   #defines temp_classifier with its parameter temp_celsius
    """    #docstring provides documentation for parameter and its returns
    
    Classify temperatures based on predefined criteria.  
    
    Parameters:
    - temp_celsius (float): Temperature in Celsius to be categorized


    Returns:
    - int: Classification based on the following criteria:
        0: Temperatures below -2 degrees Celsius
        1: Temperature equal to or warmer than -2, but less than +2 degrees Celsius
        2: Temperature equal to or warmer than +2, but less than +15 degrees Celsius
        3: Temperature equal or warmer than +15 degrees Celsius
     """
    #using if-elif-else
    if temp_celsius < -2:
        return 0
    
    elif -2 <= temp_celsius < 2:
        return 1
    
    elif 2 <= temp_celsius < 15:
        return 2
    
    else:
        return 3
    

    print (f"The temperature {temperature} degrees Celsius is classified as: {classification}")
   
    