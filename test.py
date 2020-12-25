import os
from PIL import Image, ImageChops, ImageColor

METALS = {
    'chromium':{
        'color': '#AF7CAA',
        'usable': True,
        'tool_metal': True
    },
    'aluminium_steel':{
        'color': '#8FA5A6',
        'usable': True,
        'tool_metal': True
    },
    'weak_aluminium_steel':{
        'color': '#8FA5A6',
        'usable': False,
        'tool_metal': False
    }
}

METAL_TYPES = {
    'ingot': False,
    'double_ingot': False,
    'scrap': False,
    'dust': False,
    'nugget': False,
    'sheet': False,
    'double_sheet': False,
    'trapdoor': False,
    'tuyere': True,
    'lamp': False,
    'pick': True,
    'pick_head': True,
    'shovel': True,
    'shovel_head': True,
    'axe': True,
    'axe_head': True,
    'hoe': True,
    'hoe_head': True,
    'chisel': True,
    'chisel_head': True,
    'sword': True,
    'sword_blade': True,
    'mace': True,
    'mace_head': True,
    'saw': True,
    'saw_blade': True,
    'javelin': True,
    'javelin_head': True,
    'hammer': True,
    'hammer_head': True,
    'propick': True,
    'propick_head': True,
    'knife': True,
    'knife_blade': True,
    'scythe': True,
    'scythe_blade': True,
    'shears': True,
    'unfinished_chestplate': True,
    'chestplate': True,
    'unfinished_greaves': True,
    'greaves': True,
    'unfinished_boots': True,
    'boots': True,
    'unfinished_helmet': True,
    'helmet': True,
}

def tint_image(image, tint_color):
    return ImageChops.multiply(image, Image.new('RGBA', image.size, tint_color))

def save(type_name, metal, color, tool_metal):
    isTool = METAL_TYPES[type_name]
    file = Image.open('./template/'+type_name+'.png')
    result = tint_image(file, color)
    if(tool_metal and isTool) or type_name == 'lamp' :
        if not(type_name.endswith('head') or type_name.endswith('blade') or type_name.endswith('chestplate') or type_name.endswith('greaves') or type_name.endswith('boots') or type_name.endswith('helmet') or type_name == 'tuyere' or type_name == 'shield') :
            result = Image.alpha_composite(Image.open('./template/'+type_name+'_base.png'), result)
    if(type_name == 'trapdoor') :
        os.makedirs('./out/blocks/'+type_name)
        result.save('./out/blocks/'+type_name+'/'+metal+'.png')
    else :
        os.makedirs('./out/items/metal/'+type_name)
        result.save('./out/items/metal/'+type_name+'/'+metal+'.png')

def tint(metal, info):
    metalColor = ImageColor.getrgb(info['color'])
    metal_tool = info['tool_metal']
    if(info['usable'] == False) :
        save('ingot', metal, metalColor, False)
    else :
        for metal_type in METAL_TYPES.keys() :
            save(metal_type, metal, metalColor, metal_tool)

for metal in METALS.keys() :
    tint(metal, METALS[metal])
