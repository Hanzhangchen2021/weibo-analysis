
### This document is used to create a word cloud

import wordcloud
import pickle

content_comment = pickle.load(open('Agu.pkl', 'rb'))
'''
Content-based word cloud
'''
content = ''
comment = ''
print(len(content_comment))
for i in content_comment:
    print(i)
    print(i[1])
    content += (' ' + ' '.join(i[1]))
    try:
        for j in i[3:]:
            comment += (' ' + ' '.join(j))
    except:
        continue
w = wordcloud.WordCloud(width=1000, font_path='/System/Library/Fonts/PingFang.ttc', background_color='white', height=700, stopwords={"知道", "觉得", "中国", "国家", "评论", "大家", "所有", "必须", "之前", "需要", "哈哈哈", "哈哈哈哈", "真的", "这种", "没有", "不会", "起来", "一点", "已经", "啊啊啊", "可能", "今天", "现在", "很多", "出来", "关注", "链接", "网页", "网页链接","日","月","目前","还","都","说","人","去","。","上","不","没","0","吃", "情况", "近","都","不""看","完","很","好","看"})
w.generate(content.strip())
w.to_file('jinkou_content.png')

