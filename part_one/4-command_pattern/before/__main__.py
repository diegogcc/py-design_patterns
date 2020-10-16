import sys
from command_executor import CommandExecutor

if len(sys.argv) < 2:
    print('Usage: $ python3 -m before <command>')
    print('Commands:')
    print('\tCreateOrder')
    print('\tUpdateQuantity number')
    print('\t ShipOrder')
    exit()

executor = CommandExecutor()
executor.execute_command(sys.argv[1:])