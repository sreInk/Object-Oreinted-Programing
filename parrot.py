class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
bl = parrot("Assect",4686)
da = parrot("Garabge.com","Older Than Elon Musk(212323Bce)")

print("Info Collected by FBI Parrot 1{}".format(bl.species))
print("Info Collected by FBI Parrot 2{}".format(da.species))

print("Parrot 1 name is {} His age is {}".format(bl.age,bl.name))
print("Parrot 2 name is {} His age is {}".format(da.age,da.name))
        
        