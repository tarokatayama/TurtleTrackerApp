#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Taro Katayama (taro.katayama@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#Copy and paste one line of data as a variable
lineString ="20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

#split lineString into a list of items
lineData= lineString.split()

#Assign variables to items in the lineData list
record_id= lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

#print information to the user
print(f'Record {record_id} indicates Sara was seen at {obs_lat}N, {obs_lon}W on {obs_date}')
