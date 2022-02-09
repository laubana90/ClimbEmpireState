# Climbing the Empire State

## Introduction

Imagine that you are walking up the Empire State building and playing a game with a friend: You throw a dice 100 times. Depending on the outcome you:

* 1/2 : go one step down
* 3/4/5: go one step up
* 6: throw again and go up the resulting number of steps

There are two additional considerations:
* You cannot go lower than step 0
* You have a chance of 0.1% of falling down and going back to step 0

You bet with your friend that you will reach step 60. What is the chance that you will win this bet?

## How it works
### Random walk

Your next step will be determined by the outcome of a dice roll, that means you will make a *random movement*. When you follow a succession of random movements, you are following a *random walk*, which is a well-known mathematical object. An example of random walks are the paths followed by molecules in a liquid or a gas.

We will use `random()`, a subpackage of `numpy`, to create the simulation. 

### Create a distribution

So far we have studied a single random walk. One way to know the probability of reaching step number 60 after 100 dice rolls is to compute the probability analytically. However, what we will do is to generate a set of random walks (pseudoexperiments) to create a distribution of end points. The larger the number of pseudoexperiments, the more accurate the probability will be. 

### Simulate multiple walks

We can use the function that we created above to generate a set of pseudoexperiments. We will store the outcomes in a `numpy` array.

### Compute the probability

Finally, we calculate the probability to reach at least step number X by the Y dice roll.

## About the repository
Contents of the repository:
* <code>ClimbEmpireState.py</code>: main python script to run the code
* <code>src/</code>
  * <code>utils.py</code>: module with functions to simulate the random walk and calculate probabilities
  * <code>plots.py</code>: module with functions to create figures to visualise the results
* <code>figures/</code>: directory containing the figures created 
* <code>input/</code>: 
  * config.ini: configuration file with initial parameters
* <code>notebook/</code>
  * EmpireState.ipynb: jupyter notebook for testing purposes

## How to use it
First, modify the configuration file to your desired inputs:
    * `number_of_dice_rolls` 
    * `minimum_step`
    * `number_of_pseudoexperiments`
    
You can then execute the code as:

`python3 ClimbEmpireState.py`

The output figures will be stored in the directory `figures`
