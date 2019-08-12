from flask import Blueprint
from flask import jsonify

lesson = Blueprint("lesson", __name__)


@lesson.route('/all', methods=['GET'])
def get_lessons():
    data = {
        "data": [
            {
                "lessonType": "财智书会",
                "lesson": [
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "战略成本控制",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#62888c",
                        "lessonList": [
                            {
                                "name": "战略成本控制-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/2434ca375285890781339607674/v.f210.m3u8"
                            },
                            {
                                "name": "战略成本控制-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9bd0a8705285890781446522762/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-3",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/99b469d95285890781446457098/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-4",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9bd0ad1b5285890781446522899/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-5",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9bf448f25285890781446541673/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-6",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9bf44cf05285890781446541752/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-7",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9c1bbfb95285890781446567555/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-8",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9bd11b0c5285890781446523145/v.f220.m3u8"
                            }
                        ]
                    },
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "什么才是真正的财务思维",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#f4f4f4",
                        "lessonList": [
                            {
                                "name": "什么才是真正的财务思维-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/a591cd155285890781446982370/v.f210.m3u8"
                            },
                            {
                                "name": "什么才是真正的财务思维-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/a31b39bc5285890781446867564/v.f210.m3u8"
                            },
                            {
                                "name": "什么才是真正的财务思维-3",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/a31b3d5b5285890781446867617/v.f210.m3u8"
                            },
                            {
                                "name": "什么才是真正的财务思维-4",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/a31b41b95285890781446867723/v.f210.m3u8"
                            },
                            {
                                "name": "什么才是真正的财务思维-5",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/a52780765285890781446926841/v.f210.m3u8"
                            }
                        ]
                    },
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "内向性格竞争力",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#e4ab4f",
                        "lessonList": [
                            {
                                "name": "内向性格竞争力-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd22256c5285890781447024418/v.f210.m3u8"
                            },
                            {
                                "name": "内向性格竞争力-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd2226525285890781447024487/v.f210.m3u8"
                            },
                            {
                                "name": "内向性格竞争力-3",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd222a8c5285890781447024580/v.f210.m3u8"
                            },
                            {
                                "name": "内向性格竞争力-4",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd222e8f5285890781447024664/v.f210.m3u8"
                            },
                            {
                                "name": "内向性格竞争力-5",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd22368b5285890781447024822/v.f210.m3u8"
                            },
                            {
                                "name": "内向性格竞争力-6",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd223a8d5285890781447024905/v.f210.m3u8"
                            }
                        ]
                    },
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "私募股权圣经",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#9f2e3c",
                        "lessonList": [
                            {
                                "name": "私募股权圣经-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd22c2eb5285890781447025821/v.f210.m3u8"
                            },
                            {
                                "name": "私募股权圣经-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd22c74f5285890781447025933/v.f210.m3u8"
                            },
                            {
                                "name": "私募股权圣经-3",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df5184ca5285890781447101726/v.f210.m3u8"
                            },
                            {
                                "name": "私募股权圣经-4",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df51894e5285890781447101847/v.f210.m3u8"
                            },
                            {
                                "name": "私募股权圣经-5",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd23326c5285890781447026191/v.f210.m3u8"
                            }
                        ]
                    },
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "高难度谈话",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#d4d4d4",
                        "lessonList": [
                            {
                                "name": "高难度谈话-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df5294e85285890781447103515/v.f210.m3u8"
                            },
                            {
                                "name": "高难度谈话-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df5564dd5285890781447108999/v.f210.m3u8"
                            },
                            {
                                "name": "高难度谈话-3",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df55ceca5285890781447109160/v.f210.m3u8"
                            },
                            {
                                "name": "高难度谈话-4",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df52a20a5285890781447103841/v.f210.m3u8"
                            }
                        ]
                    },
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "精进：如何成为一个很厉害的人",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#d4d4d4",
                        "lessonList": [
                            {
                                "name": "精进：如何成为一个很厉害的人-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/e1e0d5f95285890781447238919/v.f210.m3u8"
                            },
                            {
                                "name": "精进：如何成为一个很厉害的人-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df6528a35285890781447114103/v.f210.m3u8"
                            },
                            {
                                "name": "精进：如何成为一个很厉害的人-3",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/e1e1402d5285890781447239105/v.f210.m3u8"
                            },
                            {
                                "name": "精进：如何成为一个很厉害的人-4",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dfd13c705285890781447173435/v.f210.m3u8"
                            },
                            {
                                "name": "精进：如何成为一个很厉害的人-5",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dfd140b05285890781447173534/v.f210.m3u8"
                            },
                            {
                                "name": "精进：如何成为一个很厉害的人-6",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dfd141555285890781447173584/v.f210.m3u8"
                            }
                        ]
                    }
                ]
            },
            {
                "lessonType": "财智书会2",
                "lesson": [
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "战略成本控制2222",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#dddddd",
                        "lessonList": [
                            {
                                "name": "战略成本控制-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/2434ca375285890781339607674/v.f210.m3u8"
                            },
                            {
                                "name": "战略成本控制-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9bd0a8705285890781446522762/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-3",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/99b469d95285890781446457098/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-4",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9bd0ad1b5285890781446522899/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-5",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9bf448f25285890781446541673/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-6",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9bf44cf05285890781446541752/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-7",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9c1bbfb95285890781446567555/v.f220.m3u8"
                            },
                            {
                                "name": "战略成本控制-8",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/9bd11b0c5285890781446523145/v.f220.m3u8"
                            }
                        ]
                    },
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "什么才是真正的财务思维",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#dddddd",
                        "lessonList": [
                            {
                                "name": "什么才是真正的财务思维-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/a591cd155285890781446982370/v.f210.m3u8"
                            },
                            {
                                "name": "什么才是真正的财务思维-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/a31b39bc5285890781446867564/v.f210.m3u8"
                            }
                        ]
                    },
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "内向性格竞争力",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#e4ab4f",
                        "lessonList": [
                            {
                                "name": "内向性格竞争力-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd22256c5285890781447024418/v.f210.m3u8"
                            },
                            {
                                "name": "内向性格竞争力-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd2226525285890781447024487/v.f210.m3u8"
                            },
                            {
                                "name": "内向性格竞争力-3",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd222a8c5285890781447024580/v.f210.m3u8"
                            },
                            {
                                "name": "内向性格竞争力-4",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd222e8f5285890781447024664/v.f210.m3u8"
                            },
                            {
                                "name": "内向性格竞争力-5",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd22368b5285890781447024822/v.f210.m3u8"
                            },
                            {
                                "name": "内向性格竞争力-6",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd223a8d5285890781447024905/v.f210.m3u8"
                            }
                        ]
                    },
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "私募股权圣经",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#dddddd",
                        "lessonList": [
                            {
                                "name": "私募股权圣经-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd22c2eb5285890781447025821/v.f210.m3u8"
                            },
                            {
                                "name": "私募股权圣经-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd22c74f5285890781447025933/v.f210.m3u8"
                            },
                            {
                                "name": "私募股权圣经-3",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df5184ca5285890781447101726/v.f210.m3u8"
                            },
                            {
                                "name": "私募股权圣经-4",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df51894e5285890781447101847/v.f210.m3u8"
                            },
                            {
                                "name": "私募股权圣经-5",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dd23326c5285890781447026191/v.f210.m3u8"
                            }
                        ]
                    },
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "高难度谈话",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#5a524c",
                        "lessonList": [
                            {
                                "name": "高难度谈话-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df5294e85285890781447103515/v.f210.m3u8"
                            },
                            {
                                "name": "高难度谈话-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df5564dd5285890781447108999/v.f210.m3u8"
                            },
                            {
                                "name": "高难度谈话-3",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df55ceca5285890781447109160/v.f210.m3u8"
                            },
                            {
                                "name": "高难度谈话-4",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df52a20a5285890781447103841/v.f210.m3u8"
                            }
                        ]
                    },
                    {
                        "pic": "http://www.ecfo.com.cn/img2/elevenV.png",
                        "lessonTitle": "精进：如何成为一个很厉害的人",
                        "lessonTeacher": "eleven",
                        "lessonColor": "#aaaaaa",
                        "lessonList": [
                            {
                                "name": "精进：如何成为一个很厉害的人-1",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/e1e0d5f95285890781447238919/v.f210.m3u8"
                            },
                            {
                                "name": "精进：如何成为一个很厉害的人-2",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/df6528a35285890781447114103/v.f210.m3u8"
                            },
                            {
                                "name": "精进：如何成为一个很厉害的人-3",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/e1e1402d5285890781447239105/v.f210.m3u8"
                            },
                            {
                                "name": "精进：如何成为一个很厉害的人-4",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dfd13c705285890781447173435/v.f210.m3u8"
                            },
                            {
                                "name": "精进：如何成为一个很厉害的人-5",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dfd140b05285890781447173534/v.f210.m3u8"
                            },
                            {
                                "name": "精进：如何成为一个很厉害的人-6",
                                "length": "7:40",
                                "url": "http://media.ecfo.cn/43c7b66fvodtransgzp1251278716/dfd141555285890781447173584/v.f210.m3u8"
                            }
                        ]
                    }
                ]
            }
        ],
        "code": 200,
        "message": "success"
    }
    return jsonify(data)
