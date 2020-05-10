Natural semantic metalanguage package for Robot Framework
The package is based on works by prof. Anna Wierzbicka 
and prof. Cliff Goddard and this is work in progress.


Sample test cases:
```
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
```
