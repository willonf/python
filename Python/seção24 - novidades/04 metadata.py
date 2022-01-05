from importlib import metadata

# print(metadata.version('pip'))

metadados_pip = metadata.metadata('pip')
# print(metadados_pip)
print(list(metadados_pip))
print(metadados_pip['Author'])
print(len(metadata.files('pip')))
print(metadata.requires('pip'))
print(metadata.requires('ipython'))

print(globals())
