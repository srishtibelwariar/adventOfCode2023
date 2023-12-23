import re

def Trebuchet(file):
    calibrationValueTotal = 0
    with open(file) as fileData:
        contents = fileData.read().splitlines()
        for entry in contents:
            parse= re.findall(r'\d', entry)
            total = parse[0]+parse[-1]
            calibrationValueTotal+= int(total)
    print(calibrationValueTotal)

def main():
    sample_data = '/workspaces/adventOfCode2023/Day1/input.txt'
    Trebuchet(sample_data)

if __name__ == "__main__":
    main()