# method
# name = "jenny"

# print(name.endswith("y"))
numbers = [5,3,1,5,7,3,"True",True, 12,["π","π"]]
numbers.append("π")
print(numbers[-1])

# listλ¦¬μ€νΈ []: λ³κ²½κ°λ₯
days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days_of_week[2])
#days_of_week.append("Sat")
#days_of_week.remove("Fri")
#days_of_week.append("Sun")

# νν () : λΆλ³(λ³κ²½λΆκ°λ₯), λ©μλ νμ 
numbers = (1,2,3,4,5,True, "xxxxx")
days = ("Mon", "Tue", "Wed")

print(days[-1])

# λμλλ¦¬ {key:value}: λ³κ²½κ°λ₯(μΆκ° λ° μ­μ )
player = {
  'name': 'jenny', 
  'age': 20, 
  'alive': True, 
  'fav_food': ["π", "π"],
  "friend":{
    "name":"jisu",
    "fav_food":["π"]
  }
}

player['fav_food'] ="π"
player.pop("alive")
player['friend']['fav_food'].append("π")

print(player)

print(player.get('age'))
print(player.get('fav_food'))
print(player['fav_food'])
print(player)
player.pop('age')
print(player)
player['xp'] = 1500
print(player)
player['fav_food'].append("π­")
print(player.get('fav_food'))
print(player['fav_food'])

