import os

DIRS = {'assets': ['db', 'images', 'sounds', 'videos'],
        'src': ['html', 'json', 'pages', 'sidebar', 'tmp', 'utils', 'yaml']
        }

def create_dir_structure(top_dir, name, dir_list=DIRS):
    if os.path.lexists(os.path.join(top_dir, name)) == False:
        os.mkdir(top_dir)
        os.mkdir(os.path.join(top_dir, name))

    for i in range(len(dir_list)):
        path = os.path.join(top_dir, name, list(DIRS)[i])
        if os.path.lexists(path) == False:
            os.mkdir(path)
    
    for i in range(len(dir_list)):
        sub_path = list(dir_list.keys())[i]
        dirs = dir_list[sub_path]
        for k in dirs:
            p = os.path.join(top_dir, name, sub_path, k)
            if os.path.lexists(p) == False:
                os.mkdir(p)

    return True
