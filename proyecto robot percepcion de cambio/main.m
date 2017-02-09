clear ; close all; clc
Pasado = double(imread('pasado.jpg'));
Presente= double(imread('presente.jpg'));
Pasado=Pasado/255;
Presente = Presente / 255; % necesario para mostrar imageen
variacion= Presente-Pasado;
imwrite(variacion, "variacion.jpg"); 
fprintf('Program paused. Press enter to continue.\n');
pause;
#%voy a crear una imagen de fondo, luego le sobrepongo un cuadrado al azar
# dentro de la imagen, la computadora tiene que darme una cordenada X
# y luego sobreponer un cuadro con la cordenada que dio la computadora
#y verificar si se encuentra el cuadrado dentro de ella.
% a la vez correr otro programa donde el programa aprenda a identificar 
%el cuadrado, tomando el cuadro, y las distancias para arriba y abajo para
% crear ejemplos negativos, podria usar un algoritmo de anomalias,
%correrlo 1000 veces y asi el mismo programa se va creando sus propios e
%ejemplos, y puliendo asi mismo

%NOTA: ahoi que ponerle castigo si la cordenada supera el tamaño de la foto 
