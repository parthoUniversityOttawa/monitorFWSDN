import csv,json
import os


def getThoughput():
	csvfile = "result/output.csv"
	data = {}
	bigData = {}
	i=0
	with open(csvfile) as csvFile:
		csvReader = csv.DictReader(csvFile)
		for rows in csvReader:
			data ["Switch"] = rows ["Switch"]
			data ["SRC_IP"] = rows ["SRC_IP"]
			data ["DST_IP"] = rows ["DST_IP"]
			data ["Thoughput"] = rows ["Thoughput "]
			bigData["flow"+str(i)] =data
			data = {}
			i = i+1	
	
	return json.dumps(bigData,sort_keys=True, indent=10)

def getPacketLoss():
	csvfile = "result/output.csv"
	data = {}
	bigData = {}
	i=0
	with open(csvfile) as csvFile:
		csvReader = csv.DictReader(csvFile)
		for rows in csvReader:
			data ["Switch"] = rows ["Switch"]
			data ["SRC_IP"] = rows ["SRC_IP"]
			data ["DST_IP"] = rows ["DST_IP"]
			data ["Packet_Count"] = rows ["Packet_Count"]
			data ["Byte_Count"] = rows ["Byte_Count"]
			data ["Delta_Packet_Count"] = rows ["Delta_Packet_Count"]
			data ["Delta_Byte_Count"] = rows ["Delta_Byte_Count"]
			bigData["flow"+str(i)] =data
			data = {}
			i = i+1	
	
	return json.dumps(bigData,sort_keys=True, indent=10)

def getDelay():
	csvfile = "result/delay.csv"
	data = {}
	bigData = {}
	i=0
	with open(csvfile) as csvFile:
		csvReader = csv.DictReader(csvFile)
		for rows in csvReader:
			print (rows["Delay"])
			data ["Src/Initiator"] = rows ["Src/Initiator"]
			data ["Dst/Switch"] = rows ["Dst/Switch"]
			data ["Delay"] = rows ["Delay"]
			bigData["flow"+str(i)] =data
			data = {}
			i = i+1	
	
	return json.dumps(bigData,sort_keys=True, indent=10)

	
#data[id] = rows
#with open(jsonfile,'w') as jsonwrite:
#	jsonwrite.write(json.dumps(bigData))
