## Setup

To run this project:
+ [clone](https://help.github.com/en/github/using-git/which-remote-url-should-i-use) the repository or [download](https://github.com/Mokeira/buySide/archive/master.zip)  the zipped project.
+ Ensure you have Python installed (Python3 recommended)

## Description

### `countUppercase(file_name)`
Takes in a filename and returns the number of uppercase characters in the file

### `fibonacci(n)`
Takes in a number *n* and returns the *n-th* Fibonacci number

The function is implemented iteratively so as not to reach the recursion limit when *n* is large.

### `extracted_ids(data)`
Takes in a list of dictionary items and returns a sorted list containing the id values of the items

### `transformdata2(data)`
Takes in a list of dictionary items and returns a list of id-name pairs.

The id values are sorted in ascending order while the name values are sorted in descending order before pairing.


### `mergeDicts(a,b)`
Takes in 2 dictionaries (*a* and *b*) .
Creates a copy of *a* and adds to this items that are in *b*  whose keys are not already in *a*.

## Running from the terminal
Once you are done setting up the files, navigate to the project directory and start and interactive Python session.

Import the buysideAnswers module by running the following command:
`import buysideAnswers as ba`

To call any of the functions, use `ba.functionName(input)` where functionName is the name of the function and input is the argument passed to the function where applicable.
 
Below is an example of how to call *countUppercase* with the file provided in this repository:
	`ba.countUppercase("file1.txt")`

## Testing buySide
buyside_test.py contains test cases that can be used to test the program. If you want to see whether the test cases are passing, run the following command:
`python buyside_test.py`

