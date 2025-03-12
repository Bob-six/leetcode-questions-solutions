
"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"



Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

"""


class Solution:
  def convert(self, s: str, numRows: int) -> str:
    result = []

    if numRows < 2:
        return s

    counter = 0

    while counter < len(s):
        res = []

        for i in range(numRows):
           if counter == len(s):
              break
           res.append(s[counter])
           counter += 1

        result.append(res)
        
        for i in range(numRows - 2, 0, -1):
            if counter == len(s):
                break
            empty_array = [None for i in range(numRows)]
            empty_array[i] = s[counter]
            counter += 1
            result.append(empty_array)

    result_mapped = []

    for i in range(numRows):
        for arr in result:
            if i >= len(arr) or arr[i] == None:
                continue

            result_mapped.append(arr[i])
    
    return "".join(result_mapped)



print(Solution().convert("PAYPALISHIRING", 3))

print(Solution().convert("ABC", 2))




#  Optimized Solution




class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if len(s) <= numRows or numRows == 1:
        return s

    result = ["" for _ in range(numRows)]


    row, step = 0, 1


    for char in s:
        result[row] += char

        if row == 0:
            step = 1

        elif row == numRows - 1:
            step = -1

        row += step

    return "".join(result)        

