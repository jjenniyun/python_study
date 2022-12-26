# method
# name = "jenny"

# print(name.endswith("y"))
numbers = [5,3,1,5,7,3,"True",True, 12,["🍕","🍔"]]
numbers.append("😂")
print(numbers[-1])

# list리스트 []: 변경가능
days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days_of_week[2])
#days_of_week.append("Sat")
#days_of_week.remove("Fri")
#days_of_week.append("Sun")

# 튜플 () : 불변(변경불가능), 메소드 한정
numbers = (1,2,3,4,5,True, "xxxxx")
days = ("Mon", "Tue", "Wed")

print(days[-1])

# 딕셔너리 {key:value}: 변경가능(추가 및 삭제)
player = {
  'name': 'jenny', 
  'age': 20, 
  'alive': True, 
  'fav_food': ["🍕", "🍔"],
  "friend":{
    "name":"jisu",
    "fav_food":["🍉"]
  }
}

player['fav_food'] ="🍇"
player.pop("alive")
player['friend']['fav_food'].append("🍌")

print(player)

print(player.get('age'))
print(player.get('fav_food'))
print(player['fav_food'])
print(player)
player.pop('age')
print(player)
player['xp'] = 1500
print(player)
player['fav_food'].append("🌭")
print(player.get('fav_food'))
print(player['fav_food'])

