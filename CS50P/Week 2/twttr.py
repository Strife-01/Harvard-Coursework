def main() :
    ipt = input("Input: ")
    chars = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in ipt :
        if char.lower() not in vowels : chars.append(char)
        else : continue
    opt = "".join(chars)
    print(opt)


main()
