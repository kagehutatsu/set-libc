It's might be useful for someone who has been almost driven mad by different glibc in pwn.

I can deeply understand that it's really complex to set your programme's glibc same with then problem makers.
This tool is baseed on patchelf (an excellent tools for glibc change).
You have to download and install it first.

#JUST INPUT "sudo libc" INTO YOUR TERMINAL.

First, you need to rename the programme into "main".(Maybe automate it in next version)

If you just want to set the libc same with the problem itself, just choose "globle-mode".

If you need to set the libc completely same with the question, just choose "local-mode".
(remember to rename your libc file, for example: libc-2.23.so)
But if you done that, when you debug it with gdb, you will be unable to see the struct of something (such as heap).

After that you can choose you libc version, there are four choice for you.(Maybe just enough for pwn learners)

#REMEMBER:
  1. Rename your programme into "main".
  2. Store the libc file (name:extra-libc) folder in /
  3. ADD "alias libc: "sudo python 'working_path'/set-libc.py" " into /etc/bash.bashrc.(FOR AUTOMATIC THE libc COMMAND) 
  
If you can understand my programme, change it as you like.
Using it to help you learn about pwn matters most.

libc file is come from glibc-all-in-one and libc-base,thanks for them.

It's just an attempt now.(Maybe full of bugs)
The code is ugly and its function is still waiting for the complete.
