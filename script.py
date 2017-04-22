from my_user import User
import shelve

db=shelve.open('my_user.db')
user1=User('Vasa', 'Pupkin')
print(user1)
user2=user3=User('Peta', 'Vasaechkin')
print(user1.name)
print(user2.name)

# user1.name="Vasa"
user1.height=190
print(user1.name)
print(user1.height)
print(user2.height)

print(user2.name)
db['user2']=user2
del user2
user1.olde()
print(user1.age)
user1.olde()
print(user1.age)
user1.say_hello()
user1.say_name()
user1.say_hello('Ms')
db['user1']=user1
db['user3']=user3
