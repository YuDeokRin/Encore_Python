# -*-coding:utf-8 -*-


import requests
import json



def getSido():
    url = 'https://www.starbucks.co.kr/store/getSidoList.do'
    resp = requests.post(url)
    #print(resp.json())
    #print(resp.json()['list'])
    
    sido_json = resp.json()['list']
    
    sido_code = list(map(lambda x: x['sido_cd'], sido_json)) # list
    #print(sido_code)
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    #print(sido_name)
    sido_dict = dict(zip(sido_code, sido_name))
    #print(sido_dict)
    return sido_dict
   
def getGuGun(sido_code):
    url ='https://www.starbucks.co.kr/store/getGugunList.do'
    # requests 모듈을 사용하여 해당 url에 sido_cd라는 이름으로 sido_code를 요청해주세요.
    resp = requests.post(url, data={'sido_cd':sido_code})
    #print(resp.json())
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
    res_dict = dict()
    res_dict['store_list'] = store_list
    
    result = json.dumps(res_dict,  ensure_ascii=False)
    
    return result
    
    
    
if __name__ == '__main__':
    print(getSido())
    sido = input('도시 코드를 입력해 주세요 : ')
    #print(sido)
    if sido == '17':
        print(getStore(sido_code=sido))
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해 주세요 :')
        print(getStore(gugun_code=gugun))
        
        
    # 전국의 모든 starbucks 매장을 json파일로 저장하자!
    
    
        