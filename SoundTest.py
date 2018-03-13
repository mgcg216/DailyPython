"""Let's try something different this week. Our output is going to be sound instead of text/graphics"""

import winsound

def Solfege():
    #frequencies = [262, 294, 330, 349, 392, 440, 494] # C, D, E, F ,G, A, B,C
    frequencies = [523, 523, 391, 391, 587, 587, 523, 523, 391, 391, 587, 587]
    duration = 500

    for e in frequencies:
        winsound.Beep(e, duration)


Solfege()