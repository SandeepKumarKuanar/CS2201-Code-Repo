## substances of the move made 

pre_training_string = "harry love to eat . he is a good boy . he read a lot . but he is a food lover . he eat chocolate . he eat candy . he eat pizza . he eat chocolate again . he eat chocolate every day . he is never tired of eat ."
l = pre_training_string.split(" . ")
text = []
for i in l:
    words = i.split(" ")
    text += words

prompted = input("Enter the word which u want this model to guess the immediate next word for!\n").lower().strip()

words_those_follow = []
while prompted in text:
    position = text.index(prompted)
    words_those_follow.append(text[position + 1])
    text.pop(position)

needs = set(words_those_follow)
repeats = []
for i in needs:
    repeats.append(words_those_follow.count(i))


nr = [i for i in needs]
lr = [i for i in repeats]

try:
    print(f"Words those follow prompted word '{prompted}' are {needs}")
    print("This is the one with the maximum probability that would follow: " + nr[lr.index(max(lr))])
except:
    print("The word doesn't have anyone following, hence next move cannot be predicted!")
