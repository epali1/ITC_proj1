import json
import pymysql as mysql

# file = open("apple_smartphones_data.json")
DB_SCRIPT = 'Smartphone-Scraper2.sql'
DB_USER = 'root'
DB_PASS = '12345COM'
TABLES_LIST = ('Network', 'Body', 'Display', 'Selfie camera', 'Main Camera', 'Misc', 'Comms', 'Platform',
               'Launch', 'Features', 'Sound', 'Battery', 'Memory')


def run_query(x, y):
    """
    run single query
    """
    conn = mysql.connect(host="localhost", user=DB_USER, passwd=DB_PASS, db="smartphone_scraper", autocommit=True)
    with conn.cursor() as cur:
        cur.execute(x, y)
        conn.commit()


def del_db():
    if check_if_db_exist():
        query = "DROP DATABASE smartphone_scraper;"
        run_query(query, None)


def new_db():
    del_db()
    conn = mysql.connect(host="localhost", user=DB_USER, passwd=DB_PASS, autocommit=True)
    with conn.cursor() as cur:
        query = "CREATE DATABASE smartphone_scraper;"
        cur.execute(query)
    with conn.cursor() as cur:
        query = "USE smartphone_scraper;"
        cur.execute(query)
        with open(DB_SCRIPT, 'r') as sql_file:
            # for line in sql_file.readlines():
            #     print(line)
            for line in sql_file.read().replace('\n', "").split(';'):
                if not line == "":
                    cur.execute(line + ';')


def check_if_db_exist():
    query = "SHOW DATABASES;"
    conn = mysql.connect(host="localhost", user=DB_USER, passwd=DB_PASS, autocommit=True)
    cur = conn.cursor()
    cur.execute(query)
    res = [ele[0] for ele in cur.fetchall()]
    if 'smartphone_scraper' in res:
        return True
    else:
        return False


def to_database(data):
    file_data = data  # json.load(data)  # data
    # List
    mobile_models = []
    # Get Mobile Version Name ######
    for i in range(len(file_data)):
        a = file_data[i]
        model_name = list(a.keys())[0]
        mobile_models.append(model_name)

    # ##### Get Other Attributes and Saving on DB ######
    for i in range(0, len(file_data)):
        data_from_file = file_data[i]
        #=> Networks Table Data
        try:
            Network = data_from_file[mobile_models[i]]['Network']
            try   : Technology   = Network['Technology']
            except: Technology   = ""
            try   : twoG_Bands   = Network['2G bands']
            except: twoG_Bands   = ""
            try   : threeG_Bands = Network['3G bands']
            except: threeG_Bands = ""
            try   : fourG_Bands  = Network['4G bands']
            except: fourG_Bands  = ""
            try   : fiveG_Bands  = Network['5G bands']
            except: fiveG_Bands  = ""
            try   : Speed        = Network['Speed']
            except: Speed = ""
        except:
            Technology   = ""
            twoG_Bands = ""
            threeG_Bands = ""
            fourG_Bands = ""
            fiveG_Bands = ""
            Speed = ""

        #=> Body
        try:
            Body = data_from_file[mobile_models[i]]['Body']
            try   : Dimensions  = Body['Dimensions']
            except: Dimensions  = ""
            try   : Weight      = Body['Weight']
            except: Weight      = ""
            try   : Build       = Body['Build']
            except: Build       = ""
            try   : Sim         = Body['SIM']
            except: Sim         = ""
        except:
            Dimensions  = ""
            Weight = ""
            Build = ""
            Sim = ""

            #=> Display
        try:
            Display = data_from_file[mobile_models[i]]['Display']
            try    : Type  = Display['Type']
            except : Type  = ""
            try    : Size  = Display['Size']
            except : Size = ""
            try    : Resolution = Display['Resolution']
            except : Resolution = ""
        except:
            Type  = ""
            Size = ""
            Resolution = ""

        #=> Selfie Camera
        try:
            Selfie_Cam = data_from_file[mobile_models[i]]['Selfie camera']
            try    : Single_1  = Selfie_Cam['Single']
            except : Single_1= ""
            try    : Features_1 = Selfie_Cam['Features']
            except : Features_1 = ""
            try    : Video_1 = Selfie_Cam['Video']
            except : Video_1 = ""
        except:
            Single_1= ""
            Features_1 = ""
            Video_1 = ""

            #=> Main Camera
        try:
            Main_Cam = data_from_file[mobile_models[i]]['Main Camera']
            try    : Single_2  = Main_Cam['Single']
            except : Single_2 = ""
            try    : Features_2 = Main_Cam['Features']
            except : Features_2 = ""
            try    : Video_2 = Main_Cam['Video']
            except : Video_2 = ""
        except:
            Single_2 = ""
            Features_2 = ""
            Video_2 = ""

        #=> Misc
        try:
            Misc = data_from_file[mobile_models[i]]['Misc']
            try    : Colors  = Misc['Colors']
            except : Colors  = ""
            try    : Model = Misc['Models']
            except : Model = ""
            try    : SAR = Misc['SAR']
            except : SAR = ""
            try    : SAR_EU = Misc['SAR EU']
            except : SAR_EU  = ""
            try    : Price = Misc['Price']
            except : Price = ""
        except:
            Colors  = ""
            Model = ""
            SAR = ""
            SAR_EU = ""
            Price = ""

        #=> Comms
        try:
            Comms = data_from_file[mobile_models[i]]['Comms']
            try    : Wlan  = Comms['WLAN']
            except : Wlan  = ""
            try    : Bluetooth = Comms['Bluetooth']
            except : Bluetooth = ""
            try    : GPS = Comms['GPS']
            except : GPS = ""
            try    : NFC = Comms['NFC']
            except : NFC  = ""
            try    : Radio = Comms['Radio']
            except : Radio = ""
            try    : Usb = Comms['USB']
            except : Usb = ""
        except:
            Wlan  = ""
            Bluetooth = ""
            GPS = ""
            NFC = ""
            Radio = ""
            Usb = ""

        #=> Platform
        try:
            Platform = data_from_file[mobile_models[i]]['Platform']
            try    : OS  = Platform['OS']
            except : OS  = ""
            try    : Chipset = Platform['Chipset']
            except : Chipset = ""
            try    : CPU = Platform['CPU']
            except : CPU = ""
            try    : GPU = Platform['GPU']
            except : GPU  = ""
            try    : Radio = Platform['Radio']
            except : Radio = ""
            try    : USb = Platform['USB']
            except : USb = ""
        except:
            OS  = ""
            Chipset = ""
            CPU = ""
            GPU = ""
            Radio = ""
            USb = ""

        #=> Launch
        try:
            Launch = data_from_file[mobile_models[i]]['Launch']
            try    : Annou = Launch['Announced']
            except : Annou = ""
            try    : Status = Launch['Status']
            except : Status = ""
        except:
            Annou = ""
            Status = ""

        #=> Features
        try:
            Features = data_from_file[mobile_models[i]]['Features']
            try    : Sensors =str(Features['Sensors'] )
            except : Sensors = ""
            try    : other = Features['other']
            except : other = ""
        except:
            Sensors = ""
            other = ""

        #=> Sound
        try:
            Sound  = data_from_file[mobile_models[i]]['Sound']
            try    : Loud_Spk = Sound['Loudspeaker ']
            except : Loud_Spk = ""
            try    : Jack = Sound['3.5mm jack']
            except : Jack = ""
        except:
            Loud_Spk = ""
            Jack = ""

        #=> Battary
        try:
            Battery = data_from_file[mobile_models[i]]['Battery']
            try    : Type = Battery['Type']
            except : Type = ""
            try    : Standby = Battery['Stand-by']
            except : Standby = ""
            try    : Talk_time = Battery['Talk time']
            except : Talk_time = ""
        except:
            Type = ""
            Standby = ""
            Talk_time = ""

        #=> Memory
        try:
            Memory = data_from_file[mobile_models[i]]['Memory']
            try    : Card_slot = Memory['Card slot']
            except : Card_slot = ""
            try    : Internal = Memory['Internal']
            except : Internal = ""
            try    : Other = Memory['other']
            except : Other = ""
        except:
            Card_slot = ""
            Internal = ""
            Other = ""

        # Query 1 : Battery
        a = '''INSERT INTO `battary`(`Type`, `Charging`) VALUES (%s,%s)'''
        b = (Type, None)
        run_query(a, b)
        # Query 2 : Body
        a = '''INSERT INTO `body`(`Dimensions`, `Weight`, `Build`, `SIM`) VALUES (%s,%s,%s,%s)'''
        b = (Dimensions, Weight, Build, Sim)
        run_query(a, b)
        # Query 3 : Comms
        a = '''INSERT INTO `comms`(`WLAN`, `Bluetooth`, `GPS`, `NFC`, `Radio`, `USB`) VALUES (%s,%s,%s,%s,%s,%s)'''
        b = (Wlan, Bluetooth, GPS, NFC, Radio, Usb)
        run_query(a, b)
        # Query 4 : Display
        a = '''INSERT INTO `display`(`Type`, `Size`, `Resolution`) VALUES (%s,%s,%s)'''
        b = (Type, Size, Resolution)
        run_query(a, b)
        # Query 5 : Features
        a = '''INSERT INTO `features`(`Sensors`, `Other`) VALUES (%s,%s)'''
        b = (Sensors, other)
        run_query(a, b)
        # Query 6 : Launch
        a = '''INSERT INTO `launch`(`Announced`, `Status`) VALUES (%s,%s)'''
        b = (Annou, Status)
        run_query(a, b)
        # Query 7 : Main Camera
        a = '''INSERT INTO `main_camera`(`Quad`, `Features`, `Video`) VALUES (%s,%s,%s)'''
        b = (Single_2, Features_2, Video_2)
        run_query(a, b)
        # Query 8 : Memory
        a = '''INSERT INTO `memory`(`Card_slot`, `Internal`, `other`) VALUES (%s,%s,%s)'''
        b = (Card_slot, Internal, Other)
        run_query(a, b)
        # Query 9 : Misc
        a = '''INSERT INTO `misc`(`Colors`, `Model`, `SAR`, `SAR_EU`, `Price`) VALUES (%s,%s,%s,%s,%s)'''
        b = (Colors, Model, SAR, SAR_EU, Price)
        run_query(a, b)
        # Query 10 : Network
        a = '''INSERT INTO `network`( `Technology`,`2G_band`, `3G_band`, `4G_band`, `Speed`) VALUES (%s,%s,%s,%s,%s)'''
        b = (Technology, twoG_Bands, threeG_Bands, fourG_Bands, Speed)
        run_query(a, b)
        # Query 11 : Platform
        a = '''INSERT INTO `platform`(`OS`, `Chipset`, `CPU`, `GPU`) VALUES (%s,%s,%s,%s)'''
        b = (OS, Chipset, CPU, GPU)
        run_query(a, b)
        # Query 12 : Selfie Camera
        a = '''INSERT INTO `selfie_camera`(`Single`, `features`, `Video`) VALUES (%s,%s,%s)'''
        b = (Single_1, Features_1, Video_1)
        run_query(a, b)
        # Query 13 : Sound
        a = '''INSERT INTO `sound`(`Loudspeaker`, `3.5mm_jack`) VALUES (%s,%s)'''
        b = (Loud_Spk, Jack)
        run_query(a, b)
        # Query 14 : Products
        a = '''INSERT INTO `product`(`Product_Name`, `display_displaycol`, `Other_Data`, `body_b_id`, `platform_P_id`, `comms_C_id`,
                                    `selfie_camera_SC_id`, `misc_MI_id`, `network_N_id`, `launch_L_id`, `sound_S_id`, `memory_M_id`,
                                    `features_f_id`, `main_camera_MC_id`, `battary_B_id`, `display_D_id`) VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        name_p = mobile_models[i]
        i = i + 1
        b = (name_p, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i)
        run_query(a, b)


if __name__ == '__main__':
    new_db()
