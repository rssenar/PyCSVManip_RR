
'''
0 = NAME
1 = ADDRESS
2 = CITY
3 = STATE
4 = ZIP
5 = RES_PHONE#
6 = EMAIL_ADDRESS
7 = VIN
8 = YEAR
9 = MAKE
10 = MODEL
11 = DEL_DATE
12 = RO_DATE
'''
import csv
# ---------------------------------------------
CSVFilesHaveHeaderRow = True # True or False if input files include a header row
InitalPrevLineStatus = True
# ---------------------------------------------
NAME = 0
ADDRESS = 1 
CITY = 2
STATE = 3
ZIP = 4

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
InputFile = "/Users/rssenar/Desktop/BillLukeSalesService.csv"
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
FirstLine = True
PrevLineStatus = True

for line in Input:
	if CSVFilesHaveHeaderRow and FirstLine:
		FirstLine = False
	elif (line[NAME] != '' and line[ADDRESS] != '' and line[CITY] != '' and line[STATE] != '' and line[ZIP] != '') and (InitalPrevLineStatus and PrevLineStatus):
		Prevline = line
		PrevLineStatus = False
	
	elif line[NAME] != '' and line[ADDRESS] != '' and line[CITY] != '' and line[STATE] != '' and line[ZIP] != '':
		OutputClean.writerow(Prevline)
		Prevline = line
		
	elif line[NAME] == '' and line[ADDRESS] != '' and line[CITY] == '' and line[STATE] == '' and line[ZIP] == '':
		Prevline[ADDRESS] = Prevline[ADDRESS] + line[ADDRESS]
		OutputClean.writerow(Prevline)
		
	else:
		pass
# ---------------------------------------------
InputFile.close()
CleanOutput.close()
