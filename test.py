import string
teststr = "How can mirrors be real if our eyes aren't real"

def fixString(msg):
    print(msg)
    print(msg.title())
    return string.capwords(msg)

print(fixString(teststr))