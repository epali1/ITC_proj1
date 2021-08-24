import mysql.connector
class DBStorePipeline(object):
    def_init_(self)
    self.create_connection()
    self.create_table()
    def create_connection(self):
        self.conn=mysql.connector.connect(
  host='localhost',
  user='root',
  password='yourpassword',
  port = 3306, #for Mamp users
  database='smartphone-scraper'
)
        self.curr=self.conn.cursor()
        def create_table(self):
            self.curr.execute(""""DROP TABLE IF EXISTS launch""")
            self.curr.execute(""""create table launch(
              Announced text,
            Status text,
    )""")
            def process_item(self,item,spider):
                self.store_db(item)
                return item
            def store_db(self, item):
                 self.curr.execute(""""insert into launch values (%,%)""",(
                                   item['Announced'][0],
                                   item['Status'][0]
                                   ))

                 def create_table(self):
                     self.curr.execute(""""DROP TABLE IF EXISTS Misc""")
                     self.curr.execute(""""create table Misc(
                           Colors text,
                         Model text,
                         SAR text,
                         SAR_EU text,
                         Price text
                 )""")

                     def process_item(self, item, spider):
                         self.store_db(item)
                         return item

                     def store_db(self, item):
                         self.curr.execute(""""insert into Misc values (%,%,%,%,%)""", (
                             item['Colors'][0],
                             item['Model'][0],
                             item['SAR'][0],
                             item['SAR_EU'][0],
                             item['Price'][0]
                         ))

                         def create_table(self):
                             self.curr.execute(""""DROP TABLE IF EXISTS Battary""")
                             self.curr.execute(""""create table Battary(
                                     Type text,
                                   Charging text,
                           )""")

                             def process_item(self, item, spider):
                                 self.store_db(item)
                                 return item

                             def store_db(self, item):
                                 self.curr.execute(""""insert into Battary values (%,%)""", (
                                     item['Type'][0],
                                     item['Charging '][0]

                                 ))

                 def create_table(self):
                     self.curr.execute(""""DROP TABLE IF EXISTS Feature""")
                     self.curr.execute(""""create table Feature(
                                                    Sensor text,
                                                  Other text,
                                          )""")

                     def process_item(self, item, spider):
                         self.store_db(item)
                         return item

                     def store_db(self, item):
                         self.curr.execute(""""insert into Feature values (%,%)""", (
                             item['Sensor'][0],
                             item['Other '][0]

                         ))

                         def create_table(self):
                             self.curr.execute(""""DROP TABLE IF EXISTS Comms""")
                             self.curr.execute(""""create table  Comms(
                                                          WLAN   text,
                                                           Bluetooth text,
                                                           GPS text,
                                                           NFC text,
                                                           Radio text,
                                                           USB text, 
                                                  )""")

                             def process_item(self, item, spider):
                                 self.store_db(item)
                                 return item

                             def store_db(self, item):
                                 self.curr.execute(""""insert into  Comms values (%,%,%,%,%,%)""", (
                                     item['WLAN'][0],
                                     item['Bluetooth '][0],
                                     item['GPS'][0],
                                     item[' NFC'][0],
                                     item['Radio'][0],
                                     item[' USB'][0]
                                 ))

                 def create_table(self):
                     self.curr.execute(""""DROP TABLE IF EXISTS Sound""")
                     self.curr.execute(""""create table Sound(
                                                                Loudspeaker text,
                                                             3.5mm_jack text,
                                                     )""")

                     def process_item(self, item, spider):
                         self.store_db(item)
                         return item

                     def store_db(self, item):
                         self.curr.execute(""""insert into Sound values (%,%)""", (
                             item['Loudspeaker'][0],
                             item['3.5mm_jack  '][0]

                         ))

                         def create_table(self):
                             self.curr.execute(""""DROP TABLE IF EXISTS Selfie_Camera""")
                             self.curr.execute(""""create table Selfie_Camera(
                                                          Single text,
                                         Features text,
                                         Video text
                                                             )""")

                             def process_item(self, item, spider):
                                 self.store_db(item)
                                 return item

                             def store_db(self, item):
                                 self.curr.execute(""""insert into Selfie_Camera values (%,%,%)""", (
                                    item['Single'][0],
                                     item['Features'][0],
                                     item['Video'][0]

                                 ))

                                 def create_table(self):
                                     self.curr.execute(""""DROP TABLE IF EXISTS Main_Camera""")
                                     self.curr.execute(""""create table Main_Camera(
                                                           Quad text,
                                                                        Features text,
                                                                        Video text
                                                                                            )""")

                                     def process_item(self, item, spider):
                                         self.store_db(item)
                                         return item

                                     def store_db(self, item):
                                         self.curr.execute(""""insert into Main_Camera values (%,%,%)""", (
                                             item['Quad'][0],
                                             item['Features'][0],
                                             item['Video'][0]

                                         ))

                 def create_table(self):
                     self.curr.execute(""""DROP TABLE IF EXISTS Memory""")
                     self.curr.execute(""""create table Memory(
                                                                        Card_slot text,
                                                                                      Internal text,
                                                                                      Other text
                                                                                                          )""")

                     def process_item(self, item, spider):
                         self.store_db(item)
                         return item

                     def store_db(self, item):
                         self.curr.execute(""""insert into Memory values (%,%,%)""", (
                             item['Card_slot '][0],
                             item['Internal'][0],
                             item['Other'][0]

                         ))


                 def create_table(self):
                     self.curr.execute(""""DROP TABLE IF EXISTS Platform""")
                     self.curr.execute(""""create table Platform(
                                                                        OS text,
                                                                  Chipset text,
                                                             CPU text,
                                                             GPU text
                                                                                                          )""")

                     def process_item(self, item, spider):
                         self.store_db(item)
                         return item

                     def store_db(self, item):
                         self.curr.execute(""""insert into Platform values (%,%,%,%)""", (
                             item['OS'][0],
                             item['Chipset'][0],
                             item['CPU'][0],
                             item['GPU'][0]

                         ))

                         def create_table(self):
                             self.curr.execute(""""DROP TABLE IF EXISTS Dispaly""")
                             self.curr.execute(""""create table Dispaly(
                                 Type text,
                             Size text,
                           Resolution text
                                                                                                                                  )""")

                             def process_item(self, item, spider):
                                 self.store_db(item)
                                 return item

                             def store_db(self, item):
                                 self.curr.execute(""""insert into Dispaly values (%,%,%)""", (
                                     item['Type '][0],
                                     item['Size'][0],
                                     item['Resolution'][0]

                                 ))

                                 def create_table(self):
                                     self.curr.execute(""""DROP TABLE IF EXISTS Boday""")
                                     self.curr.execute(""""create table Boday(
                                                                                                Dimensions text,
                                                                                                 Weight text,
                                                                                            Build text,
                                                                                            SIM text
                                                                                                                                         )""")

                                     def process_item(self, item, spider):
                                         self.store_db(item)
                                         return item

                                     def store_db(self, item):
                                         self.curr.execute(""""insert into Boday values (%,%,%,%)""", (
                                             item['Dimensions'][0],
                                             item['Weight'][0],
                                             item['Build'][0],
                                             item['SIM'][0]

                                         ))

                                         def create_table(self):
                                             self.curr.execute(""""DROP TABLE IF EXISTS Network""")
                                             self.curr.execute(""""create table Network(
                                                        Technology text,
                                                         2G_band text,
                                                         3G_band text,
                                                         4G_band text,
                                                      Speed text,
                                                                GPRS text,
                                                                EDGE text
                                                                                           )""")

                                             def process_item(self, item, spider):
                                                 self.store_db(item)
                                                 return item

                                             def store_db(self, item):
                                                 self.curr.execute(""""insert into Network values (%,%,%,%,%,%,%)""", (
                                                     item['Technology'][0],
                                                     item['2G_band text'][0],
                                                     item['3G_band text'][0],
                                                     item['4G_band text'][0],
                                                     item['Speed'][0],
                                                     item['GPRS'][0],
                                                     item['EDGE'][0]
                                                 ))
                 self.conn.commit()