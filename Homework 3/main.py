import pathlib
import re
import os
from datetime import datetime, timedelta, date
from classbook import *
from clean import *
from notes_book import NotesBook

def error_handler(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except:
            result = input_error()
            return result
    return inner

@error_handler
def main():
    global path, book, notes_book, esc_e
    esc_e = True
    while True:
        out.out_print('a')
        out.out_print('b')
        out.out_print('c')
        command = str(input())
        if command == "load" or command == "дщфв" or command == "1":
            out.out_print('d')    
            path = str(input())
            try:
                book=sal.load(path)[0]
                notes_book=sal.load(path)[1]
                break
            except:
                out.out_print('e') 

        elif command == 'new' or command == "туц" or command == "2":
            out.out_print('f')
            path = str(input())
            book = AddressBook()
            notes_book = NotesBook()
            break

        elif command == 'exit' or command == 'esc' or command == 'close' or command =='учше' or command == "3":
            esc_e = False
            break
        else:
            out.out_print('g') 

    while esc_e:
        # print(50*'*'+'WORKING WITH ADDRESSBOOK:'+50*'*')
        # print(125*'_')
        # print('|      COMMANDS      |')
        # print(22*'_')
        # print('|      "add"  \n|      "birthday"   \n|      "change"   \n|      "find"\n|      "delete"\n|      "show"\n|      "save"\n|      "exit"')
        # print(51*'*'+'WORKING WITH NOTESBOOK:'+51*'*')
        # print('|      COMMANDS      |')
        # print(22*'_')
        # print('|      "add note"\n|      "delete note"\n|      "edit note" \n|      "find note"\n|      "sort notes"\n|      "show notes"')
        # print(51*'*'+'WORKING WITH CLEANFOLDER:'+51*'*')
        # print('|      COMMANDS      |')
        # print(22*'_')
        # print('|      "clean" \n') 
        out.out_print('a')
        user_inpu = input('   What do you want to do?\n   Type exact command you want to do, \n   "help" for list of commands.\n   "exit" to exit\n')
        
        user_inpu=user_inpu.lower()
        result = handler(user_inpu)
        if result:
            print(result)
        elif result == None:
            pass
        else:
            break

@error_handler
def add():
    out.out_print('a')
    global esc_e, book
    name = Name(str(input('Input Name: ')))

    if name == 'exit' or name == 'esc' or name == 'close' or name =='учше':
            esc_e = False
            return "Not saved"
    if len(book)>0 and len(book)<=25:
        id_n=book[-1]["Id"]+1
    else:
        id_n=1    
    record1 = Record(name,id_n)

    while True:
        out.out_print('i')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            out.out_print('j')
            phone = str(input())
            if re.fullmatch('[+]?[0-9]{3,12}', phone):
                record1.add_phone(phone)
            else:
                out.out_print('k')

        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision =='учше':
            esc_e = False
            return 'Closed'
        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет'or decision == 'тщ' or decision == 'тще' or decision == 'т':
            break
        else:
            out.out_print('g')

    while True:
        out.out_print('l')
        birthday_d=None
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            out.out_print('m')
            birthday = str(input())
            try:                
                birthday_d=datetime.strptime(birthday, "%d.%m.%Y").date()
                record1.user['Birthday'] = birthday
                break
            except:
                out.out_print('n')

        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision =='учше':
            book.add_record(record1.user)
            esc_e = False
            return 'Closed'

        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет'or decision == 'тщ' or decision == 'тще' or decision == 'т':
            break
        
        else:
            out.out_print('g')

    while True:
        out.out_print('o')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            out.out_print('p')
            address = str(input())
            if len(address)>1 and len(address)<=30:
                record1.user['Address'] = address
                break
            else:
                print(f'Your Address is {len(address)} symbols. Please no more than 30 symbols')  
        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision =='учше':
            book.add_record(record1.user)
            esc_e = False
            return 'Closed'

        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет'or decision == 'тщ' or decision == 'тще' or decision == 'т':
            break
        else:
            out.out_print('g')

#START HERE
    while True:
        out.out_print('q')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            out.out_print('r')
            email = str(input())
            if re.match('([a-zA-Z][a-zA-Z0-9\._!#$%^*=\-]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,})', email):
                if len(email)>1 and len(email)<=30:
                    record1.user['E-mail'] = email
                    break 
                else:
                    print(f'Your E-mail is {len(email)} symbols. Please no more than 30 symbols') 
            else:
                out.out_print('s')
             
        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision =='учше':
            book.add_record(record1.user)
            esc_e = False
            return 'Closed'

        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет'or decision == 'тщ' or decision == 'тще' or decision == 'т':
            break
        
        else:
            out.out_print('g')

    while True:
        out.out_print('t')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            out.out_print('u')
            tags = str(input())
            if len(tags)>1 and len(tags)<=15:
                record1.user['Tags'] = tags
                book.add_record(record1.user)
                save()
                return out.out_print('h')  
            else:
                print(f'Your Tags is {len(tags)} symbols. Please no more than 15 symbols')

        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision =='учше':
            book.add_record(record1.user)
            esc_e = False
            return 'Closed'

        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет'or decision == 'тщ' or decision == 'тще' or decision == 'т':
            book.add_record(record1.user)
            save()
            return out.out_print('h')
        else:
            out.out_print('g')

@error_handler
def change():
    out.out_print('a')
    global book, esc_e
    out.out_print('v')
    old_name = str(input())
    old_name = old_name.lower()
    result = book.find_value(old_name)

    if len(result)>0 and len(result)!=None:
        out.show_find(result)
   
        out.out_print('a')
        out.out_print('w')
        decision = str(input())
        decision = decision.lower()
        
        if decision == 'name' or decision == 'тфьу' or decision == '1':
            new_name = str(input('Input Name: '))
            
            if len(result)>1:
                print(f"I've found {len(result)} notes with this Name")
                out.show_find(result)
                out.out_print('x')
                
                del_input=int(input())
                for i in result:
                    if i["Id"]==del_input:
                        i['Name'] = new_name
                        save()
                        return out.out_print('h')
            
            elif len(result)==1:
                for i in result:
                    i['Name'] = new_name
                    save()
                    return out.out_print('h')

            else:
                print(f'{old_name} not in Adress Book')

        elif decision == 'phone' or decision == 'зрщту' or decision == '2':
            out.out_print('y')

            if len(result)>1:
                print(f"I've found {len(result)} notes with this Name")
                out.show_find(result)
                out.out_print('y')
                del_input=int(input())
                for i in result:
                    if i["Id"]==del_input:
                        old_name = str(input())
                        out.out_print('j')

                        new_name = str(input())
                        for i in result:
                            if len(i['Phones'])>1:
                                for j in i['Phones']:
                                    if j == old_name:
                                        i['Phones'].remove(j)
                                        i['Phones'].append(new_name)
                                        save()
                                        return out.out_print('h')
                                    else:
                                        print(f'{old_name} not in Adress Book')   

                            elif len(i['Phones'])==1:
                                i['Phones'].remove(old_name)
                                i['Phones'].append(new_name)
                                return out.out_print('h')
                            elif len(i['Phones'])==0:
                                i['Phones'].append(new_name)
                                save()
                                return out.out_print('h')  

            elif len(result)==1:
                old_name = str(input())
                out.out_print('j')
                new_name = str(input())
                for i in result:
                    if len(i['Phones'])>1:
                        for j in i['Phones']:
                            if j == old_name:
                                i['Phones'].remove(j)
                                i['Phones'].append(new_name)
                                save()
                                return out.out_print('h')
                        else:
                            print(f'{old_name} not in Adress Book')   

                    elif len(i['Phones'])==1:
                        i['Phones'].remove(old_name)
                        i['Phones'].append(new_name)
                        return out.out_print('h')
                    elif len(i['Phones'])==0:
                        i['Phones'].append(new_name)
                        save()
                        return out.out_print('h')  
            else:
                print(f'{old_name} not in Adress Book')  

        elif decision == 'birthday' or decision == 'ишкервфн' or decision == '3':
            
            if len(result)>1:
                print(f"I've found {len(result)} notes with this Name")
                out.show_find(result)
                out.out_print('x')
                del_input=int(input())
                for i in result:
                    if i["Id"]==del_input:
                        out.out_print('z')
                        old_name = str(input())
                        out.out_print('m')
                        new_name = str(input())
                        try:
                            new_name=datetime.strptime(new_name, "%d.%m.%Y").date()
                        except:
                            out.out_print('n')
                        for i in result:
                            if i['Birthday'] == old_name:
                                i['Birthday'] = new_name
                                save()
                                return out.out_print('h')
                            elif i['Birthday'] ==None:
                                i['Birthday'] = new_name
                                save()
                                return out.out_print('h')
                            else:
                                print(f'{old_name} not in Adress Book')
            elif len(result)==1:
                old_name = str(input())
                out.out_print('m')
                new_name = str(input())
                try:
                    new_name=datetime.strptime(new_name, "%d.%m.%Y").date()
                except:
                    out.out_print('n')
                for i in result:
                    if i['Birthday'] == old_name:
                        i['Birthday'] = new_name
                        save()
                        return out.out_print('h')
                    elif i['Birthday'] ==None:
                        i['Birthday'] = new_name
                        save()
                        return out.out_print('h')
                    else:
                        print(f'{old_name} not in Adress Book')

        elif decision == 'address' or decision == 'adress' or decision == 'adres' or decision == 'фввкуіі' or decision == 'фвкуі' or decision == '4':
            out.out_print('aa')
            old_name = str(input())
            out.out_print('p')
            new_name = str(input())
            for i in result:
                if i['Address'] == old_name:
                    i['Address'] = new_name
                    save()
                    return out.out_print('h')
                elif i['Address'] == None:
                    i['Address'] = new_name
                    save()
                    return out.out_print('h')
                else:
                    print(f'{old_name} not in Adress Book')

        elif decision == 'email' or decision == 'e-mail' or decision == 'уьфшд' or decision == '5':
            out.out_print('ab')
            
            old_name = str(input())
            out.out_print('r')
            new_name = str(input())
            for i in result:
                if i['E-mail'] == old_name:
                    i['E-mail'] = new_name
                    save()
                    return out.out_print('h')
                elif i['E-mail'] == None:
                    i['E-mail'] = new_name
                    save()
                    return out.out_print('h')    
                else:
                    print(f'{old_name} not in Adress Book')

        elif decision == 'tags'or decision == 'tag'or decision == 'ефп' or decision == '6':
            out.out_print('ac')
            old_name = str(input())
            out.out_print('u')
            
            new_name = str(input())
            for i in result:
                if i['Tags'] == old_name:
                    i['Tags'] = new_name
                    save()
                    return out.out_print('h')
                elif i['Tags'] == None:
                    i['Tags'] = new_name
                    save()
                    return out.out_print('h')       
                else:
                    print(f'{old_name} not in Adress Book')

        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision =='учше' or decision == '7':
            esc_e = False
            return esc_e

    else:
        print(f'{old_name} not in Adress Book')
def clear():
    os.system('cls' if os.name=='nt'else 'clear')

#START CHaNGE
@error_handler
def clean_folder():

    out.out_print('a')
    out.out_print('ad')
    
    out.out_print('a')
    out.out_print('ae')

    user_input=str(input())
       
    path=pathlib.Path(user_input)
    print_recursive(path,user_input)
    delete_dir(user_input)
    #D:\Tresh
    return out.out_print('af')

@error_handler
def birthday():
    global esc_e
    out.out_print('a')

    out.out_print('ag')
    decision=int(input())
    result=[]

    if decision==1:
        out.out_print('aj')
        n=int(input())
        if n>= 365:
           n=n%365
             
        today_d = datetime.now().date()
        d = timedelta(days = n)
        bday=today_d+d
        bday = bday.strftime("%d.%m.%Y")
        for i in book:
            if i["Birthday"]!=0 and i["Birthday"]!=None:
                if days_to_birthday(i["Birthday"])==n:
                    result.append(i)
        print(f'On {bday} you need to congratulate {len(result)} people from your Addressbook')        
        
        out.show_find(result)

    elif decision==2:
        out.out_print('ai')
        n=int(input())
        for i in book:
            if i["Birthday"]!=0 and i["Birthday"]!=None:
                if days_to_birthday(i["Birthday"])<=n:
                    result.append(i)
                
        if len(result)>0:
            print(f'In future {n} days you need to congratulate {len(result)} people from your Addressbook')
            out.show_find(result)
        else:
            print(f'In future {n} days nobody from your Addressbook will have birthday')


    elif decision==3:
        out.out_print('ah')
        name=input()
        result = book.find_value(name)
        if len(result)>1:
            print(f"I've found {len(result)} notes with this Name")
            out.show_find(result)
            out.out_print('ah')
            id_input=int(input())
            for i in result:
                if i["Id"]==id_input:
                    days=days_to_birthday(i['Birthday'])
                    print(f'{i["Name"]} from your Addressbook will have birthday in {days} days. Do not forget to congratulate!')   
                  
        elif len(result)==1:
            for i in result:
                days=days_to_birthday(i['Birthday'])
                print(f'{i["Name"]} from your Addressbook will have birthday in {days} days. Do not forget to congratulate!')
        else:
            out.out_print('al')
    
    elif decision==4 or decision=='exit':
        esc_e=False
        return "Closed"

    else:
        out.out_print('am')
        
                       
def days_to_birthday(bday):
    today_d = datetime.now().date()
    bday = datetime.strptime(bday, "%d.%m.%Y").date()
    bday = date(today_d.year, bday.month, bday.day)
    
    if today_d > bday:
        bday = date(today_d.year+1, bday.month, bday.day)
        days_left = (bday-today_d)
    else:
        days_left = (bday-today_d)
    
    return days_left.days

@error_handler
def delete():
    out.out_print('a')
    out.out_print('an')
    find_v = str(input())
    find_v=find_v.lower()
    result = book.find_value(find_v)
    for i in result:
        if i["Name"].lower()!=find_v:
            result.remove(i)

    if len(result)>1:
        print(f"I've found {len(result)} notes with this Name")
        out.show_find(result)
        out.out_print('ao')
        
        del_input=int(input())
        for i in book:
            if i["Name"].lower()==find_v and i["Id"]==del_input:
                book.remove(i)
                print(f"You've deleted {find_v}")
                save() 

    elif len(result)==1:
        for i in result:
            if i["Name"].lower()==find_v:
                book.remove(i)
                print(f"You've deleted {find_v}")
                save()   

    else:
        print(f"{find_v} not found")
                
#end
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@error_handler
def find():
    out.out_print('a')
    out.out_print('ap')
    find_v = str(input())
    result = book.find_value(find_v)
    out.show_find(result)
    
def save():
    sal.save(path, book, notes_book)  

def exit():
    global esc_e
    save()
    esc_e = False
    return out.out_print('aq')

#@error_handler
def show1():
    global book
    number = input('Please input the number or record on 1 page: ')
    try:
        number = int(number)
    except:
        number = 10

    out.out_print('ar')
    if number == 0 or number == None:
        number = 10
    
    iter = out.view(book,number)
    
    for i in iter:
        # Печать шапки с названием столбцов
        out.out_print('a')
        out.out_print('at')
        out.out_print('a')
        print(i)
        out.out_print('au')
        input()
        
    return out.out_print('av')
##############################################################
# Команды для Handler для работы с NotesBook

@error_handler
def add_note():
    out.out_print('aw')
    # ввод многострочной заметки
    lines = []
    flag = True
    while flag:
        line = input()
        if len(line)>0 and len(line)<=40:
            lines.append(line)
        elif len(line)>40:
            out.out_print('ax')
        else:
            flag = False
    text = '\n'.join(lines)
    # ввод тєгов
    flag = True
    while flag:
        hashtag = input('Please input the hashtag of your note: \n')
        # добавление заметки в NotesBook
        if len(line)>0 and len(line)<40:
               
            notes_book.add_note(text, hashtag.upper())
            flag = False
            return out.out_print('ay')
        else:
            return out.out_print('az')
                

@error_handler
def delete_note():
    out.out_print('ba')
    hashtag = input().upper()
    notes_book.delete_note(hashtag)
    return f"The note with hashtag '{hashtag}' is deleted"


@error_handler
def edit_note():
    out.out_print('bb')
    hashtag = input().upper()
    notes_book.edit_note(hashtag)
    
@error_handler
def find_note():
    out.out_print('bc')
    
    keyword = input().upper()
    out.out_print('bd')
    
    result=notes_book.find_note(keyword)
    if result:
        print(result)
        return out.out_print('be')
    else:
        return out.out_print('bf')

@error_handler
def sort_notes():
    out.out_print('bg')
    search_type = input()
    out.out_print('bj')
    print(notes_book.sort_notes(search_type))
    return out.out_print('bi')

@error_handler
def show_notes():
    out.out_print('bh')
    print(notes_book)
    return out.out_print('bk')

# Конец конец команд для NotesBook


def help_func():
    out.out_print('a')
    out.out_print('bl')
    out.out_print('bm')
    out.out_print('bn')
    out.out_print('bo')
    out.out_print('bp')
    out.out_print('bq')
    return out.out_print('a')


@error_handler
def handler(user_inpu):
    if user_inpu in ANSWEARS.keys():
        return ANSWEARS[user_inpu]()
    elif user_inpu in ADD:
        out.out_print('br')
        decision=str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return add()
    elif user_inpu in CHANGE:
        out.out_print('bs')
        decision=str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return change()

    elif user_inpu in FIND:
        out.out_print('bt')
        decision=str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return find()
    
    elif user_inpu in HELP:
        out.out_print('bu')
        decision=str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return help_func()

    elif user_inpu in DELETE:
        out.out_print('bv')
        decision=str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return delete()
    
    elif user_inpu in BIRTHDAY:
        out.out_print('bw')
        decision=str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return birthday()
    
    elif user_inpu in CLEAN:
        out.out_print('bx')
        decision=str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return clean_folder()

    elif user_inpu in SHOW:
        out.out_print('by')
        decision=str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return show1()
    else:
        return input_error()



def input_error():
    return out.out_print('bz')


ANSWEARS = {'add': add, 'ad': add, '+': add, 'фвв': add,'change': change, 'срфтпу': change, 'close': exit, 'exit': exit,'учше': exit, 'clear': clear, 'сдуфк': clear,
            'find': find, 'аштв': find, 'help': help_func, 'рудз': help_func, 'хелп': help_func, 'save': save, 'іфму': save, 'ыфму': save, 'show': show1, 'ырщц': show1, 'ірщц': show1,
            'delete':delete, 'del':delete, 'вуд':delete, 'вудуеу':delete,'birthday':birthday, 'ишкервфн':birthday, 'clean': clean_folder, 'сдуфт': clean_folder,
            'add note': add_note, 'фвв тщеу': add_note, 'delete note': delete_note, 'вудуеу тщеу': delete_note, 'edit note': edit_note, 'увше тщеу': edit_note,
            'find note': find_note, 'аштв тщеу': find_note, 'sort notes': sort_notes, 'ыщке тщеуы': sort_notes, 'show notes': show_notes, 'ырщц тщеуы': show_notes }

ADD=['a','ad','addd','asd','asdd','sdd','adf', 'фів', 'івв', 'фівв', 'фввв', 'фва', 'вв', 'ыва', 'фвы', 'фыв', 'явв', 'фв']
CHANGE=['chane', 'chnge', 'cange', 'chenge', 'hange', 'chng', 'cchenge', 'chhenge', 'cheenge', 'chaange', 'сменить', 'chang', 'срутпу', 'срутп', 'менять', 'изменить', 'срфтп', 'рсфтпу', 'срутпу','cheng']
FIND=['fnd', 'ind', 'fid', 'fin', 'faind', 'fand', 'ffind', 'fiind', 'finnd', 'findd', 'seek', 'look', 'look for', 'атв', 'афтв', 'штв', 'афт', 'поиск', 'искать', 'найти', 'шштв']
HELP=['&', '?', 'hlp', 'what', 'why', 'where', 'how', 'elp', 'hep', 'hel', 'healp', 'halp', 'hhelp', 'heelp', 'hellp', 'helpp', 'рфдз', 'рдз', 'руз', 'руд', 'помощь']
DELETE=['вуд', '-', 'del', 'вудуеу', 'вуфдуеу', 'dealete', 'elete', 'elet', 'delet', 'dlte', 'dlt', 'lete', 'dealete', 'вудуе', 'удалить', 'pop']
BIRTHDAY=['lf', 'birsday', 'bersday', 'bezday', 'bethday', 'birzday', 'bearsday', 'birthdey', 'beersday', 'brthday', 'иууксвфн', 'ишквфн', 'др', 'рождение', 'бездей', 'бирсдей', 'днюха', 'birthday people', 'birthday boy', 'birthday girl', 'birthda', 'birtda', 'birth','иуервфн', 'иуівфн', 'birt']
CLEAN=['cleen', 'clan', 'clin', 'cleane', 'cleene', 'klin', 'klean', 'lean', 'clen', 'kleen', 'суф', 'лдуут', 'лдуфт', 'сдуфту', 'клн', 'клин', 'разобрать', 'мусор']
SHOW=['ырща', 'ырщцу', 'showe', 'schow', 'schove', 'chov', 'shove', 'schov', 'schowe', 'how', 'sho', 'shouv', 'шов', 'ірщцу', 'показать', 'рщц', 'ірщм']


if __name__ == '__main__':
    sal=SerializeDeserilize()
    out=OutPut()
    main()
