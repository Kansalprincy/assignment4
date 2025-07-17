def read_file(sample):
    try:
        with  open("sample.txt" ,'r') as f:
            reading_file= f.read()
            print(reading_file)
    except FileNotFoundError:
        print("The file 'sample.txt' does not exist")


read_file("sample.txt")