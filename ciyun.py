import jieba
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt

# 将qqspider生成的图片生成词云
def create_word_cloud(filename):
    text = open("{}.txt".format(filename), encoding='utf-8').read()
    # 结巴分词
    wordlist = jieba.cut(text, cut_all=True)
    wl = "".join(wordlist)
    print(wl)
    bac_img=plt.imread('xiong.jpg')
    # 设置词云
    wc = WordCloud(
        # 设置背景颜色
        background_color="white",
        # 背景图片
        mask=bac_img,
         # 设置最大显示的词云数
       max_words=2000,
         # 这种字体都在电脑字体中，一般路径
       font_path='/Users/tanchengjun/Library/Fonts/SourceHanSansCN-Medium.otf',
        #  设置停用词
        stopwords=STOPWORDS,
        # 设置字体最大值
       max_font_size=150,
        # 设置字体最小值
       # min_font_size=8,
     # 设置有多少种随机生成状态，即有多少种配色方案
       random_state=30,
        # height=1600,
        # width=1100
    )

    myword = wc.generate(wl)  # 生成词云
    img_colors=ImageColorGenerator(bac_img)
    wc.recolor(color_func=img_colors)
    # 展示词云图
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file('meiyiling.png')  # 把词云保存下

if __name__ == '__main__':
   create_word_cloud('meiyiling')

