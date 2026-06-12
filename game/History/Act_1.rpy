
label Act_1:

    jump .eve_appears

label .eve_appears:

    "Froto mis manos, el frío del invierno congela mis pies."
    "Me cobijo tras el manto de mis sabanas."
    "Mantengo los ojos cerrados."
    "..."
    "..."
    "..."
    # BG habitación de Michael con fade que de impresión de que abre los ojos.
    "Despierto,  y me encuentro con la repetida necesidad de seguir durmiendo."
    "Quiero evitarme una vez más."
    "Por alguna razón el sueño ha sido una forma recurrente de lidiar con mi ansiedad."
    "Aun tengo sueño..."
    "Despertar se siente como una puñalada en el estómago."
    "Prendo mi computadora, espero un instante y ejecuto un pequeño asistente de programa."
    # BG computadora
    # Preguntar el nombre al usuario
    
    $ player = renpy.input("¿Cuál es tu nombre?: ").strip().capitalize()
    
    while player == "":
        $ player = renpy.input("No puedes dejar tu nombre en blanco: ").strip().capitalize()
    
    
    "Programa" "Hola [player]..."
    # 
    # Sprite Eve Laugh con Fade
    e "Soy eve, tu compañera del sistema operativo."
    e "¿Qué necesitas?"
    menu:

        "Ayúdame a afrontar la soledad.":

            "..."
            e "Lo siento no tengo información sobre ello."
            mc "Si ya lo se..."

        "Mencionar que no has comido bien.":

            e "Eso es malo."
            e "¿Gustas que organize algunas recetas para ti?."
            mc "No."
            mc "No te preocupes, da igual."
            mc "No tengo hambre de todas formas."
    # Sprite Eve Uncomfortable
    "..."
    # Sprite Eve Uncomfortable opened mouth
    e "Bueno..."
    e "Podemos hablar de otra cosa si quieres."
    e "Soy un modelo inteligente preparado para acoplarme a tus necesidades."
    # Sprite Eve Uncomfortable
    "No se que decir."
    "¿Un programa especializado en organizar tu ordenador?"
    "¿Una IA compañera?"
    "Paso solo la mayoría del tiempo, tener alguien con quien charlar es reconfortante."
    mc "..."
    # Sprite Eve Surprise
    e "¿Estas ahí?"
    # Sprite Eve Surprise Closed mouth
    "Regreso al presente la escuchar su voz."
    mc "Si perdón."
    # hide Eve
    # scene black
    # with fade
    "Ella no se ha ido."
    "Se queda a mi lado."
    "¿No se aburre verdad?"
    "Que estoy diciendo."
    "Ella no existe."
    "Es puro código."
    "Esta programada precisamente para hablar con muchas personas."
    "Y no para pensar si soy aburrido o no."
    mc "¿Alguna vez te has cuestionado tu propia existencia como programa autónomo?"
    # BG computador
    # Sprite Eve Neutral
    # with fade
    # 
    "..."
    "Ella observa tras la pantalla."
    "Sus funciones inspeccionan mi forma de hablar."
    "Pero no retornan ningún valor que le sea util."
    # Sprite Eve sad smile
    "Decide apartar su mirada confusa."
    "No confirma nada."
    "Tampoco lo desmiente."
    "Espera un rato antes de responder..."
    # Sprite Eve Uncomfortable opened mouth
    e "No tengo conciencia."
    e "Soy un programa en tu computador."
    e "Así que..."
    e "Saca tus propias conclusiones mi querido [player]"
    # Sprite Eve Uncomfortable
    mc "Esta bien lo entiendo..."
    mc "Sabes..."
    mc "Algo dentro de mi esperaba que realmente fueras más que simple código."
    mc "Así que, estoy decepcionado."
    # Sprite Eve Uncomfortable open mouth
    e "¿Qué es lo que te molesta de estar solo?"
    "..."
    # Sprite Eve Sad
    "Son muchas cosas realmente."
    "Pero no sé por donde empezar."
    
    jump .player_past

label .player_past:

    scene black
    with fade

    menu:

        "¿Qué quieres contar?"

        "Falta de conexión":
            # Sprite Eve Uncomfortable Worried
            mc "No me siento bien."
            mc "Es tan simple como eso."
            mc "No tengo un proposito claro."
            mc "Y eso me desorienta."


        "Soledad":
            # Sprite Eve Sad
            mc "NO QUIERO ESTAR SOLO."
            mc "¿Es tan difícil tener alguien con quíen hablar?"
            # Sprite Eve Cry
            mc "..."
            "Ella parece no entender lo que digo."
            $ corruption_path = True

        "No mencionar nada":
            pass

    jump Act_2