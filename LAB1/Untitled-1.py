# Это образец скрипта Python.
import  sys
импортная  математика
# Нажмите Shift + F10, чтобы выполнить его или заменить своим кодом.
# Нажмите Double Shift, чтобы искать повсюду классы, файлы, окна инструментов, действия и настройки.
def  is_number ( s ):
    попробуйте :
        Поплавок ( ы )
        вернуть  True
    кроме  ValueError :
        вернуть  ложь

def  is_nulli ( s ):
    попробуйте :
        если ( float ( s ) ==  0 ):
            вернуть  True
    кроме  ValueError :
        вернуть  ложь
а = 1
а1 = 2
b = 2
с = 1
while ( is_number ( a )):
    print ( 'Введите а:' )
    a1 =  вход ()

    если ( not ( is_number ( a1 ))):
        print ( 'Это не число!' )
        Продолжить
    Элиф ( is_nulli ( а1 )):
        print ( 'а не может быть нулем!' )
        Продолжить
    еще :
        a  = с  плавающей точкой ( a1 )
        перерыв

while ( is_number ( b )):
    print ( 'Введите b:' )
    b1 =  вход ()

    если ( not ( is_number ( b1 ))):
        print ( 'Это не число!' )
        Продолжить
    еще :
        b  = с  плавающей запятой ( b1 )
        перерыв

while ( is_number ( c )):
    print ( 'Введите c:' )
    c1 =  вход ()

    если ( not ( is_number ( c1 ))):
        print ( 'Это не число!' )
        Продолжить
    еще :
        c  = float ( c1 )
        перерыв

print ( «Данные введены, идет подсчет:» )
если ( a  ==  0 ):
    print ( 'a = 0! измените набор!' )
еще :
    D  =  b * b  -  4 * a * c
    если  D  <  0 :
        print ( 'Действительных решений нет' )

    еще :
        y1  = (( - Ь  - по  математике . SQRT ( D )) / ( 2  *  ))
        у2  = (( - Ь  +  математике . SQRT ( D )) / ( 2  *  ))
        print ( f'Два корня из дискримината y1 и y2: { y1 } и { y2 } ' )
        если ( y1  <  0 ) и ( y2  <  0 ):
            print ( 'Действительных решений нет' )

        еще :
            если ( y1  > =  0 ) и ( y2  > =  0 ):
                x1  =  - ( математика . SQRT ( у1 ))
                х2  =  - х1
                x3  =  - ( математика . SQRT ( у2 ))
                х4  =  - х3
                print ( f'Четыре корня: { x1 } и { x2 } и { x3 } и { x4 } ' )
            еще :
                если ( y1  > =  0 ) и ( y2  <  0 ):
                    x1  =  - ( математика . SQRT ( у1 ))
                    х2  =  -  х1
                    print ( f'Два корня: { x1 } и { x2 } ' )

                еще :
                    x1  =  - ( математика . SQRT ( у2 ))
                    х2 =  -  х1
                    print ( f'Два корня: { x1 } и { x2 } ' )