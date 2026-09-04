from django.shortcuts import render
def inicio(request):
    """Vista para la página de inicio"""
    return render(request, 'portal/inicio.html')

def proyectos(request):
    return render(request, 'portal/proyectos.html')

def tipos(request):
    return render(request, 'portal/tipos.html')

def quiensoy(request):
    return render(request, 'portal/quiensoy.html')
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google import genai
import json
import os


@csrf_exempt
def asistente(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    try:
        data = json.loads(request.body)
        pregunta = data.get("pregunta", "").strip()

        if not pregunta:
            return JsonResponse(
                {"error": "No escribiste ninguna pregunta"},
                status=400
            )

        client = genai.Client(
            api_key=os.environ.get("GEMINI_API_KEY")
        )

        prompt = f"""
        Sos el asistente virtual de ArduinoHub.

        Tu función es ayudar a los visitantes a aprender sobre:
        - Arduino
        - programación
        - electrónica
        - placas Arduino
        - componentes electrónicos
        - proyectos con Arduino

        Respondé en español, de manera clara y sencilla.
        Si la pregunta no tiene relación con Arduino, programación
        o electrónica, indicá amablemente que tu función principal
        es ayudar con esos temas.

        Pregunta del usuario:
        {pregunta}
        """

        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=prompt
        )

        return JsonResponse({
            "respuesta": response.text
        })

    except Exception as e:
        return JsonResponse(
            {"error": "Ocurrió un error al comunicarse con el asistente."},
            status=500
        )
# Create your views here.
