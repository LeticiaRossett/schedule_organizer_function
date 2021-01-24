#!/usr/bin/env python
# coding: utf-8
Assignment 01- Python for Data Science
Student: Leticia Rossett 
Instructor: Dr. Zhiyun Li 
Description: Design a function to help organize multiple meetings during a day 
Date: 01/22/2021
# In[ ]:


# Display error message
def errorMessage():
    print("The meeting hours should be in the format below: ")
    print("Ex: [start_time_1, end_time_1], [start_time_2, end_time_2], [start_time_3, end_time_3]")

# Find the minimum amount of rooms needed for multiple meetings
def findMinRooms(*args):
    if len(args) == 0:
        print("Please input meeting times.")
        errorMessage()
        return 
    
    meetings =  []
    numOfRooms = 0    
    # Check if the input is valid, then add it to a list called 'meetings'
    for i in range(len(args)):
        try:
            if type(args[i]) != list:
                print("Please, type the hours between square braquets, ex: [start_time, end_time]")
                return
            if len(args[i]) > 2:
                print("\nError! The input: " , args[i], " has too many hours.")
                errorMessage()
                return
            else:
                if 0.0 <= float(args[i][0]) <= 24.0 and 0.0 <= float(args[i][1]) <= 24.0: 
                    if float(args[i][0]) < float(args[i][1]):
                        meetings.append(args[i])
                    else:
                        print("\nLooks like your ", args[i] ," meeting time is backwards!")
                        print("Start time of meeting should be smaller than end time.")
                        return
                else:
                    print("\nError! Input " , args[i] , " not valid.")
                    print("The meeting hours must be between 0.0 and 24.0")
                    return  
            
        except TypeError:
            errorMessage()
            return 
        
        except ValueError:
            print("Please, input decimal numbers for hours. \n")
            errorMessage()
            return 
        
        except IndexError:
            print("Please, input the time slot with start and end hour. \n")
            errorMessage()
            return  

    
    # Sort list to know which meeting start first
    meetings = sorted(meetings, key = lambda x:x[0])
    
    # First meeting has a room for sure, so it is added to "room" list 
    room = [meetings[0]]
    
    # Remove first meeting from the list of meetings, because it already has a room  
    del meetings[0]
    
    for j in range(len(meetings)):      
        
        for i in range(len(room)):
            
            #Sort list of rooms to get the lowest end hour as index 0
            room = sorted(room, key = lambda x:x[1])
    
            # Meetings time conflict
            if len(meetings) != 0 and meetings[0][0] < room[0][1]:
                room.append(meetings[0])
                del meetings[0]     
            
            # No meetings time conflict
            if len(meetings) != 0 and meetings[0][0] >= room[0][1]:
                del room[0]
                room.append(meetings[0])
                del meetings[0]
            
    numOfRooms = len(room)
    return numOfRooms

