#!/usr/bin/python
# -*- coding: utf-8 -*-
from .nsm import NSMfu,langs
from robot.running import Keyword
from robot.running.context import EXECUTION_CONTEXTS
import re,pprint,os

class gennsm3(type):
	def __call__(self, *args, **kwargs):
		cls = type.__call__(self, *args)
		cls.uses_metaclass = lambda self : True
		for la in langs:
			if not os.path.exists("%s.robot" % la): continue
			wyn1=[l for l in re.findall(r"(?mi)^[ \t]+(.*)",open("%s.robot" %la).read())]
			funpar=NSMfu(wyn1,la)
			for st,name in funpar.items():
				n="%s_fun%d" % (la,st)
				if st in [0,3,5]:
					setattr(cls,n,(lambda k: lambda p1: self.call_p1(p1))(n))
				elif st==7:
					setattr(cls,n,(lambda k: lambda p1: self.call_p2(p1))(n))
				elif st==6:
					setattr(cls,n,(lambda k: lambda p1: self.call_p6(p1))(n))
				elif st==1:
					if la=="czech" or la=="japan" or la=="china" or la=='tamil':
						setattr(cls,n,(lambda k: lambda p1,p2: self.call_p2p(p2,p1))(n))
					else:
						setattr(cls,n,(lambda k: lambda p1,p2: self.call_p2p(p1,p2))(n))
				elif st==2:
					if la=="japan" or la=="china" or la=='tamil':
						setattr(cls,n,(lambda k: lambda p1,p2: self.call_p3p(p2,p1))(n))
					else:
						setattr(cls,n,(lambda k: lambda p1,p2: self.call_p3p(p1,p2))(n))
				elif st==4:
					if la=="czech" or la=="japan" or la=="china" or la=='bengali' or la=='tamil':
						setattr(cls,n,(lambda k: lambda p1,p2: self.call_p4p(p2,p1))(n))
					else:
						setattr(cls,n,(lambda k: lambda p1,p2: self.call_p4p(p1,p2))(n))
				getattr(cls,n).robot_name=name
		return cls

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

class nsm3(object,metaclass=gennsm3):
	ROBOT_LIBRARY_VERSION = '0.18'
