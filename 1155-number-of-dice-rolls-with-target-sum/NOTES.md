We start noticing that if t>nk then we must return 0.
​
If t <= nk, then we can think recursively. Indeed, let $f(n,k,t)$ be the number of ways you can roll n-dices, numbered from 1 to k, and get a sum of t. Hence the following recursion formula holds:

$f(n,k,t) = sum_{j=1}^k f(n-1,k,t-j)$

Where the base cases correspond to n=1, and for these cases we have
f(1,k,t)= 0 if k<t or t<0, 1 otherwise.
​
In the presented solution we follow this approach using Dynamic programing, i.e. we implement the above idea in an iterative manner.
