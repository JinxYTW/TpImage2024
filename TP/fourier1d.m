function []=fourier1d(f,fe);

f = abs(fftshift(fft(f,-1)));
n=length(f)/2;
figure();
clf
plot((fe/2)*(-n:n-1)/n,f);

endfunction
