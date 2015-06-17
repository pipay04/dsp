# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

touch   creates new file
pushd   takes a path and pushes it into a list for retrieval later
popd    removes path from list
-r      recursively execute command
rm -rf  remove directory and the contents
less    displays content of a file but only up until content that fits the screen. Press enter to continue displaying following         content
cat     displays entire content of a file
piping  | < > >>
find    find files indicated (syntax example: find . -name "*.txt" -print)
grep    find keywords within files
man     manual or documentation

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls - list files and directories in the current directory
ls -a - same as ls except it also lists files with .(dot) in the beginning of the filename
ls -l - displays file's filemode, owner name, group name, byte size, month and day last modified, time last modified and pathname
ls -lh - reduces filesize number of units to 2 decimal places

---


---

What does `xargs` do? Give an example of how to use it.

xargs is a command that gets input from stdin and echos it to the terminal upon typing ctrl-d. By default, it just displays (echoes back) whatever the user inputs in the terminal.
Ex. > xargs
    > Hi.
    > This is an example.
    (ctrl-d) and the following appears
    > Hi.This is an example.

---
