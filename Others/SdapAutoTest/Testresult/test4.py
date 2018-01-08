 1 # coding=utf-8
 2 
 3 # 自定义异常
 4 class HappyException(Exception):
 5     pass
 6 
 7 # 引发和捕获异常
 8 try:
 9     raise HappyException
10 except:
11     print("HappyException")
12 
13 try:
14     raise HappyException()
15 except:
16     print("HappyException")
17 
18 # 捕获多种异常
19 try:
20     raise HappyException
21 except (HappyException, TypeError):
22     print("HappyException")
23 
24 # 重新引发异常
25 try:
26     try:
27         raise HappyException
28     except (HappyException, TypeError):
29         raise
30 except:
31     print("HappyException")
32 
33 #访问异常实例
34 try:
35     raise HappyException("都是我的错")
36 except (HappyException, TypeError), e:
37     print(e)
38 
39 #按类型捕获
40 try:
41     raise HappyException
42 except HappyException:
43     print("HappyException")
44 except TypeError:
45     print("TypeError")
46 
47 #全面捕获
48 try:
49     raise HappyException
50 except:
51     print("HappyException")
52 
53 #没有异常的else
54 try:
55     pass
56 except:
57     print("HappyException")
58 else:
59     print("没有异常")
60 
61 #总会执行的final
62 try:
63     pass
64 except:
65     print("HappyException")
66 else:
67     print("没有异常")
68 finally:
69     print("总会执行")