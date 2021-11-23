# -*-coding:utf-8 -*-


import requests
import json
import folium

#pip install folium


def getSido():
    url = 'https://www.starbucks.co.kr/store/getSidoList.do'
    resp = requests.post(url)
    #print(resp.json())
    #print(resp.json()['list'])
    
    sido_json = resp.json()['list']
    
    sido_code = list(map(lambda x: x['sido_cd'], sido_json))
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    
    sido_dict = dict(zip(sido_code, sido_name))
    
    return sido_dict
   
def getGuGun(sido_code):
    url ='https://www.starbucks.co.kr/store/getGugunList.do'
    resp = requests.post(url, data={'sido_cd':sido_code})
    gugun_json = resp.json()['list']
    gugun_dict =dict(zip(list(map(lambda x: x['gugun_cd'], gugun_json)), list(map(lambda x: x['gugun_nm'], gugun_json))))
    return gugun_dict
    
def getStore(sido_code='', gugun_code=''):
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    # 알맞은 데이터를 보내면서 요청하여, 
    # s_name : "역삼이마트", tel: "1522-3232"}, {..}, ...] 로 출력하라.
    
    '''
    ins_lat: 37.4865643
    
    '''
    resp = requests.post(url, data={'ins_lat': '37.4865643',
                                    'ins_lng': '127.0206673',
                                    'p_sido_cd': sido_code,
                                    'p_gugun_cd': gugun_code,
                                    'in_biz_cd': '',
                                    'set_date': '' })
    #print(resp.json())
    store_json = resp.json()['list']
    
    store_list = list()
    for store in store_json:
        store_dict = dict()
        store_dict['s_name']= store['s_name']
        store_dict['dro_address'] = store['doro_address']
        store_dict['tel'] = store['tel']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        store_list.append(store_dict)
 
    #print(store_list)
    # res_dict = dict()
    # res_dict['store_list'] = store_list
    #
    # result = json.dumps(res_dict,  ensure_ascii=False)
    #
    # make_map(res_dict)
  
    return store_list
    
def make_map(result):
    
    #{"store_list": [{"s_name": "역삼이마트", "dro_address": "서울특별시 강남구 역삼로 310 (역삼동)", "tel": "1522-3232", "lat": "37.499367", "lot": "127.048425"}, ... ] 
    min_lat = min(list(map(lambda x: x['lat'], result['store_list']))) 
    max_lat = max(list(map(lambda x: x['lat'], result['store_list']))) 

    min_lot = max(list(map(lambda x: x['lot'], result['store_list'])))
    max_lot = max(list(map(lambda x: x['lot'], result['store_list'])))
    
    # 중간 좌표 
    center_lat = float(max_lat) - (float(max_lat) - float(min_lat))/2 
    center_lot = float(max_lot) - (float(max_lot) - float(min_lot))/2 
  
    #zoom_start 하는위치 좌표(위도 경도)값 , zoom_start=18이 max
    m = folium.Map(location=[center_lat, center_lot], zoom_start=14) 
    
    for data in result['store_list']:
        popup = folium.Popup(folium.Html(data['s_name']), max_width=len(data['s_name'])*30) # 마커위에 클릭시 문구 
        folium.Marker( # 마커 표시 
                location=[data['lat'], data['lot']],
                popup=popup, #팝업 만든거 연결 
                icon=folium.Icon(color='red')
            ).add_to(m)
    
    m.save('result.html') #result.html로 저장한다. 
    
    

    
if __name__ == '__main__':
    '''
    print(getSido())
    sido = input('도시 코드를 입력해 주세요 : ')
    if sido == '17':
        print(getStore(sido_code=sido))
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해 주세요 :')
        print(getStore(gugun_code=gugun))
    ''' 
       
    korea_starbucks = list()
    
    # 1. getSido 함수를 통해서 전국의 sido_code 가져온다
    sido_all = getSido()
    # 2. 1번에서 가지고 온 sido_code를 반복해서 getGuGun의 매개변수로 넣어준다.
    # 2-1. 만일, sido_code가 17 (세종시) 인 경우, getStore의 매개변수로 넣어준다.
    for sido in sido_all:
        if sido == '17':
            result = getStore(sido_code= sido)
            #print(result)
            korea_starbucks.extend(result) # 연결 
        else:
            gugun_all = getGuGun(sido)
            for gugun in gugun_all:
                result = getStore(gugun_code= gugun)
                #print(result)
                korea_starbucks.extend(result)
    # 3. getStore에서 리턴된 리스트를 korea_starbucks.extend 함수를 통해 합쳐준다.
    
    
    
    # 4. korea_starbucks를 {'list': [{}, {}, ... ]} 형태의 json으로 저장한다.
    starbucks_dict = dict()
    starbucks_dict['list'] = korea_starbucks
    
    result = json.dumps(starbucks_dict, ensure_ascii=False)

    with open('starbucks.json', 'w', encoding='utf-8') as f:
        f.write(result)
    
    
        