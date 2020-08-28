
from .manager import ICON_PATH
from PIL import Image, ImageOps, ImageDraw, ImageFont
from pathlib import Path
from io import BytesIO
import base64
import re
import os

rgbHex = lambda c:'#{:02x}{:02x}{:02x}'.format( *c )
chunks = lambda l, n: [l[x: x+n] for x in range(0, len(l), n)]
intFloat = lambda v : int(v) if isinstance(v, float) and v.is_integer() else v

def s (**kwargs):
    return 'style="font-family:\'{font}\';font-size:{size}px;color:{color};font-weight:{weight};"'.format(font=kwargs.get("font", "Decorative"), size=kwargs.get("size", 10), weight=kwargs.get("weight", 400),color=rgbHex(kwargs.get("color", (255,255,255))))

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

def toCamelCase (text, separators="_-"):
    cleaned = re.sub('[{}](.)'.format(separators), lambda x: x.group(1).upper(), text)
    return cleaned[0].lower() + cleaned[1:]

def arrayFromB32(n):
    b32 = '{:032b}'.format(n)
    return [int(i)+1 for i,v in enumerate(reversed(b32)) if v == "1"]

def keysToInt(x):
    if isinstance(x, dict):
            return {int(k):v for k,v in x.items()}
    return x 

def icn (name, ext="png", root = ICON_PATH):
    pathFn = lambda name, ext, root : str(Path(root, name.lower()).with_suffix(".{}".format(ext)).absolute())
    currentPath = pathFn (name, ext, root) 
    if os.path.exists(currentPath) :
        return currentPath
    return pathFn ("Inv_misc_questionmark", ext, root)

def iconBase64Html (filename, size=35, **kwargs):
    isHtml = kwargs.get("html", True)
    
    icon = icn(filename)
    if not os.path.exists(icon):
        icon = icn("inv_misc_questionmark")
    im = Image.open(icon)

    # Crop blizzard framing
    width, height = im.size 
    cr = width*0.065
    left = cr
    top = cr
    right = width-cr
    bottom = width-cr
    im = im.crop((left, top, right, bottom))
    im.thumbnail((size, size), Image.ANTIALIAS)
    im = ImageOps.expand(im, border=kwargs.get("borderSize", 1), fill=kwargs.get("borderColor", (0,0,0)))

    # text = kwargs.get("text", False)
    # if text :
    #     width, height = im.size 
    #     color = text.get("color", (255,255,255))
    #     font = text.get("font", "arial.ttf")
    #     fontSize = text.get("size", 12)
    #     position = text.get("position", (width*0.4,height*0.4))

    #     draw = ImageDraw.Draw(im)
    #     fontObj = ImageFont.truetype(font, fontSize)
    #     draw.text(position,text.get("text", ""),color,font=fontObj)

    buffered = BytesIO()
    im.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    
    return "<img src=\"data:image/png;base64,{}\" />".format(img_str.decode("utf-8") )

# Unit Format - Decorators and Functions
def formatTime (ms, formatType="long", null=None, zero=None, unit=True):
    intervals = {
        "short":(
            ('hrs', 3600000),
            ('min', 60000),
            ('sec', 1000),
            ('ms', 1),
        ),
        "long":(
            ('hours', 3600000),
            ('minutes', 60000),
            ('seconds', 1000),
            ('milliseconds', 1),
        )
    }
    if formatType == None:
        return ms
    if ms == 0 and zero:
        return zero
    if ms :
        result = []
        for name, count in intervals[formatType]:
            value = intFloat(round(ms / count, 3))
            if value and value >= 1:
                ms -= value * count
                if value == 1:
                    name = name.rstrip('s')
                    # value =  s / count
                if not unit:
                    name = ""
                result.append("{} {}".format(value, name))
                break
        if not result :
            return null
        return ' '.join(result)
    return null

def formatDistance (distance, formatType="long", null=None, zero=None, unit=True):
    units={
        "short":"yd",
        "long":"yards"
    }
    distance = intFloat(distance)
    if formatType == None or not distance:
        return distance
    else :
        currentUnit = units[formatType]
        if distance == 1 and formatType=="long":
            currentUnit = currentUnit.strip('s')
        if not unit:
            currentUnit == ""
        return "{distance} {unit}".format(distance=distance, unit=currentUnit)

def formatAngle (angle, formatType="long", null=None, unit=True):
    # toRadians option ? 
    units={
        "short":"°",
        "long":"degrees"
    }
    if formatType == None or not angle:
        return angle
    else :
        currentUnit = units[formatType]
        if angle == 1 and formatType=="long":
            currentUnit = currentUnit.strip('s')
        return "{distance} {unit}".format(distance=angle, unit=currentUnit)

def formatGold (amount, formatType="short", null=None, unit=True):
    intervals = {
        "short":(
            ('g', 10000),
            ('s', 100),
            ('c', 1),
        ),
        "long":(
            ('gold', 10000),
            ('silver', 100),
            ('cooper', 1),
        )
    }

    if amount :
        result = []
        for name, count in intervals[formatType]:
            value = intFloat(round(amount / count, 3))
            if value and value >= 1:
                amount -= value * count
                if value == 1:
                    name = name.rstrip('s')
                if not unit:
                    name = ""
                result.append("{}{}".format(value, name))
                break
        if not result :
            return null
        return ' '.join(result)
    return null

class FormatOutput:
    def __init__(self, fn, *args, **kwargs):
        self.fn = fn
        self.fn_kwargs = kwargs
        self.fn_args = args

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            kwargs_keys = ["null", "formatType", "unit", "zero"]
            self.fn_kwargs= {key:kwargs[key] for key in kwargs_keys if key in kwargs} 
            kwargs = {k:v for k,v in kwargs.items() if k not in kwargs_keys}
            result = func(*args, **kwargs)
            formatted = self.fn(result, *self.fn_args, **self.fn_kwargs)
            return formatted

        return wrapper