import re

def convertNumStringToInt(value):
    numbersWrittenOut=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if value.isdigit():
        return str(value)
    else:
        return str(numbersWrittenOut.index(value))

def Trebuchet(file):
    calibrationValueTotal = 0

    with open(file) as fileData:
        contents = fileData.read().splitlines()
        for entry in contents:
            parse= re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', entry)
            total = convertNumStringToInt(parse[0]) + convertNumStringToInt(parse[-1])
            calibrationValueTotal+= int(total)
    print(calibrationValueTotal)

def main():
    sample_data = '/workspaces/adventOfCode2023/Day1/input.txt'
    Trebuchet(sample_data)

if __name__ == "__main__":
    main()