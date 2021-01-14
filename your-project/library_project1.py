
def create_my_password():
    import random
    
    password_len = int(input("How many characters do you want the password to have? "))
    
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_char = ['!','.',',','&','%','@','*','#']
    
    random_number = random.choice(numbers) 
    random_lower = random.choice(lower_letters) 
    random_upper = random.choice(upper_letters) 
    random_special = random.choice(special_char)

    password_part1 = random_number + random_lower + random_upper + random_special

    all_options = numbers + lower_letters + upper_letters + special_char

    password_part2 = ""

    for i in range(0,password_len-4):
        i = (random.choice(all_options))
        password_part2 = password_part2 + i
    
    password = password_part1 + password_part2
    
    return "Your password is: " + password