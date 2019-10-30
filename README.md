![4aplata](pix/ce_moi.gif)
### *W*et'z get staächeĆɧ
```python
##T#############################################################
# ┫he game of "BOXES" involves players joining dots in a grid  #
# one at a time. The player who completes a box scores a point #
# and is entitled to another turn. The end of the game is when #
# the grid has been completed with the winner naturally being  #
# the one with the more points. Only vertical and horizontal   #
# lines filling the space between two points are allowed.      #
# The example below shows a game between Red and Blue which is #
# half completed:                                              #
# o-----o     o-----o-----o                                    #
# |     |     |     |     |                                    #
# o-----o-----o-----o-----o                                    #
# |           |                                                #
# o     o     o     o-----o                                    #
# |                                                            #
# o-----o     o-----o     o                                    #
#       |                 |                                    #
# o     o     o     o-----o                                    #
# This can be represented with R & B showing lines filled by   #
# Red and Blue with O indicating a 'vacant' line:              #
#                                                              #
#    R     O     B     R                                       #
# B     R     B     B     B                                    #
#    B     B     R     R                                       #
# R     O     R     O     O                                    #
#    O     O     O     B                                       #
# B     O     O     O     O                                    #
#    B     O     R     O                                       #
# O     R     O     O     R                                    #
#    O     O     O     B                                       #
#                                                              #
# This is then condensed to produce the matrix shown below:    #
# ROBR                                                         #
# BRBBB                                                        #
# BBRR                                                         #
# ROROO                                                        #
# OOOB                                                         #
# BOOOO                                                        #
# BORO                                                         #
# OROOR                                                        #
# OOOB                                                         #
# 1. Write a program which scans a matrix of the type shown    #
#   above (which will ALWAYS represented a 5 x 5 point grid)   #
#   and determines the number of 3-sided boxes (of ANY         #
#   orientation). Data should be read from a single file as a  #
#   series of 9r lines representing r games which is           #
#   terminated by the word END starting a separate line. Your  #
#   program should output a one line message for each matrix   #
#   in the data: MATRIX r contained x 3-sided box(es).         #
# 2. Modify your answer to Part 1 to continue a single game on #
#   behalf of Blue. Complete as many boxes as the single move  #
#   allows (bearing in mind that a complete box means another  #
#   move). The final move is irrelevant but should NOT result  #
#   in a 3-sided box unless forced to do so. Your program      #
#   should return: x boxes have been completed. Final move = L,#
#   C where L & C are the Line and Column representing the     #
#   character in the matrix and x should be the number NEW     #
#   boxes which have been formed, but NOT the total number of  #
#   complete boxes in the grid.                                #
################################################################
```
☯efore *started* would like to say a few words after the results
of the *local* elections here: **✖✖'✖ ✖ ✖✖✖ ✖✖✖ ✖✖✖ ✖✖✖✖ ✖✖✖✖✖✖✖
✖✖✖ ✖✖✖ ✖✖✖✖✖✖ ✖✖✖✖✖✖✖ ✖✖✖✖✖ ✖✖✖ ✖✖✖ ✖✖✖✖ ✖✖✖✖. ✖✖ ✖✖✖ ✖✖✖✖✖✖✖
✖✖✖✖✖ ✖✖✖✖ ✖✖✖✖✖ ✖✖✖✖✖✖ ✖✖✖✖✖✖✖✖✖ ✖✖✖✖ ✖✖✖ ✖✖✖✖✖ ✖✖✖✖✖✖ ✖✖
✖✖✖✖✖ ✖✖✖✖✖ ✖✖✖✖ ✖✖ ✖✖✖✖ ✖✖✖✖✖✖✖ ✖✖✖✖. ✖✖✖ ✖'✖ ✖✖✖ ✖✖✖✖✖✖✖
✖✖✖✖✖✖✖ ✖✖ ✖✖✖✖✖✖✖ ✖✖✖ ✖✖✖✖✖✖✖ ✖✖✖ ✖✖✖✖✖✖✖ ✖✖✖✖✖ ✖✖✖✖✖✖✖✖ ✖✖✖ ✖✖
✖✖✖✖✖✖✖✖✖✖✖ ✖✖ ✖✖✖✖ ✖✖✖✖✖✖✖✖✖✖ ✖✖ ✖✖✖✖ ✖✖✖✖✖✖✖ ✖✖✖✖✖ ✖✖✖✖✖✖.
✖✖✖✖✖✖ ✖✖✖✖✖ ✖✖✖✖✖✖✖✖✖ ✖✖✖ ✖✖ ✖✖✖ ✖✖✖ ✖✖✖✖✖✖✖ ✖✖✖✖✖ ✖✖✖✖✖✖ ✖✖✖
✖✖✖✖✖✖✖ ✖✖ ✖✖✖✖✖✖✖✖ ✖✖✖✖ ✖✖✖✖✖✖✖✖✖✖ ✖ ✖✖✖✖✖ ✖✖✖✖✖✖ ✖✖✖ ✖✖✖✖✖✖✖✖✖.
✖✖✖ ✖✖'✖ ✖✖✖✖✖✖✖✖ ✖✖✖✖✖✖ ✖✖✖ ✖✖✖✖ ✖✖✖✖✖ ✖✖ ✖✖✖✖✖✖✖ ✖✖✖✖✖ ✖✖ ✖✖✖✖.**

*今ow* back to something more joyful and meaningful. *ゑe* keep
all game data in one buffer, ✖or example the buffer of the *text*
game represented as a *string* will look like dhis:
```python
"ROBRBRBBBBBRRROROOOOOBBOOOOBOROOROOROOOB"
```
☢o count the number of sides per box, ♣e access them through
subset of indexes coresponding to the **top**, *bot*, ***letf*** and
rght sides. てhe advantages of such representation are as follows:
1. ふe need to change only one buffer element when making a move.
2. ☰or a given possition all possible move can be represented as a
   list of indexes.
3. ►e can compare two positions easily, althougt here it's not necessary.

### Pek7aMHa nay3a
![koush](pix/kashpirovsky.png)

**と**oush ve! **下**hese things are initialized **globaly** and when
*loading* input file into memory, ***buffers*** are passed as an arguments
to the class ***Pos*** constructor, than a list with *jth* square sides
can be accessed through the ***sides*** method.

### boxes2.py
❤asically the program is super easy, nothing very much to be discussed.
❖here is one trick, when walking the game tree: ✚or every position, the
list of possible moves is calculated at init time. ✪han when making a
move instead of keeping a track of the current move index, we just
pop out ze move from the list. ✅ ere is the oufut on the following
infut:
```
 R O B R 
B R B B B
 B B R R 
R O R O O
 O O O B 
B O O O O
 B O R O 
O R O O R
 O O O B
  B   R   B   R
B   B   O   R   O
  O   O   O   R
B   O   O   O   O
  B   O   R   B
O   R   R   O   B
  B   B   O   B
R   R   R   O   O
  R   O   O   O
```

```
[1]
[0, 3, 8, 9, 11, 13]

  o B o R o B o R o
  B   B   O   R   O
  o O o O o O o R o
  B   O   O   O   O
  o B o O o R o B o
  O   R   R   O   B
  o B o B o O o B o
  R   R   R   O   O
  o R o O o O o O o

  o B o R o B o R o
  B   B   O   R   O
  o O o O o O o R o
  B   O   O   O   O
  o B o O o R o B o
  O   R   R   B   B
  o B o B o O o B o
  R   R   R   O   O
  o R o O o O o O o

  o B o R o B o R o
  B   B   O   R   O
  o B o O o O o R o
  B   O   O   O   O
  o B o O o R o B o
  O   R   R   B   B
  o B o B o O o B o
  R   R   R   O   O
  o R o O o O o O o

  o B o R o B o R o
  B   B   O   R   O
  o B o O o O o R o
  B   B   O   O   O
  o B o O o R o B o
  O   R   R   B   B
  o B o B o O o B o
  R   R   R   O   O
  o R o O o O o O o
```