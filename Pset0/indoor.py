#This Pset requires me to take an input and output in lowercase 

#This works but i wanna try using ASCII to convert
#String = str(input("Input words here: "))
#Lowercase_String = String.casefold()
#print(Lowercase_String)

String = str(input("Input words here: "))
Split_word = list(String)

#loop to split up elements and impliement
for x in Split_word:
    if (ord(x)> 41 and ord(x)< 91):
        lower_case = chr(ord(x)+32)
        print(lower_case, end = '')
        
    else :
        print(x, end = '')