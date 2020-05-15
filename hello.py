#hello.py
print('hello git!')
import myname

print('Agrego un print al principio más otra linea')
name = myname.get_name()
print(f'hello {name}')

print('THIS IS PART OF THE BRANCH THAT GOES PUBLIC')

print('do $push remote branchNameLocale:branchNameRemote')

print('do $push -u remoteRepo branchNameLocal:branchNameRemote to associate both branches')

print('do "git config --global push.default" to see default option for git push')