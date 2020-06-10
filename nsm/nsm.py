#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
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
	Aus diesem Grund: sehe ich wörter logged auf der webpage
	Danach sehe ich die webpage nicht mehr
Test 2
	Es ist jetzt so: Ich sehe die webpage
	Ich sehe keine wörter logged auf der webpage
	dann benutze ich die worte bad credentials auf der webpage
	Aus diesem Grund: Ich sehe keine wörter logged auf der webpage
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

def nsm():
	t="""*** Settings ***
Resource  mykeywords.robot

*** Keywords ***
# english
It is like this now: ${state}
	Run keyword  ${state}

I not see words ${logged} on the ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

I use the words ${cred} on ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

because of this: ${state}
	Run keyword  ${state}

I see words ${logged} on the ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

after this ${state}
	Run keyword  ${state}

i see the ${page:[^ ]+} ${no more}
	Run keyword  ${page} teardown

i see the ${page:[^ ]+}
	Run keyword  ${page} setup

# polski
Teraz jest tak: ${state}
	Run keyword  ${state}

Ja nie widzę słowa ${logged} na ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

Potem ja użyję słów ${cred} na ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

Z tego powodu ${state}
	Run keyword  ${state}

ja widzę słowa ${logged} na ${page}
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

Ich sehe keine wörter ${logged} auf der ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

dann benutze ich die worte ${cred} auf der ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

Aus diesem grund: ${state}
	Run keyword  ${state}

sehe ich wörter ${logged} auf der ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

Danach ${state}
	Run keyword  ${state}

sehe ich die ${page:[^ ]+} ${no more}
	Run keyword  ${page} teardown

Ich sehe die ${page:[^ ]+}
	Run keyword  ${page} setup

# russian
Теперь это так: ${state}
	Run keyword  ${state}

Я не вижу слов ${logged} на ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

тогда я использую слова ${cred} на ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

из-за этого ${state}
	Run keyword  ${state}

я вижу слова ${logged} на ${page}
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

Na ${page} nevidím slova ${logged}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

pak používám slova ${cred} na ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

z tohoto důvodu: ${state}
	Run keyword  ${state}

Na ${page} vidím slova ${logged}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

po tom už ${state}
	Run keyword  ${state}

nevidím ${page}
	Run keyword  ${page} teardown

Vidím ${page}
	Run keyword  ${page} setup

# french
C'est comme ça maintenant: ${state}
	Run keyword  ${state}

Je ne vois pas les mots ${logged} sur le ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

alors j'utilise les mots ${cred} sur ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

à cause de cela: ${state}
	Run keyword  ${state}

je vois les mots ${logged} sur le ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

après cela ${state}
	Run keyword  ${state}

je ne vois plus le ${page}
	Run keyword  ${page} teardown

je vois le ${page}
	Run keyword  ${page} setup

# spanish

Es así ahora: ${state}
	Run keyword  ${state}

No veo palabras ${logged} en el ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

entonces uso las palabras ${cred} en ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

por esto: ${state}
	Run keyword  ${state}

veo palabras ${logged} en ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

después de esto ya ${state}
	Run keyword  ${state}

no veo el ${page}
	Run keyword  ${page} teardown

veo el ${page}
	Run keyword  ${page} setup

# japan

次のようになります。 ${state}
	Run keyword  ${state}

${page:[^ ]+} は ${logged:[^ ]+} という単語を表示しません
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

次に、 ${page} で ${cred} という言葉を使用します
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

このため： ${state}
	Run keyword  ${state}

${page:[^ ]+} に ${logged:[^ ]+} という言葉が表示されます
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

この後 ${state}
	Run keyword  ${state}

この後もう ${page} が見えない
	Run keyword  ${page} teardown

${page:[^ ]+} を見る
	Run keyword  ${page} setup

# china

#It is like this now: ${state}
现在是这样的：${state}
	Run keyword  ${state}

#I not see words ${logged} on the ${page}
我在 ${page} 上看不到 ${logged} 单词
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

#I use the words ${cred} on ${page}
然后我在 ${page} 上使用 ${cred} 单词
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}


#because of this: ${state}
因此${state}
	Run keyword  ${state}

#I see words ${logged} on the ${page}
我在 ${page}上看到 ${logged} 单词
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

#after this ${state}
在此之后，${state}
	Run keyword  ${state}


#i see the ${page:[^ ]+} ${no more}
我${no more:[^ ]+}看到${page}
	Run keyword  ${page} teardown

#i see the ${page:[^ ]+}
我看到 ${page:[^ ]+}
	Run keyword  ${page} setup

# portugese

#It is like this now: ${state}
É assim agora: ${state}
	Run keyword  ${state}

#I not see words ${logged} on the ${page}
Não vejo as palavras ${logged} na ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

#I use the words ${cred} on ${page}
então eu uso as palavras ${cred} em ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

#because of this: ${state}
por causa disso: ${state}
	Run keyword  ${state}

#I see words ${logged} on the ${page}
vejo as palavras ${logged} na ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

#after this ${state}
Depois disso, ${state}
	Run keyword  ${state}

#i see the ${page:[^ ]+} ${no more}
não vejo mais a ${page}
	Run keyword  ${page} teardown

#i see the ${page:[^ ]+}
eu vejo o ${page}
	Run keyword  ${page} setup

# romanian
#It is like this now: ${state}
Acum este așa: ${state}
	Run keyword  ${state}

#I not see words ${logged} on the ${page}
eu nu văd cuvintele ${logged} pe ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

#I use the words ${cred} on ${page}
Apoi eu voi folosi cuvintele ${cred} pe ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

#because of this: ${state}
Din acest motiv ${state}
	Run keyword  ${state}

#I see words ${logged} on the ${page}
eu văd cuvintele ${logged} pe ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should be equal   OK   ${result}

#after this ${state}
La scurt timp după ${state}
	Run keyword  ${state}

#i see the ${page:[^ ]+} ${no more}
eu nu mai văd ${page}
	Run keyword  ${page} teardown

#i see the ${page:[^ ]+}
eu văd ${page:[^ ]+}
	Run keyword  ${page} setup

# urdu
#It is like this now: ${state}
${state} ںیم ۔ےہ اسیا با
	run keyword      ${state}

#I not see words ${logged} on the ${page}
۔ںیہ ےتآ ںیہن رظن ظافلا ${logged} ںیم ${page} ےھجم
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

#I use the words ${cred} on ${page}
ںوہ اترک لامعتسا ظافلا ${cred} رپ ${page} ںیم رھپ	
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

#because of this: ${state}
${state} :ےس ہجو یک سا
	run keyword      ${state}

#I see words ${logged} on the ${page}
ںوہ اتکس ھکید ظافلا ${logged} رپ ${page} ںیم -
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

আমি শব্দগুলি ${logged:[^ ]+} ${page:[^ ]+} তে দেখতে পাচ্ছি না
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

আমি ${page} - তে ${logged} শব্দগুলি দেখতে পাচ্ছি
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

# silesian
Teroz je tak: ${state}
#It is like this now: ${state}
	Run keyword  ${state}

#I not see words ${logged} on the ${page}
Jo ni widza słowa ${logged} na ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

Potym jo użyja słów ${cred} na ${page}
#I use the words ${cred} on ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

#Z tego powodu ${state}
##because of this: ${state}
#	Run keyword  ${state}

#I see words ${logged} on the ${page}
jo widza słowa ${logged} na ${page}
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

# bielorusian
Зараз гэта так: ${state}
#It is like this now: ${state}
	Run keyword  ${state}

Я не бачу слоў ${logged} на ${page}
#I not see words ${logged} on the ${page}
	${words}=   Run keyword  ${logged}
	${result}=  Run keyword  ${page} check  ${words}
	Should not be equal   OK   ${result}

тады я выкарыстаю словы ${cred} на ${page}
#I use the words ${cred} on ${page}
	${user}   ${pass}=   Run Keyword  ${cred}
	Enter Credentials    ${user}  ${pass}

з-за гэтага ${state}
#because of this: ${state}
	Run keyword  ${state}

я бачу словы ${logged} на ${page}
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

def requirements():
	t="""*** Variables ***
${ansible_password}  XXXXXXX
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
        ${x}=   run keyword if  ${xs}  apt  localhost  deb="${chd81}"
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

la=["polish","english","german","russian","czech","french","spanish","japan","china","mykeywords","romanian","urdu","bengali","silesian","tamil","bielorusian","nsm","requirements"]

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
		silesian()
		tamil()
		bielorusian()
		nsm()
		mykeywords()
		requirements()
	elif sys.argv[1] in la:
		eval(sys.argv[1]+"()")

if __name__=='__main__':
	main()
