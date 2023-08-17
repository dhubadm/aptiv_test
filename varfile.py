
#infile = "C:/Users/aksha/OneDrive/Documents/naveen_files/File_Data.txt"
#outfile = "C:/Users/aksha/OneDrive/Documents/naveen_files/File_Data2.txt"
#dbc_filepath="C:/Users/aksha/OneDrive/Documents/naveen_files/"
infile = "File_Data.txt"
outfile = "File_Data2.txt"
dbc_filepath="naveen_files/"

#Expected <build> values >>> DT|WL75|WL74|WS
BUILD='WL74' 
PATCH='0x05'
VERSION="efhbjhakjfhkjfh"

#BUILD module variables    
class declare_partnumbers():
    L1_F132="0383648AEF909093494"
    L1_F133="99999AFS99"
    L1_F194="202020YZ"
    L1_F195="20"
    L2_F132="9093494"
    L2_F133="8363721"
    L2_F194="202020YZ"
    L2_F195="38"
    L1P_F132="0383609093494"
    L1P_F133="e7878272e"
    L1P_F194="20dd2020YZ"
    L1P_F195="08"

#Apptiv BST tool version variables
tool_version = {
    'TRACKER_360' : "10.15.46.0",
    'SATA' : "6.6.3.28",
    'SPP_OTP' : "16.27.0.8",
    'VSE' : "18.0.0.0",
}

#FD22 module variables (JIRA)
fd22 = {
    'ADAPTIVE_CRUISE_CONTROL' : "3.1.0",
    'COLLISION_AVOIDANCE' : "36.0.2",
    'INHIBIT_MANAGER' : "2.1.0",
    'HMI' : "1.2.1",    
	'LATERAL_CONTROL' : "2754",
	'SIDE_FEATURES' : "2772",
	'INPUT_WRAPPER' : '1117',
	'OUTPUT_WRAPPER' : '325',
	'VEHICLE_STATUS' : '1213',
	'SAF' : "1921"
}
