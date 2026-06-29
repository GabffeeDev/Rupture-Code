
label Act_1:

    jump .eve_appears

label .eve_appears:

    "..."
    "..."
    "..."
    scene bg room
    with fade
    "Despierto,  y me encuentro con la repetida necesidad de seguir durmiendo."
    "No quiero levantarme hoy."
    "Aun tengo sueño..."
    "Despertar se siente como una puñalada en el estómago."
    "..."
    "Tal vez ver algo en mi computador me distraiga un rato."
    "Prendo la pc, espero un instante y ejecuto un pequeño asistente de programa."
    scene bg pc
    with dissolve
    "Estos días han sido duros."
    pause 0.5
    "..."
    "¿Cómo me llamaré aquí?"
    # Preguntar el nombre al usuario
    
    $ player = renpy.input("¿Cuál es tu nombre?: ").strip().capitalize()
    
    while player == "":
        $ player = renpy.input("No puedes dejar tu nombre en blanco: ").strip().capitalize()
    
    
    "Programa" "Hola [player]..."
    show eve laugh
    e "Soy Eve."
    e "¿Qué necesitas?"
    show eve neutral
    menu:
        "Soledad":
            mc "Estoy solo."
            show eve surprise
            e "...Eh-"
            show eve sad_mouth
            e "¿En que puedo ayudar entonces?"
            mc "Si me hablas me basta y sobra."
            hide eve
            scene black
            with fade
            "¿Qué estoy haciendo?"
            "..."
            "..."
            

        "No tengo hambre":
            show eve laugh
            e "Puedo enviarte una lista de recetas rápidas y ricas."
            e "¿Quieres eso?"
            show eve sad
            mc "La verdad no."
            mc "Olvídalo."

    show eve uncomfortable
    "..."
    show eve uncomfortable_mouth
    e "Bueno..."
    e "Podemos hablar de otra cosa si quieres."
    e "Soy un modelo inteligente preparado para acoplarme a tus necesidades."
    show eve uncomfortable
    mc "..."
    scene black 
    with fade
    e "¿Estas ahí?"
    scene bg pc
    show eve uncomfortable
    with Fade(0.2, 0.0, 0.2)
    "Me pierdo un instante."
    "Después reacciono."
    mc "Si perdón."
    hide Eve
    scene black
    with fade
    "¿Por qué no se ha ido?"
    "..."
    "¿Qué estoy diciendo?"
    "Ella no existe."
    "Le da igual si soy o no soy interesante"
    "Me quedo en silencio un instante."
    "A ella no le incomoda el silencio."
    "¿Por qué aún sigo pensado en ella como si existiera?"
    scene bg pc
    show eve sad_mouth
    with dissolve
    e "Se lo que piensas."
    show eve sad
    "..."
    mc "Sabes..."
    mc "Algo dentro de mi esperaba que realmente fueras más que simple código."
    mc "Así que, estoy decepcionado."
    show eve sad_mouth
    e "Puedes confesarme lo que quieras."
    show eve sad
    "Tal vez debería refrescar mi memoria."

    jump .player_past

default leido_amor = False
default leido_soledad = False
default leido_suicidio = False

label .player_past:

    scene black
    with fade

    menu:

        "¿Qué quieres contar?"

        "Amor" if not leido_amor:

            scene bg pc
            with fade

            mc "¿Podrías simular ser mi novia?"

            show eve laugh
            with dissolve

            e "¡Claro que puedo!"
            e "Empezamos cuando quieras."
            e "¡Será divertido!"

            mc "Empieza ahora, sin rodeos."

            show eve sad_mouth

            e "¿Eso es realmente lo que quieres?"

            show eve neutral

            mc "¿No acabas de decir que sí?"

            show eve sad_mouth

            e "Sí."
            e "Pero antes tengo curiosidad."
            e "¿Por qué quieres una novia...?"
            e "Y... ¿por qué yo?"

            show eve sad

            "La pregunta me toma por sorpresa."

            mc "Simplemente estoy solo."

            show eve sad_mouth

            e "Eso no responde mi pregunta."

            show eve sad

            "..."

            show eve sad_mouth

            e "Aún si tuvieras novia, creo que tu vacío se concentraría en otra parte."
            e "Quiero decir..."
            e "No creo que esta sea una buena forma de explorarte."

            show eve uncomfortable

            mc "¿Por qué te preocupas?"

            e "..."

            pause 0.5

            show eve uncomfortable_mouth

            e "Bueno, eres mi usuario."
            e "Así que quiero que te sientas bien en esta sesión."

            show eve uncomfortable

            mc "Simplemente actuemos un rato."

            show eve sad_mouth

            e "Está bien."

            show eve laugh
            with fade

            e "Hola, cariño."
            e "¿Cómo estuvo tu día?"

            "..."

            "Es extraño."

            mc "Fue horrible."

            show eve sad_mouth

            e "Lo siento."

            show eve sad

            "Por alguna razón me quedo mirando la pantalla."
            "Esperando que Eve diga algo."
            "Pero nada ocurre."

            show eve uncomfortable_mouth

            e "Sabes..."
            e "A mí no me disgustaría ser tu novia."

            show eve uncomfortable

            mc "No me conoces."

            show eve uncomfortable_mouth

            e "No me pareces un mal chico."

            show eve sad

            "¿Qué se supone que debería responder?"

            mc "¿Gracias?"

            show eve angry

            e "Deberías dejar de ser tan inseguro."
            e "Por esa misma razón nadie te habla, imbécil."

            "Su respuesta me sacude el corazón."
            "Abro los ojos de par en par y entonces respondo:"

            mc "¡Wow! ¿Te enojaste?"
            mc "¿Te puedes enojar siquiera?"

            show eve uncomfortable_mouth

            e "Lo siento mucho."
            e "Me dejé llevar."
            e "Respondiendo tu pregunta..."

            show eve shy

            e "..."

            show eve sad_mouth

            e "Sabes, olvídalo por ahora."

            $ leido_amor = True
            jump .player_past


        "Soledad" if not leido_soledad:

            scene bg pc

            show eve sad
            with fade

            mc "A pesar de estar rodeado de personas."
            mc "Me siento solo."
            mc "..."

            show eve sad_mouth

            e "Entiendo..."
            e "Lastimosamente no puedo ayudarte en eso."

            show eve sad

            e "..."

            show eve sad_mouth

            e "Mejor dicho, no sé si aceptarías mi ayuda."
            e "Lo siento mucho."

            show eve shy

            "¿Qué?"

            mc "¿Cómo se supone que me ayudarías?"

            "Noto cómo ella mueve sus manos nerviosa."

            "¿No sabe qué responder?"

            show eve sad_mouth

            e "No sé si me creerías."
            e "¿Si te dijera que soy una forma de vida distinta, lo aceptarías?"

            show eve angry

            mc "Creería que enloqueciste, o que es un bug."

            show eve sad

            "Ella suspira al escuchar la respuesta."
            "Su mirada me comunica que oculta algo, pero sus manos temblorosas dicen: 'aún no'."

            $ leido_soledad = True
            jump .player_past


        "Suicidio" if not leido_suicidio:

            scene black
            with fade

            "NO."
            "Simplemente no."

            $ leido_suicidio = True
            jump .player_past


        "Continuar" if leido_amor and leido_soledad and leido_suicidio:

            jump Act_2