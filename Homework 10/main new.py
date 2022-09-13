from src.db import *
from src.models import Contact, Phone, Email, Note
from sqlalchemy.orm import joinedload
from faker import Faker
fake = Faker()

def change():
    pass

def add_contact_fake():
    for i in range(10):
        addcontact = Contact(name=fake.first_name())
        session.add(addcontact)
        session.commit()

        addphone = Phone(phone=fake.phone_number(), contact_id=addcontact.id)
        session.add(addphone)
        session.commit()
       
        addemail = Email(email=fake.ascii_free_email(), contact_id=addcontact.id)
        session.add(addemail)
        session.commit()
      
        addenote = Note(note='FAKE', contact_id=addcontact.id)
        session.add(addenote)
        session.commit()

def error_handler(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except:
            result = input_error()
            return result

    return inner


def input_error():
    return 'Wrong input! Type exact command you want to do,"exit" to exit or "help" for list of commands.'


def exit_p():
    print("Good Bye")
    return 'exit'


@error_handler
def main(esc_e=True):
    while esc_e:
        print(50 * '_')
        user_input = input(
            '   What do you want to do?\n'
            '   Type exact command you want to do, \n'
            '   "help" for list of commands.\n   '
            '"exit" to exit\n')
        print()
        user_input = user_input.lower()
        output = handler(user_input)
        if output == 'exit':
            break

#Adding Contact
def add():
    print(145 * '_')
    name = input('Input Name:\n')
    phone = input('Input Phone:\n')

    addcontact = Contact(name=name)
    session.add(addcontact)
    session.commit()

    addphone = Phone(phone=phone, contact_id=addcontact.id)
    session.add(addphone)
    session.commit()

    while True:
        print('Do you want to add E-mail? "y" (YES) or n (NO). Type "exit" to exit')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            
            email = input('Input E-mail. Please no more than 30 symbols.\n')
            #if re.match("([a-zA-Z][a-zA-Z0-9.!#$%^*=-]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,})", email):
            if 1 < len(email) <= 30:
                addemail = Email(email=email, contact_id=addcontact.id)
                session.add(addemail)
                session.commit()
                break
            else:
                print(f'Your E-mail is {len(email)} symbols. Please no more than 30 symbols')
            # else:
            #     print('Format is wrong. Try again in format: your_nickname@something.domen_name')
        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision == 'учше':
            return 'exit'

        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет' or decision == 'тщ' or decision == 'тще' or decision == 'т':
            addemail = Email(email="No", contact_id=addcontact.id)
            session.add(addemail)
            session.commit()
            break

        else:
            print('Wrong input!')

    while True:
        print('Do you want to add Notes? "y" (YES) or n (NO). Type "exit" to exit')
        decision = str(input())
        decision = decision.lower()

        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            print('Input Notes. Please no more than 50 symbols')
            notes = input()
            if 1 < len(notes) <= 50:
                addnote = Note(note=notes, contact_id=addcontact.id)
                session.add(addnote)
                session.commit()
                break
            else:
                print(f'Your Tags is {len(notes)} symbols. Please no more than 50 symbols')

        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision == 'учше':
            return 'exit'

        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет' or decision == 'тщ' or \
                decision == 'тще' or decision == 'т':

            addnote = Note(note='', contact_id=addcontact.id)
            session.add(addnote)
            session.commit()
            break

        else:
            print('Wrong input!')


def delete():
    print('DELETING')
    item = find()
    print(50*'*')
    choice = input("You are going to delete it. \nPress 1 to delete, "
                   "\nPress 0 to cancel\n")
    if choice:
        user = session.query(Contact).filter(Contact.id == item.id).first()
        session.delete(user)
        session.commit()
        print(f'{item.name} DELETED')
    else:
        print('Canceling')


def find():
    name = input('What contact do you want to find. Enter the proper name: ')
    item = session.query(Contact).filter(Contact.name == name).one()
    show(item)
    return item



def show(item=None):
    print(50 * '_')

    if item is None:
        item = session.query(Contact).options(joinedload('email'), joinedload('note'), joinedload('phone')).all()
        for person in item:
            print()
            print(f'id: {person.id},  name: {person.name},  phone: {[p.phone for p in person.phone]}, email: {[e.email for e in person.email]}, note:{[n.note for n in person.note]}')
    else:
        print(f'id: {item.id},  name: {item.name}')



@error_handler
def handler(user_inpu):
    if user_inpu in ANSWEARS.keys():
        return ANSWEARS[user_inpu]()
    elif user_inpu in ADD:
        print('Maybe you mean "add" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return add()
    elif user_inpu in CHANGE:
        print('Maybe you mean "change" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return change()

    elif user_inpu in FIND:
        print('Maybe you mean "find" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return find()

    elif user_inpu in HELP:
        print('Maybe you mean "help" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return help()

    elif user_inpu in DELETE:
        print('Maybe you mean "delete" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return delete()

    elif user_inpu in BIRTHDAY:
        print('Maybe you mean "birthday" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return birthday()

    elif user_inpu in SHOW:
        print('Maybe you mean "show" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return show()
    else:
        return input_error()


def birthday():
    pass


def help_func():
    print(60 * '*')
    # print(20 * '*' + 'WORKING WITH ADDRESSBOOK:' + 20 * '*')
    # print('*Type "clean"    to clean and structurise folder.\n')
    # print(60 * '*')
    # print(
    #     '*Type "add"    to add new contact.\n*Type "birthday" to see people that have birthday nearest days.\n*Type "change" to change contact\'s phone, name or birthday.\n*Type "find"   to see information that you are looking for.\n*Type "delete" to delete information that you don\'t need.\n*Type "show"   to show you all phonebook.\n*Type "save"   to save and exit.\n*Type "exit"   to exit')
    
    print(
         '*Type "add"    to add new contact.\n*Type "find"   to see information that you are looking for.\n*Type "delete" to delete information that you don\'t need.\n*Type "show"   to show you all phonebook.\n*Type "save"   to save and exit.\n*Type "exit"   to exit')
    print(60 * '*')


ANSWEARS = {'add': add, 'ad': add, '+': add, 'фвв': add, 'change': change, 'delete': delete, 'help': help_func,
            'close': exit_p, 'exit': exit_p, 'учше': exit_p,
            'find': find, 'аштв': find, 'show': show, 'ырщц': show}

# ANSWEARS = {'add': add, 'ad': add, '+': add, 'фвв': add,'change': change, 'срфтпу': change, 'close': exit, 'exit': exit,'учше': exit, 'clear': clear, 'сдуфк': clear,
#             'find': find, 'аштв': find, 'help': help_func, 'рудз': help_func, 'хелп': help_func, 'save': save, 'іфму': save, 'ыфму': save, 'show': show1, 'ырщц': show1, 'ірщц': show1,
#             'delete':delete, 'del':delete, 'вуд':delete, 'вудуеу':delete,'birthday':birthday, 'ишкервфн':birthday}

ADD = ['a', 'ad', 'addd', 'asd', 'asdd', 'sdd', 'adf', 'фів', 'івв', 'фівв', 'фввв', 'фва', 'вв', 'ыва', 'фвы', 'фыв',
       'явв', 'фв']
CHANGE = ['chane', 'chnge', 'cange', 'chenge', 'hange', 'chng', 'cchenge', 'chhenge', 'cheenge', 'chaange', 'сменить',
          'chang', 'срутпу', 'срутп', 'менять', 'изменить', 'срфтп', 'рсфтпу', 'срутпу', 'cheng']
FIND = ['fnd', 'ind', 'fid', 'fin', 'faind', 'fand', 'ffind', 'fiind', 'finnd', 'findd', 'seek', 'look', 'look for',
        'атв', 'афтв', 'штв', 'афт', 'поиск', 'искать', 'найти', 'шштв']
HELP = ['&', '?', 'hlp', 'what', 'why', 'where', 'how', 'elp', 'hep', 'hel', 'healp', 'halp', 'hhelp', 'heelp', 'hellp',
        'helpp', 'рфдз', 'рдз', 'руз', 'руд', 'помощь']
DELETE = ['вуд', '-', 'del', 'вудуеу', 'вуфдуеу', 'dealete', 'elete', 'elet', 'delet', 'dlte', 'dlt', 'lete', 'dealete',
          'вудуе', 'удалить', 'pop']
BIRTHDAY = ['lf', 'birsday', 'bersday', 'bezday', 'bethday', 'birzday', 'bearsday', 'birthdey', 'beersday', 'brthday',
            'иууксвфн', 'ишквфн', 'др', 'рождение', 'бездей', 'бирсдей', 'днюха', 'birthday people', 'birthday boy',
            'birthday girl', 'birthda', 'birtda', 'birth', 'иуервфн', 'иуівфн', 'birt']
CLEAN = ['cleen', 'clan', 'clin', 'cleane', 'cleene', 'klin', 'klean', 'lean', 'clen', 'kleen', 'суф', 'лдуут', 'лдуфт',
         'сдуфту', 'клн', 'клин', 'разобрать', 'мусор']
SHOW = ['ырща', 'ырщцу', 'showe', 'schow', 'schove', 'chov', 'shove', 'schov', 'schowe', 'how', 'sho', 'shouv', 'шов',
        'ірщцу', 'показать', 'рщц', 'ірщм']

if __name__ == '__main__':
    add_contact_fake()
    main()