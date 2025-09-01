# ユーザーIDのデータ
users = [
  {"id": "A001", "name": "佐藤", "team": "営業部"},
  {"id": "B002", "name": "鈴木", "team": "開発部"},
  {"id": "C003", "name": "高橋", "team": "営業部"},
  {"id": "D004", "name": "田中", "team": "情シス"},
  {"id": "E005", "name": "伊藤", "team": "開発部"}
]

def find_users_by_team(user_list,target_team):
  for user in user_list:
    if target_team == user["team"]:
      print(user["name"])

name_list = [item["name"] for item in users]
print(name_list)

# 作成した関数を呼び出す
print("営業部のメンバー:")
find_users_by_team(users, "営業部")

print("\n開発部のメンバー:")
find_users_by_team(users, "開発部")