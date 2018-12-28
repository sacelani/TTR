"""
 ===============================================================================
 Auth: Sam Celani
 Prog: ttr.py
 Revn: 12-27-2018 Ver 0.4
 Func: Read in parking ticket data, print simple table, do math on (((data))),
       plot data and try to make inferences about best parking times

 TODO: set up plotting
 ===============================================================================
 CHANGE LOG
 -------------------------------------------------------------------------------
 12-11-2018:    init
 12-20-2018:    set up master data structure
                set up data read in
                began populating data file
                    set up data file "syntax"
 12-21-2018:    init getStats()
                moved body to initStats
                created body of program
                imported editor
                comments
                cls lambda function
                update master data after changes in initStats()
*12-27-2018:    removed editor module
                init getStats() function

 IMPORTED FILES
 
    data\td.txt

        contains all ticket data


 IMPORTED MODULES

    matplotlib

        plotting shit

    os

        clear screen

"""

# ==============================================================================
#
#   IMPORTS
#
# ------------------------------------------------------------------------------

import matplotlib       # Contains plotting functions
import numpy            # Contains mathy stuff
import os               # Used for clear screen

# ==============================================================================
#
#   GLOBAL VARIABLES
#
# ------------------------------------------------------------------------------

# Master data
#           Format
data = [ [],    # 0: Citation number
         [],    # 1: Issue Date
         [],    # 2: Issue Time
         [],    # 3: Officer
         [],    # 4: Location
         [],    # 5: Sub-location
         [],    # 6: Meter Number
         [],    # 7: Violation
         [],    # 8: Penalty
         [] ]   # 9: Me

hlp = ''

# ==============================================================================
#
#   FUNCTIONS
#
# -----------------------------------------------------------------------------

"""
 ===============================================================================
 Revn: 12-27-2018
 Func: Display plots of pertinent information
 Meth: Just prints tickets right now
 Vars: None
 Retn: None, plots
 ===============================================================================
"""
def getStats():
    #print('This is where the stats get computed and the plots get plotted\n')
    for c in range(len(data[0])):       # Iterate over depth of tickets
        print('[ ', end='')             # Print the start bracket
        for b in range(len(data)):      # Iterate over all 10 attributes
            print(data[b][c], end='')   # Print each attribute per ticket
            # If its the last attribute, print end bracket, else comma
            print(' ]') if b is len(data) - 1 else print(', ', end='')
##    print('\n')                         # Finish strong with new line
            


"""
 ===============================================================================
 Revn: 12-21-2018
 Func: Initialize data from file at startup
 Meth: Open file, read line by line, split around commas, strip last char
 Vars: None
 Retn: None, changes global data variable
 ===============================================================================
"""
def initStats():
    
    global data     # Grab global variable data

    with open('data/td.txt', 'r') as Tdata: # Open file as read only
        for line in Tdata:                  # Parse line by line
            l = line.split(',')             # Split over commas :) fuck C
            for c in range(len(l)):         # Iterate over items in line
                data[c].append( l[c][:-1] ) # Strip last char, add to data set



"""
 ===============================================================================
 Revn: 12-21-2018
 Func: Clear screen
 Meth: Lambda function, import os
 Vars: None
 Retn: None

 TODO: Make system independent
 ===============================================================================
"""
cls = lambda: os.system('cls')


### ============================================================================
###
### BODY 
###
### ----------------------------------------------------------------------------

initStats()     # Pull data from file

inp = 'What would you like to do?\n Look at stats?\n Ask for help?\n\n'
exitCondition = [ 'exit', 'stop', 'quit', 'kill', 'abort', 'close', 'terminate' ]

while True:
    # Get user input, and sanitize
    i = input(inp).lower()

    # This block kind of speaks for itself
    if i == 'stats':
        getStats()
    elif i == 'help':
        print(hlp)
    elif i in exitCondition:
        break
    else:
        print('That command does not exist.\n')

### ============================================================================

