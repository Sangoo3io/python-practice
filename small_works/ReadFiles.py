def read_files(Target_file):
    print("---現在のタスク一覧---")
    try:
        with open(Target_file,"r",encoding="utf-8") as f:
            tasks = f.readlines()
            for task in tasks:
                print(task.strip())

    except FileNotFoundError:
        print("タスクファイルがまだありません。")

    print("-----------------------")

if __name__ == "__main__": 
    read_files("tasks.txt")