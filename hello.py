def myapp(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    keys = env.keys()
    body = ""
    for key in keys:
        if body:
            body += "\n"
        body = body + key + "=" + env[key]
    start_response(status, headers)
    return [body]
