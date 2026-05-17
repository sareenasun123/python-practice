# random
import random

print(random.random())

random_num = random.randint(1,50)
print(random_num)

items = [
    "apple",
    "banana",
    "cherry",
    "dragonfruit",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "iceberg lettuce",
    "jackfruit",
    "kiwi",
]
print(random.choice(items))


print("-----------------Welcome to Guess The Number Game----------------")

random_num = random.randint(1,50)
print("Random number is", random_num)

count = 0
max_limit = 5
while True:
    print(f"{max_limit-count} Attempts left")
    user_num = int(input("Guess the number: "))
    count = count + 1
    if user_num == random_num:
        print(f"Congratulation! You guessed the number successfully in {count} attempts.")
        break
    else:
        # if random_num < user_num:
        #     print("Please choose smaller number!")
        # else:
        #     print("Please choose larger number!")
        message = "Choose smaller number!" if random_num < user_num else "Choose larger number!"
       
        print(f'\n{message} \nPlease try again!')

        if count>=max_limit:
            print(f"\nNo attempts remaining. The correct number was {random_num}!")
            break

        
        
    