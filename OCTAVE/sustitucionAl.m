function sustitucionAl
  A=[4	-1	0	0	0	-1	0	0	0	0	0	0	0	0	0	0	0	0	0	0; -1	4	-1	0	0	0	-1	0	0	0	0	0	0	0	0	0	0	0	0	0;0	-1	4	-1	0	0	0	-1	0	0	0	0	0	0	0	0	0	0	0	0;0	0	-1	4	-1	0	0	0	-1	0	0	0	0	0	0	0	0	0	0	0;0	0	0	-1	4	0	0	0	0	-1	0	0	0	0	0	0	0	0	0	0;-1	0	0	0	0	4	-1	0	0	0	-1	0	0	0	0	0	0	0	0	0;0	-1	0	0	0	-1	4	-1	0	0	0	-1	0	0	0	0	0	0	0	0;0	0	-1	0	0	0	-1	4	-1	0	0	0	-1	0	0	0	0	0	0	0;0	0	0	-1	0	0	0	-1	4	-1	0	0	0	-1	0	0	0	0	0	0;0	0	0	0	-1	0	0	0	-1	4	0	0	0	0	-1	0	0	0	0	0;0	0	0	0	0	-1	0	0	0	0	4	-1	0	0	0	-1	0	0	0	0;0	0	0	0	0	0	-1	0	0	0	-1	4	-1	0	0	0	-1	0	0	0;0	0	0	0	0	0	0	-1	0	0	0	-1	4	-1	0	0	0	-1	0	0;0	0	0	0	0	0	0	0	-1	0	0	0	-1	4	-1	0	0	0	-1	0;0	0	0	0	0	0	0	0	0	-1	0	0	0	-1	4	0	0	0	0	-1;0	0	0	0	0	0	0	0	0	0	-1	0	0	0	0	4	-1	0	0	0;0	0	0	0	0	0	0	0	0	0	0	-1	0	0	0	-1	4	-1	0	0;0	0	0	0	0	0	0	0	0	0	0	0	-1	0	0	0	-1	4	-1	0;0	0	0	0	0	0	0	0	0	0	0	0	0	-1	0	0	0	-1	4	-1;0	0	0	0	0	0	0	0	0	0	0	0	0	0	-1	0	0	0	-1	4]
  B=[100 80 80 80 380 20 0 0 0 300 20 0 0 0 300 20 0 0 0 300]
  B=B'
  n=length(A);
  x(n)=B(n)/A(n,n);
  for i=n-1:-1:1
    s=1;
    for j=(i+1):n
      s=s+A(i,j)*x(j);
    endfor
    x(i)=(B(i)-s)/A(j,j);
    disp(x);
    n=0;
  endfor
endfunction