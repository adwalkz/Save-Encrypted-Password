import pickle

passwd = 'passwd.txt'

def encrypt(word):
    ew = ''

    for l in word:
        ew += chr(ord(l) + 3)

    return ew
    

def get_all_keys():
    content = {}
    try:
        with open(passwd, 'rb') as f:
            content = pickle.load(f)
    except:
        pass

    return content


def save_new_credential(username, password):    
    data = get_all_keys()
    with open(passwd, 'wb') as f:
        data[username] = encrypt(password)
        print(data)
        pickle.dump(data, f)


def test_login(username, password):
    data = get_all_keys()

    if username in data:
        if data[username] == encrypt(password):
            return 1
        
    return 0


if __name__ == '__main__':
    print('Hello! Thanks for trusting us!\n')

    while True:
        print('SELECT BEST OPTION FOR YOU:')
        print('\t1. SAVE NEW CREDENTIAL')
        print('\t2. DELETE CREDENTIALS')
        print('\t3. UPDATE CREDENTIALS')
        print('\t4. TEST LOGIN')
        print('\t5. EXIT')

        ch = int(input('Enter choice: '))

        match ch:
            case 1  :   
                        print('\n---SAVE-NEW-CREDENTIAL---\n')
                        username = input('Enter Username: ')
                        password = input('Enter Password: ')
                        save_new_credential(username=username, password=password)
                        print('\n@', username, ' your password is safe with us:)', sep='', end='\n\n')

            case 2  :   
                        print('\n---DELETE-CREDENTIAL---\n')
                        delete_credential()

            case 3  :   
                        print('\n---UPDATE-CREDENTIAL---\n')
                        update_credential()

            case 4  :   
                        print('\n---TEST-LOGIN---\n')
                        username = input('Enter Username: ')
                        password = input('Enter Password: ')
                        ret = test_login(username=username, password=password)
                        if ret:
                            print("\n:::::THAT'S CORRECT:::::\n")
                        else:
                            print("\n:::::SORRY THAT DIDN'T WORK:::::\n")

            case 5  :   
                        print('\n---BYE-BYE---\n')
                        exit()

            case _  :   
                        print(ch, 'is NOT a valid option.\n')


