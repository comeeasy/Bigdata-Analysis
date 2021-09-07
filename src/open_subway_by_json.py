import os
import requests
import urllib
import myOauth as oauth

class SubwayInfoScrapper:
    '''
    KEY: 발급받은 인증키
    TYPE: xml, xmlf, xls, json 데이터 형식
    SERVICE: 서비스명
    START_INDEX: 페이징 시작번호
    END_INDEX: Integer: 페이징 끝번호
    STATION_CD: String (선택) 전철역코드
    STATION_NM: String (선택) 전철역명
    LINE_NM: String: 호선 1~9: 1~9호선, I: 인천1호선, K: 경의중앙선, B: 분당선, A: 공항철도, G: 경춘선, S:신분당선, SU:수인선. 현재 서울교통공사관할인 1~9호선 정보만 제공.
    '''
    
    def __init__(self, key, _type, service, start_idx, 
                 end_idx, line_num, station_cd="", station_nm=""):
        '''
        url: http://openAPI.seoul.go.kr:8088
        '''
        self._key = key
        self._type = _type
        self._service = service
        self._start_idx = start_idx
        self._end_idx = end_idx
        self._line_num = line_num
        self._station_cd = station_cd
        self._station_nm = station_nm
            
        self._params = "/".join([self._key, self._type, self._service, self._start_idx,
                                 self._end_idx, self._station_cd, self._station_nm, self._line_num])
        self._base_url = 'http://openAPI.seoul.go.kr:8088'
        self._url = '/'.join([self._base_url, self._params])
    
    def request(self):
        '''
        only print result
        '''
        print(self._url)
        r = requests.get(self._url)
        print(r)
        stations = r.json()
                                
        for elem in stations['SearchSTNBySubwayLineService']['row']:
            print(f"{elem['STATION_CD']:4s}\t{elem['STATION_NM']:15s}\t{elem['LINE_NUM']:3s}\t{elem['FR_CODE']:10s}")

def main():
    keys = oauth.getKey(os.path.join(os.getcwd(), 'data', 'key.properties'))
    
    KEY = str(keys['dataseoul'])
    s = SubwayInfoScrapper(KEY, 'json', service='SearchSTNBySubwayLineService', start_idx='1',
                      end_idx='10', line_num='2')
    s.request()
    
if __name__ == '__main__':
    main()
