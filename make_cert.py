from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta, timezone
import ipaddress
import os

# Folder for certificate
FOLDER = r"GOES HERE" #YOUR FOLDER LOCATION
os.chdir(FOLDER)

# Generate private key
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Certificate subject and issuer (self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Python AI Agent"),
    x509.NameAttribute(NameOID.COMMON_NAME, "YOUR STATIC IP"),
])

cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.now(timezone.utc))
    .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))
    .add_extension(
        x509.SubjectAlternativeName([
            x509.IPAddress(ipaddress.ip_address("192.xxx.xxx.xxx")), #YOUR STATIC IP GOES HERE
        ]),
        critical=False,
    )
    .sign(key, hashes.SHA256())
)

# Write key
with open("server.key", "wb") as f:
    f.write(
        key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

# Write cert
with open("server.crt", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("New server.crt and server.key created in the folder:", FOLDER)


