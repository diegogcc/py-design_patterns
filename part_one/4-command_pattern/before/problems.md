# PROBLEMS DISCOVERED

1. All of the if/elif clauses on the `execute_command()` method.
2. The class has too many responsibilities is a violation to the **SRP** principle. 
- Parse commands.
- Handle invalid commands.
- Execute valid commands.
3. Adding/changing commands would imply changing the `CommandExecutor` class; this violates the **OCP** principle. 
4. Violates the **DIP** principle. We depend on the implementation of the `execute_command()` on the `CommandExecutor`.  