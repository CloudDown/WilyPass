# WilyPass
WilyPass is a password list creator based on keywords.

<img align="center" width="60%" alt="Wilypass Terminal" src="https://i.imgur.com/RnzQ2PI.png"/>

## 🛠️ Installation

```bash
git clone https://github.com/CloudDown/WilyPass.git
cd WilyPass/
python3 wilypass.py
```
‎ 
‎ 
‎ 

## 🍕 Mods :

### Prefix :
This feature takes the first 1, 2, 3... letters of your keyword and adds them to the search. For example, if your keyword is 'John' and you choose a prefix of three letters, the list added to the algorithm will be :
```python
['j', 'jo','joh']
```

### Number :
Add a list of numbers to the algorithm. For example, choose a limit of 10 numbers :
```python
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

### Strange :
Incorporate popular special characters into the algorithm :
```python
['', '!', '@', '/#', '$', '!@', '!@#', '!@#$', '123!', '!123', '1@']
```

### Charge-Bar :
Simply to visualize the progress of password creation :
```
[############################################################################........................] 76% ( 76/100 words )
```

