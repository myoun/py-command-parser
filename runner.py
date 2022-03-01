from command import Command, CommandManager, GlobalCommandManager, singleton

class Sum(Command):

    def __init__(self):
        super().__init__("sum", "add")
        
        # arguments

        self.addArg("a", int)
        self.addArg("b", int)
    
    def execute(self, args: dict):
        print(args["a"] + args["b"])

class Hi(Command):

    def __init__(self):
        super().__init__("hi", "hello")

        self.addArg("name", str)

    def execute(self, args: dict):
        name = args["name"]
        print(f"Hi, {name}")

@singleton
class MyCommandManager(CommandManager):
    pass


GlobalCommandManager().registerCommand(Sum())
MyCommandManager().registerCommand(Hi())


GlobalCommandManager().executeCommand("/add 5 8") # 13
MyCommandManager().executeCommand("/hi world!") # Hi, world!

