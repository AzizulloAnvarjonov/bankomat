import threading

def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        print(f"Reading from {file_name}: {data}")

def main():
    file_names = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]

    threads = []
    for file_name in file_names:
        thread = threading.Thread(target=read_file, args=(file_name,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()




import multiprocessing

def write_to_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)
        print(f"Writing to {file_name}: {data}")

def main():
    file_names = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]
    data_to_write = "Hello, multiprocessing!"

    processes = []
    for file_name in file_names:
        process = multiprocessing.Process(target=write_to_file, args=(file_name, data_to_write))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()