def get_palindrome_products(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("Max is lower than min")
    product_list = []
    max_factor = max_factor+1
    for i in range(min_factor, max_factor):
        for j in range(min_factor, max_factor):
            product = i * j
            factors = [i, j]
            if str(product) == str(product)[::-1]:
                product_list.append((product, factors))
    return product_list


def largest(min_factor, max_factor):
    palindrome_products = get_palindrome_products(min_factor, max_factor)
    if len(palindrome_products) == 0:
        return None, []
    else:
        value = max(palindrome_products, key=lambda x: x[0])[0]
        factors = []
        for product in palindrome_products:
            if product[0] == value:
                factors.append(product[1])
        return value, factors


def smallest(min_factor, max_factor):
    palindrome_products = get_palindrome_products(min_factor, max_factor)
    if len(palindrome_products) == 0:
        return None, []
    else:
        value = min(palindrome_products, key = lambda x: x[0])[0]
        factors = []
        for product in palindrome_products:
            if product[0] == value:
                factors.append(product[1])
        return value, factors


