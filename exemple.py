import sys
sys.path.append('./Vicopo/')

from Vicopo import Vicopo

print(Vicopo.http(75001))

print(Vicopo.http('paris'))
