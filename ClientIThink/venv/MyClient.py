from http import client

hostName = "localhost"
hostPort = 8000
conn = client.HTTPConnection(hostName, hostPort)





running = True;



while running:

    key = input('>> ')

    if key is '1':
        print("GET request")
        conn.request("GET", "index")
        response = conn.getresponse()
        data = response.read()
        print("GET response: " + data.decode())

    if key is '2':
        print("POST request")
        data_to_post = input("message to send >>")

        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn.request("POST", "add_score", data_to_post.encode(), headers)
        response = conn.getresponse()
        data = response.read()
        print("POST response: " + data.decode())

    if key is 'x':
        running = False