def variance_of_portfolio(w1, w2, sigma1, sigma2, correlation):
    a = (w1 * sigma1) ** 2
    b = (w2 * sigma2) ** 2
    c = 2 * w1 * w2 * correlation * sigma1 * sigma2
    variance = a + b + c
    return variance


def find_minimum_variance_portfolio(E1, E2, sigma1, sigma2, correlation):
    minimum_variance, minimum_w1 = variance_of_portfolio(0, 1, sigma1, sigma2, correlation), 0
    decimal_place = 5
    for i in range(0, 10 ** decimal_place, 1):
        w1 = (i + 1) / 10 ** decimal_place
        w2 = 1 - w1
        iteration_variance = variance_of_portfolio(w1, w2, sigma1, sigma2, correlation)
        if iteration_variance < minimum_variance:
            minimum_variance = iteration_variance
            minimum_w1 = w1
    
    expected_return_minimum_variance = minimum_w1 * E1 + (1 - minimum_w1) * E2
    minimum_standard_deviation = minimum_variance ** (1/2)
    difference = E1 - E2
    
    w_2_coefficient = (sigma1 ** 2) - (2 * sigma1 * sigma2 * correlation) + (sigma2 ** 2)
    w_1_coefficient = 2 * sigma1 * sigma2 * correlation - 2 * sigma2 ** 2
    w_0_coefficient = sigma2 ** 2
    
    sigma_coefficient_2 = (w_2_coefficient) / (difference ** 2)
    sigma_coefficient_1 = (w_1_coefficient / difference) - ((2 * w_2_coefficient * E2) / (difference ** 2))
    sigma_coefficient_0 = ((w_2_coefficient * E2 ** 2) / (difference ** 2)) - ((w_1_coefficient * E2) / difference) + w_0_coefficient
    
    minimum_variance_portfolio = {'expected return': expected_return_minimum_variance,
                                  'variance': minimum_variance,
                                  'standard variance': minimum_standard_deviation,
                                  'weight 1': minimum_w1,
                                  'weight 2': 1 - minimum_w1,
                                  'variance coefficients': [w_0_coefficient, w_1_coefficient, w_2_coefficient],
                                  'frontier coefficients': [sigma_coefficient_0, sigma_coefficient_1, sigma_coefficient_2]}
    
    return minimum_variance_portfolio


def find_tangent_portfolio(E1, E2, sigma1, sigma2, correlation, rf):
    a1 = (sigma1 ** 2) + (sigma2 ** 2) - (2 * sigma1 * sigma2 * correlation)
    b1 = (2 * sigma1 * sigma2 * correlation) - (2 * sigma2 ** 2)
    c1 = sigma2 ** 2
    difference = E1 - E2
    
    a2 = a1 / difference ** 2
    b2 = (b1 / difference) - (2 * E2 * a1 / difference ** 2)
    c2 = c1 + (E2 ** 2 * a1 / difference ** 2) - (E2 * b1 / difference)
    
    numerator = (4 * b2 * rf) + (4 * c2) + (4 * a2 * rf ** 2)
    denominator = (b2 ** 2) - (4 * a2 * c2)
    slope_squared = - numerator / denominator
    
    a3 = a2 * slope_squared - 1
    b3 = b2 * slope_squared + 2 * rf
    c3 = c2 * slope_squared - rf ** 2  # not used further
    slope = slope_squared ** (1/2)
    
    expected_return_of_tangent_portfolio = - b3 / (2 * a3)
    sigma_of_tangent_portfolio = (expected_return_of_tangent_portfolio - rf) / slope
    standard_deviation_of_tangent_portfolio = sigma_of_tangent_portfolio ** (1/2)
    weight_1 = (expected_return_of_tangent_portfolio - E2) / (E1 - E2)
    weight_2 = 1 - weight_1
    
    tangent_portfolio = {'expected return': expected_return_of_tangent_portfolio,
                         'variance': sigma_of_tangent_portfolio,
                         'standard variance': standard_deviation_of_tangent_portfolio,
                         'weight 1': weight_1,
                         'weight 2': weight_2,
                         'slope': slope}
    
    return tangent_portfolio


def sign(number):
    if number >= 0:
        return "+"
    else:
        return "-"


expected_return_1 = 0.1
expected_return_2 = 0.08
sigma_1 = 0.2
sigma_2 = 0.15
correlation = 0.25
risk_free = 0.05

minimum_variance_portfolio = find_minimum_variance_portfolio(expected_return_1, expected_return_2, sigma_1, sigma_2, correlation)
tangent_portfolio = find_tangent_portfolio(expected_return_1, expected_return_2, sigma_1, sigma_2, correlation, risk_free)

print("INPUT DATA")
print(f"E(R₁) = {expected_return_1:.5f} | Expected return of asset №1")
print(f"E(R₂) = {expected_return_2:.5f} | Expected return of asset №2")
print(f" σ₁   = {sigma_1:.5f} | Variance of asset №1")
print(f" σ₂   = {sigma_2:.5f} | Variance of asset №2")
print(f" ρ₁₂  = {correlation:.5f} | Correlation of asset №1 & №2")
print(f" Rf   = {risk_free:.5f} | Risk-free rate")
print()
print()
print(f"MINIMUM VARIANCE PORTFOLIO")
print(f"E(R) = {minimum_variance_portfolio['expected return']:.5f} | Expected return of minimum variance portfolio")
print(f" σ²  = {minimum_variance_portfolio['variance']:.5f} | Variance of minimum variance portfolio ")
print(f" σ   = {minimum_variance_portfolio['standard variance']:.5f} | Standard deviation of minimum variance portfolio")
print(f" W₁  = {minimum_variance_portfolio['weight 1']:.5f} | Weight of asset №1 in minimum variance portfolio")
print(f" W₂  = {minimum_variance_portfolio['weight 2']:.5f} | Weight of asset №2 in minimum variance portfolio")
print()
print()
print(f"TANGENT PORTFOLIO")
print(f"E(R) = {tangent_portfolio['expected return']:.5f} | Expected return of tangent portfolio")
print(f" σ²  = {tangent_portfolio['variance']:.5f} | Variance of tangent portfolio ")
print(f" σ   = {tangent_portfolio['standard variance']:.5f} | Standard deviation of tangent portfolio")
print(f" W₁  = {tangent_portfolio['weight 1']:.5f} | Weight of asset №1 in tangent portfolio")
print(f" W₂  = {tangent_portfolio['weight 2']:.5f} | Weight of asset №2 in tangent portfolio")
print()
print()
print("CML & SML")
print(f"E(R) = {risk_free:.5f} + {tangent_portfolio['slope']:.5f} * σ | Capital Market Line")
print(f"E(R) = {risk_free:.5f} + {tangent_portfolio['expected return'] - risk_free:.5f} * β | Theoretical Security Market Line")
print(f"E(R) = {risk_free * 0.67 + 0.33:.5f} + {0.67 * (tangent_portfolio['expected return'] - risk_free):.5f} * β | Actual Security Market Line")
print()
print()
print("EFFICIENCY FRONTIER")
print(f"E(R) = {expected_return_2:.5f} {sign(expected_return_1 - expected_return_2)} {abs(expected_return_1 - expected_return_2):.5f} * w1")
print(f"σ(R) = {minimum_variance_portfolio['variance coefficients'][2]:.5f} * w₁² {sign(minimum_variance_portfolio['variance coefficients'][1])} {abs(minimum_variance_portfolio['variance coefficients'][1]):.5f} * w₁ {sign(minimum_variance_portfolio['variance coefficients'][0])} {abs(minimum_variance_portfolio['variance coefficients'][0]):.5f}")
print(f"σ(R) = {minimum_variance_portfolio['frontier coefficients'][2]:.5f} * E(R)² {sign(minimum_variance_portfolio['frontier coefficients'][1])} {abs(minimum_variance_portfolio['frontier coefficients'][1]):.5f} * E(R) {sign(minimum_variance_portfolio['frontier coefficients'][0])} {abs(minimum_variance_portfolio['frontier coefficients'][0]):.5f}")
