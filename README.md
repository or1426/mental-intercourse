mental-intercourse
==================

A python (although not very pythonic) brainfuck implementation. 

Brainfuck 
----------
http://en.wikipedia.org/wiki/Brainfuck

Usage
------
On unix just:

echo 'BRAINFUCK' | python mental-intercourse 

or:

chmod u+x mental-intercourse

echo 'BRAINFUCK' | ./mental-intercourse 

If the second one gives weird errors check where your python is and change the top comment if required

For example:

echo '++++++++++[>+fgd++++++>++++++++++>+++>dfgdgdf+<<<<-]>++.>     +.+++++++..+++.>++.<<+++++++ ++++++++.>.+++.------.--------.>+.>.' | ./mental-intercourse.py

will print:
Hello World!

(echo 'Hello World!' will also do exactly the same but far less stylishly)
