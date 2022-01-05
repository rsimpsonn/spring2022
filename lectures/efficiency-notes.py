# this assumes that gradebook-random is in the same folder as this starter file
import csv

# the following code loads a csv file into regular Python (not pandas)
# it turns a csv files into a list of dictionaries
with open('gradebook-random.csv',newline='') as gradefile:
    # DictReader reads a cvs row into a dictionary with keys given in the fieldnames list
    reader = csv.DictReader(gradefile, fieldnames=['id','hwk','exam','code','cs','att'])
    next(reader,None) # skip the header row
    gradebook = [] # an empty list
    for row in reader:
        gradebook.append({'id': row['id'],
                          'hwk': float(row['hwk']),     # csv values read in as strings by default
                          'exams': float(row['exam']),
                          'coding': row['code'],
                          'conc': row['cs'],
                          'attended': row['att']})

# Coding exercise: Determine whether students with prior coding experience do better
prior_coding = list(filter(lambda row : row['coding'] == "x", gradebook))
no_prior_coding = list(filter(lambda row : row['coding'] != "x", gradebook))

def avg(rowlist, forcol):
    '''Compute average of given column in list of rows'''
    total = 0
    for row in rowlist:
        total = total + row[forcol]
    return total / len(rowlist)

print("prior coding exam average is " + str(avg(prior_coding, "exams")))
print("no prior coding exam average is " + str(avg(no_prior_coding, "exams")))

# What if we asked about the time efficiency of this program. How might we measure that?
# In CS, we typically measure efficiency as "number of operations relative to size of input"
# example: asking "is this list empty" takes the same number of steps regardless of list length
# example: asking "is item X in the list" takes time proportional to the length of the list

# How "expensive" are our calls to filter?
# filter visits each list item exactly once, and runs its given function on each item
#   the cost of computing prior_coding is
#          length-of-list * cost of row['coding'] == "x"
#   let N stand for the length of the list. Getting a value from the row dictionary costs 1,
#     as does the == check. So the cost of computing prior_coding is
#          N * (1 + 1), where N is the length of the list

# What is the cost of the entire program?

prior_coding = list(filter(lambda row : row['coding'] == "x", gradebook))     # N * 2
no_prior_coding = list(filter(lambda row : row['coding'] != "x", gradebook))  # N * 2
print("prior coding exam average is " + str(avg(prior_coding, "exams")))      # N * 2 + 2 -- for avg
print("no prior coding exam average is " + str(avg(no_prior_coding, "exams")))   # N * 2 + 2 -- for avg
# avg uses N * 2 steps to sum the columns, 1 to extract the list length, and 1 for division

# Adding this all up, our code costs
#  (N * 2) + (N * 2) + (N * 2 + 2) + (N * 2 + 2) = 8N + 4

# if we needed to speed this up, perhaps we could rewrite the code to only go over the list items once

total_coding_exam_grades = 0         # cost is 1
total_non_coding_exam_grades = 0     # cost is 1
num_coding_exams = 0                 # cost is 1
for row in gradebook:                # cost is N (times work done inside loop)
    if row['coding'] == "x":         # cost is 2
        num_coding_exams = num_coding_exams + 1  # cost is 2 (one for +, one for =)
        total_coding_exam_grades = total_coding_exam_grades + row["exams"] # cost is 3 (lookup, +, =)
    else:                            # since only one of if or else will run, and if more expensive, ignore else cost
        total_non_coding_exam_grades = total_non_coding_exam_grades + row["exams"]

print("prior coding exam average is " + str(total_coding_exam_grades / num_coding_exams))
print("no prior coding exam average is " + str(total_non_coding_exam_grades / (len(gradebook) - num_coding_exams)))

# Adding up the costs in the comments, this version costs us:
#   1 + 1 + 1 + N*(2 + 2 + 3) + cost-to-print
#  3 + 7N

# So this version is a little cheaper (basically one N), but not much. Better to keep the first version.

# ------------- Another problem ------------------
# Imagine that there was no function to remove duplicates from a list. Let's write that manually

def distinct(fromlist):
    unique = []                        # 1 step (not proportional to N -- it's constant time)
    for item in fromlist:              # N steps (directly proportional -- call this linear)
        if not(item in unique):        #    checking in unique could involve looking at N elements (if all unique)
            unique.append(item)        #        constant time
    return unique                      # constant time
print(distinct([6, 2, 6, 4, 5, 5]))
# distinct takes 1 + (N * N)
# total of N^2 steps (dropping the constants, which we do in practice)

# Notice that N*N steps is quite a bit slower than N steps. For each list element, we do an amount of work
#   proportional to the whole list, not a constant amount of work like we did in the filtering example.
# You could argue that we don't actually do N^2 steps because the unique list doesn't always contain all
#   of the elements. That's true, but in the worst case it will, and using worst-case estimates is a
#   quick way to estimate the performance costs of programs (we'll do this in more depth in 200)

# If we could reduce uniqueness checking from needing N^2 work to needing "N * constant" work, that would
#   be a win. Here's how to do that with a dictionary!
def distinct2(fromlist):
    unique_dict = {}                 # cost is 2 (make new dict, =)
    for item in fromlist:            # cost is N
        unique_dict[item] = True     # cost is 1

    unique = []                      # cost is 2 (make new list, =)
    for key in unique_dict:          # cost is num-unique-items, which is N in the worst case
        unique.append(key)           # cost is 1
    return unique

# we first build a dictionary with the list items as keys. Since a dictionary can only have one
#  value per key, when we are done reading all the elements, the dictionary keys are the unique ones!
#  We then just need to make a list of the keys to get the unique elements.

# This version costs 2 + N + 2 + N, which is 2N + 2. This is a lot less than N^2

# Note that the second for loop could be written more directly with python dictionary operators.
#  We wrote out the long version here to help with the cost analysis

def distinct3(fromlist):
    unique_dict = {}                 # cost is 2 (make new dict, =)
    for item in fromlist:            # cost is N
        unique_dict[item] = True     # cost is 1
    return list(unique_dict.keys())  # does what the prev loop does to make list of the keys

# What are the takeaways?
# - we gauge the cost of code by looking at the number of operations relative to input size
# - For sequential code steps, we add the costs
# - For loops, we multiply the number of items by the cost of the loop body
# - constants aren't important in practice (we often drop them)
# - we think about worst case measurement (at this stage in your learning)
# - doing nested iterations over data (where N^2 comes from) gets expensive. We can sometimes
#   use intermediate data structures or variables to reduce computational costs
