from flask import Flask, jsonify, request
import json
from llm.gpt import (
    tools_gpt_model_response, 
    gpt_model_response,
    format_user_query,
    format_assistant_response,
    format_system_role
)
from llm.roleTemplates import AssistantRole, FunctionCallingRole, CodeExecutionRole
from llm.functionsTemplates import tools

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    txt = """
    /tools_calling_detector -> Verificar si se ha solicitado el uso de alguna función 
    /get_model_response -> Obtener una respuesta del Modelo GPT
    """
    return txt

def validate_request_data(required_fields):
    data = request.get_json()
    if not all(field in data for field in required_fields):
        missing_fields = [field for field in required_fields if field not in data]
        raise ValueError(f"Missing fields: {', '.join(missing_fields)}")
    return data

@app.route("/tools_calling_detector", methods=["POST"])
def toolsCaller():
    try:
        data = validate_request_data(["message"])
        message = data["message"]
        
        response = tools_gpt_model_response(
            tools=tools,
            messages=[
                format_system_role(FunctionCallingRole),
                format_user_query(message)
            ]
        )
            
        return jsonify(response.to_dict())

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route("/code_ex", methods=["POST"])
def toolsCaller():
    try:
        data = validate_request_data(["message"])
        message = data["message"]
        
        response = gpt_model_response(
            temperature= 0,
            messages=[
                format_system_role(CodeExecutionRole),
                format_user_query(message),
            ]
        )
            
        return jsonify({"response" : response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get_model_response", methods=["POST"])
def modelResponse():
    try:
        data = validate_request_data(["message", "ms_history", "temperature"])

        _message = data["message"]
        _message_history = data["ms_history"]
        _temperature = data["temperature"]
        _function = data.get("function")

        message_history = json.loads(_message_history)
        temperature = float(_temperature)

        roled_messages_sequence = [format_system_role(AssistantRole)]

        if _function:
            function = json.loads(_function)
            message_history.append(function)
        
        message_history.append(format_user_query(_message))
        messages = roled_messages_sequence + message_history

        response = gpt_model_response(messages=messages, temperature=temperature)
        message_history.append(format_assistant_response(response))

        return jsonify({"response": response, "ms_history": message_history})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
