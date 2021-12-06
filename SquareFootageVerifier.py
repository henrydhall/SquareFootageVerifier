import ezsheets
import requests

def ezsheets_demo():
    ss = ezsheets.Spreadsheet('1YqAonK2A2SdadLX4sfVyhmRhqVoXEmwvnrG8ksjsMFA')
    print(ss.title)
    print(ss.sheetTitles)
    testerSheet = ss[0]
    print(testerSheet['A1'])
    testerSheet['B1'] = 'My name is Henry'
    testerSheet['A2'] = 'This is a basic demonstration of ezsheets capabilities'
    testerSheet['B2'] = input('Enter a word to put in cell B2: ')

def requests_demo():
    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    with requests.Session() as s:
        home = '3273-N-100-W-Ogden,-UT-84414_rb/'
        url = 'https://www.zillow.com/homes/'+home    
        r = s.get(url, headers=req_headers)
    print(r.text)

if __name__ == '__main__':
    pass