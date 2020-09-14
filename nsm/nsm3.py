#!/usr/bin/python
# -*- coding: utf-8 -*-
#from __future__ import absolute_import, division, print_function
from .nsm import NSMfu,langs
from robot.running import Keyword
from robot.running.context import EXECUTION_CONTEXTS
import re,pprint,os

class gennsm3(type):
	def call_impansible(self,*p):
		global results
		global resultser
		global ansible_password
		global ansible_user
		global ansible_become_password
		resultser=False
		if p[1].lower()=='local':
			myh="localhost"
		else:
			myh=p[1]
		args1=[u'ansible',u'-u',u'root',u'all',u'--inventory=%s,'%myh, u'-m',p[0]]
		if p[2:]: args1+=[u'-a',u" ".join(p[2:])]
		if p[1].lower()=='local':
			args1+=["-c","local"]
		else:
			try:
				pa = BuiltIn().get_variable_value("${ansible_password}")
			except:
				pa=ansible_password
			if ansible_become_password:
				args1+=["-e","ansible_become=yes","-e",
					"ansible_become_password=%s" % ansible_become_password,
					"-e", "ansible_user=%s" % ansible_user]
			else:
				try:
					bpa = BuiltIn().get_variable_value("${ansible_become_password}")
					buz = BuiltIn().get_variable_value("${ansible_user}")
					if bpa:
						args1+=["-e","ansible_become=yes","-e",
						"ansible_become_password=%s" % bpa,
						"-e", "ansible_user=%s" % buz]
						if not pa: pa=bpa
				except:
					pass
			if pa: args1+=[u'-e',u"ansible_password=%s"%pa]
		results_callback = ResultCallback()
		cli = mycli2(args1,results_callback)
		exit_code = cli.run()
		if resultser:
			raise RuntimeError("%s" % results["msg"])
		return results

	#def __init___z_py2(cls, name, bases, nmspc):
	def __1init__(cls, name, bases, nmspc):
		#super(genNSM, cls).__init__(name, bases, nmspc)
		cls = type.__call__(self, *args)
		cls.uses_metaclass = lambda self : True
		for la in langs:
			wyn1=[]
			if not os.path.exists("%s.robot" % la):
				continue
			for l in re.findall(r"(?mi)^[ \t]+(.*)",open("%s.robot" % la).read()): wyn1.append(l)
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

		return cls



	def __call__old(self, *args, **kwargs):
		cls = type.__call__(self, *args)
		[setattr(cls,n,(lambda n: lambda *arguments: 
		self.call_impansible(n,*arguments))(n)) for n in amodules_map.keys()]
		for n in amodules_map.keys():
			if n in amodules_docs:
				e=getattr(cls,n)
				e.__doc__= amodules_docs[n]
		return cls

	def __call__(self, *args, **kwargs):
		cls = type.__call__(self, *args)
		cls.uses_metaclass = lambda self : True
		for la in langs:
			wyn1=[]
			if not os.path.exists("%s.robot" % la):
				continue
			for l in re.findall(r"(?mi)^[ \t]+(.*)",open("%s.robot" % la).read()): wyn1.append(l)
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
				#getattr(cls,n).__func__.robot_name=name.decode("utf-8")
				#getattr(cls,n).__func__.robot_name=name
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
	ROBOT_LIBRARY_VERSION = '0.16'
