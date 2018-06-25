temp = 30
l23 = 10
q23 = 1.33
u12 = 6
theta = 0
r = 1
rugosidade = 0
d23i = 0.7
u23i = 5
trecho = 1

densidade = 101303 /(286.9 *(temp + 273.15));
visc_dinam = ((13 + 0.1 * temp) * 1e-6) * densidade;

d23, u23 = fsolve(residuals, [d23i, u23i])
if(Trecho == 1){
    dP = (densidade*f*l23*u23**2/(d23*2));
}
a = (Math.PI*d23**2)/4;