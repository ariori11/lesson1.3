immutable_var=2,'оса', True
print(immutable_var)
#immutable_var[0]=1
#print(immutable_var) #выдает ошибку, так как
# кортеж неизменяемая коллекция символов
mutable_list=['яблоко','обувь', 9, 7, False]
mutable_list[2]=2
mutable_list.append('слива')
mutable_list.extend('fp')
mutable_list.remove('яблоко')
print(mutable_list)