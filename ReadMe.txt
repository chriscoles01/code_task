
Approach:
Task 1:
    I understood this as a constraint problem and approached it accordingly. 
    I generated a constraint 'graph' (in a 1d multiindex data frame)
    This allowed me to easily approach the problem with an efficient way of managing the overlap constraint
    Realising that this problem is O(n!) time complexity, I decided to create a heuristic before running a constraint problem solver
    I used the python package python-constraint with MinConflicts as a solver for the constraint problem
    todo: improve the speed of constraint solver with a divide and conquer technique
Task 2:
    I generated a dictionary of all possible start and endpoints for the segments
    I then used a data frame to find which regions would lie in these segments, the total count being the number of overlaps
    Much quicker to solve than task 1

The example outputs in the respective Output folders are generated from the Regions_Big.txt file

RUNNING CODE:
Data supplied is in the /Data folder

cd to Task_1/src or Task_2/src as required

for both tasks:

    python main.py path_to_genome_region
    if no path is supplied it will default to "../../Data/Regions_Big.txt"


the output solution txt will be in the Task_1/Output or Task_2/Output accordingly

Virtual environment:
creating a Virtual environment (venv) is recommended
all dependencies are listed in requirements.txt
you can install these with pip install -r requirements.txt

TESTING:

run ./runpytest.bat or ./runpytest.ps1 to run the tests for each task automatically
otherwise, navigate to the appropriate test folder and run pytest in cmd