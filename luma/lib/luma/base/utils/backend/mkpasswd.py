#$Id$
'''
 Module written by Bjorn Ove Grotan <bgrotan@samfundet.no>

  Mkpasswd is free software; you can redistribute it and/or modify it
  under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.
 
  Mkpasswd is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  General Public License for more details.
 
  You should have received a copy of the GNU General Public License
  along with Cerebrum; if not, write to the Free Software Foundation,
  Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

 For extra strength passwords, we wanted SSHA in our LDAP-environment
 as the standard python-module 'sha' does not support ssha, but this can 
 easily be implemented with a few extra functions. 

 SSHA can be described as:
     the SHA1-digest of a password with a sequence of "salt" bytes, where
     the bytes are randomly chosen - followed by the same salt bytes
 For LDAP-use, the SHA1 and SSHA-digest has to be base64-encoded. 

 SHA and SSHA are described at:
 http://developer.netscape.com/docs/technote/ldap/pass-sha.html
 This page have examples for Perl and Java if one would prefer that.

 Example-LDIF:
     {SSHA}oaEG3PJ10sHxGcSxsDRRooTifL55/2NOdN3nU1VEV+NFzc9Q
 
 This package should now support passwords compatible with [1] Samba using the [2]
 smbpasswd module for [3] Python. You should find a recent copy of this software 
 at the project [4] webpage. The samba compability is added for use with Samba as
 PDC with storing user and host-information in LDAP.

 [1] http://www.samba.org
 [2] http://barryp.org/software/py-smbpasswd/
 [3] http://www.python.org
 [4] http://www.grotan.com/project/python
'''
import string,base64
import random,sys
import md5,sha,crypt
smb = 0 # Where 1 is true, and 0 is false

try:
    import smbpasswd
    smb = 1 
except:
    smb = 0

def getsalt(chars = string.letters + string.digits,length=16):
    ''' Generate a random salt. Default length is 16 '''
    salt = ''
    for i in range(int(length)):
        salt += random.choice(chars)
    return salt

def randpasswd(chars = string.digits + string.ascii_letters,length=8):
    ''' Returns a random password at a given length based on a character-set.'''
    result = ''
    for i in range(length):
        result = result + getsalt(chars,1)
    return result

def mkpasswd(pwd,sambaver=3,default='ssha'):
    ''' Make a given password cryptated, possibly with different 
        crypt-algorihtms. This module was written for use with 
        LDAP - so default is seeded sha
    '''
    alg = {
        'ssha':'Seeded SHA',
        'sha':'Secure Hash Algorithm',
        'md5':'MD5',
        'crypt':'standard unix crypt'
    }
    if smb:
        alg['lmhash'] = 'lan man hash'
        alg['nthash'] = 'nt hash'
    if default not in alg.keys():
        return 'algorithm <%s> not supported in this version.' % default
    else:
        salt = getsalt()
        if default == 'ssha':
            return "{SSHA}" + base64.encodestring(sha.new(str(pwd) + salt).digest() + salt)
        elif default =='sha':
            return "{SHA}" + base64.encodestring(sha.new(str(pwd)).digest())
        elif default =='md5':
            return "{MD5}" + base64.encodestring(md5.new(str(pwd)).digest())
        elif default =='crypt':
            return "{CRYPT}" + crypt.crypt(str(pwd),getsalt(length=2)) # crypt only uses a salt of length 2
        elif default == 'lmhash':
            if sambaver==3:
                return "{sambaLMPassword}" + smbpasswd.lmhash(pwd)
            elif sambaver==2:
                return "{lmPassword}" + smbpasswd.lmhash(pwd)
        elif default == 'nthash':
            if sambaver==3:
                "{sambaNTPassword}" + smbpasswd.lmhash(pwd)
            elif sambaver==2:
                return "{NTPassword}" + smbpasswd.lmhash(pwd)
