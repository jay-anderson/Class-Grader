#Assignment #9
#Jay Anderson
#section 002
#python


#step 1: ask the user for a file name to work with
filename = input("Enter a filename to open: ")
filename = filename + ".txt"
try: 
#step 2: open the file for reading so we can analyze it
    file_object = open(filename, "r")

except:
    print("That file doesn't exist!")

else:
    print("Successfully opened", filename)
    print()
    #step 3: grab the data as a string
    alldata = file_object.read()

    #step 4: close the file, we are done
    file_object.close()


    #this is the answer key to the exam
    answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

    #turn the answerkey into a list
    answerkey_list = answerkey.split(",")
    
    
    #isolate each line of data
    lines = alldata.split("\n")

    all_points = []
    n_numbers = []
    valid = 0
    invalid = 0
    total_students = 0
    #visit every line in our lsit
    for record in lines:
        
        values = record.split(",")
        if len(values) == 26:
            total_students += 1
            valid += 1
            
            #now you need to score each students test using the answer key
            #you need a for loop
            #use list index
            #turn string into a list
            #set up afor loop to look at every answer
            points = 0
            for i in range(1, len(values)):
                if values[i] == answerkey_list[i-1]:
                    points += 4
                elif values[i] == "":
                    points += 0
                else:
                    points -= 1
            #you will also need to store their score in a list
            #you may also want to store their N# for later use
            #can't get these to work
            n_numbers.append(values[0])
            all_points.append(points)
            
        else:
            invalid +=1
    
sorted_all = sorted(all_points, key=int)
sorted_len = len(sorted_all)
index = (sorted_len - 1) // 2

if (sorted_len % 2):
    median_score = sorted_all[index]
else:
    median_score = (sorted_all[index] + sorted_all[index + 1])/2

mode_score = max(set(all_points), key = all_points.count)


highest_score = max(all_points)
lowest_score = min(all_points)
mean_score = format((sum(all_points)/total_students), '.2f')
range_score = highest_score - lowest_score
mean = sum(all_points)/total_students

print("Grade Summary:")
print("Total students:", total_students)
print("Unusable lines in the file:", invalid)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Mean score:", mean_score)
print("Median score:", median_score)
print("Mode:", mode_score)
print("Range", range_score)

while True:
    curve_answ = input("Would you like to curve the exam? 'y' or 'n': ")
    if curve_answ == "y":
        while True:
            curve = float(input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): "))
            if curve <= mean:
                print("Invalid curve, try again.")
                print()
            elif curve > mean:
                print("Done! Check your grade file!")
                added_score = (curve - mean)
                break
        break
    elif curve_answ == "n":
        break
    else:
        print("Invalid answer")


        
#create a new file for student grades
filename = filename[0:6]
filename = filename + "_grades.txt"
file_object = open(filename, 'w')

for i in range(len(n_numbers)):    
    file_object.write(n_numbers[i])
    file_object.write(",")
    file_object.write(str(all_points[i]))
    if curve_answ == "y":
        file_object.write(",")
        new_grade = format(all_points[i] + added_score, '.2f')
        file_object.write(new_grade)
    file_object.write("\n")
file_object.close()
