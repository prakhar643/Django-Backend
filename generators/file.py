# def create_large_file(file_path, num_lines=1000000):
#     with open(file_path, 'w') as f:
#         for i in range(num_lines):
#             f.write(f"This is line number {i}\n")

# create_large_file("large.txt", 1000000)  # 1 million lines

from itertools import islice

def read_large_file(file_path):
    try:
          with open(file_path,'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
         print("File not found")



def batch_generator(iterable,batch_size):
    batch = []
    for item in iterable:
        batch.append(item)
        
        if len(batch) == batch_size:
          yield batch
          batch = []
    if batch:
        yield batch
    


for batch in batch_generator(read_large_file("large.txt"), 100):
    print(f"Processing batch of size {len(batch)}")
    # process batch here
        
# for i ,line in enumerate(read_large_file("large.txt")):
#         if i == 10:
#             break
#         print(line)

# for line in islice(read_large_file("large.txt"), 10):
#     print(line)