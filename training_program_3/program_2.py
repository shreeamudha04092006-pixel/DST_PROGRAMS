def stream_batches(data, batch_size):
    batch = []

    for item in data:
        batch.append(item)

        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch


data = [1, 2, 3, 4, 5, 6, 7, 8]
batch_size = 3

gen = stream_batches(data, batch_size)

print(list(gen))