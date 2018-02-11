# Problem
Contest Scoreboard

Want to compete in the ACM ICPC? 
then you had better know how to keep score!
Constestants are ranked first by the number of problems solved (the more the better),
then by decreasing amounts of penalty time.If two or more contestants 
are tied in both problems solved and penalty time, they are displayed in order of 
increasing team numbers.

A problem is considered solved by contestant if any of submissions for that
problem was judged correct. 
Penalty time is computed as the number of minutes 
it took until the first correct submission for a 
problem was received, plus 20 minutes for 
each incorrect submission prior to the correct solution.
unsolved problems incur no time penalties.

Input 
the input begins with a single positive integer
on a line by itself indicating the number of cases,
each described as below. This line is followed by a blank line.
There is also a blank line between two conecutive input.

The input consist of a snapshot of the judging queue, containing entries from some
or all of contestants 1 through 100 solving problem 1 through 9. Each 
line of input consist os three numbers and a letter in the format Constestants problem time L, where
L can be C, I, R, U or E. These stand for Correct, Incorrect, Clarification Request, Unjudget and
Erroneous submission. the last three cases not affect scorring.
the lines of input appear in the order in which the submission where received.

Output
The output for each test case will consist of a scoreboard, sorted by the criteria described above.
Each line of Output will contain a contestant number, the number of problems solved by the contestant
and the total time penalty accumulated by the contestant.
Since not all contestants are actually participating, only display those Constestants who have made a submission.

The output of two consecutive cases will be separated by a blank line.

Sample input

```
1
1 2 10 I
3 1 11 C
1 2 19 R
1 2 21 C
1 1 25 C

```

Output sample

```
1 2 66
3 1 11

```
# Project

The project running in ```python3 ```

# Running tests

```
python3 test.py
```