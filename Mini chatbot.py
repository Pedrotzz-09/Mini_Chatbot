name = input('What is your name?')
print("It is a pleasure to meet you{}, you have a very nice name!".format(name))
print("I don't have a name yet, but you can call me prototype.001!")
age = int(input('How old are you?'))
if age == 20:
  print('Whoa, you are my age,{}!'.format(name))
elif age > 20:
  print('Hey, you are older than me!')
else:
  print('I am older than you!')
print('Well, it was nice to talk to you{}, I hope we can chat again soon, see ya!'.format(name))
