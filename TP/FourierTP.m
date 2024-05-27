% Fermeture de toutes les figures, netoyage des variables
clear;
close;

% à compléter : Creation de l'image de synthese
img=atom();
%[img,map,alpha]=imread("Water0000GP.png");
%img = rgb2gray (img);

% Afficher l'image de synthese
affiche_image(img);

% à compléter : transform fourier 2d
fe=1;
fourier2d(img,fe);
