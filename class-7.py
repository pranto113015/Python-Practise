# Read file
File = open("Text.txt", "r")
text = File.read()
print(text)


# Write file
File = open("Text.txt", "w")
text = File.write("I am a Front-end developer")
print(text)


# Append File
File = open("Text.txt","a")
text = File.write("\nWelcome to visit my intro")
print(text)


# Forward - Indexing
a="Pranto Kumar"
print(a[4])


# Backward - Indexing
a="Pranto Kumar"
print(a[-4])



# Error handlig-1 (TypeError)
try:
    a=input("Enter the no : ")
    result = 10/a
    print(result)

except TypeError:
    print("Invalid Number")



# Error handlig-2 (ZeroDivisionError)
try:
    a=int(input("Enter the no : "))
    result = 10/a
    print(result)

except ZeroDivisionError:
    print("Invalid Number")




# Error handlig-3 (IndexError)
try:
   a="Prantokumar"
   print(a[20])

except IndexError:
    print("Invalid Key")



# Multiple Error handlig
try:
   a=int(input("Enter Your No : "))
   result = 10/a
   print(result)


except (TypeError,ZeroDivisionError):
    print("Invalid Number")