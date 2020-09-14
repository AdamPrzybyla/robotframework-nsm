#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import re
import pprint
import nsm
import functools

def nname(s):
	return functools.reduce(lambda a,b: a.replace(b,""),[s]+list("${}:+^[]")).replace(" ","_").lower()

class nsm3_test(type):
	def __call__(self, *args, **kwargs):
		cls = type.__call__(self, *args)
		cls.uses_metaclass = lambda  : True
		cls.test_sem2 = lambda self : self.assertTrue(True)
		self.test_sem3 = lambda self : self.assertTrue(True)
		t="setattr_test"
		setattr(cls,"test_%s" % t.replace('.',"_"),lambda : lambda self: self.checker(t)())
		kws=re.findall(r"(?mi)^[^ \t\n#].*",open("NSM.robot").read().split("*** Keywords ***")[1])
		cls.nsmkw={}
		cls.examples={}
		for la in nsm.langs:
			wyn=[]
			z,k=nsm.langs[la]
			for l in kws[z:k]:
				if l.strip(): wyn.append(l)
			wyn1=[l for l in re.findall(r"(?mi)^[ \t]+(.*)",open("%s.robot" %la).read())]
			cls.nsmkw[la]=wyn
			cls.examples[la]=wyn1
		return cls

	def __init__(self, *args, **kwargs):
		self.test_sem6 = lambda self : self.assertTrue(True)
		t="setattr_test"
		setattr(self,"test_%s" % t.replace('.',"_"),lambda : lambda self: self.checker(t)())
		kws=re.findall(r"(?mi)^[^ \t\n#].*",open("NSM.robot").read().split("*** Keywords ***")[1])
		self.nsmkw={}
		self.examples={}
		self.nsm=nsm.nsm()
		for la in nsm.langs:
			wyn=[]
			z,k=nsm.langs[la]
			for l in kws[z:k]:
				if l.strip(): wyn.append(l)
			wyn1=[l for l in re.findall(r"(?mi)^[ \t]+(.*)",open("%s.robot" %la).read())]
			self.nsmkw[la]=wyn
			self.examples[la]=wyn1
			for f in [e for e in enumerate(wyn)]: 
				setattr(self,"test_%s" % nname(f[1]),(lambda g,lal: lambda self: self.checker(g,lal))(f,la))
			for f in [e for e in enumerate(wyn)]: 
				setattr(self,"test_member_%s" % nname(f[1]),(lambda g,lal: lambda self: self.member_checker(g,lal))(f,la))


class test_sem_nsm3(unittest.TestCase,metaclass=nsm3_test):
	def checker(self,n,lang="polish"):
		if n=='setattr_test':
			self.assertTrue(True)
		else:
			self.assertIsInstance(self.examples[lang],list)
			d=nsm.NSMfu(self.examples[lang],lang)
			#print ([d],lang,n)
			self.assertIn(n[1],d.values(),pprint.pformat(d))
			self.assertIn(n[0],d)
			self.assertEqual(n[1],d[n[0]])

	def member_checker(self,n,lang="polish"):
		d=[getattr(self.nsm,"%s_fun%d" % (lang,nr)).robot_name for nr in range(8) if not(lang=="silesian" and nr==3)]
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

