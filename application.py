Application='''


              To
              The <Whom>
              <name of intitute> <name of department>

              subject" <for what>

              respected Sir/Ma'am

                                 <description>

                    date                           your Student
                    <date>                            <name>      
'''

a=input('whom are you writing to: ')
b=input('Enter your name of intitute: ')
c=input('Enter name of department: ')
d= input('for what are you writing: ')
e= input('Please provide your description: ')
f= input('Enter todays date')
g= input('Enter Your Name')


Application=Application.replace('<Whom>',a)
Application=Application.replace('<name of intitute>',b)
Application=Application.replace('<name of department>',c)
Application=Application.replace('<for what>',d)
Application=Application.replace('<description>',e)
Application=Application.replace('<date>',f)
Application=Application.replace('<name>',g)

print(Application)
