def manacher(inputString):  # longest palindrom
    special_character = "#"
    string = special_character + special_character.join(list(inputString)) + special_character
    counter = [0 for _ in range(len(string))]
 
    current = 1
    counter[current] = 1
    right = current + counter[current]
    for i in range(2, len(string)):
        if counter[current - (i - current)] > (right - i) > 0:
            counter[i] = counter[current - (i - current)]
        else:
            value = 0
            delta = 1
            while (i - delta) >= 0 and (i + delta) < len(string) and string[i + delta] == string[i - delta]:
                value += 1
                delta += 1
            current = i
            counter[current] = value
            right = current + counter[current]
    
    real_length = max(counter)
    center = counter.index(real_length)
    answer = string[center - real_length:center + real_length].replace(special_character, "")
    return answer
