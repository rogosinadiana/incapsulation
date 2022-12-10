class monster:
    def __init__(self):
        self.__health=100
        self.__X = 0
        self.__Y = 0
        self.__name ='МонстрДи'
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self,val):
        if val<0 or val>100:
            print('ОШИБКА!!!')
        else:
            self.__health=val
    def movement(self,direction):
        if direction=='up':
            self.__Y+=1
        elif direction=='left':
            self.__X-=1
        elif direction=='down':
            self.__Y-=1
        elif direction=='right':
            self.__X+=1
        else:
            print('НЕКОРРЕКТНОЕ НАПРАВЛЕНИЕ')
        print('Персонаж',self.__name,'перемистился в кординату:','(',self.__X,self.__Y,')','текущее здоровье:',self.__health)
def main():
    monster_di=monster()
    while True:
        direction=input('Задайте направление up,left,down,right или no, чтобы завершить операцию:')
        if direction=='no':
            break
        monster_di.movement(direction)
main()




