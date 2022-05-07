#Chris Kruger
answer = 0
def stringLen(my_string):
    #answer = 0
    global answer
    if my_string != '' :
        answer += 1
        stringLen(my_string[1:])
    return answer


test = "Hello Hoboken!"
print(stringLen(test))
