# Error and Exception
try:
    f = open('simple.txt', 'w')
    f.write('Test write to file')
except IOError:
    print("Error writing to file")
finally:
    print("I always work")
# else:
#     print("Success writing to file")
#     f.close()
    
