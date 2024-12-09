def main() :
    text = input()
    text_new = convert(text)
    print(text_new)


def convert(text) :
    #words = text.split()
    
    #for i in range(len(words)) :
    #    if words[i] == ':(' :
    #        words[i] = '\U0001F641'
    #    elif words[i] == ':)' :
    #        words[i] = '\U0001F642'

    #text = ' '.join(words)

    return text.replace(':)', '\U0001F642').replace(':(', '\U0001F641')


main()
