# About Python 100 Days
僅為學習過程中的隨手筆記。
[Python Tutorial](https://www.w3schools.com/python/)

## Day 1

- 線上 IDE：https://repl.it/
- 友善初學者的 IDE ：https://thonny.org/
- 資料型態：
  - 數值：`int()`、`float()`
  - 字串：`str()`
  - 列表：`list[]`
  - 集合：`set{}`
    - 運算
      - 聯集 `|`
      - 交集 `&`
      - 差集 `-`
      - XOR `^`
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
  - [Wiki - Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)
  - [Pseudorandom number generators](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators)
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

----

## Day 5

- [';--have i been pwned?](https://haveibeenpwned.com/)
- `for` 迴圈
- `range()`
  

> **Side Project：**
> 
> [Max min avg](https://github.com/49831117/Python-100-Days/blob/master/max_min_avg.py)
> 
> [Even sum](https://github.com/49831117/Python-100-Days/blob/master/even_sum.py)
> 
> [Fizz Buzz](https://github.com/49831117/Python-100-Days/blob/master/fizz_buzz.py)
> 
> [Password Generator](https://github.com/49831117/Python-100-Days/blob/master/password_generator.py)

----

## Day 6

- [Reeborg's World - Maze](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)
  - Tips：walk along the right-hand side ( or left-hand side ) wall.
    - [Reeborg's World - Maze 實作](https://github.com/49831117/Python-100-Days/blob/master/Reeborgs_World_Maze.md)

----

## Day 7

- [Wiki - Hangman (game)](https://en.wikipedia.org/wiki/Hangman_(game)) 
  - 紀錄思路，結合所學完成此遊戲。
  - [tool - flow chart maker](https://drow.io)
    - 此字庫與[ASCII](https://ascii.co.uk/art)可自行更換。

- 反思 
1. 改成 Bulls and cows？

> **Side Project：**
> 
> [Hangman](https://github.com/49831117/Python-100-Days/blob/master/hangman.py)

----

## Day 8

- creat a function
  1. 
    ```python
    # def function
    def func(): 
      to do
      
    # call function
    func() 
    ```
  2. 
    ```python
    # def function with 2 or more parameters
    def greet_with(name=" ", location=" "):
      print (f"Hello {name}!")
      print (f"Welcome to {location}!")

    # call function
    greet_with(location="TAIWAN", name = "Chi-Ling") 
    ```
- [Wiki - Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)


> **Side Project：**
> 
> [Hangman](https://github.com/49831117/Python-100-Days/blob/master/hangman.py)
>
> [Caesar-cipher](https://github.com/49831117/Python-100-Days/blob/master/caesar_cipher.py)

----

## Day 9

- dictionary
  ```python
  # build a dictionary
  programming_dict = {
    "Bug":"An error in a program that prevents the program from running as expectrd.",
    "Function":"A piece of code that you can easily call over and over again."
  }

  # retreive an item from the dictionary
  # fetching by key - should type exactly correct
  programming_dict["Bug"] 

  # adding new items to dictionary
  programming_dict["Loop"] = "The action of doing something over and over again."

  # creating an empty dictionary
  empty_dict = {}

  # wipe an existing dictionary
  programming_dict = {}

  # editing an item in dictionary
  programming_dict["Bug"] = "A moth in your computer."

  # loop through a dictionary
  for thing in programming_dict:
    print(thing) # print all keys
    print(programming_dict[thing]) # print all values
  ```
- nesting
  字典的 `value` 有許多種形式，如下：
  ```python
  {
    key1:value1,
    key2:[List],
    key3:{Dict}
  }
  ```
  1. Nesting dictionary in a dictionary
      ```python
      travel_log = {
        "China": {"cities_visited": ["Shanghai", "Beijin", "Nanjin"], "total_visits": 7},
        "Japan": {"cities_visited": ["Tokyo", "Osaka"], "total_visits": 2}
      }
      ```
  2. Nesting dictionary in a list
      ```python
      travel_log = [
        {
          "country": "China", 
          "cities_visited": ["Shanghai", "Beijin", "Nanjin"], 
          "total_visits": 7
        },
        {
          "country": "Japan",
          "cities_visited": ["Tokyo", "Osaka"], 
          "total_visits": 2
        }
      ]
      ```
- [VISUALIZE CODE EXECUTION](http://www.pythontutor.com/)
  - 與 [Thonny](https://thonny.org/) 相似

> **Side Project：**
> 
> [Grading Program](https://github.com/49831117/Python-100-Days/blob/master/grading_program.py)
>
> [Travel Log](https://github.com/49831117/Python-100-Days/blob/master/travel_log.py)
>
> [Blind Auction](https://github.com/49831117/Python-100-Days/blob/master/blind_auction.py)

----

## Day 10

- Function
