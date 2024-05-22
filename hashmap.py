class HashMap():
    def __init__(self, size = 100) -> None:
        self.size = size
        self.bucket = [[] for _ in range(size)]

    def get_hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hashed_key = self.get_hash(key)
        bucket = self.bucket[hashed_key]
        for index, data in enumerate(bucket):
            data_key, data_value = data
            if (data_key == key):
                bucket[index] = (key, value)
                return
        bucket.append((key, value))
    
    def delete(self, key):
        hashed_key = self.get_hash(key)
        bucket = self.bucket[hashed_key]
        for index, data in enumerate(bucket):
            data_key, data_value = data
            if (data_key == key):
                del bucket[index]
                return
        
    def get_value(self, key):
        hashed_key = self.get_hash(key)
        bucket = self.bucket[hashed_key]
        for data_key, data_value in bucket:
            if (data_key == key):
                return data_value
        print("not found")

    def __str__(self):
        items = []
        for i, bucket in enumerate(self.bucket):
            if bucket:
                items.append(f"Bucket {i}: {bucket}")
        return "\n".join(items)
