import csv
from tqdm import tqdm
# ---------------------------------------------
CSVFilesHaveHeaderRow = True
InitalPrevLineStatus = True
# ---------------------------------------------
NAME = 0
ADDRESS = 1 
CITY = 2
STATE = 3
ZIP = 4
RES_PHONE = 5
EMAIL_ADDRESS = 6
VIN = 7
YEAR = 8
MAKE = 9
MODEL = 10
DEL_DATE = 11
RO_DATE = 12

HeaderRow = [\
	'NAME',\
	'ADDRESS',\
	'CITY',\
	'STATE',\
	'ZIP',\
	'RES_PHONE#',\
	'EMAIL_ADDRESS',\
	'VIN',\
	'YEAR',\
	'MAKE',\
	'MODEL',\
	'DEL_DATE',\
	'RO_DATE'\
	]
# ---------------------------------------------
InputFileName = input("Enter Suppression File Name : ")
InputFile = "/Users/rssenar/Desktop/" + InputFileName + ".csv"
TotalRows = input("Enter Total Rows : ")

CleanOutput = "/Users/rssenar/Desktop/__CleanOutputMAIN.csv"
# ---------------------------------------------
InputFile = open(InputFile,'r')
CleanOutput = open(CleanOutput,'a')
# ---------------------------------------------
Input = csv.reader(InputFile)
OutputClean = csv.writer(CleanOutput)
# ---------------------------------------------
OutputClean.writerow(HeaderRow)
# ---------------------------------------------
CountDown = int(TotalRows)

FirstLine = True
IsFirstRow = True
Condition = True

while CountDown != 0:
	for line in tqdm(Input):
		if CSVFilesHaveHeaderRow and FirstLine:
			FirstLine = False
		elif IsFirstRow == True:
			Prevline = line
			IsFirstRow = False
		elif line[VIN] != '' and  Condition == True:
			OutputClean.writerow(Prevline)
			Prevline = line
		elif Condition == True:
			Prevline[NAME] = Prevline[NAME] + line[NAME]
			Prevline[ADDRESS] = Prevline[ADDRESS] + line[ADDRESS]
			Prevline[CITY] = Prevline[CITY] + line[CITY]
			Prevline[STATE] = Prevline[STATE] + line[STATE]
			Prevline[ZIP] = Prevline[ZIP] + line[ZIP]
			Prevline[RES_PHONE] = Prevline[RES_PHONE] + line[RES_PHONE]
			Prevline[EMAIL_ADDRESS] = Prevline[EMAIL_ADDRESS] + line[EMAIL_ADDRESS]
			Prevline[YEAR] = Prevline[YEAR] + line[YEAR]
			Prevline[MAKE] = Prevline[MAKE] + line[MAKE]
			Prevline[MODEL] = Prevline[MODEL] + line[MODEL]
			OutputClean.writerow(Prevline)
			Condition = False
		else:
			Prevline = line
			Condition = True
		CountDown-=1
OutputClean.writerow(line)
# ---------------------------------------------
InputFile.close()
CleanOutput.close()
