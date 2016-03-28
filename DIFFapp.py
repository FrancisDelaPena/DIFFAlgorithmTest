'''
Basic Python DIFF application for Dr. Hayward's COMP 398 course
For week of 3/21/16 to 3/28/16
References from: https://pymotw.com/2/difflib/
'''

import difflib, sys, io

def tcompare(text1, text2): #short for "text comparer"
    text1split = text1.splitlines()
    text2split = text2.splitlines()

    d = difflib.Differ()

    dif = d.compare(text1split, text2split)

    print('\n'.join(list(dif)))

def tcomparefile(file1, file2): #expansion of tcompare which reads files then uses original tcompare to find differences
    with io.open(file1, encoding="utf-8") as file1: #ASCII could not decode certain characters
        page1 = file1.read()
    with io.open(file2, encoding="utf-8") as file2: #ASCII particularly had problems with the 2nd file
        page2 = file2.read()
    tcompare(page1, page2)
    

def main():
    
    '''LINE COMPARISON: A very famous movie line.'''

    line1 = "Luke, I am your father." #The often misquoted version
    line2 = "No. I am your father." #The actual line
    print("Comparing single lines...")
    print("------------------------------------------------------")
    tcompare(line1, line2) #simply enter two variables in parameters
    print("------------------------------------------------------")
    
    '''PARAGRAPH COMPARISON: The paragraph is a reference to the early internet flash cartoon "Homestar Runner"
    Source: http://www.homestarrunner.com/sbemail64.html
    Second paragraph contains my own edits.'''
    
    par1 = """First, moving around quickly, and with purpose, is a
    true sign of character. Secondarily, bustle(e.g. hustle)
    yields more product for the working types. "Hustle and bustle
    are like my right and left arms," said Li'l Spicy in his famous
    "Hustle and Bustle Are Like My Right and Left Arms" speech.
    Webster's defines bustle as "excited and often noisy activity;
    a stir." A stir, indeed. Finally, sometimes gross stuff can
    be funny.
    """
    par2 = """First.  Moving around quickly, and with purpose, is a
    true sign of character. Secondly, bustle(e.g. hustle)
    yields more product for the working types. "Hustle and bustle
    are like my right and left arms," said Little Spicy in his famous
    "Hustle and Bustle Are Like My Right and Left Arms" speech.
    Webster's dictionary defines bustle as "excited and often noisy activity;
    a stir." A stir, indeed. Finally, sometimes gross stuff can
    be funny.
    """
    print("Comparing paragraphs...")
    print("------------------------------------------------------")
    tcompare(par1, par2)
    print("------------------------------------------------------")
    
    '''PAGE COMPARISON: This is the first page of the infamously bad fantasy novel "The Eye of Argon."
    All spelling and grammatical mistakes from the original have been left intact.
    For the second version, I have edited the grammatical and spelling mistakes myself, while changing up some words.'''
    
    print("Comparing pages...")
    print("------------------------------------------------------")
    tcomparefile("argon1.txt", "argon1edit.txt")

main()
