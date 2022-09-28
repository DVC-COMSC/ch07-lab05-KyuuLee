strval = input().split()
numbers = []
for v in strval:
	numbers.append(int(v))
print (numbers)
# numbers = list(map(int, strval))
# print (numbers)

target = int(input('Enter your number'))
cnt = numbers.count(target)
print (cnt)
