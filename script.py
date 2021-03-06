import os
from PIL import Image, ImageChops, ImageColor, ImagePalette

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
    },
    'bismuth_steel': {
        'color': '#32505A',
        'usable': True,
        'tool_metal': True
    },
    'weak_bismuth_steel': {
        'color': '#32505A',
        'usable': False,
        'tool_metal': False
    },
    'damascus_steel': {
        'color': '#9B8E85',
        'usable': True,
        'tool_metal': True
    },
    'weak_damascus_steel': {
        'color': '#9B8E85',
        'usable': False,
        'tool_metal': False
    },
    'stainless_steel': {
        'color': '#5C8D9D',
        'usable': True,
        'tool_metal': True
    },
    'weak_stainless_steel': {
        'color': '#5C8D9D',
        'usable': False,
        'tool_metal': False
    },
    'rose_alloy': {
        'color': '#453D30',
        'usable': True,
        'tool_metal': False
    },
    'ferrochrome': {
        'color': '#4A4A64',
        'usable': True,
        'tool_metal': False
    },
    'cadmium': {
        'color': '#5C5C5E',
        'usable': True,
        'tool_metal': False
    },
    'nichrome': {
        'color': '#77898E',
        'usable': True,
        'tool_metal': True
    },
    'alnico': {
        'color': '#F9A135',
        'usable': True,
        'tool_metal': False
    },
    'vanadium': {
        'color': '#5C5677',
        'usable': True,
        'tool_metal': False
    },
    'rhodium': {
        'color': '#9F9393',
        'usable': True,
        'tool_metal': False
    },
    'palladium': {
        'color': '#ADA895',
        'usable': True,
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
    'shield': True,
    'armor_layer_1': True,
    'armor_layer_2': True,
    'ingot_mold': False,
    'block': False
}

def translation(metal, info):
    usable = info['usable']
    tool_metal = info['tool_metal']

    output = '\n\n#Metal: %s\n' % metal
    output+= 'tfc.types.metal.%s=%s' % (metal, Upper(metal))
    output+='\nfluid.%s=Molten %s' % (metal, Upper(metal))

    if not(usable) :
        output+='\nitem.tfc.metal.ingot.%s.name=%s Ingot' % (metal, Upper(metal))
    if tool_metal :
        output+='\nitem.tfc.metal.anvil.%s.name=%s Anvil' % (metal, Upper(metal))
    else :
        for types in METAL_TYPES.keys() :
            value = METAL_TYPES[types]
            if not(tool_metal and value) or (tool_metal and value) :
                if(types == 'trapdoor') :
                    output+='\ntile.tfc.%s.%s.name=%s %s' % (types,metal, Upper(metal), Upper(types))
                elif types not in ['block'] :
                    if(types.startswith('unfinished')) :
                        ah = types.replace('_', ' %s ' % metal)
                        output+='\nitem.tfc.metal.%s.%s.name=%s' % (types,metal, Upper(ah))
                    elif types.__contains__('mold') :
                        output+='\nitem.tfc.ceramics.fired.mold.%s.%s.name=Unshaped %s' % (types.removesuffix('_mold'),metal, Upper(metal))
                    else :
                        output+='\nitem.tfc.metal.%s.%s.name=%s %s' % (types,metal, Upper(metal), Upper(types))
    os.makedirs('./out/lang', exist_ok=True)
    f = open('./out/lang/en_us.lang', 'a')
    f.write(output)
    f.close()

def Upper(s) :
    splitString = s.replace('_', ' ').title()
    return splitString

def tint_image(image, tint_color):
    return ImageChops.multiply(image, Image.new('RGBA', image.size, tint_color))

def save(type_name, metal, color, tool_metal):

    # boolean used to check if the type is a tool type
    isTool = METAL_TYPES[type_name]

    # open the file
    file = Image.open('./template/'+type_name+'.png')

    # tint the image
    result = tint_image(file, color)

    if type_name.__contains__('mold') :
        result = Image.alpha_composite(Image.open('./template/'+type_name+'_base.png'), result)

    # if it's a tool composite the base image
    if type_name in ['axe', 'chisel', 'hammer', 'hoe', 'javelin', 'knife', 'lamp', 'mace', 'pick', 'propick', 'saw', 'scythe', 'shears', 'shovel', 'sword'] :
        if tool_metal and isTool :
            result = Image.alpha_composite(Image.open('./template/'+type_name+'_base.png'), result)
    
    if  type_name == 'trapdoor' :
        os.makedirs('./out/textures/blocks/'+type_name, exist_ok=True)
        result.save('./out/textures/blocks/'+type_name+'/'+metal+'.png')
    elif type_name == 'armor_layer_1' or type_name == 'armor_layer_2' :
        os.makedirs('./out/textures/models/armor', exist_ok=True)
        result.save('./out/textures/models/armor/'+type_name.replace('armor', metal)+'.png')
    elif type_name.__contains__('mold') :
        os.makedirs('./out/textures/items/ceramics/fired/mold/'+type_name.removesuffix('_mold'), exist_ok=True)
        result.save('./out/textures/items/ceramics/fired/mold/'+type_name.removesuffix('_mold')+'/'+metal+'.png')
    elif type_name == 'block' :
        os.makedirs('./out/textures/blocks/metal/', exist_ok=True)
        result.save('./out/textures/blocks/metal/'+metal+'.png')
    else :
        os.makedirs('./out/textures/items/metal/'+type_name, exist_ok=True)
        if (not isTool and not tool_metal) or (isTool and tool_metal) or (not isTool and tool_metal):
            result.save('./out/textures/items/metal/'+type_name+'/'+metal+'.png')

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