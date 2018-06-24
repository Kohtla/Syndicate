from PIL import Image, ImageDraw, ImageFont
import math as m

from io import BytesIO

from django.core.files.base import ContentFile


def r(first, second):
    return  m.sqrt(pow(first[0] -second[0],2)+pow(first[1] -second[1],2))

def draw(chest, height, neck, sleeve, shoulder):
    n = 20
    lineWidth = 3
    smallLineWidth = 4
    image = Image.new("RGBA", ((2 * chest) * n, (2 * height) * n), (30, 30, 30, 30))
    half = chest / 2
    halfneck = neck /2
    draw = ImageDraw.Draw(image)

    fnt = ImageFont.truetype('E:/Images/IndieFlower.ttf', 40)
    fntsmall = ImageFont.truetype('E:/Images/IndieFlower.ttf', 40)

    oX = 100
    oY = 20
    A = (oX * n, oY * n)
    B = ((oX + half) * n, oY * n)
    H = (oX * n, (oY + height) * n)
    H1 = ((oX + half) * n, (oY + height) * n)
    H2 = ((oX+(half / 3 )+(half / 6 )) * n, (oY + height) * n)

    G0 = ((oX) * n, (oY + (half / 3 )) * n)
    G1 = ((oX+half) * n, (oY + (half / 3 )) * n)
    G2 = ((oX+(half / 3 )) * n, (oY + (half / 3 )) * n)
    G3 = ((oX+(half / 3 )+(half / 3 )) * n, (oY + (half / 3 )) * n)
    G4 = ((oX+(half / 3 )+(half / 6 )) * n, (oY + (half / 3 )) * n)

    P = ((oX+(half / 3  )) * n, (oY) * n)
    B1 = ((oX+(half / 3 )+(half / 3 )) * n, (oY) * n)

    A1 = ((oX +halfneck/3)*n,(oY)*n)
    A0 = ((oX * n, (oY-halfneck/6)*n))
    A2 = ((oX +halfneck/3)*n,(oY-halfneck/6)*n)
    P1 = ((oX+(half / 3  )) * n, (oY+halfneck/12) * n)
    P4 = ((oX+(half / 3 )+(half / 3 )) * n, (oY+halfneck/6) * n)
    B2 = ((oX+half - halfneck/3)*n,(oY)*n)
    B3 = ((oX+half)*n,(oY+halfneck/3)*n)

    p1p2 = r(P1,P) * 0.7


    p1x = ((r(A1, A2) + r(P1, P)) * p1p2) / r(A2, P1)
    xp2 = ((r(A,P)-r(A,A1))*p1p2)/r(A2,P1)

    P2 = ((oX+(half / 3  )) * n+xp2, (oY+halfneck/12) * n+p1x)
    P5 = ((oX+(half / 3 )+(half / 3 )) * n - xp2, (oY+halfneck/6) * n+p1x)



    draw.line([A, B], fill="black", width=lineWidth)
    draw.line([A, H], fill="black", width=lineWidth)
    draw.line([H, H1], fill="black", width=lineWidth)
    draw.line([B, H1], fill="black", width=lineWidth)
    draw.line([G0, G1], fill="black", width=lineWidth)
    draw.line([G2, P], fill="black", width=lineWidth)
    draw.line([G3, B1], fill="black", width=lineWidth)
    draw.line([G4, H2], fill="black", width=lineWidth)
    draw.line([A1, A2], fill="black", width=lineWidth)
    draw.line([A2, P2], fill="black", width=smallLineWidth)
    draw.line([B2, P5], fill="black", width=smallLineWidth)


    tempB2 = ((oX+half - halfneck/3)*n,(oY-halfneck/3)*n)
    tempB3 = ((oX+half+halfneck/3)*n,(oY+halfneck/3)*n)
    tempA0 = (((oX-halfneck/3) * n, (oY-halfneck/3)*n))

    temp1l = ((oX+(half / 3  )) * n, (oY+halfneck/12) * n+p1x)
    temp1r = ((oX+(half / 3 )) * n + 2*xp2, (oY + (half / 3 )) * n)

    temp3l = ((oX+(half / 3 )) * n, (oY+halfneck/6) * n+p1x)
    temp4l = ((oX+(half / 3 )+(half / 3 )) * n - 2*xp2, (oY+halfneck/6) * n+p1x)



    draw.arc([temp1l,temp1r],180,270,'black')
    draw.arc([temp1l, G3], 90, 180, 'black')
    draw.arc([tempA0,A1], 0, 90, 'black')
    draw.arc([temp4l, G3], 270, 0, 'black')
    draw.arc([temp3l, G3], 0, 90, 'black')
    draw.arc([tempB2,tempB3], 90, 180, 'black')



    draw.text(A, "A", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(B, "B", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(H, "H", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(H1, "H1", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(G0, "G0", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(G1, "G1", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(G2, "G2", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(G3, "G3", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(G4, "G4", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    #draw.text(P, "P", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    #draw.text(B1, "B1", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(H2, "H2", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)

    draw.text(A1, "A1", fill="black", font=fntsmall, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(A2, "A2", fill="black", font=fntsmall, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(B2, "B2", fill="black", font=fntsmall, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(B3, "B3", fill="black", font=fntsmall, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(P1, "P1", fill="black", font=fntsmall, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(P4, "P4", fill="black", font=fntsmall, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(P2, "P2", fill="black", font=fntsmall, anchor=None, spacing=0, align="left", direction=None,
              features=None)
    draw.text(P5, "P5", fill="black", font=fntsmall, anchor=None, spacing=0, align="left", direction=None,
              features=None)


    per = r(P,B1) + r(B1,G3) +r(G3,G2) +r(G2,P)
    x = m.pi*2/8*per*0.34/n
    os = sleeve
    sh = shoulder
    print(x)
    oXs = 10
    oYs = 20


    O1 = (oXs * n, oYs * n)
    O2 = ((oXs +sh) * n, oYs * n)
    S1 = (oXs * n, (oYs +os) * n)
    S2 = ((oXs+sh) * n, (oYs+os) * n)

    O = ((oXs+ sh/2) * n, (oYs) * n)
    V = ((oXs+ sh/2) * n, (oYs+x) * n)
    V1 = ((oXs) * n, (oYs+x) * n)
    V2 = ((oXs+ sh) * n, (oYs+x) * n)
    S = ((oXs+ sh/2) * n, (oYs+os) * n)

    C1 = ((oXs+ sh/4) * n, (oYs) * n)
    C2 = ((oXs+ sh/4 + sh/2) * n, (oYs) * n)
    C3 = ((oXs+ sh/4) * n, (oYs+x/2) * n)
    C4 = ((oXs+ sh/4 + sh/2) * n, (oYs+x/2) * n)
    C5 = ((oXs+ sh/4) * n, (oYs+x) * n)
    C6 = ((oXs+ sh/4 + sh/2) * n, (oYs+x) * n)
    C7 = ((oXs+ sh/4) * n, (oYs+os) * n)
    C8 = ((oXs+ sh/4 + sh/2) * n, (oYs+os) * n)

    tempO1 = ((oXs - sh/4) * n, oYs * n)
    tempV2 = ((oXs+sh+sh/4) * n, (oYs+x) * n)

    draw.arc([C1, C6], 180, 0, 'black')

    draw.arc([tempO1, C5], 0, 90, 'black')
    draw.arc([C2, tempV2], 90, 180, 'black')



    draw.line([O1, O2], fill="black", width=lineWidth)
    draw.line([S1, S2], fill="black", width=lineWidth)
    draw.line([O1, S1], fill="black", width=lineWidth)
    draw.line([O2, S2], fill="black", width=lineWidth)
    draw.line([O, S], fill="black", width=lineWidth)
    draw.line([V1, V2], fill="black", width=lineWidth)
    draw.line([C1, C7], fill="black", width=lineWidth)
    draw.line([C2, C8], fill="black", width=lineWidth)
    draw.line([C3, C4], fill="black", width=lineWidth)

    draw.text(O1, "O1", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(S1, "S", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(S2, "S2", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(O2, "O2", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(O, "O", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(S, "S", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(V, "V", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(V1, "V1", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(V2, "V2", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(C1, "C1", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(C2, "C2", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(C3, "C3", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(C4, "C4", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(C5, "C5", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(C6, "C6", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(C7, "C7", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)
    draw.text(C8, "C8", fill="black", font=fnt, anchor=None, spacing=0, align="left", direction=None, features=None)

    del draw
    buffer = BytesIO()
    image.save(fp=buffer, format='PNG')
    return ContentFile(buffer.getvalue())



draw(100, 60, 30,30, 40)
