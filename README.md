## Simple API Rest server

##### Setup

- **Certs & key** 
```
mkdir -p ~/certs
openssl req -x509 -newkey rsa:2048 -nodes \
  -keyout ~/certs/localhost.key \
  -out ~/certs/localhost.crt \
  -days 365 \
  -subj "/CN=localhost"
```

- **Nginx** `sudo apt update && sudo apt install nginx -y`
- For testing: add to `/etc/hosts`: `127.0.0.1   myapi.local`
- Create nginx conf file: see `conf/myapi`, ensure it points to your cert and key files
- Create a symbolic link to your nginx conf file: `sudo ln -s [path-to-your-project]/conf/myapi /etc/nginx/sites-enabled/myapi`
- Start / Restart nginx: `sudo nginx -t && sudo systemctl reload nginx`

- **pip install** `pip install uvicorn fastapi`


##### Usage

- In a "server" terminal: `python srv.py`

```bash
(myenv) ➜  python srv.py                                          
INFO:     Started server process [6532]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:35428 - "POST /raw HTTP/1.1" 200 OK
INFO:     127.0.0.1:55288 - "POST /raw HTTP/1.1" 200 OK
INFO:     127.0.0.1:55300 - "POST /raw HTTP/1.1" 200 OK
```


- In a "client" terminal: 
```bash
➜  curl -k https://myapi.local/hello
{"message":"Hello from FastAPI via Nginx"}

➜  curl -k -X POST https://myapi.local/raw -d "Hello world in raw data"
{"length":23,"preview":"Hello world in raw data","saved":"uploads/20250922T131419Z.bin"}

➜  curl -k -X POST http://localhost:8000/raw --data-binary @test_data/received_file_20250708_060657.bin
{"length":11311,"preview":"\u0000\u0000\u0007,HM-0225-00031\u0000PlhF4:00:46:29:7F:A7c1\u0012\u00002\u0000\u0015\u0018\u0001\u0001\u0000\u0003\u0000\u0000\u0000olh\b\u0000\u0000\u0000<\u0011\f\u0000\u0013\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0004\u0000\u0007\u000f\u0002ZZ2\u0000\u0005\u0000\u0000\u0000\u0000\u0000\u0000","saved":"uploads/20250922T155451Z.bin"}%
```

The route `raw` will create a bin file with the raw binary received in the payload
