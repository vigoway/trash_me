l1 = [ x for x in range(1,5) ]
for i in l1:
	print i
input = int(raw_input("type in a number from 1 to 10:"))
matrix = [[x for x in range(input)] for i in range(input)]
print matrix
