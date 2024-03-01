# set exr precomp defaults

this_write = nuke.thisNode()
this_write['file_type'].setValue('exr')
this_write['datatype'].setValue('16 bit half')
this_write['compression'].setValue('none')
this_write['transformType'].setValue('colorspace')