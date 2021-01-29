# About Python 100 Days
> 僅為學習過程中的隨手筆記。

## Day 1
- 線上 IDE：https://repl.it/
- 友善初學者的 IDE ：https://thonny.org/
- 資料型態：
  - 數值：`int()`、`float()`
  - 字串：`str()`
  - 列表：`list[]`
  - 集合：`set{}`
    - 運算
      1. 聯集 `|`
      2. 交集 `&`
      3. 差集 `-`
      4. XOR `^`
  - 元組：`tuple()`
  - 字典：`{}`
  - 布林值：True、False
  - `print(str1 + str2)`及`print(str1, str2)`的差異
- 運算子：+、-、*、/、//、% 
- `input()`
- `print()`

> **Side Project：**
> 
> [Band Name Generator](https://github.com/49831117/Python-100-Days/blob/master/band-name-generator.py)

----

## Day 2
- 運算子的運用
- ***f-string***
- `round( float, decimal places)`：浮點數的小數位數
  
> **Side Project：**
> 
> [Tips Calculator](https://github.com/49831117/Python-100-Days/blob/master/tips_calculator.py)
> 
> [Your Life](https://github.com/49831117/Python-100-Days/blob/master/your_life.py)

----

## Day 3
- if/elif/else
- `str.count( sub, start = 0, end = len(string) )`

> **Side Project：**
> 
> [Roller Coaster Ticket](https://github.com/49831117/Python-100-Days/blob/master/roller_coaster_ticket.py)
> 
> [Love Calculator](https://github.com/49831117/Python-100-Days/blob/master/love_calculator.py)

----

## Day 4
- `import random`
  - `random.randint(a, b)` : random integer belongs to [a, b]
  - `random.random()` : [0, 1) 之間隨機的浮點數
  - `random.uniform(a, b)` : [a, b]中隨機的浮點數
- `sorted()`：重新排列大小
  - `sorted`和`sort`的差異
- `list = []`
- 新增自己的 module：
  開新 .py 檔案（如：mymodule.py）
        ---- mymodule.py ----
        pi = 3.1415926
    `print( mymodule.pi )`：叫出 mymodule.py 中的 pi 函數
- [NOTE - List](https://docs.python.org/3/tutorial/datastructures.html#data-structures)


- 反思 
1. 若事先決定「贏」、「輸」、「平手」，搭配 array 的可行性？


> **Side Project：**
> 
> [Toss A Coin](https://github.com/49831117/Python-100-Days/blob/master/toaa_a_coin.py)
> 
> [Who Pay?](https://github.com/49831117/Python-100-Days/blob/master/who_pay.py)
> 
> [Treasure Map](https://github.com/49831117/Python-100-Days/blob/master/treasure_map.py)
> 
> [Paper Scissors Stone](https://github.com/49831117/Python-100-Days/blob/master/paper_scissors_stone.py)


##### 反思 
1. 若事先決定「贏」、「輸」、「平手」，搭配 array 的可行性？