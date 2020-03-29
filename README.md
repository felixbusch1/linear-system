# Linear system of equations

This python script solves linear systems of equations

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install numpy.

```bash
pip install numpy
```

## Usage

You just have to do 3 steps.
1) Open solve.py
2) Edit your inputs.

Setup your matrix, for example like this

```python
matrix = np.matrix('1 -2 4; 4 3 -4; 1 5 6')
```
Then set the dimension, in this example is n=3
```python
n = 3
```
The last thing to edit is to set your solution vector.
```python
svector = [7, -1, -5]
```

Then you have this system
# 1x -2y + 4z = 7  
# 4x +3y -4z = -1 
# 1x +5y + 6z = -5 

The output is numerated like this: x1, x2..., xn

So in this example x1 = x, x2 = y and x3 = z

3) Run the script with
```bash
python solve.py
```
and you should get your results.
