# Write the function between the START and END tags
# START
def SortWordsAlphabetically(Sentence):
    # words = Sentence.replace("-", " ").lower()
    items=[n for n in Sentence.split('-')]
    items.sort()
    items = '-'.join(items)
    return items
    



# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
# print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
# print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))
print(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible"))