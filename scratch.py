#ways of opening files:

print("hello world i'm working")
try:
    f=open("file.txt")
    #f=open("numfile.txt")
    for line in f:
        print(f.read(10))
        print("*")
except:
    print("Error in reading the file")
finally:
    f.close
    


with open("file.txt") as f:
    print(f.read()) 