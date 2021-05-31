# from BOOK.random import getwordsfromuser


# def limit(1,3)
# while True:
#     sentence = input("Type a sentence: ")
#     x = sentence
#     words = len(sentence.split())
#     if words < min or words > maxi:
#         print("Words entered not within defined range. ")
#     else:
#         print('Good Job')
#         print('The words you have entered are:')
#         print(*x.lower().split(), sep='\n')
#         break

# # while True:
#     try:
#         temp = int(input("Enter the temperature of the hour: "))
#     except ValueError:
#         print('Value must be a number.')
#     else:
#         if -50 <= temp <= 130:
#             break
#         else:
#             print('Value must be between -50 and 130')

# while True:
#         min = input('Please enter a minimum number: ')
#         if min.isdigit():
#             break
# min = int(min)
# while True:
#         maxi = input('Please enter a maxium number: ')
#         if maxi.isdigit():
#             break
# maxi = int(maxi)
# while True:
#     sentence = input("Type a sentence: ")
#     x = sentence
#     words = len(sentence.split())
#     if words < min or words > maxi:
#         print("Words entered not within defined range. ")
#     else:
#         print('Good Job')
#         print('The words you have entered are:')
#         print(*x.lower().split(), sep='\n')
#         break

# def getword(min, max):
#     while True:
#         wordlist=[]
#         sentence = input("Type a sentence: ")
#         wordlist = sentence.split()
#         wordlist.append(sentence)
#         if len(wordlist) not in range(min, max):
#             print("Words entered not within defined range. ")
#         else:
#             print('Good Job')
#             print('The words you have entered are:')
#             print(" ".join(wordlist), sep='\n')
#             break
# getword(4,5)

def getword(min, max):
    while True:
        wordlist = []
        sentence = input("Type a sentence: ")
        wordlist = sentence.split()
        print(wordlist)
        x = sentence
        if len(wordlist) not in range(min, max):
            print("Words entered not within defined range. ")
        else:
            print("Good Job")
            print("The words you have entered are:")
            print(*x.lower().split(), sep='\n')
            break
getword(3, 5)
