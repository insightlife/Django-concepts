def write_file(variable):
    var=variable
    file=open('../../new.txt', 'w')
    files=file.write(var)
    file.close()
write_file('sumann')
print(__name__)