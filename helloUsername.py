# Question 1
def hello_name (user_name):
    print ('hello_' + user_name)

hello_name("Eman")

# Question 2
for odd in range(1, 100):
    if odd % 2 == 1:
        print (odd)

# Question 3
def max_num_in_list(a_list):
    userInput = []
    for a_list in userInput:
        #print (max(a_list), a_list)
        return (max(a_list))
        
max_num_in_list([9, 4, 46, 23, 45, 56, 21])

# Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0 & a_year % 400 == 0:
        #print ('Leap Year!')
        return True
    else:
        #print ('No Leap')
        return False

is_leap_year(2017)

# Question 5
def is_consecutive(a_list):
    #userInput = [a_list]
    #userInput.sort = ()
    # a_list.sort = ()
    # orderCal = 0
    # if orderCal === 1:
        
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1)) 
    # ^^^algo taken from stackoverflow...Don't really understand yet

    #do something the difference of each number in the list is 1 after it is sorted then true if more than 1 then false
    #     print True
    #     return True
    # else
    #     print False
    #     return False
# print (is_consecutive([1, 2, 3, 4, 5, 6]))
is_consecutive([1, 2, 3, 4, 5, 6])