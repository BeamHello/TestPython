a = 5
b = 10

print("Hello my name is Beam.")
print(a+b)

if a < b:
    print("a < b")
elif a == b:
    print(a == b)
else:
    print("I don't know")

# -------------------------------------------

def mul_a_b(a, b):
    '''
    This function multiply a and b together.
    return a*b
    '''
    print(a * b)

mul_a_b(3, 4)

for i in range(0,10):
    print(i)

'''the_array = [1,2,3,4,5]
the_array[0] # first element
the_array[-1] # last element
the_array.append(10) # add 10 at the array
print(the_array)'''

'''for (int i = 0; i < 10; i++):
    print(i)'''

# Challenge!
# create a function to calculate the area of circles.
# Users will specify the number of circles,
# the program will calculate the area of each circle with radius -1
# for example
# input: 5
# process: [the area of circles of radius 1-5 will be calculate].
# output: [print all areas in the screen.]

def cal_circle_area(radius):
    return 3.141 * radius * radius

areas = []

circle_number = int(input("Enter number: "))
for i in range(1, circle_number + 1):
    area = cal_circle_area(i)
    areas.append(area)
    # print("the area of " + str(i) + " is" + str(cal_circle_area(i)))
    print(f"the area of {i} is  {area}")

areas.pop(0)
areas.append(10)
print(areas)
print(f"sum is {sum(areas)}")

# Challenge 2!
# ---------------------------------------
# from the first changllenge...store all areas in an array. :)
# take the first areasof the list, and the add 10 at the end of the array.
# Then, sum of all areas and display name.

grades = {'Mark': 'A', 'Jib' : 'B'}

print(grades['Mark']) #A
print("Hello!!!")