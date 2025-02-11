import random
import string

def generate_password(length, complexity):
    """Generate a random password based on specified length and complexity."""
    
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    
    char_pool = lowercase
    
    
    if 'uppercase' in complexity:
        char_pool += uppercase
    if 'digits' in complexity:
        char_pool += digits
    if 'punctuation' in complexity:
        char_pool += punctuation
    
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
   
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 6:
                print("Password length should be at least 6 characters for better security.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the password length.")
    
   
    print("\nChoose the complexity of the password:")
    print("1. Lowercase only")
    print("2. Lowercase + Uppercase")
    print("3. Lowercase + Uppercase + Digits")
    print("4. Lowercase + Uppercase + Digits + Special Characters")
    
    while True:
        complexity_choice = input("Enter your choice (1/2/3/4): ")
        if complexity_choice == '1':
            complexity = ['lowercase']
            break
        elif complexity_choice == '2':
            complexity = ['lowercase', 'uppercase']
            break
        elif complexity_choice == '3':
            complexity = ['lowercase', 'uppercase', 'digits']
            break
        elif complexity_choice == '4':
            complexity = ['lowercase', 'uppercase', 'digits', 'punctuation']
            break
        else:
            print("Invalid choice, please select 1, 2, 3, or 4.")
    
    
    password = generate_password(length, complexity)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
