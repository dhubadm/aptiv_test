###BUILD FILE HANDLER SCRIPT V1.0###
import re,datetime,os,glob,sys
from feeder import *

###FUNCTION TO CONVERT ASCII VALUES TO DECIMAL###
def ascii2decimal():
    #print("[DEBUG] Executing >>> ", sys._getframe().f_code.co_name)
    checkstr=""
    for val in part_number:
        checkstr = checkstr + str(ord(val)) + ","
    checkstr = checkstr[:-1]
    checkstr = "{" + checkstr + "}"
    return checkstr

###FUNCTION TO SEARCH AND REPLACE PART_NUMBERS IN FILE###
def replace_build(checkstr,module):
    global filedata
    #print("[DEBUG] Executing >>> ", sys._getframe().f_code.co_name)
    if (re.search('F195', line_number)):
        filedata = re.sub(r"(" + module + "\s.*)({.*})(.*("+ line_number +"))", r'\g<1>' + '{0,'+ part_number +'}' + r'\g<3>', filedata)
    else:
        #filedata = re.sub(r"(" + module + "\s.*)({.*})(.*("+ line_number +"))", r'\g<1>' + checkstr + r'\g<3>', filedata)
        filedata = re.sub(r"(" + module + "\s.*)({.*})(.*("+ line_number +")) (.*) (-)", r'\g<1>' + checkstr + r'\g<3> ' + part_number, filedata)

###FUNCTION TO SEARCH AND REPLACE <SW_BUILD_YEAR|SW_BUILD_WEEK|SW_BUILD_PATCH> VALUES IN FILE###
def replace_swbuild():
    global filedata
    print("[DEBUG] Executing >>> ", sys._getframe().f_code.co_name)
    year = hex(int(datetime.date.today().strftime("%y")))
    week = hex(int(datetime.date.today().strftime("%V"))).upper()
    Dict = {'SW_BUILD_YEAR': year, 'SW_BUILD_WEEK': week, 'SW_BUILD_PATCH': PATCH}
    for renew,value in Dict.items():
        filedata = re.sub(r"("+ renew +"\s*)(.*)", r'\g<1>' + value, filedata)

###FUNCTION TO SEARCH AND REPLACE <SW_EBOM_PN|EBOM_ECU_PN|EBOM_ASSEMBLY_PN> VALUES IN FILE###
def replace_l2module():
    global filedata
    print("[DEBUG] Executing >>> ", sys._getframe().f_code.co_name)
    l2module = ["SW_EBOM_PN","EBOM_ECU_PN","EBOM_ASSEMBLY_PN"]
    checkstrU=""
    for vals in eval(BUILD)[module]['F132']:
        checkstrU = checkstrU + str(ord(vals)) + "U,"        
    checkstrU = checkstrU[:-1]
    checkstrU = "{" + checkstrU + "}"
    for l2 in l2module:
        filedata = re.sub(r"(" + l2 + "\s.*)({.*})", r'\g<1>' + checkstrU, filedata)

###FUNCTION TO SEARCH AND REPLACE BST TOOL VERSION VALUES IN FILE###
def replace_fd23():
    global filedata
    print("[DEBUG] Executing >>> ", sys._getframe().f_code.co_name)
    arrlist = ["_MAJOR_VERSION","_MINOR_VERSION","_FIELD_VERSION","_WRAPPER_VERSION"]
    for name,vers in tool_version.items():
        version=vers.split('.')
        for arr in arrlist:
            filedata = re.sub(r'('+ name + arr + '\s.*8\))(.\d*)', r'\g<1>' + version[arrlist.index(arr)], filedata)

###FUNCTION TO REPLACE <FD22> MODULE VERSION VALUES IN FILE###
def replace_fd22():
    global filedata
    print("[DEBUG] Executing >>> ", sys._getframe().f_code.co_name)
    arrlist = ["_SWC_MAJOR_VERSION","_SWC_MINOR_VERSION","_SWC_FIELD_VERSION"]
    for name,vers in fd22.items():
        version=vers.split('.')
        for arr in arrlist:
            if len(version) != 1:
                filedata = re.sub(r'(FMV_'+ name + arr +'\s.*6\))(.\d*)', r'\g<1>' + version[arrlist.index(arr)], filedata)
            else:
                filedata = re.sub(r'(FMV_'+ name +'_SWC_VERSION\s.*6\))(.\d*)', r'\g<1>' + version[0], filedata)

###FUNCTION TO REPLACE <FD02> MODULE VERSION VALUES FROM DBC FILES###
def replace_fd02():
    global filedata
    print("[DEBUG] Executing >>> ", sys._getframe().f_code.co_name)
    for file_name in glob.glob(dbc_filepath + 'P' + BUILD + '*FDCAN*.dbc'): 
        with open(file_name, 'r') as file :
            FDCAN = file.read() 
            canvalue = "CAN3" if 'FDCAN3' in os.path.split(file_name)[1] else "CAN14"
            fdcanlist = {
            'BA_DEF_DEF_ "VersionYear"' : "FD02_FD_" + canvalue + "_DBC_CalYear",
            'BA_DEF_DEF_ "VersionWeek"' : "FD02_FD_" + canvalue + "_DBC_CalWeek",
            'BA_DEF_DEF_ "Version"' : "FD02_FD_" + canvalue + "_DBC_Version"
            }
            for list1,list2 in fdcanlist.items():
                result = re.findall('(' + list1 + ' )(.\d*)', FDCAN)
                filedata = re.sub(r'(' + list2 + '.* )(\d+)(U.*)', r'\g<1>' + result[0][1] + r'\g<3>', filedata)
            
    for file_name in glob.glob(dbc_filepath + 'CADM_CAN_SB*.dbc'):     
        with open(file_name, 'r') as file :
            FDCANSB = file.read()  
            result1 = re.findall('(BA_ "GenRevisionDate".*)(.*)("(.*)")', FDCANSB)
            result2 = re.findall('(BA_ "VersionNumber_B".*)(.*)("(.*)")', FDCANSB)
            for datevalue in result1[0][3].split(" "):
                if datevalue.isalnum() and not datevalue.isalpha() and not datevalue.isdigit():
                    result = result1[0][3].replace(datevalue,re.sub("\D", "", datevalue))
            sbvalue = "SB1" if 'SB1' in os.path.split(file_name)[1] else "SB2"
            print(result1[0][3])
            filedata = re.sub(r'(FD02_FD_CAN'+ sbvalue +'_DBC_CalYear.* )(\d+)(U.*)', r'\g<1>' + str(datetime.datetime.strptime(result, '%B %d %Y').year)[-2:] + r'\g<3>', filedata)
            filedata = re.sub(r'(FD02_FD_CAN'+ sbvalue +'_DBC_CalWeek.* )(\d+)(U.*\/\*)(.*)', r'\g<1>' + datetime.datetime.strptime(result, '%B %d %Y').date().strftime("%V") + r'\g<3>' + " " + str(result1[0][3]) + " */" , filedata)
            filedata = re.sub(r'(FD02_FD_CAN'+ sbvalue +'_DBC_Version.* )(\d+)(U.*\/\*)(.*)', r'\g<1>' + str(int(result2[0][3].replace('_',''), 16)) + r'\g<3>' + " 0x" + str(result2[0][3].replace('_','')) + " */", filedata)
   
###STARTING POINT - TO READ AND VALIDATE VARIABLES###
with open(infile, 'r') as file :
    filedata = file.read()          
    if BUILD in ('DT','WL75','WL74','WS'):
        print("\n[INFO] BUILD triggered: " + BUILD)
        replace_swbuild()
        replace_fd23()
        replace_fd22()
        replace_fd02()
        for module in eval(BUILD):
            if 'L2' in module: 
                replace_l2module()
            for line_number,part_number in eval(BUILD)[str(module)].items():
                print("[INFO] Module Name: %s\n[INFO] Line Number: %s\n[INFO] Part Number: %s\n" %  (module ,line_number,part_number))
                conv = ascii2decimal()
                if 'WL74' in BUILD:
                    phev =  module.replace(BUILD, BUILD + "_PHEV" )
                    print("[INFO] Module Name: %s\n[INFO] Line Number: %s\n[INFO] Part Number: %s\n" %  (phev ,line_number,part_number))
                    replace_build(conv,phev)
                replace_build(conv,module)        
    else:
        print("[ERROR]BUILD value not specified OR incorrect!\n[INFO]Expected BUILD values - WS | DT | WL75 | WL74")

#file.close()
with open(outfile, 'w') as file:
    file.write(filedata)