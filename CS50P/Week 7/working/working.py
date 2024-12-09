import re


def main():
    print(convert(input("Hours: ")))


def convert(t):
    if us_t := re.match(r"(\d{1,2}):?(\d{0,2})?\s*(am|pm)?\s*(?:(?:\w|[-])*)?\s?(\d{1,2}):?(\d{0,2})?\s*(am|pm)?", t, re.IGNORECASE):
        h1, min1, mer1, h2, min2, mer2 = us_t.group(1), us_t.group(2), us_t.group(3).lower(), us_t.group(4), us_t.group(5), us_t.group(6).lower()
        try:
            h1 = int(h1)
        except:
            h1 = 0
        if mer1 == "pm":
            h1 += 12

        try:
            h2 = int(h2)
        except:
            h2 = 0
        if mer2 == "pm":
            h2 += 12

        if h1 > 12 and mer1 == 'am':
            h1 -= 12
        
        if h2 > 12 and mer2 == 'am':
            h2 -= 12

        if h1 > 24 and mer1 == 'pm':
            h1 -= 12

        if h2 > 24 and mer2 == 'pm':
            h2 -= 12

        try:
            min1 = int(min1)
        except:
            min1 = 0

        try:
            min2 = int(min2)
        except:
            min2 = 0

        if min1 >= 60:
            added_h = min1 // 60
            h1 += added_h
            min1 -= added_h * 60

        if min2 >= 60:
            added_h = min2 // 60
            h2 += added_h
            min2 -= added_h * 60

        if h1 < 10:
            h1 = f"0{h1}"
        else:
            h1 = f"{h1}"

        if h2 < 10:
            h2 = f"0{h2}"
        else:
            h2 = f"{h2}"

        if min1 < 10:
            min1 = f"0{min1}"
        else:
            min1 = f"{min1}"

        if min2 < 10:
            min2 = f"0{min2}"
        else:
            min2 = f"{min2}"

        return f"{h1}:{min1} to {h2}:{min2}"
    else:
        return None

if __name__ == "__main__":
    main()
