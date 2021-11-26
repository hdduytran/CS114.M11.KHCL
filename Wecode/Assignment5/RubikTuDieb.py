def Rotate(Rubik, action):
    Case = [action[0].upper(), len(action)]
    indexCombination = [[4, 6, 5, 1], [8, 3, 7, 6]]
    if Case[0] == "U":
        Top, Left, Right = 0, 2, 3
    elif Case[0] == "B":
        Top, Left, Right = 1, 3, 2
    elif Case[0] == "L":
        Top, Left, Right = 2, 0, 1
    elif Case[0] == "R":
        Top, Left, Right = 3, 1, 0

    if Case[1] == 2:
        Left, Right = Right, Left
        indexCombination = indexCombination[::-1]
    Floor = 1 if action[0].isupper() else 4

    for floor in range(Floor):       
        Rubik[Top][floor], Rubik[Left][indexCombination[0][floor]], Rubik[Right][indexCombination[1][floor]] = Rubik[Left][indexCombination[0][floor]], Rubik[Right][indexCombination[1][floor]], Rubik[Top][floor]
       
def Anti_Rotate(Rubik, action):
    if len(action) == 1:
        Rotate(Rubik, action + "'")
    else:
        Rotate(Rubik, action[0])
    

Colors = list(input().split())
Actions = list(input().split())
End = input()
Rubik = [[color for _ in range(9)] for color in Colors]
Actions.reverse()
for action in Actions:
    Anti_Rotate(Rubik, action)
for i in Rubik:
    for j in i:
        print(j, end = " ")
    print()