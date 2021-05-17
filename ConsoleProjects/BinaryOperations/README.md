# Binary operations

This is a simple program that uses binary operations to convert a number from integer to binary and also shows the
integer of the reversed binary representation of the number.

# How it works

The program uses two finctions

- to_bin()
- reverse_bin()

each function takes a list of integers as input and print the result.

The first function uses the builtin python function and just prints the number in binary format. There is a small
control for negative numbers where are automatically converted to positive numbers.

An example of use of this function is the following:
> to_bin([10])
>
> returns: '1010'

*It is important to pass the numbers always as a list format.*

The second function takes a list of integers and prints an integer of the reversed binary number

For example if we take the previous number '1010' (10 in decimal) the reversed binary would be
(assuming numbers are 32-bit) '1010000000000000000000000000000000'. We just transferred each bit 32 bits to the right
minus the length of the original number (4 in this case). Now if we convert this binary to integer it would be
equivalent to 10737418240

# Big0

Finally, to check the algorithm's behavior we calculate the Big0 notation. To do this we use the open python
library [big-O-calculator](https://pypi.org/project/big-O-calculator/). It runs automatically multiple times the
algorithms using different type of inputs (*check the documentation for further information*)

In our case both algorithms finish *N* number of operations for inputs size of *n*.

So the Big0 is `O(N)`.

<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Comparison_computational_complexity.svg/1024px-Comparison_computational_complexity.svg.png"
width="500" height="500">
</p>

*Image Source:Wikipedia*
