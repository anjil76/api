import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON"}),
            status_code=400,
            mimetype="application/json"
        )

    text = body.get("text")
    if not text:
        return func.HttpResponse(
            json.dumps({"error": "Missing 'text' field"}),
            status_code=400,
            mimetype="application/json"
        )

    return func.HttpResponse(
        json.dumps({"you_sent": text}),
        status_code=200,
        mimetype="application/json"
    )
