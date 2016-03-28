# DIFFAlgorithmTest
A simple app that tests Python 3.4's diff capabilities.  For March 21st-28th stage of Independent Study course.

The app first compares two lines, then two paragraphs, then two pages, all of which are of my choosing.

The only difficulties that I faced were the unicode issues with ASCII when comparing entire pages.  Everything else was easy to figure out.

------------------------------------------------------------------------

Files:
"DIFFapp.py" is the sole file containing the code that I wrote in Python.  Comments and references within.

"argon1.txt" and "argon1edit.txt" are the two text files I have chosen to compare for the third (pages) comparison.  The former is the first page of the infamous 1970 fantasy novel "The Eye of Argon", and the latter is my edited version of the same.

"testresults.txt" is the exact IDLE output of the line, paragraph, and page results.

------------------------------------------------------------------------
References:
Much of the reference for the code and logic were from the following pages:
1. https://pymotw.com/2/difflib/
2. https://docs.python.org/2/library/difflib.html

Reading materials used for comparison are taken from:
1. Paragraph comparison: www.homestarrunner.com/englishpaper.doc
2. Page comparison: https://www-users.cs.york.ac.uk/susan/sf/eyeargon/eyeargon.htm
