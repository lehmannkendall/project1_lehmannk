# The Simple Banking Application
This program is a flask application for a simple banking app.

## Web Pages
Each decorator provides a function that designates what should be shown on the given web page.
The home page welcomes users to the banking app. - Welcome to the banking application!
Another page provides information about the name of the bank. - Welcome to -bank name-!
Three pages let you know the dollar, pound, or yuan amount. - -currency name- -value amount-
The final page provides information about the bank name, currency, and amount. - Welcome to the -bank name-! -bank name- Bank holds the -currency- currency and currently holds -value- of -currency-.
 -- = input

## Other Code
In order for the simple banking app to work, there is a separate file (lab3_code.py) that provides more code. The definitions in the separate file inform what should be returned on each web page. The definitions include sub classes (Dollar, Yuan, Pound) of the class Currency and another class, Bank.

## Dependencies
You can install everything you need by referencing the requirements.txt file.

## How to Run
Download SI507_project1.py and lab3_code.py into the same directory. In your terminal window type: python SI507_project1.py runserver. Then go to your web browser and type in localhost:5000.
For the homepage type: localhost:5000 in the URL.
For the welcome to -bank name- page type: localhost:5000/-bank name- in the URL.
For the -currency name- -value amount- page type: localhost:5000/-currency name-/-value amount- in the URL.
For the final page type: localhost: 5000/bank/-bank name-/-currency name-/-value amount- in the URL.
When you are done with the flask banking application press control and c in the terminal window.
