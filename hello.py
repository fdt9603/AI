from numba.core.types import none


def func(a, b):
    print(a + b)
    c=a+b
    return none
func(a=1, b=2)
print(func(a=1, b=2))


"""""""""""""""""""''"""
'''''''''''''''''''''''''''
'''''''''''''''''''

我要提交