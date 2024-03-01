import os, re

def precompName():
	# project file name
	projname = nuke.root()['name'].value()
	#project file directory
	projdir = os.path.dirname(projname)

	# get the current write node
	this_write = nuke.thisNode()

	# get name of top node with tcl
	topnode_name = nuke.tcl("full_name [topnode %s]" % this_write.name())
	# get actual top node with python
	topnode = nuke.toNode(topnode_name)
	# get file value of top node
	topnode_file = topnode['file'].value()

	topnode_base = os.path.basename(topnode_file)

	# Regular expression to match the version pattern
	version_pattern = r"v\d+"

	# Search for the version pattern in the file path
	version_match = re.search(version_pattern, projname)

	# Extract the version string if found
	proj_version = version_match.group(0) if version_match else "No version found"

	# Replace "project_files" with "renders"
	renders_folder = projdir.replace("project_files", "renders")
	renders_folder = renders_folder.replace("/Volumes/Macintosh HD", "")

	task_name = this_write['task'].value()

	write_name = topnode_base.rsplit('.', 1)[0] + '_' + task_name + '_' + proj_version

	full_write_path = f'{renders_folder}/precomps/{write_name}/{write_name}.####.exr'

	# Set the path to the knob
	nuke.thisNode()['do_not_modify'].setValue(full_write_path)

	nuke.thisNode()['create_directories'].setValue(1)



precompName()





