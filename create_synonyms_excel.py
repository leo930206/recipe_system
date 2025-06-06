import pandas as pd

# 你的同義詞字典
synonyms_map = {
    "蒜頭": [
        "蒜頭", "蒜", "大蒜", "蒜瓣", "蒜末",
        "蒜泥", "蒜蓉", "蒜汁", "白蒜", "紫皮蒜",
        "京蒜", "蒜仁", "整顆蒜", "蒜粉", "蒜酥",
        "烤蒜", "蒜苔", "蒜苗", "肉蒜", "生蒜"
    ],
    "蒜": [
        "蒜頭", "蒜", "大蒜", "蒜瓣", "蒜末",
        "蒜泥", "蒜蓉", "蒜汁", "白蒜", "紫皮蒜",
        "京蒜", "蒜仁", "整顆蒜", "蒜粉", "蒜酥",
        "烤蒜", "蒜苔", "蒜苗", "肉蒜", "生蒜"
    ],
    "大蒜": [
        "蒜頭", "蒜", "大蒜", "蒜瓣", "蒜末",
        "蒜泥", "蒜蓉", "蒜汁", "白蒜", "紫皮蒜",
        "京蒜", "蒜仁", "整顆蒜", "蒜粉", "蒜酥",
        "烤蒜", "蒜苔", "蒜苗", "肉蒜", "生蒜"
    ],
    "薑": [
        "薑", "老薑", "嫩薑", "薑末", "薑泥",
        "薑絲", "薑片", "生薑", "子薑", "粉薑",
        "薑黃", "薑黃塊", "薑粉", "薑蓉", "薑汁",
        "泰國薑", "乾薑", "薑母", "薑芽", "野薑"
    ],
    "辣椒": [
        "辣椒", "紅辣椒", "青辣椒", "指天椒", "小辣椒",
        "野山椒", "泡椒", "辣椒絲",
        "辣椒碎", "乾辣椒", "辣椒片", "剁椒", "虎皮椒",
        "辣椒油", "朝天椒", "香辣椒"
    ],
    "雞肉": [
        "雞肉", "雞胸肉", "雞腿肉", "去骨雞腿", "雞翅",
        "雞里肌", "土雞肉", "雞全腿", "雞丁", "雞排",
        "柴雞", "走地雞", "烤雞肉", "熏雞肉", "水煮雞",
        "雞絲", "炸雞塊", "滷雞肉", "燉雞肉", "雞扒"
    ],
    "牛肉": [
        "牛肉", "牛腩", "牛肋條", "牛小排", "沙朗牛排",
        "牛絞肉", "雪花牛", "牛腱心", "菲力牛排", "肋眼牛排",
        "牛肉絲", "牛肉片", "牛肉條", "嫩肩牛", "黃牛肉",
        "水牛肉", "乾煸牛肉", "燒牛肉", "牛肉丁", "炙燒牛肉"
    ],
    "豬肉": [
        "豬肉", "五花肉", "三層肉", "豬絞肉", "豬梅花",
        "里肌肉", "豬肩肉", "黑毛豬肉", "豬肋排", "松阪豬",
        "培根", "煙燻培根", "豬肉絲", "豬肉片", "豬肉塊",
        "豬里肌", "豬頸肉", "豬腿肉", "滷肉", "燒肉"
    ],
    "洋蔥": [
        "洋蔥", "紅洋蔥", "黃洋蔥", "白洋蔥", "紫洋蔥",
        "小洋蔥", "洋蔥絲", "洋蔥末", "洋蔥丁", "洋蔥圈",
        "脆洋蔥", "烤洋蔥", "炸洋蔥", "焦糖洋蔥", "青洋蔥",
        "大洋蔥", "洋蔥粒", "洋蔥粒", "生洋蔥", "甜洋蔥"
    ],
    "高麗菜": [
        "高麗菜", "包心菜", "捲心菜", "大頭菜", "捲白菜",
        "高麗捲", "球莖甘藍", "甘藍菜", "洋白菜", "娃娃菜",
        "紫高麗菜", "紫甘藍", "圓白菜", "高麗菜片", "高麗菜絲",
        "高麗菜梗", "高麗菜葉", "炒高麗菜", "醃高麗菜", "切絲高麗菜"
    ],
    "番茄": [
        "番茄", "蕃茄", "西紅柿", "牛番茄", "小番茄",
        "聖女番茄", "番茄塊", "番茄丁", "番茄片", "番茄泥",
        "番茄醬", "番茄糊", "番茄汁", "番茄沙司", "烤番茄",
        "晒番茄", "蕃茄乾", "黃番茄", "有機番茄", "甜番茄"
    ],
    "馬鈴薯": [
        "馬鈴薯", "土豆", "洋芋", "薯仔", "馬鈴薯塊",
        "馬鈴薯片", "馬鈴薯絲", "馬鈴薯泥", "粉心馬鈴薯", "黃心馬鈴薯",
        "炸薯條", "薯泥球", "薯角", "洋芋片", "薯絲煎餅",
        "新馬鈴薯", "小馬鈴薯", "甘藷馬鈴薯", "麻辣薯塊", "培根馬鈴薯"
    ],
    "土豆": [
        "馬鈴薯", "土豆", "洋芋", "薯仔", "馬鈴薯塊",
        "馬鈴薯片", "馬鈴薯絲", "馬鈴薯泥", "粉心馬鈴薯", "黃心馬鈴薯",
        "炸薯條", "薯泥球", "薯角", "洋芋片", "薯絲煎餅",
        "新馬鈴薯", "小馬鈴薯", "甘藷馬鈴薯", "麻辣薯塊", "培根馬鈴薯"
    ],
    "胡蘿蔔": [
        "胡蘿蔔", "紅蘿蔔", "蘿蔔仔", "胡蘿蔔條", "胡蘿蔔塊",
        "胡蘿蔔絲", "胡蘿蔔丁", "胡蘿蔔泥", "嫩胡蘿蔔", "彩色胡蘿蔔",
        "紅蘿蔔絲", "紅蘿蔔片", "黃蘿蔔", "橙蘿蔔", "紫蘿蔔",
        "蘿蔔花", "脆蘿蔔", "甜蘿蔔", "烤胡蘿蔔", "白胡蘿蔔","紅蘿蔔塊"
    ],
    "紅蘿蔔": [
        "胡蘿蔔", "紅蘿蔔", "蘿蔔仔", "胡蘿蔔條", "胡蘿蔔塊",
        "胡蘿蔔絲", "胡蘿蔔丁", "胡蘿蔔泥", "嫩胡蘿蔔", "彩色胡蘿蔔",
        "紅蘿蔔絲", "紅蘿蔔片", "黃蘿蔔", "橙蘿蔔", "紫蘿蔔",
        "蘿蔔花", "脆蘿蔔", "甜蘿蔔", "烤胡蘿蔔", "白胡蘿蔔","紅蘿蔔塊"
    ],
    "紅蘿蔔塊": [
        "胡蘿蔔塊","紅蘿蔔塊"
    ],
    "胡蘿蔔塊": [
        "紅蘿蔔塊","胡蘿蔔塊"
    ],
    "青蔥": [
        "青蔥", "蔥", "蔥白", "蔥綠", "蔥段",
        "蔥花", "蔥絲", "小蔥", "大蔥", "細蔥",
        "蔥苗", "京蔥", "大葱", "香葱", "青蔥粒",
        "烤蔥", "油蔥", "蔥爆", "法式蔥", "蘇格蘭蔥"
    ],
    "蔥": [
        "青蔥", "蔥", "蔥白", "蔥綠", "蔥段",
        "蔥花", "蔥絲", "小蔥", "大蔥", "細蔥",
        "蔥苗", "京蔥", "大葱", "香葱", "青蔥粒",
        "烤蔥", "油蔥", "蔥爆", "法式蔥", "蘇格蘭蔥"
    ],
    "花椰菜": [
        "花椰菜", "青花椰", "綠花椰", "綠花椰菜", "青花菜",
        "白花椰菜", "紫花椰菜", "花椰球", "羅馬花椰菜", "菜花",
        "菜花朵", "花椰菜梗", "花椰菜碎", "花椰菜丁", "烤花椰菜",
        "炸花椰菜", "香料花椰菜", "奶油花椰菜", "蒜香花椰菜", "炸脆花椰"
    ],
    "香菇": [
        "香菇", "冬菇", "花菇", "乾香菇", "香菇絲",
        "香菇片", "香菇丁", "香菇碎", "香菇蓉", "香菇根",
        "香菇朵", "炙香菇", "滷香菇", "鮮香菇", "黑香菇",
        "香菇醬", "香菇粉", "金香菇", "破菇", "小香菇"
    ],
    "菇": [
        "香菇", "冬菇", "花菇", "乾香菇", "香菇絲",
        "香菇片", "香菇丁", "香菇碎", "香菇蓉", "香菇根",
        "香菇朵", "炙香菇", "滷香菇", "鮮香菇", "黑香菇",
        "香菇醬", "香菇粉", "金香菇", "破菇", "小香菇"
    ],
    "蘑菇": [
        "蘑菇", "白蘑菇", "洋菇", "蘑菇片", "蘑菇丁",
        "褐色蘑菇", "鮮蘑菇", "乾蘑菇", "金蘑菇", "香蘑菇",
        "義大利蘑菇", "牛肝菌", "松茸", "杏鮑菇", "鴻禧菇",
        "雪白菇", "鴛鴦菇", "魔菇", "磨菇", "迷你蘑菇"
    ],
    "玉米": [
        "玉米", "玉米粒", "甜玉米", "爆米花玉米", "糯玉米",
        "甜玉米粒", "黃玉米", "白玉米", "玉米芯", "玉米筍",
        "玉米片", "玉米粉", "玉米澱粉", "玉米碎", "玉米絲",
        "炒玉米", "燙玉米", "烤玉米", "焗烤玉米", "爆米花"
    ],
    "米": [
        "米", "白米", "糙米", "珍珠米", "壽司米",
        "長糯米", "在來米", "泰國香米", "巴斯馬蒂米", "糯米",
        "黑糯米", "紫米", "紅米", "黃金米", "五穀米",
        "十穀米", "紅藜麥米", "有機米", "香米", "老米"
    ],
    "麵粉": [
        "麵粉", "中筋麵粉", "高筋麵粉", "低筋麵粉", "通用麵粉",
        "全麥麵粉", "全穀麵粉", "蛋糕粉", "麵包粉", "餃子粉",
        "麵糊粉", "天婦羅粉", "炸粉", "義大利麵粉", "披薩粉",
        "膳食纖維粉", "藜麥粉", "米麩粉", "燕麥粉", "自發粉"
    ],
    "蛋": [
        "蛋", "雞蛋", "鴨蛋", "鵝蛋", "鵪鶉蛋",
        "皮蛋", "松花蛋", "鹹蛋", "蛋黃", "蛋白",
        "全蛋", "生蛋", "熟蛋", "溏心蛋", "滷蛋",
        "茶葉蛋", "水煮蛋", "蛋液", "蛋絲", "蛋碎"
    ],
    "雞蛋": [
        "蛋", "雞蛋", "鴨蛋", "鵝蛋", "鵪鶉蛋",
        "皮蛋", "松花蛋", "鹹蛋", "蛋黃", "蛋白",
        "全蛋", "生蛋", "熟蛋", "溏心蛋", "滷蛋",
        "茶葉蛋", "水煮蛋", "蛋液", "蛋絲", "蛋碎"
    ],
    "牛奶": [
        "牛奶", "鮮奶", "全脂牛奶", "低脂牛奶", "脫脂牛奶",
        "調味乳", "煉乳", "奶粉", "奶精", "奶水",
        "乳飲料", "草莓牛奶", "巧克力牛奶", "高鈣牛奶", "優酪乳",
        "優格", "酸奶", "希臘優格", "奶昔", "豆奶"
    ],
    "醬油": [
        "醬油", "生抽", "老抽", "醬油膏", "薄鹽醬油",
        "濃口醬油", "淡口醬油", "特級醬油", "醬油汁", "醬汁",
        "味極鮮", "海鮮醬油", "蒸魚豉油", "壺底油", "油膏",
        "滷汁", "醬油露", "蔭油", "日式醬油", "台式醬油"
    ],
    "糖": [
        "糖", "白糖", "砂糖", "冰糖", "二砂糖",
        "紅糖", "黃糖", "黑糖", "糖粉", "糖霜",
        "糖漿", "果糖", "棕櫚糖", "椰糖", "麥芽糖",
        "楓糖", "蜂蜜", "龍眼蜜", "葡萄糖", "甜味劑"
    ],
    "砂糖": [
        "糖", "白糖", "砂糖", "冰糖", "二砂糖",
        "紅糖", "黃糖", "黑糖", "糖粉", "糖霜",
        "糖漿", "果糖", "棕櫚糖", "椰糖", "麥芽糖",
        "楓糖", "蜂蜜", "龍眼蜜", "葡萄糖", "甜味劑"
    ],
    "鹽": [
        "鹽", "食鹽", "海鹽", "岩鹽", "玫瑰鹽",
        "黑鹽", "喜馬拉雅粉鹽", "粗鹽", "細鹽", "調味鹽",
        "低鈉鹽", "香草鹽", "柚子鹽", "抹茶鹽", "竹鹽",
        "蘑菇鹽", "烟燻鹽", "義式香料鹽", "檸檬鹽", "松露鹽"
    ],
    "食鹽": [
        "鹽", "食鹽", "海鹽", "岩鹽", "玫瑰鹽",
        "黑鹽", "喜馬拉雅粉鹽", "粗鹽", "細鹽", "調味鹽",
        "低鈉鹽", "香草鹽", "柚子鹽", "抹茶鹽", "竹鹽",
        "蘑菇鹽", "烟燻鹽", "義式香料鹽", "檸檬鹽", "松露鹽"
    ],
    "胡椒": [
        "胡椒", "白胡椒", "黑胡椒", "花椒", "青胡椒",
        "黑胡椒粒", "白胡椒粉", "黑胡椒粉", "花椒粉", "花椒粒",
        "粗胡椒", "細胡椒", "五香胡椒", "四季胡椒", "綜合胡椒",
        "咖哩胡椒", "爆香胡椒", "麻椒", "川椒", "鹽酥胡椒"
    ],
    "油": [
        "油", "食用油", "沙拉油", "大豆油", "葵花油",
        "橄欖油", "花生油", "玉米油", "菜籽油", "葡萄籽油",
        "棕櫚油", "椰子油", "麻油", "芝麻油", "香油",
        "辣椒油", "花椒油", "牛油", "豬油", "奶油"
    ],
    "食用油": [
        "油", "食用油", "沙拉油", "大豆油", "葵花油",
        "橄欖油", "花生油", "玉米油", "菜籽油", "葡萄籽油",
        "棕櫚油", "椰子油", "麻油", "芝麻油", "香油",
        "辣椒油", "花椒油", "牛油", "豬油", "奶油"
    ],
    "香菜": [
        "香菜", "芫荽", "羌仔菜", "香草", "芫荽葉",
        "香草葉", "歐芫荽", "胡荽", "香料葉", "新鮮香菜",
        "香菜末", "香菜梗", "香菜根", "切碎香菜", "墨西哥香菜",
        "越南香菜", "滷味香菜", "香菜苗", "香菜枝", "香綠葉"
    ]
}

# 將字典轉換成 DataFrame，每一筆資料包含 key 與其同義詞字串（以逗號分隔）
rows = []
for key, syn_list in synonyms_map.items():
    rows.append({
        "key": key,
        "synonyms": ", ".join(syn_list)
    })

df_syn = pd.DataFrame(rows)

# 輸出成 Excel 檔案，檔名為 synonyms.xlsx
df_syn.to_excel("synonyms.xlsx", index=False)

print("已成功產生 synonyms.xlsx")
