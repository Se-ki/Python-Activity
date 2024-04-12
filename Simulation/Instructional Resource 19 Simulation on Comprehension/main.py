# Python Simulation 19
# Comprehension in Python

#without list comprehension
print()
n1 = int(input("Enter a number: "))
even_nums = []

for x in range(n1):
    if x%2 == 0:
        even_nums.append(x)

print(f"List of Even Numbers: {even_nums}")

#with list comprehension
print()
n2 = int(input("Enter a number: "))
even_num = [x for x in range(n2) if x%2==0]
print(f"Even Numbers: {even_num}")

#more on list comprehension
print()
user = ["Junell", "Maria", "Hannah", "Elisha", "Azaliah", "Rosario"]
print(f"List of Users: {user}")
print()
new_user1 = [un for un in user if 'i' in un]
print(f"New User: {new_user1}")
print()
new_user2 = [un2 for un2 in new_user1 if 'h' in un2]
print(f"Selected User: {new_user2}")

#square of a number
print()
squares = [x*x for x in range(1,11)]
print(f"Squared Numbers: {squares}")

#identifying odd or even
print()
odd_even = ["Even" if i%2==0 else "Odd" for i in range(1,6)]
print(odd_even)
print()
odd_even_list = [str(i)+" = Even" if i%2==0 else str(i)+" = Odd" for i in range(1,11)]
print(odd_even_list)
print()
oe_list = [f"{i} = Even" if i%2==0 else f"{i} = Odd" for i in range(1,11)]
print(oe_list)

#itering with dictionary comprehension
print()
cities = {"SC":"Surigao", "BXU":"Butuan", "CDO":"Cagayan"}
print(f"Cities: {cities}")
for c in cities:
    print(f"{c} = {cities[c]}  \tTypes:{type(c)}|{type(cities[c])}")

print()
print([c for c in cities])
print([cities[c] for c in cities])
print([f"{c} = {cities[c]}" for c in cities])
city_info = [f"{c} = {cities[c]}" for c in cities]
print(f"City Information {city_info}\tType: {type(city_info)}")