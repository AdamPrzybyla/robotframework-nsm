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
		wyn=[]
		for l in re.findall(r"(?mi)^[^ \t\n#].*",file("NSM.robot").read().split("*** Keywords ***")[1])[8:16]:
			if l.strip(): wyn.append(l)
		wyn1=[]
		for l in re.findall(r"(?mi)^[ \t]+(.*)",file("polish.robot").read()): wyn1.append(l)
		cls.uses_metaclass = lambda self : True
		cls.test_sem2 = lambda self : self.assertTrue(True)
		cls.nsmkw=wyn
		cls.examples=wyn1
		t="setattr_test"
		setattr(cls,"test_%s" % t.replace('.',"_"),lambda self: self.checker(t))
		for f in [e for e in enumerate(wyn)]: 
			setattr(cls,"test_%s" % nname(f[1]),(lambda g: lambda self: self.checker(g)) (f))

class test_sem_NSM(unittest.TestCase):
	__metaclass__ = nsm_test

	def checker(self,n):
		if n=='setattr_test':
			self.assertTrue(True)
		else:
			self.assertIsInstance(self.examples,list)
			d=nsm.NSMfu(self.examples)
			self.assertIn(n[1],d.values())
			self.assertIn(n[0],d)
			self.assertEqual(n[1],d[n[0]])

	def test_sem(self):
		self.assertTrue(True)

	def test_meta(self):
		self.assertTrue(self.uses_metaclass())

	def test_first(self):
		self.assertEqual(self.nsmkw[0],'Teraz jest tak: ${state}')

	def test_len(self):
		self.assertEqual(len(nsm.NSMfu(self.examples)),8)

	def test_no_duplicates(self):
		g=nsm.NSMfu(self.examples)
		g1=sorted(g)
		g2=sorted(list(set(g)))
		self.assertEqual(g1,g2)

if __name__=="__main__":
	unittest.main()
