"""
smartphone scraper test data file
"""
number_of_apple_smartphones_2015_links = 41
brand_samsung = 'Samsung'
brand_apple = 'Apple'

test_website_urls = [
    'https://www.gsmarena.com/results.php3?nYearMin=2009&nYearMax=2009&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2010&nYearMax=2010&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2011&nYearMax=2011&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2012&nYearMax=2012&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2013&nYearMax=2013&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2014&nYearMax=2014&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2015&nYearMax=2015&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2016&nYearMax=2016&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2017&nYearMax=2017&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2018&nYearMax=2018&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2019&nYearMax=2019&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2020&nYearMax=2020&sMakers=9&sAvailabilities=1,3&sFormFactors=1',
    'https://www.gsmarena.com/results.php3?nYearMin=2021&nYearMax=2021&sMakers=9&sAvailabilities=1,3&sFormFactors=1'
]

test_phones_links = [
    'https://www.gsmarena.com/samsung_s5230_star-2739.php',
    'https://www.gsmarena.com/samsung_s3650_corby-2908.php',
    'https://www.gsmarena.com/samsung_i8910_omnia_hd-2691.php',
    'https://www.gsmarena.com/samsung_i7500_galaxy-2791.php',
    'https://www.gsmarena.com/samsung_s8000_jet-2835.php',
    'https://www.gsmarena.com/samsung_i5700_galaxy_spica-2965.php',
    'https://www.gsmarena.com/samsung_i8000_omnia_ii-2836.php',
    'https://www.gsmarena.com/samsung_m8910_pixon12-2813.php',
    'https://www.gsmarena.com/samsung_s3310-2812.php',
    'https://www.gsmarena.com/samsung_w880_amoled_12m-2948.php',
    'https://www.gsmarena.com/samsung_e1080t-2941.php',
    'https://www.gsmarena.com/samsung_b2100_xplorer-2747.php',
    'https://www.gsmarena.com/samsung_s5230w_star_wifi-2935.php',
    'https://www.gsmarena.com/samsung_c5212-2709.php',
    'https://www.gsmarena.com/samsung_s5560_marvel-2989.php',
    'https://www.gsmarena.com/samsung_e2120-2900.php',
    'https://www.gsmarena.com/samsung_s5600_preston-2738.php',
    'https://www.gsmarena.com/samsung_s5233t-3235.php',
    'https://www.gsmarena.com/samsung_c3010-2707.php',
    'https://www.gsmarena.com/samsung_t929_memoir-2663.php',
    'https://www.gsmarena.com/samsung_e1070-2672.php',
    'https://www.gsmarena.com/samsung_m7600_beat_dj-2684.php',
    'https://www.gsmarena.com/samsung_s7550_blue_earth-2931.php',
    'https://www.gsmarena.com/samsung_vodafone_360_h1-2954.php',
    'https://www.gsmarena.com/samsung_f480i-2987.php',
    'https://www.gsmarena.com/samsung_c3510_genoa-3068.php',
    'https://www.gsmarena.com/samsung_b7300_omnialite-2837.php',
    'https://www.gsmarena.com/samsung_s5600v_blade-2860.php',
    'https://www.gsmarena.com/samsung_e1100-2673.php',
    'https://www.gsmarena.com/samsung_i7410-2698.php',
    'https://www.gsmarena.com/samsung_e1120-2711.php',
    'https://www.gsmarena.com/samsung_e1107_crest_solar-2829.php',
    'https://www.gsmarena.com/samsung_b3210_corbytxt-2943.php',
]

test_phones_data = {'Samsung E1107 Crest Solar':
    {
        'Network': {'Technology': 'GSM', '2G bands': 'GSM 900 / 1800 ', 'GPRS': 'Class 10', 'EDGE': 'No'},
        'Launch': {'Announced': '2009, June. Released 2009, July', 'Status': 'Discontinued'},
        'Body': {'Dimensions': '105.2 x 44.2 x 16.4 mm (4.14 x 1.74 x 0.65 in)',
                 'Weight': '77 g (2.72 oz)', 'SIM': 'Mini-SIM', 'other': ['Flashlight']},
        'Display': {'Type': 'CSTN, 65K colors', 'Size': '1.52 inches, 7.5 cm2 (~16.0% screen-to-body ratio)',
                    'Resolution': '128 x 128 pixels, 1:1 ratio (~119 ppi density)'},
        'Memory': {'Card slot': 'No', 'Phonebook': 'Yes, up to 500 entries',
                   'Call records': '30 dialed, 30 received, 30 missed calls'},
        'Camera': {'other': ['No']},
        'Sound': {'Loudspeaker ': 'Yes', '3.5mm jack ': 'No'},
        'Comms': {'WLAN': 'No', 'Bluetooth': 'No', 'GPS': 'No', 'Radio': 'FM radio', 'USB': ''},
        'Features': {'Sensors': '', 'Messaging': 'SMS', 'Browser': 'WAP 2.0/xHTML', 'Games': 'Yes',
                     'Java': 'Yes, MIDP 2.0',
                     'other': ['Organizer\r\nVoice memo\r\nMobile Tracker\r\nPredictive text input']},
        'Battery': {'Type': 'Removable Li-Ion 800 mAh battery',
                    'Charging': 'Solar panel for battery charging - optional\n',
                    'Stand-by': 'Upto 30 min', 'Talk time': 'Up to 1 min 40 sec'},
        'Misc': {'Colors': 'Black', 'SAR EU': '0.56 W/kg (head)     ', 'Price': 'About 50 EUR'}
    }
}
