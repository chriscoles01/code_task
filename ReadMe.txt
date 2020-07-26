
Approach:
Task 1:
    I understood this as a constraint problem and approached it accordingly. 
    I generated a constraint 'graph' (in a 1d multiindex dataframe)
    This allowed me to easily approach the problem with an efficient way of managing the overlap constraint
    Realising that this problem is O(n!) time complexity, I decided to create a heuristic before runnning a constraint problem solver
    I used the python package python-constraint with MinConflicts as a solver for the constraint problem
    I used a divide and conquer method to try to reduce the amount of time it takes to find the lowest number of rows

Task 2:
    I generated a dictionary of all possible start and end points for the segments
    I then used a dataframe to find which regions would lie in these segments, the total count being the number of overlaps
    Much quicker to solve than task 1

The example outputs in the respective Output folders are generated from the Regions_Big.txt file

Virtual environment:
creating a Virtual environment (venv) is recommended
all dependencies are listed in requirements.txt
you can install these with pip install -r requirements.txt

TESTING:

run ./runpytest.bat or ./runpytest.ps1 to run the tests for each task automatically
otherwise navigate to the appropriate test folder and run pytest in cmd