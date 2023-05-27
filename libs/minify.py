m='__main__'
l='All tests passed \\o/'
k='>'
j='The following scripts failed'
i='test_adodbapi_dbapi20.py'
h='adodbapitest.py'
g='1'
f='com'
e='testall.py'
d='win32com'
c='Pythonwin/pywin/test/all.py'
b='win32/test/testall.py'
a="Skip the adodbapi tests; useful for CI where there's no provider"
Z='-skip-adodbapi'
Y='Include tests which require user interaction'
X='(This is now the default - use `-user-interaction` to include them)'
W='-no-user-interaction'
V='A script to trigger tests in all subprojects of PyWin32.'
U='Failed to locate a test script in one of %s'
T="*** Test script '%s' exited with %s"
S="--- Running '%s' ---"
R='-u'
Q=RuntimeError
M='adodbapi'
L='-user-interaction'
H='test'
G='store_true'
F=False
B=print
import os as A,site as I,subprocess as N,sys as C
J=A.path.dirname(__file__)
K=[I.getusersitepackages()]+I.getsitepackages()
E=[]
def O(script,cmdline_extras):
	D=script;H,I=A.path.split(D);J=[C.executable,R,I]+cmdline_extras;B(S%D);C.stdout.flush();G=N.run(J,check=F,cwd=H);B(T%(D,G.returncode));C.stdout.flush()
	if G.returncode:E.append(D)
def D(possible_locations,extras):
	B=possible_locations
	for C in B:
		if A.path.isfile(C):O(C,extras);break
	else:raise Q(U%B)
def P():
	import argparse as S;Q=[J]+K;O=S.ArgumentParser(description=V);O.add_argument(W,default=F,action=G,help=X);O.add_argument(L,action=G,help=Y);O.add_argument(Z,default=F,action=G,help=a);R,P=O.parse_known_args();N=[]
	if R.user_interaction:N+=[L]
	N.extend(P);T=[b,c]
	for U in T:I=[A.path.join(B,U)for B in Q];D(I,N)
	I=[A.path.join(B,d,H,e)for B in[A.path.join(J,f)]+K];N=P+[g];D(I,N)
	if not R.skip_adodbapi:I=[A.path.join(B,M,H,h)for B in Q];D(I,P);I=[A.path.join(B,M,H,i)for B in Q];D(I,P)
	if E:
		B(j)
		for m in E:B(k,m)
		C.exit(1)
	B(l)
if __name__==m:P()
import os as A,site as I,subprocess as N,sys as C
J=A.path.dirname(__file__)
K=[I.getusersitepackages()]+I.getsitepackages()
E=[]
def O(script,cmdline_extras):
	D=script;H,I=A.path.split(D);J=[C.executable,R,I]+cmdline_extras;B(S%D);C.stdout.flush();G=N.run(J,check=F,cwd=H);B(T%(D,G.returncode));C.stdout.flush()
	if G.returncode:E.append(D)
def D(possible_locations,extras):
	B=possible_locations
	for C in B:
		if A.path.isfile(C):O(C,extras);break
	else:raise Q(U%B)
def P():
	import argparse as S;Q=[J]+K;O=S.ArgumentParser(description=V);O.add_argument(W,default=F,action=G,help=X);O.add_argument(L,action=G,help=Y);O.add_argument(Z,default=F,action=G,help=a);R,P=O.parse_known_args();N=[]
	if R.user_interaction:N+=[L]
	N.extend(P);T=[b,c]
	for U in T:I=[A.path.join(B,U)for B in Q];D(I,N)
	I=[A.path.join(B,d,H,e)for B in[A.path.join(J,f)]+K];N=P+[g];D(I,N)
	if not R.skip_adodbapi:I=[A.path.join(B,M,H,h)for B in Q];D(I,P);I=[A.path.join(B,M,H,i)for B in Q];D(I,P)
	if E:
		B(j)
		for m in E:B(k,m)
		C.exit(1)
	B(l)
if __name__==m:P()
import os as A,site as I,subprocess as N,sys as C
J=A.path.dirname(__file__)
K=[I.getusersitepackages()]+I.getsitepackages()
E=[]
def O(script,cmdline_extras):
	D=script;H,I=A.path.split(D);J=[C.executable,R,I]+cmdline_extras;B(S%D);C.stdout.flush();G=N.run(J,check=F,cwd=H);B(T%(D,G.returncode));C.stdout.flush()
	if G.returncode:E.append(D)
def D(possible_locations,extras):
	B=possible_locations
	for C in B:
		if A.path.isfile(C):O(C,extras);break
	else:raise Q(U%B)
def P():
	import argparse as S;Q=[J]+K;O=S.ArgumentParser(description=V);O.add_argument(W,default=F,action=G,help=X);O.add_argument(L,action=G,help=Y);O.add_argument(Z,default=F,action=G,help=a);R,P=O.parse_known_args();N=[]
	if R.user_interaction:N+=[L]
	N.extend(P);T=[b,c]
	for U in T:I=[A.path.join(B,U)for B in Q];D(I,N)
	I=[A.path.join(B,d,H,e)for B in[A.path.join(J,f)]+K];N=P+[g];D(I,N)
	if not R.skip_adodbapi:I=[A.path.join(B,M,H,h)for B in Q];D(I,P);I=[A.path.join(B,M,H,i)for B in Q];D(I,P)
	if E:
		B(j)
		for m in E:B(k,m)
		C.exit(1)
	B(l)
if __name__==m:P()
import os as A,site as I,subprocess as N,sys as C
J=A.path.dirname(__file__)
K=[I.getusersitepackages()]+I.getsitepackages()
E=[]
def O(script,cmdline_extras):
	D=script;H,I=A.path.split(D);J=[C.executable,R,I]+cmdline_extras;B(S%D);C.stdout.flush();G=N.run(J,check=F,cwd=H);B(T%(D,G.returncode));C.stdout.flush()
	if G.returncode:E.append(D)
def D(possible_locations,extras):
	B=possible_locations
	for C in B:
		if A.path.isfile(C):O(C,extras);break
	else:raise Q(U%B)
def P():
	import argparse as S;Q=[J]+K;O=S.ArgumentParser(description=V);O.add_argument(W,default=F,action=G,help=X);O.add_argument(L,action=G,help=Y);O.add_argument(Z,default=F,action=G,help=a);R,P=O.parse_known_args();N=[]
	if R.user_interaction:N+=[L]
	N.extend(P);T=[b,c]
	for U in T:I=[A.path.join(B,U)for B in Q];D(I,N)
	I=[A.path.join(B,d,H,e)for B in[A.path.join(J,f)]+K];N=P+[g];D(I,N)
	if not R.skip_adodbapi:I=[A.path.join(B,M,H,h)for B in Q];D(I,P);I=[A.path.join(B,M,H,i)for B in Q];D(I,P)
	if E:
		B(j)
		for m in E:B(k,m)
		C.exit(1)
	B(l)
if __name__==m:P()
import os as A,site as I,subprocess as N,sys as C
J=A.path.dirname(__file__)
K=[I.getusersitepackages()]+I.getsitepackages()
E=[]
def O(script,cmdline_extras):
	D=script;H,I=A.path.split(D);J=[C.executable,R,I]+cmdline_extras;B(S%D);C.stdout.flush();G=N.run(J,check=F,cwd=H);B(T%(D,G.returncode));C.stdout.flush()
	if G.returncode:E.append(D)
def D(possible_locations,extras):
	B=possible_locations
	for C in B:
		if A.path.isfile(C):O(C,extras);break
	else:raise Q(U%B)
def P():
	import argparse as S;Q=[J]+K;O=S.ArgumentParser(description=V);O.add_argument(W,default=F,action=G,help=X);O.add_argument(L,action=G,help=Y);O.add_argument(Z,default=F,action=G,help=a);R,P=O.parse_known_args();N=[]
	if R.user_interaction:N+=[L]
	N.extend(P);T=[b,c]
	for U in T:I=[A.path.join(B,U)for B in Q];D(I,N)
	I=[A.path.join(B,d,H,e)for B in[A.path.join(J,f)]+K];N=P+[g];D(I,N)
	if not R.skip_adodbapi:I=[A.path.join(B,M,H,h)for B in Q];D(I,P);I=[A.path.join(B,M,H,i)for B in Q];D(I,P)
	if E:
		B(j)
		for m in E:B(k,m)
		C.exit(1)
	B(l)
if __name__==m:P()
import os as A,site as I,subprocess as N,sys as C
J=A.path.dirname(__file__)
K=[I.getusersitepackages()]+I.getsitepackages()
E=[]
def O(script,cmdline_extras):
	D=script;H,I=A.path.split(D);J=[C.executable,R,I]+cmdline_extras;B(S%D);C.stdout.flush();G=N.run(J,check=F,cwd=H);B(T%(D,G.returncode));C.stdout.flush()
	if G.returncode:E.append(D)
def D(possible_locations,extras):
	B=possible_locations
	for C in B:
		if A.path.isfile(C):O(C,extras);break
	else:raise Q(U%B)
def P():
	import argparse as S;Q=[J]+K;O=S.ArgumentParser(description=V);O.add_argument(W,default=F,action=G,help=X);O.add_argument(L,action=G,help=Y);O.add_argument(Z,default=F,action=G,help=a);R,P=O.parse_known_args();N=[]
	if R.user_interaction:N+=[L]
	N.extend(P);T=[b,c]
	for U in T:I=[A.path.join(B,U)for B in Q];D(I,N)
	I=[A.path.join(B,d,H,e)for B in[A.path.join(J,f)]+K];N=P+[g];D(I,N)
	if not R.skip_adodbapi:I=[A.path.join(B,M,H,h)for B in Q];D(I,P);I=[A.path.join(B,M,H,i)for B in Q];D(I,P)
	if E:
		B(j)
		for m in E:B(k,m)
		C.exit(1)
	B(l)
if __name__==m:P()
