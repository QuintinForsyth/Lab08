import summonFile as s

people = s.csv21list("people.csv")

def country_count(people):
  """
  counts contries
  """
  countries = []
  for country in people:
    if country[4] not in countries:
      countries.append(country[4])
      countries.append(1)
    elif country[4] in countries:
      for i in countries:
        if i == country[4]:
          f = countries.index(i)
          f=f+1
          countries[f] = countries[f] +1

  f = 0
  for i in countries:
      f = countries.index(i)
      f+=1
      if f %2 == 0:
        continue
      print(f"We have {countries[f]} from {i} attending this Class")

country_count(people)