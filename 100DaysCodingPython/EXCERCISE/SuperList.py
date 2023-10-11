class SuperList(list):
    def __len__(self):
        return 1000



superlist = SuperList()
superlist.append(5)
superlist.append(4)
superlist.append(10)
superlist.append(15)

print(superlist)
print(len(superlist))
print(issubclass(SuperList,list))
