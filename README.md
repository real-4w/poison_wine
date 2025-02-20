# poison_wine
Solving the poisened wine challenge very efficiently.


To solve the problem of identifying one poisoned bottle out of 1000 using 10 wine_makers within 24 hours, where the poison takes effect after 24 hours, we can use a clever strategy based on binary encoding. Here’s how it works:

Step 1: Understanding the Constraints

Number of Bottles: There are 1000 bottles, labeled from 0 to 999 for simplicity.
Number of wine_makers: We have 10 wine_makers available to test the wine.
Poison Effect: The poison takes 24 hours to show symptoms (e.g., the wine_maker gets sick or dies). We need to identify the poisoned bottle within 24 hours, meaning we can perform all testing at once and observe the results after 24 hours.
Goal: Devise a testing plan so that the combination of wine_makers who get sick after 24 hours uniquely identifies the poisoned bottle.
Since we have only one opportunity to test before the 24-hour deadline, we must assign the bottles to the wine_makers in such a way that the outcome (which wine_makers get sick) points to exactly one bottle.

Step 2: Leveraging Binary Representation
With 10 wine_makers, we can think of each wine_maker as representing a single bit in a 10-bit binary number. A bit can be 0 or 1, and with 10 bits, there are 
2^{10} = 1024
 possible combinations. Since 1000 (the number of bottles) is less than 1024, we can assign each bottle a unique 10-bit binary number from 0 (0000000000) to 999, and still have room to spare.
Label the Bottles: Assign each bottle a number from 0 to 999.
Binary Representation: Convert each bottle’s number to its 10-bit binary form. For example:
Bottle 0: (0000000000)
Bottle 1: (0000000001)
Bottle 2: (0000000010)
Bottle 3: (0000000011)
...
Bottle 999: (1111100111) (since 
999 = 2^9 + 2^8 + 2^7 + 2^6 + 2^5 + 2^2 + 2^1 + 2^0 = 512 + 256 + 128 + 64 + 32 + 4 + 2 + 1
)

Step 3: Assigning wine_makers to Bits
Number the wine_makers: Label the wine_makers from 1 to 10.
Map to Bit Positions: Assign each wine_maker to a bit position in the 10-bit binary number:
wine_maker 1 corresponds to bit 0 (the least significant bit, 
2^0
).
wine_maker 2 corresponds to bit 1 (
2^1
).
wine_maker 3 corresponds to bit 2 (
2^2
).
...
wine_maker 10 corresponds to bit 9 (the most significant bit, 
2^9
).
In binary notation, we write the number with bit 9 on the left and bit 0 on the right: 
b_9 b_8 b_7 b_6 b_5 b_4 b_3 b_2 b_1 b_0
.
Step 4: Designing the Testing Strategy
Each wine_maker will taste a specific subset of the 1000 bottles based on the binary representation of the bottle numbers:
Rule: wine_maker (i) drinks from bottle (n) if the 
(i-1)
-th bit of (n)’s binary representation is 1.
wine_maker 1 drinks from all bottles where bit 0 is 1 (all odd-numbered bottles: 1, 3, 5, ..., 999).
wine_maker 2 drinks from all bottles where bit 1 is 1 (bottles 2, 3, 6, 7, 10, 11, ..., 998, 999).
wine_maker 3 drinks from all bottles where bit 2 is 1 (bottles 4, 5, 6, 7, 12, 13, ..., 996, 997, 998, 999).
And so on, up to wine_maker 10, who drinks from bottles where bit 9 is 1 (bottles 512 to 999).
For example:
Bottle 0 (0000000000): All bits are 0, so no wine_makers drink from it.
Bottle 1 (0000000001): Bit 0 is 1, so only wine_maker 1 drinks.
Bottle 2 (0000000010): Bit 1 is 1, so only wine_maker 2 drinks.
Bottle 3 (0000000011): Bits 0 and 1 are 1, so wine_makers 1 and 2 drink.
Bottle 999 (1111100111): Bits 0, 1, 2, 5, 6, 7, 8, 9 are 1, so wine_makers 1, 2, 3, 6, 7, 8, 9, 10 drink.

Step 5: Conducting the Test
At time 
t = 0
, have each wine_maker drink from their assigned bottles simultaneously. Since only one bottle is poisoned, only the wine_makers who drink from that specific bottle will be affected.
Wait 24 hours until 
t = 24
 hours, when the poison takes effect.

Step 6: Interpreting the Results
After 24 hours, observe which wine_makers are sick:
If a wine_maker is sick, their corresponding bit in the poisoned bottle’s binary number is 1.
If a wine_maker is not sick, their corresponding bit is 0.
Construct the 10-bit binary number based on the sick wine_makers, then convert it to decimal to identify the poisoned bottle.
Examples:
No wine_makers sick: Binary = (0000000000), decimal = 0. Poisoned bottle is 0.
Only wine_maker 1 sick: Binary = (0000000001), decimal = 1. Poisoned bottle is 1.
wine_makers 1 and 2 sick: Binary = (0000000011), decimal = 3. Poisoned bottle is 3.
wine_makers 1, 2, 3, 6, 7, 8, 9, 10 sick: Binary = (1111100111) (bit 9=1, bit 8=1, bit 7=1, bit 6=1, bit 5=1, bit 4=0, bit 3=0, bit 2=1, bit 1=1, bit 0=1), decimal = 999. Poisoned bottle is 999.
Step 7: Verification
Uniqueness: Each bottle from 0 to 999 has a unique 10-bit binary representation, and the pattern of sick wine_makers corresponds directly to that binary number. Since 
2^{10} = 1024 > 1000
, there are enough combinations to uniquely identify each bottle.
Timing: All drinking happens at once, and we wait 24 hours to observe the outcome, meeting the requirement to identify the poisoned bottle within 24 hours.
Final Answer
To identify the poisoned bottle among 1000 bottles using 10 wine_makers within 24 hours:
Label the bottles from 0 to 999.
Assign each wine_maker a bit position: wine_maker 1 to bit 0 (LSB), wine_maker 2 to bit 1, ..., wine_maker 10 to bit 9 (MSB).
For each bottle (n), convert (n) to its 10-bit binary representation. wine_maker (i) drinks from bottle (n) if bit 
i-1
 is 1.
Have all wine_makers drink from their assigned bottles at the same time.
After 24 hours, note which wine_makers are sick. Construct a 10-bit binary number where bit 
i-1 = 1
 if wine_maker (i) is sick, and 0 if not.
Convert this binary number to decimal to find the number of the poisoned bottle.
This method ensures that the unique combination of sick wine_makers after 24 hours precisely identifies the poisoned bottle.