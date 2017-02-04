#!/bin/env python
# -*- coding: utf-8 -*-

import subprocess

class PuppetInst:
	puppetrep = "https://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm"	
	yumrepo   = "epel-release"	
	
	codesucess = 0
   
	def __init__(self):
		self.install_repo()
		self.do_install()

	def install_repo(self):
		subprocess.call("yum install " + self.yumrepo, shell = True)
		subprocess.call("rpm -Uvh " + self.puppetrep, shell = True)

	def do_install(self):
		if subprocess.call("which puppet", shell = True) != self.codesucess:
			subprocess.call("yum install puppet -y", shell = True)

			subprocess.call('echo "export PATH=/opt/puppetlabs/bin:$PATH" > /etc/profile.d/puppet_path.sh',shell = True)
			subprocess.call("source /etc/profile.d/puppet_path.sh")

			if subprocess.call("puppet --version", shell = True) == self.codesucess:
				print "Instacao realizada com sucesso."
			else:
				print "Ocorreu um erro na instalacao. Contate o desenvolvedor do programa."
		else:
			print "O puppet ja esta instalado. Nenhuma operacao sera realizada."


if __name__ == "__main__":
	try:
		PuppetInst()
	except:
		print "Ocorreu o erro na execucao da instalacao. Operacao mal sucedida."

