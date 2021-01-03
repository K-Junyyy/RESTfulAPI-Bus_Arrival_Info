# RESTfulAPI-Bus_Arrival_Info
## 공공데이터 Open API를 이용한 버스 도착정보 서비스
![대문 이미지](https://user-images.githubusercontent.com/74912530/103458602-1714ed00-4d4d-11eb-98a9-818bde8fab6e.png) 
서울시 1일 교통수단별 통행 현황(분담률) 통계를 봤을 때 버스는 전체 중 24.4%를 차지할 만큼 비중이 큽니다. 
버스정류장 정보와 도착정보 및 정류장 정보들은 수요가 많을 것으로 예상되기 때문에 
서울시의 버스노선, 정류장 정보를 제공하는 서비스를 한번 제작해보았습니다.
<br/>
<br/>
<br/>

### 프론트엔드
![그림1](https://user-images.githubusercontent.com/74912530/103458720-32ccc300-4d4e-11eb-98fe-fef0dd390ba1.png)
![그림2](https://user-images.githubusercontent.com/74912530/103458724-352f1d00-4d4e-11eb-8b62-435fc5fc2353.png)

![그림3](https://user-images.githubusercontent.com/74912530/103458725-35c7b380-4d4e-11eb-8843-e12611864539.png)
![그림4](https://user-images.githubusercontent.com/74912530/103458726-36f8e080-4d4e-11eb-8993-d77eff01314c.png)

메인화면의 모습. 그리고 원하는 정보를 얻기위해 버스 번호를 폼에 입력 시, 서버로 데이터를 보냅니다. 
<br/>
<br/>
<br/>

### 공공데이터 포털에서 받아오는 정보들
![그림8](https://user-images.githubusercontent.com/74912530/103458754-745d6e00-4d4e-11eb-9597-2158efc44635.png)
![그림9](https://user-images.githubusercontent.com/74912530/103458756-74f60480-4d4e-11eb-9559-20f4a897a173.png)

![그림10](https://user-images.githubusercontent.com/74912530/103458752-732c4100-4d4e-11eb-8875-32ca160061c9.png)
![그림11](https://user-images.githubusercontent.com/74912530/103458753-73c4d780-4d4e-11eb-91ba-ecb1e60edd4e.png)
<br/>
#### 활용한 공공데이터
- 버스위치정보조회 서비스 : 실시간 버스 위치를 제공한다.
- 버스도착정보조회 서비스 : 특정 정류소에 대한 버스 도착예정 정보 제공한다.
- 버스노선 조회 서비스 : 노선에 대한 정보 제공한다.
- 정류소정보조회 서비스 : 정류소에 대한 정보를 제공한다.
<br/>
<br/>
<br/>

### AWS람다에서 파이썬 코드로 데이터들을 스크래핑
![그림12](https://user-images.githubusercontent.com/74912530/103459054-b3d88a00-4d4f-11eb-8c28-9abb1fe4a2ce.png)
![그림13](https://user-images.githubusercontent.com/74912530/103459253-462d5d80-4d51-11eb-9436-e1c89381038a.PNG)
<br/>
AWS에서 람다함수는 3개를 사용하였고 각각의 API게이트웨이의 엔드포인트에는 버스노선정보, 버스도착예정 정보, 실시간 버스위치정보들이 출력되어있고 웹페이지에서 request시 response로 해당 정보들이 넘어올 수 있도록 합니다.
<br/>
<br/>
<br/>
