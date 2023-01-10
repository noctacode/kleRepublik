################
# DICTIONARIES #
################

code_item = {
 '1_1': 'Q1F',  '1_2': 'Q2F',  '1_3': 'Q3F',  '1_4': 'Q4F',  '1_5': 'Q5F',  '1_6': 'Q6F',  '1_7': 'Q7F',  '7_1': 'FRM',  '7_1_partial': 'FRMp',
 '2_1': 'Q1W',  '2_2': 'Q2W',  '2_3': 'Q3W',  '2_4': 'Q4W',  '2_5': 'Q5W',  '2_6': 'Q6W',  '2_7': 'Q7W', '12_1': 'WRM', '12_1_partial': 'WRMp',
'23_1': 'Q1A', '23_2': 'Q2A', '23_3': 'Q3A', '23_4': 'Q4A', '23_5': 'Q5A', '23_6': 'Q6A', '23_7': 'Q7A', '24_1': 'ARM', '24_1_partial': 'ARMp',
 '4_1': 'Q1H',  '4_2': 'Q2H',  '4_3': 'Q3H',  '4_4': 'Q4H',  '4_5': 'Q5H',  '4_6': 'Q6H',  '4_7': 'Q7H', '17_1': 'HRM', '17_1_partial': 'HRMp',
 '3_1': 'Q1M',  '3_2': 'Q2M',  '3_3': 'Q3M',  '3_4': 'Q4M',  '3_5': 'Q5M',
'1_10': 'EB', '4_100': 'OP', '1000_4': 'FRT', '100_25': 'BB', '100_30': 'GB', '100_1': 'PPB',
'Barrel': 'barrel', 'Scope': 'scope', 'Projectile': 'projectile', 'Trigger Kit': 'trigger', 'Stock': 'stock'}

country_code_name = {'167':'Albania', '27':'Argentina', '169':'Armenia', '50':'Australia', '33':'Austria', '83':'Belarus', '32':'Belgium', '76':'Bolivia', '69':'Bosnia and Herzegovina', '9':'Brazil', '42':'Bulgaria', '23':'Canada', '64':'Chile', '14':'China', '78':'Colombia', '63':'Croatia', '171':'Cuba', '82':'Cyprus', '34':'Czech Republic', '55':'Denmark', '165':'Egypt', '70':'Estonia', '39':'Finland', '11':'France', '168':'Georgia', '12':'Germany', '44':'Greece', '13':'Hungary', '48':'India', '49':'Indonesia', '56':'Iran', '54':'Ireland', '58':'Israel', '10':'Italy', '45':'Japan', '71':'Latvia', '72':'Lithuania', '79':'Macedonia', '66':'Malaysia', '26':'Mexico', '52':'Moldova', '80':'Montenegro', '31':'Netherlands', '84':'New Zealand', '170':'Nigeria', '73':'North Korea', '37':'Norway', '57':'Pakistan', '75':'Paraguay', '77':'Peru', '67':'Philippines', '35':'Poland', '53':'Portugal', '1':'Romania', '41':'Russia', '164':'Saudi Arabia', '65':'Serbia', '68':'Singapore', '36':'Slovakia', '61':'Slovenia', '51':'South Africa', '47':'South Korea', '15':'Spain', '38':'Sweden', '30':'Switzerland', '81':'Taiwan', '59':'Thailand', '43':'Turkey', '40':'Ukraine', '166':'United Arab Emirates', '29':'United Kingdom', '74':'Uruguay', '24':'USA', '28':'Venezuela'}

country_name_code = {'Albania': '167', 'Argentina': '27', 'Armenia': '169', 'Australia': '50', 'Austria': '33', 'Belarus': '83', 'Belgium': '32', 'Bolivia': '76', 'Bosnia and Herzegovina': '69', 'Brazil': '9', 'Bulgaria': '42', 'Canada': '23', 'Chile': '64', 'China': '14', 'Colombia': '78', 'Croatia': '63', 'Cuba': '171', 'Cyprus': '82', 'Czech Republic': '34', 'Denmark': '55', 'Egypt': '165', 'Estonia': '70', 'Finland': '39', 'France': '11', 'Georgia': '168', 'Germany': '12', 'Greece': '44', 'Hungary': '13', 'India': '48', 'Indonesia': '49', 'Iran': '56', 'Ireland': '54', 'Israel': '58', 'Italy': '10', 'Japan': '45', 'Latvia': '71', 'Lithuania': '72', 'Macedonia': '79', 'Malaysia': '66', 'Mexico': '26', 'Moldova': '52', 'Montenegro': '80', 'Netherlands': '31', 'New Zealand': '84', 'Nigeria': '170', 'North Korea': '73', 'Norway': '37', 'Pakistan': '57', 'Paraguay': '75', 'Peru': '77', 'Philippines': '67', 'Poland': '35', 'Portugal': '53', 'Romania': '1', 'Russia': '41', 'Saudi Arabia': '164', 'Serbia': '65', 'Singapore': '68', 'Slovakia': '36', 'Slovenia': '61', 'South Africa': '51', 'South Korea': '47', 'Spain': '15', 'Sweden': '38', 'Switzerland': '30', 'Taiwan': '81', 'Thailand': '59', 'Turkey': '43', 'Ukraine': '40', 'United Arab Emirates': '166', 'United Kingdom': '29', 'Uruguay': '74', 'USA': '24', 'Venezuela': '28'}

item_code = {
'Q1F':  '1_1',  'Q2F':  '1_2', 'Q3F':  '1_3', 'Q4F':  '1_4', 'Q5F':  '1_5', 'Q6F':  '1_6', 'Q7F':  '1_7', 'FRM':  '7_1', 'FRMp':  '7_1_partial',
'Q1W':  '2_1',  'Q2W':  '2_2', 'Q3W':  '2_3', 'Q4W':  '2_4', 'Q5W':  '2_5', 'Q6W':  '2_6', 'Q7W':  '2_7', 'WRM': '12_1', 'WRMp': '12_1_partial',
'Q1A': '23_1',  'Q2A': '23_2', 'Q3A': '23_3', 'Q4A': '23_4', 'Q5A': '23_5', 'Q6A': '23_6', 'Q7A': '23_7', 'ARM': '24_1', 'ARMp': '24_1_partial',
'Q1H':  '4_1',  'Q2H':  '4_2', 'Q3H':  '4_3', 'Q4H':  '4_4', 'Q5H':  '4_5', 'Q6H':  '4_6', 'Q7H':  '4_7', 'HRM': '17_1', 'HRMp': '17_1_partial',
'Q1M':  '3_1',  'Q2M':  '3_2', 'Q3M':  '3_3', 'Q4M':  '3_4', 'Q5M':  '3_5',
'EB': '1_10', 'OP': '4_100', 'FRT': '1000_4', 'BB': '100_25', 'GB': '100_30', 'PPB': '100_1',
'barrel': 'Barrel', 'scope': 'Scope', 'projectile': 'Projectile', 'trigger': 'Trigger Kit', 'stock': 'Stock'}

#########
# LISTS #
#########

countries = ['Albania', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Belarus', 'Belgium', 'Bolivia', 'Bosnia and Herzegovina', 'Brazil', 'Bulgaria', 'Canada', 'Chile', 'China', 'Colombia', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Egypt', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'India', 'Indonesia', 'Iran', 'Ireland', 'Israel', 'Italy', 'Japan', 'Latvia', 'Lithuania', 'Macedonia', 'Malaysia', 'Mexico', 'Moldova', 'Montenegro', 'Netherlands', 'New Zealand', 'Nigeria', 'North Korea', 'Norway', 'Pakistan', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Romania', 'Russia', 'Saudi Arabia', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Turkey', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'USA', 'Venezuela']

tradeables = [
'ARM', 'FRM', 'HRM', 'WRM',
'Q1A', 'Q2A', 'Q3A' , 'Q4A', 'Q5A',
'Q1F', 'Q2F', 'Q3F', 'Q4F', 'Q5F', 'Q6F', 'Q7F',
'Q1H', 'Q2H', 'Q3H', 'Q4H', 'Q5H',
'Q1M', 'Q2M', 'Q3M', 'Q4M', 'Q5M',
'Q1W', 'Q2W', 'Q3W', 'Q4W', 'Q5W', 'Q6W', 'Q7W']

#############
# VARIABLES #
#############

country_set = []

money = {'cc': -1, 'g': -1}
money_old = {'cc': -2, 'g': -2}

offers_got = []
offers_file = []
offers_closed = []
offers_set = []

storage = {
'Q1F':0, 'Q2F':0, 'Q3F':0, 'Q4F':0, 'Q5F':0, 'Q6F':0, 'Q7F':0, 'FRM':0, 'FRMp':0,
'Q1W':0, 'Q2W':0, 'Q3W':0, 'Q4W':0, 'Q5W':0, 'Q6W':0, 'Q7W':0, 'WRM':0, 'WRMp':0,
'Q1A':0, 'Q2A':0, 'Q3A':0, 'Q4A':0, 'Q5A':0, 'ARM':0, 'ARMp':0,
'Q1H':0, 'Q2H':0, 'Q3H':0, 'Q4H':0, 'Q5H':0, 'HRM':0, 'HRMp':0,
'Q1M':0, 'Q2M':0, 'Q3M':0, 'Q4M':0, 'Q5M':0,
'EB':0, 'OP':0, 'FRT':0, 'BB':0, 'GB':0, 'PPB':0,
'barrel':0, 'scope':0, 'projectile':0, 'trigger':0, 'stock':0}

offers_list_duplicates = {
'ARM' : [], 'FRM' : [], 'HRM' : [], 'WRM' : [],
'Q1A' : [], 'Q2A' : [], 'Q3A' : [], 'Q4A' : [], 'Q5A' : [],
'Q1F' : [], 'Q2F' : [], 'Q3F' : [], 'Q4F' : [], 'Q5F' : [], 'Q6F' : [], 'Q7F' : [],
'Q1H' : [], 'Q2H' : [], 'Q3H' : [], 'Q4H' : [], 'Q5H' : [],
'Q1M' : [], 'Q2M' : [], 'Q3M' : [], 'Q4M' : [], 'Q5M' : [],
'Q1W' : [], 'Q2W' : [], 'Q3W' : [], 'Q4W' : [], 'Q5W' : [], 'Q6W' : [], 'Q7W' : []}

offers_list_got = {
'ARM' : [], 'FRM' : [], 'HRM' : [], 'WRM' : [],
'Q1A' : [], 'Q2A' : [], 'Q3A' : [], 'Q4A' : [], 'Q5A' : [],
'Q1F' : [], 'Q2F' : [], 'Q3F' : [], 'Q4F' : [], 'Q5F' : [], 'Q6F' : [], 'Q7F' : [],
'Q1H' : [], 'Q2H' : [], 'Q3H' : [], 'Q4H' : [], 'Q5H' : [],
'Q1M' : [], 'Q2M' : [], 'Q3M' : [], 'Q4M' : [], 'Q5M' : [],
'Q1W' : [], 'Q2W' : [], 'Q3W' : [], 'Q4W' : [], 'Q5W' : [], 'Q6W' : [], 'Q7W' : []}

offers_list_read_id = []

offers_list_modified = {
'ARM' : [], 'FRM' : [], 'HRM' : [], 'WRM' : [],
'Q1A' : [], 'Q2A' : [], 'Q3A' : [], 'Q4A' : [], 'Q5A' : [],
'Q1F' : [], 'Q2F' : [], 'Q3F' : [], 'Q4F' : [], 'Q5F' : [], 'Q6F' : [], 'Q7F' : [],
'Q1H' : [], 'Q2H' : [], 'Q3H' : [], 'Q4H' : [], 'Q5H' : [],
'Q1M' : [], 'Q2M' : [], 'Q3M' : [], 'Q4M' : [], 'Q5M' : [],
'Q1W' : [], 'Q2W' : [], 'Q3W' : [], 'Q4W' : [], 'Q5W' : [], 'Q6W' : [], 'Q7W' : []}

offers_list_new = {
'ARM' : [], 'FRM' : [], 'HRM' : [], 'WRM' : [],
'Q1A' : [], 'Q2A' : [], 'Q3A' : [], 'Q4A' : [], 'Q5A' : [],
'Q1F' : [], 'Q2F' : [], 'Q3F' : [], 'Q4F' : [], 'Q5F' : [], 'Q6F' : [], 'Q7F' : [],
'Q1H' : [], 'Q2H' : [], 'Q3H' : [], 'Q4H' : [], 'Q5H' : [],
'Q1M' : [], 'Q2M' : [], 'Q3M' : [], 'Q4M' : [], 'Q5M' : [],
'Q1W' : [], 'Q2W' : [], 'Q3W' : [], 'Q4W' : [], 'Q5W' : [], 'Q6W' : [], 'Q7W' : []}

offers_list_read = {
'ARM' : [], 'FRM' : [], 'HRM' : [], 'WRM' : [],
'Q1A' : [], 'Q2A' : [], 'Q3A' : [], 'Q4A' : [], 'Q5A' : [],
'Q1F' : [], 'Q2F' : [], 'Q3F' : [], 'Q4F' : [], 'Q5F' : [], 'Q6F' : [], 'Q7F' : [],
'Q1H' : [], 'Q2H' : [], 'Q3H' : [], 'Q4H' : [], 'Q5H' : [],
'Q1M' : [], 'Q2M' : [], 'Q3M' : [], 'Q4M' : [], 'Q5M' : [],
'Q1W' : [], 'Q2W' : [], 'Q3W' : [], 'Q4W' : [], 'Q5W' : [], 'Q6W' : [], 'Q7W' : []}

offers_list_sold = {
'ARM' : [], 'FRM' : [], 'HRM' : [], 'WRM' : [],
'Q1A' : [], 'Q2A' : [], 'Q3A' : [], 'Q4A' : [], 'Q5A' : [],
'Q1F' : [], 'Q2F' : [], 'Q3F' : [], 'Q4F' : [], 'Q5F' : [], 'Q6F' : [], 'Q7F' : [],
'Q1H' : [], 'Q2H' : [], 'Q3H' : [], 'Q4H' : [], 'Q5H' : [],
'Q1M' : [], 'Q2M' : [], 'Q3M' : [], 'Q4M' : [], 'Q5M' : [],
'Q1W' : [], 'Q2W' : [], 'Q3W' : [], 'Q4W' : [], 'Q5W' : [], 'Q6W' : [], 'Q7W' : []}