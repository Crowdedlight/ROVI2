clear all;
clc;
clear;

% parameters
Ra = 1.9; %winding resistance
L = 0.003; %winding inductance
lambda = 0.1; %motor constant
J = 0.00018; %moment of inertia
B = 0.001; %Coefficient of viscous friction

ControlNoise = 0.01; % std dev of uncertainty in control inputs
MeasNoise = 0.1; %standard deviation of measurement noise
R            = [MeasNoise^2 0; 0 MeasNoise^2]; % measurement noise covariance
xdotNoise    = [ControlNoise/L ControlNoise/L 0.5 0];
Q            = [xdotNoise(1)^2 0 0 0 ; 0 xdotNoise(2)^2 0 0; 0 0 xdotNoise(3)^2 0; 0 0 0 xdotNoise(4)^2];
P            = 1*eye(4); % initial state estimation covariance

dt = 0.0005; % integration step size
tf = 1.5; % simulation length

% Initialization
x    = [0; 0; 0; 0];
xhat = x; 

dtPlot  = 0.01;
tPlot   = -inf;

% Initialize arrays for plotting at the end of the program
xArray    = [];
xhatArray = [];
tArray    = [];


for t = 0 : dt : tf
    if t >= tPlot + dtPlot
        % Save data for plotting
        tPlot     = t + dtPlot - eps;
        xArray    = [xArray x];
        xhatArray = [xhatArray xhat];
        tArray    = [tArray t];
    end
    
    %calculate A matrix
    A = [
        -R/L 0 (lambda*sin(x(4)))/L (x(3)*lambda*cos(x(4)))/L;
        0 -R/L (-lambda*cos(x(4)))/L (x(3)*lambda*sin(x(4)))/L;
        (-3*lambda*sin(x(4)))/2/J (-3*lambda*cos(x(4)))/2/J -F/J (-3*lambda*(x(1)*cos(x(4))+x(2)*sin(x(4))))/2/J ;
        0 0 1 0
    ];
    
    % Simulation
    ua0 = sin(w*t);
    ub0 = cos(w*t);
    
    xdot = A*x;
    
    x    = x + xdot * dt + [xdotNoise(1)*randn; xdotNoise(2)*randn; xdotNoise(3)*randn; xdotNoise(4)*randn] * dt;
    
    % Kalman filter
    
    
    xhatdot = A*xhat;
    K       = P * C' / R;
    xhatdot = xhatdot + K * (y - C * xhat);
    xhat    = xhat + xhatdot * dt;
    Pdot    = A * P + P * A' + Q - P * C' / R * C * P;
    P       = P + Pdot * dt;
end

% Plot data.
close all;
figure; set(gcf,'Color','White');
 
subplot(2,1,1); hold on; box on;
plot(tArray, xArray(1,:), 'b-', 'LineWidth', 2);
plot(tArray, xhatArray(1,:), 'r:', 'LineWidth', 2)
set(gca,'FontSize',12); 
ylabel('Current A (Amps)');
 
subplot(2,1,2); hold on; box on;
plot(tArray, xArray(2,:), 'b-', 'LineWidth', 2);
plot(tArray, xhatArray(2,:), 'r:', 'LineWidth', 2)
set(gca,'FontSize',12); 
ylabel('Current B (Amps)');
