#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
lstTbl = []
objFile = None

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
   
    @staticmethod
    def format_data():
        """This function formats data that is input by the user"""
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        lstTbl.append(dicRow)
        IO.show_inventory(lstTbl)
    
    pass

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    @staticmethod
    def format_read(): 
        """This function reads information from a file"""
        text_file = open("cdInventory.txt")
        whole_thing = text_file.read()
        print(whole_thing)
        text_file.close() 
    
        pass

    @staticmethod
    def format_write():
        """This function adds information to a file"""
        objFile = open('cdInventory.txt', 'w')
        
        objFile.write(str(lstTbl))
        print('Saving your information')
        print('\n')
        
        objFile.close()
        pass










# -- PRESENTATION (Input/Output) -- #
class IO:
    
    @staticmethod
    def format_other():
    
    #This section of the code shows the user a menu, adds to the list the user create new extries, displays the current info 
    
        """This function shows the user the main menu"""
        print('This is a very cool CD Inventory Program\n')
        while True:
            # 1. Display menu allowing the user to choose:
            print('Current Inventory')    
            print('\n')
            text_file = open("cdInventory.txt")
            whole_thing = text_file.read()
            print(whole_thing)
            text_file.close() 
            print('\n')    
             
            print('Menu Options')
            print('\n')        
            print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
            print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
            strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
            print()
            pass
    
    # add code to captures user's choice and add code to get CD data from user
        """This function captures the users information"""
        if strChoice == 'a':
        
            strID = input('Enter ID: ').strip()
            strTitle = input('What is the CD\'s title? ').strip()
            stArtist = input('What is the Artist\'s name? ').strip()
            

            intID = int(strID)
            dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
            lstTbl.append(dicRow)
            print(lstTbl)
            print('\n')
            pass
    
    # add code to display the current data on screen
        """This function displays the current data input by the user"""
        if strChoice == 'i':
            
            print('Printing all user input information, for a full list please save your information to a text file')
            print(lstTbl)
            print('\n')
            pass
    
   
        
    
    
        pass










# -- Main Body of Script -- #


print('This is a very cool CD Inventory Program\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('Current Inventory')    
    print('\n')
    text_file = open("cdInventory.txt")
    whole_thing = text_file.read()
    print(whole_thing)
    text_file.close() 
    print('\n')    
     
    print('Menu Options')
    print('\n')        
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
       
        print('Program has been closed :(')
    
        break

    if strChoice == 'i':
        
        print('Printing all user input information, for a full list please save your information to a text file')
        print(lstTbl)
        print('\n')
        
    
    
    
    if strChoice == 'a':
    
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        

        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        lstTbl.append(dicRow)
        print(lstTbl)
        print('\n')
        
        
        
        
    if strChoice == 's':
        
        objFile = open('cdInventory.txt', 'w')
        
        objFile.write(str(lstTbl))
        print('Saving your information')
        print('\n')
        
        objFile.close()
        
        
    if strChoice == 'l':
        
        text_file = open("cdInventory.txt")
        whole_thing = text_file.read()
        print(whole_thing)
        text_file.close()
        
    
    # 3.5 process delete a CD
    if strChoice == 'd':
       
        print(lstTbl)
        
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
            
    
   

