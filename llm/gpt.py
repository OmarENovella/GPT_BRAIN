from openai import OpenAI

client = OpenAI()

format_user_query = lambda ms: {"role" : "user", "content" : ms} # Formatear una peticion de usuario para su uso
format_system_role = lambda rl: {"role" : "system", "content" : rl} # Formatear un rol de asistente
format_assistant_response = lambda rsp: {"role" : "assistant", "content" : rsp} # Formatear una respuesta del asistente

def gpt_model_response(
        messages: list, 
        temperature: int, 
        modelName: str = "gpt-3.5-turbo"):
    
    """
    Esta funcion nos permitira obtener una respuesta simple del modelo a desear
    esta solo retornara el contenido, en los parametros a manejarse se deberan colocar
    los valores en base a lo siguiente:

    temperature - La temperatura de nuestra respuesta, si la temperatura es proxima a 0
    la respuesta sera mas precisa en base a la cercania, si la temperatura es alejada de 0
    esta cera mas creativa 

    modelName - el nombre del modelo de gpt a utilizarse, por defecto el modelo sera el gpt-3.5-turbo

    messages - aqui ira la lista con todas nuestras peticiones y mensajes para el modelo
    las peticiones insertadas a la lista deberan estar formateadas en base a lo que corresponda

    mensaje de usuario -> {"role" : "user", "content" : "mi mensaje como usuario"}

    Aqui ira nuestro mensaje de usuario con la peticion que queramos realizar

    respuesta del asistente -> {"role" : "assistant", "content" : "la respuesta del asistente"}

    Nos servira para conservar el hilo de la conversacion y que el asistente tenga nocion
    de las respuestas que este mismo ha mencionado anteriormente

    prompt (rol de asistente) -> {"role" : "system", "content" : "el rol del asistente" } 

    El rol que queremos que tome nuestro asistente este siempre debera estar al inicio de la
    secuencia de mensajes para un buen funcionamiento

    Documentacion - Omar Novella
    """

    completion = client.chat.completions.create(
        model= modelName,
        temperature= temperature,
        messages= messages
    )

    return completion.choices[0].message.content

def tools_gpt_model_response(
        messages: list, 
        tools: list, 
        temperature: int = 0,
        tools_choice: str =  "auto",
        modelName: str = "gpt-3.5-turbo"):
    
    """
    Nos permitira obtener una respuesta en base a la funcion que invoque 
    el modelo deseado si no hay funcion que invocarse esta retornara un valor de tipo None,
    en los parametros a manejarse se deberan colocar los valores en base a lo siguiente:

    temperature - La temperatura de nuestra respuesta, si la temperatura es proxima a 0
    la respuesta sera mas precisa en base a la cercania, si la temperatura es alejada de 0
    esta cera mas creativa 

    modelName - el nombre del modelo de gpt a utilizarse, por defecto el modelo sera el gpt-3.5-turbo

    tools - La lista de diccionarios con la variedad de funciones integradas desarrolladas por el usuario

    messages - aqui ira la lista con todas nuestras peticiones y mensajes para el modelo
    las peticiones insertadas a la lista deberan estar formateadas en base a lo que corresponda

    mensaje de usuario -> {"role" : "user", "content" : "mi mensaje como usuario"}

    Aqui ira nuestro mensaje de usuario con la peticion que queramos realizar

    respuesta del asistente -> {"role" : "assistant", "content" : "la respuesta del asistente"}

    Nos servira para conservar el hilo de la conversacion y que el asistente tenga nocion
    de las respuestas que este mismo ha mencionado anteriormente

    prompt (rol de asistente) -> {"role" : "system", "content" : "el rol del asistente" } 

    El rol que queremos que tome nuestro asistente este siempre debera estar al inicio de la
    secuencia de mensajes para un buen funcionamiento

    Documentacion - Omar Novella
    """

    completion = client.chat.completions.create(
        model= modelName,
        temperature= temperature,
        tools= tools,
        tool_choice= tools_choice,
        messages= messages
    ) 

    responseMessage = completion.choices[0].message

    return responseMessage 


