
srcCode = 'x = 20\ny = 30\nmul = x * y\nprint("mul =", mul)'
execCode = compile(srcCode, 'mulstring', 'exec')
exec(execCode)
