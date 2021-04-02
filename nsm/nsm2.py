#! /usr/bin/python
# -*- coding: utf-8 -*-

from .nsm import NSMfu,langs
from robot.running import Keyword
from robot.running.context import EXECUTION_CONTEXTS
import re,pprint,os

class genNSM(type):
	def __init__(cls, name, bases, nmspc):
		super(genNSM, cls).__init__(name, bases, nmspc)
		cls.uses_metaclass = lambda self : True
		for la in langs:
			wyn1=[]
			if not os.path.exists("%s.robot" % la):
				continue
			for l in re.findall(r"(?mi)^[ \t]+(.*)",file("%s.robot" % la).read()): wyn1.append(l)
			funpar=NSMfu(wyn1,la)
			for st,name in funpar.items():
				n="%s_fun%d" % (la,st)
				if st in [0,3,5]:
					setattr(cls,n,(lambda k: lambda self,p1: self.call_p1(p1))(n))
				elif st==7:
					setattr(cls,n,(lambda k: lambda self,p1: self.call_p2(p1))(n))
				elif st==6:
					setattr(cls,n,(lambda k: lambda self,p1: self.call_p6(p1))(n))
				elif st==1:
					if la=="czech" or la=="japan" or la=="china" or la=='tamil':
						setattr(cls,n,(lambda k: lambda self,p1,p2: self.call_p2p(p2,p1))(n))
					else:
						setattr(cls,n,(lambda k: lambda self,p1,p2: self.call_p2p(p1,p2))(n))
				elif st==2:
					if la=="japan" or la=="china" or la=='tamil':
						setattr(cls,n,(lambda k: lambda self,p1,p2: self.call_p3p(p2,p1))(n))
					else:
						setattr(cls,n,(lambda k: lambda self,p1,p2: self.call_p3p(p1,p2))(n))
				elif st==4:
					if la=="czech" or la=="japan" or la=="china" or la=='bengali' or la=='tamil':
						setattr(cls,n,(lambda k: lambda self,p1,p2: self.call_p4p(p2,p1))(n))
					else:
						setattr(cls,n,(lambda k: lambda self,p1,p2: self.call_p4p(p1,p2))(n))
				getattr(cls,n).__func__.robot_name=name.decode("utf-8")
			
class nsm(object):
	ROBOT_LIBRARY_VERSION = '0.18'
	__metaclass__ = genNSM

	def call_p1(self,p1):
		kw = Keyword(p1, args=[])
		return kw.run(EXECUTION_CONTEXTS.current)

	def call_p2(self,p1):
		pw="%s setup" %  p1
		kw = Keyword(pw, args=[])
		return kw.run(EXECUTION_CONTEXTS.current)

	def call_p6(self,p1):
		pw="%s teardown" %  p1
		kw = Keyword(pw, args=[])
		return kw.run(EXECUTION_CONTEXTS.current)

	def call_p2p(self,p1,p2):
		kw = Keyword(p1, args=[])
		words = kw.run(EXECUTION_CONTEXTS.current)
		pw="%s check" %  p2
		kw = Keyword(pw, args=[words])
		result = kw.run(EXECUTION_CONTEXTS.current)
		kw = Keyword("Should not be equal", args=["OK",result])
		return kw.run(EXECUTION_CONTEXTS.current)

	def call_p3p(self,p1,p2):
		kw = Keyword(p1, args=[])
		user,passwd = kw.run(EXECUTION_CONTEXTS.current)
		pw="Enter Credentials"
		kw = Keyword(pw, args=[user,passwd])
		return kw.run(EXECUTION_CONTEXTS.current)

	def call_p4p(self,p1,p2):
		kw = Keyword(p1, args=[])
		words = kw.run(EXECUTION_CONTEXTS.current)
		pw="%s check" %  p2
		kw = Keyword(pw, args=[words])
		result = kw.run(EXECUTION_CONTEXTS.current)
		kw = Keyword("Should be equal", args=["OK",result])
		return kw.run(EXECUTION_CONTEXTS.current)

