 Variables - Part I
 
Just about every programming language in existence has the concept of variables - a symbolic name for a chunk of memory to

which we can assign values, read and manipulate its contents. The Bourne shell is no exception, and this section introduces 

that idea. This is taken further in Variables - Part II which looks into variables which are set for us by the environment.

Let's look back at our first Hello World example. This could be done using variables (though it's such a simple example that it 

doesn't really warrant it!)

Note that there must be no spaces around the "=" sign: VAR=value works; VAR = value doesn't work. In the first case, the shell 

sees the "=" symbol and treats the command as a variable assignment. In the second case, the shell assumes that VAR must be the 

name of a command and tries to execute it.

If you think about it, this makes sense - how else could you tell it to run the command VAR with its first argument being "=" 

and its second argument being "value"?


Enter the following code into var.sh:
