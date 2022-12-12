def remove_trash2(setW, let1, let2, det1, det2, det3):
    setR = set()
    for each in setW:
        if (let1 in each) and (let2 in each) and (det1 not in each) and (det2 not in each) and (det3 not in each):
            setR.add(each)
    return setR

def remove_trash3(setW, let1, let2, let3, det1, det2):
    setR = set()
    for each in setW:
        if (let1 in each) and (let2 in each) and (let3 in each) and (det1 not in each) and (det2 not in each):
            setR.add(each)
    return setR

def remove_trash4(setW, let1, let2, let3, let4, det1):
    setR = set()
    for each in setW:
        if (let1 in each) and (let2 in each) and (let3 in each) and (let4 in each) and (det1 not in each):
            setR.add(each)
    return setR

def cleanSet(final_res, setW):
    temp = []
    valid = 0
    trash = []
    for each in final_res:
        if each != "":
            count = final_res.index(each)
            temp.append(count)
    print(final_res)
    # print(temp)
    
    if len(temp) != 0:
        valid = 1
        for each in temp:
            for e in setW:
                if e[each] != final_res[each]:
                    trash.append(e)
    
    if valid == 1:
        for each in trash:
            setW.remove(each)
        return setW
    else:
        return setW

def checkdup(word, colors):
    word = list(word)
    colors = list(colors)
    d = []
    tmp = []
    i = 0

    for each in word:
        if each in tmp:
            d.append([each, i])
        tmp.append(each)
        i+=1
    for each in d:
        if colors[each[1]] == "n":
            colors[each[1]] = "y"
    colors = "".join(colors)
    word = "".join(word)
    return [word, colors]


setW = set()
counter = 0
contains = []
final_res = ["","","","",""]

#main loop
while len(contains) != 5:
    contains = []
    d_contains = []
    word = input("Enter word > ")
    colors = input("Input colors returned in G Y N > ")
    item = checkdup(word, colors)
    word = item[0]
    colors = item[1]
    i = 0
    for each in colors:
        if each == "g": #if letter is marked as green it is in the right place
            final_res[i] = word[i]
            contains.append(word[i])
        elif each == "y": # if letter is marked as yellow it is in the word but not right place
            contains.append(word[i])
        else:
            d_contains.append(word[i])
        i += 1
    #suggesting
    contain = ""
    contain = contain.join(contains)
    if counter == 0:
        f = open("words.csv", "r")
        for each in f:
            tmp = each.split(",")
            for e in tmp:
                for i in range(len(contains)):
                    if contains[i] in e:
                        e = e.replace("\n", "")
                        setW.add(e)

    if len(contains) == 2:
        setW = remove_trash2(setW, contains[0], contains[1], d_contains[0], d_contains[1], d_contains[2])
    elif len(contains) == 3:
        setW = remove_trash3(setW, contains[0], contains[1], contains[2], d_contains[0], d_contains[1])
    elif len(contains) == 4:
        setW = remove_trash4(setW, contains[0], contains[1], contains[2], contains[3], d_contains[0])

    if colors == "ggggg":
        print("WELL DONE!")
    else:
        setW = cleanSet(final_res, setW)
        print(setW)
    counter += 1