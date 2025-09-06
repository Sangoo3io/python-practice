import json

my_profile = {
    "name":"sangoo3io",
    "skills":["インターネット","Python(初級)"],
    "Ideal":"Couch potate",
}

with open("profile.json","w",encoding="utf-8") as f:
    json.dump(my_profile,f,indent=2,ensure_ascii=False)

print("profile.jsonを作成しました。")