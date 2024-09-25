import sqlite3

class DB:
    def _init_(self):
        self.con = sqlite3.connect("database db")
        self.cur = self.con.cursor()

    def create_table(self):
        sql = """create table if not exists game
            (point integer);"""
        self.cur.execute(sql)
        self.con.commit()
        
    def write_point(self,point):
        sql = f"""insert into game (point)
            values ({point});"""
            
    def get_points(self):
        sql = """select distinct point from game order by point desc limit 3"""
        return self.cur.execute(sql).fetchall()


db = DB()
db.create_table()