def display_name(user_name):
    print(user_name)

display_name("Emiliya")

def print_odd():
    for num in range(1, 100):
        if num % 2 == 0:
            print(num)


print_odd()

def max_num_in_list(a_list):
    print(max(a_list))


alist = [ 1,2,3,4,888]
max_num_in_list(alist)

def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        print("leap")
    else:
        print("no leap")

    
is_leap_year(3000)


