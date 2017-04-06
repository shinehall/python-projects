# coding=utf-8

#操作列表，验证切片后是否得到一个新数组或是原数组的引用
spam = ['cat', 'dog', 'elephant', 'tiger', 'fox']
subSpam = spam[0 : 3]
print("origin spam is : " + str(spam))
print("get subSpam from spam : " + str(subSpam))
subSpam[0] = 'dog'
print("after change, origin spam is " + str(spam))  #打印结果：cat dog elephant tiger fox
print("after change, subSpam is " + str(subSpam))   #打印结果：dog dog elephant  说明分割后得到的是一个新列表而非原列表的引用
