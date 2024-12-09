#!/bin/python


import sqlite3


con = sqlite3.connect("mcq.db")


cur = con.cursor()

answers = [
"interface between the hardware and application programs",
"collection of programs that manages hardware resources",
"system service provider to the application programs",
"all of the mentioned - correct",

"to provide the interface between the API and application program",
"to handle the files in the operating system",
"to get and execute the next user-specified command - correct",
"none of the mentioned",

"Priority",
"Round Robin",
"Shortest Job First",
"All of the mentioned - correct",

"Library",
"System calls - correct",
"Assembly instructions",
"API",

"multiprogramming operating systems - correct",
"larger memory sized systems",
"multiprocessor systems",
"none of the mentioned",

"kernel remains in the memory during the entire computer session",
"kernel is made of various modules which can not be loaded in running operating system - correct",
"kernel is the first part of the operating system to load into memory during booting",
"kernel is the program that constitutes the central core of the operating system",

"lack of paper in printer",
"connection failure in the network",
"power failure",
"all of the mentioned - correct",

"either low or high memory (depending on the location of interrupt vector) - correct",
"in the low memory",
"in the high memory",
"none of the mentioned",

"new file",
"another running process",
"log file - correct",
"none of the mentioned",

"RTLinux",
"Palm OS - b",
"QNX",
"VxWorks",

"monolithic kernel with modules",
"microkernel",
"monolithic kernel",
"hybrid kernel - correct",

"open files",
"pending alarms, signals, and signal handlers",
"address space and global variables",
"all of the mentioned - correct",

"Suspended state",
"Terminated state",
"Ready state - correct",
"Blocked state",

"Normally or abnormally - correct",
"Abnormally",
"Normally",
"None of the mentioned",

"Terminated state",
"Suspended state",
"Running state",
"Ready state - correct",

"stays in the memory always",
"never enters the memory space",
"comes and goes as needed - correct",
"is not easily accessible",

"assigning ready processes to waiting queue",
"assigning running processes to blocked queue",
"assigning ready processes to CPU - correct",
"all of the mentioned",

"operating systems",
"multiprocessor systems",
"time sharing systems - correct",
"multiprogramming systems",

"every time a resource request is made at fixed time intervals - correct",
"at fixed time intervals",
"every time a resource request is made",
"none of the mentioned",

"operating system",
"resources",
"system storage state",
"resource allocation state - correct",
]


# TOPICS = (
#            "Operating System MCQ",
#            "Computer Networks MCQ",
#            "Data Structures & Algorithms MCQ",
#            "Design and Analysis of Algorithms MCQ",
#            "Computer Architecture MCQ",
#            "Database Management System MCQ",
#            "Software Engineering MCQ",
#            "Software Architecture & Design MCQ",
#            "Microprocessor MCQ",
#            "Compilers MCQ",
#            "Discrete Mathematics MCQ", 
#            "Automata Theory / Theory of Computation MCQ", 
#            "Unix MCQ",
#            "Computer Fundamentals MCQ", 
#            "Cryptography & Network Security MCQ", 
#            "Cyber Security MCQ", 
#            "Cloud Computing MCQ", 
#            "Computer Graphics MCQ",         
#           "Web Technology MCQ",
#        )

#for topic in TOPICS:
#    cur.execute("INSERT INTO topics (name) VALUES (?);", (topic,))


res = cur.execute("SELECT id FROM questions;")
ids = [id_[0] for id_ in res.fetchall()]

#for id_ in ids:
#    cur.execute("INSERT INTO topic_questions(topic_id, question_id) VALUES (?, ?)", (1, id_))

answer_index = 0

for id_ in ids:
    i = 0
    while i < 4:
        correct = False
        if answers[answer_index].endswith(" - correct"):
            correct = True
            answers[answer_index] = answers[answer_index].replace(" - correct", "")
        cur.execute("INSERT INTO possible_answers (text) VALUES (?);", (answers[answer_index], ))
        con.commit()
        res = cur.execute("SELECT id FROM possible_answers WHERE text = ?;", (answers[answer_index], ))
        t_id = res.fetchone()[0]
        if correct == True:
            print("True-x")
            con.execute("INSERT INTO answers (question_id, possible_answer_id, is_correct) VALUES (?, ?, TRUE);", (id_, t_id))
        else:
            con.execute("INSERT INTO answers (question_id, possible_answer_id) VALUES (?, ?);", (id_, t_id))
        con.commit()
        answer_index += 1
        i += 1

con.commit()


