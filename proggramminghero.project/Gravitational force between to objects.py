def gravitational_force_between_2_objects(m1, m2, r):
    G = 6.67 * (10 ** (-11))
    gravitation = (G * m1 * m2) / (r ** 2)

    return round(gravitation)

mass1 = float(input("Enter mass 1st Object: "))
mass2 = float(input("Enter mass 2nd Object: "))
r = float(input("Enter distance between 2 objects: "))

all_amounts = gravitational_force_between_2_objects(mass1, mass2, r)
print(all_amounts, "N")


