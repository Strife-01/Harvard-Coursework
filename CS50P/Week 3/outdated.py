import re
import string


MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main() :
    # get the date in an array in the [yyyy, mm, dd] format
    date = get_date()

    # ad 0 next to the mm or/and dd if necessary
    if len(date[1]) == 1 : date[1] = '0' + date[1]
    if len(date[2]) == 1 : date[2] = '0' + date[2]
    
    # print the date
    date_s = "-".join(date)
    print(date_s)


def get_date() :
    while True :
        date = input("Date: ").title()
        # check and get the input only in the 2 accepted formats
        format_1 = re.fullmatch("\d{1,2}\s*/?\s*\d{1,2}\s*/?\s*\d+", date)
        format_2 = re.fullmatch("[a-zA-Z]+\s*\d{1,2}\s*,?\s*\d+", date)
        
        # create a list with the year month and day and return it
        try :
            comp = format_1.string.split('/')
            return [comp[2], comp[0], comp[1]]
        except : pass
        try : 
            comp = format_2.string.translate(str.maketrans('', '', string.punctuation)).split()
        except : pass
        else :
            if len(comp) == 3 and comp[0] in MONTHS : return [comp[2], str(MONTHS.index(comp[0]) + 1), comp[1]]


main()
