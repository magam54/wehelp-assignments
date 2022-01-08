def calculate(min, max):
    result = 0
    for sum in range (min, max+1):
        result += sum
    print(result)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

def avg(data):
    li = (data["employees"]) #取出employees的列表
    sum = 0
    for x in (data["employees"]):   #取出每個employees中的數值
        M = x["salary"]   #取出每位的薪水
        sum = sum+M   #累加薪水
    print(sum/len(li)) #累加後薪水除以employees列表的長度

avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
}) # 呼叫 avg 函式


def maxProduct(nums):
    li=list() #宣告一個空的列表，最後用來找最大值
    for x in nums: #取出列表中每個數字作為變數1
        for y in nums: #取出列表中每個數字作為變數2
            if x != y: #因不能乘以本身，下條件為變數1不等於變數2
                sum = x*y #變數1+變數2
                li.append(sum)  #最後一一加入列表中
            else: None
    print(max(li))

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

def twoSum(nums, target):
    for x in nums: #取出列表中每個數字作為變數1
        for y in nums: #取出列表中每個數字作為變數2
            if nums.index(x) != nums.index(y) and x+y == target: #位置不能相同，所以條件為變數1&變數2位置不相等，另外兩變數相加要等於Target
                ans = (nums.index(x),nums.index(y))
                return list(ans)

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9




def maxZeros(nums):
    li = list() #先建立一個空列表，為了取最大值
    count = 0  #定義變數為0，為出現0的次數
    for x in nums:  #取出列表數字
        if x == 0 :  #如果取出0
            count += 1  #次數加1
            li.append(count)  #加入列表中
        if x == 1 :  #如果取出1
            count = 0  #次數歸零
            li.append(count)  #加入列表中
    print(max(li))

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3