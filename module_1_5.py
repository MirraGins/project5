
tuple_immutable_var=([1 ,7] ,'orange' ,True ,'fork')
print(tuple_immutable_var)
tuple_immutable_var[0][1]=3
print(tuple_immutable_var)

mutable_list=["popcorn","car","charger",5 ,9]
print(mutable_list)
mutable_list[1]="pen"
print(mutable_list)
mutable_list.extend('abc')
print(mutable_list)