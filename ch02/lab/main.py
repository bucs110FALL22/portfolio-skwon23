import random
#Part A
weeks = 16
classes = 5
tuition = 6000

classes_per_week = 3
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

cost_per_class = int(cost_per_week) / int(classes_per_week)

print("The cost per class is", float(cost_per_class))

#Part B
list = ['apple','banana','grape','watermelon', 'peach']
random_fruit = random.choice(list)
print(random_fruit)