def minion_game(s):
    vowels = 'AEIOU'
    str_lenght = len(s)
    kevin_score, stuart_score = 0, 0

    for i in range(str_lenght):
        if s[i] in vowels:
            print(str_lenght - i)
            kevin_score += (str_lenght - i)
        else:
            stuart_score += (str_lenght - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

minion_game("BANANA")

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)