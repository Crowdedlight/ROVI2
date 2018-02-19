function compare_original_and_segmented_image( figure_number, original_image, segmented_image )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

figure(figure_number);
sp1 = subplot(1, 2, 1);
image(original_image);
axis image;
sp2 = subplot(1, 2, 2);
imagesc(segmented_image);
axis image;
linkaxes([sp1, sp2]);

end

