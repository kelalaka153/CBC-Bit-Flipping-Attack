# CBC-Bit-Flipping-Attack
CBC Bit-Flipping Attack Example with Python

CBC as a block cipher mode of operation has [Ind-CPA](https://crypto.stackexchange.com/q/26689/18298) secuirty and has no [Ind-CCA](https://crypto.stackexchange.com/q/26689/18298) security like any encryption mode that doesn't include integrity and authentication.

This simple python code written to demostrate how to execute the attack. This code is used for this question on Cryptography.SE

 - [Bit Flipping Attack on CBC Mode](https://crypto.stackexchange.com/q/66085/18298)

There is another [exampe](https://crypto.stackexchange.com/q/88338/18298) that uses full modification of the first block to surprize someone that AES has key that shifts!. Yes there can be such permutation from the family of the AES's permutations but this example is for fooling!

----
# Mitigation

To mitigate this kind of attacks one needs authentication. For CBC mode one can use HMAC with two keys. The two keys can be easily derived with [HKDF](https://crypto.stackexchange.com/q/76588/18298). 

Actually [CBC is no more in TLS 1.3](https://crypto.stackexchange.com/q/52566/18298) and new project must be get rid of it, too. Now we have 5 cipher suits

 - {0x13,0x01} - TLS_AES_256_GCM_SHA384
 - {0x13,0x02} - TLS_CHACHA20_POLY1305_SHA256
 - {0x13,0x03} - TLS_AES_128_GCM_SHA256
 - {0x13,0x04} - TLS_AES_128_CCM_8_SHA256
 - {0x13,0x05} - TLS_AES_128_CCM_SHA256

One must be carefull the [AES-GCM](https://crypto.stackexchange.com/q/84357/18298) since there are various traps.
