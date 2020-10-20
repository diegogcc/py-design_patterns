from director import Director
from mycomputer_builder import MyComputerBuilder
from budget_box_builder import BudgetBoxBuilder

computer_builder = Director(MyComputerBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

# Custom Computer:
#               Case: CoolerMaster N300
#          Mainboard: MSI 970
#                CPU: Intel Core i7-4770
#             Memory: Corsair Vengeance 16B
#         Hard Drive: Seagate 2TB
#         Video Card: GeForce GTX 1070


computer_builder = Director(BudgetBoxBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

# Custom Computer:
#               Case: IN WIN BP655
#          Mainboard: ASRock AM1H-IX
#                CPU: AMD Athlon 5150
#             Memory: Kingstono ValueRAM 4GB
#         Hard Drive: WD Blue 1TB
#         Video Card: On Board
