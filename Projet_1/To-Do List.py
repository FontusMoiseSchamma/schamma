import pickle
Todo_list = []

def add_task():
    wi="w"
    non="n"
    a= True
    while a :
        chwa = input("Mete deskripsyon yon tach :")
        Todo_list.append(chwa)
        repons = input("Tape (w) si wap mete yon lot tach, tape (n) si ou psp mete on lot tach :")
        if(repons == non):
            break    
        if(repons == wi):
            continue
        if(repons != non and repons != wi):
            while a:
                repons = input("Tape (w) pou wi oubyen (n) pou non :")
                if(repons == wi or repons == non):
                    break
        if(repons == non):
            break        

def display_tasks(l):
    b=0
    print("Men lis tach ou yo :")
    for c in Todo_list:
        b+=1
        print(b,'-',c)


def mark_task_done():
    try:
        fini = int(input('Tape nimero tach ki fini an :'))
        n=fini-1
        Todo_list.pop(n)
    except IndexError:
        print('Mete on nimero tach ki nan lis la :')    
    print('Ou fini ak tach nimero {} an, li soti nan lis la.'.format(fini))        


def save_tasks(l):
    try:
        fich = open('task.txt','wb')
        t = Todo_list
        pickle.dump(t,fich)
    except Exception as e:
        print('Anregistreman gen ere !',str(e))
        fich.close()


def meni():
    vre = True
    while vre :
        print('To-Do List \n')
        print('MENI')
        print('1.Mete yon tach.')
        print('2.Afiche tout tach yo.')
        print('3.Fini yon tach.')
        print('4.Anregistre epi femen.\n')
        chwa = int(input("Fe chwa paw la ak youn nan nimero yo :"))

        if chwa == 1:
            add_task()
        if chwa == 2:
            display_tasks(Todo_list)
        if chwa == 3:
            mark_task_done()
        if chwa == 4:
            save_tasks(Todo_list)
            print('Eleman ou yo anregistre nan fichye a.!')
            print('Pwogram nan femen.')
            break
meni()
