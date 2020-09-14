#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import re
import pprint
import nsm

def nname(s):
	return reduce(lambda a,b: a.replace(b,""),[s]+list("${}:+^[]")).replace(" ","_").lower()

class nsm_test(type):
	def __init__(cls, name, bases, nmspc):
		super(nsm_test, cls).__init__(name, bases, nmspc)
		cls.uses_metaclass = lambda self : True
		cls.test_sem2 = lambda self : self.assertTrue(True)
		t="setattr_test"
		setattr(cls,"test_%s" % t.replace('.',"_"),lambda self: self.checker(t))
		kws=re.findall(r"(?mi)^[^ \t\n#].*",file("NSM.robot").read().split("*** Keywords ***")[1])
		cls.nsmkw={}
		cls.examples={}
		for la in nsm.langs:
			wyn=[]
			for l in kws.__getslice__(*nsm.langs[la]):
				if l.strip(): wyn.append(l)
			wyn1=[l for l in re.findall(r"(?mi)^[ \t]+(.*)",file("%s.robot" %la).read())]
			cls.nsmkw[la]=wyn
			cls.examples[la]=wyn1
			cls.nsm=nsm.nsm()
			for f in [e for e in enumerate(wyn)]: 
				setattr(cls,"test_%s" % nname(f[1]),(lambda g,lal: lambda self: self.checker(g,lal))(f,la))
			for f in [e for e in enumerate(wyn)]: 
				setattr(cls,"test_member_%s" % nname(f[1]),(lambda g,lal: lambda self: self.member_checker(g,lal))(f,la))

class test_sem_NSM(unittest.TestCase):
	__metaclass__ = nsm_test

	def checker(self,n,lang="polish"):
		if n=='setattr_test':
			self.assertTrue(True)
		else:
			self.assertIsInstance(self.examples[lang],list)
			d=nsm.NSMfu(self.examples[lang],lang)
			self.assertIn(n[1],d.values(),pprint.pformat(d))
			self.assertIn(n[0],d)
			self.assertEqual(n[1],d[n[0]])

	def member_checker(self,n,lang="polish"):
		d=[getattr(self.nsm,"%s_fun%d" % (lang,nr)).__func__.robot_name.encode("utf-8") for nr in range(8)]
		self.assertIn(n[1],d)

	def test_sem(self):
		self.assertTrue(True)

	def test_meta(self):
		self.assertTrue(self.uses_metaclass())

	def test_first(self):
		self.assertEqual(self.nsmkw["polish"][0],'Teraz jest tak: ${state}')

	def test_len(self):
		self.assertEqual(len(nsm.NSMfu(self.examples["polish"],"polish")),8
			,pprint.pformat(nsm.NSMfu(self.examples["polish"],"polish")))

	def test_len_en(self):
		self.assertEqual(len(nsm.NSMfu(self.examples["english"],"english")),8
			,pprint.pformat(nsm.NSMfu(self.examples["english"],"english")))

	def test_no_duplicates(self):
		g=nsm.NSMfu(self.examples)
		g1=sorted(g)
		g2=sorted(list(set(g)))
		self.assertEqual(g1,g2)

if __name__=="__main__":
	unittest.main()
