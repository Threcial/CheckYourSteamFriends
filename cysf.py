import cmd
import shlex
from datetime import datetime

class cysf(cmd.Cmd):

    prompt = "cysf>"

    def do_exit(self, arg):
        """exit"""
        print("bye")
        return True
    
    def do_time(self, arg):
        """now"""
        print(datetime.now())

    def emptyline(self):
        return super().emptyline()

if __name__ == "__main__":
    cysf().cmdloop()