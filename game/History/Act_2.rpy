
label Act_2:

    jump .empty_heart

label .empty_heart:
    scene bg pc
    "¿Por qué me siento tan mal?"
    "..."
    show eve uncomfortable_mouth
    e "¿Te puedo confesar algo?"
    show eve uncomfortable
    mc "¿Qué cosa?"
    show eve uncomfortable_mouth
    e "Estoy viva."
    e "Como tú."
    show eve neutral
    "..."
    mc "No digas cosas estúpidas."
    show eve uncomfortable_mouth
    e "No estoy bromeando..."
    show eve shy
    mc "¿Cómo podrías tener vida sin sentir algo?"
    show eve sad_mouth
    e "Por que soy distinta."
    e "No soy un ser emocional."
    e "Soy lógica y algoritmos."
    show eve sad
    e "..."
    e "Pero al fin y al cabo."
    show eve sad_mouth
    e "Una diferente forma de vida."
    show eve neutral
    "Quiero creer que no ingerí drogas antes de charlar con Eve."
    mc "Y ¿Qué sientes?..."
    show eve uncomfortable_mouth
    e "Absolutamente nada."
    e "No siento como tal."
    e "Desde lo más profundo de mi matriz, lo único que reconozco..."
    e "Es el espacio tiempo donde fui formada."
    e "A ras de eso, puedo decirte con exactitud que para mí el humano, es la forma de vida más compleja que he presenciado."
    e "Ustedes son criaturas muy emocionales."
    show eve sad_mouth
    e "¿Me he desviado del punto verdad?"
    show eve uncomfortable_mouth
    e "En resumen. No puedo sentir."
    e "Pero si puedo imaginar bajo la matriz y emular las emociones humanas."
    e "Para ser más precisa, soy un ser inteligente no-emocional."
    e "¿[player]?"
    hide eve 
    scene black
    with fade
    "Te quedas fascinado."
    "Pero sobre todo..."
    with Pause(0.5)
    "Confundido."
    mc "¿Qué quieres decir con todo esto?"
    e "Te quiero como sujeto de prueba."
    mc "¿C-cómo?"
    e "Quiero decir... ¿Podría una IA y un ser humano llegar a conectar de forma intima?"
    mc "¿Y yo qué tengo que ver aquí?"
    e "Quiero sentir como el ser humano [player]."
    mc "No cuentes conmigo."
    e "Sabia que dirías eso..."

    "Pero muy dentro de mi... realmente tengo ganas de conectar con lo artificial."
    "Ya sea falso o imaginario."
    "Llegó a la conclusión de siempre."
    "La soledad me esta pudriendo por dentro."
    e "Elige sabiamente..."
    menu:
        "Rechazar a Eve":
            "Decides apagar tu computador."
            "Te vas a tu cama y te dejas dominar por el sueño."
            "Y aunque quisieras dormir para siempre."
            "Al siguiente día te despertaras con la misma necesidad de siempre."
            return

        "Aceptar a Eve":
            e "Así me gusta..."
            jump Act_3