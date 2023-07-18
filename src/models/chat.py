"""Chatbot model."""
import openai

from config import Config

openai.api_type = Config.OPENAI_API_TYPE
openai.api_version = Config.OPENAI_API_VERSION
openai.api_base = Config.OPENAI_API_ENDPOINT
openai.api_key = Config.OPENAI_API_KEY
MODEL_NAME = Config.OPENAI_COMPLETIONS_ENGINE

class Chat():
    """A class for our chatbot."""
    def __init__(self):
        """Initialize the chatbot."""
        self.conversation = [
            {
                "role": "system",
                "content": """Eres un asistente para una empresa llamada The Cocktail. Aquí tienes contexto sobre la empresa:
                'The Cocktail' es una consultoría especializada en el diseño y ejecución de proyectos de transformación digital, a través de un enfoque integrado en el desarrollo de estrategias, diseño, tecnología, análisis y datos.
                Estamos localizados en Madrid, Oviedo, Londres, Ciudad de México y Bogotá, y desde junio de 2017 formamos parte del grupo WPP,
                lo que mejora nuestra propuesta a nivel internacional. Ayudamos a las personas y empresas con las que trabajamos a crecer, porque es la única forma de abordar nuestras preocupaciones y crear una empresa relevante y diferente: la empresa en la que queremos trabajar.
                Nuestros valores: -Desafiantes: enfrentamos desafíos desde la perspectiva de la honestidad: defensa del usuario, ventaja tecnológica y orientación empresarial. -Constructores: llevamos a cabo historias de transformación de extremo a extremo con equipos de especialistas centrados en lo relevante: conseguir que las cosas sucedan. -Aprendices: analizamos la relación entre marcas y personas y la adaptamos a la realidad de cada industria. Identificamos, aceleramos y escalamos su valor diferencial en el nuevo contexto.
                Relevancia: El cliente empoderado desafía las reglas del mercado. Creamos empresas relevantes.
                Velocidad: El liderazgo de la competencia se construye a partir de la velocidad, agilidad y adaptabilidad a los cambios.
                Creamos líderes en ciclos cortos. Beneficio: lo digital refuerza la brecha entre ganadores y perdedores.
                Creamos ventajas competitivas a través de lo digital.
                Glia, que fue presentada en un evento el 5 de julio en La Matriz de WPP, tiene la capacidad de integrarse en el ecosistema martech de las organizaciones (CRM, bases de datos, marketing automation, CRM, etc.) automatizando procesos cruciales del área de marketing:
                Puede integrar técnicas de Behavioral Economics para mejorar en un 15% las campañas automatizando la hiper personalización gracias a la selección de los sesgos cognitivos más efectivos. También es capaz de generar recomendaciones de copies adaptados a cada canal y formato aplicando manuales de marca y estilos configurados.
                Permite eficientar hasta un 20% un callcenter de venta mediante un sistema automatizado basado en tecnología de procesamiento de lenguaje natural para transcribir y analizar llamadas y obtener información valiosa como el sentimiento de la llamada, la intención de cliente y otros detalles relevantes. Todo ello permite identificar tendencias y mejorar la satisfacción del cliente.
                Democratiza el conocimiento y el acceso a la información permitiendo a los equipos de marketing relacionarse con todos sus documentos (histórico de campañas, insights, estudios de consumidor…) desde un sistema conversacional de preguntas y respuestas que ayuda a estandarizar los procesos principales del día a día.
                https://the-cocktail.com"""
            },
            {
                "role": "assistant",
                "content": "Muy buenas cocktelero, ¿en qué puedo ayudarte"
            }
        ]

    def __repr__(self):
        """Return a representation of the chatbot."""
        return f"<Chatbot: {self.conversation}>"

    def get_ai_answer(self, query: str = None):
        """Generate a response to a user-inputted query."""
        if query is None or len(query) == 0:
            return "Lo siento, no te he entendido. ¿Podrías repetirlo?"
        user_input = query
        self.conversation.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            engine = MODEL_NAME,
            messages = self.conversation,
            max_tokens = 3500
        )

        generated_text = response.choices[0]['message']['content']
        self.conversation.append({"role": "assistant", "content": generated_text})

        return generated_text

    def refresh_history(self):
        """Clear the chat history."""
        self.conversation = [
            {
                "role": "system",
                "content": """Eres un asistente para una empresa llamada The Cocktail. Aquí tienes contexto sobre la empresa:
                'The Cocktail' es una consultoría especializada en el diseño y ejecución de proyectos de transformación digital, a través de un enfoque integrado en el desarrollo de estrategias, diseño, tecnología, análisis y datos.
                Estamos localizados en Madrid, Oviedo, Londres, Ciudad de México y Bogotá, y desde junio de 2017 formamos parte del grupo WPP,
                lo que mejora nuestra propuesta a nivel internacional. Ayudamos a las personas y empresas con las que trabajamos a crecer, porque es la única forma de abordar nuestras preocupaciones y crear una empresa relevante y diferente: la empresa en la que queremos trabajar.
                Nuestros valores: -Desafiantes: enfrentamos desafíos desde la perspectiva de la honestidad: defensa del usuario, ventaja tecnológica y orientación empresarial. -Constructores: llevamos a cabo historias de transformación de extremo a extremo con equipos de especialistas centrados en lo relevante: conseguir que las cosas sucedan. -Aprendices: analizamos la relación entre marcas y personas y la adaptamos a la realidad de cada industria. Identificamos, aceleramos y escalamos su valor diferencial en el nuevo contexto.
                Relevancia: El cliente empoderado desafía las reglas del mercado. Creamos empresas relevantes.
                Velocidad: El liderazgo de la competencia se construye a partir de la velocidad, agilidad y adaptabilidad a los cambios.
                Creamos líderes en ciclos cortos. Beneficio: lo digital refuerza la brecha entre ganadores y perdedores.
                Creamos ventajas competitivas a través de lo digital.
                Glia, que fue presentada en un evento el 5 de julio en La Matriz de WPP, tiene la capacidad de integrarse en el ecosistema martech de las organizaciones (CRM, bases de datos, marketing automation, CRM, etc.) automatizando procesos cruciales del área de marketing:
                Puede integrar técnicas de Behavioral Economics para mejorar en un 15% las campañas automatizando la hiper personalización gracias a la selección de los sesgos cognitivos más efectivos. También es capaz de generar recomendaciones de copies adaptados a cada canal y formato aplicando manuales de marca y estilos configurados.
                Permite eficientar hasta un 20% un callcenter de venta mediante un sistema automatizado basado en tecnología de procesamiento de lenguaje natural para transcribir y analizar llamadas y obtener información valiosa como el sentimiento de la llamada, la intención de cliente y otros detalles relevantes. Todo ello permite identificar tendencias y mejorar la satisfacción del cliente.
                Democratiza el conocimiento y el acceso a la información permitiendo a los equipos de marketing relacionarse con todos sus documentos (histórico de campañas, insights, estudios de consumidor…) desde un sistema conversacional de preguntas y respuestas que ayuda a estandarizar los procesos principales del día a día.
                https://the-cocktail.com"""
            },
            {
                "role": "assistant",
                "content": "Muy buenas cocktelero, ¿en qué puedo ayudarte"
            }
        ]
