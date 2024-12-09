#!/bin/python


from bs4 import BeautifulSoup
from random import randint
import argparse
import requests


project: str = None


def main() -> None:
    """ Retrieve a project from the CS50P projects list """
    
    # Get the CLA
    arg_parser = argparse.ArgumentParser(description="How to choose the project from the list")
    arg_parser.add_argument("-r", action="store_true", help="Chose a random project from the list of projects")
    args = arg_parser.parse_args()
    
    # Get the project based on user preference
    # 1. Random
    if args.r:
        global project
        project = get_rand_project()
    
    # 2. A list of first -n projects
    # TODO

    # Append the project to a list of projects
    with open("project.txt", "a") as fhand:
        fhand.write(project)


def get_rand_project() -> str:
    """ Returns a random project from the list of projects """
    
    p_list = get_projects_list()

    # Get the project from the list and ckeck if it is in the output file, if not return it else get another
    while True:
        p_index = randint(0, len(p_list) - 1)
        p_name = get_project_name(p_list[p_index])
        p_video_link = get_project_v_link(p_list[p_index])
        if found := not_found(f"{p_name}\n{p_video_link}"):
            return f"{p_name}\n{p_video_link}\n\n"
        else:
            pass

def get_projects_list():
    """ Returns a list of all th projects from the CS50P Gallery """

    r = requests.get("https://cs50.harvard.edu/python/2022/gallery/")
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all("div", class_="project")


def get_project_name(p) -> str:
    """ Returns the name of the project that was passed to the function """

    return p.find("p", class_="mb-0").text.strip()


def get_project_v_link(p) -> str:
    """ Returns the link for the video description of the provided project """

    return p.find("a", class_="font-weight-bold").get("href")


def not_found(string) -> bool:
    with open("project.txt", "r") as fhand:
        if string in fhand:
            return False
        return True


if __name__ == "__main__":
    main()
