"""
The following section contains the physics calculations used in the file answer.py.
"""

# Create a new Python file called `physics.py`. Import your new file/module
# in `answer.py` using the import statement: `import physics`
#
# In your physics module create a function `free_fall` that calculates the
# speed after a free fall without air resistance. The function takes two
# arguments time and initial speed. The inital speed argument should have a
# default value of 0 and it should be possible to call the function only with
# a time argument.
#
# Tip: the formula for calculating the speed of a free fall without air
# resistance is:
#
#     speed = initial speed + g * time, where g = 9.82

def free_fall(time, initial_speed=0, g=9.82):
    """
    The function calculates the speed of a free fall.
    """
    speed = initial_speed + g * time
    return speed



# Kinetic energy describes the energy of an object with a certain mass (m)
# and velocity (v).
#
# Create a function `kinetic_energy` that calculates the amount of kinetic
# energy of an object.
#
# The formula for calculating kinetic energy is:
#
#     energy = 0.5 * m * v².
#
# Use your defined function `free_fall` in combination with `kinetic_energy`
# to calculate the kinetic energy of an object with m = 10 after a free fall
# of time = 8 with the default gravity of earth (9.82).

def kinetic_energy(m, t):
    """
    This function calculates the kinetic energy of an object.
    """
    energy = 0.5 * m * (free_fall(t))**2
    return energy



# Potential energy is the energy stored in an object by virtue of the objects
# position in a gravitational field. The higher an object is lifted the
# greater the potential energy.
#
# The formula for calculating the potential energy is:
#
#     energy = m * g * h
#
# with m being the mass of the object, g the gravity and h the height of the
# object.
#
# When an object falls, all of the potential energy is converted into kinetic
# energy. So it is possible to calculate the height of the fall based on the
# amount of kinetic energy an object has at the end of the fall using the
# following formula:
#
#     height = kinetic_energy / (m * g)
#
# Create a function `height` that calculates the height of a free fall of
# time = 8 for an object with m = 10 and g = 9.82. Use your already defined
# functions `free_fall` to calculate the velocity and `kinetic_energy` the
# kinetic energy.

def height(m, t, g=9.82):
    """
    This function combines the free_fall function and kinetic_energy function to calculate height.
    """
    h = kinetic_energy(m, t) / (m * g)
    return h
