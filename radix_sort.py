import sys


def radix_sort(array):
    x = 1  
    
    
    while x <= 10000:
        bins = [[] for place in range(10)] 
        
        for num in array:
            digit = (num // x) % 10  
            bins[digit].append(num)  
       
        array = []  
        for bin in bins:
            for num in bin:
                array.append(num)  

        x *= 10  
        
        all_done = True
        for num in array:
            if num // x > 0: 
                all_done = False
                break

        if all_done:
            break

    return array



if __name__ == "__main__":

    if len(sys.argv) > 1:
        
        numbers = []

        
        for num in sys.argv[1:]:
            numbers.append(int(num))  

        
        sorted_numbers = radix_sort(numbers)

        
        result = ""
        for num in sorted_numbers:
            result += str(num) + " "  
        print(result.strip())  
    else:
        print("Please provide a list of numbers to sort.")

