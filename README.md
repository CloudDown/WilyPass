# WilyPass - Ultimate Password List Creator

<img align="center" width="60%" alt="Wilypass Terminal" src="https://i.imgur.com/RnzQ2PI.png"/>

## Introduction

WilyPass is a powerful password list creator designed for Linux and Windows users. This Python script generates diverse password variations based on provided keywords, incorporating prefixes, numbers, special characters, and more.

## Features

- **Cross-Platform Compatibility** : Supports both Linux and Windows environments.
- **Variant Creation** : Generates a wide range of password variants for enhanced security.
- **Dynamic Prefixing** : Incorporates dynamic prefixing based on user-defined weights and complexity levels.
- **Number Lists** : Includes numerical variations to increase password complexity.
- **Strange Characters** : Integrates popular special characters for added strength.
- **Charge-Bar Visualization** : Displays a progress bar for password list creation.

## 🛠️ Installation

```bash
git clone https://github.com/CloudDown/WilyPass.git
cd WilyPass/
python3 wilypass.py
```

## 🍕 Mods :

### Prefix :
This feature takes the first 1, 2, 3... letters of your keyword and adds them to the search. For example, if your keyword is 'John' and you choose a prefix of three letters, the list added to the algorithm will be :
```python
['j', 'jo','joh']
```
‎
### Number :
Add a list of numbers to the algorithm. For example, choose a limit of 10 numbers :
```python
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```
‎
### Strange :
Incorporate popular special characters into the algorithm :
```python
['', '!', '@', '/#', '$', '!@', '!@#', '!@#$', '123!', '!123', '1@']
```
‎
### Charge-Bar :
Simply to visualize the progress of password creation :
```
[############################################################################........................] 76% ( 76/100 words )
```

