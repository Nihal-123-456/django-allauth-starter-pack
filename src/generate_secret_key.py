import secrets
import string

def generate_django_secret_key():
    characters = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(characters) for _ in range(50))
    return secret_key

print(generate_django_secret_key())
