import cgi
import os
path = "C:/Users/Greg/Downloads/01_Code/SE_Foundation/Color_Picker/cgi-bin/colors.txt"
form = cgi.FieldStorage()
#color= form.getvalue("color")
color= "red"


yescolor = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
  </head>  
  <body>
    <h1>Congrats! {color} is a color :)</h1>
    
    <p>
    Try it again if you want to!
    </p>
    
  </body>
</html>
'''.format(color=color)

nocolor =  '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
  </head>  
  <body>
    <h1>Mhhhh! {color} is not a color :)</h1>
    
    <p>
    Try it again if you want to!
    </p>
    
  </body>
</html>
'''.format(color=color)

f = open(path,"r")
fi= f.read()
if color in fi:
  print (yescolor)
else:
  print (nocolor)
