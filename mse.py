
def mse(
    p_real_values,
    p_predicted_value
):
    b_check =\
        len(p_real_values) == len(p_predicted_value)
 
    if b_check:
        the_sum = 0
        for idx in range(len(p_real_values)):
            r = p_real_values[idx]
            p = p_predicted_value[idx]
            diff = r-p
            diff_squared = diff**2
            the_sum += diff_squared
        # for
        return the_sum / len(p_real_values)
    else:
        return "Inconsistent data"
    # if-else
# def mse
 
feature1 = [10, 20, 30]
predictions1 = [11, 19, 33]
mse_for_f1 = mse(feature1, predictions1)
print(mse_for_f1)
 
#------------------------------------------
 
import numpy as np
 
def mse_vnp(p_r, p_p):
    b_check = len(p_r) == len(p_p)
    if b_check:
        p_r = np.array(p_r)
        p_p = np.array(p_p)
        diff = p_r - p_p # broadcasting
        diff_squared = diff**2
        the_sum:np.array = diff_squared.sum()
        return the_sum / len(p_r)
    # if
    else:
        return "Inconsistent data"
    # if
# def mse_vnp
 
feature1 = [10, 20, 30]
predictions1 = [11, 19, 33]
mse_for_f1 = mse_vnp(feature1, predictions1)
print(mse_for_f1)