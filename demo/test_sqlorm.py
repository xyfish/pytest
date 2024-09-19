from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

# 資料庫連線資訊
# uri = 'mysql+mysqlconnector://root:******@localhost/mini_main'  # 資料庫URI
uri = 'mysql+mysqlconnector://ewaytech:ewaytech2020@localhost/pmc_main'  # 資料庫URI
db = create_engine(uri, echo=False)  # 建立資料庫引擎，echo=False表示不輸出SQL語句
conn = sessionmaker(db)()  # 建立會話，用於與資料庫互動

# 建立資料結構
Base = automap_base()  # 建立自動映射基礎類
Base.prepare(db, reflect=True)  # 反射資料庫，獲取表結構並映射到類
Base.classes.keys()  # 獲取所有的物件名稱，方便後續使用

# 獲取表物件
# ads = Base.classes.ads  # 獲取ads表物件
admin = Base.classes.admin  # 獲取admin表物件
document = Base.classes.document  # 獲取document表物件

# 執行查詢
result = conn.query(document).filter(document.id > 0, document.id < 999).limit(1).all()  # 查詢id在1到999之間的document

print(len(result))  # 輸出查詢結果的數量
for row in result:  # 遍歷查詢結果
    print("############################################################")
    for k, v in row.__dict__.items():  # 遍歷每一行的字典屬性
        print(k)  # 輸出屬性名稱
        print("================")
        print(v)  # 輸出屬性值
        print("\n")

# 在ipython中建立兩個映射類的範例
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, backref

# 建立資料庫引擎
# engine = create_engine('mysql://root@localhost/test?charset=utf8')  # 連接到MySQL資料庫
engine = create_engine('mysql+mysqlconnector://ewaytech:ewaytech2020@localhost/test?charset=utf8mb4')  # 連接到MySQL資料庫
Base = declarative_base()  # 建立聲明基礎類
session = sessionmaker(engine)()  # 建立會話

# 定義User類，映射到user表
class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)  # 主鍵
    name = Column(String(64), unique=True, index=True)  # 使用者名稱，唯一且有索引

    def __repr__(self):
        return '<User: {}>'.format(self.name)  # 返回使用者的字串表示

# 定義Course類，映射到course表
class Course(Base):
    __tablename__ = 'course'  # 表名
    id = Column(Integer, primary_key=True)  # 主鍵
    name = Column(String(64), unique=True, nullable=False)  # 課程名稱，唯一且不能為空
    user_id = Column(Integer, ForeignKey('user.id'))  # 外鍵，關聯User表
    user = relationship('User', backref='course')  # 定義與User的關係

    def __repr__(self):
        return '<Course: {}>'.format(self.name)  # 返回課程的字串表示

# 建立資料庫表，添加測試資料
Base.metadata.create_all(bind=engine)  # 建立所有表
u1 = User(name='Kobe')  # 建立使用者Kobe
u2 = User(name='Nash')  # 建立使用者Nash
u3 = User(name='James')  # 建立使用者James
c1 = Course(name='Mysql 基礎', user=u1)  # 建立課程，關聯使用者Kobe
c2 = Course(name='Flask-SQLAlchemy 快速入門', user=u1)  # 建立課程，關聯使用者Kobe

# 批量添加使用者和課程到會話
for i in (u1, u2, u3, c1, c2):
    session.add(i)  # 添加到會話
session.commit()  # 提交會話，保存到資料庫

# 查詢範例
# 查詢全部使用者，相當於 SQL 查詢語句：select * from user;
all_users = session.query(User).all()  # 查詢所有使用者
print(all_users)  # 輸出所有使用者

# 查詢第一個使用者
first_user = session.query(User).first()  # 查詢第一個使用者
print(first_user)  # 輸出第一個使用者

# 條件查詢，查找名字為'James'的使用者
james_user = session.query(User).filter(User.name == 'James').first()  # 查詢名字為James的使用者
print(james_user)  # 輸出使用者James

# 使用!=進行反查詢，查找名字不是'Kobe'的使用者
not_kobe_users = session.query(User).filter(User.name != 'Kobe').all()  # 查詢名字不是Kobe的使用者
print(not_kobe_users)  # 輸出結果

# 多條件查詢，查找名字為'Kobe'且id為1的使用者
multi_condition_users = session.query(User).filter_by(name='Kobe', id=1).all()  # 查詢名字為Kobe且id為1的使用者
print(multi_condition_users)  # 輸出結果

# 查詢User表中全部資料的name值
user_names = session.query(User.name).all()  # 查詢所有使用者的名字
print(user_names)  # 輸出所有名字

# 使用like進行模糊查詢，查找名字中包含'e'的使用者
like_query_users = session.query(User).filter(User.name.like('%e%')).all()  # 查詢名字中包含'e'的使用者
print(like_query_users)  # 輸出結果

# 使用in_查詢，查找名字在指定列表中的使用者
in_query_users = session.query(User).filter(User.name.in_(['Kobe', 'James'])).all()  # 查詢名字在Kobe和James中的使用者
print(in_query_users)  # 輸出結果

# 使用and_進行多條件查詢
from sqlalchemy import and_
and_query_users = session.query(User).filter(and_(User.name == 'Kobe', User.id == 1)).all()  # 查詢名字為Kobe且id為1的使用者
print(and_query_users)  # 輸出結果

# 使用or_進行條件查詢
from sqlalchemy import or_
or_query_users = session.query(User).filter(or_(User.name == 'Kobe', User.id == 2)).all()  # 查詢名字為Kobe或id為2的使用者
print(or_query_users)  # 輸出結果

# 使用join進行連表查詢，查找名字為'Kobe'的使用者對應的所有課程
joined_courses = session.query(Course).join(User).filter(User.name == 'Kobe').all()  # 查詢Kobe的所有課程
print(joined_courses)  # 輸出結果

# 使用order_by進行排序，查詢所有使用者並按名字排序
sorted_users = session.query(User).order_by(User.name).all()  # 按名字排序查詢所有使用者
print(sorted_users)  # 輸出結果

# 使用limit限制查詢數量，查詢前兩個使用者
limited_users = session.query(User).order_by(User.name.desc()).limit(2).all()  # 降序排序並限制為兩個使用者
print(limited_users)  # 輸出結果

# 使用count統計使用者數量
user_count = session.query(User).order_by(User.name.desc()).count()  # 統計使用者數量
print(user_count)  # 輸出使用者數量

# 使用ORM進行批量插入
import db.sp_info as sp
data = []

# 方法 1：使用字典批量插入
for x in range(1, 15):
    data.append({'symbol': 'F', 'timestamp': time.time(), 'price': x})  # 添加資料到列表

sp.conn.bulk_insert_mappings(sp.Market, data)  # 批量插入資料
sp.conn.commit()  # 提交會話

# 方法 2：使用物件批量插入
for x in range(1, 15):
    data.append(sp.Market({'symbol': 'F', 'timestamp': time.time(), 'price': x}))  # 建立Market物件並添加到列表

sp.conn.bulk_save_objects(data)  # 批量保存物件
sp.conn.commit()  # 提交會話

# 使用ORM進行批量刪除
delete_q = Report.__table__.delete().where(Report.data == 'test')  # 建立刪除查詢
db.session.execute(delete_q)  # 執行刪除查詢
db.session.commit()  # 提交會話

# 使用ORM插入記錄
from yourapp import User
me = User('admin', 'admin@example.com')  # 建立使用者物件
session.add(me)  # 添加到會話
session.commit()  # 提交會話

# 使用ORM進行記錄更改
rs = session.query(User).filter(User.name == 'James').first()  # 查詢使用者James
rs.username = 'some_thing_else'  # 修改使用者名稱
session.commit()  # 提交會話

# 使用ORM進行刪除記錄
session.delete(me)  # 刪除使用者
session.commit()  # 提交會話

# 使用execute時的處理方法
# 正確的做法
name = "peter"
age = 20
session.execute("INSERT INTO users (name, age) VALUES (:name, :age)", {"name": name, "age": age})  # 使用參數化查詢
session.commit()  # 提交會話

# 錯誤的做法
name = "peter'; DROP TABLE users; --"  # 潛在的SQL注入
age = 20
session.execute("INSERT INTO users (name, age) VALUES ('" + name + "', " + str(age) + ")")  # 不安全的拼接查詢
session.commit()  # 提交會話
