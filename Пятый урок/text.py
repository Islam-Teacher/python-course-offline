#Что такое массив в Python?

Массив — это фундаментальная структура данных и 
важная часть большинства языков программирования. 
В Python массивы — это контейнеры, способные хранить более 
одного элемента одновременно.

В частности, они представляют собой упорядоченный набор элементов,
каждое значение которого относится к одному и тому же типу данных. 
Это самое важное, что нужно помнить о массивах в Python. 
Они могут содержать последовательность нескольких элементов только одного типа.

В чем разница между списками и массивами в Python?
Списки — одна из наиболее распространенных 
структур данных в Python и основная часть языка.

Списки и массивы ведут себя сходным образом.

Как и массивы, списки представляют собой упорядоченную 
последовательность элементов.

Они также изменяемы и не имеют фиксированного размера, 
то есть могут увеличиваться и уменьшаться на протяжении 
всей жизни программы. Элементы можно добавлять и удалять, 
что делает списки очень гибкими в работе.

Однако списки и массивы — это не одно и то же.

В списках могут храниться элементы различных типов данных. 
Это означает, что список может одновременно содержать целые числа, 
числа с плавающей запятой, строки или любой другой тип данных Python.
С массивами это не сработает.

Как уже упоминалось, массивы хранят элементы только какого-то одного 
типа данных. Это важно помнить! Есть массивы целых чисел, 
массивы чисел с плавающей запятой и т.д.

[python_ad_block]
Когда следует использовать массивы в Python
Списки встроены по умолчанию в язык программирования Python, 
а массивы — нет. Поэтому, если вы хотите использовать массивы, 
их сперва нужно импортировать через модуль array.

Массивы модуля array представляют собой тонкую обертку массивов в C.
Они полезны, к
огда вам нужно работать с однородными данными.

Они также более компактны и занимают меньше памяти и места, 
что делает их более эффективными по сравнению со списками.

Если вы хотите выполнять математические вычисления, 
лучше воспользоваться массивами NumPy, импортировав модуль NumPy.

Стоит отметить, что использовать массивы в Python 
следует только тогда, когда вам это действительно нужно,
ведь списки работают аналогичным образом и более гибки в работе.

#Как использовать массивы в Python

Чтобы создавать массивы в Python, 
вам сначала нужно импортировать модуль array, 
который содержит все необходимые для работы функции.

Импортировать модуль массива можно тремя способами:

1. Использовать import array в верхней части файла. 
Это позволит нам подключить модуль array. 
После чего мы сможем создать массив, используя array.array().

import array
# Создание массива
array.array()
2. Чтобы не вводить постоянно array.array(), 
можно прописать import array as arr в верхней части файла 
вместо просто import array. 
После чего для создания массива нужно будет набрать arr.array(). 
Arr действует как псевдоним, 
после которого сразу следует конструктор для создания массива.

import array as arr
# Создание массива
arr.array()
3. Наконец, вы также можете использовать from array import *, 
где с помощью * импортируются все доступные функции данного модуля. 
В таком случае, чтобы создать массив, нужно написать просто array().

from array import *
# Создание массива
array()

#Как определить массив в Python

После того, как вы импортировали модуль array, 
вы можете перейти к непосредственному созданию массива Python.

Общий синтаксис создания массива выглядит следующим образом:

variable_name = array(typecode,[elements])
Давайте разберем синтаксис подробнее:

variable_name будет именем массива
typecode указывает, какие элементы будут храниться в массиве. 
Это может быть массив целых чисел, массив чисел 
с плавающей запятой 
или массив любого другого типа данных в Python. 
Но помните, что все элементы должны быть одного типа данных.
Внутри квадратных скобок вы указываете элементы, которые 
будут храниться в массиве, при этом каждый элемент 
отделяется запятой. 
Вы также можете создать пустой массив, 
просто написав variable_name = array(typecode) без каких-либо элементов.
Ниже приведена таблица кодов для различных типов данных.

TYPECODE	ТИП В C	ТИП В PYTHON	РАЗМЕР
‘b’	signed char	int	1
‘B’	unsigned char	int	1
‘u’	wchar_t	Unicode character	2
‘h’	signed short	int	2
‘H’	unsigned short	int	2
‘i’	signed int	int	2
‘I’	unsigned int	int	2
‘l’	signed long	int	4
‘L’	unsigned long	int	4
‘q’	signed long long	int	8
‘Q’	unsigned long long	int	8
‘f’	float	float	4
‘d’	double	float	8

#Создание массива на практике

Вот пример того, как можно определить массив в Python:

import array as arr 

numbers = arr.array('i',[10,20,30])

print(numbers)

#output
#array('i', [10, 20, 30])

Давайте разберем, что мы только что сделали.

Сначала мы подключили модуль array, 
в данном случае с помощью import array as arr.

Затем мы создали массив чисел.

Мы использовали arr.array(), так как arr это наш псевдоним для модуля.

Внутри конструктора array() мы сначала указали i для целых чисел. 
Это означает, что массив может включать как положительные, 
так и отрицательные значения. Если бы мы, например, указали H, 
это бы означало, что отрицательные значения не допускаются.

Наконец, мы перечислили значения, 
которые будут храниться в массиве, в квадратных скобках.

Имейте в виду, что если вы попытаетесь включить значения, 
тип которых не соответствует коду i, то есть не целочисленные значения, 
вы получите сообщение об ошибке:

import array as arr 
numbers = arr.array('i',[10.0,20,30])
print(numbers)
#output
#Traceback (most recent call last):
# File "/Users/dionysialemonaki/python_articles/demo.py", line 14, in <module>
#   numbers = arr.array('i',[10.0,20,30])
#TypeError: 'float' object cannot be interpreted as an integer

В этом примере мы попытались включить в массив число с плавающей запятой.
И получили ошибку, потому что это целочисленный массив.

Другой способ создания массива:

from array import *
# Массив чисел с плавающей запятой
numbers = array('d',[10.0,20.0,30.0])
print(numbers)
#output
#array('d', [10.0, 20.0, 30.0])
В этом примере модуль массива был импортирован через from array import *. 
Затем был создан массив чисел с типом данных float. 
Это означает, что он содержит только числа с плавающей запятой, 
которым соответствует код d.

Как найти длину массива в Python
Чтобы узнать точное количество элементов, содержащихся в массиве, 
можно использовать встроенный метод len().

Он вернет вам целое число, равное общему количеству элементов
в указанном вами массиве.

import array as arr 
numbers = arr.array('i',[10,20,30])
print(len(numbers))
#output
# 3
В этом примере массив содержал три элемента — 10, 20, 30. 
Поэтому длина массива равна 3.

Индексация массива и доступ к отдельным элементам
Каждый элемент массива имеет определенный адрес. 
Доступ к отдельным элементам осуществляется путем ссылки на их порядковый номер.

Индексация в Python, как и во всех языках программирования, 
и вычислениях в целом начинается с 0, а не с 1. Об этом важно помнить.

Чтобы получить доступ к элементу, вы сначала пишете имя массива, 
за которым следуют квадратные скобки. Внутри квадратных скобок 
вы указываете индекс нужного элемента.

Общий синтаксис будет выглядеть так:

array_name[index_value_of_item]
Вот так можно получить доступ к каждому отдельному элементу в массиве:

import array as arr 
numbers = arr.array('i',[10,20,30])
print(numbers[0]) # Получение 1-го элемента
print(numbers[1]) # Получение 2-го элемента
print(numbers[2]) # Получение 3-го элемента
#output
#10
#20
#30
Помните, что значение индекса последнего элемента 
массива всегда на единицу меньше, чем длина массива. 
Если n — длина массива, то значением индекса последнего элемента будет n-1.

Обратите внимание, что вы также можете получить доступ к
каждому отдельному элементу, используя отрицательную индексацию.

При отрицательной индексации последний элемент будет 
иметь индекс -1, предпоследний элемент — -2 и так далее.

К примеру, получить каждый элемент массива можно следующим образом:

import array as arr 
numbers = arr.array('i',[10,20,30])
print(numbers[-1]) # Получение последнего элемента
print(numbers[-2]) # Получение предпоследнего элемента
print(numbers[-3]) # Получение первого элемента
 
#output
#30
#20
#10
Как искать элемент в массиве в Python
Вы можете узнать порядковый номер элемента с помощью метода index().

В качестве аргумента метода вы передаете значение 
искомого элемента, и вам возвращается его индекс.

import array as arr 
numbers = arr.array('i',[10,20,30])
# Поиск индекса элемента со значением 10
print(numbers.index(10))
#output
#0
Если имеется более одного элемента с указанным значением, 
будет возвращен индекс элемента, который встречается первым. 
К примеру, это может выглядеть так:

import array as arr 
numbers = arr.array('i',[10,20,30,10,20,30])
# Поиск индекса элемента со значением 10
# Возвращается индекс первого из двух элементов со значением 10
print(numbers.index(10))
#output
#0
Как перебрать массив в Python с помощью цикла
Мы рассмотрели, как получить доступ к каждому отдельному 
элементу массива и распечатать элементы по отдельности.

Вы также видели, как распечатать массив с помощью метода print().
Этот метод дает следующий результат:

import array as arr 
numbers = arr.array('i',[10,20,30])
print(numbers)
#output
#array('i', [10, 20, 30])
Но что делать, если вы хотите вывести значения одно за другим?

Здесь на помощь приходит цикл. Вы можете идти по массиву и
распечатывать значения одно за другим с каждой новой итерацией цикла.
Подробнее о циклах в Python можно почитать в статье «Pythonic циклы».

К примеру, для решения нашей задачи вы можете 
использовать простой цикл for:

import array as arr 
numbers = arr.array('i',[10,20,30])
for number in numbers:
    print(number)
    
#output
#10
#20
#30
Вы также можете использовать функцию range() и передать метод len() 
в качестве ее параметра. Это даст тот же результат:

import array as arr  
values = arr.array('i',[10,20,30])
# Распечатка всех значений массива по отдельности
for value in range(len(values)):
    print(values[value])
#output
#10
#20
#30
Как использовать срезы с массивами в Python
Чтобы получить доступ к определенному диапазону значений 
внутри массива, используйте оператор среза (двоеточие :).

Если, используя срез, вы укажете только одно значение, 
отсчет по умолчанию начнется с 0. Код получает первый элемент 
(с индексом 0) и идет до элемента с указанным вами индексом, 
но не захватывает его.

import array as arr 
# Исходный массив
numbers = arr.array('i',[10,20,30])
# Получение только значений 10 и 20
print(numbers[:2])  # С первой по вторую позицию (индексы 0 и 1)
#output
#array('i', [10, 20])
Когда вы передаете два числа в качестве аргументов, 
вы указываете диапазон индексов. В этом случае отсчет начинается
с первого указанного вами индекса и идет до второго, не включая его:

import array as arr 
# Исходный массив
numbers = arr.array('i',[10,20,30])
# Получение только значений 20 и 30
print(numbers[1:3]) # Со второй по третью позицию
#output
#array('i', [20, 30])
Методы выполнения операций с массивами в Python
Массивы изменчивы, это означает, что мы можем менять их
элементы самым разным образом. Можно изменить значение элементов, 
добавить новые или удалить те, которые вам больше не нужны в вашей программе.

Давайте рассмотрим несколько методов, наиболее часто используемых 
для выполнения операций с массивами.

Изменение значения элемента в массиве
Вы можете изменить значение определенного элемента,
указав его позицию (индекс) и присвоив ему новое значение. 
Сделать это можно так:

import array as arr 
#original array
numbers = arr.array('i',[10,20,30])
# Изменение первого элемента
# Меняется значение с 10 на 40
numbers[0] = 40
print(numbers)
#output
#array('i', [40, 20, 30])
Добавление нового значения в массив
Чтобы добавить одно значение в конец массива, используйте метод append():

import array as arr 
# Исходный массив
numbers = arr.array('i',[10,20,30])
# В конец  numbers добавляется целое число 40 
numbers.append(40)
print(numbers)
#output
#array('i', [10, 20, 30, 40])
Имейте в виду, что новый элемент, который вы добавляете,
должен иметь тот же тип данных, что и остальные элементы в массиве.

Посмотрите, что произойдет, если мы пытаемся добавить число с 
плавающей запятой в массив целых чисел:

import array as arr 
# Исходный массив
numbers = arr.array('i',[10,20,30])
# В конец numbers добавляется число с плавающей запятой 40.0
numbers.append(40.0)
print(numbers)
#output
#Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_articles/demo.py", line 19, in <module>
#   numbers.append(40.0)
#TypeError: 'float' object cannot be interpreted as an integer
Но что, если вы хотите добавить более одного значения в конец массива?

Тогда используйте метод extend(), который принимает итерируемый 
объект (например, список элементов) в качестве аргумента. 
Опять же, убедитесь, что все новые элементы имеют один и тот же тип данных.

import array as arr 
# Исходный массив
numbers = arr.array('i',[10,20,30])
# Добавление целых чисел 40,50,60 в конец numbers
# Числа берутся в квадратные скобки
numbers.extend([40,50,60])
print(numbers)
#output
#array('i', [10, 20, 30, 40, 50, 60])
А что, если вы  хотите добавить элемент не в конец массива?
В таком случае используйте метод insert(): 
он позволяет добавить элемент на определенную позицию.

Функция insert() принимает два аргумента: индекс позиции, 
на которую будет вставлен новый элемент, и значение нового элемента.

import array as arr 
# Исходный массив
numbers = arr.array('i',[10,20,30])
# Добавление целого числа 40 на первую позицию
# Помните, что индексация начинается с  0
numbers.insert(0,40)
print(numbers)
#output
#array('i', [40, 10, 20, 30])
Удаление значения из массива
Чтобы удалить элемент из массива, используйте метод remove() 
и укажите значение элемента в качестве аргумента.

import array as arr 
# Исходный массив
numbers = arr.array('i',[10,20,30])
numbers.remove(10)
print(numbers)
#output
#array('i', [20, 30])
С помощью remove() будет удален только первый экземпляр значения, 
которое вы передаете в качестве аргумента.

Посмотрите, что происходит, когда имеется несколько 
элементов с одинаковым значением:

import array as arr 
# Исходный массив
numbers = arr.array('i',[10,20,30,10,20])
numbers.remove(10)
print(numbers)
#output
#array('i', [20, 30, 10, 20])
Удаляется только первое вхождение числа 10.

Вы также можете использовать метод pop() и указать позицию удаляемого элемента:

import array as arr 
# Исходный массив
numbers = arr.array('i',[10,20,30,10,20])
# Удаление первого вхождения 10
numbers.pop(0)
print(numbers)
#output
#array('i', [20, 30, 10, 20])
Заключение
Вот и все — теперь вы знаете, что такое массив в Python,
как его создать с помощью модуля array и какие есть методы для работы с ним. 
