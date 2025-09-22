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
- In a "client" terminal: 
```
curl -k https://myapi.local/hello
{"message":"Hello from FastAPI via Nginx"}

curl -k -X POST https://myapi.local/raw -d "Hello world in raw data"
{"length":23,"preview":"Hello world in raw data","saved":"uploads/20250922T131419Z.bin"}
```

The route `raw` will create a bin file with the raw binary received in the payload
