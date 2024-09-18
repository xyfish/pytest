import redis,json

'''
https://redis.io/commands
https://github.com/redis/redis-py
'''
# 連接到本地 Redis 資料庫
r = redis.Redis(host='localhost', port=6379, db=0)

# 測試值，設定並獲取
testval = {"a":1,"b":2,"c":3}
r.set('testval', json.dumps(testval))  # 將字典轉換為 JSON 並儲存
rs = r.get("testval")  # 獲取儲存的值
print(rs)  # 打印獲取的值

exit()  # 退出程式

import os,sys,time,asyncio
import configparser
import redis,json

# 讀取配置檔
config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + "/inc.config.conf")  # 讀取配置檔路徑

# 從配置中獲取股票觀察列表
watchlist = config['STOCK']['WatchList'].split(',')

# 連接到遠端 Redis 資料庫
r = redis.Redis(host='redishost', port=6379, db=0)

# 遍歷觀察列表中的每個股票符號
for symbol in watchlist:
    current_index = "index_" + symbol  # 創建當前索引的鍵名
    # 獲取當前值，如果不存在則默認為 1
    current_val = 1 if r.get(current_index) is None else int(r.get(current_index).decode())
    
    # 遍歷當前值的範圍
    for i in range(1, current_val):
        src = symbol + "_" + str(i)  # 源鍵名
        dst = "symbol_" + src  # 目標鍵名
        if r.exists(src):  # 檢查源鍵是否存在
            r.rename(src, dst)  # 重命名鍵
        else:
            print(src, ' is not existing')  # 如果源鍵不存在，打印提示

        print('Rename: ', src, ' <--> ', dst)  # 打印重命名操作

print("All done!")  # 完成所有操作的提示

# 設定一個簡單的鍵值對
r.set('example_key', 'example_value')  # 設定鍵 'example_key' 的值為 'example_value'
print(r.get('example_key'))  # 獲取並打印 'example_key' 的值

# 刪除鍵
r.delete('example_key')  # 刪除 'example_key'
print(r.get('example_key'))  # 確認 'example_key' 是否已被刪除，應返回 None

# 使用列表
r.lpush('my_list', 'item1')  # 將 'item1' 添加到列表 'my_list' 的左側
r.lpush('my_list', 'item2')  # 將 'item2' 添加到列表 'my_list' 的左側
print(r.lrange('my_list', 0, -1))  # 獲取並打印 'my_list' 中的所有項目

# 使用集合
r.sadd('my_set', 'member1')  # 向集合 'my_set' 添加 'member1'
r.sadd('my_set', 'member2')  # 向集合 'my_set' 添加 'member2'
print(r.smembers('my_set'))  # 獲取並打印 'my_set' 中的所有成員

# 使用哈希
r.hset('my_hash', 'field1', 'value1')  # 在哈希 'my_hash' 中設定 'field1' 的值為 'value1'
print(r.hget('my_hash', 'field1'))  # 獲取並打印 'my_hash' 中 'field1' 的值
