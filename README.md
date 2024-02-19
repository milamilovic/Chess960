# Ficher random chess (Chess960) 

## Authors
Sonja Baljicki and Mila Milović

## Problem Description
The Fischer random chess (Chess960) problem, invented by American chess grandmaster and former world champion Bobby Fischer, needs to be solved. This problem is called Chess960 because there are 960 possible combinations that players can get. The constraints for solving the problem are as follows:

The pawns are located on the usual fields
Other figures are in the first row
The king is placed on any field between two rooks, it cannot be placed on fields a and h because then there would be no place for the rook
Bishops are placed on two fields of different colors
All given constraints must be respected, and a satisfactory arrangement of figures must be found. The optimality criterion is that the arrangement of figures should be as close as possible to the arrangement of figures in regular chess. Because the arrangement of figures in the classic version of chess satisfies the constraints of the problem, the algorithm usually finds that arrangement. A genetic algorithm will be used for implementation.

## Introduction
The genetic algorithm is inspired by Charles Darwin's theory of natural evolution. This algorithm mimics the process of natural selection where the most capable individuals are selected for reproduction, crossbreeding, to produce offspring of the next generation, so that their fitness value (measure of their ability) is as good as possible. The genetic algorithm procedure is as follows:

Initialization of the initial population
Calculating the fitness function
Iterate:
Selection
Crossing
Mutation
Calculating the fitness function

## Implementation
The implementation starts by defining individuals needed for further work of the genetic algorithm. One individual represents an array of numbers from 1 to 5, where 1: rook, 2: knight, 3: bishop, 4: queen, and 5: king. The first generation is formed by creating an array of 10 elements that are permutations of the basic arrangement of figures.

Permutations are implemented using a function specifically made for this problem, to avoid a large number of invalid arrangements, which would further cause the program to execute very slowly. The function consists of several parts:

First, the king is placed in a random position with an index between 1 and 6, which is any position except the end ones.
After that, the rooks are placed one by one, with the first one placed in a random position to the left of the king, and the second one to the right.
Bishops are placed in random positions until the indices are different congruent modulo 2, meaning one bishop is on a black square and the other on a white square.
After the bishops are placed, the queen is placed in a random free location.
Finally, knights are placed in the remaining free positions.
After generating the initial population, we enter the genetic algorithm loop, where the population is ranked first. The ranking function returns a list containing individuals from the initial population, sorted in ascending order by the fitness value criterion.

The fitness value is calculated as the sum of the distances between the position of each figure and its position in the classical chess arrangement, because the optimality criterion is the arrangement most similar to the regular chess arrangement.

Roulette selection allows pairs of parents to be formed from the population, which will be crossed in the next phase to produce the next generation. In roulette selection, the fitness value of each individual is multiplied by a randomly chosen value, which leads to diversity in pairs. This avoids the situation where the genetic algorithm selects only the best individuals. Also, together with mutation, it prevents the algorithm from ending up at a local instead of a global optimum.

The next phase is crossing previously made parent pairs to produce one child from one pair of parents. The first attempt at implementation worked as follows: the last n positions of one parent were replaced with the last n positions of the other, creating two children. However, this way, children with an arrangement of figures that did not match the conditions of Fischer chess were obtained. Even worse, children did not have the appropriate number of each figure. Putting crossing into a for loop that ended only when a valid solution was found did not help because this for loop executed for several minutes. For the above reasons, a special function for crossing was composed. Its algorithm is as follows:

First, it checks if the king of the first parent is at a position that is between the positions of the second parent's rooks. If yes, the king and rooks are placed like this. If not, the opposite is checked. If neither is valid, the king and rooks are placed in positions like those of the first parent.

It is checked whether the bishops can be placed on the board, one from one parent, and the other from the other parent. If this is not possible, we try to place bishops on the positions of the second parent, then on the positions of the first parent. If this is also not possible, the bishops are placed on random positions that satisfy the condition of being on squares of different colors.

After placing the bishops, we try to place the queen on the second parent's position, then on the queen's position in the first parent. If none of the previous methods are successful, the queen is placed in a random position.

Finally, we place the knights on the remaining free positions.

After crossing comes the mutation of the obtained children. Mutation allows genetic diversity. It happens by there being a small probability for each child that two figures will change places. The probability is set to 0.1 because a higher probability would produce too many invalid positions or arrangements, and a lower one would result in mutation having too small an impact.

Elitism, i.e., forming a new generation, allows new initial populations to be formed from parents and children for the next iteration. The parameter of the function that performs elitism is a coefficient representing what percentage of children and what percentage of parents make up the new generation. By testing the program, it was concluded that the coefficient 0.5 best suits the Fischer chess problem.

## Preview
![Example of console output](C:\Users\computer\Videos\Captures\sah960.png)
![Example of graph](C:\Users\computer\Videos\Captures\chess960graph.png)

## Conclusion
The program has several parameters, the values of which were chosen through testing:

Population size → 10

Number of iterations of the main for loop → 50

Mutation coefficient → 0.1

Elitism coefficient → 0.5
After running the program, a graph is drawn where the x-axis represents the number of iterations, and the y-axis represents the fitness values of individuals. This graph helps us in analyzing the efficiency of the program in finding a solution because it is easy to read to which value individuals converge. The result of the program's execution is usually an individual with a fitness value in the interval [0,4], because those are the sequences that are closest to the regular sequence, which is the optimality criterion. Some of the results of the program's work are:

♖ ♘ ♔ ♕ ♗ ♗ ♘ ♖ --> fitness value is 4

♖ ♘ ♗ ♔ ♕ ♗ ♖ ♘ --> fitness value is 4

♖ ♘ ♗ ♔ ♕ ♗ ♘ ♖ --> fitness value is 2

♖ ♘ ♗ ♕ ♔ ♗ ♖ ♘ --> fitness value is 2

♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ --> fitness value is 0

Given that the program's result is approximately 50% of the time a sequence with a fitness value of 0, we can conclude that solving this problem with a genetic algorithm gives satisfactory results.
