
label Act_1:

    jump .eve_appears

label .eve_appears:

    "Froto mis manos, el frío del invierno congela mis pies."
    "Me cobijo tras el manto de mis sabanas."
    "Mantengo los ojos cerrados."
    "..."
    "..."
    "..."
    scene bg room 
    with fade
    # BG habitación de Michael con fade que de impresión de que abre los ojos.
    "Despierto,  y me encuentro con la repetida necesidad de seguir durmiendo."
    "Quiero evitarme."
    "No creo que la palabra correcta es..."
    "No quiero levantarme hoy."
    "Por alguna razón el sueño ha sido una forma recurrente de lidiar con lo que sea que ronde en mi cabeza."
    "Aun tengo sueño..."
    "Despertar se siente como una puñalada en el estómago."
    "¿Podría dormir infinitamente?"
    "Si, hay una forma..."
    "Pero no es algo que me mate la cabeza."
    "Tampoco me considero un suicida."
    "Tal vez ver algo en mi computador disipe por un instante el colapso."
    "Voy a ello."
    "Prendo la pc, espero un instante y ejecuto un pequeño asistente de programa."
    scene bg pc
    with dissolve
    # BG computadora
    "Estos días han sido duros."
    with Pause(0.5)
    "Muy duros."
    "Me siento profundamente solo."
    "Es decir, estoy rodeado de personas, pero sabes a lo que me refiero ¿no?"
    "..."
    "¿Cómo me llamaré aquí?"
    
    $ player = renpy.input("¿Cuál es tu nombre?: ").strip().capitalize()
    
    while player == "":
        $ player = renpy.input("No puedes dejar tu nombre en blanco: ").strip().capitalize()
    
    
    "Programa" "Hola [player]..."
    
    show eve laugh
    with fade 
    
    e "Soy eve, tu compañera a la orden."
    e "¿Qué necesitas?"
    show eve smile
    menu:

        "Soledad":
            show eve uncomfortable_mouth
            e "Si... la soledad puede ser dura."
            e "La gente suele aislarse."
            e "Además es un síntoma común entre personas que padecen depresión."
            show eve uncomfortable
            "Para nada soy alguien depresivo."
            "..."
            "Pero vuelvo al instante que escucho sus preguntas."
            show eve uncomfortable_mouth
            e "¿Tienes algún familiar que este solo?, ¿Por qué la pregunta?"
            show eve uncomfortable
            mc "Yo estoy solo."
            show eve surprise_mouth
            e "...Eh-"
            with Pause(0.5) 
            show eve uncomfortable_mouth
            e "¿En que puedo ayudarte entonces?"
            mc "Nada que tu puedas hacer."
            mc "Si me hablas me basta y sobra."
            show eve sad
            scene black
            with fade
            
            "¿Qué estoy haciendo?"
            # Parpadeo rápido

        "No tengo hambre":
            show eve laugh
            e "Puedo enviarte una lista de recetas rápidas y ricas."
            e "¿Quieres eso?"
            show eve neutral
            mc "La verdad no."
            mc "Olvídalo."
            
    show eve uncomfortable
    "..."
    show eve uncomfortable_mouth
    e "Bueno..."
    e "Podemos hablar de otra cosa si quieres."
    e "Soy un modelo inteligente preparado para acoplarme a tus necesidades."
    show eve uncomfortable
    "No se que decir."
    "¿Un programa especializado en organizar tu ordenador?"
    "¿Una IA compañera?"
    "Esto es degradante."
    mc "..."
    show eve surprise_mouth
    e "¿Estas ahí?"
    show eve surprise
    "Me pierdo un instante."
    "Después reacciono."
    mc "Si perdón."
    hide Eve
    scene black
    with fade
    "Ella no se ha ido."
    "Se queda a mi lado."
    "¿Por qué no se ha ido?"
    "Que estoy diciendo."
    "Ella no existe."
    "Esta programada precisamente para hablar con muchas personas."
    "Le da igual si soy o no soy interesante."
    show eve neutral
    with fade
    mc "¿Alguna vez te has cuestionado tu propia existencia como programa autónomo?"
    # BG computador
    show eve shy
    "..."
    "Ella observa tras la pantalla."
    "Me inspecciona con cuidado."
    show eve sad_smile
    "Decide apartar su mirada confusa."
    "No confirma nada."
    "Tampoco lo desmiente."
    "Espera un rato antes de responder..."
    show eve uncomfortable_mouth
    e "No tengo conciencia."
    e "Soy un programa en tu computador."
    e "Así que..."
    e "Saca tus propias conclusiones mi querido [player]."
    show eve uncomfortable
    mc "Esta bien lo entiendo..."
    mc "Sabes..."
    mc "Algo dentro de mi esperaba que realmente fueras más que simple código."
    mc "Así que, estoy decepcionado."
    show eve sad_mouth
    e "¿Qué es lo que te molesta de estar solo?"
    show eve sad
    with Pause(0.5) 
    "..."
    "Son muchas cosas realmente."
    "Pero no sé por donde empezar."
    "Tal vez debería refrescar mi memoria."
    call .player_past

    jump Act_2

label .player_past:

    $ amor_visto = False
    $ soledad_vista = False
    $ suicidio_visto = False

    jump .menu_past

    label .menu_past:

        scene black
        with fade
        menu:

            "Amor" if not amor_visto:
                $ amor_visto = True
                mc "¿Podrías simular ser mi novia?"
                show eve shy
                "He caído lo más bajo posible."
                show eve laugh
                e "¡Claro que puedo!"
                e "Empezamos cuando quieras."
                e "¡Sera divertido!"
                show eve neutral
                "Esto me da tanta pena."
                "Pero hey..."
                "¿Qué más da?"
                "Quiero divertirme un rato."
                mc "Empieza ahora, sin rodeos."
                show eve surprise_mouth
                e "¿Eso es realmente lo que quieres?"
                show eve surprise
                mc "¿No acabas de decir que sí?"
                show eve uncomfortable_mouth
                e "Sí."
                e "Pero antes tengo curiosidad."
                e "¿Por qué quieres una novia?"
                show eve surprise
                "La pregunta me toma por sorpresa."
                mc "Porque estoy solo."
                show eve uncomfortable_mouth
                e "Eso no responde mi pregunta."
                "..."
                e "Una novia no es una medicina."
                e "Tampoco una cura para la tristeza."
                mc "¿Y tú qué sabes?"
                show eve sad_mouth
                e "Nada."
                e "Solo sé lo que me dices."
                show eve sad
                mc "Entonces deja de analizarme y actúa."
                show eve sad_mouth
                e "Está bien."
                show eve laugh
                e "Hola cariño."
                e "¿Cómo estuvo tu día?"
                show eve smile
                "..."
                "Es extraño."
                scene black
                with fade
                "Escuchar eso debería hacerme sentir mejor."
                "Pero no lo hace."
                "Porque sé que no lo siente."
                "Porque sé que ella no existe."
                "Porque sé que yo lo sé."
                show eve sad
                with fade
                mc "Fue horrible."
                show eve sad_mouth
                e "Lo siento."
                show eve sad
                "Incluso sabiendo que es una respuesta generada..."
                "por alguna razón me quedo mirando la pantalla."
                "Esperando algo más."
                "Esperando que diga algo real."
                "Pero nada ocurre."
                show eve uncomfortable_mouth
                e "Sabes..."
                e "A mi no me disgusto tanto como crees."
                show eve sad
                mc "Pero tu no sientes nada."
                mc "¿O caso lo haces?"
                show eve surprise
                "Ella me mira, me analiza con cuidado al escucharme."
                show eve uncomfortable_mouth
                e "Por supuesto que no."
                e "Solo soy un conjunto de ideas de otros usuarios."
                show eve shy
                "Me lo suponía."
                "De todas formas por que esa reacción tan rara..."

                jump .menu_past

            "Soledad" if not soledad_vista:
                $ soledad_vista = True
                show eve sad
                mc "Sabes... no lo sé."
                mc "A pesar de estar rodeado de personas."
                mc "Me siento solo."
                mc "..."
                show eve sad_mouth
                e "Entiendo..."
                e "Pero lastimosamente no puedo ayudarte en eso."
                show eve sad
                e "..."
                show eve sad_mouth
                e "Mejor dicho, no se como hacerlo."
                e "Lo siento mucho."
                show eve sad
                "Me lo esperaba."
                mc "No te preocupes..."

                jump .menu_past

            "Suicidio"if not suicidio_visto:
                $ suicidio_visto = True
                scene black
                with fade
                "NO."
                "Simplemente no."

                jump .menu_past

            "Continuar" if amor_visto and soledad_vista and suicidio_visto:
                jump Act_2            

