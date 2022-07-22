from enum import auto
import re
from abc import ABC, abstractmethod
from collections import UserList
from datetime import datetime
import pickle
from typing import ByteString


class InfoView(ABC):
    @abstractmethod
    def view(self):
        pass
    @abstractmethod
    def show_find(self):
        pass
    @abstractmethod
    def out_print(self):
        pass

class Field:
    def __init__(self, value):
        self.__value = value
        # self.value=value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class AddressBook(UserList):

    data = []

    def add_record(self, record):
        self.data.append(record)

    def find_value(self, f_value):
        f_value = f_value.lower()

        result = []
        for i in self:
            for value in i.values():
                if (isinstance(value, str)):
                    value = value.lower()
                    if value.find(f_value) != -1:
                        if i not in result:
                            result.append(i)
                            break
                elif value != None:
                    if (isinstance(value, list)):
                        for j in value:
                            j = j.lower()
                            if j.find(f_value) != -1:
                                result.append(i)
                                break
        return result

class OutPut(InfoView):

    def view(self, data, n):
        counter = 0
        result = ""
        for i in data:
            result += f'|{i["Id"]:<5}| {i["Name"]:<25}| { i["Phones"][0] if len(i["Phones"])>=1 else " ":<15} | {i["Birthday"]if i["Birthday"] else " ":<11}|{i["Address"]if i["Address"] else " ":<30}|  {i["E-mail"]if i["E-mail"] else " ":<30}| {i["Tags"] if i["Tags"] else " ":<15}|\n'
            if len(i["Phones"]) > 1:
                for elem in i["Phones"][1:]:
                    result += f'|     |                          | {elem: <15} |            |                              |                                |                | \n'
            result += f"{145*'_'}\n"
            # конец записи строки с описанием 1 контакта
            counter += 1
            if counter == n:
                result = result.rstrip("\n")
                yield result
                result = ""
                counter = 0
        if result:
            result = result.rstrip("\n")
            yield result

    def show_find(self, v_list,n=10):
    
        print("I've found following:")
        # Печать шапки с названием столбцов
        print(145*'_')
        print('| ID  |           Name           |     Phones      |  Birthday  |           Address            |              E-mail            |       Tags     |')
        print(145*'-')
        
        for i in v_list:
            print(f'|{i["Id"]:<5}| {i["Name"]:<25}| { i["Phones"][0] if len(i["Phones"])>=1 else " ":<15} | {i["Birthday"]if i["Birthday"] else " ":<11}|{i["Address"]if i["Address"] else " ":<30}|  {i["E-mail"]if i["E-mail"] else " ":<30}| {i["Tags"] if i["Tags"] else " ":<15}|')
            if len(i["Phones"]) > 1:
                for elem in i["Phones"][1:]:
                    print(f'|     |                          | {elem: <15} |            |                              |                                |                |')
            print(145*'_')

    def out_print(self,data):

        a=145*'_'
        b='What do you want to do?\nYou can use commands:\n'
        c='1.  "load" to load AddressBook and NotesBook\n2.  "new" to create new Book\n3.  "exit"/"close" to close application:'
        d='Please write the full path to file with addressbook and notebook. Example: "d:\\test\\book.txt":'
        e='Please write right path to file! This file is empty!'
        f='Please write the full path where to create file. Example: "d:\test\book.txt":'
        g='Wrong command.'
        h='Successfully changed'
        i='Do you want to add phone-number? "y" (YES) or "n" (NO). Type "exit" to exit'
        j='Input Phone Number. Example: +380501234567'
        k='Wrong input! Phone may start with + and has from 3 to 12 digits max. Example +380501234567'
        l='Do you want to add Birthday? "y" (YES) or n (NO). Type "exit" to exit'
        m='Input Birthday. Expected day.month.year(Example:25.12.1970)'
        n='Wrong Birthday. Expected day.month.year. Format: dd.mm.yyyy (Example:25.12.1970)'
        o='Do you want to add Address? "y" (YES) or n (NO). Type "exit" to exit'
        p='Input Address. Please no more than 30 symbols'
        q='Do you want to add E-mail? "y" (YES) or n (NO). Type "exit" to exit'
        r='Input E-mail. Please no more than 30 symbols'
        s='Format is wrong. Try again in format: your_nickname@something.domen_name'
        t='Do you want to add Tags? "y" (YES) or n (NO). Type "exit" to exit'
        u='Input Tags. Please no more than 15 symbols'
        v='Type name of record you want to change'
        w='1.   To change Name: type "name".\n2.   To change Phone: type "phone".\n3.   To change Birthday: type "birthday".\n4.   To change Address: type "address".\n5.   To change E-mail: type "email".\n6.   To change Tags: type "tags"\n7.   To exit: type "exit".'
        x='Please enter Id to change the right record'
        y='Type phone you want to change.If there are no phones - just press "enter".'
        z='Type birthday you want to change. Expected day.month.year(Example:25.12.1970). If there is no birthday - just press "enter".'
        aa='Type address you want to change. If there is no address - just press "enter".'
        ab='Type E-mail you want to change.)'
        ac='Type Tags you want to change. If there are no Tags - just press "enter"'
        ad='Welcome to clean folder instrument!'
        ae='Please enter path to clean and structurise.'
        af='Everything done! Please check yor folder!'
        ag="1.   If you want to find, who'll have birthday in exact date TYPE 1.\n2.   If you need to know who'll have birthday in period of time TYPE 2.\n3.   If you need to know how many days to somebody's birthday TYPE 3.\n4.   Type 'exit' to exit"
        aj="Please write in how many days will be people's birthday."
        ai="Please write how many days in advance to warn you about people's birthday."
        ah='Please write name to know how many days left to birthday.'
        ak='Please enter Id to know how many days left to birthday the exact person'
        al='No information about birthday. Please enter valid information using command "change" or add new person to Addressbook'
        am='Not found this Name!'
        an='Put Name, you want to find and delete from your addressbook'
        ao='Please enter Id to delete the right note'
        ap='Put word, half of word or digits you want to find'
        aq='Good Bye'
        ar='The contacts book is following:'
        at='| ID  |           Name           |     Phones      |  Birthday  |           Address            |              E-mail            |      Tags      |'
        au=52*'_'+'The end of the page. PRESS ENTER'+52*'_'
        av="The end of the contacts book"
        aw='Please input your note (to stop entering note press "ENTER" twice):'
        ax='Please no more than 40 symbols in one line'
        ay='Your note is successfully saved'
        az='Please no more than 30 symbols'
        ba='Please input a hashtag of note that you would like to delete:'
        bb='Please input a hashtag of note that you would like to edit:'
        bc='Please input keyword for search:'
        bd='THE RESULTS OF SEARCH:'
        be="The search is sucessfully finished"
        bf="Not found keyword"
        bg='What type of sort would you like? Please input:\n1 - to sort from A to Z\n2 - to sort from Z to A\n3 - to sort from old notes to new notes\n4 - to sort from new notes to old notes'
        bj='The sorted Notes are:'
        bi='The end of sorted Notes'
        bh='Your Notes Book:'
        bk="The end of Notes Book"
        bl=20*'*'+'WORKING WITH ADDRESSBOOK:'+20*'*'
        bm='*Type "add"      to add new contact.\n*Type "birthday" to see people that have birthday nearest days.\n*Type "change"   to change contact\'s phone, name or birthday.\n*Type "clear"    to clear terminal window.\n*Type "delete"    to delete information that you don\'t need.\n*Type "find"      to see information that you are looking for.\n*Type "show"      to show you all phonebook.\n*Type "save"      to save and exit.\n*Type "exit"      to exit'
        bn=20*'*'+'WORKING WITH NOTESBOOK:'+20*'*'
        bo='*Type "add note"     to add new note.\n*Type "delete note" to delete note.\n*Type "edit note"    to edit note.\n*Type "find note"    to look through notes.\n*Type "sort notes"   to sort notes.\n*Type "show notes"   to show your notes.\n'
        bp=20*'*'+'WORKING WITH CLEANFOLDER:'+20*'*'
        bq='*Type "clean"    to clean and structurise folder.\n' 
        br='Maybe you mean "add" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"'
        bs='Maybe you mean "change" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"'
        bt='Maybe you mean "find" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"'
        bu='Maybe you mean "help" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"'
        bv='Maybe you mean "delete" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"'
        bw='Maybe you mean "birthday" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"'
        bx='Maybe you mean "clean" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"'
        by='Maybe you mean "show" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"'
        bz='Wrong input! Type exact command you want to do,"exit" to exit or "help" for list of commands.'

        out_print_dict={'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'g':g, 'h':h,
                        'i':i, 'j':j, 'k':k, 'l':l, 'm':m, 'n':n, 'o':o, 'p':p,
                        'q':q, 'r':r, 's':s, 't':t, 'u':u, 'v':v, 'w':w, 'x':x, 
                        'y':y, 'z':z, 'aa':aa, 'ab':ab, 'ac':ac, 'ad':ad, 'ae':ae, 
                        'af':af, 'ag':ag, 'aj':aj, 'ai':ai, 'ah':ah, 'ak':ak, 'al':al,
                        'am':am, 'an':an, 'ao':ao, 'ap':ap, 'aq':aq, 'ar':ar,
                        'at':at, 'au':au, 'av':av, 'aw':aw, 'ax':ax, 'ay':ay, 'az':az,
                        'ba':ba, 'bb':bb, 'bd':bd, 'be':be, 'bf':bf, 'bg':bg, 'bj':bj,
                        'bi':bi, 'bh':bh, 'bk':bk, 'bl':bl, 'bm':bm, 'bn':bn, 'bo':bo,
                        'bp':bp, 'bq':bq, 'br':br, 'bs':bs, 'bt':bt, 'bu':bu, 'bc':bc,
                        'bv':bv, 'bw':bw, 'bx':bx, 'by':by, 'bz':bz}
        
        return print((out_print_dict[data]))


#START OF CHANGING
class Address(Field):
    def __init__(self, address):
        self.address = address

class Tags(Field):
    def __init__(self, tags):
        self.tags = tags

class Id(Field):
    def __init__(self, id_n):
        self.id_n = id_n

class Email(Field):
    def __init__(self, email):
        self.email=email

class Birthday(Field):
    def __init__(self, value):
        self.__birthday = None
        self.birthday = value

    @ property
    def birthday(self):
        return self.__birthday.strftime('%d.%m.%Y')

    @ birthday.setter
    def birthday(self, birthday):
        try:
            self.__birthday = datetime.strptime(birthday, '%d.%m.%Y')
        except Exception:
            print("Incorrect format, expected day.month.year (Example:25.12.1970)")
    

class Record():
    def __init__(self, name, id_n, phones=None, birthday=None, address=None, email=None, tags=None ):
        self.id_n = id_n
        self.phones = []
        self.birthday = None
        self.address=None
        self.email=None
        self.tags=None
        self.user = {'Id': self.id_n, 'Name': name.name,
                     'Phones': self.phones, 
                     'Birthday': self.birthday, 
                     'Address':self.address, 
                     'E-mail':self.email, 
                     'Tags':self.tags}
#Start to add


    def add_address(self, address):
        self.address = address

    def add_email(self, email):
        self.email = email

    def add_id(self, id_n):
        self.id_n = id_n
    
    #End       
    def add_phone(self, phone):
        phone = str(phone)
        try:
            num = re.fullmatch('[+]?[0-9]{3,12}', phone)
            if num:
                self.phones.append(phone)
        except:
            print('Phone must start with + and have 12 digits. Example +380501234567 ADD')

    

    def remove_phone(self, phone):
        for i in range(len(self.phones)):
            if self.phones[i].phone == phone:
                self.phones.pop(i)

    def edit_phone(self, phone, new_phone):
        self.remove_phone(phone)
        self.add_phone(new_phone)


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        phones = []
        self.phones = list()
        self.__phone = phone

    @ property
    def phone(self):
        return self.__phone

    @ phone.setter
    def phone(self, value):
        self.__phone = ''
        if re.fullmatch('[+]?[0-9]{3,12}', value):
            self.__phone = value
        else:
            print('Phone must start with + and have 12 digits. Example +380501234567')

    # def __str__(self):
        # return self.phone
    def __repr__(self):
        return self.phone

class SerializeDeserilize():

    def save(self,path, book, notes_book):
        with open(path, 'wb') as fh:
            pickle.dump(book, fh)
            pickle.dump(notes_book, fh)
            
    def load(self,path):
        with open(path, 'rb') as fh:
            book = pickle.load(fh)
            notes_book = pickle.load(fh)
        return book, notes_book