#! /usr/bin/python
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
${xb}  css:.nSubmit
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
${DBHost}  localhost
${DBName}  w3schools
${DBUser}  XXXXXX
${DBPass}  XXXXXX
${DBPort}  3306
${DBFile}  w3schools.sql
${Furl}    https://raw.githubusercontent.com/AndrejPHP/w3schools-database/master/w3schools.sql
${gr}      /etc/apt/sources.list.d/google-chrome.list
${grep}    http://mirror.cs.uchicago.edu/google-chrome/pool/main/g/google-chrome-stable/
#${chrome_version}  False
${chrome_version}  google-chrome-stable_81.0.4044.138-1_amd64.deb
${chd81}  http://launchpadlibrarian.net/478575933/chromium-chromedriver_81.0.4044.138-0ubuntu0.18.04.1_amd64.deb


*** Settings ***
Library  Impansible
library  Collections
library  OperatingSystem
library  String
#Library  DatabaseLibrary

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
        ${x}=   get from dictionary  ${x}[0]   version
        ${xs}=  run keyword and return status  should start with  ${x}  81
        ${x}=   run keyword if  not ${xs}  apt    localhost   package=chromium-chromedriver state=present
                run keyword if  ${xs}  apt  localhost  update_cache=yes
        ${x}=   run keyword if  ${xs}  apt  localhost  deb="${chd81}"  force=True
        #log to console   ${x}
	#${x}=	apt    localhost   package=chromium-chromedriver   state=present
        #${x}=	get from dictionary  ${x}   invocation
        #${y}=	get from dictionary  ${x}   module_args
        #${s}=	get from dictionary  ${y}   state
        #Should be Equal  ${s}  present
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
	${x}=	apt    localhost   package=python-mysqldb   state=present
	${x}=	get from dictionary  ${x}   invocation
	${y}=	get from dictionary  ${x}   module_args
	${s}=	get from dictionary  ${y}   state
		Should be Equal  ${s}  present

The MySQL user have all privileges
	[Timeout]    600
	${x}=	apt    localhost   package=python-mysqldb   state=present
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

Mysql requirements
	The MySQL server should be installed
	Python should have MySQL support
	Mysql should have no database imported
	Mysql should have database imported
	The MySQL user have all privileges

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

def appium():
	t="""*** Settings ***
Metadata  Author  Adam Przybyla  <adam.przybyla@gmail.com>

library  Collections
library  Impansible
library  OperatingSystem
library  AppiumLibrary
library  Process

Suite Setup  Requirements
Suite Teardown  Terminate Process

*** Variables ***
${ansible_become_password}  xxxxxxxxxxxx
${ansible_user}  xxxxxxxxxxxx
${btool}  https://github.com/google/bundletool/releases/download/1.2.0/bundletool-all-1.2.0.jar
${demoapp}  https://github.com/appium/appium/raw/master/sample-code/apps/ApiDemos-debug.apk

${ANDROID_AUTOMATION_NAME}    UIAutomator1
${ANDROID_APP}                ${CURDIR}/ApiDemos-debug.apk
${ANDROID_PLATFORM_NAME}      Android
${ANDROID_PLATFORM_VERSION}   %{ANDROID_PLATFORM_VERSION=4}

*** Test Cases ***
Should send keys to search box and then check the value
  Open Test Application
  Input Search Query  Hello World!
  Submit Search
  Search Query Should Be Matching  Hello World!

*** Keywords ***
Open Test Application
  Open Application  http://127.0.0.1:4723/wd/hub  automationName=${ANDROID_AUTOMATION_NAME}
  ...  platformName=${ANDROID_PLATFORM_NAME}  platformVersion=${ANDROID_PLATFORM_VERSION}
  ...  app=${ANDROID_APP}  appPackage=io.appium.android.apis  appActivity=.app.SearchInvoke

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

Requirements
	Lemat 1 - appium is installed
	Lemat 2 - appium works
	Lemat 3 - appium has been started

Lemat 1 - appium is installed
	[Timeout]    1800
        run keyword and ignore error  npm   apt   localhost  update_cache=yes       force_apt_get=yes
        apt   localhost  upgrade=dist           force_apt_get=yes
        apt   localhost  package=openjdk-8-jre  state=present
        apt   localhost  package=openjdk-8-jdk  state=present
        apt   localhost  package=android-sdk    state=present
        apt   localhost  package=npm            state=present
        apt   localhost  package=ffmpeg         state=present
        run keyword and ignore error  npm   localhost  name=appium            global=yes  state=present
        npm   localhost  name=appium            global=yes  state=present
        run keyword and ignore error  npm   localhost  name=appium-doctor     global=yes  state=present
        npm   localhost  name=appium-doctor     global=yes  state=present
        run keyword and ignore error  npm   localhost  name=opencv4nodejs     global=yes  state=present
        npm   localhost  name=opencv4nodejs     global=yes  state=present
        run keyword and ignore error  npm   localhost  name=mjpeg-consumer    global=yes  state=present
        npm   localhost  name=mjpeg-consumer    global=yes  state=present
        alternatives  localhost   name=java     path=/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
        Set Environment Variable  ANDROID_HOME  /usr/lib/android-sdk/
        Set Environment Variable  JAVA_HOME     /usr/lib/jvm/java-8-openjdk-amd64
        ${P}=   Get Environment Variable   PATH
        Set Environment Variable  PATH  /usr/lib/jvm/java-8-openjdk-amd64/bin:${P}
        Set Environment Variable  PATH  /usr/lib/jvm/java-8-openjdk-amd64/bin:${P}
        Get url  LOCAL  url=${btool}  dest=bin/bundletool.jar  mode="0755"
        Get url  LOCAL  url=${demoapp}  dest=${CURDIR}/ApiDemos-debug.apk

Lemat 2 - appium works
	${w}=  Shell  local   appium-doctor 2>&1 |grep -v emulator
	${err}=   get from dictionary  ${w}   stdout
	Should Not Contain   ${err}   WARN   ${err}

Lemat 3 - appium has been started
	Start Process  appium  shell=True  alias=appiumserver  stdout=${CURDIR}/appium_stdout.txt  stderr=${CURDIR}/appium_stderr.txt
	Sleep  10
"""
	open("appium.robot","w").write(t)

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
${xb}  css:.nSubmit
${BROWSER}   firefox
${ansible_user}  %{USER}
${ansible_become_password}   xxxxxxxxxxxxxxx
${ansible_password}  ${FALSE}

*** Test Cases ***
test poczty
  Open Browser  http://poczta.wp.pl  ${BROWSER}
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
	shell  localhost  wget -qO - https://pkg.jenkins.io/debian-stable/jenkins.io.key | apt-key add -
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

la=["polish","english","german","russian","czech","french","spanish","japan","china","mykeywords","mykeywords0","romanian","urdu","bengali","silesian","tamil","bielorusian","portugese","nsmlib","requirements","appium","selenium"]

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
		requirements()
	elif sys.argv[1] in la:
		eval(sys.argv[1]+"()")

if __name__=='__main__':
	main()
