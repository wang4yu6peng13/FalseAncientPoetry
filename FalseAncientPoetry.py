#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Inspired By Weibo @戈多大王的小号
Ruby By Weibo @程序员Delton

@two_chars_words = %w"朱砂 天下 杀伐 人家 韶华 风华 繁华 血染 墨染 白衣 素衣 嫁衣 倾城 孤城 空城 旧城 旧人 伊人 心疼 春风 古琴 无情 迷离 奈何 断弦 焚尽 散乱 陌路 乱世 笑靥 浅笑 明眸 轻叹 烟火 一生 三生 浮生 桃花 梨花 落花 烟花 离殇 情殇 爱殇 剑殇 灼伤 仓皇 匆忙 陌上 清商 焚香 墨香 微凉 断肠 痴狂 凄凉 黄梁 未央 成双 无恙 虚妄 凝霜 洛阳 长安 江南 忘川 千年 纸伞 烟雨 回眸 公子 红尘 红颜 红衣 红豆 红线 青丝 青史 青冢 白发 白首 白骨 黄土 黄泉 碧落 紫陌"
@four_chars_words = %w"情深缘浅 情深不寿 莫失莫忘 阴阳相隔 如花美眷 似水流年 眉目如画 曲终人散 繁华落尽 不诉离殇 一世长安"
@sentence_model = %w"xx，xx，xx了xx。 xxxx，xxxx，不过是一场xxxx。 你说xxxx，我说xxxx，最后不过xxxx。 xx，xx，许我一场xxxx。 一x一x一xx，半x半x半xx。 你说xxxxxxxx，后来xxxxxxxx。 xxxx，xxxx，终不敌xxxx。"

def get_sentence
  model = @sentence_model.sample(1)[0].clone
  while model.include?'xxxx'
    model.sub!(/xxxx/, @four_chars_words.sample(1)[0])
  end
  while model.include?'xx'
    model.sub!(/xx/, @two_chars_words.sample(1)[0])
  end
  while model.include?'x'
    model.sub!(/x/, @two_chars_words.sample(1)[0][rand(0..1)])
  end
  puts model
end

while true
  get_sentence
  sleep 1
end
'''

# Python(Rewrite) by Weibo @雨棚Lemon

import random

two_chars_words = "朱砂 天下 杀伐 人家 韶华 风华 繁华 血染 墨染 白衣 素衣 嫁衣 倾城 孤城 空城 旧城 旧人 伊人 心疼 春风 古琴 无情 迷离 奈何 断弦 焚尽 散乱 陌路 乱世 笑靥 浅笑 明眸 轻叹 烟火 一生 三生 浮生 桃花 梨花 落花 烟花 离殇 情殇 爱殇 剑殇 灼伤 仓皇 匆忙 陌上 清商 焚香 墨香 微凉 断肠 痴狂 凄凉 黄梁 未央 成双 无恙 虚妄 凝霜 洛阳 长安 江南 忘川 千年 纸伞 烟雨 回眸 公子 红尘 红颜 红衣 红豆 红线 青丝 青史 青冢 白发 白首 白骨 黄土 黄泉 碧落 紫陌"
four_chars_words = "情深缘浅 情深不寿 莫失莫忘 阴阳相隔 如花美眷 似水流年 眉目如画 曲终人散 繁华落尽 不诉离殇 一世长安"
sentence_model = "xx，xx，xx了xx。 xxxx，xxxx，不过是一场xxxx。 你说xxxx，我说xxxx，最后不过xxxx。 xx，xx，许我一场xxxx。 一x一x一xx，半x半x半xx。 你说xxxxxxxx，后来xxxxxxxx。 xxxx，xxxx，终不敌xxxx。"
tcw = two_chars_words.split(' ')
fcw = four_chars_words.split(' ')
sentences = sentence_model.split(' ')


def get_sentence():
    model = random.choice(sentences)
    old = []
    while 'xxxx' in model:
        strre = random.choice(fcw)
        if strre not in old:
            model = model.replace('xxxx', strre, 1)
            old.append(strre)
    while 'xx' in model:
        strre = random.choice(tcw)
        if strre not in old:
            model = model.replace('xx', strre, 1)
            old.append(strre)
    while 'x' in model:
        strre = random.choice(tcw)
        if strre not in old:
            model = model.replace('x', strre[random.randint(0, 1)], 1)
            old.append(strre)
    print(model)


if __name__ == '__main__':
    for i in range(100):
        get_sentence()
