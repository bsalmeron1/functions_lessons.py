# Indefinite Arguments (*args) Practice #1




def tea_order(customer, type, milk=None, *args, **kwargs):  #TWO STARS MEANS TWO VALUE I THINK The equals signs. extra keyword arguements into a dictionary milk sweetney
    print(customer, "ordered a ", type, " tea")
    # if milk!=None:
    #     print (customer, "ordered a ", type, " tea, with no milk")
    for key, value in kwargs.items():  #THIS IS ABLE TO MAKE A DIFFERENT DICTIONARY 
        print("   - Add", key, ":" , value)
    for arg in args:
        print("  -Add", arg)

    # for kwargs in kwargs:
        #print("kwargs contains: ", kwargs)
#tea_order("alice", "pink", milk="oat", sweetner="honey")
print(tea_order)











# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).

def sum_squares(*args):
    sum=0 #initialize sum is zero
    for num in args: #iterate trhough each  arguement
        sum += num ** 2 #sqaure the umber ad add it to sum
    return sum 
print(sum_squares(1,2,3))
# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total=0
    for num in args: #add the absolute value of the numner to 
        total += abs(num) # add the abs value to each numner

return total
print(absolute_sum(-1,-2,-3))
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"