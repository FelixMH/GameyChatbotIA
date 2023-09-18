from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Agente inteligente")
trainer = ListTrainer(chatbot=chatbot)

# Entrenar al chatbot.
# oswi1 = [
#     "¿Quién da clase de iOS?",
#     "¿Que pues?, el Oswaldo"
# ]

# oswi2 = [
#     "¿El inge que da la clase de desarrollo en iOS?",
#     "El Oswi"
# ]
trainer.train(
    conversation=[
        "Hola",
        "¡Hola:D! ¿En qué puedo ayudarte el día de hoy?",
    ]
)

trainer.train(
    conversation=[
        "Que tal",
        "¡Hola:D! ¿En qué puedo ayudarte el día de hoy?",
    ]
)

trainer.train(
    conversation=[
        "¿Quién da iOS a las 10am?",
        "El Oswi",
    ]
)

trainer.train(
    conversation=[
        "¿Cómo le dice Chespi al Oswi?",
        "Brillitos",
    ]
)

# entrenando al chatbot con preguntas sobre videojuegos

trainer.train(
    conversation=[
        "¿Cuál es tu juego de rol favorito?",
        "Me encanta Skyrim, ¿y tú?",
    ]
)

trainer.train(
    conversation=[
        "Háblame acerca de los videojuegos",
        "Los videojuegos son una forma popular de entretenimiento interactivo. Se juegan en diversas plataformas, como consolas, PC y dispositivos móviles. Los videojuegos pueden abarcar una amplia variedad de géneros, desde juegos de acción y aventuras hasta juegos de estrategia y simulación. A lo largo de los años, los videojuegos han evolucionado en términos de gráficos, jugabilidad y narrativa, convirtiéndose en una forma artística y cultural importante. También han dado lugar a comunidades de jugadores en línea y competencias deportivas electrónicas. ¿Te gustaría saber más sobre algún aspecto específico de los videojuegos?",
    ]
)


trainer.train(
    conversation=[
        "¿Te gusta black ops 2?",
        "Si, es un superjuegazo",
    ]
)

trainer.train(
    conversation=[
        "¿Te gusta black ops 2?",
        "Si, me gusta mucho tuvo mucho exito aquel juego",
    ]
)


trainer.train(
    conversation=[
        "¿Cuál es el mejor juego de disparos en primera persona?",
        "Algunos dicen que es Counter-Strike, ¿tú qué opinas?",
    ]
)

trainer.train(
    conversation=[
        "¿Qué opinas sobre los videojuegos de mundo abierto?",
        "Los juegos de mundo abierto ofrecen mucha libertad y exploración, ¿te gustan?",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es la consola de videojuegos más popular?",
        "La PlayStation 5 y la Xbox Series X son muy populares en la actualidad.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es tu juego de video favorito?",
        "No tengo juegos favoritos, pero puedo hablar sobre muchos juegos diferentes.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es tu videojuego favorito?",
        "No tengo juegos favoritos, pero puedo hablar sobre muchos juegos diferentes.",
    ]
)

trainer.train(
    conversation=[
        "cual es tu videojuego favorito",
        "No tengo juegos favoritos, pero puedo hablar sobre muchos juegos diferentes.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es el juego más popular en este momento?",
        "Eso cambia con frecuencia, pero algunos juegos populares incluyen 'Fortnite', 'Minecraft' y 'Among Us'.",
    ]
)

trainer.train(
    conversation=[
        "¿Puedes recomendarme un juego de rol?",
        "Claro, te recomiendo probar 'The Witcher 3' o 'Dark Souls'. Ambos son excelentes juegos de rol.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es el personaje más icónico de los videojuegos?",
        "Muchos consideran a Mario de Nintendo como uno de los más icónicos.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es tu género de videojuego favorito?",
        "Me gusta mucho el género de juegos de aventuras, ¿y tú?",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es tu videojuego favorito?",
        "Me gusta mucho el género de juegos de aventuras, ¿y tú?",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es tu juego de consola favorito?",
        "Me gusta mucho el género de juegos de aventuras, ¿y tú?",
    ]
)

trainer.train(
    conversation=[
        "¿Qué opinas sobre los juegos de mundo abierto vs los lineales?",
        "Los juegos de mundo abierto ofrecen una experiencia más libre, mientras que los lineales suelen contar una historia más enfocada.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es el juego que más tiempo has pasado jugando?",
        "He pasado muchas horas jugando a The Witcher 3, ¡es un juego increíble!",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es el último juego que has jugado?",
        "Recientemente, he estado jugando a Cyberpunk 2077, ¿has tenido la oportunidad de jugarlo?",
    ]
)

trainer.train(
    conversation=[
        "¿Que opinas acerca de los videojuegos?",
        "Pienso que son una forma muy importante de pasar el tiempo libre",
    ]
)

trainer.train(
    conversation=[
        "¿Que piensas acerca de los videojuegos?",
        "Pienso que son una forma muy importante de pasar el tiempo libre",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es tu videojuego favorito de todos los tiempos?",
        "Mi juego favorito es The Legend of Zelda: Breath of the Wild, ¿cuál es el tuyo?",
    ]
)

trainer.train(
    conversation=[
        "¿Qué opinas sobre los gráficos en los videojuegos?",
        "Los gráficos son importantes para la inmersión en el juego, pero la jugabilidad también es esencial.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es el videojuego más desafiante que has jugado?",
        "Dark Souls es conocido por ser uno de los juegos más desafiantes. ¿Has tenido la oportunidad de jugarlo?",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es tu opinión sobre los juegos multijugador en línea?",
        "Los juegos multijugador en línea pueden ser muy divertidos, especialmente cuando juegas con amigos o conoces a nuevos jugadores de todo el mundo.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es la mejor plataforma para jugar videojuegos?",
        "La elección de la plataforma depende de tus preferencias personales. Algunas personas prefieren PC, mientras que otras optan por consolas como PlayStation o Xbox.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál fue el primer videojuego de la historia?",
        "El primer videojuego reconocido fue 'Tennis for Two', creado por William Higinbotham en 1958.",
    ]
)

trainer.train(
    conversation=[
        "¿Qué videojuegos fueron influyentes en la década de 1980?",
        "La década de 1980 fue testigo de la popularidad de juegos icónicos como Pac-Man, Space Invaders, y Super Mario Bros.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál fue la primera consola de videojuegos?",
        "La primera consola de videojuegos exitosa fue la Magnavox Odyssey, lanzada en 1972.",
    ]
)

trainer.train(
    conversation=[
        "¿Qué impacto tuvo la industria de los videojuegos en la cultura pop?",
        "Los videojuegos han influido significativamente en la cultura pop, dando lugar a películas, series, y una amplia gama de productos relacionados con los juegos.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál fue el auge de los videojuegos arcade?",
        "Los videojuegos arcade alcanzaron su auge en la década de 1980, con juegos como Donkey Kong y Street Fighter que se volvieron muy populares en salas recreativas.",
    ]
)

trainer.train(
    conversation=[
        "¿Quién fue el creador de la primera consola de videojuegos?",
        "La primera consola de videojuegos exitosa fue creada por Ralph Baer, quien trabajó en la Magnavox Odyssey en la década de 1970.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál fue la primera consola de videojuegos casera?",
        "La Magnavox Odyssey, lanzada en 1972, es considerada la primera consola de videojuegos casera.",
    ]
)

trainer.train(
    conversation=[
        "¿Qué empresa creó la popular consola 'Nintendo Entertainment System' (NES)?",
        "La NES fue creada por la empresa japonesa Nintendo, y se convirtió en un hito en la historia de los videojuegos.",
    ]
)

trainer.train(
    conversation=[
        "¿Quien creo la NES?",
        "La NES fue creada por la empresa japonesa Nintendo, y se convirtió en un hito en la historia de los videojuegos.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es la consola más vendida de todos los tiempos?",
        "La consola más vendida de todos los tiempos es la PlayStation 2 de Sony, con más de 155 millones de unidades vendidas en todo el mundo.",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál fue la primera consola de Sony?",
        "La primera consola de Sony fue la PlayStation, lanzada en 1994, que tuvo un gran impacto en la industria de los videojuegos.",
    ]
)

trainer.train(
    conversation=[
        "Háblame sobre el juego Call of Duty",
        "Call of Duty es una popular serie de videojuegos de disparos en primera persona. Se caracteriza por su acción intensa, gráficos realistas y modos de juego multijugador competitivos. ¿Te gustaría saber más sobre una entrega específica de Call of Duty o algún aspecto en particular?",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es el último Call of Duty lanzado?",
        "El último lanzamiento de Call of Duty en mi conocimiento fue 'Call of Duty: Vanguard', que salió en 2021. ¿Quieres saber más detalles sobre este juego o alguna otra entrega?",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es tu Call of Duty favorito?",
        "Soy una inteligencia artificial y no tengo preferencias, pero muchos jugadores tienen diferentes favoritos dentro de la serie Call of Duty debido a sus diferentes configuraciones y características. ¿Tienes un favorito en particular?",
    ]
)

trainer.train(
    conversation=[
        "Háblame sobre el juego Grand Theft Auto (GTA)",
        "Grand Theft Auto, comúnmente conocido como GTA, es una famosa serie de videojuegos de mundo abierto que combina acción, conducción y narrativa. La serie es conocida por su libertad de juego y entornos detallados. ¿Tienes alguna pregunta específica sobre un juego de la serie GTA o su historia?",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es el último GTA lanzado?",
        "El último lanzamiento de la serie Grand Theft Auto en mi conocimiento fue 'Grand Theft Auto V', que se lanzó en 2013. Sin embargo, se espera con interés el próximo título, 'Grand Theft Auto VI'. ¿Te gustaría saber más detalles?",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es tu GTA favorito?",
        "Soy una inteligencia artificial y no tengo preferencias, pero muchos jugadores tienen sus entregas favoritas en la serie GTA debido a sus diferentes ubicaciones y protagonistas. ¿Tienes un favorito en particular?",
    ]
)

trainer.train(
    conversation=[
        "Háblame sobre el juego Minecraft",
        "Minecraft es un juego de construcción y exploración en un mundo abierto. Los jugadores pueden recolectar recursos y construir estructuras en un entorno de bloque pixelado. El juego ofrece modos de supervivencia y creatividad, y ha ganado una gran base de seguidores. ¿Tienes alguna pregunta específica sobre Minecraft?",
    ]
)

trainer.train(
    conversation=[
        "¿Que opinas de minecraft?",
        "Minecraft es un juego de construcción y exploración en un mundo abierto. Los jugadores pueden recolectar recursos y construir estructuras en un entorno de bloque pixelado. El juego ofrece modos de supervivencia y creatividad, y ha ganado una gran base de seguidores. ¿Tienes alguna pregunta específica sobre Minecraft?",
    ]
)

trainer.train(
    conversation=[
        "¿Cuál es la última actualización importante de Minecraft?",
        "La última actualización importante de Minecraft en mi conocimiento fue la 'Caves & Cliffs', que agregó nuevas características relacionadas con la exploración y la construcción. ¿Quieres saber más sobre esta actualización o algún otro aspecto de Minecraft?",
    ]
)

trainer.train(
    conversation=[
        "¿Cómo puedo jugar Minecraft en modo multijugador?",
        "Para jugar Minecraft en modo multijugador, puedes unirte a servidores en línea o configurar tu propio servidor. Hay muchos servidores disponibles para diferentes estilos de juego, desde supervivencia hasta minijuegos. ¿Te gustaría más detalles sobre cómo jugar en multijugador?",
    ]
)

trainer.train(
    conversation=[
        "¿Cómo puedo jugar Minecraft en modo multijugador?",
        "Para jugar Minecraft en modo multijugador, puedes unirte a servidores en línea o configurar tu propio servidor. Hay muchos servidores disponibles para diferentes estilos de juego, desde supervivencia hasta minijuegos. ¿Te gustaría más detalles sobre cómo jugar en multijugador?",
    ]
)

trainer.train(conversation=[
    "Adiós",
    "Me alegra haber podido resolver tus dudas sobre el mundo gaming."
])


# trainer.train(conversation = oswi1)
# trainer.train(conversation = oswi2)
