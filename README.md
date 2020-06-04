# Monte_Carlo_Simulation
 Simulation of the game Craps.

## Goals

```
    Part 1: Roll 2 dice a specified number of times.
        - A win is 7 or 11
        - A loss is 2, 3, or 12
        - Continue to Part 2 if a roll was not a win or loss
    
    Part 2: Roll until win/loose
        - Win if re-roll number from Part 1 again
        - Loss if 7
```

## Results

This is a method to find the probability of winning craps by simulating the game a large number of times.
Speed is increased by using numpy arrays and masks to store the games and find results.

Using 10 million iterations, the solution results in a win 49.2% of the time.

Using 10 million iterations, the solution takes 1.4 seconds. Using 1 million iterations, the solution takes 0.13 seconds.