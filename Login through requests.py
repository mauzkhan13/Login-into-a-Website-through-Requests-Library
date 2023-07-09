# Importing necessary libraries

# from bs4 import BeautifulSoup
import requests

# Define the login and main URLs.

login_url = 'https://expertisenews.be/fr/login/'
main_url = 'https://expertisenews.be/fr/wp-admin/admin-ajax.php'

# Define the login credentials

payload = {
    'username': 'abc@gmail.com',
    'password': '123456789' 
}

# Create a session and log in

with requests.session() as s:
    response = s.post(login_url, data=payload)  # Send a POST request to the login URL with the login credentials

    if response.status_code == 200:  # Check if the login is successful (status code 200)
        print("Login successful!")
        r = s.get(main_url)  # Send a GET request to the main URL using the session
        soup = BeautifulSoup(r.content, 'html.parser')  # Create a BeautifulSoup object from the response content

        print(soup.prettify())  # Print the prettified HTML content
    elif response.status_code == 401:  # Check if the payload is incorrect (status code 401)
        print("Incorrect login credentials!")
    else:
        print("Login failed!")  # Print a message if the login is unsuccessful
