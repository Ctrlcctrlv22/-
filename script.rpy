define e = Character('Shkolnik', color="#c8f9ff", image 'Shkolnik')
define d = Character('Borya', color="#ffdd00", image 'Borya')

label start:

    scene bg dvor

    show Shkolnik at left
    
    e "Ля ля ля Ля ля ля"
    play sound "lalala.mp3"

        menu :
        
        "Посмотреть цыплят":
            jump ciplyata 
        "Посмотреть будку бори":
            jump budka

label ciplyata:
    


    e "а тут у нас "
    stop sound 
    return
