"""
Sistema de arquivos - Manipulação
.path.exists() -> dado um path, verifica se este existe
open() -> criação de arquivos (Obs.: mode=w)
os.mknod() -> criar novo arquivo
.mkdir() -> criar novo diretório
.rename() -> Renomear arquivos e diretórios
.remove() -> remover arquivos

Obs.: essa remoção não manda os arquivos para a lixeira.
Par mandar para a lixeira, usar pacote sendToTrash
"""
import os
import tempfile

#
# print(os.path.exists('arquivo.txt'))
# print(os.path.exists('text'))
# print(os.path.exists('../../Python'))
# print(25 * '+=')
#
# open('novo_arquivo.txt', 'w').close()
#
# with open('novo_arquivo2.txt', 'w') as file:
#     pass
# print(25 * '+=')
#
# os.mknod('novo_arquivo3.txt')
# os.mknod('novo_arquivo4.txt')
# print(25 * '+=')
#
# os.mkdir('template')
# os.mkdir('template2')
# os.mkdirs('.\\template2\\geek\\direct', exist_ok=True) Criação de diretórios em cadeia
print(25 * '+=')

# os.rename('novo_arquivo.txt', 'new_file.txt')
# os.rename('template', 'new_template')
print(25 * '+=')

# os.remove('text2')
print(25 * '+=')

# os.rmdir('template2')
# os.remidrs('geek2/directory) Remover árvore de diretórios
print(25 * '+=')

# Remoção de arquivos de diretório
# for file in os.scandir('new_template'):
#     if file.is_file():
#         os.remove(file.path)


# Trabalhando com arquivos e diretórios temporários

# with tempfile.TemporaryDirectory() as tmp:
#     print(f'Criei o diretório temporário em {tmp}')
#     with open(os.path.join(tmp, 'arquivo_temp.xt'), 'w') as file:
#         file.write('Will')
#     input()

# with tempfile.TemporaryFile() as tmp:
#     # Em um arquivo temporário só é possível escrever binário
#     tmp.write(b'Geek university\n')  # Convertendo para binário
#     tmp.seek(0)
#     print(tmp.read())

# arquivo = tempfile.TemporaryFile()
# arquivo.write(b'Geek university\n')
# arquivo.seek(0)
# print(arquivo.read())
# arquivo.close()

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek university\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
