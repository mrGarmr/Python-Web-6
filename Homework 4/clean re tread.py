import re
import aiopath
import shutil
import time
from threading import Thread

dir_list = ['audio', 'images', 'documents', 'video', 'archives', 'unknown']

AUDIO = ['.amr', '.ogg', '.wav', '.mp3']
IMAGES = ['.svg','.jpg','.jpeg','.png']
VIDEO = ['.avi', '.mp4', '.mov', '.mkv']
DOCUMENTS = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx','.rtf','.xls']
ARCHIVES = ['.zip', '.gz', '.tar']
UNKNOWN = []

def change_dist(path_dist,path_g,name_list_dir,user_input):
    
    e_suf=path_dist.suffix
    name_new=str(path_dist.stem).split('.')[0]
    name_w=normalize(path_dist.stem)
    
    name_n=name_w+e_suf
    d_d=user_input+'\\'+name_list_dir
    d_dpath=aiopath.path(d_d)
    
    if not d_dpath.exists():
        d_dpath.mkdir()
    d=user_input+'\\'+name_list_dir+'\\'+name_n
    if name_list_dir!='archives':
        shutil.move(path_dist, d)
    else:
        d_w=user_input+'\\'+name_list_dir+'\\'+name_w
        shutil.move(path_dist, d)
        shutil.unpack_archive(d, d_w)
        rem_ar=aiopath.path(d)
        rem_ar.unlink()

def normalize(text):
    
    cyrilic_f = ['А','Б','В','Г','Ґ','Д','Е','Є','Ж','З','И','І','Ї','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ю','Я', 'Ы', 'Ё', 'Э',
                'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я', 'ы', 'ё', 'э']
    cyr=','.join(cyrilic_f)            

    trans_f = ['A','B','V','H','G','D','E','E','Z','Z','Y','I','I','Y','K','L','M','N','O','P','R','S','T','U','F','H','T','C','S','S','Y','Y', 'Y', 'E', 'E',
              'а', 'b', 'v', 'h', 'g', 'd', 'е', 'e', 'z', 'z', 'y', 'i', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 't', 'c', 's', 's', 'y', 'y', 'y', 'e','e']
    trans = ','.join(trans_f)
    
    dictionary = str.maketrans(cyr, trans)
    clean_text = re.sub('[^\w\s]', '_', text)
    result = clean_text.translate(dictionary)
    
    return result
 
def print_recursive(path,user_input):
    audio_list=[]
    video_list=[]
    images_list=[]
    documents_list=[]
    archive_list=[]
    unknown_list=[]

    if path.exists():
        if path.is_dir() and path.name not in dir_list :
            for element in path.iterdir():
                t = Thread(target=print_recursive, args=(element,user_input))
                t.start()
                t.join()


                if element.is_file():
                    if element.suffix in AUDIO:
                        audio_list.append(element)

                    elif element.suffix in IMAGES:
                        images_list.append(element)
                        
                    elif element.suffix in DOCUMENTS:
                        documents_list.append(element)
                    
                    elif element.suffix in ARCHIVES:
                        archive_list.append(element)

                    elif element.suffix in VIDEO: 
                        video_list.append(element)   

                    else:
                        unknown_list.append(element)

                else:
                    print_recursive(element,user_input)
          
    for element in audio_list:
        t1 = Thread(target=change_dist, args=(element,path,'audio',user_input))
        t1.start()
        t1.join()


    for element in documents_list:
        t2 = Thread(target=change_dist, args=(element,path,'documents',user_input))
        t2.start()
        t2.join()


    for element in archive_list:
        t3 = Thread(target=change_dist, args=(element,path,'archives',user_input))
        t3.start()
        t3.join()
   
    for element in video_list:
        t4 = Thread(target=change_dist, args=(element,path,'video',user_input))
        t4.start()
        t4.join()

    for element in images_list:
        t5 = Thread(target=change_dist, args=(element,path,'images',user_input))
        t5.start()
        t5.join()
   
    for element in unknown_list:
        t6 = Thread(target=change_dist, args=(element,path,'unknown',user_input))
        t6.start()
        t6.join()

def delete_dir(path):
    
    path = aiopath.path(path)
    if path.is_dir() and path.name not in dir_list:
        for element in path.iterdir():
            if element.is_dir() and element.name not in dir_list:
                shutil.rmtree(element)
            else:
                delete_dir(element)


def main(user_input):
    path = aiopath.path(user_input)  
    print_recursive(path,user_input)
    delete_dir(path)
    return path

def delete_dir(path):
    path = aiopath.path(path)
    if path.is_dir() and path.name not in dir_list:
        for element in path.iterdir():
            if element.is_dir() and element.name not in dir_list:
                shutil.rmtree(element)
            else:
                delete_dir(element)

if __name__=='__main__':
    print(100*'_')
    print('Please enter the path to directory, you need to clean up:')
    print(100*'_')
    started = time.time()
    main(input())
    
    elapsed = time.time() - started
    print("Времени затрачено: {:.5f}s".format(elapsed))
    
    