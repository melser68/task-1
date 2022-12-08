from pathlib import *
import shutil
import sys, re
import rarfile
import os
from unicodedata import normalize

# Списки розширень для сортування
list_img = ['.JPEG', '.jpeg', '.PNG', '.png', '.JPG', '.jpg', '.SVG', '.svg']
list_archive = ['.rar', '.RAR', '.zip', '.ZIP',
                '.gz', '.GZ', '.tar', '.TAR', '.7z', '.7Z']
list_video = ['.AVI', '.avi', '.MP4', '.mp4', '.MOV', '.mov', '.MKV', '.mkv']
list_documents = ['.DOC', '.doc', '.DOCX', '.docs', '.TXT', '.txt',
                  '.PDF', '.pdf', '.XLSX', '.xlsx', '.PPTX', '.pptx', '.xml', '.XML']
list_music = ['.MP3', '.mp3', '.OGG', '.ogg', '.WAV', '.wav', '.AMR', '.amr']

# Загальний список файлів
rez = []

# Список ігноруємих папок
list_ignore = set()

# Списки відсортованих файлів
rez_img = []
rez_archive = []
rez_video = []
rez_documents = []
rez_music = []
rez_other = []

# Список знайдених розширень
suffix_img = set()
suffix_archive = set()
suffix_video = set()
suffix_document = set()
suffix_music = set()
suffix_other = set()


# Аналіз папки з файлами та ігнорування папок якщо в назві міститься "sorted"
def analiz_files(path_file, level=1):
    for i in os.listdir(path_file):
        adres_string = str(Path(path_file + '\\' + i))  
        if re.search('.sorted', adres_string) == None:
            if os.path.isdir(path_file + '\\' + i):
                analiz_files(path_file + '\\' + i, level=level+1)
            else:
                rez.append(i)
    return rez


# Створюємо папку для відсортованих файлів
def create_folder(path_folder, name_folder):
    new_folder = Path(path_folder) / name_folder
    if not Path.exists(new_folder):
        Path.mkdir(new_folder)
        list_ignore.add(new_folder)
        #print(list_ignore)

# Складаємо список знайдених суфіксів


def create_list_suffix():
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

# Виводимо повідомлення про знайдене та створюємо папки


def report_create_folder():
    if len(suffix_img) > 0:
        print('__________________________________________________________')
        print('__________________________________________________________')
        print('Результат фото (знайдені розширення та відповідні файли):')
        print('Розширення фото:')
        for d in suffix_img:
            print(d)
        print('__________________________________________________________')
        print('Файли фото:')
        count_foto = 0
        for g in rez_img:
            rez_img[count_foto] = normalize('NFC', g)
            print(g)
            count_foto = count_foto + 1
        create_folder(sys.argv[1], 'image_sorted')
    else:
        print('__________________________________________________________')
        print('Файлів типу "Зображення" не знайдено.')
        print('__________________________________________________________')
        
    if len(suffix_archive) > 0:
        print('__________________________________________________________')
        print('__________________________________________________________')
        print('Результат архіви (знайдені розширення та відповідні файли):')
        print('Розширення архівів:')
        for h in suffix_archive:
            print(h)
        print('__________________________________________________________')
        print('Файли архівів:')
        count_archive = 0
        for k in rez_archive:
            rez_archive[count_archive] = normalize('NFC', k)
            print(k)
            count_archive = count_archive + 1
        create_folder(sys.argv[1], 'archive_sorted')
    else:
        print('__________________________________________________________')
        print('Файлів типу "Архів" не знайдено.')
        print('__________________________________________________________')
        
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
        count_video = 0
        for z in rez_video:
            rez_video[count_video] = normalize('NFC', z)
            print(z)
            count_video = count_video + 1
        create_folder(sys.argv[1], 'video_sorted')
    else:
        print('__________________________________________________________')
        print('Файлів типу "Відео" не знайдено.')
        print('__________________________________________________________')

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
        count_music = 0
        for c in rez_music:
            rez_music[count_music] = normalize('NFC', c)
            print(c)
            count_music = count_music + 1
        create_folder(sys.argv[1], 'music_sorted')
    else:
        print('__________________________________________________________')
        print('Файлів типу "Музика" не знайдено.')
        print('__________________________________________________________')

    if len(suffix_document) > 0:
        print('__________________________________________________________')
        print('Результат документи (знайдені розширення та відповідні файли):')
        print('__________________________________________________________')
        print('Розширення документи')
        for v in suffix_document:
            print(v)
        print('__________________________________________________________')
        print('Файли документів:')
        count_documents = 0
        for b in rez_documents:
            rez_documents[count_documents] = normalize('NFC', b)
            print(b)
            count_documents = count_documents + 1
        create_folder(sys.argv[1], 'documents_sorted')
    else:
        print('__________________________________________________________')
        print('Файлів типу "Текстовий документ" не знайдено.')
        print('__________________________________________________________')
        
    if len(suffix_other) > 0:
        print('__________________________________________________________')
        print('Результат інші файли (знайдені розширення та відповідні файли):')
        print('__________________________________________________________')
        print('Розширення інше:')
        for n in suffix_other:
            print(n)
        print('__________________________________________________________')
        print('Файли інше:')
        count_other = 0
        for m in rez_other:
            rez_other[count_other] = normalize('NFC', m)
            print(m)
            count_other = count_other + 1
        create_folder(sys.argv[1], 'other_sorted')
    else:
        print('__________________________________________________________')
        print('Файлів невідомого типу не знайдено.')
        print('__________________________________________________________')


# Головна процедура для проведення розбору файлів


def __main__():
    try:
        dyrectory_current = sys.argv[1]
        analiz_files(dyrectory_current)
        create_list_suffix()
        report_create_folder()   
        #print(list_ignore, 'Результат ігнор')     

    except:
        print('Введіть шлях до папки')


__main__()
