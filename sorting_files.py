from pathlib import *
import shutil , sys, rarfile, os

# Списки розширень для сортування
list_img = ['.JPEG', '.jpeg', '.PNG', '.png', '.JPG', '.jpg', '.SVG', '.svg']
list_archive = ['.rar', '.RAR', '.zip', '.ZIP', '.gz', '.GZ', '.tar', '.TAR']
list_video = ['.AVI', '.avi', '.MP4', '.mp4', '.MOV', '.mov', '.MKV', '.mkv']
list_documents = ['.DOC', '.doc', '.DOCX', '.docs', '.TXT','.txt', '.PDF', '.pdf', '.XLSX', '.xlsx', '.PPTX', '.pptx']
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
            elif Path(j).suffix in list_archive:
                rez_archive.append(j)
            elif Path(j).suffix in list_video:
                rez_video.append(j)
            elif Path(j).suffix in list_music:
                rez_music.append(j)
            elif Path(j).suffix in list_documents:
                rez_documents.append(j)
            else:
                rez_other.append(j)        

        print('Результат фото  ', rez_img)
        print('Результат архіви  ', rez_archive)
        print('Результат відео  ', rez_video)
        print('Результат музика  ', rez_music)
        print('Результат документи  ', rez_documents)
        print('Результат інші файли  ' , rez_other)
          
    except:
        print('Введіть шлях до папки')

__sorting_files__()


#Створюємо папку для відсортованих файлів
new_folder = Path.cwd() /'Нова папка'
if not Path.exists(new_folder):
    Path.mkdir(new_folder)