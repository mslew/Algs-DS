
def signup(username, password):
    hash_username = hash(username)
    hash_password = hash(password)
    return hash_username, hash_password

def login(username, password, database):
    username = hash(input('Enter your username: '))
    password = hash(input('Enter your password: '))
    for e in database:
        if e == (username, password):
            return True
    return False 
    
if __name__ == '__main__':
    saved_username = input('Enter your signup username: ')
    saved_password = input('Enter your signup password: ')
    database = []
    database.append(signup(saved_username, saved_password))
    print(login(saved_username, saved_password, database))