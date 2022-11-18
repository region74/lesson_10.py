def my_function(**kwargs):
    print(type(kwargs))
    print(kwargs)
    pass


my_function(name='Leo', age=20, is_man=True)
my_function(age=20, name='Leo')
my_function(name='Leo')

def megafunction(first,second=2,*args,**kwargs):
    print(first)
    print(second)
    print(args)
    print(kwargs)

megafunction(1,20,4,5,name='tom')