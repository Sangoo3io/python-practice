FILENAME="tasks.txt"

import small_works.ReadFiles as ReadFiles
import small_works.EditFiles as EditFiles

# 選択肢を表示
while True:
    print("以下の数字を入力し、操作を選択してください。")
    user_choice=input("1: タスクを追加, 2: タスクを表示, 3: 終了")
    if user_choice == "1":
        EditFiles.EditFiles(FILENAME)
    elif user_choice == "2":
        ReadFiles.ReadFiles(FILENAME)
    elif user_choice == "3":
        print("YourTaskManager.pyを終了します。")
        print("お疲れさまでした。")
        break
    else:
        print("1~3以外の文字列が入力されました。")

if __name__ == "__main__":
    main()