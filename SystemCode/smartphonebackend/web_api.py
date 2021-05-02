import json
from ruletable import ruletable
from queryDB import getInfo, getId
from flask import Flask, Response, request
from flask_cors import *  # support cross platform (important)

weight1 = {"cpu_score": 15, "screen_size": 15, "price": 25, "light_version": 5,
           "endurance_version": 15, "have_5G": 8, "fast_charge": 7, "is_apple": 30}
# weight_video = {"cpu_score": 20, "weight_score": 5, "screen_size": 15, "price": 25, "light_version": 5,
#             "endurance_version": 15, "have_5G": 10, "fast_charge": 5}
# weight_game = {"cpu_score": 15, "weight_score": 5, "screen_size": 20, "price": 25, "light_version": 10,
#             "endurance_version": 12, "have_5G": 8, "fast_charge": 5}

# col_name = ["ID", "brand_model", "Brand", "CPU", "GPU", "RAM", "Storage", "Resolutions", "Screen Size", "Dimensions",
#             "Weight", "Front", "Rear", "Capacity", "SIM", "Color", "Carrier", "OS", "Chipset", "USB", "Sensors",
#             "NFC",
#             "WaterAndDustProof", "Features", "Card Slot", "3.5mm Audio Jack Port", "Rating", "cpu_score",
#             "weight_score",
#             "screen", "screen_size", "price", "light_version", "game_version", "endurance_version", "have_5G",
#             "fast_charge", "Fast charging", "Screen_Dimension", "link", "img_src"]

col_name = ["id", "brand_model", "brand", "cpu", "chipset", "gpu", "ram", "storage", "resolutions", "screen size",
            "dimensions","weight", "front", "rear", "capacity", "sim", "color", "carrier", "cpu_score", "weight_score",
            "screen_size", "price", "is_apple", "light_version", "game_version", "endurance_version", "have_5G",
            "fast_charge", "fast_charging", "link", "img_src"]

app = Flask(__name__)
CORS(app)
RT = ruletable('rules.txt')

def convert_number(num_str):
    for i in num_str.keys():
        try:
            num = int(num_str[i])
            if num != 1 or num != 0:
                num_str[i] = num
        except:
            continue
    return num_str


@app.route('/interface', methods=['POST', 'GET'])
def respond():
    req = request.form
    req = req.to_dict()
    temp = float(req['price'])
    req = convert_number(req)
    try:
        m = req['constraint']
    except:
        m = 'price'
    conf = RT.reasoning(req)
    if 'battery_life' in m:
        conf['endurance_version'] = 1
    if 'weight' in m:
        conf['light_version'] = 1
    if 'FastCharge' in m:
        conf['fast_charge'] = 1
    if 'Need_5G' in m:
        conf['have_5G'] = 1
    if 'brand' in m:
        conf['is_apple'] = 1
    del conf['budget_type']
    conf['price'] = temp
    print(conf.items())
    item_no = 3

    idList, score = getId(conf, item_no, weight1)
    if idList == 0:
        mes = [{'mes': "No hand phone matched, please adjust your constraint and try again",
                'message': "No hand phone matched, please adjust your constraint and try again"}]
        return Response(json.dumps(mes), status=200, content_type="application/json")

    SearchResult = getInfo(idList)

    if len(SearchResult) < 1:
        return Response(json.dumps({'msg': 404}), status=202, content_type="application/json")

    res = []
    n = 0
    for i in SearchResult:
        temp = {}
        e = 0
        for j in col_name:
            temp[j] = i[e]
            e += 1
        temp['matching_score'] = score[n]
        n += 1
        res.append(temp)
    print(res)
    return Response(json.dumps(res), status=200, content_type="application/json")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
