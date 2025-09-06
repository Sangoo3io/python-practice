# 名前、値段のデータを持つインスタンスを作るJuiceクラスを作る
class Juice:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

# Juiceでインスタンスを作りながら、自販機のメニュー内容を最初のうちに辞書で定義しておく
MENU = {
    "コーラ" : Juice("コーラ",120,2),
    "お茶" : Juice("お茶",110,3),
    "水" : Juice("水",100,5),
}

# 自販機インスタンスを作るときに必要な、お金が何も入ってない変数を定義する
INITIAL_AMOUNT = 0
MINIMUMPRICE = 100

# 数字かどうかチェックする関数
def validation(target_number):
    if target_number.isdigit() == True:
        # print("これは数字です")
        return True
    else:
        # print("これは数字じゃないです")
        return False

# メニュー、投入金額のデータを持つインスタンスを作るVendingMachineクラスを作る
class VendingMachine:
    def __init__(self,menu,amount):
        self.menu = menu
        self.amount = amount
    
    # お金を入れるinsert_moneyメソッドを作る
    def insert_money(self):
        insert_amount = input("投入金額を入力してください：")
        while True: #投入するお金の入力を半角数字のみに限定する
            if validation(insert_amount) == True:
                self.amount = self.amount + int(insert_amount)
                print(f"{insert_amount}円お金を入れました。")
                break
            else:
                print("数字のみ入力してください。")
                insert_amount = input("投入金額を入力してください：")

    # 売られているドリンクを表示するshow_drinksメソッドを作る
    def show_drinks(self):
        print("--------------")
        for selling_items in self.menu:
            if self.menu[selling_items].stock > 0:
                print(f"{selling_items}：{self.menu[selling_items].price}円")
            else:
                print(f"{selling_items}：{self.menu[selling_items].price}円（売り切れ）")
            print("--------------")

    # ジュースを買うbuy_drinksメソッドを作る
    def buy_drinks(self):
        which_to_buy = input("何を買いますか？：")
        if which_to_buy in self.menu: #menuの中に一致するジュースがあるか？
            if self.menu[which_to_buy].stock > 0: #在庫があるか？
                if self.menu[which_to_buy].price <= self.amount: #それが投入額以下の金額か？
                    print(f"ガラガラガラ…{which_to_buy}が下の方から出てきました。") #それを購入したログを出す
                    self.amount = self.amount - self.menu[which_to_buy].price
                    self.menu[which_to_buy].stock -= 1
                    if self.amount < MINIMUMPRICE and self.amount > 0:
                        self.give_change()
                else:
                    print("ピー！お金が足りません。")
            else:
                print(f"{which_to_buy}は売り切れのようです。")
        else: #menuの中に買いたいジュースがないなら以下を出す
            print(f"この自販機に{which_to_buy}はありませんでした。")

    def give_change(self):
        if self.amount == 0:
            print("カタカタ…お金が入っていないので、おつりが出てきませんでした。")
        else:
            print(f"ジャラジャラ…{self.amount}円のおつりが出てきました。")
            self.amount = 0

# 以上のメソッド(機能)を持つ自動販売機「sanden」を作る
sanden = VendingMachine(MENU,INITIAL_AMOUNT)

# メイン処理スタート
# 自販機について紹介したのち、行動を決めさせる

print("-----------------------------------------")
print("|道を歩いていたら、自販機を見つけました。|")
print("|どうしようかな？　　　　　　　　　　　　|")
print("-----------------------------------------\n")

while True:
    pointer = input("金を入れる:1\n商品を見る:2\nボタンを押す:3\nおつりレバーを引く:4\n帰る:5\n\n………………………：")
    if validation(pointer) == False:
        print("選択肢の中から入力して下さい。")
    elif int(pointer) == 1:
        print("「金を入れる」")
        sanden.insert_money()
    elif int(pointer) == 2:
        print("「商品を見る」")
        sanden.show_drinks()
    elif int(pointer) == 3:
        print("「ボタンを押す」")
        sanden.buy_drinks()
    elif int(pointer) == 4:
        print("「おつりレバーを引く」")
        sanden.give_change()
    elif int(pointer) == 5:
        print("「帰る」")
        print("あなたは帰りました。")
        break
    else:
        print("選択肢の中から入力して下さい。")
    
    print(f"今、自販機には{sanden.amount}円と表示されている。")
    print("さて、どうしようかな…\n")