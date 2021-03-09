from PIL import Image

template = Image.new('P', (16, 16), '#AF7CAA')
template = template.convert('PA')
oldimage = Image.open("./template/block.png").convert('PA')
oldimage.putpalette(template.getpalette())
oldimage = oldimage.convert('RGBA')
oldimage.show()