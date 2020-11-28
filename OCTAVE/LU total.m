function total();
    disp('Para este metodo usaremos eliminación Gaussiana sin pivoteo.');
    disp("");
    %Gauss sin pivoteo 
    A=[4	-1	0	0	0	-1	0	0	0	0	0	0	0	0	0	0	0	0	0	0; -1	4	-1	0	0	0	-1	0	0	0	0	0	0	0	0	0	0	0	0	0;0	-1	4	-1	0	0	0	-1	0	0	0	0	0	0	0	0	0	0	0	0;0	0	-1	4	-1	0	0	0	-1	0	0	0	0	0	0	0	0	0	0	0;0	0	0	-1	4	0	0	0	0	-1	0	0	0	0	0	0	0	0	0	0;-1	0	0	0	0	4	-1	0	0	0	-1	0	0	0	0	0	0	0	0	0;0	-1	0	0	0	-1	4	-1	0	0	0	-1	0	0	0	0	0	0	0	0;0	0	-1	0	0	0	-1	4	-1	0	0	0	-1	0	0	0	0	0	0	0;0	0	0	-1	0	0	0	-1	4	-1	0	0	0	-1	0	0	0	0	0	0;0	0	0	0	-1	0	0	0	-1	4	0	0	0	0	-1	0	0	0	0	0;0	0	0	0	0	-1	0	0	0	0	4	-1	0	0	0	-1	0	0	0	0;0	0	0	0	0	0	-1	0	0	0	-1	4	-1	0	0	0	-1	0	0	0;0	0	0	0	0	0	0	-1	0	0	0	-1	4	-1	0	0	0	-1	0	0;0	0	0	0	0	0	0	0	-1	0	0	0	-1	4	-1	0	0	0	-1	0;0	0	0	0	0	0	0	0	0	-1	0	0	0	-1	4	0	0	0	0	-1;0	0	0	0	0	0	0	0	0	0	-1	0	0	0	0	4	-1	0	0	0;0	0	0	0	0	0	0	0	0	0	0	-1	0	0	0	-1	4	-1	0	0;0	0	0	0	0	0	0	0	0	0	0	0	-1	0	0	0	-1	4	-1	0;0	0	0	0	0	0	0	0	0	0	0	0	0	-1	0	0	0	-1	4	-1;0	0	0	0	0	0	0	0	0	0	0	0	0	0	-1	0	0	0	-1	4]

    n=size(A);
    B=eye(n);
    for k=1:n-1,                  
        for i=k+1:n,
          for j=k+1:n,   
            m = A(i,k)/A(k,k);
            %Hallamos L que en este caso seria B
            B(i,k)=m;
            %Hallamos U que en este caso seria A
            A(i,j) = A(i,j) - m*A(k,j);
          endfor
          A(i,k)=0;
        endfor    
    endfor
    disp("La matriz L que es una matriz triangular inferior es:");
    disp(B);
    disp("");
    disp("La matriz U que es una matriz escalonada es: ");
    disp(A);
    
  
    %Sabiendo que ahora A=LU
    %Entonces Ax=b va a ser LUx=b 
    %Nosotros pondremos Ux=y y Ly=b y con eso trabajaremos y hallaremos las x.   
    x=[100 80 80 80 380 20 0 0 0 300 20 0 0 0 300 20 0 0 0 300]
    n=length(B);
    r(1)=x(1)/B(1,1);
    %En este proceso hallaremos las variables que primero serian las y
    %usando los metodos ya vistos de sustitucion
    for i=2:n,
      s=0;
    for j=1:i-1,
      s=s+r(j)*B(i,j);
    end
    r(i)=(x(i)-s)/B(i,i);
    endfor
    disp('Resolviendo el sistema Ly = b,hallamos las y que son:');
    disp(r);
    disp("");
    disp('Con las y halladas podemos hallar las x que es lo que nos pide.');
    disp("");
    
    %En este proceso hallaremos las variables que primero serian las x
    %usando los metodos ya vistos de sustitucion
    n=length(A);
    t(n)=r(n)/A(n,n);
    for i=n-1:-1:1
      s=0;
    for j=(i+1):n
      s=s+A(i,j)*t(j);
    endfor
    t(i)=(r(i)-s)/A(i,i);
  endfor
  disp('Ahora resolviendo el sistema Ux=y:, hallamos las x que son: ');
  disp(t);
  disp("");
  disp('Con eso tendriamos resuelto el sistema');
  %Con eso hemos hayado la respuesta al sistema Ax=b solo que A
  %vendria a ser ahora LU
  
endfunction
