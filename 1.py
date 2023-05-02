path = 'C:\Thecode\Media\статья.txt'


def file_path(k: str):
    a, b = k.split('.')
    *a, c = a.split('\\')
    a = '\\'.join(a)
    return (a, c, b)


print(file_path(path))
