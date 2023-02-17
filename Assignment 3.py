 
#Maxwell Ntiamoah
# Index Number: 6942721


#Question (a)
import numpy as np

L = 12                                     #Length of the beam
w = 10                                     #Load intensity of the beam
ends = np.linspace(0,12,2)                 #ends represent the values of the bending moment and shear force at the ends of the beam


for x in ends:                             #x represents a distance on the beam
    # Bending Moment M
    M = w * (-6*x**2 + 6*L*x - L**2)/12
  
    # Shear Force V
    V = w * (L/2 - x)
    print(f'Bending Moment (M) and Shear Force (V) at {x}m are {M} kN/m and\{V} kN respectively.\n')

    

#Question (b)
"The bending moment equation when M is zero is -6x**2 + 72x -144=0"
a = -6
b = 72
c = -144
discriminant =b**2 - 4*a*c
complete_square = b/(2*a)                       #Represents the coefficient of x in the quadratic of the form ax^2 + bx + c = 0 of which we multiply by 1/2
constant = (c/a) - complete_square**2
#Square the term b/2a and add it to the constant -c/a 
#The constant is - in order to represent the quadratic -6x^2 + 72x - 144 in the form x^2 + bx/a = -c/a 
point_of_contra_flexure_1 =(constant)**0.5-complete_square
point_of_contra_flexure_2 = (-(constant**0.5)-complete_square)
#point_of_contraflexure_1 and point_of_contraflexure_2 are roots of the quadratic equation.
print(f'b)The distances at which the bending moment will be zero are x1 = {point_of_contra_flexure_1} and x2= {point_of_contra_flexure_2}') 




#Question (c)
V = 0
#The expression for x when the Shear Force is zero
x = V + (L/2)
#The point_V0 represents the point when the shear force is zero
point_V0 = x              
print('the point when the Shear force is 0 is = ' + str(point_V0) + 'm') 




#Question (d)
discretize_span = np.linspace(0,12,1201)        #The discretize_span gives the distances from 0 to 12 at a step of 0.01

M_calculated = list()                          #M_calculated is an empty list 

for x in discretize_span:
    # Bending Moment M
    M = w * (-6*x**2 + 6*L*x - L**2)/12
    M_calculated.append(round(M,1))            #This step stores the values of x starting from 0 to 12 with a step of 0.01 using the original Bending Moment equation M and rounds it up to 1 decimal place
Bend_Moment = np.array(M_calculated)           #Bend_Moment is an array of the M_calculated
print(Bend_Moment)



# Qustion (e)
V_calculated = list()                    #The V_calculated is an empty list
for x in discretize_span:
    # Shear Force V
    V = w * (L/2 - x)
    V_calculated.append(round(V,1))      #This step stores the values of x starting from 0 to 12 at a step of 0.01 using the original Shear Force equation V and rounds it up to 1 decimal place
    
Shear_Force = np.array(V_calculated)      #Shear_Force is an array of V_calculated
print(Shear_Force)



#Question (f)
"""
Let the absolute value of the bending moment array be M_absolute
Also let the minimum AM be Minimum_absolute_moment"""
M_absolute = abs(Bend_Moment)            #Find the values of x within the beam_span that are close to zero and take them to zero
Minimum_absolute_moment= min(M_absolute)   #This operation is carried out because Bending Moment is minimum when x = 0(Absolute)

"""When the bending moment is Minimum_absolute_moment, we get an expression x**2 - Lx + (L**2/6)+(2*Minimum_absolute_moment)/w = 0"""

#from the above expression
a = 1
b = -L
c = (L**2/6)+(2*Minimum_absolute_moment)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a
print()
print(f'f)The points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(root_1f,root_2f))     


#Question g
"""
Let the relative errors be r_error
"""
r_error_a = ((9.464101615137753-9.46)/9.464101615137753*100)
r_error_b = (( 2.539999999999999-2.5358983848622456)/2.539999999999999*100)
print()
print('(g) The relative errors between estimated points of contra-flexure are {0}% and {1}%'.format(r_error_a,r_error_b))


#Question h
for y in Bend_Moment:
    z_1 = min(Bend_Moment) # Finding the minium bending moment
    z_2 = max(Bend_Moment) # Finding the maximum bending moment
    position_1 = np.where(Bend_Moment == z_1) # Finding the indexes of the min bending moment in the array
    position_2 = np.where(Bend_Moment == z_2) # Finding the indexes of the max bending moment in the array
    
points_pos_1 = list(position_1[0]) # Making the indexes of min bending moment into a list
points_1 = list(discretize_span[points_pos_1]) # Indexing the corresponding points in the discretize span

points_pos_2 = list(position_2[0]) # Making the indexes of max bending moment into a list
points_2 = list(discretize_span[points_pos_2]) # Indexing the corresponding points in the discretize span


print(f'The points at which the minimum bending moment occur are {points_1[0]}m and {points_1[1]}m')
print(f'The point at which the maximum bending moment occur is {points_2[0]}m')

 

#Githiub Username = mntiamoah546
