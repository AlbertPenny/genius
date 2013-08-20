#encoding:utf-8
from scseg.digital import chinese_to_number

def test_chinese_to_number():
    test_dig = [(u'九',9),
            (u'十一',11),
            (u'一百二十三',123),
            (u'一千二百零三',1203),
            (u'一万一千一百零一',11101),
            (u'十万零三千六百零九',103609),
            (u'一百二十三万四千五百六十七',1234567),
            (u'一千一百二十三万四千五百六十七',11234567),
            (u'一亿一千一百二十三万四千五百六十七',111234567),
            (u'一百零二亿五千零一万零一千零三十八',10250011038),
            (u'一千一百一十一亿一千一百二十三万四千五百六十七',111111234567),
            (u'一兆一千一百一十一亿一千一百二十三万四千五百六十七',1111111234567),
            ]
    for test in test_dig:
        assert chinese_to_number(test[0])==test[1]
