#!/usr/bin/python3

import cmd

class myCommand(cmd.Cmd):
    prompt = ">> "
    

myCommand().cmdloop()
