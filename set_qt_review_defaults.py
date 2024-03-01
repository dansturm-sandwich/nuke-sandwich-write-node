# set qt review defaults

this_write = nuke.thisNode()
this_write['file_type'].setValue('mov')
this_write['mov64_codec'].setValue('appr')
this_write['mov64_format'].setValue('mov (QuickTime / MOV)')
this_write['mov_prores_codec_profile'].setValue('ProRes 4:2:2 Proxy 10-bit')
this_write['transformType'].setValue('display')