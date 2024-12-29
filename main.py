import random
import time
import math as mt

global choice
# encrypt or decrypt options
choice = input("Do you want to encrypt or decrypt a file? \n TYPE YOUR OPTION IN LOWERCASE. \n ")


def is_ciphered(file_name):
    # check if the file content is unchanged
    with open (file_input) as secret_file:
        text = secret_file.read()
        if (text != text):
            return True
        return False
    
# make file input global for ease of use 
global file_input
global random_num1
global random_num2
global product
global cipher_text

# selected numbers must be large
random_num1 = random.randint(1, 100)
random_num2 = random.randint(1, 100)


# e - public exponent
public_exponent = 7

# make sure selected numbers are prime
def check_prime(random_number) -> bool:
    # must be whole number
    if (random_number) % 1 == 0:
        # must be greater than 1
        if (random_number > 1):
            # cannot be divisible by any number other than 1 and itself
            if (random_number % 1 == 0 and random_number % random_number == 0):
                return True
            return False
        return False
    return False

# make sure selected numbers have a substantial difference
def check_difference(num1, num2) -> bool:
    if (num1 - num2) > 200 or (num2 - num1) > 200:
        return True
    return False


# RSA encryption
def rsa_encrypt():
    if (check_prime(random_num1) and check_prime(random_num2)):
        # carry on with next step of RSA encryption
        print("Both numbers are prime. Carry on")
        time.sleep(2)
        
        # calculate the product of the two numbers
        product = random_num1 * random_num2
        print(f"The product of the two numbers is: {product}")
        
        public_key = (product, public_exponent)
        print(f"Your public key is: {public_key}")
        
        # encrypt the file using the generated RSA keys
        enter_public_key = input("Now, enter your public key to encrypt the file: ")
        
        # cipher text is m^public_exponent mod product. The m indicates the plaintext message from the file.
        # get plaintext message from file
        with open (file_input) as secret_file:
            plain_text = secret_file.read()
            
            # convert string to int
            plain_text_int = int(plain_text)
            
        cipher_text = (mt.pow(plain_text_int, public_exponent)) % product 
        
        # whitespace for readability in terminal
        print("")
        
        print("Congratulations, you have ciphered the text file. \n This is what the cipher text looks like: \n")
        
        # whitespace for readability in terminal
        print("")
        
        print(f"Ciphered text: {cipher_text}")
        
        
        print(f"These are the files that have been ciphered: {choice} \n Do you want to decrypt it?")
        
        # get input
        ch = input("Yes to decrypt, No to stop program.\n lowercase only please. ")
        
        time.sleep(2)
        if ch == 'yes':
            rsa_decrypt()
        
        print("Decrypting... ")
        time.sleep(2)
            
    else:
        print("The two numbers are not prime.")


# RSA decryption
def rsa_decrypt():
    '''
    When decrypting an RSA encrypted message, 
    the recipient uses their private key (n, d) to compute 
    the plaintext message, where the plaintext message = c^d mod n.
    '''
    # with open (file_input) as secret_file:
    #     cipher_text = secret_file.read()
    
    #     # convert string to int
    #     plain_text_int = int(plain_text)
    
    phi_n = (random_num1 - 1) * (random_num2 - 1)
    d = (mt.pow(public_exponent, -1)) % phi_n
    
    decrypted_text = (mt.pow(cipher_text, d)) % product 
    
    private_key = (product, d)
    
    print("Congratulations, you have deciphered the text file. \n This is what the deciphered text looks like: \n")
            
    # whitespace for readability in terminal
    print("")
    
    print(f"Deciphered text: {decrypted_text}")
                

# prompt the user to select a .txt file to encrypt

if choice == "encrypt":
    file_input = input("Select a text file to be encrypted: \n These are the options of the files you can select: \n 'secret_file1.txt', 'secret_file2.txt', 'secret_file3.txt'\n ")
    print("The encryption process is beginning. Please wait...")
    time.sleep(3)
    
    # whitespace for readability in terminal
    print("")
    
    # read the file in the background
    with open (file_input) as secret_file:
        secret_file.read()
    
    rsa_encrypt()

# receiver's side
elif choice == "decrypt":
    file_input = input("Select a text file to be decrypted: ")
    print("The decryption process is beginning. Please wait...")
    time.sleep(3)
    
    # whitespace for readability in terminal
    print("")
    
    with open (file_input) as secret_file:
        text = secret_file.read()
        rsa_decrypt()
        
        # if (is_ciphered(secret_file)):
        #     # code block SHOULD run if file is encrypted
        
else:
    print("Invalid option. Please select either 'encrypt' or 'decrypt'.")




# allow the user to generate RSA public and private keys.
'''
RSA procedure
- choose two large prime numbers for the key pair, 
which is difficult to factorize. the prime numbers must be selected 
randomly and with a substantial difference between them.

- calculate the product of the two numbers. the two numbers must be
kpet secret, while their product is public.

- the Carmecheals’ totient function is calculated using p and q, 
and the integer e, whose value is used as the public exponent, 
is selected. Then the next step is calculating the value of d, 
which is used as the private exponent.

- public key = (product(n), public exponent(e))
'''


print("Two random prime numbers are currently being selected for encryption: \n Please wait...")
time.sleep(3)

# whitespace for readability in terminal
print("")


'''
The system should handle cases where an incorrect key is used to
decrypt the message, explaining why decryption fails.
Log and display the results, detailing whether the decryption
succeeded or failed.
'''
