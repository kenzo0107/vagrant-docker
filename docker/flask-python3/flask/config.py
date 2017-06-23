SECRET_KEY = 'RWpPwNz1KPObtJYqgNa40HUKaufHWDayCKjRnxHqmE6Mq3xiWGa5gNYIQKHTtiihKvwP4T3TEFdYPK8wJor1J0g2NZuzp5lAH9xvjfSJZqtsuYLZDO0bNbR9SHf0tRAciwgq1rK9DmSZ24nL0OwlVxBtb2E3eoTVuE0WMSJXK6hRA6lceD0oGKLkxK5fb3soBHMCRZzK0eUAvDPWvjZWbIBlIh4QefMYs46Xf3pZOq9UkZqnJyH3hptubK8MvRM5'

DEFAULTS = {
    'circuit_id':    1,     # 循環ID
    'station_id':    12,    # 停留所ID
}

CIRCUITS = {
    1: {'id': 1, 'name': '南西', 'bgcolor': '#8C8'},
    2: {'id': 2, 'name': '喜沢', 'bgcolor': '#FAAC58'},
    3: {'id': 3, 'name': '川岸', 'bgcolor': '#F5A9A9'},
    4: {'id': 4, 'name': '西',   'bgcolor': '#2E64FE'},
    5: {'id': 5, 'name': '美笹', 'bgcolor': '#F5A9F2'},
}

TIME_TABLES = {
    1: {
        'id': 1,
        'exclude_hours': {16},
        'interval_minutes': 60,
        'stations': {
             1: {"id": 1, 'start': '8:00', 'end':'18:00', 'arrived_at': '00', 'name': '0 下笹目'},
             2: {"id": 2, 'start': '8:01', 'end':'18:01', 'arrived_at': '01', 'name': '1 下町橋'},
             3: {"id": 3, 'start': '8:02', 'end':'18:02', 'arrived_at': '02', 'name': '2 笹目公園'},
             4: {"id": 4, 'start': '8:03', 'end':'18:03', 'arrived_at': '03', 'name': '3 笹目七丁目'},
             5: {"id": 5, 'start': '8:04', 'end':'18:04', 'arrived_at': '04', 'name': '4 早瀬公園'},
             5: {"id": 5, 'start': '8:05', 'end':'18:05', 'arrived_at': '04', 'name': '5 早瀬二丁目'},
             6: {"id": 6, 'start': '8:07', 'end':'18:07', 'arrived_at': '05', 'name': '6 早瀬会館'},
             8: {"id": 8, 'start': '8:11', 'end':'18:11', 'arrived_at': '11', 'name': '7 戸田公園大橋'},
             9: {"id": 9, 'start': '8:12', 'end':'18:12', 'arrived_at': '12', 'name': '8 下町さくら西ひろば'},
            10: {"id":10, 'start': '8:13', 'end':'18:13', 'arrived_at': '13', 'name': '9 金森橋'},
            11: {"id":11, 'start': '8:14', 'end':'18:14', 'arrived_at': '14', 'name': '10 新曽南三丁目'},
            12: {"id":12, 'start': '8:15', 'end':'18:15', 'arrived_at': '15', 'name': '11 南町'},
            13: {"id":13, 'start': '8:16', 'end':'18:16', 'arrived_at': '16', 'name': '12 上戸田南保育園'},
            14: {"id":14, 'start': '8:25', 'end':'18:25', 'arrived_at': '18', 'name': '13 戸田公園駅西口'},
            15: {"id":15, 'start': '8:27', 'end':'18:27', 'arrived_at': '27', 'name': '14 本町五丁目'},
            16: {"id":16, 'start': '8:28', 'end':'18:28', 'arrived_at': '28', 'name': '15 ボートコース入口'},
            17: {"id":17, 'start': '8:32', 'end':'18:32', 'arrived_at': '32', 'name': '16 県営戸田公園'},
            18: {"id":18, 'start': '8:33', 'end':'18:33', 'arrived_at': '33', 'name': '17 旭ヶ丘'},
            19: {"id":19, 'start': '8:34', 'end':'18:34', 'arrived_at': '34', 'name': '18 ボートコース入口'},
            20: {"id":20, 'start': '8:36', 'end':'18:36', 'arrived_at': '36', 'name': '19 戸田公園駅南'},
            21: {"id":21, 'start': '8:37', 'end':'18:37', 'arrived_at': '37', 'name': '20 上戸田南保育園'},
            22: {"id":22, 'start': '8:38', 'end':'18:38', 'arrived_at': '38', 'name': '21 南町'},
            23: {"id":23, 'start': '8:39', 'end':'18:39', 'arrived_at': '39', 'name': '22 新曽南三丁目'},
            24: {"id":24, 'start': '8:40', 'end':'18:40', 'arrived_at': '40', 'name': '23 給食センター入り口'},
            25: {"id":25, 'start': '8:41', 'end':'18:41', 'arrived_at': '41', 'name': '24 戸田公園大橋'},
            26: {"id":26, 'start': '8:44', 'end':'18:44', 'arrived_at': '44', 'name': '25 笹目川排水機場'},
            27: {"id":27, 'start': '8:46', 'end':'18:46', 'arrived_at': '46', 'name': '26 早瀬二丁目'},
            28: {"id":28, 'start': '8:48', 'end':'18:48', 'arrived_at': '48', 'name': '27 聖橋'},
            29: {"id":28, 'start': '8:49', 'end':'18:49', 'arrived_at': '49', 'name': '28 笹目六丁目'},
        }
    },
    2: {
        'id': 2,
        'exclude_hours': {},
        'interval_minutes': 30,
        'stations': {
             1: {"id": 1, 'start':'7:40', 'end':'18:10', 'arrived_at': '40', 'name': '0 戸田公園駅西口'},
             2: {"id": 2, 'start':'7:41', 'end':'18:11', 'arrived_at': '41', 'name': '1 こどもの国'},
             3: {"id": 3, 'start':'7:42', 'end':'18:12', 'arrived_at': '42', 'name': '2 戸田中央総合病院'},
             4: {"id": 4, 'start':'7:43', 'end':'18:13', 'arrived_at': '43', 'name': '3 上戸田二丁目'},
             5: {"id": 5, 'start':'7:45', 'end':'18:15', 'arrived_at': '45', 'name': '4 戸田市役所南'},
             5: {"id": 5, 'start':'7:47', 'end':'18:17', 'arrived_at': '47', 'name': '5 上戸田稲荷'},
             6: {"id": 6, 'start':'7:49', 'end':'18:19', 'arrived_at': '49', 'name': '6 中島病院'},
             8: {"id": 8, 'start':'7:50', 'end':'18:20', 'arrived_at': '50', 'name': '7 戸田東中学校北'},
             9: {"id": 9, 'start':'7:51', 'end':'18:21', 'arrived_at': '51', 'name': '8 中町一丁目北'},
            10: {"id":10, 'start':'7:52', 'end':'18:22', 'arrived_at': '52', 'name': '9 中町公園'},
            11: {"id":11, 'start':'7:54', 'end':'18:24', 'arrived_at': '54', 'name': '10 カリン通り'},
            12: {"id":12, 'start':'7:55', 'end':'18:25', 'arrived_at': '55', 'name': '11 とだ小林医院'},
            13: {"id":13, 'start':'7:55', 'end':'18:25', 'arrived_at': '56', 'name': '12 喜沢一丁目'},
            14: {"id":14, 'start':'7:56', 'end':'18:26', 'arrived_at': '57', 'name': '13 喜沢記念会館'},
            15: {"id":15, 'start':'7:57', 'end':'18:27', 'arrived_at': '58', 'name': '14 喜沢小学校南'},
            16: {"id":16, 'start':'7:58', 'end':'18:28', 'arrived_at': '59', 'name': '15 アリスの広場東'},
            17: {"id":17, 'start':'7:59', 'end':'18:29', 'arrived_at': '32', 'name': '16 喜沢橋'},
            18: {"id":18, 'start':'8:01', 'end':'18:31', 'arrived_at': '33', 'name': '17 喜沢南一丁目'},
            19: {"id":19, 'start':'8:02', 'end':'18:32', 'arrived_at': '34', 'name': '18 喜沢中学校'},
            20: {"id":20, 'start':'8:03', 'end':'18:33', 'arrived_at': '36', 'name': '19 喜沢南二丁目'},
            21: {"id":21, 'start':'8:03', 'end':'18:33', 'arrived_at': '37', 'name': '20 中町多目的広場'},
            22: {"id":22, 'start':'8:04', 'end':'18:34', 'arrived_at': '38', 'name': '21 こぶし公園前'},
            23: {"id":23, 'start':'8:05', 'end':'18:35', 'arrived_at': '39', 'name': '22 障害者福祉会館北'},
            24: {"id":24, 'start':'8:07', 'end':'18:37', 'arrived_at': '40', 'name': '23 戸田南小学校南'},
            25: {"id":25, 'start':'8:15', 'end':'18:45', 'arrived_at': '41', 'name': '24 戸田公園駅西口'},
        }
    }
}
