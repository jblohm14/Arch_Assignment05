# Overview

## Test Case 1
```
$ cat input1.txt | ./tokenizer.py | ./lowercase_filter.py | ./word_frequency_filter.py 2 | ./length_filter.py 4 6
```
### Input
```
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
No, I'm never gonna give you up
No, I'm never gonna let you down
No, I'll never run around and hurt you
I'll never, ever desert you
```
### Output
```
around
desert
down
give
gonna
hurt
i'll
never
```

## Test Case 2
```
$ cat input2.txt | ./tokenizer.py | ./lowercase_filter.py | ./word_frequency_filter.py 2 | ./length_filter.py 4 6
```
### Input
```
In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, 
filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy 
hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and 
that means comfort.
```
## Output
```
hobbit
hole
with
```

## Test Case 3
```
$ cat input3.txt | ./tokenizer.py | ./lowercase_filter.py | ./word_frequency_filter.py 2 | ./length_filter.py 4 6
```
### Input
```
It is a dark time for the Rebellion. Although the Death Star has been destroyed, Imperial troops have driven the Rebel forces from their hidden base and pursued them across the galaxy.

Evading the dreaded Imperial Starfleet, a group of freedom fighters led by Luke Skywalker has established a new secret base on the remote ice world of Hoth.
```
### Output
```
base
```