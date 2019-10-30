#!/usr/bin/env python2
# -*- coding: utf-8 -*-
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
import sys #                                                   ☰
################################################################
games = [] # list of initial game positions (Pos)              ♒
width = 4 ## board width                                       =
sqrs = range(width**2) # square indexes                        ♒
buflen = 40 # namba of sides                                   =
scenario = [] # list of all game continuations                 =
rec = [] # record stack for walking a game tree                =
# Yea, Ok bcoz for some squares top move is also a bot move    =
# for another square ve keep that data in a buffer and refer   =
# to it as a subset of indexes for top, bot, left and rght     =
# sides respectively. Thus we need change only buffer values. oo =
# Also later in the second sub-problem it might be necessary   =
# to have a list with possible moves for a given position.     =
# Keeping all data in one buffer, we can specify a move by     =
# giving just one index.                                       =
#                                                              =
#   o--_0--o--_1--o--_2--o--_3--o                              =
#  _4     _5     _6     _7     _8                              =
#   o--_9--o--10--o--11--o--12--o                              =
#  13     14     15     16     17                              =
#   o--18--o--19--o--20--o--21--o                              =
#  22     23     24     25     26                              =
#   o--27--o--28--o--29--o--30--o                              =
#  31     32     33     34     35                              =
#   o--36--o--37--o--38--o--39--o                              =
#                                                              =
top  = [0, 1, 2, 3, 9,10,11,12,18,19,20,21,27,28,29,30] ###### =
bot  = [9,10,11,12,18,19,20,21,27,28,29,30,36,37,38,39] ###### =
left = [4, 5, 6, 7,13,14,15,16,22,23,24,25,31,32,33,34] ###### =
rght = [5, 6, 7, 8,14,15,16,17,23,24,25,26,32,33,34,35] ###### =
dir  = (top, rght, bot, left) #                      .. ###### = 
board = '  o   o   o   o   o\n'\
        '                   \n'\
        '  o   o   o   o   o\n'\
        '                   \n'\
        '  o   o   o   o   o\n'\
        '                   \n'\
        '  o   o   o   o   o\n'\
        '                   \n'\
        '  o   o   o   o   o\n'
################################################################
board_coorz = [4,8,12,16,           #    # # # #   ### #   ### =
               22,26,30,34,38,      ## ###   # # s ### # s ### =
               44,48,52,56,         ## ### # # #   ### #   ### =
               62,66,70,74,78,      #                          =
               84,88,92,96,         #                          =
               102,106,110,114,118, #  A  M  A  S  S  I  N  G  =
               124,128,132,136,     #                          =
               142,146,150,154,158, #                          =
               164,168,172,176]     #                          =
#############P####################s#r###########################
class Pos: # ℘osition             ┊ ┋                          ¦
    def __init__(self, buf): # constҫuctor ####################¦
        self.buf = buf[:] #       ┊                            ¦
        self.moves = self.get_moves() #                        ¦
    ############################################################
    
    def sides(self, j): # get jth ÿquare sides ################¦
        t = self.buf[ top[j]] ###  ,`                          ¦
        b = self.buf[ bot[j]] ###  \    o    o                 ¦
        l = self.buf[left[j]] #     |     ..                   ¦
        r = self.buf[rght[j]] #     *===__                     ¦
        return [t, r, b, l]   ####       ~                     ¦
    ############################################################
                                                #              =
                                                #           oo ¦
    ############################################################
    def get_3side_boxes(self): #                               ¦
        ls = [] #                                              ¦
        for j in sqrs: #                                       ¦
            sides = self.sides(j) #                            ¦
            if sides.count('O') == 1: ls.append(j) #           ¦
        return ls #                                            ¦
    ############################################################

    def get_moves(self): #######################################
        moves = [] #                                           ¦
        ls = self.get_3side_boxes() #                          ¦
        for j in ls: # loop over 3 sided boxes                 ¦
            sides = self.sides(j) #                            ¦
            i = sides.index('O') #                             ¦
            sides.remove('O') #                                ¦
            if sides == ['B','B','B']: #                       ¦
                moves.append(dir[i][j]) #                      ¦
        return moves #                                         ¦
     ############################################################    

    def __str__(self): #########################################
        ls = list(board) #                                     ¦
        for j in range(buflen): #                              ¦
            ls[board_coorz[j]] = self.buf[j] #                 ¦
        return ''.join(ls) #                                   ¦
    ############################################################
    
    def move(self): ############################################
        j = self.moves.pop() #                                 ¦
        buf = self.buf[:] #                                    ¦
        buf[j] = 'B' #                                         ¦
        return Pos(buf) #                                      ¦
    ############################################################

##################################################################
def load(): #                                                  ┋ 
    buf, cntr, n = [], 0, 9 #                           wtf?   ┋ 
    for line in sys.stdin: #                                   ┋ 
        cntr += 1 #                                            ┋ 
        buf.extend(line.rstrip('\n').split()) #                ┋  
        if (cntr % n) == 0: #                                  ┋
            games.append(Pos(buf)) #   ..                      ┋ 
            buf[:] = [] # clear buffer  oo                     ┋..
        ##### .. ##############################################┋##
    ####### boom ##############################################┋##
#######   BOOM   ##############################################┋##

def walk(pos): #################################################
    rec.append(pos) #                                          ] 
    while pos.moves: #                                         ]
        walk(pos.move()) #                                     ] 
    if not rec[-1].get_moves(): # no moar moves                ]
        scenario.append(rec[:]) #                              ]
    rec.pop() #                                                ]
################################################################

def get_last_move(s): ##########################################
    z = s[-1] # last postion                                   _
    y = s[-2] # previous to last position                      _
    for j in range(buflen): #                                  _
        if y.buf[j] != z.buf[j]: #                             _
            return j # thats                                   _
################################################################        

def get_adj_sqrs(j): ###########################################
    adj = [] #                                                 ;
    for d in dir: #                                            ;
        if j in d: #                                           ;
            adj.append(d.index(j)) #                           ;
    return adj #                                               ;
################################################################

def ck_last_move(j, pos): ######################################
    adj = get_adj_sqrs(j) #                                    *
    for a in adj: #                                            *
        sides = pos.sides(a) #                                 *
        if sides.count('O') == 1: #                            *
            return 0 #                                         *
    return 1 #                                                 *
################################################################

def ck(s): #####################################################
    j = get_last_move(s) #                                     #
    return ck_last_move(j, s[-1]) #                            #
################################################################

load()
for g in games:
    print g.get_3side_boxes()
print    
walk(games[1])
for s in scenario:
    if ck(s):
        for r in s: print r
        break
############################################################ log:
