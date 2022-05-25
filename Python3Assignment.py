from datetime import date, datetime, timedelta
from xml.etree import ElementTree as et
import json
import csv

def csv_parser():
    infile1 = 'inputfiles\Jmeter_log1.jtl'
    infile2 = 'inputfiles\Jmeter_log2.jtl'
    with open(infile1, 'r') as f:
        csvreaderobject = csv.reader(f)
        for row in csvreaderobject:
            if row[3] != 200:
                print(row[2]+"--"+row[3]+"--"+row[4]+"--"+row[8]+"--"+row[1])

def json_parser(x):
    filename = 'inputfiles/test_payload.json'
    resultfilename = 'outputfiles/test_payload_result.json'
    with open(filename, 'r+') as file:
     rjson = open(resultfilename, 'w')
    # dictionary used for loading input data
     file_data = json.load(file)
     new_fdata = file_data
     if x in file_data.keys():
        del new_fdata[x]
    json.dump(new_fdata, rjson, indent = 4)
    file.close()
    rjson.close()

def xml_parser(x,y):
    today = date.today()
    departdate = datetime.today() + timedelta(days=x)
    returndate = datetime.today() + timedelta(days=y)
    tree = et.parse('inputfiles/test_payload1.xml')
    tree.find('.//DEPART').text = str(departdate)
    tree.find('.//RETURN').text = str(returndate)
    tree.write('outputfiles/test_payload_result.xml')

if ( __name__ == "__main__"):
    csv_parser()
    xml_parser(1, 1)
    json_parser('outParams')