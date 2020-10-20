# Singleton Pattern

It is a **CREATIONAL** pattern.

1. Ensure that a class has only **one** instance.
2. Useful to control access to a limited resource.
- Device access.
- Buffer pools.
- Web/DB connections.
3. Global point of access for the instance.

### What's wrong?

1. Singletons violate the **SRP**
2. Non-standard class access.
3. Harder to test.
4. Carry a global state. 
5. Hard to sub-class.

That's why sometimes Singleton is called an *anti*pattern.

## Structure

![structure](structure.png)

## Exercise

A logging sub-system for an app.
1. Events should be logged to a file (i.e. events, erros, warnings, messages)
2. Control access to the file.


### Solution:

1. See the standard implementation of Singleton in `/classic`.
2. In `/base` there's a fix for the **SRP** violation mentioned in the "What's wrong?" section:
- Base class for all singletons.
- Inherit form the base class for each one. 
There's a fix for the non-standard class access issue. 
*Other problems still remain*
3. In `/meta` there's another implementation that allows multiple inheritance through a metaclass. 
4. In `/mono` there's an impementation in which there's a global state (singleton has to do this anyways but done in a different way)

