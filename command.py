from typing import Tuple

class Command:
    
    def __init__(self, name: str, *aliases) -> None:
        self.args = []
        self.name = name
        self.aliases = aliases
    
    def addArg(self, arg: str, argtype):
        self.args.append({arg:argtype})
    
    def execute(self, args: dict):
        if __name__ == "command":
            raise Exception("Not Yet Implemented")
        pass
    

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance



class CommandManager:

    def __init__(self):
        self.commands = {}
        self.aliases = {}

    def registerCommand(self, command: Command):
        self.commands[command.name] = command
        for alias in command.aliases:
            self.aliases[alias] = command.name
    
    def parse(self, command: str) -> Tuple[Command, dict]:
        if command.startswith("/") == False:
            raise Exception(f"`{command}` is not a command!")
        
        splited = command.split()
        name = splited[0][1:]
        
        command = None
        try:
            command : Command = self.commands[name]
        except:
            command : Command = self.commands[self.aliases[name]]


        if (command == None):
            raise Exception(f"Commmand `{name}` Not found!")
        
        args = splited[1:]

        if (len(args) != len(command.args)):
            print(args, command.ar)
            raise Exception("args size not same")

        result = {}
        
        for i in range(len(args)):
            reqarg : dict = command.args[i]
            arg : str = args[i]
            
            reqtype : type = list(reqarg.values())[0]

            parsed = reqtype(arg)
            result[list(reqarg.keys())[0]] = parsed
        
        return (command, result)
    
    def executeCommand(self, command: str):
        cmd, parsed = self.parse(command)
        cmd.execute(parsed)

@singleton
class GlobalCommandManager(CommandManager):

    pass