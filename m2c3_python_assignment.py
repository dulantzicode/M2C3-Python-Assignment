# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
str_var= 'one is less than two'
num_var= 510
list_var= ['hello','wordl',125,True]
bool_var= False



# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 
first_three_letters= str_var[0:4]



# Exercise 3: Use an index to grab the first element from your list.
first_element= list_var[0]



# Exercise 4: Create a new number variable that adds 10 to your original number.
new_num_var= num_var+10



# Exercise 5: Use an index to get the last element in your list.
last_element= list_var[-1]



# Exercise 6: Use split to transform the following string into a list.
# 	names = 'harry,alex,susie,jared,gail,conner'
names = 'harry,alex,susie,jared,gail,conner'
list_name = names.split()



# Exercise 7: Get the first word from your string using indexes. 
# Use the upper function to transform the letters into uppercase. 
# Create a new string that takes the uppercase word and the rest of the original string.
first_element_uppercase= list_var[0].upper()
new_list_var= list_var
new_list_var[0]= first_element_uppercase



# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
print(f'There are almost {num_var} bugs in my code')


# Exercise 9: Print “hello world”.
print('hello world') 