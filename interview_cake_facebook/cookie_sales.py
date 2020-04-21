def combine_sales (sales_1,sales_2):
    combined_sales = []
    total_orders = len(sales_1) + len(sales_2)
    while len(combined_sales) <= total_orders:
        if len(sales_1) == 0:
            for sale in sales_2:
                combined_sales.append(sale)
            break
        elif len(sales_2) == 0:
            for sale in sales_1:
                combined_sales.append(sale)
            break
        else:
            s1 = sales_1[0]
            s2 = sales_2[0]
            if s1 > s2:
                combined_sales.append(sales_2.pop(0))
            else:
                combined_sales.append(sales_1.pop(0))
    return combined_sales

# Tests
test_1 = combine_sales([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
test_2 = combine_sales([3, 10, 11, 15], [1, 5, 8, 12, 14, 19]) == [1, 3, 5, 8, 10, 11, 12, 14, 15, 19]
test_3 = combine_sales([3, 4, 6, 10, 11, 15], [ 5, 8, 12, 19]) == [3, 5, 8, 10, 11, 12, 15, 19]

if not test_1 and not test_2 and not test_3:
    print("Fail")
else:
    print("All tests passing!!")
# Time/Space Complexity: O(n)
