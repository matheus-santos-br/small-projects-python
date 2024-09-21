import urllib.request as urllib

def main(url):
    print("Checking connectivity  ")

    response = urllib.urlopen(url)
    print(F"Connected to {url} succesfuly")
    print(F"The response code was: {response.getcode()}")

print("This is a connection checker.")
input_url = input("Input the url you want to check: ")

main(input_url)