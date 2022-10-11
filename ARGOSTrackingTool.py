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

#Create a varaiable point to the data file
file_name = 'data/raw/Sara.txt'

#Create a file object from the filename
file_object = open(file = file_name, mode='r')

#Read contents of file into a list
lineString = file_object.readline()


#Extract one data line into a variable
<<<<<<< HEAD
<<<<<<< HEAD
while lineString:

    #Check to see if the lineString is a data line
    if lineString[0]=='#' or lineString[0] == 'u':
        lineString = file_object.readline()
        continue
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

    #Move to the next line in the file
    lineString = file_object.readline()
    
#close the file object
file_object.close()
=======
lineString = line_list[200]

=======
lineString = line_list[200]

>>>>>>> parent of dc53abf (task 4a)
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
<<<<<<< HEAD
>>>>>>> parent of dc53abf (task 4a)
=======
>>>>>>> parent of dc53abf (task 4a)
