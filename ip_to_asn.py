from pyasn import pyasn

# Load the ASN database
asn_db = pyasn('ipasn.dat')  # Replace 'ipasn.dat' with the path to your database

# Get the ASN for a given IP address
ip_address = '8.8.8.8'
asn, prefix = asn_db.lookup(ip_address)

print(f"ASN for {ip_address}: {asn}")
