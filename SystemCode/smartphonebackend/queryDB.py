import sqlite3 as sql

# dic = {'Price': 300}
weight_video = {"cpu_score": 20, "weight_score": 5, "screen_size": 15, "price": 25, "light_version": 5,
            "endurance_version": 15, "have_5G": 10, "fast_charge": 5}
weight_game = {"cpu_score": 15, "weight_score": 5, "screen_size": 20, "price": 25, "light_version": 10,
            "endurance_version": 12, "have_5G": 8, "fast_charge": 5}
weight1 = {"cpu_score": 20, "screen_size": 20, "price": 25, "light_version": 5,
           "endurance_version": 15, "have_5G": 8, "fast_charge": 7, "is_apple": 100}

db_name = "phonesDB.db"


def getId(dic, num=3, weight=weight1, constraint=None):  # mainkey='Price'
    """get id from database based on user input then calculate the score based on weight and
    return "num" number of sorted ID and score with highest score"""

    c = {}
    answer = []
    score = []

    db_conn = sql.connect(db_name)
    cur = db_conn.cursor()

    for i in dic.keys():
        if i == 'price':
            queryCMD = f"SELECT ID, {i} FROM phones WHERE {i} BETWEEN {float(dic[i]) * 0.9} AND {float(dic[i]) * 1.1}"
            cur.execute(queryCMD)
            queryResult = cur.fetchall()
            if len(c) == 0:  # default constraint
                for j in queryResult:
                    c[j[0]] = float(dic[i]) / (float(j[1]) * weight[i])
            else:
                for j in queryResult:
                    if j[0] in c.keys():
                        c[j[0]] += c[j[0]] + float(dic[i]) / (float(j[1]) * weight[i])

        elif i == 'weight_score':
            queryCMD = f"SELECT ID, {i} FROM phones WHERE {i} <= {float(dic[i])}"
            cur.execute(queryCMD)
            queryResult = cur.fetchall()
            if len(c) == 0:
                for j in queryResult:
                    c[j[0]] = (0.1 * (float(j[1]) - float(dic[i])) + 1) * weight[i]
            else:
                for j in queryResult:
                    if j[0] in c.keys():
                        c[j[0]] += (0.1 * (float(j[1]) - float(dic[i])) + 1) * weight[i]

        elif i == 'cpu_score':
            queryCMD = f"SELECT ID, {i} FROM phones WHERE {i} <= {float(dic[i])}"
            cur.execute(queryCMD)
            queryResult = cur.fetchall()
            if len(c) == 0:
                for j in queryResult:
                    c[j[0]] = (0.1 * (float(j[1]) - float(dic[i])) + 1) * weight[i]
            else:
                for j in queryResult:
                    if j[0] in c.keys():
                        c[j[0]] += (0.1 * (float(j[1]) - float(dic[i])) + 1) * weight[i]

        else:
            queryCMD = f"SELECT ID, {i} FROM phones WHERE {i} = '{dic[i]}'"
            cur.execute(queryCMD)
            queryResult = cur.fetchall()
            if len(c) == 0:  # if start with constraint
                for j in queryResult:
                    c[j[0]] = weight[i]
            else:
                for j in queryResult:
                    if j[0] in c.keys():
                        c[j[0]] += weight[i]

    db_conn.close()
    selected_list = sorted(c.items(), key=lambda x: x[1], reverse=True)  # sorted by score
    i = 0
    answer.clear()
    score.clear()
    while len(answer) < num:
        answer.append(selected_list[i][0])
        score.append(selected_list[i][1])
        i += 1
    return answer, score


def getInfo(idList):
    """query database using calculated score"""
    db_conn = sql.connect(db_name)
    cur = db_conn.cursor()
    result = []
    for i in idList:
        queryCMD = f"SELECT * FROM phones where id = {i}"
        cur.execute(queryCMD)
        fetched_value = cur.fetchone()
        result.append(fetched_value)
    db_conn.close()
    return result


if __name__ == "__main__":
    case = {"price": 500, "have_5G": 1, "cpu_score": 7, "endurance_version": 1}
    testid, testscore = getId(case, 3, weight_video)
    result = getInfo(testid)
    # dic = {'Price': 300}
    # er = getId(dic)
    print(testid)
    print(result)
    print()
