def write_page(page):
	"""Writes the specified page/module
	To take advantage of this function, a multipage app should be structured into sub-files with a `def write()` function
	Arguments:
		page {module} -- A module with a "def write():" function
	"""
	page.write()
