# cryptography

## RSA

The RSA method is an asymmetric public key cryptographic algorithm.
The user must independently generate two keys: one public and accessible to all that can be used by another user to encrypt the message to be sent, a private one known only by the user which is used to decrypt the message received.

Math behind RSA:

We choose two prime numbers p and q and define n = pq which we will call module. We also compute the euler function of n:

$$
\varphi(n) = n \Bigg[ \Bigg(1 - \frac{1}{p_1} \Bigg) \Bigg(1 - \frac{1}{p_2} \Bigg)...\Bigg(1 - \frac{1}{p_n} \Bigg)\Bigg]
$$

where the various $p_i$ are those that make up the decomposition of n

but as n is defined, we simply have:

$$
\varphi(n) =  (p-1)(q-1)
$$

We choose a number such that it is coprime with phi(n), that is GCD (e, phi(n)) = 1.

Now we are searching for a number d such that ed = 1 mod((p-1)(q-1)). To find d we use the Extended Euclidean algorithm which, in this case, states that:

$$
ex + \varphi(n)y = \text{GCD}(e, \varphi(n))
$$

Since e and phi (n) are coprime integers we have that x is the multiplicative inverse of e module phi (n) and y is the multiplicative inverse of phi (n) modulo e, so x=d.

If we have an 'm' message the encrypted message will be:

$$
c = m^e \text{mod}(n)
$$

and to decipher it

$$
m = c^d \text{mod}(n)
$$

we show that it is actually decrypted as mentioned:

$$
c^d \text{mod}(n) = m^{ed} \text{mod}(n) \qquad ed = 1 \text{ mod}(\varphi)(n)
$$

From the last equation we obtain, by definition of phi (n):

$$
ed = \text{mod}(p-1) \quad \text{and} \quad ed = \text{mod}(q-1) 
$$

Using, then, Fermat's little theorem we get:

$$
m^{ed} = m \text{ mod}(p) \quad \text{and} \quad m^{ed} = m \text{ mod}(q)
$$

We observe now that p and q are different prime numbers so we can use Chinese remainder theorem obtaining that:

$$
m^{ed} = m \text{ mod}(pq) \Rightarrow c^d = m \text{ mod}(n) 
$$

The power of the algorithm lies in the unproven assumption that deciphering the message without knowing the factors of n is computationally intractable (the factoring of a number is an operation with a sub exponential trend):

The fastest known algorithm to date is called General
Number Field Sieve, with a complexity in the order of:

$$
\mathcal{O}\Bigg(\exp \Bigg( \Bigg(\frac{64b}{9}\Bigg)^{1/3} \ln(b)^{2/3}\Bigg)\Bigg)
$$

Where b is the size (in bits) of the number from
factorize.
