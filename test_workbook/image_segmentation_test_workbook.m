%%
% Load image to segment
img = imread('data/DJI_0486.JPG');
img = im2double(img);

%%
% Segment image based on RGB values
r = img(:, :, 1);
g = img(:, :, 2);
b = img(:, :, 3);

segmented_image = r > 0.6;
compare_original_and_segmented_image(2, img, segmented_image);
