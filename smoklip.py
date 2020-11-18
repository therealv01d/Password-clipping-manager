import pyperclip
import sys 

class Smoklip(object):
    def __init__(self):
        pass

    # This function just returns a dictionary
    def returnDict(self):
        accounts = {"user1": {"email": "user1@gmail.com", "password": "password123"},
                "user2": {"email": "user2@gmail.com", "password": "password123"}}
        return accounts


    # Clipping function
    def askusername(self, username):
        # Storing the dictionary inside accounts 
        accounts = self.returnDict()
        if username.lower() in accounts:
            for key, values in accounts.items():
                pyperclip.copy(values["password"])
                print("Password for account " + username + " has been copied to clipboard")
                break
        else:
            print("Not found")
            sys.exit()
