# SOLID Principles

## Single Responsibility Principle

A class should only have **one** responsibility or only one reason to change. 

*i.e Either cooking or washing but not both*

## Open-closed Principle

A class should be **open** for extension (*inheritance*),
but **closed** for modification.

*(We can add more methods and properties but not modify the structure)*

## Liskov Substitution Principle

Subclasses must be substitutable for their base/parent classes.

## Interface Segregation Principle 

Many specific interfaces are better than one **do-it-all** interface.

## Dependency Inversion Principle

We should depend on abstractions and not on concrete classes. 
* High-level modules should not depend on low-level modules. Both should depend on abstractions
* Abstractions should not depend on details. Details should depend on abstractions.