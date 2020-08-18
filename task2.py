def WordSearch(len: int, s: str, subs: str):
    words = s.split(' ')
    output = []
    not_empty = False
    i = 0
    for word in words:
        if findLen(word) <= len and not_empty == False:
            output.append(word)
            not_empty = True
            continue
        elif findLen(word) > len and not_empty == False:
            output.append(word[:len])
            output.append(word[len:])
            not_empty = True
            i += 1
            continue
        elif not_empty == True:
            if findLen(output[i] + ' ' + word) <= len:
                output[i] = output[i] + ' ' + word
                continue
            else:
                i += 1
                if findLen(word) <= len:
                    output.append(word)
                    continue
                else:
                    output.append(word[:len])
                    output.append(word[len:])
                    i += 1
                    continue
    result = []
    for out_str in output:
        if subs in out_str.split(' '):
            result.append(1)
        else:
            result.append(0)
    return result

def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter
