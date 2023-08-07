import os
import shutil

def normalize(text):
    translit_table = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i',
        'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu', 'я': 'ia'
    }

    result = []
    for char in text:
        if char.isalnum():
            result.append(char)
        elif char.lower() in translit_table:
            result.append(translit_table[char.lower()])
        else:
            result.append('_')

    return ''.join(result)

def process_folder(folder_path):
    images_ext = ('.jpeg', '.png', '.jpg', '.svg')
    videos_ext = ('.avi', '.mp4', '.mov', '.mkv')
    documents_ext = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
    music_ext = ('.mp3', '.ogg', '.wav', '.amr')
    archives_ext = ('.zip', '.gz', '.tar')
    
    extensions = {}
    
    folders = {
        'images': 'images',
        'videos': 'videos',
        'documents': 'documents',
        'music': 'music',
        'archives': 'archives',
    }
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        
        if os.path.isdir(item_path):
            if item not in folders.values():
                process_folder(item_path)
        else:
            base_name, ext = os.path.splitext(item)
            new_name = normalize(base_name) + ext
            new_path = os.path.join(folder_path, new_name)
            
            os.rename(item_path, new_path)
            
            if ext not in extensions:
                extensions[ext] = []
            extensions[ext].append(new_name)
            
            if ext.lower() in images_ext:
                shutil.move(new_path, os.path.join(folder_path, folders['images'], new_name))
            elif ext.lower() in videos_ext:
                shutil.move(new_path, os.path.join(folder_path, folders['videos'], new_name))
            elif ext.lower() in documents_ext:
                shutil.move(new_path, os.path.join(folder_path, folders['documents'], new_name))
            elif ext.lower() in music_ext:
                shutil.move(new_path, os.path.join(folder_path, folders['music'], new_name))
            elif ext.lower() in archives_ext:
                archive_folder = os.path.join(folder_path, folders['archives'], os.path.splitext(new_name)[0])
                os.makedirs(archive_folder, exist_ok=True)
                shutil.unpack_archive(new_path, archive_folder)
                os.remove(new_path)
    
    # Виведемо результат
    print("Sorted files:")
    for folder, files in folders.items():
        if folder != 'archives':
            folder_path = os.path.join(folder_path, files)
            if os.path.exists(folder_path):
                sorted_files = os.listdir(folder_path)
                if sorted_files:
                    print(f"{folder}: {sorted_files}")
                else:
                    print(f"{folder}: No files")
    
    print("\nKnown extensions:")
    for ext, files in extensions.items():
        print(f"{ext}: {files}")
    
    unknown_ext = set(os.path.splitext(f)[1].lower() for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)))
    unknown_ext -= set(extensions.keys())
    print("\nUnknown extensions:")
    print(list(unknown_ext))

# Приклад використання:
folder_to_sort = './path_to_folder'
process_folder(folder_to_sort)