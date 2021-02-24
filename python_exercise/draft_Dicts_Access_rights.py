Statement
The virus attacked the filesystem of the supercomputer and broke the control of access rights to the files. For each file there is a known set of operations which may be applied to it:

write W,
read R,
execute X.

The first line contains the number N — the number of files contained in the filesystem. The following N lines contain the file names and allowed operations with them, separated by spaces. The next line contains an integer M — the number of operations to the files. In the last M lines specify the operations that are requested for files. One file can be requested many times.

You need to recover the control over the access rights to the files. For each request your program should return OK if the requested operation is valid or Access denied if the operation is invalid.

Example input
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog

# 4
# tmp_796487715 X R W
# tmp_31144126 X R
# tmp_967334538 R
# tmp_264755563 R W
# 3
# read tmp_264755563
# execute tmp_796487715
# execute tmp_796487715


Example output
OK
Access denied
Access denied
OK
OK

# OK
# OK
# OK

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/dictionaries_dicts/


n = int(input())

r_list = []
w_list = []
x_list = []

for i in range(n):
  list = [str(k) for k in input().split()]
  if "R" in list:
    r_list += [list[0]]
  elif "W" in list:
    w_list += [list[0]]
  elif "X" in list:
    x_list += [list[0]]
   
print(x_list)



