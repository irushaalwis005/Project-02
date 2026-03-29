x= input("Enter Your Msg:")
shift = 6



for i in x:
    new_char = ord(i)-6
    letter = chr(new_char)
    print(letter,end="")
