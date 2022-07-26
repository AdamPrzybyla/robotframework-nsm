﻿#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re,pprint,os

def polish():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla

*** Test Cases ***
Test 1
	Teraz jest tak: ja widzę webpage
	Ja nie widzę słowa logged na webpage
	Potem ja użyję słów credentials na webpage
	Z tego powodu ja widzę słowa logged na webpage
	Niedługo potem ja nie widzę webpage

Test 2
	Teraz jest tak: ja widzę webpage
	Ja nie widzę słowa logged na webpage
	Potem ja użyję słów bad credentials na webpage
	Z tego powodu ja nie widzę słowa logged na webpage
	Niedługo potem ja nie widzę webpage

Test 3
	Teraz jest tak: ja widzę webpage
	Ja nie widzę słowa logged na webpage
	Niedługo potem ja nie widzę webpage
"""
	open("polish.robot","w").write(t)

def english():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
Test 1
	It is like this now: I see the webpage
	I not see words logged on the webpage
	then i use the words credentials on webpage
	because of this: I see words logged on the webpage
	after this i see the webpage no more

Test 2
	It is like this now: I see the webpage
	I not see words logged on the webpage
	then i use the words bad credentials on webpage
	because of this: I not see words logged on the webpage
	after this i see the webpage no more

Test 3
	It is like this now: I see the webpage
	I not see words logged on the webpage
	after this i see the webpage no more
"""
	open("english.robot","w").write(t)

def german():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
Test 1
	Es ist jetzt so: Ich sehe die webpage
	Ich sehe keine wörter logged auf der webpage
	dann benutze ich die worte credentials auf der webpage
	Aus diesem grund: sehe ich wörter logged auf der webpage
	Danach sehe ich die webpage nicht mehr
Test 2
	Es ist jetzt so: Ich sehe die webpage
	Ich sehe keine wörter logged auf der webpage
	dann benutze ich die worte bad credentials auf der webpage
	Aus diesem grund: Ich sehe keine wörter logged auf der webpage
	Danach sehe ich die webpage nicht mehr
Test 3
	Es ist jetzt so: Ich sehe die webpage
	Ich sehe keine wörter logged auf der webpage
	Danach sehe ich die webpage nicht mehr
"""
	open("german.robot","w").write(t)

def russian():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
Тест 1
	Теперь это так: я вижу webpage
	Я не вижу слов logged на webpage
	тогда я использую слова credentials на webpage
	из-за этого я вижу слова logged на webpage
	после этого я больше не вижу webpage
Тест 2
	Теперь это так: я вижу webpage
	Я не вижу слов logged на webpage
	тогда я использую слова bad credentials на webpage
	из-за этого Я не вижу слов logged на webpage
	после этого я больше не вижу webpage
Тест 3
	Теперь это так: я вижу webpage
	Я не вижу слов logged на webpage
	после этого я больше не вижу webpage
"""
	open("russian.robot","w").write(t)


def spanish():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
Prueba 1
	Es así ahora: veo el webpage
	No veo palabras logged en el webpage
	entonces uso las palabras credentials en webpage
	por esto: veo palabras logged en webpage
	después de esto ya no veo el webpage
Prueba 2
	Es así ahora: veo el webpage
	No veo palabras logged en el webpage
	entonces uso las palabras bad credentials en webpage
	por esto: no veo palabras logged en el webpage
	después de esto ya no veo el webpage
Prueba 3
	Es así ahora: veo el webpage
	No veo palabras logged en el webpage
	después de esto ya no veo el webpage
"""
	open("spanish.robot","w").write(t)

def czech():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
Test 1
	Teď je to takto: Vidím webpage
	Na webpage nevidím slova logged
	pak používám slova credentials na webpage
	z tohoto důvodu: Na webpage vidím slova logged
	po tom už nevidím webpage

Test 2
	Teď je to takto: Vidím webpage
	Na webpage nevidím slova logged
	pak používám slova bad credentials na webpage
	z tohoto důvodu: Na webpage nevidím slova logged
	po tom už nevidím webpage

Test 3
	Teď je to takto: Vidím webpage
	Na webpage nevidím slova logged
	po tom už nevidím webpage
"""
	open("czech.robot","w").write(t)

def french():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
Test 1
	C'est comme ça maintenant: je vois le webpage
	Je ne vois pas les mots logged sur le webpage
	alors j'utilise les mots credentials sur webpage
	à cause de cela: je vois les mots logged sur le webpage
	après cela je ne vois plus le webpage

Test 2
	C'est comme ça maintenant: je vois le webpage
	Je ne vois pas les mots logged sur le webpage
	alors j'utilise les mots bad credentials sur webpage
	à cause de cela: je ne vois pas les mots logged sur le webpage
	après cela je ne vois plus le webpage

Test 3
	C'est comme ça maintenant: je vois le webpage
	Je ne vois pas les mots logged sur le webpage
	après cela je ne vois plus le webpage
"""
	open("french.robot","w").write(t)

def japan():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
テスト 1
	次のようになります。webpage を見る
	webpage は logged という単語を表示しません
	次に、 webpage で credentials という言葉を使用します
	このため： webpage に logged という言葉が表示されます
	この後もう webpage が見えない
テスト 2
	次のようになります。webpage を見る
	webpage は logged という単語を表示しません
	次に、 webpage で bad credentials という言葉を使用します
	このため： webpage は logged という単語を表示しません
	この後もう webpage が見えない
テスト 3
	次のようになります。webpage を見る
	webpage は logged という単語を表示しません
	この後もう webpage が見えない
"""
	open("japan.robot","w").write(t)

def china():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla

*** Test Cases ***
测试1
	现在是这样的：我看到 webpage
	我在 webpage 上看不到 logged 单词
	然后我在 webpage 上使用 credentials 单词
	因此我在 webpage上看到 logged 单词
	在此之后，我不再看到 webpage

测试2
	现在是这样的：我看到 webpage
	我在 webpage 上看不到 logged 单词
	然后我在 webpage 上使用 bad credentials 单词
	因此我在 webpage 上看不到 logged 单词
	在此之后，我不再看到 webpage

测试3
	现在是这样的：我看到 webpage
	我在 webpage 上看不到 logged 单词
	在此之后，我不再看到 webpage
"""
	open("china.robot","w").write(t)


def portugese():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
Teste 1
	É assim agora: eu vejo o webpage
	Não vejo as palavras logged na webpage
	então eu uso as palavras credentials em webpage
	por causa disso: vejo as palavras logged na webpage
	Depois disso, não vejo mais a webpage

Teste 2
	É assim agora: eu vejo o webpage
	Não vejo as palavras logged na webpage
	então eu uso as palavras bad credentials em webpage
	por causa disso: não vejo as palavras logged na webpage
	Depois disso, não vejo mais a webpage

Teste 3
	É assim agora: eu vejo o webpage
	Não vejo as palavras logged na webpage
	Depois disso, não vejo mais a webpage
"""
	open("portugese.robot","w").write(t)

def romanian():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
Testul 1
	Acum este așa: eu văd webpage
	Eu nu văd cuvintele logged pe webpage
	Apoi eu voi folosi cuvintele credentials pe webpage
	Din acest motiv eu văd cuvintele logged pe webpage
	La scurt timp după eu nu mai văd webpage

Testul 2
	Acum este așa: eu văd webpage
	Eu nu văd cuvintele logged pe webpage
	Apoi eu voi folosi cuvintele bad credentials pe webpage
	Din acest motiv eu nu văd cuvintele logged pe webpage
	La scurt timp după eu nu mai văd webpage

Testul 3
	Acum este așa: eu văd webpage
	Eu nu văd cuvintele logged pe webpage
	La scurt timp după eu nu mai văd webpage
"""
	open("romanian.robot","w").write(t)

def urdu():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** test cases ***
١ٹسیٹ
	                   ںوہ اتکس ھکید webpage ںیم ۔ےہ اسیا با
	          ۔ںیہ ےتآ ںیہن رظن ظافلا logged ںیم webpage ےھجم
	     ںوہ اترک لامعتسا ظافلا credentials رپ webpage ںیم رھپ
	ںوہ اتکس ھکید ظافلا logged رپ webpage ںیم - :ےس ہجو یک سا
	                 اتھکید ںیہن وک webpage با ںیم دعب ےک سا

۲ٹسیٹ

	                  ںوہ اتکس ھکید webpage ںیم ۔ےہ اسیا با
	         ۔ںیہ ےتآ ںیہن رظن ظافلا logged ںیم webpage ےھجم
	ںوہ اترک لامعتسا ظافلا bad credentials رپ webpage ںیم رھپ	
   ۔ںیہ ےتآ ںیہن رظن ظافلا logged ںیم webpage ےھجم :ےس ہجو یک سا
	                اتھکید ںیہن وک webpage با ںیم دعب ےک سا

۳ٹسیٹ

	                  ںوہ اتکس ھکید webpage ںیم ۔ےہ اسیا با
	         ۔ںیہ ےتآ ںیہن رظن ظافلا logged ںیم webpage ےھجم
	                اتھکید ںیہن وک webpage با ںیم دعب ےک سا

"""
	open("urdu.robot","w").write(t)

def bengali():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
পরীক্ষা 1
	এটি এখন এই মত: আমি webpage দেখতে পাচ্ছি
	আমি শব্দগুলি logged webpage তে দেখতে পাচ্ছি না
	তাহলে আমি শব্দগুলি credentials ব্যবহার করি webpage তে 
	এর জন্য: আমি webpage - তে logged শব্দগুলি দেখতে পাচ্ছি
	এর পরে আমি আর ওয়েবসাইট webpage দেখতে পাচ্ছি না

পরীক্ষা 2
	এটি এখন এই মত: আমি webpage দেখতে পাচ্ছি
	আমি শব্দগুলি logged webpage তে দেখতে পাচ্ছি না
	তাহলে আমি শব্দগুলি bad credentials ব্যবহার করি webpage তে
	এর জন্য: আমি শব্দগুলি logged webpage তে দেখতে পাচ্ছি না
	এর পরে আমি আর ওয়েবসাইট webpage দেখতে পাচ্ছি না

পরীক্ষা 3
	এটি এখন এই মত: আমি webpage দেখতে পাচ্ছি
	আমি শব্দগুলি logged webpage তে দেখতে পাচ্ছি না
	এর পরে আমি আর ওয়েবসাইট webpage দেখতে পাচ্ছি না
"""
	open("bengali.robot","w").write(t)

def silesian():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
Sprowdź 1
	Teroz je tak: jo widza webpage
	Jo ni widza słowa logged na webpage
	Potym jo użyja słów credentials na webpage
	Z tego powodu jo widza słowa logged na webpage
	Terozki uż jo ni widza webpage

Sprowdź 2
	Teroz je tak: jo widza webpage
	Jo ni widza słowa logged na webpage
	Potym jo użyja słów bad credentials na webpage
	Z tego powodu jo ni widza słowa logged na webpage
	Terozki uż jo ni widza webpage

Sprowdź 3
	Teroz je tak: jo widza webpage
	Jo ni widza słowa logged na webpage
	Terozki uż jo ni widza webpage
"""
	open("silesian.robot","w").write(t)

def bielorusian():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
Тест 1
	Зараз гэта так: Я бачу webpage
	Я не бачу слоў logged на webpage
	тады я выкарыстаю словы credentials на webpage
	з-за гэтага я бачу словы logged на webpage
	пасля гэтага я больш не бачу webpage

Тест 2
	Зараз гэта так: Я бачу webpage
	Я не бачу слоў logged на webpage
	тады я выкарыстаю словы bad credentials на webpage
	з-за гэтага Я не бачу слоў logged на webpage
	пасля гэтага я больш не бачу webpage

Тест 3
	Зараз гэта так: Я бачу webpage
	Я не бачу слоў logged на webpage
	пасля гэтага я больш не бачу webpage
"""
	open("bielorusian.robot","w").write(t)

def tamil():
	t="""*** Settings ***
Resource  NSM.robot
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

*** Test Cases ***
சோதனை 1
	இப்போது இது போன்றது: நான் webpage ஐப் பார்க்கிறேன்
	webpage இல் logged சொற்களை நான் காணவில்லை
	நான் webpage இல் credentials என்ற சொற்களைப் பயன்படுத்துகிறேன்
	இதன் காரணமாக webpage இல் logged சொற்களைக் காண்கிறேன்
	இதற்கு பிறகு நான் இனி webpage ஐப் பார்க்கவில்லை

சோதனை 2
	இப்போது இது போன்றது: நான் webpage ஐப் பார்க்கிறேன்
	webpage இல் logged சொற்களை நான் காணவில்லை
	நான் webpage இல் bad credentials என்ற சொற்களைப் பயன்படுத்துகிறேன்
	இதன் காரணமாக webpage இல் logged சொற்களை நான் காணவில்லை
	இதற்கு பிறகு நான் இனி webpage ஐப் பார்க்கவில்லை

சோதனை 3
	இப்போது இது போன்றது: நான் webpage ஐப் பார்க்கிறேன்
	webpage இல் logged சொற்களை நான் காணவில்லை
	இதற்கு பிறகு நான் இனி webpage ஐப் பார்க்கவில்லை
"""
	open("tamil.robot","w").write(t)

def nsmlib():
	t="""*** Settings ***
Resource  mykeywords.robot

*** Keywords ***
# english
It is like this now: ${state}
	Run keyword  ${state}

I not see words ${logged} on the ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

i use the words ${cred} on ${page:[^ ]+}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

because of this: ${state}
	Run keyword  ${state}

I see words ${logged} on the ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

after this ${state}
	Run keyword  ${state}

i see the ${page:[^ ]+} no more
	Run keyword  ${page} teardown

I see the ${page:[^ ]+}
	Run keyword  ${page} setup

# polski
Teraz jest tak: ${state}
	Run keyword  ${state}

Ja nie widzę słowa ${logged} na ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

Potem ja użyję słów ${cred} na ${page:[^ ]+}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

Z tego powodu ${state}
	Run keyword  ${state}

ja widzę słowa ${logged} na ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

Niedługo potem ${state}
	Run keyword  ${state}

ja nie widzę ${page:[^ ]+}
	Run keyword  ${page} teardown

ja widzę ${page:[^ ]+}
	Run keyword  ${page} setup

# deutsche
Es ist jetzt so: ${state}
	Run keyword  ${state}

Ich sehe keine wörter ${logged} auf der ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

dann benutze ich die worte ${cred} auf der ${page:[^ ]+}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

Aus diesem grund: ${state}
	Run keyword  ${state}

sehe ich wörter ${logged} auf der ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

Danach ${state}
	Run keyword  ${state}

sehe ich die ${page:[^ ]+} nicht mehr
	Run keyword  ${page} teardown

Ich sehe die ${page:[^ ]+}
	Run keyword  ${page} setup

# russian
Теперь это так: ${state}
	Run keyword  ${state}

Я не вижу слов ${logged} на ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

тогда я использую слова ${cred} на ${page:[^ ]+}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

из-за этого ${state}
	Run keyword  ${state}

я вижу слова ${logged} на ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

после этого ${state}
	Run keyword  ${state}

я больше не вижу ${page:[^ ]+}
	Run keyword  ${page} teardown

я вижу ${page:[^ ]+}
	Run keyword  ${page} setup

# czech
Teď je to takto: ${state}
	Run keyword  ${state}

Na ${page:[^ ]+} nevidím slova ${logged}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

pak používám slova ${cred} na ${page:[^ ]+}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

z tohoto důvodu: ${state}
	Run keyword  ${state}

Na ${page:[^ ]+} vidím slova ${logged}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

po tom už ${state}
	Run keyword  ${state}

nevidím ${page:[^ ]+}
	Run keyword  ${page} teardown

Vidím ${page:[^ ]+}
	Run keyword  ${page} setup

# french
C'est comme ça maintenant: ${state}
	Run keyword  ${state}

Je ne vois pas les mots ${logged} sur le ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

alors j'utilise les mots ${cred} sur ${page:[^ ]+}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

à cause de cela: ${state}
	Run keyword  ${state}

je vois les mots ${logged} sur le ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

après cela ${state}
	Run keyword  ${state}

je ne vois plus le ${page:[^ ]+}
	Run keyword  ${page} teardown

je vois le ${page:[^ ]+}
	Run keyword  ${page} setup

# spanish

Es así ahora: ${state}
	Run keyword  ${state}

No veo palabras ${logged} en el ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

entonces uso las palabras ${cred} en ${page:[^ ]+}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

por esto: ${state}
	Run keyword  ${state}

veo palabras ${logged} en ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

después de esto ya ${state}
	Run keyword  ${state}

no veo el ${page:[^ ]+}
	Run keyword  ${page} teardown

veo el ${page:[^ ]+}
	Run keyword  ${page} setup

# japan

次のようになります。 ${state}
	Run keyword  ${state}

${page:[^ ]+} は ${logged} という単語を表示しません
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

次に、 ${page:[^ ]+} で ${cred} という言葉を使用します
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

このため： ${state}
	Run keyword  ${state}

${page:[^ ]+} に ${logged} という言葉が表示されます
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

この後${state}
	Run keyword  ${state}

もう ${page:[^ ]+} が見えない
	Run keyword  ${page} teardown

${page:[^ ]+} を見る
	Run keyword  ${page} setup

# china

#It is like this now: ${state}
现在是这样的：${state}
	Run keyword  ${state}

#I not see words ${logged} on the ${page}
我在 ${page:[^ ]+} 上看不到 ${logged} 单词
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

#I use the words ${cred} on ${page}
然后我在 ${page:[^ ]+} 上使用 ${cred} 单词
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}


#because of this: ${state}
因此${state}
	Run keyword  ${state}

#I see words ${logged} on the ${page}
我在 ${page:[^ ]+}上看到 ${logged} 单词
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

#after this ${state}
在此之后，${state}
	Run keyword  ${state}


#i see the ${page:[^ ]+} ${no more}
我不再看到 ${page:[^ ]+}
	Run keyword  ${page} teardown

#i see the ${page:[^ ]+}
我看到 ${page:[^ ]+}
	Run keyword  ${page} setup

# portugese

#It is like this now: ${state}
É assim agora: ${state}
	Run keyword  ${state}

#I not see words ${logged} on the ${page}
Não vejo as palavras ${logged} na ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

#I use the words ${cred} on ${page}
então eu uso as palavras ${cred} em ${page:[^ ]+}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

#because of this: ${state}
por causa disso: ${state}
	Run keyword  ${state}

#I see words ${logged} on the ${page}
vejo as palavras ${logged} na ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

#after this ${state}
Depois disso, ${state}
	Run keyword  ${state}

#i see the ${page:[^ ]+} ${no more}
não vejo mais a ${page:[^ ]+}
	Run keyword  ${page} teardown

#i see the ${page:[^ ]+}
eu vejo o ${page:[^ ]+}
	Run keyword  ${page} setup

# romanian
#It is like this now: ${state}
Acum este așa: ${state}
	Run keyword  ${state}

#I not see words ${logged} on the ${page}
Eu nu văd cuvintele ${logged} pe ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

#I use the words ${cred} on ${page}
Apoi eu voi folosi cuvintele ${cred} pe ${page:[^ ]+}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

#because of this: ${state}
Din acest motiv ${state}
	Run keyword  ${state}

#I see words ${logged} on the ${page}
eu văd cuvintele ${logged} pe ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

#after this ${state}
La scurt timp după ${state}
	Run keyword  ${state}

#i see the ${page:[^ ]+} ${no more}
eu nu mai văd ${page:[^ ]+}
	Run keyword  ${page} teardown

#i see the ${page:[^ ]+}
eu văd ${page:[^ ]+}
	Run keyword  ${page} setup

# urdu
#It is like this now: ${state}
${state} ںیم ۔ےہ اسیا با
	Run keyword      ${state}

#I not see words ${logged} on the ${page:[^ ]+}
۔ںیہ ےتآ ںیہن رظن ظافلا ${logged} ںیم ${page:[^ ]+} ےھجم
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

#I use the words ${cred} on ${page}
ںوہ اترک لامعتسا ظافلا ${cred} رپ ${page:[^ ]+} ںیم رھپ
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

#because of this: ${state}
${state} :ےس ہجو یک سا
	Run keyword      ${state}

#I see words ${logged} on the ${page}
ںوہ اتکس ھکید ظافلا ${logged} رپ ${page:[^ ]+} ںیم -
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

#after this ${state}
${state} ںیم دعب ےک سا
	Run keyword  ${state}

#i see the ${page:[^ ]+} ${no more}
اتھکید ںیہن وک ${page:[^ ]+} با
	Run keyword  ${page} teardown

#i see the ${page:[^ ]+}
ںوہ اتکس ھکید ${page:[^ ]+}
	Run keyword  ${page} setup

# bengali
এটি এখন এই মত: ${state}
#It is like this now: ${state}
	Run keyword  ${state}

আমি শব্দগুলি ${logged} ${page:[^ ]+} তে দেখতে পাচ্ছি না
#I not see words ${logged} on the ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

তাহলে আমি শব্দগুলি ${cred} ব্যবহার করি ${page:[^ ]+} তে
#I use the words ${cred} on ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

এর জন্য: ${state}
#because of this: ${state}
	Run keyword  ${state}

আমি ${page:[^ ]+} - তে ${logged} শব্দগুলি দেখতে পাচ্ছি
#I see words ${logged} on the ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

এর পরে ${state}
#after this ${state}
	Run keyword  ${state}

আমি আর ওয়েবসাইট ${page:[^ ]+} দেখতে পাচ্ছি না
#i see the ${page:[^ ]+} ${no more}
	Run keyword  ${page} teardown

আমি ${page:[^ ]+} দেখতে পাচ্ছি
#i see the ${page:[^ ]+}
	Run keyword  ${page} setup

# bielorusian
Зараз гэта так: ${state}
#It is like this now: ${state}
	Run keyword  ${state}

Я не бачу слоў ${logged} на ${page:[^ ]+}
#I not see words ${logged} on the ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

тады я выкарыстаю словы ${cred} на ${page:[^ ]+}
#I use the words ${cred} on ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

з-за гэтага ${state}
#because of this: ${state}
	Run keyword  ${state}

я бачу словы ${logged} на ${page:[^ ]+}
#I see words ${logged} on the ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

пасля гэтага ${state}
#after this ${state}
	Run keyword  ${state}

я больш не бачу ${page:[^ ]+}
#i see the ${page:[^ ]+} ${no more}
	Run keyword  ${page} teardown

Я бачу ${page:[^ ]+}
#i see the ${page:[^ ]+}
	Run keyword  ${page} setup

# tamil
இப்போது இது போன்றது: ${state}
#It is like this now: ${state}
	Run keyword  ${state}

#I not see words ${logged} on the ${page}
${page:[^ ]+} இல் ${logged} சொற்களை நான் காணவில்லை
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

நான் ${page:[^ ]+} இல் ${cred} என்ற சொற்களைப் பயன்படுத்துகிறேன்
#I use the words ${cred} on ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

இதன் காரணமாக ${state}
#because of this: ${state}
	Run keyword  ${state}

#I see words ${logged} on the ${page}
${page:[^ ]+} இல் ${logged} சொற்களைக் காண்கிறேன்
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

#after this ${state}
இதற்கு பிறகு ${state}
	Run keyword  ${state}

#i see the ${page:[^ ]+} ${no more}
நான் இனி ${page:[^ ]+} ஐப் பார்க்கவில்லை
	Run keyword  ${page} teardown

#i see the ${page:[^ ]+}
நான் ${page:[^ ]+} ஐப் பார்க்கிறேன்
	Run keyword  ${page} setup

# silesian
Teroz je tak: ${state}
#It is like this now: ${state}
	Run keyword  ${state}

#I not see words ${logged} on the ${page}
Jo ni widza słowa ${logged} na ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

Potym jo użyja słów ${cred} na ${page:[^ ]+}
#I use the words ${cred} on ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

#Z tego powodu ${state}
##because of this: ${state}
#	Run keyword  ${state}

#I see words ${logged} on the ${page}
jo widza słowa ${logged} na ${page:[^ ]+}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

#after this ${state}
Terozki uż ${state}
	Run keyword  ${state}

#i see the ${page:[^ ]+} ${no more}
jo ni widza ${page:[^ ]+}
	Run keyword  ${page} teardown

#i see the ${page:[^ ]+}
jo widza ${page:[^ ]+}
	Run keyword  ${page} setup
"""
	open("NSM.robot","w").write(t)

def mykeywords():
	t="""*** Settings ***
Resource  requirements.robot

*** Keywords ***
${page} setup
	Log to console  Wchodze na strone ${page}

${page} teardown
	Log to console  Wychodze ze strony ${page}

credentials
	Log to console  wyslalem dobre cred
	[Return]  user  pass

bad credentials
	Log to console  wyslalem zle cred
	[Return]  baduser  badpass

logged
	Log to console  szukaj Odebrane
	[Return]  Odebrane


Enter Credentials
	[Arguments]  ${user}  ${pass}
	Log to console  uzylem cred ${user} ${pass}

webpage check
	[Arguments]  ${slowo}
	Log to console  szukalem slowa ${slowo}
	[Return]  OK
"""
	open("mykeywords.robot","w").write(t)

def mykeywords0():
	t="""*** Settings ***
Resource  requirements.robot
Library  SeleniumLibrary

*** Variables ***
${xu}  //*[@id="login"]
${xp}  //*[@id="password"]
${xb}  //button[@type='submit']
${RODO}     //button[contains(text(),'PRZECHODZ')]
${BROWSER}   Firefox

*** Keywords ***
${page} setup
	Open Browser  about:blank   ${BROWSER}
	Go To  http://poczta.wp.pl

${page} teardown
	Capture Page Screenshot
	Close All Browsers

credentials
	[Return]  mailtest007  MailTest007

bad credentials
	[Return]  baduser  badpass

logged
	[Return]  Odebrane


Enter Credentials
	[Arguments]  ${user}  ${pass}
	Sleep  5
	Click Element  ${RODO}
	Sleep  5
	Input Text  ${xu}   ${user}
	Input Text  ${xp}   ${pass}
	Click Element  ${xb}
	Sleep   20

webpage check
	[Arguments]  ${slowo}
	${result}=  Run Keyword and return status  Page Should Contain  ${slowo}
	${result}=  set variable if  ${result}   OK  NOTOK
	[Return]  ${result}
"""
	open("mykeywords.robot","w").write(t)

def requirements():
	t="""*** Variables ***
${ansible_password}   ${FALSE}
${ansible_user}  %{USER}
${DBHost}  localhost
${DBName}  w3schools
${DBUser}  %{USER}
${DBPass}  %{USER}
${DBPort}  3306
${DBFile}  w3schools.sql
${Furl}    https://raw.githubusercontent.com/AndrejPHP/w3schools-database/master/w3schools.sql
${gr}      /etc/apt/sources.list.d/google-chrome.list
${grep}    http://mirror.cs.uchicago.edu/google-chrome/pool/main/g/google-chrome-stable/
#${chrome_version}  False
${chrome_version}  google-chrome-stable_81.0.4044.138-1_amd64.deb
${chd81}  http://launchpadlibrarian.net/478575933/chromium-chromedriver_81.0.4044.138-0ubuntu0.18.04.1_amd64.deb
${chd89}  https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip

*** Settings ***
Library  Impansible
library  Collections
library  OperatingSystem
library  String

*** Keywords ***
Requirements
	No Operation
	#The Operating System should be Ubuntu
	#The Firefox browser should be installed if needed
	#The Geckodriver should be installed if needed
	#The google repo should be available
	#The Chrome should be installed if needed
	#The Chromedriver should be installed if needed
	#The MySQL server should be installed
	#Python should have MySQL support
	#The MySQL user have all privileges
	#Mysql should have no database imported
	#Mysql should have database imported

The Operating System should be Ubuntu
	${x}=	Setup  localhost
	${y}=	get from dictionary  ${x}   ansible_facts
	${z}=	get from dictionary  ${y}   ansible_distribution
	Should be Equal  ${z}  Ubuntu
	
The Firefox browser should be installed if needed
	[Timeout]    600
	${x}=  Convert To Lower Case  ${BROWSER}
	${x}=  Run Keyword and return status  Should Contain  ${x}  firefox
	Return from keyword if  not ${x}
	${x}=	apt    localhost   package=firefox   state=present
        ${x}=	get from dictionary  ${x}   invocation
        ${y}=	get from dictionary  ${x}   module_args
        ${s}=	get from dictionary  ${y}   state
        Should be Equal  ${s}  present
	${w}=	Run	which firefox
	Should Contain  ${w}  firefox

The Geckodriver should be installed if needed
	[Timeout]    600
	${x}=  Convert To Lower Case  ${BROWSER}
	${x}=  Run Keyword and return status  Should Contain  ${x}  firefox
	Return from keyword if  not ${x}
	${x}=	apt    localhost   package=firefox-geckodriver   state=present
        ${x}=	get from dictionary  ${x}   invocation
        ${y}=	get from dictionary  ${x}   module_args
        ${s}=	get from dictionary  ${y}   state
        Should be Equal  ${s}  present
	${w}=	Run	which geckodriver
	Should Contain  ${w}  geckodriver

The Chrome should be installed if needed
	[Timeout]    600
	${x}=  Convert To Lower Case  ${BROWSER}
	${x}=  Run Keyword and return status  Should Contain  ${x}  chrome
	       Return from keyword if  not ${x}
	${w}=	Run	which google-chrome-stable
	${x}=   run keyword and return status  Should Contain  ${w}  google-chrome-stable
	        Return from keyword if  ${x}
		run keyword if  "${chrome_version}"!="False"  apt  localhost  deb="${grep}${chrome_version}"
	${x}=	apt    localhost   package=google-chrome-stable   state=present
        ${x}=	get from dictionary  ${x}   invocation
        ${y}=	get from dictionary  ${x}   module_args
        ${s}=	get from dictionary  ${y}   state
        Should be Equal  ${s}  present
	${w}=	Run	which google-chrome-stable
	Should Contain  ${w}  google-chrome-stable

The Chromedriver should be installed if needed
	[Timeout]    600
	${x}=  Convert To Lower Case  ${BROWSER}
	${x}=  Run Keyword and return status  Should Contain  ${x}  chrome
	Return from keyword if  not ${x}
        ${x}=   package facts  localhost
        ${x}=   get from dictionary  ${x}   ansible_facts
        ${x}=   get from dictionary  ${x}   packages
        ${x}=   get from dictionary  ${x}   google-chrome-stable
        ${xv}=  get from dictionary  ${x}[0]   version
        ${dp}=  Evaluate  "%{PATH}".split(":")[0]
        ${xs}=  Run keyword and return status  should start with  ${xv}  81
        ${xz}=  Run keyword and return status  should start with  ${xv}  89
                Run keyword if  not ${xs}  apt    localhost   package=chromium-chromedriver state=present
                Run keyword if  ${xs}  apt  localhost  update_cache=yes
                Run keyword if  ${xs}  apt  localhost  deb="${chd81}"  force=True
                Run keyword if  ${xz}  Get Url  LOCAL  url=${chd89}  dest=.
                Run keyword if  ${xz}  Evaluate  zipfile.ZipFile("chromedriver_linux64.zip").extract("chromedriver",$dp)   modules=zipfile
                Run keyword if  ${xz}  Evaluate  os.chmod('${dp}/chromedriver',0o755)  modules=os
	${w}=	Run	which chromedriver
	Should Contain  ${w}  chromedriver

The MySQL server should be installed
	[Timeout]    600
	${x}=	apt    localhost   package=mysql-server   state=present
	${x}=	get from dictionary  ${x}   invocation
	${y}=	get from dictionary  ${x}   module_args
	${s}=	get from dictionary  ${y}   state
		Should be Equal  ${s}  present
	${w}=	Run	which mysqld
		Should Contain  ${w}  mysqld

Python should have MySQL support
	[Timeout]    600
	${x}=	apt    localhost   package=python3-mysqldb   state=present
	${x}=	get from dictionary  ${x}   invocation
	${y}=	get from dictionary  ${x}   module_args
	${s}=	get from dictionary  ${y}   state
		Should be Equal  ${s}  present

The MySQL user have all privileges
	[Timeout]    600
	${x}=	apt    localhost   package=python3-mysqldb   state=present
	${x}=	get from dictionary  ${x}   invocation
	${y}=	get from dictionary  ${x}   module_args
	${s}=	get from dictionary  ${y}   state
		Should be Equal  ${s}  present
		mysql_user  localhost  name=${DBUser}  password=${DBPass}  priv=*.*:ALL

Mysql should have no database imported
	[Timeout]    600
	mysql db  localhost  name=${DBName}  state=absent

Mysql should have database imported
	[Timeout]    600
	mysql db  localhost  name=${DBName}  state=present
	Get url   localhost  url=${Furl}     dest=/tmp/${DBFile}
	mysql db  localhost  name=${DBName}  state=import  target=/tmp/${DBFile}

We should be connected to database
        Import Library  DatabaseLibrary
        Connect To Database   pymysql  ${DBName}  ${DBUser}  ${DBPass}  ${DBHost}  ${DBPort}

Mysql requirements
	The system should be upgraded
	The MySQL server should be installed
	Python should have MySQL support
	Mysql should have no database imported
	Mysql should have database imported
	The MySQL user have all privileges
	We should be connected to database

The system should be upgraded
        apt   localhost  upgrade=dist           force_apt_get=yes

The google repo should be available
	[Timeout]    600
	${x}=	Stat  localhost  path="${gr}"
        ${x}=   get from dictionary  ${x}   stat
        ${x}=   get from dictionary  ${x}   exists
		run keyword if  not ${x}  Copy  localhost  content='deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main'  dest="${gr}"
		run keyword if  not ${x}  shell  localhost  wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
		run keyword if  not ${x}  apt  localhost  update_cache=yes
	${x}=	Stat  localhost  path="${gr}"
        ${x}=   get from dictionary  ${x}   stat
        ${x}=   get from dictionary  ${x}   exists
	Should be true  ${x}   "The google repo is not available"
"""
	open("requirements.robot","w").write(t)

def mymysql():
	t="""*** Settings ***
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>
Documentation  Examples: https://github.com/franz-see/Robotframework-Database-Library/blob/master/test/MySQL_DB_Tests.robot
Resource  requirements.robot
Suite Setup   MySQL Requirements

*** Test Cases ***
Simple SQL test
	${wynik}=  Execute SQL String  SELECT * FROM customers
	log  ${wynik}
	${wynik}=  Query   select * from w3schools.customers where City='Berlin'
	log  ${wynik}
	${wynik}=   Get from list  ${wynik}  0
	log  ${wynik}
	${wynik}=   Get from list  ${wynik}  1
	log  ${wynik}
	Should be equal   ${wynik}   Alfreds Futterkiste
"""
	open("mymysql.robot","w").write(t)


def appium():
	t="""*** Settings ***
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>
Resource  lemat.robot
Suite Setup  Appium Requirements
Suite Teardown  Terminate Process

*** Test Cases ***
Should open the wp.pl and login to website
	Open Chrome Application on Android device
	Go to Url  https://poczta.wp.pl
	${page_title}=  execute script  return document.title
	Should Contain  ${page_title}  Poczta
	Capture Page Screenshot
	Click Element  ${RODO}
	Sleep  10
	Input Text  ${xu}   mailtest007
	Input Text  ${xp}   MailTest007
	Wait Until Element is visible  ${xb}  15s
	Wait Until Keyword Succeeds  3x  5s  Click Element  ${xb}
	Sleep  10
	Page Should Contain Text  Odebrane
	Capture Page Screenshot
	Close Application

Should send keys to search box and then check the value
	Open Android Test App  .app.SearchInvoke
	Input Text  txt_query_prefill  Hello world!
	Click Element  btn_start_search
	Wait until Page Contains Element  android:id/search_src_text
	Element Text Should be  android:id/search_src_text  Hello world!
	Close Application

Should click a button that opens an alert and then dismisses it
	Open Android Test App  .app.AlertDialogSamples
	Click element  two_buttons
	Wait until Page Contains Element  android:id/alertTitle
	Element should contain text  android:id/alertTitle  Lorem ipsum dolor sit aie consectetur adipiscing
	${close_dialog_button}  get webelement  android:id/button1
	Click Element  ${close_dialog_button}
	Close Application

Should Create and Destroy Android Session
	[Documentation]  Android Create Native Test Session
	[teardown]  No Operation
	Open Android Test App
	${activity}  get activity
	Should be Equal  ${activity}  .ApiDemos
	Close Application
	Sleep  3s
	${previous kw}=         Register Keyword To Run On Failure      Nothing
	Run Keyword and Expect Error  No application is open  get activity
	Register Keyword To Run On Failure      ${previous kw}

Should Create and Destroy Android Web Session
	[Documentation]  Android Web Session
	[teardown]  No Operation
	Open Chrome Application on Android device
	Go to Url  https://www.google.com
	${page_title}  execute script  return document.title
	Should be Equal  ${page_title}  Google
	Close Application
	Sleep  3s
	${previous kw}=         Register Keyword To Run On Failure      Nothing
	Run Keyword and Expect Error  No application is open  Execute Script  return document.title
	Register Keyword To Run On Failure      ${previous kw}

Should find elements by Accessibility ID
	[Documentation]  Android Selectors
	Open Android Test App
	${element}  get webelement  accessibility_id=Content
	element should be visible  ${element}
	Close Application

Should find elements by ID
	Open Android Test App
	page should contain element  android:id/action_bar_container
	Close Application

Should find elements by class name
	Open Android Test App
	@{elements}  get webelements  class=android.widget.FrameLayout
	length should be  ${elements}  3
	Close Application

Should find elements by XPath
	Open Android Test App
	@{elements}  get webelements  //*[@class='android.widget.FrameLayout']
	length should be  ${elements}  3
	Close Application

Should send keys to search box and then check the value 2
	[Documentation]  Simple example using AppiumLibrary
	Open Android Test App  .app.SearchInvoke
	Input Search Query  Hello World!
	Submit Search
	Search Query Should Be Matching  Hello World!
	Close Application
"""
	open("appium.robot","w").write(t)

def emulator():
	t="""*** Settings ***
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>
Resource  lemat.robot
Suite Setup  Appium Emulator Requirements
Suite Teardown  Terminate All Processes

*** Test Cases ***
Should open the wp.pl and login to website
	Open Chrome Application on Android device
	Go to Url  https://poczta.wp.pl
	${page_title}=  execute script  return document.title
	Should Contain  ${page_title}  Poczta
	Capture Page Screenshot
	Click Element  ${RODO}
	Sleep  10
	Input Text  ${xu}   mailtest007
	Input Text  ${xp}   MailTest007
	Wait Until Element is visible  ${xb}  15s
	Wait Until Keyword Succeeds  3x  5s  Click Element  ${xb}
	Page Should Contain Text  Odebrane
	Capture Page Screenshot
	Close Application

Should send keys to search box and then check the value
	Open Android Test App  .app.SearchInvoke
	Input Text  txt_query_prefill  Hello world!
	Click Element  btn_start_search
	Wait until Page Contains Element  android:id/search_src_text
	Element Text Should be  android:id/search_src_text  Hello world!
	Close Application

Should click a button that opens an alert and then dismisses it
	Open Android Test App  .app.AlertDialogSamples
	Click element  two_buttons
	Wait until Page Contains Element  android:id/alertTitle
	Element should contain text  android:id/alertTitle  Lorem ipsum dolor sit aie consectetur adipiscing
	${close_dialog_button}  get webelement  android:id/button1
	Click Element  ${close_dialog_button}
	Close Application

Should Create and Destroy Android Session
	[Documentation]  Android Create Native Test Session
	[teardown]  No Operation
	Open Android Test App
	${activity}  get activity
	Should be Equal  ${activity}  .ApiDemos
	Close Application
	Sleep  3s
	${previous kw}=         Register Keyword To Run On Failure      Nothing
	Run Keyword and Expect Error  No application is open  get activity
	Register Keyword To Run On Failure      ${previous kw}

Should Create and Destroy Android Web Session
	[Documentation]  Android Web Session
	[teardown]  No Operation
	Open Chrome Application on Android device
	Go to Url  https://www.google.com
	${page_title}  execute script  return document.title
	Should be Equal  ${page_title}  Google
	Close Application
	Sleep  3s
	${previous kw}=         Register Keyword To Run On Failure      Nothing
	Run Keyword and Expect Error  No application is open  Execute Script  return document.title
	Register Keyword To Run On Failure      ${previous kw}

Should find elements by Accessibility ID
	[Documentation]  Android Selectors
	Open Android Test App
	${element}  get webelement  accessibility_id=Content
	element should be visible  ${element}
	Close Application

Should find elements by ID
	Open Android Test App
	page should contain element  android:id/action_bar_container
	Close Application

Should find elements by class name
	Open Android Test App
	@{elements}  get webelements  class=android.widget.FrameLayout
	length should be  ${elements}  3
	Close Application

Should find elements by XPath
	Open Android Test App
	@{elements}  get webelements  //*[@class='android.widget.FrameLayout']
	length should be  ${elements}  3
	Close Application

Should send keys to search box and then check the value 2
	[Documentation]  Simple example using AppiumLibrary
	Open Android Test App  .app.SearchInvoke
	Input Search Query  Hello World!
	Submit Search
	Search Query Should Be Matching  Hello World!
	Close Application
"""
	open("emulator.robot","w").write(t)

def selenium():
	t="""*** Settings ***
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

Resource  requirements.robot
Library  SeleniumLibrary
Suite setup  requirements
Suite teardown  Close All Browsers

*** Variables ***
${xu}  //*[@id="login"]
${xp}  //*[@id="password"]
${xb}  //button[@type='submit']
${RODO}     //button[contains(text(),'PRZECHODZ')]

${BROWSER}   firefox
${ansible_user}  %{USER}
${ansible_become_password}   xxxxxxxxxxxxxx
${ansible_password}  ${FALSE}

*** Test Cases ***
test poczty
  Open Browser  http://poczta.wp.pl  ${BROWSER}
  Sleep  5
  Click Element  ${RODO}
  Sleep  5
  Input Text  ${xu}   mailtest007
  Input Text  ${xp}   MailTest007
  Click Element  ${xb}
  Sleep  10
  Page Should Contain  Odebrane
  Close All Browsers

** keywords ***
Requirements
	lemat 0 - Apt system should work
	Lemat 1 - Firefox is installed
	Lemat 2 - Selenium driver is installed
	Lemat 3 - The Chrome should be installed if needed
        Lemat 4 - Chrome in the latest version
	Lemat 5 - The Chromedriver should be installed if needed

lemat 0 - Apt system should work
	#shell  localhost  wget -qO - https://pkg.jenkins.io/debian-stable/jenkins.io.key | apt-key add -
	Run Keyword And Ignore Error   shell  localhost  sed -i 's/deb/#deb/' /etc/apt/sources.list.d/jenkins.list
        apt  localhost  update_cache=yes
        apt  localhost  autoremove=yes

Lemat 1 - Firefox is installed
	The Firefox browser should be installed if needed

Lemat 2 - Selenium driver is installed
	The Geckodriver should be installed if needed

Lemat 3 - The Chrome should be installed if needed
	The google repo should be available
	The Chrome should be installed if needed

Lemat 4 - Chrome in the latest version
        apt  localhost  update_cache=yes
        apt  localhost  only_upgrade=yes  package=google-chrome-stable  state=latest

Lemat 5 - The Chromedriver should be installed if needed
	The google repo should be available
	The Chromedriver should be installed if needed
"""
	open("selenium.robot","w").write(t)

la=["polish","english","german","russian","czech","french","spanish","japan","china","mykeywords","mykeywords0","romanian","urdu","bengali","silesian","tamil","bielorusian","portugese","nsmlib","requirements","appium","selenium","mygames","gameslist","game","mymysql","lemat","jenkins","mymycsv","emulator","sonar"]

def NSMfu(data,la1="polish"):
	if la1=="polish":
		init={0: "Teraz jest tak: ${state}", 3:"Z tego powodu ${state}",5:"Niedługo potem ${state}"}
	elif la1=='english':
		init={0:"It is like this now: ${state}",3:"because of this: ${state}",5:"after this ${state}"}
	elif la1=='german':
		init={0:"Es ist jetzt so: ${state}",3:"Aus diesem grund: ${state}",5:"Danach ${state}"}
	elif la1=='russian':
		init={0:"Теперь это так: ${state}",3:"из-за этого ${state}",5:"после этого ${state}"}
	elif la1=='czech':
		init={0:"Teď je to takto: ${state}",3:"z tohoto důvodu: ${state}",5:"po tom už ${state}"}
	elif la1=='french':
		init={0:"C'est comme ça maintenant: ${state}",3:"à cause de cela: ${state}",5:"après cela ${state}"}
	elif la1=='spanish':
		init={0:"Es así ahora: ${state}",3:"por esto: ${state}",5:"después de esto ya ${state}"}
	elif la1=='japan':
		init={0:"次のようになります。 ${state}",3:"このため： ${state}",5:"この後${state}"}
	elif la1=='china':
		init={0:"现在是这样的：${state}",3:"因此${state}",5:"在此之后，${state}"}
	elif la1=='portugese':
		init={0:"É assim agora: ${state}",3:"por causa disso: ${state}",5:"Depois disso, ${state}"}
	elif la1=='romanian':
		init={0:"Acum este așa: ${state}",3:"Din acest motiv ${state}",5:"La scurt timp după ${state}"}
	elif la1=='urdu':
		init={0:"${state} ںیم ۔ےہ اسیا با",3:"${state} :ےس ہجو یک سا",5:"${state} ںیم دعب ےک سا"}
	elif la1=='bengali':
		init={0:'''এটি এখন এই মত: ${state}''',3:'''এর জন্য: ${state}''',5:'''এর পরে ${state}'''}
	elif la1=='bielorusian':
		init={0:"Зараз гэта так: ${state}",3:"з-за гэтага ${state}",5:'пасля гэтага ${state}'}
	elif la1=='tamil':
		init={0:"இப்போது இது போன்றது: ${state}",3:"இதன் காரணமாக ${state}",5:"இதற்கு பிறகு ${state}"}
	elif la1=='silesian':
		init={0:"Teroz je tak: ${state}",3:"Z tego powodu ${state}",5:"Terozki uż ${state}"}

	wyn=init.copy()
	for nrp,linia in enumerate(data):
		for v in init.items():
			v1=v[1].strip().replace("${state}","").strip()
			if v1 in linia:
				nl=linia.replace(v1,"").strip()
				nl1=nl.replace("webpage","${page:[^ ]+}").replace("logged","${logged}")
				nr={0:7,3:4,5:6}[v[0]]
				if nr not in wyn.keys():
					wyn[nr]=nl1
				break
		else:
			nl=linia.strip()
			nl1=nl.replace("webpage","${page:[^ ]+}").replace("logged","${logged}")
			nl1=re.sub("(bad )?credentials","${cred}",nl1)
			if nrp in [6,11,7]: continue
			if nl1.startswith("then "): nl1=nl1[5:]
			wyn[nrp]=nl1
	if la1=='silesian':
		del wyn[3]
	return wyn

langs={"polish":[8,16],"english":[0,8],"german":[16,24],"russian":[24,32],"czech":[32,40],"french":[40,48],"spanish":[48,56],
"japan":[56,64],"china":[64,72],"portugese":[72,80],"romanian":[80,88],"urdu":[88,96],"bengali":[96,104],"bielorusian":[104,112]
,"tamil":[112,120],"silesian":[120,127]}

def main():
	if sys.argv[1]=='all':
		polish()
		english()
		german()
		russian()
		czech()
		french()
		spanish()
		japan()
		china()
		portugese()
		romanian()
		urdu()
		bengali()
		bielorusian()
		tamil()
		silesian()
		selenium()
		nsmlib()
		mykeywords()
		mymysql()
		mymycsv()
		requirements()
		sonar()
		lemat()
		emulator()
		jenkins()
	elif sys.argv[1] in la:
		eval(sys.argv[1]+"()")


# -*- coding: utf-8 -*-
def gameslist():
	try:
	    from urllib.request import urlopen
	except ImportError:
	    from urllib2 import urlopen
	import re
	t1='(?smi)<h2><a href="details.php\?ID=(.*?)">([^<>]*?)</a>'
	t3='https://www.lemon64.com/games/list.php?title=%s&page=%s'
	oldies={}
	w=u"""*** Settings ***
Library   OperatingSystem
Library   String
Library   Collections
Resource  gameslist.robot

*** Keywords ***
"""
	for e in '0ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		for i in range(1,20):
			g=urlopen(t3%(e,i)).read().decode("utf-8","ignore")
			for ty in re.findall(t1,g):
				nr,nazwa=ty
				#nazwa=nazwa.decode("utf-8","ignore").replace("&amp;","&")
				nazwa=nazwa.replace("&amp;","&")
				nazwas=nazwa.replace(" ","").lower()
				if nazwas in oldies:
					nr2=oldies[nazwas]
					nazwap=nazwa+" (%d)" % nr2
				else:
					nr2=0
					nazwap=nazwa
				oldies[nazwas]=nr2+1
				w+=u"""Game %s should be installed
	doinstallgame  %s

"""  % (nazwap,nr)
			if not 'Next&nbsp;' in g: break
	w=w+r"""doinstallgame
	[Arguments]   ${gamenr}
	${u}=   Set Variable  http://www.lemon64.com/games/details.php?ID=${gamenr}
	${name}=    gamename     ${u}
	Should Not Be Empty  ${name}
	${zipek}=   getgameurl   ${u}
	should contain  ${zipek}  8bitfiles
	${uc}=   getcoverturl   ${u}
	should contain   ${uc}  lemon64
	#should contain   ${uc}  thumb
	${m}=   getgame  ${zipek}
	should contain   ${m}   64
	${nico}=   creategameicon   ${name}  ${m}  ${uc}
	Should Contain  ${nico}  Icon

Gamename
	[Arguments]   ${u}
	${w}   ${g}=   Should Match Regexp     ${u}   =([0-9]+)
	${u}=  Catenate    SEPARATOR=   https://www.lemon64.com/games/details.php?ID=  ${g}
	${w}=  pyigeturl   ${u}
	${w}   ${g}=   Should Match Regexp     ${w}   (?smi)<meta property="og:title" content="Lemon64 - (.*?)" />
	${g} = 	Replace String Using Regexp 	${g}   , The$   ${EMPTY}
	[return]   ${g}

Getgameurl
	[Arguments]   ${u}
	${g}=  pyigeturl   ${u}
		log   ${g}
	${ug}=    Should Match Regexp     ${g}   (?smi)http://www.gb64.com/game.php[?]id=[0-9]+
	${g1}=  pyigeturl   ${ug}
	${s}  ${ftpu}=   Run Keyword And Ignore Error    Should Match Regexp  ${g1}   (?smi)ftp://8bitfiles.net/gamebase_64/[^"]+
	${ftpu1}=    Run Keyword If  "${s}"=="FAIL"   Should Match Regexp  ${g1}   (?smi)[^<>]+\.zip
	${ftpu1}=    Run Keyword If  "${s}"=="FAIL"   Catenate    SEPARATOR=   ftp://8bitfiles.net/gamebase_64/Games/  ${ftpu1}
	${ftpu}=    Set Variable If  "${s}"=="FAIL"   ${ftpu1}  ${ftpu}
	[return]   ${ftpu}

Getcoverturl
	[Arguments]   ${u}
	${g}=  pyigeturl   ${u}
	#${uc}=    Should Match Regexp     ${g}   (?smi)https://www.lemon64.com/covers/thumbs/[^"]+
        ${rc}  ${uc}=    Run Keyword And Ignore Error   Should Match Regexp     ${g}   (?smi)https://www.lemon64.com/covers/thumbs/[^"]+
        ${rc1}  ${ucs}=    Run Keyword And Ignore Error   Should Match Regexp     ${g}   (?smi)https://www.lemon64.com/games/screenshots/[^"]+
        ${uc}   set variable if  $rc=="PASS"   ${uc}   ${ucs}
	${g}=  pyigeturlb   ${uc}
	${iconn}=    Should Match Regexp     ${uc}  [^/]*$
	Create Binary File   .images/${iconn}    ${g}
	[return]   ${uc}

getgame
	[Arguments]   ${u}
	${v}=  Evaluate  sys.version_info.major   modules=sys
	${us}=  Replace String   ${u}  !  \! 
	${f}=  Run  curl -sk '${us}' | base64
	${f2}=  Run Keyword if  ${v}==2  Evaluate  base64.decodestring($f)   modules=base64
	${f3}=  Run Keyword if  ${v}==3  Evaluate  base64.decodebytes($f.encode("utf"))   modules=base64
	${f}=   Set Variable if  ${v}==2  ${f2}  ${f3}
	${m2}=  Run Keyword if  ${v}==2  Evaluate  zipfile.ZipFile(StringIO.StringIO($f)).namelist()   modules=zipfile,StringIO
	${m3}=  Run Keyword if  ${v}==3  Evaluate  zipfile.ZipFile(io.BytesIO($f)).namelist()   modules=zipfile,io
	${m}=   Set Variable if  ${v}==2  ${m2}  ${m3}
	${ma}=  Remove Values From List  ${m}   VERSION.NFO
	${mg}=   Get From List  ${m}  0
	FOR    ${i}    IN    @{m}
		Run Keyword if  ${v}==2  Evaluate  zipfile.ZipFile(StringIO.StringIO($f)).extract($i,".data")   modules=zipfile,StringIO
		Run Keyword if  ${v}==3  Evaluate  zipfile.ZipFile(io.BytesIO($f)).extract($i,".data")   modules=zipfile,io
	END
	[return]   ${mg}

CreateGameIcon
	[Arguments]   ${n}  ${d}  ${i}
	${nn} =  Replace String Using Regexp 	${n}   !   ${EMPTY}
	${in}=   Should Match Regexp     ${i}   [^/]*$
	${iv}=   Set Variable   [Desktop Entry]\nName=${n}\nComment=${n}\nExec=x64 '${OUTPUT DIR}/.data/${d}'\nIcon=${OUTPUT DIR}/.images/${in}\nTerminal=false\nType=Application\nEncoding=UTF-8\nCategories=Game;ArcadeGame;
	Create File  ${nn}.desktop   ${iv}
	Evaluate  os.chmod('${nn}.desktop',0o755)  modules=os
	Run  dbus-run-session -- gio set "${nn}.desktop" metadata::trusted yes
	[return]  ${iv}

pyigeturl
	[Arguments]   ${u}
	${v}=  Evaluate  sys.version_info.major   modules=sys
	${w2}=  run keyword if  ${v}==2  Evaluate  urllib2.urlopen($u).read()  modules=urllib2
	${w3}=  run keyword if  ${v}==3  Evaluate  urllib.request.urlopen($u).read().decode("utf-8","ignore")  modules=urllib
	${w}=   set variable if  ${v}==2  ${w2}  ${w3}
	[return]   ${w}

pyigeturlb
	[Arguments]   ${u}
	${v}=  Evaluate  sys.version_info.major   modules=sys
	${w2}=  run keyword if  ${v}==2  Evaluate  urllib2.urlopen($u).read()  modules=urllib2
	${w3}=  run keyword if  ${v}==3  Evaluate  urllib.request.urlopen($u).read()  modules=urllib
	${w}=   set variable if  ${v}==2  ${w2}  ${w3}
	[return]   ${w}
"""
	open("gameslist.robot","w").write(w)

def mygames():
	w="""*** Settings ***
Resource  gameslist.robot
Metadata  Author  Adam Przybyla

*** Test cases ***
My favorite games
	Game H.E.R.O. - Helicopter Emergency Rescue Operation should be installed
	Game Chessmaster 2000, The should be installed
	Game Rick Dangerous should be installed
	Game Rick Dangerous II should be installed
	Game Archon: The Light and the Dark should be installed
	Game Blagger should be installed
	Game Wizard of Wor should be installed
	Game Boulder Dash should be installed
	Game Cauldron II: The Pumpkin Strikes Back should be installed
	Game Cauldron should be installed
	Game Commando should be installed
	Game Elite should be installed
	Game Falklands 82 should be installed
	Game Frantic Freddie should be installed
	Game Ghostbusters should be installed
	Game IK+ should be installed
	Game Loco should be installed
	Game Monty on the Run should be installed
	Game Nebulus should be installed
	Game Paradroid should be installed
	Game Pirates! should be installed
	Game River Raid should be installed
	Game Uridium should be installed
	Game V - The Computer Game should be installed
"""
	open("mygames.robot","w").write(w)

def game():
	w="""*** Settings ***
Resource  gameslist.robot
Metadata  Author  Adam Przybyla

*** Variables ***
${NR}  136

*** Test cases ***
Game Installation 
	doinstallgame  ${NR}
"""
	open("game.robot","w").write(w)

def jenkins():
	w=r"""*** Settings ***
Metadata  Author  Adam Przybyla
library  Impansible
library  Collections
library  OperatingSystem

*** Variables ***
${jenkinskey}  https://pkg.jenkins.io/debian-stable/jenkins.io.key
${jenkinsrepo}  deb https://pkg.jenkins.io/debian-stable binary
${ansible_user}  %{USER}
${ansible_become_password}  xxxxxxxxxxxxxxxxxxxx
${jenkinsconf0}  <?xml version='1.1' encoding='UTF-8'?>{\n}<jenkins.model.JenkinsLocationConfiguration>{\n}  <jenkinsUrl>http://
${jenkinsconf1}  :8080/</jenkinsUrl>{\n}</jenkins.model.JenkinsLocationConfiguration>

*** Test Cases ***
Jenkins Setup
	Add Jenkins to Your Server

*** Keywords ***
Add Jenkins to Your Server
	[Timeout]    7200
	${ip}=   Run   ip -o r g 8.8.8.8|cut -f7 -d" "
	apt   localhost  upgrade=dist
	apt   localhost  package=openjdk-8-jre  state=present
        apt   localhost  package=openjdk-8-jdk  state=present
	Apt Key  localhost  url=${jenkinskey}
	Apt Repository  localhost  repo="deb https://pkg.jenkins.io/debian-stable binary/"  filename=jenkins
	#Apt  localhost  package=jenkins  state=present
	Apt  localhost  deb=https://ftp.halifax.rwth-aachen.de/jenkins/debian-stable/jenkins_2.332.3_all.deb
	Systemd  localhost  name=jenkins  enabled=yes  state=started
	${password}=   Shell  localhost  cat /var/lib/jenkins/secrets/initialAdminPassword
	${password}=  get from dictionary  ${password}   stdout
	${full_crumb}=  Run  curl -sk -u "admin:${password}" --cookie-jar ".tmpfile" http://localhost:8080/crumbIssuer/api/xml?xpath=concat\\(//crumbRequestField,%22:%22,//crumb\\)
	${only_crumb}=  Evaluate   $full_crumb.split(":")[1]
	${result}=  Run  curl -X POST -u "admin:${password}" http://localhost:8080/setupWizard/createAdminUser -H "Connection: keep-alive" -H "Accept: application/json, text/javascript" -H "X-Requested-With: XMLHttpRequest" -H "${full_crumb}" -H "Content-Type: application/x-www-form-urlencoded" --cookie ".tmpfile" --data-raw "username=user&password1=password&password2=password&fullname=full%20name&email=hello%40world.com&Jenkins-Crumb=${only_crumb}&json=%7B%22username%22%3A%20%22user%22%2C%20%22password1%22%3A%20%22password%22%2C%20%22%24redact%22%3A%20%5B%22password1%22%2C%20%22password2%22%5D%2C%20%22password2%22%3A%20%22password%22%2C%20%22fullname%22%3A%20%22full%20name%22%2C%20%22email%22%3A%20%22hello%40world.com%22%2C%20%22Jenkins-Crumb%22%3A%20%22${only_crumb}%22%7D&core%3Aapply=&Submit=Save&json=%7B%22username%22%3A%20%22user%22%2C%20%22password1%22%3A%20%22password%22%2C%20%22%24redact%22%3A%20%5B%22password1%22%2C%20%22password2%22%5D%2C%20%22password2%22%3A%20%22password%22%2C%20%22fullname%22%3A%20%22full%20name%22%2C%20%22email%22%3A%20%22hello%40world.com%22%2C%20%22Jenkins-Crumb%22%3A%20%22${only_crumb}%22%7D"
	${result}=  Run  curl -X POST -u "admin:${password}" http://localhost:8080/pluginManager/installPlugins -H 'Connection: keep-alive' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'X-Requested-With: XMLHttpRequest' -H "${full_crumb}" -H 'Content-Type: application/json' -H 'Accept-Language: en,en-US;q=0.9,it;q=0.8' --cookie .tmpfile --data-raw "{'dynamicLoad':true,'plugins':['cloudbees-folder','antisamy-markup-formatter','build-timeout','credentials-binding','timestamper','ws-cleanup','ant','gradle','workflow-aggregator','github-branch-source','pipeline-github-lib','pipeline-stage-view','git','ssh-slaves','matrix-auth','pam-auth','ldap','email-ext','mailer'],'Jenkins-Crumb':'${only_crumb}'}"
	${result}=  Run  curl -X POST -u "user:password" http://localhost:8080/pluginManager/installPlugins -H 'Connection: keep-alive' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'X-Requested-With: XMLHttpRequest' -H "${full_crumb}" -H 'Content-Type: application/json' -H 'Accept-Language: en,en-US;q=0.9,it;q=0.8' --cookie .tmpfile --data-raw "{'dynamicLoad':true,'plugins':['cloudbees-folder','antisamy-markup-formatter','build-timeout','credentials-binding','timestamper','ws-cleanup','ant','gradle','workflow-aggregator','github-branch-source','pipeline-github-lib','pipeline-stage-view','git','ssh-slaves','matrix-auth','pam-auth','ldap','email-ext','mailer'],'Jenkins-Crumb':'${only_crumb}'}"
        ${x}=   package facts  localhost
        ${x}=   get from dictionary  ${x}   ansible_facts
        ${x}=   get from dictionary  ${x}   packages
        ${x}=   get from dictionary  ${x}   jenkins
        ${v}=  get from dictionary  ${x}[0]   version
	Systemd  localhost  name=jenkins state=stopped
	Copy  localhost   content=${v}  dest=/var/lib/jenkins/jenkins.install.InstallUtil.lastExecVersion  owner=jenkins  group=jenkins
	Copy  localhost   content=${v}  dest=/var/lib/jenkins/jenkins.install.UpgradeWizard.state  owner=jenkins  group=jenkins
	Copy  localhost   content='${jenkinsconf0}${ip}${jenkinsconf1}'  dest=/var/lib/jenkins/jenkins.model.JenkinsLocationConfiguration.xml  owner=jenkins  group=jenkins
	Systemd  localhost  name=jenkins state=started
"""
	open("jenkins.robot","w").write(w)

def lemat():
	w=r"""*** Settings ***
library  Collections
library  Impansible
library  OperatingSystem
library  AppiumLibrary
library  Process

*** Variables ***
${ansible_become_password}  xxxxxxxxxxxxxx
${ansible_user}  %{USER}
${btool}  https://github.com/google/bundletool/releases/download/1.2.0/bundletool-all-1.2.0.jar
${demoapp}  https://github.com/appium/appium/raw/master/sample-code/apps/ApiDemos-debug.apk
${androidtools}  https://dl.google.com/android/repository/commandlinetools-linux-6200805_latest.zip

${ANDROID_AUTOMATION_NAME}    UIAutomator2
${ANDROID_PLATFORM_NAME}      Android
${ANDROID_PLATFORM_VERSION}   %{ANDROID_PLATFORM_VERSION=5.1}
${ANDROID_APP}                ${CURDIR}/ApiDemos-debug.apk
${RODO}     //button[contains(text(),'PRZECHODZ')]
${nolo}  android:id/infobar_close_button
${xu}  //*[@id="login"]
${xp}  //*[@id="password"]
${xb}  //button[@type='submit']
${RODO}     //button[contains(text(),'PRZECHODZ')]
${chdpage}  https://chromedriver.storage.googleapis.com/

*** Keywords ***
Open Chrome Application on Android device
	${v}=   Chrome Main Version
	${pv}=  Android Main Version
	${av}=  Android Automation Version
	Open Application  http://127.0.0.1:4723/wd/hub  automationName=UIAutomator${av}
	...  platformName=${ANDROID_PLATFORM_NAME}  platformVersion=${pv}
	...  browserName=Chrome  chromedriverExecutable=${CURDIR}/bin/chromedriver${v}

Appium Requirements
	The Appium should be installed
	The ApiDemo has been available
	The Chromedriver for Android should be installed
	The Appium works
	The Appium has been started

Appium Emulator Requirements
	The Appium should be installed
	The ApiDemo has been available
	The Appium Emulator has been started
	The Chromedriver for Android should be installed
	The Appium works
	The Appium has been started

The Appium should be installed
	[Timeout]    7200
        run keyword and ignore error  apt   localhost  update_cache=yes       force_apt_get=yes
        apt   localhost  upgrade=dist           force_apt_get=yes
        apt   localhost  package=openjdk-8-jre  state=present
        apt   localhost  package=openjdk-8-jdk  state=present
        apt   localhost  package=android-sdk    state=present
	${w}=   Run     which npm
        ${w}=   run keyword and return status  Should Contain  ${w}  npm
        Run keyword if  not ${w}  apt   localhost  package=npm            state=present
        apt   localhost  package=cmake          state=present
        Get url  LOCAL  url=${androidtools}  dest=/tmp/commandlinetools-linux-6200805_latest.zip  mode="0755"
        Command  localhost  unzip -xn /tmp/commandlinetools-linux-6200805_latest.zip -d /usr/lib/android-sdk/
        alternatives  localhost   name=java     path=/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
        Set Environment Variable  ANDROID_HOME  /usr/lib/android-sdk/
        Set Environment Variable  JAVA_HOME     /usr/lib/jvm/java-8-openjdk-amd64
        ${P}=   Get Environment Variable   PATH
        Set Environment Variable  PATH  /usr/lib/jvm/java-8-openjdk-amd64/bin:${P}
        Get url  LOCAL  url=${btool}  dest=bin/bundletool.jar  mode="0755"
        Shell  localhost  yes | /usr/lib/android-sdk/tools/bin/sdkmanager --sdk_root=/usr/lib/android-sdk/ "tools" >/dev/null
	Shell  localhost  yes | /usr/lib/android-sdk/tools/bin/sdkmanager --install "platform-tools" "platforms;android-28"
	Shell  localhost  yes | /usr/lib/android-sdk/tools/bin/sdkmanager --install "system-images;android-28;google_apis;x86"
	Shell  localhost  yes | /usr/lib/android-sdk/tools/bin/sdkmanager --licenses
	Shell  localhost  /usr/lib/android-sdk/tools/bin/sdkmanager --update
	Run    echo no | /usr/lib/android-sdk/tools/bin/avdmanager create avd -n Android28 -k "system-images;android-28;google_apis;x86" -f
	User   localhost  name=${ansible_user}  groups=kvm  append=yes
        Shell  localhost  curl -sL https://deb.nodesource.com/setup_14.x | bash -
        apt   localhost  upgrade=dist           force_apt_get=yes
        apt   localhost  package=nodejs         state=present
        apt   localhost  package=ffmpeg         state=present
        run keyword and ignore error  npm   localhost  name=appium            global=yes  state=present  unsafe_perm=yes
        npm   localhost  name=appium            global=yes  state=present  unsafe_perm=yes
        run keyword and ignore error  npm   localhost  name=appium-doctor     global=yes  state=present
        npm   localhost  name=appium-doctor     global=yes  state=present
        run keyword and ignore error  npm   localhost  name=opencv4nodejs     global=yes  state=present  unsafe_perm=yes
        npm   localhost  name=opencv4nodejs     global=yes  state=present  unsafe_perm=yes
        run keyword and ignore error  npm   localhost  name=mjpeg-consumer    global=yes  state=present
        npm   localhost  name=mjpeg-consumer    global=yes  state=present

The Chromedriver for Android should be installed
	[Timeout]    600
	${v}=  Chrome Main Version
	${chd}=  Get Chromedriver url  ${v}
	${xz}=   Run keyword and return status  File Should Exist   ${CURDIR}/bin/chromedriver${v}
	Run keyword if  not ${xz}  Get Url  LOCAL  url=${chd}  dest=.
	Run keyword if  not ${xz}  Evaluate  zipfile.ZipFile("chromedriver_linux64.zip").extract("chromedriver",'${CURDIR}/')   modules=zipfile
        Run keyword if  not ${xz}  Evaluate  os.chmod('${CURDIR}/chromedriver',0o755)  modules=os
        Run keyword if  not ${xz}  Evaluate  os.rename('${CURDIR}/chromedriver','${CURDIR}/bin/chromedriver${v}')  modules=os

The ApiDemo has been available
        Get url  LOCAL  url=${demoapp}  dest=${CURDIR}/ApiDemos-debug.apk

The Appium works
	${w}=  Shell  local   appium-doctor 2>&1
	${err}=   get from dictionary  ${w}   stdout
	Should Not Contain   ${err}   WARN   ${err}

The Appium has been started
	${w}=  Shell  localhost   adb devices
	Start Process  appium  shell=True  alias=appiumserver  stdout=${CURDIR}/appium_stdout.txt
	...  stderr=${CURDIR}/appium_stderr.txt
	Sleep  10

The Appium Emulator has been started
	${w}=  Shell  localhost   adb devices
	Start Process  sg kvm -c "/usr/lib/android-sdk//emulator/emulator -no-window \@Android28"  shell=True  alias=appiumemulator  stdout=${CURDIR}/appium_emulator_stdout.txt
	...  stderr=${CURDIR}/appium_emulator_stderr.txt
	Sleep  120

Open Android Test App
	[Arguments]    ${appActivity}=${EMPTY}
	${pv}=  Android Main Version
	${av}=  Android Automation Version
	Open Application  http://127.0.0.1:4723/wd/hub  automationName=UIAutomator${av}
	...  platformName=${ANDROID_PLATFORM_NAME}  platformVersion=${pv}
	...  app=${ANDROID_APP}  appPackage=io.appium.android.apis  appActivity=${appActivity}

Input Search Query
	[Arguments]  ${query}
	Input Text  txt_query_prefill  ${query}
	log  ${ANDROID_PLATFORM_VERSION}

Submit Search
	Click Element  btn_start_search

Search Query Should Be Matching
	[Arguments]  ${text}
	Wait Until Page Contains Element  android:id/search_src_text
	Element Text Should Be  android:id/search_src_text  ${text}
	Capture Page Screenshot

Get Chromedriver url
        [Arguments]   ${va}
        ${v}=  Evaluate  sys.version_info.major   modules=sys
        ${w2}=  run keyword if  ${v}==2  Evaluate  urllib2.urlopen($chdpage).read()  modules=urllib2
        ${w3}=  run keyword if  ${v}==3  Evaluate  urllib.request.urlopen($chdpage).read().decode("utf-8","ignore")  modules=urllib
        ${w}=   set variable if  ${v}==2  ${w2}  ${w3}
	${z}=   Evaluate   {"68":"2.42","69":"2.44","70":"2.45","71":"2.46","72":"2.46"}.get($va)
	${va}=   set variable if  int(${va})<73    ${z}  ${va}
	${match}=    Evaluate   re.findall(r'(?smi)<Key>('+$va+'[0-9.]*)/chromedriver_linux64.zip\</Key>',$w)[-1]  modules=re
        [return]   https://chromedriver.storage.googleapis.com/${match}/chromedriver_linux64.zip

Chrome Main Version
	${w}=   Shell  localhost  adb shell dumpsys package com.android.chrome | /usr/bin/sed -n '/versionName=/\{s/\\(.*\\)=\\([0-9]*\\).*/\\2/p;q\}'
	[return]  ${w["stdout"]}

Android Main Version
	${w}=   Shell  localhost  adb shell getprop ro.build.version.release
	[return]  ${w["stdout"]}

Android Main api Version
	${w}=   Shell  localhost  adb shell getprop ro.build.version.sdk
	[return]  ${w["stdout"]}

Android Automation Version
	${w}=   Shell  localhost  adb shell getprop ro.build.version.sdk
	${w}=   Evaluate   "12"[(int($w["stdout"])>20)]
	[return]  ${w}
"""
	open("lemat.robot","w").write(w)

def mymycsv():
	w=r"""*** Settings ***
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>
Documentation  Examples: https://github.com/franz-see/Robotframework-Database-Library/blob/master/test/MySQL_DB_Tests.robot
Library  DatabaseLibrary
Resource  requirements.robot
Suite Setup   MySQL Requirements

*** Variables ***
${myCSV}  https://gist.githubusercontent.com/thulioph/ba51413417b566e70205717c0189c9f9/raw/18e43bcf7e7c182c4ed341cde502870fc331ca27/MOCK_DATA.csv
${wyfile}  /var/lib/mysql-files/mock_data.csv
${DBName}  app

*** Test Cases ***
Simple SQL test
        ${wynik}=  Query   select email from users where first_name='Donn'
        log  ${wynik}
        ${wynik}=   Get from list  ${wynik}  0
        log  ${wynik}
        ${wynik}=   Get from list  ${wynik}  0
        log  ${wynik}
        Should be equal   ${wynik}   dcohenj@eepurl.com

*** Keywords ***
Mysql should have database imported
        [Timeout]    600
        MySQL DB  localhost  name=${DBName}  state=present
        Get url   localhost  url=${myCSV}     dest=${wyfile}  group=mysql  owner=mysql
	MySQL User  localhost  name=${DBUser}  password=${DBPass}  priv=*.*:ALL
        Connect To Database   pymysql  ${DBName}  ${DBUser}  ${DBPass}  ${DBHost}  ${DBPort}
        Execute SQL String  SET GLOBAL local_infile=1;
        Execute SQL String  Drop table if exists users
        Execute SQL String  CREATE TABLE users (id INT NOT NULL AUTO_INCREMENT, first_name VARCHAR(255) NOT NULL, last_name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, transactions INT NOT NULL, account_creation DATE NOT NULL, PRIMARY KEY (id))
        Shell  localhost   mysql --local-infile=1 app -e "LOAD DATA LOCAL INFILE '/var/lib/mysql-files/mock_data.csv' INTO TABLE users FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id, first_name, last_name, email, transactions, @account_creation)SET account_creation = STR_TO_DATE(@account_creation, '%m/%d/%y');"
"""
	open("mymycsv.robot","w").write(w)

def sonar():
	w=r"""*** Settings ***
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>
library  Impansible
library  Collections
library  OperatingSystem
#Resource  lemat.robot
#Suite Setup  Sonar Requirements
*** Variables ***
${sonarlocalurl}  http://localhost:9000
${sonarurl}    https://binaries.sonarsource.com/Distribution/
${sonarbin}    https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-8.9.8.54436.zip
${scannerbin}  https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744-linux.zip
${ansible_user}  %{USER}
${ansible_become_password}  xxxxxxxxxxxxxxxxxxxx
${sonarconf}  [Unit]\n
...  Description=SonarQube service\n
...  After=syslog.target network.target\n
...  \n
...  [Service]\n
...  Type=forking\n
...  ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start\n
...  ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop\n
...  LimitNOFILE=131072\n
...  LimitNPROC=8192\n
...  User=sonar\n
...  Group=sonar\n
...  Restart=on-failure\n
...  \n
...  [Install]\n
...  WantedBy=multi-user.target\n

*** Test Cases ***
Add Sonar to Your Server
	Add Sonar to Your Server

*** Keywords ***
Add Sonar to Your Server
	apt   localhost  package=openjdk-11-jre  state=present
	Group  localhost   name=sonar
	User  localhost   name=sonar  group=sonar  password=sonar  password_lock=yes
	Copy  localhost   content='${sonarconf}'  dest=/etc/systemd/system/sonar.service  owner=sonar  group=sonar
        Get url  LOCAL  url=${sonarbin}  dest=/tmp/  mode="0755"
        Command  localhost  unzip -xn /tmp/sonarqube-8.9.8.54436.zip -d /opt
        Get url  LOCAL  url=${scannerbin}  dest=/tmp/  mode="0755"
        Command  localhost  unzip -xn /tmp/sonar-scanner-cli-4.0.0.1744-linux.zip -d /opt
	Command  localhost  chown -R sonar:sonar /opt/sonarqube-8.9.8.54436/
	Command  localhost   ln -s sonarqube-8.9.8.54436 sonarqube  chdir=/opt
	Command  localhost   sed -i '/wrapper.java.command/s/=java/=\\/usr\\/lib\\/jvm\\/java-11-openjdk-amd64\\/bin\\/java/g' /opt/sonarqube-8.9.8.54436/conf/wrapper.conf
	Systemd  localhost  name=sonar  state=started  enabled=yes  daemon_reload=yes
        Wait Until Keyword Succeeds  10x  25s  Sonar should be powered up
	${result}=   Run   curl -u admin:admin -X POST "http://localhost:9000/api/users/change_password?login\=admin&previousPassword\=admin&password\=tester"

Sonar should be powered up
        ${v}=  Evaluate  sys.version_info.major   modules=sys
        ${w2}=  run keyword if  ${v}==2  Evaluate  urllib2.urlopen($sonarlocalurl).read()  modules=urllib2
        ${w3}=  run keyword if  ${v}==3  Evaluate  urllib.request.urlopen($sonarlocalurl).read().decode("utf-8","ignore")  modules=urllib
        ${w}=   set variable if  ${v}==2  ${w2}  ${w3}
	should contain   ${w}   UP   Sonar is not powered up
"""
	open("sonar.robot","w").write(w)

if __name__=='__main__':
	main()
