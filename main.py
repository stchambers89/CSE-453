def main():


    class PathSegment:
        def __init__(self, first, last, total, value):
            self.first = first
            self.last = last
            self.total = total
            self.value = value
    
    def getPaths():
        filePath1 = input('Enter the frist filename: ')
        filePath2 = input('Enter the second filename: ')
        paths = [filePath1, filePath2]
        return paths

    def getPathEndings(pathList):
        pathEndings = []
        for path in pathList:
            splitPath = path.split('\\')
            pathEnd = splitPath[-1]
            pathEndings.append(pathEnd.lower())
        
   
    
   

    pathList = getPaths()
    getPathEndings(pathList)





    
    #fileList1 = splitFile(filePath1)
    #fileList2 = splitFile(filePath2)

    #filePathEnd1 = fileList1[-1]
    #filePathEnd2 = fileList2[-1]


    # def compareFileNames(firstFile, secondFile):
    #     return firstFile == secondFile

    #def canon(file, splitFileList):
        #convert string into ascii values (h = 104, e = 101, etc)
        #for letter
        #value = [ord(character) for character in splitFileList]
        #print(value)
    
    #canon(firstFile)
    
    # Determines if two file paths are the same.
    #def homograph():
       #print('This function exists and works in some capacity. 50%!')
        
if __name__ == "__main__":
    main()



     #print(' ') 
    #print("the first filename is: " + firstFile)
    ##print("the second filename is: " + forbiddenFilePath)
    #if secondFile == forbiddenFilePath:
    #    print("True")
    


    
    
#TO DO
# Find Symbols for windows shell navigation
# Create non-homographs
# Compare two filepaths to see if they lead to the same file 
# (our homograph function should rely on canon function)
# 


# Non Homograph Test Cases
# topSecret.txt
# ..\topSecret.txt
# ..\Forbidden\topSecret.txt
# ..\Jim\Forbidden\topSecret.txt

# Homograph Test Cases
# C:\User\Jim\Forbidden\topSecret.txt
# C:.\..\Jim\Forbidden\topSecret.txt
# C:.\..\..\Forbidden\topSecret.txt
# C:.\..\..\..\topSecret.txt

# WHYYYYYY?!?!?!?!?!?!?!?!
