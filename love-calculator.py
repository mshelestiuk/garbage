print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combine_names = name1 + name2
lower_names = combine_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digits = t + r + u + e
# print(first_digits) # for checking

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digits = l + o + v + e
# print(second_digits) # for checking

score = int(str(first_digits) + str(second_digits))
# print(f"{score}") # for checking
if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}. Move on.")

