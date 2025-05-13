from setuptools import find_packages, setup


with open("README.md") as f:
	setup(
			name = "GaxaSQLMAP",
			version = "1.0.0",
			packages = find_packages(),
			scripts = ['gaxasqlmap.py', 'nsmmongo.py', 'nsmcouch.py', 'nsmscan.py', 'nsmweb.py', 'exception.py'],
			
			entry_points = {
				"console_scripts": [
					"GaxaSQLMAP = nosqlmap:main"
					]
				},
			
			install_requires = [ "CouchDB==1.0", "httplib2==0.19.0", "ipcalc==1.1.3",\
								 "gaxasqlmap==1.0.0", "pbkdf2==1.3", "pymongo==2.7.2",\
								 "requests==2.20.0"],
	
			author = "isReyy",
			author_email = "aulidanraja@gmail.com",
			description = "Automated MongoDB and NoSQL web application exploitation tool",
			license = "GPLv3",
			long_description = f.read(),
			url = "http://www.nosqlmap.net"
		)
