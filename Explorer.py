import time

print('Welcome traveller to the exploration cave')
time.sleep(1.5)
print('I see you have the spirit of a lion within you')
time.sleep(1.5)
print('Before you enter, I must know you name.... Tell me...')
myName = input()
print()
time.sleep(1)

print('How old are you explorer?')
myAge = input()
time.sleep(1)
if myAge <= str(int(20)):
    print('ah, fresh to the world')
elif myAge > str(int(20)) and myAge <= str(int(50)):
    print('I see you know the way of the world')
elif myAge > str(int(51)):
    print('I guess you know what you are getting into')
