#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var=(1,[2,3,4],5,'dog',False)
print(immutable_var)
immutable_var[1][2]=90
print(immutable_var)
mutable_list=[7,8,9,'cat']
print(mutable_list)
mutable_list.append(12)
print(mutable_list)
print(mutable_list[1:4:2])
