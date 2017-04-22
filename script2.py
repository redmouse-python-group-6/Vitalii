from my_user import User
import shelve

db=shelve.open('my_user.db')
print db['user1']