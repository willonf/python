"""
os -> Operating System

.getcwd() -> pega o diretório atual
.chdir() -> muda de diretório
.path.isabs() -> Verifica se é um caminho absoluto
.name -> sistema operacional
uname() -> mais detalhes sobre o SO
sys.platform -> SO
.path.join() -> Unindo caminhos
.listdir() -> listar o diretório
.os.scandir() -> listar o diretório com mais detalhes (Necessário fechar depois de aberto. Usar com with)
"""

import os

print(os.getcwd())
os.chdir('..')  # Voltar 1 nível
print(os.getcwd())
os.chdir('..')  # Voltar 1 nível
print(os.getcwd())

print(25 * '+=')
# Em windows:
print(os.path.isabs('D:\\Cliente'))

# Em linux:
print(os.path.isabs('/home/willonf'))
print(25 * '+=')

print(os.name)
# No linux
# print(os.uname())

# No windows:
import sys

print(sys.platform)

print(25 * '+=')
print(os.getcwd())  # D:\Cliente\Diversos\python-Udemy
# new_path = os.path.join(os.getcwd(), os.path.join('Python', 'seção13 - arquivos')) ou:
new_path = os.path.join(os.getcwd(), 'Python', 'seção13 - arquivos')
os.chdir(new_path)
print(os.getcwd())

print(25 * '+=')
print(os.listdir())
print(os.listdir('D:\\Cliente\\Área de Trabalho'))

print(25 * '+=')
print(list(os.scandir()))
scan = os.scandir('D:\\Cliente\\Área de Trabalho')
desktop_files = list(scan)
print(desktop_files[0].inode())
print(desktop_files[0].name)
print(desktop_files[0].is_dir())
print(desktop_files[0].is_file())
print(desktop_files[0].is_symlink())
print(desktop_files[0].path)
print(desktop_files[0].stat())
scan.close()
