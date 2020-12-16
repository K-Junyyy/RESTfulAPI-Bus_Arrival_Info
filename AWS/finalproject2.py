import requests, xmltodict, json

def lambda_handler(event, context): 
    
    bus_id = 100100112
    # 인증키
    key = "zhcgaqfAQqhbqRR02bUVpPGKyvNIE%2BCQrM1SLAaZqTo5Ip6IxdyEtzPKJ1CwuvCJQVhbEYrmgFIfD1oh0%2BKxTw%3D%3D"
    # 노선ID로 차량들의 위치정보를 조회
    url4 = "http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?ServiceKey={}&busRouteId={}".format(key,bus_id)
    
    
    # 노선ID로 차량들의 위치정보를 조회

    content = requests.get(url4).content # GET요청
    dict=xmltodict.parse(content) # XML을 dictionary로 파싱
    #파싱은 어떤 페이지(문서, html 등)에서 내가 원하는 데이터를 특정 패턴이나 순서로 추출해 가공하는 것

    jsonString = json.dumps(dict['ServiceResult']['msgBody']['itemList'], ensure_ascii=False) # dict을 json으로 변환
    jsonObj = json.loads(jsonString) # json을 dict으로 변환

    gps = [[0 for col in range(3)] for row in range(30)]

    for i in range(len(jsonObj)):
        gps[i][0] = jsonObj[i]['plainNo']  # plainNo : 차량번호
        gps[i][1] = jsonObj[i]['gpsX']  # gpsX : gps x좌표
        gps[i][2] = jsonObj[i]['gpsY']  # gpsY : gps y좌표
    

    return { 
    'statusCode': 200, 
    'headers':{'Access-Control-Allow-Origin':'*'},
    'body': 
            json.dumps(gps, ensure_ascii=False)
            
    }
