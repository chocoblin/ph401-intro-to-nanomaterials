#   NAME    -   ADITYA RAJ
#   ROLL NO.-   1901CB02
#   COURSE  -   PH401 (Introduction to Nanomaterials) 
#   QUESTION-   Write a computer programming to deduce the total number of atoms and
#               surface atoms for different shell of cuboctahedral/spherical shape. 
#               Plot % of atoms in bulk/surface versus particle size. The user should
#               get idea to generate the thickness or size of nanoparticle for a 
#               particular application(optical/electrical/magnetic/strength)

#Importing the libraries
import matplotlib.pyplot as plt
plt.style.use('dark_background')

# surface/bulk atoms w.r.t shell no.
shell = int(input("Enter shell no. "))
total = (10*shell*shell*shell-15*shell*shell+11*shell-3)//3
surface = (10*shell*shell-20*shell+12)
print("Total no. of atoms is :")
print(total)
print("")
print("No. of surface atoms is :")
print(surface)


x = []
y=[]
# Plotting of graph
for i in range(1,100):
    
    x.append(i)
    num = (10*i*i*i-15*i*i+11*i-3)//3
    den = (10*i*i-20*i+12)
    y.append((den/num)*100)
plt.plot(x,y)
plt.xlabel('shell number')
plt.ylabel('% surface atoms')
plt.show()

# Properties
size = int(input("Enter the size of the nano-particle(in nm)"))
if(size>100):
    print("The particle behaves normally and does not show nano-behaviours.")
elif(size>80):
    print("The mechanical properties are changed.")
elif(size>30):
    print("The mechanical properties and optical properties both are changed")
elif (size>10):
    print("The magnetic,mechanical and optical properties, all are changed")
else:
    print("The magnetic,mechanical,electrical and optical properties, all are changed")