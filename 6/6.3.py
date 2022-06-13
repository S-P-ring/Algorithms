
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""
N=31
M=11
authors=[None]*M
titles=[None]*M

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global authors;
    global titles;
    authors=[None]*M
    titles=[None]*M
  



def hash(key):
    l=0
    for i in range(len(key)):
        l=l*N+ord(key[i])
    return l % M

def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    h=hash(author)
    while authors[h] != None:
        if(authors[h] == author) and (titles[h] == title):
            titles[h] = title
            return
        elif(authors[h] == author):
            titles[h]=titles[h] + ','+ title
            return
            
        h = (h + 1) % M
        
    authors[h] = author
    titles[h] = title
    return None


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці. :param author:
    Автор :param title: Назва книги :return: True, якщо книга міститься
    у бібліотеці та False у іншому разі. """
    h=hash(author)
    print(title in titles[h])
    


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    b=0
    h=hash(author)
    spisok=(f'{titles[h].split(",")}')
    op = spisok.strip('][').split(', ')
    listt = []
    for i in op:
        listt.append(i.replace("'", ""))
    for k in listt:
        if k == title:
            listt.remove(k)
        b+=1
    titles[h]=(",".join(listt))
    


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    h=hash(author)
    print(titles[h])
    

if __name__=='__main__':
    init()
    addBook('Валерьян Петрович Пидмогильный', 'Місто')
    addBook('Леся Українка', 'Лісова пісня')
    addBook('Леся Українка', 'Камінний господар')
    find('Леся Українка', 'Камінний господар')
    print(authors)
    print(titles)
    delete('Леся Українка', 'Лісова пісня')
    print(authors)
    print(titles)
    findByAuthor('Валерьян Петрович Пидмогильный')
    addBook('Іван Карпенко-Карий', 'Мартин Боруля')
    addBook('Іван Карпенко-Карий', 'Бурлака')
    print(authors)
    print(titles)    
    delete('Іван Карпенко-Карий', 'Мартин Боруля')
    print(authors)
    print(titles) 
