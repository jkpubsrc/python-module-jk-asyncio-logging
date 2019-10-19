################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"License :: OSI Approved :: Apache Software License",
		"Topic :: Software Development :: Testing",
		"Topic :: System :: Logging",
	],
	description = "This is a logging framework. It is based on jk_logging but can be used with Asyncio.",
	download_url = "https://github.com/jkpubsrc/python-module-jk-asyncio-logging/tarball/0.2019.10.19",
	include_package_data = False,
	install_requires = [
		"jk_logging",
		"jk_asyncio_syncasync",
	],
	keywords = [
		"debugging",
		"logging",
		"asyncio",
	],
	license = "Apache 2.0",
	name = "jk_asyncio_logging",
	packages = [
		"jk_asyncio_logging",
	],
	url = "https://github.com/jkpubsrc/python-module-jk-asyncio-logging",
	version = "0.2019.10.19",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)