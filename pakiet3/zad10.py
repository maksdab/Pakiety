def cumulative_sum(input_list):
    cum_sum = []
    total = 0
    for num in input_list:
        total += num
        cum_sum.append(total)
    return cum_sum

input_list = [1, 2, 3, 4, 5]
print(cumulative_sum(input_list))
