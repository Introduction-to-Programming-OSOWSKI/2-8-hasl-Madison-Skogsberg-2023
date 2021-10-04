#WRITE YOUR CODE IN THIS FILE
#create function
#add parameters

def hasL(w):

    for i in range (0, len(w)):

        if w[i] == "l":
            return True
    return False

print(hasL("dog"))