#name

name = input('What is your name? ')

while True:
    try: 
        if len(name) < 3:
            print("Name must be at least 3 characters:")
            name = input('What is your name? ')
            continue
            
        elif len(name) > 15:
            print("Name must be a max 15 characters")
            name = input('What is your name? ')
            continue
        else:
            break
    except ValueError:
        continue


last = input('What is your last name? ')

while True:
    try: 
        if len(last) < 3:
            print("Name must be at least 3 characters:")
            last = input('What is your last name? ')
            continue
            
        elif len(last) > 15:
            print("Name must be a max 15 characters")
            last = input('What is your last name? ')
            continue
        else:
            break
    except ValueError:
        continue


    # if answer in [len(3), len(15)]
    #     break   

# last = input('What is your last name? ')

# if len(last) < 3:
#     print("Name must be at least 3 characters:")
# elif len(last) > 15:
#     print("Name must be a max 15 characters")
# else:
#    last = input('What is your last name? ')



# print("Hello")
# print("I love you")
# answer = input("Do you love me?")

# # while True:
# #     try:
# #         if answer == "yes":
# #             print("Yey! I knew it! Thank You!")
# #             break
# #         elif answer == "no":
# #             print("O-ok, I understand, no worries.")
# #             break
# #         else:
# #             print("Please answer me.")
# #             answer = input("Do you love me?")
# #     except ValueError:
# #         continue


# while True:
#   try:
#     print("Please answer me.")
#     answer = input("Do you love me?")
#   except ValueError:
#     continue
#   if answer in ["yes", "no"]:
#     break




# from multiprocessing import Process
 
# def loop_a():
#     while 1:
#         print("a")
 
# def loop_b():
#     while 1:
#         print("b")
 
# if __name__ == '__main__':
#     Process(target=loop_a).start()
#     Process(target=loop_b).start()