Amount_of_motors=int(input("How many motors are carrying the packages?"))
Kg_packages=int(input("How many kg of packages do we expect?"))

if Kg_packages/Amount_of_motors<=12:
    print("Yes! The conceyor belt can carry the packages")
else:
    print("No. The conveyor belt cannot carry the packages")
