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
    },
    'solder': {
        'color': '#A19A99',
        'usable': True,
        'tool_metal': False
    },
    'kanthal': {
        'color': '#AD9CAB',
        'usable': True,
        'tool_metal': True
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
    'shield': True
}

def translation(metal, info):
    usable = info['usable']
    tool_metal = info['tool_metal']

    output = '\n\n#Metal: %s\n' % metal
    output+= 'types.tfc.metal.%s=%s' % (metal, Upper(metal))
    output+='\nfluid.%s=Molten %s' % (metal, Upper(metal))

    if not(usable) :
        output+='\nitem.tfc.metal.ingot.%s.name=%s Ingot' % (metal, Upper(metal))
    else :
        for types in METAL_TYPES.keys() :
            value = METAL_TYPES[types]
            if (not(tool_metal) and value) or (tool_metal and value) :
                if(types == 'trapdoor') :
                    output+='\ntile.tfc.%s.%s.name=%s %s' % (types,metal, Upper(metal), Upper(types))
                else :
                    if(types.startswith('unfinished')) :
                        ah = types.replace('_', ' %s ' % metal)
                        output+='\nitem.tfc.metal.%s.%s.name=%s' % (types,metal, ah)    
                    else :
                        output+='\nitem.tfc.metal.%s.%s.name=%s %s' % (types,metal, Upper(metal), Upper(types))
    os.makedirs('./out/Lang', exist_ok=True)
    f = open('./out/lang/en_us.lang', 'a')
    f.write(output)
    f.close()

def Upper(s) :
    splitString = s.replace('_', ' ').title()
    return splitString


def tint_image(image, tint_color):
    return ImageChops.overlay(image, Image.new('RGBA', image.size, tint_color))

def save(type_name, metal, color, tool_metal):

    # boolean used to check if the type is a tool type
    isTool = METAL_TYPES[type_name]

    # open the file
    file = Image.open('./template/'+type_name+'.png')
    result = tint_image(file, color)
    if type_name in ['axe', 'chisel', 'hammer', 'hoe', 'javelin', 'knife', 'lamp', 'mace', 'pick', 'propick', 'saw', 'scythe', 'shears', 'shovel', 'sword'] :
        if tool_metal and isTool :
            result = Image.alpha_composite(Image.open('./template/'+type_name+'_base.png'), result)
    
    if(type_name == 'trapdoor') :
        os.makedirs('./out/blocks/'+type_name, exist_ok=True)
        result.save('./out/blocks/'+type_name+'/'+metal+'.png')
    else :
        os.makedirs('./out/items/metal/'+type_name, exist_ok=True)
        if (not isTool and not tool_metal) or (isTool and tool_metal) or (not isTool and tool_metal):
            result.save('./out/items/metal/'+type_name+'/'+metal+'.png')

def tint(metal, info):
    metalColor = ImageColor.getrgb(info['color'])

    # boolean used to check if the metal is a tool metal
    metal_tool = info['tool_metal']

    # if the metal is not usable, you only do it for the
    if(info['usable'] == False) :
        save('ingot', metal, metalColor, False)
    else :
        for metal_type in METAL_TYPES.keys() :
            save(metal_type, metal, metalColor, metal_tool)

for metal in METALS.keys() :

    # provide the metal and the metal information
    tint(metal, METALS[metal])
    translation(metal, METALS[metal])