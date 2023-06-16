motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modification
motorcycles[0] = 'test'
print(motorcycles)

# adding to the end of a list
motorcycles.append('ford')
motorcycles.append('ferari')

print(motorcycles)

# inserting elements
motorcycles.insert(0, 'bmw')
print(motorcycles)

# removing elements
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# using pop()
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print(first_owned)

# using remove

motorcycles.remove('yamaha')
print(motorcycles)