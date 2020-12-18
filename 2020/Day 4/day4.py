# Advent of Code 2020 - Day 4: Passport Processing

# Part 1, read passport records from file (full empty line between, may span multiple lines). validate that each record contains the 7 required fields, find number of valid records
# Requires: byr (birth year), iyr (issue year), eyr (expiration year), hgt (height), hcl (hair color), ecl (eye color), pid (passport id)
# technically the cid (country id) is also required, but lets ignore that as Santa has his North Pole credentials, not his passport, which contains all but the country id

combinedData = []

recordString = ''
with open('input.txt', 'r') as file:
	for line in file:
		if line == '\n':
			recordString = recordString.rstrip()
			recordString = recordString.replace('\n', ' ')
			combinedData.append(recordString)
			recordString = ''
		else:
			recordString = recordString + line

records = []

for string in combinedData:
	record = {}

	for data in string.split(' '):
		if ':' in data:
			key, value = data.split(':', 1)
			record[key] = value

	records.append(record)

validCount = 0

for record in records:
	if (len(record.keys()) == 8) or (len(record.keys()) == 7 and not 'cid' in record.keys()):
		validCount += 1

print('Part 1: There were ' + str(validCount) + ' valid records')

# Part 2, need to apply some validation on the 7 required fields (country id is still ignored), find number of valid records containing enough fields and validated fields

import re

def isYearValid(year, length, lower, upper):
	return len(year) == length and int(year) >= lower and int(year) <= upper

def isBirthYearValid(year):
	return isYearValid(year, 4, 1920, 2020)

def isIssueYearValid(year):
	return isYearValid(year, 4, 2010, 2020)

def isExpirationYearValid(year):
	return isYearValid(year, 4, 2020, 2030)

def isDistanceValid(string): # string is of format numberunit ex: 60in is 60 inches
	lower = {'cm': 150, 'in': 59}
	upper = {'cm': 193, 'in': 76}

	pattern = '(\\d+)(cm|in)'
	groups = re.match(pattern, string)

	if groups is not None:
		value = int(groups.group(1))
		return value >= lower[groups.group(2)] and value <= upper[groups.group(2)]
	else:
		return False

def isHairColorValid(string):
	return True if re.search('#[0-9a-f]{6}', string) else False

def isEyeColorValid(string):
	validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	return True if string in validEyeColors else False

validCount = 0

for record in records:
	if (len(record.keys()) == 8) or (len(record.keys()) == 7 and not 'cid' in record.keys()):
		validBirthYear = isBirthYearValid(record['byr'])
		validIssueYear = isIssueYearValid(record['iyr'])
		validExpirationYear = isExpirationYearValid(record['eyr'])
		validHeight = isDistanceValid(record['hgt'])
		validHairColor = isHairColorValid(record['hcl'])
		validEyeColor = isEyeColorValid(record['ecl'])
		validPassportID = len(record['pid']) == 9

		if validBirthYear and validIssueYear and validExpirationYear and validHeight and validHairColor and validEyeColor and validPassportID:
			validCount += 1
		else:
			print(str(record), validBirthYear, validIssueYear, validExpirationYear, validHeight, validHairColor, validEyeColor, validPassportID)

print('Part 2: There were ' + str(validCount) + ' valid records')
