pub fn nth(n: u32) -> u32 {
    let mut counter = 0;
    let mut prime = 0;

    loop {
        if is_prime(prime) {
            if counter == n {
            	return prime
            }
            counter += 1
        }
        prime += 1;
    }
}

pub fn is_prime(n: u32) -> bool {
    if n <= 3 {
        return n > 1;
    } else if n % 2 == 0 || n % 3 == 0 {
        return false;
    }
    let mut i: u32 = 5;

    while i.pow(2) <= n {
        if n % i == 0 || n % (i + 2) == 0 {
            return false;
        }
        i += 6;
    }
    true
}
