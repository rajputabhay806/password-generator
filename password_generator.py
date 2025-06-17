import random 
import string 

def generate_password(length):
    characters=string.ascii_letters+ string.digits+ string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("----password generate----")
    try:
        length=int(input("Enter your desire length: "))
        if length<=0:
            print("Please Enter positive number")
        else: 
            password=generate_password(length)
            print(f"Your generated password: {password}")
            
    except:
        print("Invalid input . Please enter a number.")
        
main()        
    
    
