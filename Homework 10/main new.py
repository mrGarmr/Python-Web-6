from src.mongo import *

# from faker import Faker
# fake = Faker()


def change():
    print('CHANGING PHONE NUMBER')
    name = input('Please enter the name of contact you want to change phone number: \n')
    contact_counter = assistant.count_documents(
        {"name": name})

    if contact_counter > 0:
        phone = input(f'Please enter new phone for {name}: \n')
        assistant.delete_many({"name": name})
        assistant.insert_one({"name": name, "phone": phone})

    else:
        print('There is not such contact.')


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
    contact_counter = assistant.count_documents({"name": name, "phone": phone})

    if contact_counter == 0:
        assistant.insert_one({"name": name, "phone": phone})
        print(f'\n\tContact has been successfully added to addressbook')
    else:
        print(f'\n\tEntered contact with phone {phone} already exist')


def delete():
    print('DELETING')
    name = find()
    print(50*'*')
    choice = input("You are going to delete it. \nPress 1 to delete, "
                   "\nPress 0 to cancel\n")
    if choice and name:
        assistant.delete_many({"name": name})
    else:
        print('Enter correct data.')


def find():
    name = input('What contact do you want to find. Enter the proper name: ')

    show(name)
    contact_counter = assistant.count_documents(
        {"name": name})
    if contact_counter:
        return name
    else:
        return None


def show(name = None):
    if name is None:
        print(50 * '_')
        result = assistant.find({})
        for el in result:
            name = el['name']
            phone = el['phone']
            print()
            print(f'name: {name},  phone: {phone}')

    else:
        contact_counter = assistant.count_documents(
            {"name": name})

        if contact_counter > 0:
            result = assistant.find({'name': name})
            for el in result:
                name = el['name']
                phone = el['phone']
                print()
                print(f'name: {name},  phone: {phone}')
        else:
            print(f'\tThere is not such contact.')

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
    # add_contact_fake()
    main()