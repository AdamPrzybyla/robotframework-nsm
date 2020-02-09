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
"""
	open("NSM.robot","w").write(t)

def mykeywords():
	t="""*** Keywords ***
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
	[Return]  OK"""
	open("mykeywords.robot","w").write(t)

la=["polish","english","german","russian","czech","french","spanish","japan","china","mykeywords","nsm"]

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
		nsm()
		mykeywords()
	elif sys.argv[1] in la:
		eval(sys.argv[1]+"()")

if __name__=='__main__':
	main()
