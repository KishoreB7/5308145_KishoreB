def timeConversion(s):
    hour = int(s[:2])
    suffix = s[-2:]
    rest = s[2:8]
    if suffix == 'AM' and hour == 12:
        converted_hour = '00'
    elif suffix == 'PM' and hour != 12:
        converted_hour = f"{hour + 12:02d}"
    else:
        converted_hour = f"{hour:02d}"
    return converted_hour + rest

if __name__ == '__main__':
    s = input().strip()
    print(timeConversion(s))
