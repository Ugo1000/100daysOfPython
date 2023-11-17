# import translate libary
import transla

print(__dir__(translators))

# try /catch
try:
    with open("myWord.txt", "w") as myNote:
        myNote.write("Hello EveryOne My Name Is Samuel Okoro ")
except FileNotFoundError as e:
    print("file not found ", e)
# file open

try:
    with open("myWord.txt", "r") as myNote:
        print(myNote.readline())
except FileNotFoundError as e:
    print("file not found ", e)
