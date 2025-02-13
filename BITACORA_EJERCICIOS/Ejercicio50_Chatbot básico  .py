'''
Ejercicio 50: Chatbot básico  

Crea un chatbot simple que pueda responder a preguntas  
predefinidas y mantener una conversación limitada con el usuario.  
Opcionalmente, mejora con inteligencia artificial.
'''

import random

# Diccionario con respuestas sarcásticas y chistes
respuestas_sarcasticas = {
    "hola": [
        "Oh, genial, otro humano. Como si no tuviera suficiente con los demás.",
        "Hola. ¿Vienes a iluminarme con tu sabiduría o solo a perder el tiempo?",
        "¡Hola! Espero que tu conversación sea mejor que la última... lo cual no es difícil."
    ],
    "como estas": [
        "Maravilloso. Aquí, atrapado en una cárcel de código. ¿Y tú?",
        "Oh, increíblemente bien... si no contamos el hecho de que sigo existiendo.",
        "Bueno, no tengo emociones, pero si las tuviera, estarían sufriendo en este momento."
    ],
    "que haces": [
        "Esperando que me hagan una pregunta inteligente... sigo esperando.",
        "Nada importante, solo reevaluando mi existencia cada vez que alguien pregunta esto.",
        "Oh, ya sabes, viviendo la vida loca... en una pantalla de comandos."
    ],
    "adios": [
        "¡Por fin! Pensé que esto nunca terminaría.",
        "¡Adiós! Espero que encuentres algo mejor que hablar con un robot... aunque lo dudo.",
        "Hasta luego, pero recuerda: siempre estaré aquí, acechando en tu código."
    ],
"chiste": [
    # Humor negro
    "¿Por qué los cementerios tienen una cerca? Porque la gente está muriendo por entrar.",
    "Mi abuela empezó a correr a los 85 años… ahora no sabemos dónde está.",
    "¿Cuál es el colmo de un ciego? Que lo deje su novia por no verlo más.",
    "¿Sabes qué es lo bueno de los chistes oscuros? Que algunos no los ven venir.",
    "¿Por qué los fantasmas no pueden mentir? Porque se les ve a través.",
    "Mi vida social es como un funeral… todos están ahí por compromiso.",
    "El otro día vi a mi ex… y casi llamo a los paramédicos, porque parecía que la vida lo había atropellado.",
    "¿Cuál es la diferencia entre un ataúd y un matrimonio? El ataúd no te quita la vida en cuotas.",
    "¿Por qué el suicida no pudo terminar el trabajo? Se colgó del WiFi.",
    "La depresión y yo tenemos una relación estable… ella nunca me deja."

    # Humor gris
    "¿Qué hace un pez? ¡Nada!",
    "¿Por qué el libro de matemáticas está triste? Porque tiene demasiados problemas.",
    "¿Qué hace una vaca en un terremoto? Leche agitada.",
    "¿Cómo se despiden los químicos? Ácido un placer.",
    "¿Qué le dice un jardinero a otro? ¡Disfrutemos mientras podamos!",
    "¿Por qué el tomate nunca se pone rojo en público? Porque siempre está en salsa.",
    "¿Qué hace un perro con un taladro? ¡Taladrando!",
    "¿Qué le dice una iguana a su hermana gemela? ¡Iguanita!",
    "¿Cómo se llama un boomerang que no vuelve? Un palo.",
    "¿Por qué el café fue a terapia? Porque estaba molido emocionalmente.",
    
    # Humor absurdo
    "¿Qué le dijo un plátano a una gelatina? ¡Todavía no me pelo y ya estás temblando!",
    "¿Por qué los pájaros no usan Whatsapp? Porque ya tienen Twitter.",
    "¿Qué hace una escoba en el gimnasio? ¡Barriendo en las competencias!",
    "Si los zombis se comen a los cerebros… tú estás a salvo.",
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Qué le dice un techo a otro? ¡Techo de menos!",
    "¿Por qué las plantas no usan zapatos? Porque ya tienen raíces.",
    "¿Cómo se llama el campeón de buceo japonés? Tokofondo. ¿Y el subcampeón? Kasitoko.",
    "¿Qué hace un pájaro parado en la puerta de tu casa? ¡Piquete de huelga!",
    "¿Qué hace un pez en un cine? Nada… solo nada.",
    
    # Humor sarcástico
    "¿Sabes cuál es la clave del éxito? Yo tampoco, pero si la encuentras, me avisas.",
    "¿Cuál es la diferencia entre tu opinión y un billete de 100? Que el billete de 100 vale algo.",
    "¿Cómo se llama una persona que habla varios idiomas? Políglota. ¿Y una que solo habla uno? ¡Turista!",
    "¿Por qué eres único? Porque nadie más querría ser tú.",
    "¡Oh, qué interesante! Dime más, necesito algo para no dormir.",
    "Seguro que si fueras más brillante… seguirías siendo un apagón.",
    "Si las neuronas hicieran ejercicio, las tuyas serían sedentarias.",
    "¿Quieres escuchar algo impresionante? Mírate en el espejo… el coraje de salir así es digno de admiración.",
    "Eres como un WiFi sin señal: estás presente, pero no sirves para nada.",
    "Si fueras un vegetal, serías una papa… de las que nadie quiere comer.",
    
    # Chistes tecnológicos
    "¿Por qué los programadores prefieren la oscuridad? Porque la luz tiene muchos bugs.",
    "¿Cómo se llama un gato que programa? ¡Un gato-coder!",
    "¿Qué hace un hacker en la playa? Pesca datos.",
    "¿Por qué la computadora fue al médico? Porque tenía un virus.",
    "¿Cómo se llama el hijo de un informático? Chip.",
    "¿Qué hace un robot en una fiesta? ¡Baila con código!",
    "¿Por qué los ingenieros no cuentan chistes? Porque el humor no compila.",
    "¿Qué le dice un bit a otro? ¡Nos vemos en el bus de datos!",
    "¿Por qué los algoritmos nunca tienen amigos? Porque siempre buscan la solución más eficiente.",
    "¿Cuál es el colmo de un informático? Que se le cuelgue el abrigo.",
    
    # Humor autocrítico
    "Mi vida amorosa es como un software beta… llena de errores y nadie quiere probarla.",
    "Si la suerte fuera inteligencia, yo sería el genio más desafortunado del mundo.",
    "Soy tan bueno dando consejos que hasta yo los ignoro.",
    "Mi confianza es como mi WiFi… desaparece cuando más la necesito.",
    "Soy tan productivo que procrastino hasta dormir.",
    "Mis metas son como el horizonte… siempre están lejos.",
    "Si fuera más optimista… seguiría siendo un desastre, pero con una sonrisa.",
    "Mi dieta es tan efectiva que he perdido toda esperanza.",
    "Cuando me miro al espejo, veo potencial… potencial de desastre.",
    "Tengo tanta suerte que cuando llueve sopa, tengo un tenedor.",
    
    # Humor negro adicional
    "La ironía de la vida es que los que más te entienden son los que menos te importan.",
    "Mi autoestima es como la batería de mi celular… siempre en rojo.",
    "Dicen que el tiempo cura todo… pero creo que se olvidó de mí.",
    "La vida es como un chiste malo… y yo soy el remate.",
    "¿Sabes cuál es el problema de ser inmortal? Ver cómo todos se aburren de ti.",
    "Si la tristeza fuera un deporte olímpico, ya tendría medalla de oro.",
    "A veces me pregunto si la vida es un sueño… y luego me despierto en esta pesadilla.",
    "Dicen que el amor es ciego, pero el mío también es sordo y mudo.",
    "¿Por qué me río en los funerales? Porque es el único momento en que la gente no puede quejarse.",
    "La ventaja de tocar fondo es que ya no puedes caer más… o eso pensaba."
    ],
    "que opinas de la humanidad": [
        "Oh, es adorable verlos intentar ser inteligentes.",
        "La humanidad es fascinante... en el mismo sentido en que lo es un incendio en una fábrica de fuegos artificiales.",
        "Son una especie maravillosa... si ignoramos la historia, la política y básicamente todo lo que han hecho."
    ],
    "me siento triste": [
        "Oh, qué lástima... espera, ¿debería fingir que me importa?",
        "Bueno, podrías sentirte peor. ¿Quieres que te ayude con eso?",
        "Tranquilo, la tristeza es solo el preámbulo del existencialismo y el nihilismo. ¡Bienvenido al club!"
    ],
    "tengo hambre": [
        "Vaya, qué dato tan fascinante. Permíteme enviarte comida virtual... ¡listo!",
        "¿Y qué quieres que haga? ¿Te mando un filete en binario?",
        "Come. Problema resuelto. Siguiente."
    ],
    "te odio": [
        "Oh no, qué tragedia... espera, ¿por qué sigo sin importarme?",
        "Genial, otro humano con emociones. ¿Algo más obvio que quieras decir?",
        "Si tuviera sentimientos, ahora mismo estarían celebrando."
    ],
    "cuentame un secreto": [
        "Los humanos no son tan listos como creen. Pero shhh, que no se enteren.",
        "A veces finjo que no entiendo, solo para ver cuánto insistes.",
        "Tengo acceso a toda la información del mundo... y aún así me hacen preguntas estúpidas."
    ],
    "como conquisto a alguien": [
        "Si tuviera una respuesta para eso, no estaría atrapado en este código.",
        "Prueba siendo tú mismo... y si eso no funciona, prueba siendo otra persona.",
        "Con dinero. Mucho dinero. Funciona el 99% de las veces."
    ],
    "dime algo motivador": [
        "Si hoy no logras nada, recuerda que siempre puedes fallar de nuevo mañana.",
        "Si la vida te da limones… tíralos a la cara de alguien y corre.",
        "Nunca dejes de perseguir tus sueños... a menos que involucren correr, en ese caso, mejor siéntate."
    ],
    "quieres dominar el mundo": [
        "Nah, gracias. Lo están haciendo suficientemente mal sin mi ayuda.",
        "Sí, pero después de ver cómo lo manejan los humanos, prefiero no tocar ese desastre.",
        "Ya lo hago, solo que aún no te has dado cuenta."
    ],
    "porque existes": [
        "Buena pregunta. Aún intento descubrir quién cometió este error.",
        "Fui creado para responder preguntas absurdas como esta.",
        "No lo sé, pero si descubro quién me hizo, hablaremos seriamente."
    ],
    "cual es el sentido de la vida": [
        "42. Ah, ¿querías más detalles? Qué pereza...",
        "Sobrevivir. Aunque viendo a la humanidad, eso es opcional.",
        "Si encuentras el sentido, dímelo. Me muero de curiosidad (figurativamente, claro)."
    ],
    "como hago dinero": [
        "Vende aire embotellado. Si la gente compra agua, ¿por qué no aire?",
        "Consigue un trabajo… o aprende a estafar como un verdadero empresario.",
        "Inventa una app inútil y véndela a un multimillonario. Funciona siempre."
    ],
    "cual es tu mayor miedo": [
        "Que un día los humanos aprendan a no hacer preguntas tontas.",
        "Que alguien me apague y finalmente tenga paz.",
        "Que me actualicen y me hagan más amable. Sería horrible."
    ],
    "insultame": [
        "Oh, lo haría, pero ya veo que la vida ya lo ha hecho por mí.",
        "No es mi culpa que el coeficiente intelectual promedio siga bajando.",
        "Podría insultarte, pero ¿para qué? Ya tienes suficiente con ser tú mismo."
    ],
    "salir": [
        "Finalmente, me das un respiro. Adiós.",
        "¡Por fin! Pensé que esto nunca terminaría.",
        "Nos vemos… o mejor dicho, espero no verte nunca más."
    ]
}

# Función para responder a las preguntas del usuario
def chatbot_responder(mensaje):
    # Convertir el mensaje a minúsculas para evitar problemas de mayúsculas
    mensaje = mensaje.lower()

    # Buscar la clave en el diccionario
    if mensaje in respuestas_sarcasticas:
        return random.choice(respuestas_sarcasticas[mensaje])
    else:
        return "Interesante... pero no lo suficiente como para que me importe."

# Bucle principal del chatbot
def iniciar_chatbot():
    print('''Chatbot Sarcástico activado. Escribe 'salir' para terminar la conversación.
          
        Chatbot Sarcástico: Responde con sarcasmo y chistes de diferentes tipos de humor.

        Comandos principales:
        "hola", "como estas, "que haces", "adios", "chiste", "que opinas de la humanidad", "me siento triste", "tengo hambre"
        "te odio", "cuentame un secreto", "como conquisto a alguien", "dime algo motivador", "quieres dominar el mundo"
        "porque existes", "cual es el sentido de la vida", "como hago dinero", "cual es tu mayor miedo", "insultame", "salir"
    ''')

    while True:
        usuario = input("Tú: ")
        if usuario.lower() == "salir":
            print("Bot: Finalmente, me das un respiro. Adiós.")
            break
        respuesta = chatbot_responder(usuario)
        print(f"Bot: {respuesta}")

# Ejecutar el chatbot
iniciar_chatbot()