# Name: Garrett DesRosiers
# Description:
# Class: CSC 349-03
# Programming Assignment #3

import sys

#Input: Two strings (x and y) and a scoring matrix
#The match between the two strings with the highest score, and the score

def get_inputs(filename):
  fp = open(filename, "r")
  inputs = fp.read().split('\n')
  fp.close()
  x = inputs[0]
  y = inputs[1]
  for i in range(2, len(inputs)):
     inputs[i] = inputs[i].split(' ')
  scoring_matrix = inputs[3:(len(inputs)-1)]
  for j in range(len(scoring_matrix)):
     scoring_matrix[j] = scoring_matrix[j][1:]
     for k in range(len(scoring_matrix[j])):
         scoring_matrix[j][k] = int(scoring_matrix[j][k])
  return (x, y, scoring_matrix)

def get_score(x_char, y_char, scoring_matrix):
   l = ['A', 'C', 'G', 'T', '-']
   row = l.index(x_char)
   column = l.index(y_char)
   return scoring_matrix[row][column]

def populate_table(x, y, scoring_matrix):
   table = [[[0, "", ""] for x_character in range(len(x)+1)] for y_character in range(len(y)+1)]
   for k in range(1, len(table)):
      table[k][0][1] = table[k-1][0][1] + "-"
      table[k][0][2] = table[k-1][0][2] + y[k-1]
   for l in range(1, len(table[0])):
      table[0][l][1] = table[0][l-1][1] + x[l-1]
      table[0][l][2] = table[0][l-1][2] + "-"
   for i in range(1, len(table)):
      for j in range(1, len(table[i])):
         up = table[i-1][j][0] + get_score('-', y[i-1], scoring_matrix)
         left = table[i][j-1][0] + get_score(x[j-1], '-', scoring_matrix)
         diag = table[i-1][j-1][0] + get_score(x[j-1], y[i-1], scoring_matrix) 
         maximum = max(up, left, diag)
         if (maximum == diag):
            table[i][j][0] = diag
            table[i][j][1] = table[i-1][j-1][1] + x[j-1]
            table[i][j][2] = table[i-1][j-1][2] + y[i-1]
         elif (maximum == left):
            table[i][j][0] = left
            table[i][j][1] = table[i][j-1][1] + x[j-1]
            table[i][j][2] = table[i][j-1][2] + '-'
         elif (maximum == up):
            table[i][j][0] = up
            table[i][j][1] = table[i-1][j][1] + '-'
            table[i][j][2] = table[i-1][j][2] + y[i-1]
   return table[len(table)-1][len(table[0])-1]

def main(argv):
   inputs = get_inputs(argv[1])
   x = inputs[0]
   y = inputs[1]
   scoring_matrix = inputs[2]
   outputs = populate_table(x, y, scoring_matrix)
   x = [outputs[1][i] for i in range(len(outputs[1]))]
   y = [outputs[2][j] for j in range(len(outputs[2]))]
   x = " ".join(x)
   y = " ".join(y)
   print("x: " + x)
   print("y: " + y)
   print("Score: " + str(outputs[0]))
   
if __name__ == "__main__":
   main(sys.argv) 
