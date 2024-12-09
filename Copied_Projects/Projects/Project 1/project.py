#!/bin/python


from colorama import Fore, Style
from inputimeout import inputimeout
import os
import random
import sqlite3
import sys


# Time to answer a question
TIME = 10

# Nr of questions the user will receive
NR_QUESTIONS = 10

# Connect to the database
DATABASE = "mcq.db"
con = sqlite3.connect(f"{DATABASE}")
cur = con.cursor()


def main() -> None:
    """
    Questions and answers from
    https://www.sanfoundry.com/computer-science-questions-answers/
    """

    # Ask user to choose a topic
    clear_viewport()
    topic_id = choose_topic()
    if topic_id == None:
        sys.exit("No topics to choose from...")

    # Clear the screen
    clear_viewport()

    # Chose 10 questions ids randomly
    questions_ids = get_questions_ids(topic_id)
    # If no questions let the user know
    if questions_ids == None:
        sys.exit("No questions for this topic...")

    # Print questions one-by-one (query the database for the ids of the questions)
    answered_correctly, user_session = print_questions(questions_ids)

    # Clear viewport
    clear_viewport()

    # After no more questions print all the questions with their answers and show feedback to user
    # Green Correct
    # Red Wrong
    # Next to each anser mark a sign that the user picked them
    # Compute the grade as a float with 1 dec out of 10.0
    grade = answered_correctly * 10 / NR_QUESTIONS
    print(
        "--- You have got a score of",
        Fore.BLUE,
        f"{grade:.1f}",
        Style.RESET_ALL,
        "out of 10.0 ---\n",
    )
    print_summary(user_session)


def choose_topic() -> int:
    # Reprompt untill valid
    while True:
        # Get a list with options's ids
        options = print_topics()

        # If no topics return
        if len(options) < 1:
            return None

        # Ask the user for a choice
        choice = input("Choose a topic: ")

        # Check user's input
        try:
            # Convert choice to int
            choice = int(choice)
        except ValueError:
            # In case of not number
            print("\nPlease choose a valid option...")
            continue
        else:
            if choice not in options:
                # In case the number is not a valid option
                ("\nPlease choose a valid option...")
                continue
            else:
                # Print the choice selected by user
                # Get choice from database
                res = cur.execute("SELECT name FROM topics WHERE id = ?", (choice,))
                # Print choice
                topic = res.fetchone()[0]
                print(f"\nYou choose {topic}...\n")
                return choice


def print_topics() -> list:
    # Format char_num
    CHAR_NUM = 50
    OPTIONS = []

    # Title
    print("\n--- CHOOSE A TOPIC ---\n")
    print(f"--- You will receive {NR_QUESTIONS} random questions ---\n")

    # Topics

    # Query the database for the topics
    res = con.execute("SELECT * FROM topics;")
    topics = res.fetchall()

    # If no topics return
    if len(topics) < 1:
        return None

    # Print the topics
    for topic_id, topic_name in topics:
        print(format(f"{topic_name} ", f"*<{CHAR_NUM}s"), f"{topic_id}")
        OPTIONS.append(topic_id)

    # Emty new line
    print()

    # Return a list with all the options
    return OPTIONS


def get_questions_ids(topic_id) -> list:
    # Query the database for questions ids
    res = cur.execute(
        "SELECT question_id FROM topic_questions WHERE topic_id = ?", (topic_id,)
    )
    if questions_ids := res.fetchall():
        # Randomize the questions and return first 10 random questions
        questions = [question_id[0] for question_id in questions_ids]
        random.shuffle(questions)
        return questions[:NR_QUESTIONS]
    return None


def print_questions(questions_ids) -> tuple:
    # Nr of correc answers
    answered_correctly = 0

    # Store the questions and answers
    user_session = []

    # Parse the questions
    for q_id in questions_ids:
        # User Answer
        user_answer_id = None

        # Get the question text
        question = get_question(q_id)

        # Get the question answers
        res = cur.execute(
            "SELECT id, text FROM possible_answers WHERE id IN (SELECT possible_answer_id FROM answers WHERE question_id = ?);",
            (q_id,),
        )
        answers = res.fetchall()

        # Print question and possible answers
        print(f"Question:\n\n{question}\n")

        print("Possible answers:\n")
        for index, answer in enumerate(answers):
            print(f"{index + 1}. {answer[1]}\n")

        # Allow user 10 seconds to enter the answer
        try:
            answer = inputimeout(
                prompt=f"--- 10 Seconds starting NOW ---\n\nAnswer: ", timeout=TIME
            )
            # If answered check the answer
            # If the answer is not valid Clear the viewport and continue
            try:
                answer = int(answer)
            except:
                user_session.append((q_id, -1))
                freeze_1_sec()
                clear_viewport()
                continue
            else:
                if answer < 1 or answer > 4:
                    user_session.append((q_id, -1))
                    freeze_1_sec()
                    clear_viewport()
                    continue
                else:
                    # Correct the index and access the the answer id
                    answer -= 1
                    user_answer_id = answers[answer][0]
                    user_session.append((q_id, user_answer_id))

        # If they did not answered in time
        except Exception:
            user_session.append((q_id, -1))
            freeze_1_sec()
            clear_viewport()
            print("FAILED ANSWER")
            continue

        # If user provided a valid answer
        # Check answer
        res = cur.execute(
            "SELECT is_correct FROM answers WHERE question_id = ? AND possible_answer_id = ?",
            (q_id, user_answer_id),
        )
        is_correct = res.fetchone()[0]
        if is_correct == 1:
            answered_correctly += 1

        # Freeze the prompt for 1 second then clear the screen
        freeze_1_sec()
        clear_viewport()

    # Return how many questions were answered correctly
    return (answered_correctly, user_session)


def get_question(question_id) -> str:
    return cur.execute(
        "SELECT text FROM questions WHERE id = ?", (question_id,)
    ).fetchone()[0]


def print_summary(user_session) -> None:
    for session in user_session:
        # Get the question text
        res = cur.execute("SELECT text FROM questions WHERE id = ?;", (session[0],))
        question = res.fetchone()[0]
        print(f"\n\nQUESTION: {question}\n")

        # Get all the possible answers
        res = cur.execute(
            "SELECT possible_answer_id, is_correct FROM answers WHERE question_id = ?",
            (session[0],),
        )
        answers = res.fetchall()

        # Print the answers
        print("ANSWERS:")
        for answer in answers:
            res = cur.execute(
                "SELECT text FROM possible_answers WHERE id = ?", (answer[0],)
            )
            answer_text = res.fetchone()[0]

            # Color the answer green if correct else red
            if answer[1] == 1:
                answer_text = Fore.GREEN + answer_text
            else:
                answer_text = Fore.RED + answer_text

            # Print the answer
            print(f"{answer_text}", end="")

            # Reset the style of print
            print(Style.RESET_ALL, end="")

            # Let the user know if they chose that specific answer
            if session[1] != -1 and answer[0] == session[1]:
                print(" - YOUR CHOICE")
            else:
                print()


def clear_viewport() -> None:
    cmd = "clear"
    os.system(cmd)


def freeze_1_sec() -> None:
    cmd = "sleep 1"
    os.system(cmd)


if __name__ == "__main__":
    main()
