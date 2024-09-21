
def slicer():
    print("Welcome to the email slicer")
    print("")

    email = input("Input your e-mail address: ")

    (username, domain) = email.split("@")
    (domain, extension) = domain.split(".")

    print(F"Username: {username}")
    print(F"Domain: {domain}")
    print(F"Extension: {extension}")

slicer()