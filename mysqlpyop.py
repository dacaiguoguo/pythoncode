#!/usr/bin/env python
# -*- coding: utf-8 -*-
# hanhan load
import MySQLdb
import json

file_object = open('dt_questionover.json')
all_the_text = file_object.read()
jsonArray = json.loads(all_the_text)
conn = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = '511guoguoMysql',
        db = 'books',
        charset="utf8"
    )
f = open('/Users/sunyanguo/thefile.txt', 'w')

cur = conn.cursor()
# odic = jsonArray[0]
for odic in jsonArray:
    bstring = r"INSERT INTO `dt_question` (`id`, `course`, `question_id`, `chapter`, `category`, `type`, `cert_type`, `question`, `media_type`, `media`, `option_a`, `option_b`, `option_c`, `option_d`, `answer`, `difficulty`, `comments`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s');" % (odic['id'],odic['course'],odic['question_id'],odic['chapter'],odic['category'],odic['type'],odic['cert_type'],odic['question'],odic['media_type'],odic['media'],odic['option_a'],odic['option_b'],odic['option_c'],odic['option_d'],odic['answer'],odic['difficulty'],odic['comments'])
    # print bstring
    f.write(bstring.encode('utf-8'))
    f.write('\n')
#     cur.execute(bstring)
# cur.close()
# conn.commit()
# conn.close()
f.close()
file_object.close()