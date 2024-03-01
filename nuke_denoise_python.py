import os, re

# project file name
projname = nuke.root()['name'].value()

# get the current write node
this_write = nuke.thisNode()
# get precomp task
task_name = this_write['task'].value()

# get write type selection
renderType = this_write['render_type'].value()

# make sure create directories is always checked
this_write['create_directories'].setValue(1)

def precompPlateName():
	this_write['views'].setValue('main')
	#project file directory
	projdir = os.path.dirname(projname)

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

	write_name = topnode_base.rsplit('.', 1)[0] + '_' + task_name + '_' + proj_version

	full_write_path = f'{renders_folder}/precomps/{write_name}/{write_name}.####.exr'

	# Set the path to the knob
	this_write['do_not_modify'].setValue(full_write_path)


def precompCompName():
	this_write['views'].setValue('main')
	render_path = projname.replace("project_files", "renders")
	render_path = render_path.replace(".nk", ".####.exr")
	render_path = render_path.replace("comp_v", "comp_" + task_name + "_v")
	render_subfolder = os.path.splitext(os.path.splitext(os.path.basename(render_path))[0])[0]
	render_path = render_path.replace("/comp/", "/comp/precomps/" + render_subfolder + "/")
	this_write['do_not_modify'].setValue(render_path)



def renderMain():
	render_path = projname.replace("project_files", "renders")
	render_path = render_path.replace(".nk", ".mov")
	this_write['do_not_modify'].setValue(render_path)


def renderReview():
	render_path = projname.replace("project_files", "renders")
	render_path = render_path.replace(".nk", "_review.mov")
	this_write['do_not_modify'].setValue(render_path)


def renderSwitch():
	if renderType == "main (final)":
		renderMain()
	elif renderType == "main (review)":
		renderReview()
	elif renderType == "precomp (plate name)":
		precompPlateName()
	elif renderType == "precomp (comp name)":
		precompCompName()
	else:
		pass

renderSwitch()