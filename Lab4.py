print("1)\n")
a = True
if a == True:
    print('a result is true')
print("\n")

print("2)\n")
b = 5
if b <= 5:
    print('b is less or equal to 5')
print("\n")

print("3)\n")
a,b = 5,6
if a is not b:
    print('a is not b is true')
print("\n")

print("4)\n")
a,b = 5,6
if a > 5 and b > 5 :
    print('a and b is greater than 5')
elif a > 5 or b > 5 :
    print('a or b is greater than 5')
else:
    print('a and b is lesser or equal to 5) # try to change b to value less or equal to 5')\

print("5)\n")
n=6
current_sum = 0
i = 0
while i <= n:
    current_sum += i
    i += 1
    print(current_sum)
print("\n")

print("5)\n, \r")
myFriends = ['Joe', 'Zoe', 'Alvin', 'Paris']
for friend in myFriends:
    invite = 'Hi ' + friend + '. Please come to my party!'
    print(invite)
print("\n")

print("6)\n,")
dict = {}
dict['one'] = 'Thid is one'
dict[2] = 'This is two'
tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
print("\n")
 
print("7)\n,")
dictionary_tk = { "name": "Leandro", "nickname": "Tk", "nationality": "Brazilian", "age": 24 }
for attribute, value in dictionary_tk.items():
    print("My %s is %s" %(attribute, value))
    
print("hello")

print('test')
























































































































































