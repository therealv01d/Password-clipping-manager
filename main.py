from project import Smoklip
import sys

if len(sys.argv) < 2:
    print("[*] Usage: python smoclip.py account")
    sys.exit()
username = sys.argv[1] 

try:
    s = Smoklip()
    s.askusername(username)
except Exception as e:
    print(str(e))
