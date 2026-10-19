def calculate_schwarzchild(): 
    # physics constants 
    G = 6.67430e-11 #gravity constant
    C = 299792458 #speed of light 
    
    # user inputs 
    mass_kg = float(input("In kilograms (w/o the units) input the desired mass: "))
    
    # equation 
    sc_radius = (2 * G * mass_kg) / (C**2) 
    
    # Using a comma instead of an f-string
    print("The Schwarzschild radius is", sc_radius, "meters.")
    
calculate_schwarzchild()

#mass of the universe: 1.5e53
#The Schwarzschild radius of the universe is 2.2278480807355996e+26 meters