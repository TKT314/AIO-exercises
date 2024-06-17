import math
import random
#Bài 1: Viết function thực hiện đánh giá classification model bằng F1-Score.
def evaluate_classification(tp, fp, fn):
    # Kiểm tra kiểu dữ liệu đầu vào
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return

    # Kiểm tra giá trị đầu vào phải lớn hơn 0
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return

    # Tính toán Precision, Recall, và F1-Score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    # In kết quả
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1-score: {f1_score:.4f}')
#Bài 2. Viết function mô phỏng theo 3 activation function.
def is_number(n):
    try :
        float(n) # Type - casting the string to ‘float ‘.
                 # If string is not a valid ‘float ‘ ,
                 # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True
def calc_activation_func(x, activation_function):
    if is_number(x) == False:
        print('x must be a number')
        return
    x = float(x)
    if activation_function=='sigmoid':
            
        y = 1 / (1 + math.exp(-x))
    elif activation_function == 'relu':
        y=max(0,x)
    elif activation_function == 'elu':
        if x <= 0:
            alpha = 0.01
            y = alpha * (math.e**(x) - 1)
        elif x > 0:
            y = x
    else:
        print(f'{activation_function} is not supported')
        return
    print(y)
#Bài 3:Viết function lựa chọn regression loss function để tính loss
def calculate_loss(num_samples, loss_name):
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return

    num_samples = int(num_samples)
    loss = 0

    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        
        if loss_name.upper() == 'MAE':
            loss += abs(predict - target)
        elif loss_name.upper() == 'MSE':
            loss += (target - predict) ** 2
        elif loss_name.upper() == 'RMSE':
            loss += (target - predict) ** 2
        
        print(f'loss name: {loss_name}')
        print(f'sample: {i}')
        print(f'pred: {predict:.4f}')
        print(f'target: {target:.4f}')
        print(f'loss: {loss:.4f}')
    
    if loss_name.upper() == 'RMSE':
        final_loss = math.sqrt(loss / num_samples)
    else:
        final_loss = loss / num_samples
    
    print(f'final_loss: {final_loss:.4f}')
#Bài 4:Viết 4 functions để ước lượng các hàm số sau.
def factorial(n):
    if type(n) != int or n < 0:
        print('n is not valid')
        return None
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        result = 1
        for i in range(n):
            result *= (i +1)
        
        return result
def approximate_sin(x, n):
	result = 0
	for i in range(n + 1):
		result += ((-1)**i)*(x**(2*i+1))/factorial(2*i+1)
	print(f'sin: {result}')
	
	
def approximate_cos(x, n):
	result = 0
	for i in range(n + 1):
		result += ((-1)**i)*(x**(2*i))/factorial(2*i)
	print(f'cos: {result}')
	
	
def approximate_sinh(x, n):
	result = 0
	for i in range(n + 1):
		result += (x**(2*i+1))/factorial(2*i+1)
	print(f'sinh: {result}')
	
	
def approximate_cosh(x, n):
	result = 0
	for i in range(n + 1):
		result += (x**(2*i))/factorial(2*i)
	print(f'cosh: {result}')
# Bài 5. Viết function thực hiện Mean Difference of nth Root Error.
def MD_nRE(y, y_hat, n, p):
     
	loss = (y**(1 / n) - y_hat**(1 / n))**p
	print(loss)    





     

if __name__ == "__main__":
    # Thực nghiệm bài 1.
    evaluate_classification(tp = 3, fp = 1 ,fn = 4)

    # Thực nghiệm bài 2:.
    calc_activation_func(4, 'belu')

    #Thực nghiệm bài 3:
    n_sample = input('number of samples : ')
    loss_name = input('loss name: ')
    calculate_loss(n_sample, loss_name)

    #Thực nghiệm bài 4:
    approximate_sin(3.14, 5)
    approximate_cos(3.14, 5)
    approximate_sinh(3.14, 5)
    approximate_cosh(3.14, 5)
	
    #Thực nghiệm bài 5:
    MD_nRE(50, 49.5, 2, 1)
    



