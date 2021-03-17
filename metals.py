
import os
from PIL import Image, ImageChops, ImageColor, ImagePalette
# item.ironbackpacks.backpack.tfcompat.metal_name.name=metal_name Backpack

SUPPORTED_MODS = {
    'tfcompat': {
        'loaded': True,
        'types': {
            'backpack': {
                'textures': [
                    'mods/ironbackpacks/backpack/base',
                ],
                'lang': 'item.ironbackpacks.backpack.tfcompat.%metal%.name=%upper_metal% Backpack'
            }
        }
    },
    'firmalife': {
        'loaded': True
    }
    
}

TFC_METALS = {
    'copper': {
        'color': '#AF7CAA',
        'usable': True,
        'tool_metal': True
    },
}

MODDED_METALS = {
    'tfc_metallum': {
        'aluminium': {
            'color': '#D9FBFC',
            'usable': True,
            'tool_metal': True
        },
        'aluminium_brass': {
            'color': '#DCDABE',
            'usable': True,
            'tool_metal': False
        },
        'antimony': {
            'color': '#E7E7F5',
            'usable': True,
            'tool_metal': False
        },
        'ardite': {
            'color': '#F09614',
            'usable': True,
            'tool_metal': False
        },
        'cobalt': {
            'color': '#6CA6E5',
            'usable': True,
            'tool_metal': True
        },
        'constantan': {
            'color': '#D28874',
            'usable': True,
            'tool_metal': False
        },
        'electrum': {
            'color': '#DFB950',
            'usable': True,
            'tool_metal': True
        },
        'invar': {
            'color': '#AAAA9E',
            'usable': True,
            'tool_metal': True
        },
        'manyullyn': {
            'color': '#B052C0',
            'usable': True,
            'tool_metal': True
        },
        'mithril': {
            'color': '#8ADAF6',
            'usable': True,
            'tool_metal': True
        },
        'osmium': {
            'color': '#B8D8DE',
            'usable': True,
            'tool_metal': True
        },
        'titanium': {
            'color': '#C2C4CC',
            'usable': True,
            'tool_metal': True
        },
        'tungsten': {
            'color': '#41454B',
            'usable': True,
            'tool_metal': False
        },
        'tungsten_steel': {
            'color': '#565F6E',
            'usable': True,
            'tool_metal': True
        },
        'nickel_silver': {
            'color': '#A4A4A5',
            'usable': True,
            'tool_metal': True
        },
        'red_alloy': {
            'color': '#DA6E6E',
            'usable': True,
            'tool_metal': False
        },
        'boron': {
            'color': '#252525',
            'usable': True,
            'tool_metal': True
        },
        'ferroboron': {
            'color': '#4B4B4B',
            'usable': True,
            'tool_metal': True
        },
        'thorium': {
            'color': '#3D4548',
            'usable': True,
            'tool_metal': False
        },
        'lithium': {
            'color': '#C9CBC3',
            'usable': True,
            'tool_metal': False
        },
        'manganese': {
            'color': '#9397A8',
            'usable': True,
            'tool_metal': False
        },
        'magnesium': {
            'color': '#978195',
            'usable': True,
            'tool_metal': False
        },
        'beryllium': {
            'color': '#E4EADA',
            'usable': True,
            'tool_metal': False
        },
        'beryllium_copper': {
            'color': '#EAAE90',
            'usable': True,
            'tool_metal': True
        },
        'zirconium': {
            'color': '#747527',
            'usable': True,
            'tool_metal': False
        },
        'zircaloy': {
            'color': '#43423A',
            'usable': True,
            'tool_metal': True
        },
        'hsla_steel': {
            'color': '#3F4180',
            'usable': True,
            'tool_metal': False
        }
    },
    'tfcompat': {
        'enderium': {
            'color': '#0E6A6A',
            'usable': True,
            'tool_metal': True
        },
        'signalum': {
            'color': '#A13800',
            'usable': True,
            'tool_metal': True
        },
        'lumium': {
            'color': '#FFE46A',
            'usable': True,
            'tool_metal': True
        },
        'thaumium': {
            'color': '#5A4B8B',
            'usable': True,
            'tool_metal': True
        },
        'void_metal': {
            'color': '#2D1847',
            'usable': True,
            'tool_metal': False
        },
        'refined_iron': {
            'color': '#AF7CAA',
            'usable': True,
            'tool_metal': True
        }
    },
    'tfcflux': {
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
            'usable': False,
            'tool_metal': False
        },
        'rhodium': {
            'color': '#9F9393',
            'usable': False,
            'tool_metal': False
        },
        'palladium': {
            'color': '#ADA895',
            'usable': False,
            'tool_metal': False
        }

    }
}

Metal_Types = {
    'ingot': {
        'isWeapon': False,
        'isBlock': False,
        'texture': 'ingot',
        'base_texture': ''
    },
    'double_ingot': {
        'isWeapon': False,
        'isBlock': False,
        'texture': 'double_ingot',
        'base_texture': ''
    },
    'scrap': {
        'isWeapon': False,
        'isBlock': False,
        'texture': 'scrap',
        'base_texture': ''
    },
    'dust': {
        'isWeapon': False,
        'texture': 'dust',
        'base_texture': ''
    },
    'nugget': {
        'isWeapon': False,
        'isBlock': False,
        'texture': 'nugget',
        'base_texture': ''
    },
    'sheet': {
        'isWeapon': False,
        'isBlock': False,
        'texture': 'sheet',
        'base_texture': ''
    },
    'double_sheet': {
        'isWeapon': False,
        'isBlock': False,
        'texture': 'double_sheet',
        'base_texture': ''
    },
    'tuyere': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'tuyere',
        'base_texture': ''
    },
    'lamp': {
        'isWeapon': False,
        'isBlock': False,
        'texture': 'lamp',
        'base_texture': 'lamp_base'
    },
    'pick': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'pick',
        'base_texture': 'pick_base'
    },
    'pick_head': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'pick_head',
        'base_texture': ''
    },
    'shovel': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'shovel',
        'base_texture': 'shovel_base'
    },
    'shovel_head': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'shovel',
        'base_texture': ''
    },
    'axe': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'axe',
        'base_texture': 'axe_base'
    },
    'axe_head': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'axe_head',
        'base_texture': ''
    },
    'hoe': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'hoe',
        'base_texture': 'hoe_base'
    },
    'hoe_head': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'hoe_head',
        'base_texture': ''
    },
    'chisel': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'chisel',
        'base_texture': 'chisel_base'
    },
    'chisel_head': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'chisel_head',
        'base_texture': ''
    },
    'sword': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'sword',
        'base_texture': 'sword_base'
    },
    'sword_blade': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'sword_blade',
        'base_texture': ''
    },
    'mace': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'mace',
        'base_texture': 'mace_base'
    },
    'mace_head': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'mace_head',
        'base_texture': ''
    },
    'saw': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'saw',
        'base_texture': 'saw_base'
    },
    'saw_blade': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'saw_blade',
        'base_texture': ''
    },
    'javelin': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'javelin',
        'base_texture': 'javelin_base'
    },
    'javelin_head': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'javelin_head',
        'base_texture': ''
    },
    'hammer': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'hammer',
        'base_texture': 'hammer_base'
    },
    'hammer_head': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'hammer_head',
        'base_texture': ''
    },
    'propick': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'propick',
        'base_texture': 'propick_base'
    },
    'propick_head': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'propick_head',
        'base_texture': ''
    },
    'knife': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'knife',
        'base_texture': 'knife_base'
    },
    'knife_blade': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'knife_blade',
        'base_texture': ''
    },
    'scythe': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'scythe',
        'base_texture': 'scythe_base'
    },
    'scythe_blade': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'scythe_blade',
        'base_texture': ''
    },
    'shears': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'shears',
        'base_texture': 'shears_base'
    },
    'unfinished_helmet': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'unfinished_helmet',
        'base_texture': ''
    },
    'unfinished_chestplate': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'unfinished_chestplate',
        'base_texture': ''
    },
    'unfinished_greaves': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'unfinished_greaves',
        'base_texture': ''
    },
    'unfinished_boots': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'unfinished_boots',
        'base_texture': ''
    },
    'helmet': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'helmet',
        'base_texture': ''
    },
    'chestplate': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'chestplate',
        'base_texture': ''
    },
    'greaves': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'greaves',
        'base_texture': ''
    },
    'boots': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'boots',
        'base_texture': ''
    },
    'shield': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'shield',
        'base_texture': ''
    },
    'armor_layer_1': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'armor_layer_1',
        'base_texture': ''
    },
    'armor_layer_2': {
        'isWeapon': True,
        'isBlock': False,
        'texture': 'armor_layer_2',
        'base_texture': ''
    },
    'block': {
        'isWeapon': False,
        'isBlock': True,
        'texture': 'block',
        'base_texture': ''
    },
    'trapdoor': {
        'isWeapon': False,
        'isBlock': True,
        'texture': 'trapdoor',
        'base_texture': ''
    },
}

# metal stuff
def getMetal(METALS, metal_name) :
    """
    Returns
    -------
    dict
    """
    return METALS.get(metal_name)
def getColor(metal) :
    return metal.get('color')
def isUsable(metal) :
    return metal.get('usable')
def isToolMetal(metal) :
    return metal.get('tool_metal')
def hasDefaultKey(metal, key) :
    return key in metal.get('default')

# type stuff
def getType(type_name) :
    return Metal_Types.get(type_name)
def isTypeWeapon(type_name) :
    return getType(type_name).get('isWeapon')
def getTexture(type_name) :
    return getType(type_name).get('texture')
def isTypeBlock(type_name) :
    return getType(type_name).get('isBlock')
def getBaseTexture(type_name) :
    return getType(type_name).get('base_texture')
def hasBaseTexture(type_name) :
    return not ( getBaseTexture(type_name) == '' )

def ColorImage(image, color) :
    rgb = ImageColor.getrgb(color)
    image = image.convert("RGBA")
    img = Image.new('RGBA', image.size, (rgb[0], rgb[1], rgb[2], 170))
    multiply_image = ImageChops.multiply(img, image)
    overlay_image = ImageChops.overlay(multiply_image, image)
    return overlay_image

# metals

tfcflux_metals = MODDED_METALS.get('tfcflux')

for metal_name in tfcflux_metals.keys() :
    # metal dict
    metal = getMetal(tfcflux_metals, metal_name)
    
    # metal color
    metal_color = getColor(metal)
    
    # if the metal is usable? meaning we will only generate ingot and block texture
    metal_is_usable = isUsable(metal)

    # metal is a tool metal? meaning we will generate tools and armors texture.
    metal_is_tool = isToolMetal(metal)

    if metal_is_usable :
        for type_name in Metal_Types.keys() :
            
            # get the type dict
            item_type = getType(type_name)

            # check if the type is a block  type
            type_is_block = isTypeBlock(type_name)

            # check if the type is a weapon type. meaning it will generate tools, armors and more if the metal is a tool metal
            type_is_weapon = isTypeWeapon(type_name)

            # check if the type has a texture override
            #type_has_default = hasDefaultKey(metal, type_name)

            # get the type base texture if it has one. if it doesn't have one the base texture is ''
            base_texture = getBaseTexture(type_name)

            # get the type texture
            texture = getTexture(type_name)

            # debug print
            #print(metal_name, type_name)

            # paths
            texture_path = './template/%s.png' % texture
            base_texture_path = './template/%s.png' % base_texture
            output_path = './out/textures/items/metal/%s' % type_name

            # block
            if type_is_block :
                output = 'metal' if type_name == 'block' else type_name
                output_path =  './out/textures/block/%s/%s' % (output, metal_name)
            if type_name == 'armor_layer_1' or type_name == 'armor_layer_2' :
                output_path = './out/textures/models/armor'

            # images
            image = Image.open(texture_path)
            base_image = None

            result = ColorImage(image, metal_color)

            if hasBaseTexture(type_name) :
                base_image = Image.open(base_texture_path)
                base_image = base_image.convert('RGBA')

                result = Image.alpha_composite(base_image, result)

            if (not metal_is_tool and type_is_weapon) or (metal_is_tool and type_is_weapon) or (metal_is_tool and not type_is_weapon) :
                os.makedirs(output_path, exist_ok=True)
                
                if type_name == 'armor_layer_1' or type_name == 'armor_layer_2' :
                    result.save(output_path+'/%s.png' % type_name.replace('armor', metal_name))
                else : 
                    result.save(output_path+'/'+metal_name+'.png')

    else :
        # metal is not usable, we only generate ingot and block texture
        print('')

