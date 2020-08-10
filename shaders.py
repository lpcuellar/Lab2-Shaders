from gl import *


def gourad(render, **kwargs):
    u, v, w = kwargs['barycentric_coords']
    ta, tb, tc = kwargs['texture_coords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.current_texture :
        tx = ta[0] * u + tb[0] * v + tc[0] * w
        ty = ta[1] * u + tb[1] * v + tc[1] * w

        texture_color = render.current_texture.getColor(tx, ty)

        b *= texture_color[0] / 255
        g *= texture_color[1] / 255
        r *= texture_color[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = [nx, ny, nz]

    intensity = dot(normal, render.light)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0 :
        return r, g, b

    else :
        return 0, 0, 0

def toon(render, **kwargs):
    u, v, w = kwargs['barycentric_coords']
    ta, tb, tc = kwargs['texture_coords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.current_texture :
        tx = ta[0] * u + tb[0] * v + tc[0] * w
        ty = ta[1] * u + tb[1] * v + tc[1] * w

        texture_color = render.current_texture.getColor(tx, ty)

        b *= texture_color[0] / 255
        g *= texture_color[1] / 255
        r *= texture_color[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = [nx, ny, nz]

    intensity = dot(normal, render.light)

    if (intensity > 0) and (intensity < 0.10) :
        intensity = 0.10

    elif (intensity > 0.10) and (intensity < 0.20) :
        intensity = 0.20

    elif  (intensity > 0.20) and (intensity < 0.30) :
        intensity = 0.30

    elif  (intensity > 0.30) and (intensity < 0.40) :
        intensity = 0.40

    elif  (intensity > 0.40) and (intensity < 0.50) :
        intensity = 0.50

    elif  (intensity > 0.50) and (intensity < 0.60) :
        intensity = 0.60

    elif  (intensity > 0.60) and (intensity < 0.70) :
        intensity = 0.70

    elif  (intensity > 0.70) and (intensity < 0.80) :
        intensity = 0.80

    elif  (intensity > 0.80) and (intensity < 0.90) :
        intensity = 0.90

    elif  (intensity > 0.90) and (intensity <= 1) :
        intensity = 1

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0 :
        return r, g, b

    else :
        return 0, 0, 0
