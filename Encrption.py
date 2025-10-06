import random
import string

class work:
        def __init__(self,name):
              self.name=name

        def calculation(self):
                self.char=" "+string.punctuation+string.ascii_letters+string.digits
                self.char=list(self.char)
                self.key=self.char.copy()
                random.shuffle(self.key)
                
#arfagrg
#ganyo
        def encrypt(self):  
                
                plain_text=input("Enter the text to encrypt here: ")
                cypher_text=""
                for letter in plain_text:
                        index=self.char.index(letter)
                        cypher_text+=self.key[index]
                print(cypher_text)
        def decrypt(self):
                decrypt=input("Enter the word to decrypt...")
                plain=""
                for letter in decrypt:
                        index=self.key.index(letter)
                        plain+=self.char[index]
                print(plain)
user=work("Ganyo")
user.calculation()
user.encrypt()
user.decrypt()


# hashlib.sha1(te)
# print(f"Your encrypted text is: {cypher_text}")
# # print(f"Your original text is: {plain_text}")



   


