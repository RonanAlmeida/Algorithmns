a_val="GUNBYGUNCWM"
letter_count = {chr(i+64):i for i in range(1,27)}
for char in a_val:
	print(char , letter_count[char])

# print("\n new stuff ")
inv_map = {v: k for k, v in letter_count.items()}
s =""
for char in a_val:
	res = 20- letter_count[char]
	if res == 0:
		print(inv_map[26])
	if res < 0:
		print(inv_map[abs(res)],end =" ")
        # s += inv_map[ abs(res) ]
    
	if res > 0:
		print(inv_map[26-res],end =" ")
        # s += inv_map[26-abs(res)]

b_val="COMPUTING"
print("\n \n \n \n ")
for char in b_val:
	val=(letter_count[char]+20)%26
	print(char,letter_count[char], val, inv_map[val] )

print("hello")

print("\n")
for char in b_val:

    print(inv_map[(letter_count[char]+20)%26],end =" ")


print("\n \n \n \n ")

b_val="GUNBYGUNCWM"
for char in b_val:
	res = 20- letter_count[char]
	# res is 0
	if res == 0:
		print(inv_map[26]) 

	# res is negative
	if res < 0:
		print(inv_map[abs(res)],end =" ")
    
	# res is postive
	if res > 0:
		print(inv_map[26-res],end =" ")


		
print("\n \n \n \n ")
print("\n \n \n \n ")
print("\n \n \n \n ")
print("\n \n \n \n ")
print("\n \n \n \n ")
print("\n \n \n \n ")
