
import os, json
from PIL import Image, ImageChops, ImageColor, ImagePalette

def readJSON(file_name) :
    file = open(file_name, 'r')
    return json.load(file)

# metals supported
METALS = readJSON('./resources/metals.json')
# types supported
TYPES = readJSON('./resources/types.json')
# overrides
OVERRIDES = readJSON('./resources/overrides.json')

def ColorImage(image, color) :
    rgb = ImageColor.getrgb(color)
    rgb = (int(rgb[0]/0.7), int(rgb[1]/0.7), int(rgb[2]/0.7))
    image = image.convert("RGBA")
    img = Image.new('RGBA', image.size, (rgb[0], rgb[1], rgb[2], 170))
    multiply_image = ImageChops.multiply(img, image)
    overlay_image = ImageChops.overlay(multiply_image, image)
    return overlay_image

for metal_name in METALS.keys() :
    # metal dict
    metal = METALS.get(metal_name)
    
    # metal color
    metal_color = metal.get('color')
    
    # if the metal is usable? meaning we will only generate ingot and block texture
    metal_is_usable = metal.get('usable')

    # metal is a tool metal? meaning we will generate tools and armors texture.
    metal_is_tool = metal.get('tool_metal')

    metal_mod = metal.get('mod')

    if metal_is_usable :
        for type_name in TYPES.keys() :
            
            
            # get the type dict
            item_type = TYPES.get(type_name)

            # check if the type is a block  type
            type_is_block = item_type.get('isBlock')

            # check if the type is a weapon type. meaning it will generate tools, armors and more if the metal is a tool metal
            type_is_weapon = item_type.get('isWeapon')

            # check if the type has a texture override
            type_has_default = False
            if item_type in OVERRIDES :
                item_override = OVERRIDES.get(item_type)
                type_has_default = metal_name in item_override

            # get the type base texture if it has one. if it doesn't have one the base texture is ''
            base_texture = item_type.get('base_texture')

            # get the type texture
            texture = item_type.get('texture')

            mod_id = item_type.get('mod')

            if (metal_mod == 'tfc' or metal_mod == 'tfcmetallum') and mod_id == 'tfc':
                continue

            # debug print
            #print(metal_name, type_name)

            # paths
            texture_path = './template/%s.png' % texture
            base_texture_path = './template/%s.png' % base_texture
            output_path = './out/assets/%s/textures/items/metal/%s' % (mod_id, type_name)

            # block
            if type_is_block :
                output = 'metal' if type_name == 'block' else type_name
                output_path =  './out/assets/%s/textures/block/%s' % (mod_id, output)
            if type_name == 'armor_layer_1' or type_name == 'armor_layer_2' :
                output_path = './out/textures/models/armor'

            # images
            image = Image.open(texture_path)
            base_image = None

            result = ColorImage(image, metal_color)

            if not base_texture == '' :
                base_image = Image.open(base_texture_path)
                base_image = base_image.convert('RGBA')

                result = Image.alpha_composite(base_image, result)

            if not(not metal_is_tool and type_is_weapon)  :
                os.makedirs(output_path, exist_ok=True)
                
                if type_name == 'armor_layer_1' or type_name == 'armor_layer_2' :
                    result.save(output_path+'/%s.png' % type_name.replace('armor', metal_name))
                if type_is_block :
                    result.save(output_path+'/%s.png' % metal_name)
                else : 
                    result.save(output_path+'/'+metal_name+'.png')

    else :
        # metal is not usable, we only generate ingot and block texture
        print('')

