This program reads the JSON files created by the Drumbit program according to the 
current requirements of a rubric given to my sixth grade students:

* "Four on the Floor" rhythm in the bass drum track (Track #8)
That's a strike on beats 1,2,3, and 4; index numbers 0,4,8, and 12 (2 points toward final score)

* Snare Drum part (Track #7) has "Backbeat"; a strike on beats 2 and 4 (index #'s 4 and 12) (2 points toward final score)

* Closed Hi-Hat track (Track #6) has at least four strikes in the pattern (1 point toward final score)

* At least one other track is has at least one strike at least once (1 point toward final score)

* Tempo is set to any number in the range between 70-150 BPM;
NOT including 80 BPM, which is default setting - 80 indicates that student didn't explore 
any other options. (This feature not yet implemented in code) (1 point toward final score)

* At least one track has volume adjusted from default and at least one track has panning adjusted from default
(1 point toward final score)

If all requirements are met, student receives 8/8.

Two functions create two seperate outputs, one is the student's name and final score in csv format, 
the other is a template of messaging to each student a point by point report of their pattern in 
relation to the requirements of the rubric.

Each of these functions currently only produce an output when piped through bash in the terminal.


Wish list:

A GUI for students to input Team number, first name, and last name, from which the 
file name is then give for grader to read when students attach file when submitting.

A more thorough filename checker (try/except, etc.) and adjuster to strip spaces, analyze 
several separators (currently using only comma), capitalize first letter and first letter following
the separator. Accommodate apostrophes and hyphens within students' last names without mistaking it for a separator.

A version of the autograder online for students to run the program on and get immediate feedback of the report to let
them know what's meeting the rubric requirements and what is not.

An option to auto email each student when they submit the file that sends the report of their grade point by point.

A GUI for the teacher to submit files/folder to autograde. Options include CSV output version, auto emailer, 
and eventually other options for setting template requirements, such as specific rhythms for specific tracks and other
settings. Might even be able to customize using a 16 step row that changes code requirement.




