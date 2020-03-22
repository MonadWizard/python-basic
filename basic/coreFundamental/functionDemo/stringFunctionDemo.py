"""

>>> str1
'hello I am Rakib'
>>>
>>>
>>> str1.capitalize()
'Hello i am rakib'
>>>
>>>
>>> str2 = "I know you know me..."
>>> str2
'I know you know me...'
>>> str2.capitalize()
'I know you know me...'
>>>
>>>
>>> str1 = '''Rakib Rakib yes papa
... eating suger no papa
... telling lie no papa
... open your mouth haha'''
>>> str1
'Rakib Rakib yes papa\neating suger no papa\ntelling lie no papa\nopen your mouth haha'
>>> str1.count('rakib')
0
>>> str1.count('Rakib')
2
>>>
>>> str1.count("no")
2
>>>
>>> str1.endswith(haha)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'haha' is not defined
>>> str1.endswith('haha')
True
>>>
>>> str1.endswith('haha')
True
>>>
>>> str1.endswith('a')
True
>>> str1.endswith('ha')
True
>>> str1.endswith('haa')
False
>>>

> str1 = "Rakib is a good boy"
>>> str1
'Rakib is a good boy'
>>> str1.find("o")
12
>>>
>>> str1.find("r")
-1
>>> str1.find("R")
0
>>> str1.find("x")
-1
>>>
>>>
>>> len(str1)
19
>>>
>>>
>>>
>>> len(str1)
19
>>>
>>> srt1.split()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'srt1' is not defined
>>> srt1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'srt1' is not defined
>>> str1
'Rakib is a good boy'
>>>
>>>
>>> str1.split()
['Rakib', 'is', 'a', 'good', 'boy']
>>> str1.split(i)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'i' is not defined
>>> str1.split('i')
['Rak', 'b ', 's a good boy']
>>> str1
'Rakib is a good boy'
>>> str1(" ")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> str1.split(" ")
['Rakib', 'is', 'a', 'good', 'boy']
>>>
>>> str1.title()
'Rakib Is A Good Boy'
>>>


>>> str1.lower()
'rakib is a good boy'
>>>
>>> str2
'I know you know me...'
>>>
>>> str2.is lower()
  File "<stdin>", line 1
    str2.is lower()
          ^
SyntaxError: invalid syntax
>>> str2.islower()
False
>>>
>>> str1.islower()
False
>>>
>>> str3 = "i am rakib"
>>> str3.islower()
True
>>>
>>> str3.upper()
'I AM RAKIB'
>>> str3
'i am rakib'
>>> sr = str3.upper()
>>> sr.isupper()
True
>>> sr
'I AM RAKIB'
>>>
>>>
>>> str1 = " i Am raKib "
>>>
>>> srt1.swapcase()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'srt1' is not defined
>>> str1.swapcase()
' I aM RAkIB '
>>>
>>> str1.swapcase()
' I aM RAkIB '
>>>

>>> s1 = "hello I am Rakib"
>>> s2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 's2' is not defined
>>> s1
'hello I am Rakib'
>>> s1.replace('Rakib','careless')
'hello I am careless'
>>>
>>> s1
'hello I am Rakib'
>>>
>>> s2 = s1.replace('rakib','careless')
>>> s2
'hello I am Rakib'
>>> s2 = s2.replace('Rakib','careleess')
>>> s2
'hello I am careleess'
>>>
>>> s2.replace('a','*')
'hello I *m c*releess'
>>>
>>> s2
'hello I am careleess'
>>>
>>> s2 = s2.replace('e','*')
>>> s2
'h*llo I am car*l**ss'
>>>
>>>
>>> s1.isdigit()
False
>>>
>>> s1 = '546453'
>>> s1
'546453'
>>> s1.isdigit()
True
>>>
>>> s1 = '54634f'
>>> s1.isdigit()
False
>>>
>>>
>>> s1.isalpha()
False
>>> s2.isalpha()
False
>>> s4 = 'erghse;rh'
>>> s4
'erghse;rh'
>>> s4.isalpha()
False
>>> s4.replace(';','dd')
'erghseddrh'
>>> s4 = s4.replace(';','rgaeg')
>>> s4.isalpha()
True
>>>

>>> str1 = '!!!!!!!!hello!!!!!!!!'
>>> str1.strip('!')
'hello'
>>>
>>>
>>>
>>> str= "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaarakibaaaaaaaaaaaaahasanaaaaaaaaaaaaaaaaaaaaa"
>>> str.strip('a')
'rakibaaaaaaaaaaaaahasan'
>>> str
'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaarakibaaaaaaaaaaaaahasanaaaaaaaaaaaaaaaaaaaaa'
>>> str.lstrip('a')
'rakibaaaaaaaaaaaaahasanaaaaaaaaaaaaaaaaaaaaa'
>>>
>>>
>>> str.rstrip('a')
'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaarakibaaaaaaaaaaaaahasan'
>>>
>>>
>>>

"""