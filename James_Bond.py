def introduction(first_name, last_name):
  name = last_name + ',' + ' ' + first_name + ' ' + last_name
  return name

print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou