def edit_files(Target_file):
    new_task = input("新しいタスクを入力してください：")

    with open(Target_file,"a",encoding="utf-8") as f:
        f.write(new_task + "\n")

    print(f"タスク「{new_task}」を{Target_file}に追加しました。")

if __name__ == "__main__": 
    edit_files("tasks.txt") 