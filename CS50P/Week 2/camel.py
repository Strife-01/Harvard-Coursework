def main() :
    camel_name = input("camelCase: ")
    snake = []
    for letter in camel_name :
        if letter.islower() : snake.append(letter)
        else : snake.append(f"_{letter.lower()}")
    snake_name = "".join(snake)
    print(f"snake_case: {snake_name}")


main()
