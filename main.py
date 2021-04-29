"""targil 1"""
#seif a
def sumNumbers():
    sum=0
    num=input("Enter number: ")
    while num.lower() != "stop":
        sum+=int(num)
        num = input("Enter number ")
    print(sum)

#seif b
def sumList():
    sum=0
    numList=input("Enter list: ").split(',')
    for num in numList:
        sum+=int(num)
    print(sum)
#sumList()
"""targil 2"""
def ticTacToe(mat):
    # check horizontal lines for player1
    if((mat[0][0] == mat[0][1] == mat[0][2] == 1) or (mat[1][0] == mat[1][1] == mat[1][2] == 1) or (mat[2][0] == mat[2][1] == mat[2][2] == 1)):
        return "player 1 won"
    # check vertical lines for player1
    elif ((mat[0][0] == mat[1][0] == mat[2][0] == 1) or (mat[0][1] == mat[1][1] == mat[2][1] == 1) or (mat[0][2] == mat[1][2] == mat[2][2] == 1)):
        return "player 1 won"
    # check the crosses for player1
    elif ((mat[0][0] == mat[1][1] == mat[2][2] == 1) or (mat[0][2] == mat[1][1] == mat[2][0] == 1)):
        return "player 1 won"
    # check the horizontal lines for player2
    elif ((mat[0][0] == mat[0][1] == mat[0][2] == 2) or (mat[1][0] == mat[1][1] == mat[1][2] == 2) or (mat[2][0] == mat[2][1] == mat[2][2] == 2)):
        return "player 2 won"
    # check vertical lines for player2
    elif ((mat[0][0] == mat[1][0] == mat[2][0] == 2) or (mat[0][1] == mat[1][1] == mat[2][1] == 2) or (mat[0][2] == mat[1][2] == mat[2][2] == 2)):
        return "player 2 won"
    # check crosses for player2
    elif ((mat[0][0] == mat[1][1] == mat[2][2] == 2) or (mat[0][2] == mat[1][1] == mat[2][0] == 2)):
        return "player 2 won"
    # if non of the checks is true, the game represents a draw
    else:
        return "it's a tie"
game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]
#print(ticTacToe(game))


"""targil 3"""
def minimizeString():
    st=input("Enter string: ")
    count=1
    st2=""
    if len(st) > 1:
        for i in range (len(st)-1):
            if st[i] == st[i+1] and i+1 != len(st)-1:
                count += 1
            else:
                if i+1 == len(st)-1 and st[i] == st[i+1]:
                    count += 1
                st2 += st[i]
                st2 += str(count)
                count = 1
        if st[i] != st[i+1]:
            st2 += st[i+1]
            st2 += str(count)
    else:
        st2 += st[0]
        st2 += str(1)
    return st2
#print(minimizeString())

"""targil 4"""
def isValidID():
    st = input("Enter ID: ")
    sum=0
    for i in range (len(st)-1):
        if i % 2 == 0:
            sum += int(st[i])
        else:
            temp = int(st[i]) * 2
            if temp > 9:
                sum += temp % 10 + int(temp / 10)
            else:
                sum += temp

    if sum % 10 != 0:
        sum2 = sum + (10 - sum % 10)
    else:
        sum2 = sum
    if sum2 - sum == int(st[8]):
        return "Valid"
    return "Not valid"
#print(isValidID())

"""targil 5"""
def func(value):
    return value * value

def mapFunc(arr, funcName):
    return [funcName(val) for val in arr]

"""targil 6"""
class CacheDec(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result

@CacheDec
def powNum(base,power):
    if power == 0:
        return 1
    if base == 0:
        return 0
    return powNum(base,power - 1) * base
#print(powNum(2,5))

def main():
    print("targil 1a: \n")
    sumNumbers()
    print("#################################\n")
    print("targil 1b: \n")
    sumList()
    print("#################################\n")
    print("targil 2: \n")
    print(ticTacToe())
    print("#################################\n")
    print("targil 3: \n")
    print(minimizeString())
    print("#################################\n")
    print("targil 4: \n")
    print(isValidID())
    print("#################################\n")
    print("targil 5: \n")
    arr = [1,2,3]
    print(mapFunc(arr, func))
    print("#################################\n")
    print("targil 6: \n")
    print(powNum(2,5))
    print("all powNum that cached: ", powNum)
    print("#################################\n")

if __name__ == "__main__":
    main()










