def myapp(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    s = env["QUERY_STRING"]
    print s
    s = s.replace("&","\n")
    print s
    start_response(status, headers)
    return [s]
