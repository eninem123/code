import json


json_data1={
  "bscode": "1",
  "code": 1,
  "data": {
    "frees": [
      {
        "ls": [
          {
            "timesinfo": "",
            "id": 1,
            "name": "卡介苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 0,
            "end_age": 3,
            "pandemic": "结核病(结核性脑膜炎、栗粒性肺结核)",
            "month_info": "出生当天",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          },
          {
            "timesinfo": "第1次",
            "id": 2,
            "name": "乙肝疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 0,
            "end_age": 3,
            "pandemic": "乙型病毒性肝炎(乙肝)",
            "month_info": "出生当天",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          }
        ],
        "minfo": "出生当天"
      },
      {
        "ls": [
          {
            "timesinfo": "第2次",
            "id": 3,
            "name": "乙肝疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 23,
            "end_age": 65,
            "pandemic": "乙型病毒性肝炎(乙肝)",
            "month_info": "1月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          }
        ],
        "minfo": "1月龄"
      },
      {
        "ls": [
          {
            "timesinfo": "第1次",
            "id": 19,
            "name": "脊灰灭活疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 54,
            "end_age": 95,
            "pandemic": "脊髓灰质炎(小儿麻痹症)",
            "month_info": "2月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          }
        ],
        "minfo": "2月龄"
      },
      {
        "ls": [
          {
            "timesinfo": "第1次",
            "id": 6,
            "name": "脊髓灰质炎口服疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 85,
            "end_age": 126,
            "pandemic": "脊髓灰质炎(小儿麻痹症)",
            "month_info": "3月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          },
          {
            "timesinfo": "第1次",
            "id": 8,
            "name": "百白破疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 85,
            "end_age": 126,
            "pandemic": "百日咳、白喉、破伤风",
            "month_info": "3月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          }
        ],
        "minfo": "3月龄"
      },
      {
        "ls": [
          {
            "timesinfo": "第2次",
            "id": 7,
            "name": "脊髓灰质炎口服疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 115,
            "end_age": 156,
            "pandemic": "脊髓灰质炎(小儿麻痹症)",
            "month_info": "4月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          },
          {
            "timesinfo": "第2次",
            "id": 9,
            "name": "百白破疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 115,
            "end_age": 156,
            "pandemic": "百日咳、白喉、破伤风",
            "month_info": "4月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          }
        ],
        "minfo": "4月龄"
      },
      {
        "ls": [
          {
            "timesinfo": "第3次",
            "id": 10,
            "name": "百白破疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 145,
            "end_age": 186,
            "pandemic": "百日咳、白喉、破伤风",
            "month_info": "5月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          }
        ],
        "minfo": "5月龄"
      },
      {
        "ls": [
          {
            "timesinfo": "第3次",
            "id": 4,
            "name": "乙肝疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 176,
            "end_age": 217,
            "pandemic": "乙型病毒性肝炎(乙肝）",
            "month_info": "6月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          },
          {
            "timesinfo": "第1次",
            "id": 13,
            "name": "A群流脑疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 176,
            "end_age": 217,
            "pandemic": "流行性脑脊髓膜炎(流脑)",
            "month_info": "6月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          }
        ],
        "minfo": "6月龄"
      },
      {
        "ls": [
          {
            "timesinfo": "第1次",
            "id": 23,
            "name": "麻风疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 237,
            "end_age": 278,
            "pandemic": "麻疹，风疹",
            "month_info": "8月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          },
          {
            "timesinfo": "第1次",
            "id": 26,
            "name": "乙脑减毒活疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 237,
            "end_age": 278,
            "pandemic": "乙型脑炎",
            "month_info": "8月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          }
        ],
        "minfo": "8月龄"
      },
      {
        "ls": [
          {
            "timesinfo": "第2次",
            "id": 14,
            "name": "A群流脑疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 267,
            "end_age": 308,
            "pandemic": "流行性脑脊髓膜炎(流脑)",
            "month_info": "9月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 1
          }
        ],
        "minfo": "9月龄"
      },
      {
        "ls": [
          {
            "timesinfo": "第4次",
            "id": 11,
            "name": "百白破疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 541,
            "end_age": 764,
            "pandemic": "百日咳、白喉、破伤风",
            "month_info": "18月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 0
          },
          {
            "timesinfo": "第1次",
            "id": 24,
            "name": "麻风腮三联疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 541,
            "end_age": 582,
            "pandemic": "麻疹、腮腺炎和风疹",
            "month_info": "18月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 0
          },
          {
            "timesinfo": "",
            "id": 28,
            "name": "甲肝减毒活疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 541,
            "end_age": 582,
            "pandemic": "甲型肝炎",
            "month_info": "18月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 0
          }
        ],
        "minfo": "18月龄"
      },
      {
        "ls": [
          {
            "timesinfo": "第2次",
            "id": 27,
            "name": "乙脑减毒活疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 723,
            "end_age": 764,
            "pandemic": "乙型脑炎",
            "month_info": "24月龄",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 0
          }
        ],
        "minfo": "24月龄"
      },
      {
        "ls": [
          {
            "timesinfo": "第1次",
            "id": 29,
            "name": "A+C流脑疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 1088,
            "end_age": 1129,
            "pandemic": "流行性脑脊髓膜炎(流脑)",
            "month_info": "3岁",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 0
          }
        ],
        "minfo": "3岁"
      },
      {
        "ls": [
          {
            "timesinfo": "第3次",
            "id": 5,
            "name": "脊髓灰质炎口服疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 1445,
            "end_age": 1495,
            "pandemic": "脊髓灰质炎(小儿麻痹症)",
            "month_info": "4岁",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 0
          }
        ],
        "minfo": "4岁"
      },
      {
        "ls": [
          {
            "timesinfo": "第1次",
            "id": 12,
            "name": "白破疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 2182,
            "end_age": 2223,
            "pandemic": "白喉、破伤风",
            "month_info": "6岁",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 0
          },
          {
            "timesinfo": "第2次",
            "id": 25,
            "name": "麻风腮三联疫苗",
            "is_free": 0,
            "is_must": 1,
            "start_age": 2182,
            "end_age": 2223,
            "pandemic": "麻疹、腮腺炎和风疹",
            "month_info": "6岁",
            "stime": "",
            "is_inoculation": 0,
            "sid": 0,
            "isable": 1,
            "isadd": 0,
            "isapplies": 0
          }
        ],
        "minfo": "6岁"
      }
    ]
  },
  "msg": "操作成功"
}

json_data2 = {
    "bscode": "1",
    "code": 1,
    "data": {
        "nofrees": [
            {
                "ls": [
                    {
                        "timesinfo": "第1次",
                        "id": 15,
                        "name": "Hib结合疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 54,
                        "end_age": 95,
                        "pandemic": "b型流感嗜血杆菌感染",
                        "month_info": "2月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第1次",
                        "id": 31,
                        "name": "五联疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 54,
                        "end_age": 95,
                        "pandemic": "白喉、破伤风、百日咳、脊髓灰质炎、b型流感嗜血杆菌引起的侵入性感染（如脑膜炎、败血症、蜂窝织炎、关节炎、会厌炎等）",
                        "month_info": "2月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第1次",
                        "id": 50,
                        "name": "肺炎球菌结合疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 54,
                        "end_age": 95,
                        "pandemic": "肺炎球菌引起的肺炎、脑膜炎、中耳炎、支气管炎",
                        "month_info": "2月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    }
                ],
                "minfo": "2月龄"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第2次",
                        "id": 20,
                        "name": "脊灰灭活疫苗",
                        "is_free": 1,
                        "is_must": 1,
                        "start_age": 85,
                        "end_age": 126,
                        "pandemic": "脊髓灰质炎（小儿麻痹症）",
                        "month_info": "3月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第2次",
                        "id": 32,
                        "name": "五联疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 85,
                        "end_age": 126,
                        "pandemic": "白喉、破伤风、百日咳、脊髓灰质炎、b型流感嗜血杆菌引起的侵入性感染（如脑膜炎、败血症、蜂窝织炎、关节炎、会厌炎等）",
                        "month_info": "3月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第1次",
                        "id": 60,
                        "name": "四联疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 85,
                        "end_age": 126,
                        "pandemic": "预防百日咳、白喉、破伤风和由b型流感嗜血杆菌引起的侵袭性疾病（包括脑膜炎、肺炎、上呼吸道感染、败血症、蜂窝组织炎、关节炎、会厌炎等）。",
                        "month_info": "3月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    }
                ],
                "minfo": "3月龄"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第2次",
                        "id": 16,
                        "name": "Hib结合疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 115,
                        "end_age": 156,
                        "pandemic": "b型流感嗜血杆菌感染",
                        "month_info": "4月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第3次",
                        "id": 21,
                        "name": "脊灰灭活疫苗",
                        "is_free": 1,
                        "is_must": 1,
                        "start_age": 115,
                        "end_age": 156,
                        "pandemic": "脊髓灰质炎（小儿麻痹症）",
                        "month_info": "4月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第3次",
                        "id": 33,
                        "name": "五联疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 115,
                        "end_age": 156,
                        "pandemic": "白喉、破伤风、百日咳、脊髓灰质炎、b型流感嗜血杆菌引起的侵入性感染（如脑膜炎、败血症、蜂窝织炎、关节炎、会厌炎等）",
                        "month_info": "4月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第2次",
                        "id": 51,
                        "name": "肺炎球菌结合疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 115,
                        "end_age": 156,
                        "pandemic": "肺炎球菌引起的肺炎、脑膜炎、中耳炎、支气管炎",
                        "month_info": "4月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第2次",
                        "id": 61,
                        "name": "四联疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 115,
                        "end_age": 156,
                        "pandemic": "预防百日咳、白喉、破伤风和由b型流感嗜血杆菌引起的侵袭性疾病（包括脑膜炎、肺炎、上呼吸道感染、败血症、蜂窝组织炎、关节炎、会厌炎等）。",
                        "month_info": "4月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    }
                ],
                "minfo": "4月龄"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第3次",
                        "id": 62,
                        "name": "四联疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 145,
                        "end_age": 186,
                        "pandemic": "预防百日咳、白喉、破伤风和由b型流感嗜血杆菌引起的侵袭性疾病（包括脑膜炎、肺炎、上呼吸道感染、败血症、蜂窝组织炎、关节炎、会厌炎等）。",
                        "month_info": "5月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    }
                ],
                "minfo": "5月龄"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第3次",
                        "id": 17,
                        "name": "Hib结合疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 176,
                        "end_age": 217,
                        "pandemic": "b型流感嗜血杆菌感染",
                        "month_info": "6月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第1次",
                        "id": 45,
                        "name": "轮状病毒活疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 176,
                        "end_age": 217,
                        "pandemic": "A群轮状病毒引起的腹泻",
                        "month_info": "6月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第1次",
                        "id": 48,
                        "name": "流感疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 176,
                        "end_age": 217,
                        "pandemic": "流行性感冒",
                        "month_info": "6月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第3次",
                        "id": 52,
                        "name": "肺炎球菌结合疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 176,
                        "end_age": 217,
                        "pandemic": "肺炎球菌引起的肺炎、脑膜炎、中耳炎、支气管炎",
                        "month_info": "6月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第1次",
                        "id": 54,
                        "name": "A+C群流脑结合疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 176,
                        "end_age": 217,
                        "pandemic": "流行性脑脊髓膜炎（流脑）",
                        "month_info": "6月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第1次",
                        "id": 56,
                        "name": "EV71型手足口病疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 176,
                        "end_age": 217,
                        "pandemic": "肠道病毒71型（EV71型）感染所致的手足口病",
                        "month_info": "6月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    }
                ],
                "minfo": "6月龄"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第2次",
                        "id": 57,
                        "name": "EV71型手足口病疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 206,
                        "end_age": 247,
                        "pandemic": "肠道病毒71型（EV71型）感染所致的手足口病",
                        "month_info": "7月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第2次",
                        "id": 58,
                        "name": "流感疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 206,
                        "end_age": 247,
                        "pandemic": "流行性感冒",
                        "month_info": "7月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    }
                ],
                "minfo": "7月龄"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第1次",
                        "id": 37,
                        "name": "乙脑灭活疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 237,
                        "end_age": 278,
                        "pandemic": "流行性乙型脑炎",
                        "month_info": "8月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第2次",
                        "id": 38,
                        "name": "乙脑灭活疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 242,
                        "end_age": 278,
                        "pandemic": "流行性乙型脑炎",
                        "month_info": "8月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    }
                ],
                "minfo": "8月龄"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第2次",
                        "id": 55,
                        "name": "A+C群流脑结合疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 267,
                        "end_age": 308,
                        "pandemic": "流行性脑脊髓膜炎（流脑）",
                        "month_info": "9月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    }
                ],
                "minfo": "9月龄"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第4次",
                        "id": 18,
                        "name": "Hib结合疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 358,
                        "end_age": 399,
                        "pandemic": "b型流感嗜血杆菌感染",
                        "month_info": "12月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    },
                    {
                        "timesinfo": "第4次",
                        "id": 53,
                        "name": "肺炎球菌结合疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 358,
                        "end_age": 399,
                        "pandemic": "肺炎球菌引起的肺炎、脑膜炎、中耳炎、支气管炎",
                        "month_info": "12月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 1
                    }
                ],
                "minfo": "12月龄"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第4次",
                        "id": 22,
                        "name": "脊灰灭活疫苗",
                        "is_free": 1,
                        "is_must": 1,
                        "start_age": 541,
                        "end_age": 582,
                        "pandemic": "脊髓灰质炎（小儿麻痹症）",
                        "month_info": "18月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 0
                    },
                    {
                        "timesinfo": "第4次",
                        "id": 34,
                        "name": "五联疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 541,
                        "end_age": 582,
                        "pandemic": "白喉、破伤风、百日咳、脊髓灰质炎、b型流感嗜血杆菌引起的侵入性感染（如脑膜炎、败血症、蜂窝织炎、关节炎、会厌炎等）",
                        "month_info": "18月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 0
                    },
                    {
                        "timesinfo": "第1次",
                        "id": 35,
                        "name": "水痘疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 541,
                        "end_age": 582,
                        "pandemic": "水痘",
                        "month_info": "18月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 0
                    },
                    {
                        "timesinfo": "第1次",
                        "id": 44,
                        "name": "甲肝灭活疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 541,
                        "end_age": 582,
                        "pandemic": "甲型肝炎",
                        "month_info": "18月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 0
                    },
                    {
                        "timesinfo": "第2次",
                        "id": 46,
                        "name": "轮状病毒活疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 541,
                        "end_age": 582,
                        "pandemic": "A群轮状病毒引起的腹泻",
                        "month_info": "18月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 0
                    },
                    {
                        "timesinfo": "第4次",
                        "id": 63,
                        "name": "四联疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 541,
                        "end_age": 582,
                        "pandemic": "预防百日咳、白喉、破伤风和由b型流感嗜血杆菌引起的侵袭性疾病（包括脑膜炎、肺炎、上呼吸道感染、败血症、蜂窝组织炎、关节炎、会厌炎等）。",
                        "month_info": "18月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 0
                    }
                ],
                "minfo": "18月龄"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第3次",
                        "id": 39,
                        "name": "乙脑灭活疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 723,
                        "end_age": 764,
                        "pandemic": "流行性乙型脑炎",
                        "month_info": "24月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 0
                    },
                    {
                        "timesinfo": "第2次",
                        "id": 49,
                        "name": "甲肝灭活疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 723,
                        "end_age": 764,
                        "pandemic": "甲型肝炎",
                        "month_info": "24月龄",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 0
                    }
                ],
                "minfo": "24月龄"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第3次",
                        "id": 47,
                        "name": "轮状病毒活疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 905,
                        "end_age": 946,
                        "pandemic": "A群轮状病毒引起的腹泻",
                        "month_info": "2岁半",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 0
                    }
                ],
                "minfo": "2岁半"
            },
            {
                "ls": [
                    {
                        "timesinfo": "第2次",
                        "id": 36,
                        "name": "水痘疫苗",
                        "is_free": 1,
                        "is_must": 0,
                        "start_age": 1453,
                        "end_age": 1494,
                        "pandemic": "水痘",
                        "month_info": "4岁",
                        "stime": "",
                        "is_inoculation": 0,
                        "sid": 0,
                        "isadd": 0,
                        "isapplies": 0
                    }
                ],
                "minfo": "4岁"
            }
        ]
    },
    "msg": "操作成功"
}

json_data = json.dumps(json_data2)
data = json.loads(json_data)

for v in data['data']['nofrees']:
    for ls in v['ls'] :
        name = ls['name']
        timesinfo = ls['timesinfo']
        pandemic = ls['pandemic']
        month_info = ls['month_info']
        print(name,timesinfo,pandemic,month_info)


#匹配规则：<(?<=<)[^<>]+>