import random

#三本勝負
mywin = 0
oppwin = 0

# 勝ち負け判定のタプルを作る
wins = [("グー","チョキ"),("チョキ","パー"),("パー","グー")]

#三本先取の連続バトルを行う
while mywin < 2 and oppwin < 2:

    # 相手の手をランダムに決める
    opphand=random.choice(["グー","チョキ","パー"])
    print(f"相手は{opphand}を出そうとしています…")

    # 自分の手を入力させる
    while True:
        myhand = input("グー、チョキ、パーのどれかを入力してください！")
        print(f"あなたは{myhand}を繰り出します…") 
        if myhand not in["グー","チョキ","パー"]:
            print("無効な手です！グー、チョキ、パーのどれかを入力してください！")
        else:
            break  

    # 勝ち負け判定をする
    print(f"あなたの{myhand}と、相手の{opphand}は…！")

    if (myhand,opphand) in wins:
        mywin += 1
        print("あなたの勝ちです！")
    elif myhand == opphand:
        print("引き分けでした")
    else:
        oppwin += 1
        print("あなたの負けです…")

    print(f"あなたは現在{mywin}勝{oppwin}負です")

# 繰り返しが終わった条件によって、分岐を行う
if mywin == 2:
    print("あなたはじゃんけん三本勝負に勝ちました！")
else:
    print("あなたはじゃんけん三本勝負に負けました…")
    
