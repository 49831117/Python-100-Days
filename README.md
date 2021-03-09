# About Python 100 Days
僅為學習過程中的隨手筆記。

[Python Tutorial](https://www.w3schools.com/python/)

1. 初階練習（Day1～Day14）
2. 中階練習（Day15～Day57）
3. 高級練習（Day57～Day79）
4. 專業練習（Dat80～Day100）


   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|
   |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
   |[Day 1](https://github.com/49831117/Python-100-Days#day-1) | [Day 2](https://github.com/49831117/Python-100-Days#day-2) |  [Day 3](https://github.com/49831117/Python-100-Days#day-3) | [Day 4](https://github.com/49831117/Python-100-Days#day-4) | [Day 5](https://github.com/49831117/Python-100-Days#day-5) | [Day 6](https://github.com/49831117/Python-100-Days#day-6) |  [Day 7](https://github.com/49831117/Python-100-Days#day-7) | [Day 8](https://github.com/49831117/Python-100-Days#day-8) | [Day 9](https://github.com/49831117/Python-100-Days#day-9) | [Day 10](https://github.com/49831117/Python-100-Days#day-10)
   |[Day 11](https://github.com/49831117/Python-100-Days#day-11) | [Day 12](https://github.com/49831117/Python-100-Days#day-12)|[Day 13](https://github.com/49831117/Python-100-Days#day-13)|[Day 14](https://github.com/49831117/Python-100-Days#day-14)


----
# 初階
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
> [Band Name Generator](https://github.com/49831117/Python-100-Days/blob/master/.py/band_name_generator.py)

----

## Day 2

- 運算子的運用
- ***f-string***
- `round( float, decimal places)`：浮點數的小數位數

  
> **Side Project：**
> 
> [Tips Calculator](https://github.com/49831117/Python-100-Days/blob/master/.py/tips_calculator.py)
> 
> [Your Life](https://github.com/49831117/Python-100-Days/blob/master/.py/your_life.py)

----

## Day 3

- if/elif/else
- `str.count( sub, start = 0, end = len(string) )`


> **Side Project：**
>
> [Leap Year](https://github.com/49831117/Python-100-Days/blob/master/.py/leap_year.py)
>
> [Roller Coaster Ticket](https://github.com/49831117/Python-100-Days/blob/master/.py/roller_coaster_ticket.py)
> 
> [Love Calculator](https://github.com/49831117/Python-100-Days/blob/master/.py/love_calculator.py)

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
> [Toss A Coin](https://github.com/49831117/Python-100-Days/blob/master/.py/toaa_a_coin.py)
> 
> [Who Pay?](https://github.com/49831117/Python-100-Days/blob/master/.py/who_pay.py)
> 
> [Treasure Map](https://github.com/49831117/Python-100-Days/blob/master/.py/treasure_map.py)
> 
> [Paper Scissors Stone](https://github.com/49831117/Python-100-Days/blob/master/.py/paper_scissors_stone.py)

----

## Day 5

- [';--have i been pwned?](https://haveibeenpwned.com/)
- `for` 迴圈
- `range()`
  

> **Side Project：**
> 
> [Max min average](https://github.com/49831117/Python-100-Days/blob/master/.py/max_min_avg.py)
> 
> [Even sum](https://github.com/49831117/Python-100-Days/blob/master/.py/even_sum.py)
> 
> [Fizz Buzz](https://github.com/49831117/Python-100-Days/blob/master/.py/fizz_buzz.py)
> 
> [Password Generator](https://github.com/49831117/Python-100-Days/blob/master/.py/password_generator.py)

----

## Day 6

- [Reeborg's World - Maze](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)
  - Tips：walk along the right-hand side ( or left-hand side ) wall.
    - [Reeborg's World - Maze 實作](https://github.com/49831117/Python-100-Days/blob/master/.py/Reeborgs_World_Maze.md)

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
> [Hangman](https://github.com/49831117/Python-100-Days/blob/master/.py/hangman.py)

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
> [Prime Checker](https://github.com/49831117/Python-100-Days/blob/master/.py/prime_checker.py)
>  
> [Caesar-cipher](https://github.com/49831117/Python-100-Days/blob/master/.py/caesar_cipher.py)

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
> [Grading Program](https://github.com/49831117/Python-100-Days/blob/master/.py/grading_program.py)
>
> [Travel Log](https://github.com/49831117/Python-100-Days/blob/master/.py/travel_log.py)
>
> [Blind Auction](https://github.com/49831117/Python-100-Days/blob/master/.py/blind_auction.py)

----

## Day 10

- Function
  [Format Name](https://github.com/49831117/Python-100-Days/blob/master/format_name.py)
  1. `string.capitalize()` 及 `string.title()` 的應用
  2. `return` 紀錄 function 的回傳值，同時結束該 function，意即：不論 `return` 後還有多少指令，皆不執行。
- **Docstring**
    ```python
    def func(a, b):
      """docstring"""
      define func(a, b) here
    ```


> **Side Project：**
> 
> [Leap Year 2](https://github.com/49831117/Python-100-Days/blob/master/.py/leap_year2.py)
> 
> [Calculator](https://github.com/49831117/Python-100-Days/blob/master/.py/calculator.py)

----

## Day 11

- 綜合前面 10 天內容，完成簡單的 Blackjack 遊戲。
- 實際玩玩看：[Online Free Blackjack](https://games.washingtonpost.com/games/blackjack/)
- **Regularly test your code so that you don't wait until the end when they're a lot of problem.**
- To do list
  - [ ] Deal both user and computer a starting hand of 2 random card values.
  - [ ] Detect when computer or user has a blackjack. (Ace + 10 value card).
  - [ ] If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a blackjack, then they win (unless the computer also has a blackjack).
  - [ ] Calculate the user's and computer's scores based on their card values.
  - [ ] If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
  - [ ] Reveal computer's first card to the user.
  - [ ] Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
  - [ ] Ask the user if they want to get another card.
  - [ ] Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.
  - [ ] Compare user and computer scores and see if it's a win, loss, or draw.
  - [ ] Print out the player's and computer's final hand and their scores at the end of the game.
  - [ ] After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.


> **Side Project：**
> 
> [Black Jack](https://github.com/49831117/Python-100-Days/blob/master/.py/blackjack2.py)

----

## Day 12

- Scope
  1. local scope: exist within functions
  2. global scope
  - difference: where you define or where you create the variables or the functions
  - name space
  - **Dose Python have block space?** ans: NO. But in C++, Java, etc.
  - 如果要在自訂函數中呼叫 global variable？
      ```python
      enemies = 1
      def increase_enemies():
        global enemies ### 在函數中使用 global 呼叫該變數
        enemies += 1
      ```
      - 但缺點是容易混淆甚至產生 bug，故應盡量避免使用。
      - **Avoid modifying global variable.**
      - **替代方案** 使用 `return`
      ```python
      def increase_enemies():
        return enemies + 1
      enemies = increase_enemies()
      ```
- Python constants and global scope
  - globe variable 應小心使用
  - 但可以用在不變的常數，如：PI。（使用上習慣全大寫拼寫，以利分辨。）
- [Text to ASCII Art Generator(TAAG)](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)

> **Side Project：**
> 
> [The Number Guessing Game](https://github.com/49831117/Python-100-Days/blob/master/.py/the_number_guessing_game.py)

----

## Day 13

- **Steps to Debug**
  > It's an important part of every programmer's journey.
  1. Describe the problem.
      > Untangle the problem and try to make sense of what's going on.
  2. Reproduce the bug.
      > Sometimes the bug not show up in the first time.
  3. Play computer.
  4. Fix the errors
  5. Use `print()`.
  6. Use a debugger.
      > [Python Tutor](http://www.pythontutor.com/visualize.html#mode=edit) (onlone debugger)
  7. Take a break.
  8. Ask your friend.
  9. Run often.
      > If you do end up in that situation and you can see multiple bugs at the same time, try to tackle them one at a time instead of trying to do bits and bobs of each.
  10. Ask Stack Overflow.

- [7 Steps to Debug Efficiently and Effectively](https://www.codementor.io/@mattgoldspink/how-to-debug-code-efficiently-and-effectively-du107u9jh)

----

## Day 14

- 玩玩看：[The Higher Lower Game](http://www.higherlowergame.com/)
  - Step 1. 觀察遊戲規則，完成 flow chart
  - Step 2. Break down the problem
  - Step 3. To - do list
    1. 讀取 `game_data.py` 資料 (a list of a dictionary)
    2. 將字典中資訊組成語句印出
    3. `input()` 使用者猜測值
    4. 比較、印出猜測結果
  - Step 4. Turn the problem into comments

> **Side Project：**
> 
> [Higher Lower](https://github.com/49831117/Python-100-Days/blob/master/.py/higher_lower.py)
> 
----

## Day 15

- IDE, Integrated Development Environment
  1. Download Python：https://www.python.org/downloads/
      > "Disable path length limit." → (click) → "Do you want to allow this app to make changes to your device?"  → (click 'Yes')
  2. Install PyCharm (Community is FREE)：https://www.jetbrains.com/pycharm/download/
      - Build-in Linter
        > [PEP 8](https://www.python.org/dev/peps/pep-0008/)
      - Local history：Last 12 hours
      - View structure
      - Refactor rename
      - [PyCharm keyboard shortcut - Running and debugging](https://www.jetbrains.com/help/pycharm/running-and-debugging-shortcuts.html?keymap=secondary_windows)
- emoji
  - [Windows 10 keyboard tips and tricks](https://support.microsoft.com/en-us/windows/windows-10-keyboard-tips-and-tricks-588e0b72-0fff-6d3f-aeee-6e5116097942)
  - [Use emoji and symbols on Mac](https://support.apple.com/en-gb/guide/mac-help/mchlp1560/mac)

- [Coffee Machine Program Requirements](https://github.com/49831117/Python-100-Days/blob/master/.pdf/Coffee%2BMachine%2BProgram%2BRequirements.pdf)
  - 根據此表完成[Coffee Machine]()
----

## Day 25

- [pandas documentation](https://pandas.pydata.org/docs/)
- [pandas API reference](https://pandas.pydata.org/docs/reference/index.html)
- common seperated values
- weather_data.csv
    |day|temp|condition|
    |:---:|:---:|:---:|
    |Monday|12|Sunny|
    |Tuesday|14|Rain|
    |Wednesday|15|Rain|
    |Thursday|14|Cloudy|
    |Friday|21|Sunny|
    |Saturday|22|Sunny|
    |Sunday|24|Sunny|

  **to-do 1**
  1. open up this file.
  2. add each line of data into a list which we'll called data.
    ```python
    # 讀取 .csv 檔，存在 data
    with open(".py\\weather_data.csv") as data_file:
      data = data_file.readlines()
      print(data)
    ```
- `import pandas`  
- [2018 Central Park Squirrel Census - Squirrel Data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)
    - 計算各毛色數量
        > 只有三種顏色
          ||Primary Fur Color|Count|
          |:---:|:---:|:---:|
          |0|Gray||
          |1|Cinnamon||
          |2|Black||
- [Sporcle - Can you name the US states?](https://www.sporcle.com/games/g/states)
    - [Get mouse click coordinates in Python turtle](https://stackoverflow.com/questions/42878641/get-mouse-click-coordinates-in-python-turtle)

> **Side Project**
> 
> [Name The States Game](https://github.com/49831117/Python-100-Days/blob/master/.py/us-states-game/main.py)