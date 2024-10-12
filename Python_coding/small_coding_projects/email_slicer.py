# collect email from user
# split the email using the @ saving the first part as the username and the second part as the domain
#split the domain using .,

def main():
    print("Welcome to the email slicer ")
    print("")
    
    email_input = input("Input your email address: ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username : ", username)
    print("Domain : ", domain)
    print("Extension: ", extension)
    
while True:
    main()