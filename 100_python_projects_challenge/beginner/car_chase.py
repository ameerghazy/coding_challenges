print('''
                                              _____________
                                  ..---:::::::-----------. ::::;;.
                               .'""""""                  ;;   \  ":.
                            .''                          ;     \   "\__.
                          .'                            ;;      ;   \\";
                        .'                              ;   _____;   \\/
                      .'                               :; ;"     \ ___:'.
                    .'--...........................    : =   ____:"    \ \
               ..-""                               """'  o"""     ;     ; :
          .--""  .----- ..----...    _.-    --.  ..-"     ;       ;     ; ;
       .""_-     "--""-----'""    _-"        .-""         ;        ;    .-.
    .'  .'                      ."         ."              ;       ;   /. |
   /-./'                      ."          /           _..  ;       ;   ;;;|
  :  ;-.______               /       _________==.    /_  \ ;       ;   ;;;;
  ;  / |      """"""""""".---."""""""          :    /" ". |;       ; _; ;;;
 /"-/  |                /   /                  /   /     ;|;      ;-" | ;';
:-  :   """----______  /   /              ____.   .  ."'. ;;   .-"..T"   .
'. "  ___            "":   '""""""""""""""    .   ; ;    ;; ;." ."   '--"
 ",   __ """  ""---... :- - - - - - - - - ' '  ; ;  ;    ;;"  ."
  /. ;  """---___                             ;  ; ;     ;|.""
 :  ":           """----.    .-------.       ;   ; ;     ;:
  \  '--__               \   \        \     /    | ;     ;;
   '-..   """"---___      :   .______..\ __/..-""|  ;   ; ;
       ""--..       """--"        m l s         .   ". . ;
             ""------...                  ..--""      " :
                        """"""""""""""""""    \        /
                                               "------"

''')
print("Welcome to the car chase!")
print("You're being chased by a criminal. You get into a random car to try to get away.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

step_1 = input("Do you want to go forward or reverse? (pick 'Forward' or 'Reverse'): ").lower()
if step_1 == 'forward':
  print("GAME OVER - You crash into a tree and spin out of control and go off a cliff and die!!")
elif step_1 == 'reverse':
  print("You reverse all the way to the end of the street.")
  step_2 = input("Do you want to get out of the car and run or drive forward? (pick 'Run' or 'Forward'): ").lower()
  if step_2 == 'run':
    print("You are caught by the criminal and are shot multiple times!!!! - GAME OVER")
  elif step_2 == 'forward':
    print("You hit the criminal..")
    step_3 = input("Do you want to drive forward, reverse or call your mom? (pick 'Mom','Forward' or 'Reverse'): ").lower()
    if step_3 == 'forward':
      print ("The police spots you driving away, think you murdered an innocent man, and they take you to JAIL! - GAME OVER")
    elif step_3 == 'reverse':
      print ("You hit the criminal again, he turns into a zombie and kills you!!! - GAME OVER")
    elif step_3 == 'mom':
      print ("Mom tells you to calm down, call the police and tell them what happened - YOU WIN!!")
