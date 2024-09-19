from pymemcache.client.base import Client
import json  # 添加缺失的導入

# pip install --user pymemcache
# https://pymemcache.readthedocs.io/en/latest/apidoc/pymemcache.client.base.html
# https://pymemcache.readthedocs.io/en/latest/getting_started.html#basic-usage

class JsonSerde(object):
    def serialize(self, key, value):
        if isinstance(value, str):
            return value.encode('utf-8'), 1
        return json.dumps(value).encode('utf-8'), 2

    def deserialize(self, key, value, flags):
        if flags == 1:
            return value.decode('utf-8')
        if flags == 2:
            return json.loads(value.decode('utf-8'))
        raise Exception("未知的序列化格式")

client = Client('localhost', serde=JsonSerde())

# 設定鍵值對
client.set('key', {'a': 'b', 'c': 'd'})  # 儲存字典
client.set('string_key', 'Hello, World!')  # 儲存字串

# 獲取鍵值對
result = client.get('key')  # 獲取字典
string_result = client.get('string_key')  # 獲取字串

# 打印結果類型
print(type(result))  # 應該是 <class 'dict'>
print(type(string_result))  # 應該是 <class 'str'>

# 刪除鍵值對
client.delete('key')  # 刪除字典
deleted_result = client.get('key')  # 嘗試獲取已刪除的字典
print(deleted_result)  # 應該是 None

# 檢查鍵是否存在
exists = client.get('string_key') is not None  # 檢查字串鍵是否存在
print(f"字串鍵存在: {exists}")  # 打印存在性檢查結果