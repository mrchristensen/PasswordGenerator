# Password File Generator

This project replicates the format that unix stores passwords ([/etc/passwd](https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/) and [/etc/shadow](https://www.cyberciti.biz/faq/understanding-etcshadow-file/)) in order to study the stength of weaknesses of different passwords and formats against password cracking.

For the methodology and results, see [Report.pdf](Project%207%20-%20Password%20Cracking%20Report.pdf).

For the implementation, see [main.py](main.py).

Not included is the rockyou.txt file (of cracked passwords).

## Commands

```python3 main.py us password123```

```unshadow passwd shadow > unshadowed-.txt```

```john -wordlist="rockyou.txt" unshadowed.txt```
