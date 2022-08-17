import ast
import asyncio
from mimetypes import suffix_map
import re
import aioshutil
import time
  
from aiopath import AsyncPath

dir_list=['audio', 'images', 'documents', 'video', 'archives', 'unknown']
dict_of_value={'audio':[], 'images':[], 'documents':[], 'video':[], 'archives':[], 'unknown':[]}

AUDIO=['.amr', '.ogg', '.wav', '.mp3']
IMAGES=['.svg','.jpg','.jpeg','.png']
VIDEO=['.avi', '.mp4', '.mov', '.mkv', '.wmv']
DOCUMENTS=['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx','.rtf','.xls']
ARCHIVES=['.zip', '.gz', '.tar']
UNKNOWN=[]

async def create_dir(path): #Создание папки для сортировки мусора
    
    new_dir = AsyncPath(path + '_sorted')
    print(new_dir)

    if not await new_dir.exists():
        await new_dir.mkdir()
        
    return new_dir



async def scan_directory(as_path):
    global dict_of_value

    if await as_path.exists():
        if await as_path.is_dir() and as_path.name not in dir_list :
            async for element in as_path.iterdir():
                if await  element.is_file():
                    if element.suffix in AUDIO:
                        dict_of_value['audio'].append(element)
                        
                    elif element.suffix in IMAGES:
                        dict_of_value['images'].append(element)
                    
                    elif element.suffix in DOCUMENTS:
                        dict_of_value['documents'].append(element)
                        
                    elif element.suffix in ARCHIVES:
                        dict_of_value['archives'].append(element)
                    
                    elif element.suffix in VIDEO: 
                        dict_of_value['video'].append(element)
                    else:
                        dict_of_value['unknown'].append(element)
                else:
                    await scan_directory(element)
                    

async def change_dist(key, value):
    start_dir = AsyncPath(path)
    new_dir = AsyncPath(start_dir/key)
    
    if not await new_dir.exists():
        await new_dir.mkdir()

    for elem in value:
        new_name=normalize(elem)
        
        if key=='archives':
            await unzip(elem,new_name)   
            
        else:
            await aioshutil.move(elem, new_dir/new_name)


async def delete_dir(path):
    path=AsyncPath(path)
    if await path.is_dir() and path.name not in dir_list:
        async for element in path.iterdir():
            if await element.is_dir() and element.name not in dir_list:
                await aioshutil.rmtree(element)
            else:
                await delete_dir(element)


async def main():
    
    #new_path = await create_dir(path)
    await scan_directory(as_path)
    await tasks_asc()
    await delete_dir(as_path)

def normalize(text):
    
    cyrilic_f = ['А','Б','В','Г','Ґ','Д','Е','Є','Ж','З','И','І','Ї','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ю','Я', 'Ы', 'Ё', 'Э',
                'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я', 'ы', 'ё', 'э']
    cyr = ','.join(cyrilic_f)            

    trans_f = ['A','B','V','H','G','D','E','E','Z','Z','Y','I','I','Y','K','L','M','N','O','P','R','S','T','U','F','H','T','C','S','S','Y','Y', 'Y', 'E', 'E',
              'а', 'b', 'v', 'h', 'g', 'd', 'е', 'e', 'z', 'z', 'y', 'i', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 't', 'c', 's', 's', 'y', 'y', 'y', 'e','e']
    trans = ','.join(trans_f) 
    text=AsyncPath(text)
    
    new_name=text.stem
    end_suff=text.suffix
    dictionary = str.maketrans(cyr, trans)
    
    clean_text = re.sub('[^\w\s]', '_', new_name)
    result=clean_text.translate(dictionary)
    return result+end_suff

async def tasks_asc():
    features=[change_dist(key,value) for key,value in dict_of_value.items()]
    result=[]
    for i in features:
        result.append(asyncio.ensure_future(i))
    for j in result:
        await j

async def unzip(elem,new_name):
    new_name=AsyncPath(new_name)
    start_dir=AsyncPath(path)
    new_dir=(start_dir/'archives')
    await aioshutil.unpack_archive(elem, new_dir/new_name.stem, elem.suffix[1:])
    await elem.unlink()   
 

if __name__ == "__main__":
    #path = (r'C:\Users\EcoVista\Desktop\Trasch')
    path = input(f'Укажите полный путь к папке, которую нужно разобрать: \n')
    as_path = AsyncPath(path)
    print(100*'*')

    started = time.time()
    asyncio.run(main())
    elapsed = time.time() - started
    
    print("Времени затрачено: {:.5f}s".format(elapsed))
    
