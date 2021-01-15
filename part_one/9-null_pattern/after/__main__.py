from myobjectfactory import MyObjectFactory

myobj = MyObjectFactory.create_object('myotherclass')
myobj.do_something('something')

myobj = MyObjectFactory.create_object('myclass')
myobj.do_something('something')


# Not doing something
# Doing something