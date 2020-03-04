# Paired Data Example in python

## setting and printing the list values
celebs=[("Brad Pit",1963),("Kama Kacha",1945),("Mr Anaconda",1990)]
print (celebs)
print (len(celebs))

## using loop to get the value from the paired list
for name, years in celebs:
    if years <1964:
        print (name,years)


## Nested Data Example

students = [
("John", ["CompSci", "Physics"]),
("Vusi", ["Maths", "CompSci", "Stats"]),
("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

for nanme, subjects in students:
    print (name, "takes",len(subjects),"courses")



# Count how many students are taking CompSci
counter = 0
for name, subjects in students:
    for s in subjects: # A nested loop!
        if s == "CompSci":
             counter += 1
print("The number of students taking CompSci is", counter)