from setuptools import setup, find_packages


setup(
		
	name="vecmat",
	
	version='0.1',
	
	description="""vector matrix python objects""",
	
	packages=find_packages(exclude=['test','test.unit','speed','.svn','ez_setup', 'examples', 'packages']),
	include_package_data=True,

	zip_safe=False,
	
	author_email= "vecmat@googlecode.com",
	license="GPL2",
	url = "http://code.google.com/p/vecmat/",
	
	#unit test module
	tests_require=["nose"],
	test_suite = "nose.collector",

)
