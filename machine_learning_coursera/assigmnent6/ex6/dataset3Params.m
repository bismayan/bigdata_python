function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C_try= [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
sigma_try=[0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
sig_len=length(sigma_try);
C_len=length(C_try);
% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%

%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))

%
min_err=-999
for i=1:C_len
	for j=1:sig_len
	model= svmTrain(X, y, C_try(i), @(x1, x2) gaussianKernel(x1, x2, sigma_try(j))); 
	predictions=svmPredict(model,Xval);
	err=mean(double(predictions ~= yval));
	if (min_err==-999)
		min_err=err;
		C=C_try(i);sigma=sigma_try(j);
	elseif (err<min_err) 
		min_err=err;
		C=C_try(i);sigma=sigma_try(j);
	endif
end


	





% =========================================================================

end
