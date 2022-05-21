# Declare variables.
file1 = ''
file2 = ''

# Get input from user.
first_filename = input('Specify the first filename: ')
second_filename = input('Specify the second filename: ')

# Write a canonicalization function.
def canon(filename):

    # Declare temporary string variable
    temp_string = ''

    for i in range(len(filename)):
        if filename[i] == "/" or filename[i] == "." or filename[i] == "\\" or filename[i] == ":":
            i += 1
        else:
            temp_string += filename[i]

    # Convert to lowercase string.
    temp_string = temp_string.lower()

    # For Testing
    # print(temp_string)

    return temp_string

# Write a homograph function.
def  homograph(first_filename, second_filename):

    # Declare values
    isHomograph = False
    count = 0

    # Call canon()
    f1 = canon(first_filename)
    f2 = canon(second_filename)

    #Reverse the strings for comparison.
    file1 = f1[::-1]
    file2 = f2[::-1]

    # For Testing.
    # print(f'File1: {file1}')
    # print(f'File2: {file2}')

    # Compare files
    if len(file1) < len(file2):

        # Use for loop to compare strings.
        for i in range(len(file1)):

            # Compare each letter to each other. If they are not
            # identical then increase the count variable. If count
            # ends up greater than or equal to 1, it must be a non-
            # homograph.
            if file1[i] != file2[i]:
                count += 1
            else:
                i += 1

        # If count == 0, update the boolean value.
        if count == 0:
            isHomograph = True

    # Else file2 is smaller and we should use that one.         
    else: 
        
        for i in range(len(file2)):

            if file2[i] != file1[i]:
                count += 1
            else:
                i += 1

        if count == 0:
            isHomograph = True

    # Print appropriate statement.
    if isHomograph == True:
        print("The paths are homographs")
    else:
        print("The paths are not homographs")

homograph(first_filename, second_filename)
