from myobjectfactory import MyObjectFactory

myobj = MyObjectFactory.create_object('myotherclass')
if myobj is not None:
    myobj.do_something('something')
else:
    print('Not doing anything.')

myobj = MyObjectFactory.create_object('myclass')
if myobj is not None:
    myobj.do_something('something')
else:
    print('Not doing anything.')


# Not doing anything.
# Doing something