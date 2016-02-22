filename = 'data2.xlsx';            %reading the file
h = xlsread(filename,'A:A');        %reading height, weight and age of training data
w = xlsread(filename,'B:B');
a = xlsread(filename,'C:C');
x = [h w a];
y = xlsread(filename,'D:D');

m = length(y);
x0=ones(m,1);       %adding first column of on
x = [x0,x];

theta = zeros(size(x(1,:)))'; %taking theta values zero and transposing
disp(theta)
MAX = 2000;           %number of iterations
alpha = 0.000001;

for n =1:MAX
    %calculating sigmoid function
    hyp=x*theta;
    g = 1 ./(1+exp(-hyp));
    
    %calculating theta using stochastic gradient descent
    for i = 1:m
        p = (y(i)-g(i))*x(i,:)';
        theta = theta + ((alpha) * p);
    end
    
    disp('Iteration')
    disp(n)
    disp('Theta Vector')
    disp(theta)
    %checking cost to keep track of right direction
    cost = (-1/m) * sum( y .* log(g) + (1 - y) .* log(1 - g) );
    disp('cost')
    disp(cost)
end
disp('Final')
disp(theta)
disp(cost)

% predict for Test Data, if sigmoid function > 0.5, then it belong to class 1(Man) else (W) 
predict1 = [1, 162, 53, 28] *theta;
g1 = 1 ./(1+exp(-predict1));
predict2 = [1, 168, 75, 32] * theta;
g2 = 1 ./(1+exp(-predict2));
predict3 = [1, 175, 70, 30] *theta;
g3 = 1 ./(1+exp(-predict3));
predict4 = [1, 180, 85, 29] * theta;
g4 = 1 ./(1+exp(-predict4));
disp(g1)
disp(g2)
disp(g3)
disp(g4)



