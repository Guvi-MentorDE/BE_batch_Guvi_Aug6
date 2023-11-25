def myFun(arg1, **kwargs):
    print(arg1)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
        
        
myFun("Hi", first='we', mid='are', last='learning  Ariflow')


def myFun2(*argv):
    for arg in argv:
        print(arg)
        
myFun2('Hi', 'we', 'are', 'learning Airflow', 'we', 'are', 'learning Airflow')