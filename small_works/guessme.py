import random

# ランダムに数字を生成する
guessme = random.randint(1,20)

# print(f"デバッグ用文：当てなきゃいけない数字は{guessme}です")

#数を当てさせる
def ask_number():
    while True:
        guess = input("1~20の自然数を入力してください：")
        if guess.isdigit() == False:
            print("1~20の自然数ではありません。")
        elif int(guess) < 1 or int(guess) > 20:
            print("1~20の自然数ではありません。")
        else:
            return int(guess)

#数字の大小をチェックして、大小の判定を行う
def check_number(guess,guessme):
    if guess < guessme:
        print("もっと大きい数字です")
        return False    
    elif guess == guessme:
        print("正解です！")
        return True
    else:
        print("もっと小さい数字です")
        return False

# 数当てと正誤判定を5回繰り返す
for i in range(5):
    guess = ask_number()
    Clear = check_number(guess,guessme)
    if Clear == True:
        print("お疲れさまでした")
        break
    elif i == 4:
        print(f"正解は{guessme}でした")