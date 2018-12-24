"""
 ===============================================================================
 Auth: Sam Celani
 Prog: editor.py
 Revn: 12-21-2018 Ver 1.0
 Func: Add, delete, or edit ticket entries
 ===============================================================================
 CHANGE LOG
 -------------------------------------------------------------------------------
 12-21-2018:    init
                init menu, add, edit, delete functions
                init fast functions
 12-22-2018:    comments?

 TODO


"""

def add():
    print('a')

def fadd():
    print('fa')

def edit():
    print('e')

def fedit():
    print('fe')

def delete():
    """
    Alg:
        List ticket attributes
        User select
        Search for user input in that field
            List closes
        Print entry or entries that satisfy
        Ask for confirm
        Remove line from file
        Return 1 if positive confirm
    """
    print('d')

def fdel():
    print('fd')


def menu( exitCondition ):
    """
    Alg:
        Get and check user input
        Increment counter variable with returns from functions
        Return
    """
    changes = 0
    
    while True:
        
        print('What would you like to do?')
        i = input(' Add, Edit, or Delete an entry?\n\n').lower()

        if i == 'add':
            changes += add()
        elif i == 'fadd':
            changes += fadd()
        elif i == 'edit':
            changes += edit()
        elif i == 'fedit':
            changes += fedit()
        elif i == 'delete':
            changes += delete()
        elif i == 'fdel':
            changes += fdel()
        elif i in exitCondition:
            break
        else:
            print('That command does not exist.\n')

    return changes > 0
