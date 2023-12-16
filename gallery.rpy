init python:
    g = Gallery()

    g.button("red") 
    g.unlock_image("CG_red") 

    g.button("blue") 
    g.image("CG_blue")
    g.condition("persistent.blue_unlocked") 

    g.button("green_and_orange")
    g.unlock_image("CG_green")
    g.unlock_image("CG_orange") 

    g.button("green_and_orange2") 
    g.condition("persistent.green_unlocked and persistent.orange_unlocked") 
    g.image("CG_green")
    g.image("CG_orange") 
    g.image("CG_pink") 
    g.condition("persistent.pink_unlocked") 

screen gallery():
    add "gui/mm/MainMenu.avif"
    tag menu

    fixed:
        draggroup:
            drag:
                drag_raise True
                draggable True
                drag_name "memourys"
                xpos 500
                ypos 50

                imagemap:
                    ground "images/bg/resize.jpg"
                    text "memourys" xpos 0.4
        
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 15
                        grid 2 2:
                            add g.make_button(name="red",unlocked="CG/red_small.jpg",locked="images/cg/locked.jpg") 
                            add g.make_button(name="blue",unlocked="CG/blue_small.jpg",locked="images/cg/locked.jpg") 
                            add g.make_button(name="green_and_orange",unlocked="CG/green_small.jpg",locked="images/cg/locked.jpg") 
                            add g.make_button(name="green_and_orange2",unlocked="CG/red_small.jpg",locked="images/cg/locked.jpg") 
                            spacing 15
                    at transform:
                        alpha 0
                        pause 0.5
                        linear 0.7 alpha 1.0

                    textbutton "cg time" action Show("gallery_sprite")

            drag:
                drag_raise True
                draggable True
                drag_name "cg"
                xpos 920
                ypos 4

                imagemap:
                    ground "images/bg/resize.jpg"
                    text "cg" xpos 0.4
        
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 15
                        grid 2 2:
                            add g.make_button(name="red",unlocked="CG/red_small.jpg",locked="images/cg/locked.jpg") 
                            add g.make_button(name="blue",unlocked="CG/blue_small.jpg",locked="images/cg/locked.jpg") 
                            add g.make_button(name="green_and_orange",unlocked="CG/green_small.jpg",locked="images/cg/locked.jpg") 
                            add g.make_button(name="green_and_orange2",unlocked="CG/red_small.jpg",locked="images/cg/locked.jpg") 
                            spacing 15   
                    at transform:
                        alpha 0
                        pause 0.5
                        linear 0.4 alpha 1.0

            drag:
                drag_raise True
                draggable True
                drag_name "animations"
                xpos 200
                ypos 150

                imagemap:
                    ground "images/bg/resize.jpg"
                    text "Anim" xpos 0.4
        
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 15
                        grid 2 2:
                            add g.make_button(name="red",unlocked="CG/red_small.jpg",locked="images/cg/locked.jpg") 
                            add g.make_button(name="blue",unlocked="CG/blue_small.jpg",locked="images/cg/locked.jpg") 
                            add g.make_button(name="green_and_orange",unlocked="CG/green_small.jpg",locked="images/cg/locked.jpg") 
                            add g.make_button(name="green_and_orange2",unlocked="CG/red_small.jpg",locked="images/cg/locked.jpg") 
                            spacing 15                
                    at transform:
                        alpha 0
                        pause 0.2
                        linear 1 alpha 1.0

    use taskbar
    textbutton "Return" action Return() xpos 0.05 ypos 0.9

#First attempt
screen gallery_sprite():
    tag menu
    zorder 1
    modal True
    add "gui/mm/MainMenu.avif"

    hbox:
        xpos 50
        ypos 600
        textbutton "main gallery" action Show("gallery")

    fixed:
        drag:
            draggable True
            xpos 500
            ypos 50

            imagemap:
                ground "images/bg/resize.jpg"
                #use gallerynav
    
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 15
                    grid 2 2:
                        add g.make_button(name="red",unlocked="CG/red_small.jpg",locked="images/cg/locked.jpg") 
                        add g.make_button(name="blue",unlocked="CG/blue_small.jpg",locked="images/cg/locked.jpg") 
                        add g.make_button(name="green_and_orange",unlocked="CG/green_small.jpg",locked="images/cg/locked.jpg") 
                        add g.make_button(name="green_and_orange2",unlocked="CG/red_small.jpg",locked="images/cg/locked.jpg") 
                        spacing 15  

screen gallery_secret():
    tag menu
    zorder 1
    modal True
    add "gui/mm/MainMenu.avif"

    fixed:
        drag:
            draggable True
            xpos 500
            ypos 50

            imagemap:
                ground "images/bg/resize.jpg"
    
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 15
                    grid 2 2:
                        add g.make_button(name="red",unlocked="CG/red_small.jpg",locked="images/cg/locked.jpg") 
                        add g.make_button(name="blue",unlocked="CG/blue_small.jpg",locked="images/cg/locked.jpg") 
                        add g.make_button(name="green_and_orange",unlocked="CG/green_small.jpg",locked="images/cg/locked.jpg") 
                        add g.make_button(name="green_and_orange2",unlocked="CG/red_small.jpg",locked="images/cg/locked.jpg") 
                        spacing 15  
    textbutton "Return" action Return() xpos 0.05 ypos 0.9