# A function that calculates the speed needed for a given set of values
# of the target distance (in m) and launch angle (in degrees)
# the function has input arguments L and theta
import math as m

def launch_speed( L, theta ): 
    g = 9.81 # the acceleration in m/s^2
    theta_rad = m.radians(theta) # converting the angle from degrees to radians 
    v0 = m.sqrt( L*g / (m.sin(2*theta_rad) ) ) # calculate the speed
    return v0 # return the calculated value
