tools = [

{
    "type" : "function",
    "function" : {
    "name" : "opening_app",
    "description" : """
        Permite abrir solo programas nativos de Windows directamente del Inicio 
    """,
    "parameters" : {
        "type" : "object",
        "properties" : {
            "app_name" : {
                "type" : "string",
                "description" : """
                    Muestra el nombre de la aplicacion que se desea abrir
                """
                }
            },
            "required" : ["app_name"]
        }
    }
},

{
    "type" : "function",
    "function" : {
    "name" : "window_actions_manager",
    "description" : """
        Permite controlar distintas funciones de control de programas como minimizar / maximizar o
        cerrar programas
    """,
    "parameters" : {
        "type" : "object",
            "properties" : {
                "value" : {
                    "type" : "integer",
                    "description" : """
                    Devuelve:
                    1 - maximizar,
                    2 - minimizar,
                    3 - cerrar.
                    """
                }
            },
            "required" : ["value"]
        }
    }
},

{
    "type" : "function",
    "function" : {
        
        "name" : "volume_control",
        "description" : """
        Permite controlar el volumen del sistema en digitos del 0 al 100 de acuerdo
        con la peticion del usuario
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "volume_value" : {
                    "type" : "integer",
                    "description" : """
                    Devuelve un numero entre 0 y 100 que representa
                    el volumen solicitado por el usuario para el sistema
                    """
                }
            },
            "required" : ["volume_value"]
        }
    }
},

{
    "type" : "function",
    "function" : {
        "name" : "media_manager",
        "description" : """
        Permite controlar elementos multimedia como la pausa / reproduccion, pista siguiente y pista anterior
        por medio de teclas de pyautogui cuando el usuario mencione alguna de las acciones
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "key" : {
                    "type" : "integer",
                    "description" : """
                    Devuelve:
                    1 - pausa o play, 
                    2 - pista siguiente,
                    3 - pista anterior.
                    """
                }
            },
            "required" : ["key"]
        }
    }
},

{
    "type" : "function",
    "function" : {
        "name" : "play_on_youtube",
        "description" : """
        Detecta cuando el usuario ha solicitado buscar un video / musica / tutorial
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "name" : {
                    "type" : "string",
                    "description" : """
                    Muestra el nombre del video que se desea reproducir
                    """
                }
            },
            "required" : ["name"]
        }
    }
},

{
    "type" : "function",
    "function" : {
        "name" : "volume_control",
        "description" : """
        Permite controlar el volumen del sistema en digitos del 0 al 100 de acuerdo
        con la peticion del usuario
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "volume_value" : {
                    "type" : "integer",
                    "description" : """
                    Devuelve un numero entre 0 y 100 que representa
                    el volumen solicitado por el usuario para el sistema
                    """
                }
            },
            "required" : ["volume_value"]
        }
    }
},

{
    "type" : "function",
    "function" : {
        "name" : "keyboard_control",
        "description" : """
        Detecta cuando el usuario ha solicitado que se presionen ciertas teclas, usando
        el nombre de los botones disponibles de pyautogui
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "keys" : {
                    "type" : "string",
                    "description" : """
                    Devuelve:
                    contiene todas la sequencia de teclas
                    que se presionaran en formato de pyautogui
                    con su nombre respectivo separada cada una por una coma ','
                    """
                }
            },
            "required" : ["keys"]
        }
    }
},

{
    "type" : "function",
    "function" : {
        "name" : "tab_manager",
        "description" : """
        Controla las pestañas del navegador google chrome
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "action" : {
                    "type" : "integer",
                    "description" : """
                        1 - cerrar la pestaña
                        2 - pestaña siguiente
                        3 - pestaña anterior
                        4 - abrir nueva pestaña
                        5 - Abrir la ultima pestaña abierta
                        6 - Abrir nueva pestaña en modo incognito
                    """
                }
            },
            "required" : ["action"]
        }
    }
},

{
    "type" : "function",
    "function" : {
        "name" : "code_creation",
        "description" : """
        Cuando un usuario pida la creacion de codigo o haga una peticion que no este en los registros y amerite la creacion de codigo
        esta funcion retornara la peticion del usuario
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "query" : {
                    "type" : "string",
                    "description" : """
                        La peticion del usuario con ortografia corregida y directa a su proposito
                    """
                }
            },
            "required" : ["query"]
        }
    }
},

{
    "type" : "function",
    "function" : {
        "name" : "assistant_manners",
        "description" : """
        Esta funcion se activa con el fin de que el usuario tenga mas control sobre
        las acciones del asistente 
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "action" : {
                    "type" : "integer",
                    "description" : """
                    1- Se le ha solicitado que guarde silencio al asistente
                    """
                }
            },
            "required" : ["action"]
        }
    }
}





]