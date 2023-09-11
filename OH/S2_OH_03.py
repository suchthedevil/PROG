def zisti1(text):
    slova = list(map(str,text.split(", ")))
    sum_final = 0
    for s in range(len(slova[0])-2):
        sum_final += abs(ord(slova[0].lower()[s])-ord(slova[0].lower()[s+1]))
    count = -1
    for i in slova:
        sum_word = 0
        count += 1
        for j in range(len(i)-1):
            sum_word += abs(ord(i.lower()[j])-ord(i.lower()[j+1]))-1
        if sum_word <= sum_final:
            sum_final = sum_word
            word_final = i
    print(f"{word_final} - {sum_final}")

zisti1("jednotka, Prepadnem, string, GBAS, abeceda")
zisti1("Adolf, Gregor, Filip, Natalia")

#alternativa s funkciami ktore sme prebrali

def zisti2(text):
    sum_final = 0
    for i in range(len(text)):
        if text[i] == ",":
            word = text[0:i]
            for j in range(len(word)-1):
                    sum_final += abs(ord(word.lower()[j]) - ord(word.lower()[j+1]))-1
    pocet = 0
    text += ","
    for i in text:
        if i == ",":
            pocet += 1        
    while pocet:
        sum_word = 0
        for i in range(len(text)):
            if text[i] == ",":
                word = text[0:i]
                for j in range(len(word)-1):
                    sum_word += abs(ord(word.lower()[j]) - ord(word.lower()[j+1]))-1
                if sum_word <= sum_final:
                    word_final = word
                    sum_final = sum_word
                break
        text = text[i+2:]
        pocet -= 1
    print(f"{word_final} - {sum_final}")  

zisti2("jednotka, Prepadnem, string, GBAS, abeceda")
zisti2("Adolf, Gregor, Filip, Natalia")


#s preberanymi funkciami ale este lepsie

def zisti3(text):
    text += ","
    min, val = 0, 0
    word = text[:text.find(",")]
    for i in range(len(word)-1):
        min += abs(ord(word.lower()[i])-ord(word.lower()[i+1]))-1
        final_word = word
    while text:
        if "," not in text:
            break
        else:
            word = text[:text.find(",")]
            text = text[text.find(",")+2:]
            for i in range(len(word)-1):
                val += abs(ord(word.lower()[i])-ord(word.lower()[i+1]))-1
            if val < min:
                min = val
                final_word = word
        val = 0
    print(f"{final_word}-{min}")          

zisti3("jednotka, Prepadnem, string, GBAS, abeceda")
zisti3("Adolf, Gregor, Filip, Natalia")