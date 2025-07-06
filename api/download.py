import requests

def handler(request, response):
    url = request.query.get("url")
    if not url:
        response.status_code = 400
        return response.send("Missing 'url' query parameter")

    try:
        img_res = requests.get(url)
        if img_res.status_code != 200:
            response.status_code = 502
            return response.send("Failed to fetch image")

        response.set_header("Content-Type", img_res.headers.get("Content-Type", "application/octet-stream"))
        response.set_header("Content-Disposition", 'attachment; filename="enhanced.jpg"')
        response.body = img_res.content
        return response
    except Exception as e:
        response.status_code = 500
        return response.send(f"Error: {str(e)}")
