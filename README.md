# cryptography

## RSA

The RSA method is an asymmetric public key cryptographic algorithm.
The user must independently generate two keys: one public and accessible to all that can be used by another user to encrypt the message to be sent, a private one known only by the user which is used to decrypt the message received.


Math behind RSA:

We choose two prime numbers p and q and define n = pq which we will call module. We also compute the euler function of n:

<a href="https://www.codecogs.com/eqnedit.php?latex=\varphi(n)=n\cdot&space;\left[\left(1-\frac{1}{p_1}\right)\left(1-\frac{1}{p_2}\right)\cdots\left(1-\frac{1}{p_r}\right)\right]&space;=&space;n&space;\prod_{p\mid&space;n}&space;\left(1-\frac{1}{p}\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\varphi(n)=n\cdot&space;\left[\left(1-\frac{1}{p_1}\right)\left(1-\frac{1}{p_2}\right)\cdots\left(1-\frac{1}{p_r}\right)\right]&space;=&space;n&space;\prod_{p\mid&space;n}&space;\left(1-\frac{1}{p}\right)" title="\varphi(n)=n\cdot \left[\left(1-\frac{1}{p_1}\right)\left(1-\frac{1}{p_2}\right)\cdots\left(1-\frac{1}{p_r}\right)\right] = n \prod_{p\mid n} \left(1-\frac{1}{p}\right)" /></a>

where the various p_i are those that make up the decomposition of n

but as n is defined, we simply have:

<a href="https://www.codecogs.com/eqnedit.php?latex=\varphi(n)=(p-1)(q-1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\varphi(n)=(p-1)(q-1)" title="\varphi(n)=(p-1)(q-1)" /></a>

We choose a number such that it is coprime with phi(n), that is GCD (e, phi(n)) = 1.


Now we are searching for a number d such that ed = 1 mod((p-1)(q-1)). To find d we use the Extended Euclidean algorithm which, in this case, states that:


<a href="https://www.codecogs.com/eqnedit.php?latex=e&space;x&space;&plus;&space;\varphi(n)&space;y&space;=&space;GCD(e,&space;\varphi(n))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e&space;x&space;&plus;&space;\varphi(n)&space;y&space;=&space;GCD(e,&space;\varphi(n))" title="e x + \varphi(n) y = GCD(e, \varphi(n))" /></a>

Since e and phi (n) are coprime integers we have that x is the multiplicative inverse of e module phi (n) and y is the multiplicative inverse of phi (n) modulo e, so x=d.

If we have an 'm' message the encrypted message will be:

<a href="https://www.codecogs.com/eqnedit.php?latex=c=m^e&space;\hspace{1&space;mm}mod(n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c=m^e&space;\hspace{1&space;mm}mod(n)" title="c=m^e \hspace{1 mm}mod(n)" /></a>

and to decipher it

<a href="https://www.codecogs.com/eqnedit.php?latex=m=c^d&space;\hspace{1&space;mm}mod(n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?m=c^d&space;\hspace{1&space;mm}mod(n)" title="m=c^d \hspace{1 mm}mod(n)" /></a>


we show that it is actually decrypted as mentioned:

<a href="https://www.codecogs.com/eqnedit.php?latex=c^d&space;\hspace{1&space;mm}mod(n)&space;=&space;m^{ed}&space;\hspace{1&space;mm}mod(n)&space;\hspace{20&space;mm}&space;ed=1&space;\hspace{1&space;mm}&space;mod(\varphi(n))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c^d&space;\hspace{1&space;mm}mod(n)&space;=&space;m^{ed}&space;\hspace{1&space;mm}mod(n)&space;\hspace{20&space;mm}&space;ed=1&space;\hspace{1&space;mm}&space;mod(\varphi(n))" title="c^d \hspace{1 mm}mod(n) = m^{ed} \hspace{1 mm}mod(n) \hspace{20 mm} ed=1 \hspace{1 mm} mod(\varphi(n))" /></a>

From the last equation we obtain, by definition of phi (n):

<a href="https://www.codecogs.com/eqnedit.php?latex=ed&space;=&space;mod(p-1)&space;\text{&space;and&space;}&space;ed&space;=&space;mod(q-1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ed&space;=&space;mod(p-1)&space;\text{&space;and&space;}&space;ed&space;=&space;mod(q-1)" title="ed = mod(p-1) \text{ and } ed = mod(q-1)" /></a>

Using, then, Fermat's little theorem we get:

<a href="https://www.codecogs.com/eqnedit.php?latex=m^{ed}&space;=&space;m&space;~&space;mod(p)&space;\text{&space;and&space;}&space;m^{ed}&space;=&space;m&space;~&space;mod(q)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?m^{ed}&space;=&space;m&space;~&space;mod(p)&space;\text{&space;and&space;}&space;m^{ed}&space;=&space;m&space;~&space;mod(q)" title="m^{ed} = m ~ mod(p) \text{ and } m^{ed} = m ~ mod(q)" /></a>

We observe now that p and q are different prime numbers so we can use Chinese remainder theorem obtaining that:

<a href="https://www.codecogs.com/eqnedit.php?latex=m^{ed}&space;=&space;m&space;~&space;mod(pq)&space;\Rightarrow&space;c^d&space;=&space;m&space;~&space;mod(n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?m^{ed}&space;=&space;m&space;~&space;mod(pq)&space;\Rightarrow&space;c^d&space;=&space;m&space;~&space;mod(n)" title="m^{ed} = m ~ mod(pq) \Rightarrow c^d = m ~ mod(n)" /></a>


the power of the algorithm lies in the unproven assumption that deciphering the message without knowing the factors of n is computationally intractable (the factoring of a number is an operation with a sub exponential trend):

The fastest known algorithm to date is called General
Number Field Sieve, with a complexity in the order of:

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{O}(e^{(\frac{64}{9}b)^{\frac{1}{3}}&space;(\ln&space;b)^{\frac{2}{3}}}\)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathcal{O}(e^{(\frac{64}{9}b)^{\frac{1}{3}}&space;(\ln&space;b)^{\frac{2}{3}}}\)" title="\mathcal{O}(e^{(\frac{64}{9}b)^{\frac{1}{3}} (\ln b)^{\frac{2}{3}}}\)" /></a>

Where b is the size (in bits) of the number from
factorize.

