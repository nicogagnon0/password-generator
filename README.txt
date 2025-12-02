Password Generator - NET2008 Assignment 4

1. Description
- A Python password generator application that offers options for length and types of characters.

- Lets the user choose the password length (between 8 and 128).
- Options to include:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Digits (0-9)
  - Symbols (!@#$)
- Guarantees at least one character from each selected category.
- Can generate multiple passwords in one run until user exits.

2. Run the App Locally
Prerequisites:
- Python 3 installed on your system.
 
Steps:
- Open a terminal or command prompt.
- Navigate to the folder that contains 'app.py'.
- Run the command:

   python app.py
 
- Follow the on-screen prompts to generate passwords.

3. Running the App with Docker
Prerequisites:
- Docker installed and running on your machine.
 
Build the Docker image:
 
   docker build -t YOUR_DOCKERHUB_USERNAME/password-generator:latest .
 
Run the container (interactive mode to answer prompts):
 
   docker run --rm -it YOUR_DOCKERHUB_USERNAME/password-generator:latest

4. Links
https://github.com/nicogagnon0/password-generator
https://hub.docker.com/repository/docker/nickg10/password-generator