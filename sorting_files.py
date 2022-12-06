from pathlib import *
import shutil , sys, rarfile, os

# Списки розширень для сортування
list_img = ['.JPEG', '.jpeg', '.PNG', '.png', '.JPG', '.jpg', '.SVG', '.svg']
list_archive = ['.rar', '.RAR', '.zip', '.ZIP', '.gz', '.GZ', '.tar', '.TAR', '.7z', '.7Z']
list_video = ['.AVI', '.avi', '.MP4', '.mp4', '.MOV', '.mov', '.MKV', '.mkv']
list_documents = ['.DOC', '.doc', '.DOCX', '.docs', '.TXT','.txt', '.PDF', '.pdf', '.XLSX', '.xlsx', '.PPTX', '.pptx', '.xml', '.XML']
list_music = ['.MP3', '.mp3', '.OGG', '.ogg', '.WAV', '.wav', '.AMR', '.amr']

#Загальний список файлів
rez = []

# Списки відсортованих файлів
rez_img = []
rez_archive = []
rez_video = []
rez_documents = []
rez_music = []
rez_other = []

#Список знайдених розширень
suffix_img = set()
suffix_archive = set()
suffix_video = set()
suffix_document = set()
suffix_music = set()
suffix_other = set()


# Аналіз папки з файлами
def analiz_files(path_file, level=1):
    #print('Рівень = ', level, 'Контент = ' , os.listdir(path_file))
    
    for i in os.listdir(path_file):               
        if os.path.isdir(path_file + '\\' + i):
            #print('Заходимо у папку: ' + path_file + '\\' + i)
            analiz_files(path_file + '\\' + i, level = level+1)            
        else:
            #print(Path(i)) 
            rez.append(i)            
    return rez                     
                
           
#Робоча директорія для проведення розбору файлів
def __sorting_files__():
    try:
        dyrectory_current = sys.argv[1]
        analiz_files(dyrectory_current)
    
        for j in rez:
            if Path(j).suffix in list_img:
                rez_img.append(j) 
                suffix_img.add(Path(j).suffix)      
            elif Path(j).suffix in list_archive:
                rez_archive.append(j)
                suffix_archive.add(Path(j).suffix)
            elif Path(j).suffix in list_video:
                rez_video.append(j)
                suffix_video.add(Path(j).suffix)
            elif Path(j).suffix in list_music:
                rez_music.append(j)
                suffix_music.add(Path(j).suffix)
            elif Path(j).suffix in list_documents:
                rez_documents.append(j)
                suffix_document.add(Path(j).suffix)
            else:
                rez_other.append(j) 
                suffix_other.add(Path(j).suffix)  


        #Виводимо повідомлення про знайдене:
        if len(suffix_img) > 0:
            print('__________________________________________________________')
            print('__________________________________________________________')
            print('Результат фото (знайдені розширення та відповідні файли):')
            print('Розширення фото:')
            for d in suffix_img:
                print(d)
            print('__________________________________________________________')
            print('Файли фото:')
            for g in rez_img:
                print(g)
        if len(suffix_archive) > 0:
            print('__________________________________________________________')
            print('__________________________________________________________')
            print('Результат архіви (знайдені розширення та відповідні файли):')
            print('Розширення архівів:')
            for h in suffix_archive:
                print(h)
            print('__________________________________________________________')
            print('Файли архівів:')
            for k in rez_archive:
                print(k)
        if len(suffix_video) > 0:
            print('__________________________________________________________')
            print('__________________________________________________________')
            print('Результат відео (знайдені розширення та відповідні файли):')
            print('__________________________________________________________')
            print('Розширення відео:')
            for l in suffix_video:
                print(l)
            print('__________________________________________________________')
            print('Файли відео:')
            for z in rez_video:
                print(z)
        if len(suffix_music) > 0:
            print('__________________________________________________________')
            print('__________________________________________________________')
            print('Результат музика (знайдені розширення та відповідні файли):')
            print('__________________________________________________________')
            print('Розширення музика:')
            for x in suffix_music:
               print(x)
            print('__________________________________________________________')
            print('Файли музика:')
            for c in rez_music:
                print(c)
        if len(suffix_document) > 0:
            print('__________________________________________________________')
            print('Результат документи (знайдені розширення та відповідні файли):')
            print('__________________________________________________________')
            print('Розширення документи')
            for v in suffix_document:
                print(v)
            print('__________________________________________________________')
            print('Файли документів:')
            for b in rez_documents:
                print(b)
        if len (suffix_other) > 0:
            print('__________________________________________________________')
            print('Результат інші файли (знайдені розширення та відповідні файли):')
            print('__________________________________________________________')
            print('Розширення інше:')
            for n in suffix_other:
                print(n)
            print('__________________________________________________________')
            print('Файли інше:')
            for m in rez_other:
                print(m)
          
    except:
        print('Введіть шлях до папки')

__sorting_files__()


#Створюємо папку для відсортованих файлів
new_folder = Path.cwd() /'Нова папка'
if not Path.exists(new_folder):
    Path.mkdir(new_folder)