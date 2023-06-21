import sqlite3

DATABASE_FILE = 'guests.db'

def create_guests_table():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY,
            full_name TEXT,
            email TEXT,
            company TEXT,
            mobile_number TEXT,
            checked_in INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def populate_guests_data():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()

    guestData = [
    {
        "full_name": "Hamza Alali",
        "email": "alali415h@gmail.com",
        "company": "Mubadala Excellence Program",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Faris Al Zaabi",
        "email": "alzaabi.faris@gmail.com",
        "company": "Mubadala Excellence Program",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Nouf Al Katheeri",
        "email": "k_nouf@yahoo.com",
        "company": "Social Media Influencer",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Saad Almarzooqi",
        "email": "Saad.almarzooqi@adpolice.gov.ae",
        "company": "Abu Dhabi Police",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Talib Alhinai",
        "email": "talib_alhinai@mckinsey.com",
        "company": "Mickensy",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Ali Al Shimmari",
        "email": "Ali.AlShimmari@taqa.com",
        "company": "TAQA",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Intesar Zenki",
        "email": "intesar.zenki@miral.ae",
        "company": "Miral",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Khadija Al Hashimi",
        "email": "khadija.alhashmi@miral.ae",
        "company": "Miral",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Khaled AlZaabi",
        "email": "Khaled.AlZaabi@taqa.com",
        "company": "TAQA",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Khuzama Alseiari",
        "email": "Khuzama.Alseiari@taqa.com",
        "company": "TAQA",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Maitha Hasan Al Shamsi",
        "email": "maitha.alshamsi@aadc.ae",
        "company": "TAQA (AADC)",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Nhayan AlDhaheri",
        "email": "Nhayan@gmail.com",
        "company": "Emirates Youth Council",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Noora alhosani",
        "email": "Noora.Alhosani@etihadrail.ae",
        "company": "Etihad Rail youth council",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Rashed AlMansoori",
        "email": "Rashed.AlMansoori@taqa.com",
        "company": "TAQA",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Tawadud Mohamed AlKatheeri",
        "email": "tawadud.alkatheeri@transco.ae",
        "company": "TAQA (TRANSCO)",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Nasir Hassan AlMazmi",
        "email": None,
        "company": "UAEI Platform",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Sultan Suhail Al Mazrouei",
        "email": None,
        "company": "UAEI Platform",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mohammed Bin Khalifa Al-Nahyan",
        "email": None,
        "company": "UAEI Platform",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Maher Chekir",
        "email": None,
        "company": "UAEI Platform",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Eisa Ahmed Al ali",
        "email": None,
        "company": "UAEI Platform",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Saad Abdulla Hamoodi",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Layla Saeed Al Nuwais",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mohamed Ghassan Al Khawaja",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mohamed Jasem Al Sayegh",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Jasem Ali Al Teneiji",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mariam Al Haddad",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Rand Alfraih",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Seeneen\u00a0Al Bastaki",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Ahmed Al Dhaheri",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Abdulla Al Balooshi",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Charles De Souza",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Hend Al Nuaimi",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Julia Woiwood",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Noura Alkaabi",
        "email": "nalkaabi@amanahealthcare.com",
        "company": "MH",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Khaled Ghaleb",
        "email": "GhalebK@ClevelandClinicAbuDhabi.ae;",
        "company": "MH",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Eissa Alhashmi",
        "email": "eissa.alhashmi@capitalhealth.ae;",
        "company": "MH",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Nouf Taha Alajami",
        "email": "nalajami@mubadalahealth.ae",
        "company": "MH",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Shafaa Omar Salem Mohsin",
        "email": "Almenhali shafaa.almenhali@danatalemarat.ae",
        "company": "MH",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Sara Alali",
        "email": "sarah.al-ali@g42.ai",
        "company": "MH",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Saed Al Jneibi",
        "email": "saljneibi@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Ahmed Al Romaithi",
        "email": "ajalromaithi@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Ahmed Saif",
        "email": "afsaif@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Maitha Al Hammadi",
        "email": "mtalhammadi@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Reem Al Breiki",
        "email": "ralbreiki@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Maha Al Ketbi",
        "email": "makalketbi@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Alreem Alhammdi",
        "email": "alreem.alhammadi@etihadrail.ae",
        "company": "Etihad Rail",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Bashayer Almazrouei",
        "email": "bashayer.almazrouei@etihadrail.ae",
        "company": "Etihad Rail",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Noura Albadi",
        "email": "noura.albadi@etihadrail.ae",
        "company": "Etihad Rail",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Noora Alhosani",
        "email": "noora.alhosani@etihadrail.ae",
        "company": "Etihad Rail",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Helen Bachir",
        "email": "hebachir@hub71.com",
        "company": "HUB71",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Al Hanoof Al Mansoori",
        "email": "alhalmansoori@hub71.com",
        "company": "HUB71",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Zahra Alhosani",
        "email": "zalhosani@hub71.com",
        "company": "HUB71",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Dana Almadhi",
        "email": "dalmadhi@hub71.com",
        "company": "HUB71",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Shamma Al Thehli",
        "email": "sthehli@hub71.com",
        "company": "HUB71",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Abdullah Abou Ali",
        "email": "aabouali@irena.org",
        "company": "International Renewable Energy Agency",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Riccardo Toxiri",
        "email": "RToxiri@irena.org",
        "company": "International Renewable Energy Agency",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mohamed Khalifa alowaid",
        "email": "malowaid@adnoc.ae",
        "company": "ADNOC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Capt. Ahmed Mohamed Alsalmi",
        "email": "amalsalmi@adnoc.ae",
        "company": "ADNOC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Capt. Osama Al Marashda",
        "email": "oalmarashda@adnoc.ae",
        "company": "ADNOC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Fatima Yousif Al Suwaidi",
        "email": "fyalsuwaidi@adnoc.ae",
        "company": "ADNOC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Reem Abdulla Alkuwaiti",
        "email": "raalkuwaiti@adnoc.ae",
        "company": "ADNOC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Azza Aljuwaied",
        "email": "azaljuwaied@microsoft.com",
        "company": "Microsoft Youth Council",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Jawahir Almaazmi",
        "email": "jalmaazmi@microsoft.com",
        "company": "Microsoft Youth Council",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Sondos Al Mehairbi",
        "email": "sondos.almehairbi@maan.gov.ae",
        "company": "Ma'an",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Alshumoos Al Hosani",
        "email": "alshumoos.alhosani@maan.gov.ae",
        "company": "Ma'an",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Salama Al Mazrouoi",
        "email": "salama.almazrouei@maan.gov.ae",
        "company": "Ma'an",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mohamed Helal Balooshi",
        "email": "Mohamed.alBalooshi@addcd.gov.ae",
        "company": "DCD",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Salama Amer Alameri",
        "email": "Salama.Alameri@addcd.gov.ae",
        "company": "DCD",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Saeed Abdulla Bahareth",
        "email": "Saeed.Bahareth@addcd.gov.ae",
        "company": "DCD",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mariam Adel Al Rabeea",
        "email": "mariam.alrabeea@addcd.gov.ae",
        "company": "DCD",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Amna AlBastaki",
        "email": "Amnalbastaki@outlook.com",
        "company": "Abu Dhabi Global Shapers",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Abdulla Aldhaheri",
        "email": "Abahshabeeb@gmail.com",
        "company": "Abu Dhabi Global Shapers",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Malak Abdullah",
        "email": "Malak.thyab@outlook.com",
        "company": "Abu Dhabi Global Shapers",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Abdelqader Al Saqqaf",
        "email": "Abedqader.alsaqqaf@cpc.com",
        "company": "Abu Dhabi Global Shapers",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Aida Al Yaaqoubi",
        "email": "aalyaaqoubi@yahsat.ae",
        "company": "Yahsat Youth Council",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Abdulrahman Al Zarooni",
        "email": "aalzarooni@yahsat.ae",
        "company": "Yahsat Youth Council",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Maryam Al Hashmi",
        "email": "malhashmi@yahsat.ae",
        "company": "Yahsat Youth Council",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Marwa Al Hosani",
        "email": "malhosani@yahsat.ae",
        "company": "Yahsat Youth Council",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Iman Abdulla",
        "email": "iabdulla@yahsat.ae",
        "company": "Yahsat Youth Council",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Ziad Ahmad Mahafza",
        "email": "zmahafza@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Sara Alkatheeri",
        "email": "ssalkatheeri@aldar.com",
        "company": "Aldar",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Sara Al Satrawi",
        "email": "salsatrawi@aldar.com",
        "company": "Aldar",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "AlDana Alhashmi",
        "email": "dalhashmi@aldar.com",
        "company": "Aldar",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Sarah Mohamed Ahmed Al Bakeri",
        "email": "salbakeri@tabreed.ae",
        "company": "Tabreed",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Fatima Aldhaheri",
        "email": "faldhaheri@tabreed.ae",
        "company": "Tabreed",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Sara Mousa",
        "email": "sara.mousa@edelman.com",
        "company": "Edelman",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mazar Masud",
        "email": "mazar.masud@edelman.com",
        "company": "Edelman",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Eleanor O'Keeffe",
        "email": "eleanor.okeeffe@edelman.com",
        "company": "Edelman",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Muhannad Salahi",
        "email": "muhannad.salahi@hkstrategies.com",
        "company": "Edelman",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Jaafar Al Aydaroos \u2013 UAE Idustries",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Khalifa Al Bishr \u2013 UAE Clusters",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Nasir Al Maazmi \u2013 UAE Industries",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Saeed Al Suwaidi \u2013 Traditional Infra.",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mohamed Al Mazroui \u2013 will confirm",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Ahmed Al Sharhan \u2013 UAE Clusters",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Maitha Al Hammadi \u2013 Real Estate",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Ohoud Al Messabi \u2013 Employee Relations",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Saba Hajaj \u2013 Talent Partner",
        "email": None,
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Hamad Al Mheiri",
        "email": "halmheiri@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Aysha Al Darmaki",
        "email": "asaaldarmaki@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Bashaer Al Ameri",
        "email": "balameri@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Hamad Al Mansoori",
        "email": "hjalmansoori@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Ahmed Al Haddad",
        "email": "aalhaddad@ega.ae",
        "company": "EGA",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Amal Al Sayegh",
        "email": "amalsayegh@ega.ae",
        "company": "EGA",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Rawan Al Qadi",
        "email": "raalqadi@ega.ae",
        "company": "EGA",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Khadija Al Abbasi",
        "email": "khabbasi@ega.ae",
        "company": "EGA",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Abdulaziz Al Bannai",
        "email": "aalbannai@ega.ae",
        "company": "EGA",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Reem Al Hammadi",
        "email": "ralhammadi@ega.ae",
        "company": "EGA",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Muhra Jamal AlMulla",
        "email": "mjalmulla@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mariyam Habib Al Sayegh",
        "email": "maalsayegh@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Sara Saeed Rashed Alzaabi",
        "email": None,
        "company": "ADQ",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mariam Alkhoori",
        "email": None,
        "company": "ADQ",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Shamma Alriyami",
        "email": None,
        "company": "ADQ",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Salem Alderei",
        "email": None,
        "company": "ADQ",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Monira Saleh Elhabil",
        "email": None,
        "company": "AD Police",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Hamdah Mohamed Elzarouny",
        "email": None,
        "company": "AD Police",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Mytha Ayoub Mohamed",
        "email": None,
        "company": "AD Police",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Alaa AL HANAFI",
        "email": "a00020718@Sorbonne.ae",
        "company": None,
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Ali ALHADDAD",
        "email": "a00022475@Sorbonne.ae",
        "company": None,
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Dana Halwani",
        "email": "Dana.Halwani@sorbonne.ae",
        "company": None,
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Soraya Bourhany",
        "email": "Soraya.Bourhany@sorbonne.ae",
        "company": None,
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Abdulla Almir",
        "email": "aalmir@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Khalid Abdulhamid",
        "email": "kabdulhamid@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Maitha AlHammadi",
        "email": "mtalhammadi@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Noora Al Kaabi",
        "email": "nalkaabi@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Sultan AlMazrouei",
        "email": "salmazrouee@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Ignacio Reynna",
        "email": "ireyna@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Nouf AlSuwaidi",
        "email": "noalsuwaidi@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Omar AlDhuhoori",
        "email": "oaldhuhoori@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Omar Al Marzooqi",
        "email": "oalmarzooqi@mubadala.ae",
        "company": "MIC",
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Muneera Al Mansoori",
        "email": "muneera.almansoori@eca.gov.ae",
        "company": None,
        "mobile_number": None,
        "checked_in": 0
    },
    {
        "full_name": "Hala Zainal",
        "email": "hala.zainal@eca.gov.ae",
        "company": None,
        "mobile_number": None,
        "checked_in": 0
    }
]

    for guest in guestData:
        c.execute('''
            INSERT INTO guests (full_name, email, company, mobile_number, checked_in)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            guest['full_name'],
            guest['email'],
            guest['company'],
            guest['mobile_number'],
            guest['checked_in']
        ))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_guests_table()
    populate_guests_data()
    print("Database guests.db created and populated with sample data.")
