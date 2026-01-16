def rotate_array(array, k):
    n = len(array)
    if n == 0:
        return []
    if k == 0:
        return array

    k = k % n

    result = [0] * n

    for i in range(n):
        new_index = (i + k) % n
        result[new_index] = array[i]

    return result

def max_area(height):
    """
    We're using 2 pointers here:
    - l = left, starting from the beginning of the array
    - r = right, starting from the end of the array
    - lv = left value, the height of the left wall
    - rv = right value, the height of the right wall
    Calculate area using the formula:
        min(lv, rv) * (r - l)
        - water should be contained inside the container so that
        the water level maximum height will be the lower wall --> min (lv, rv)
        - (r - l) = the side of the container
    """
    l = 0
    r = len(height) - 1
    area = 0
    
    while (l < r):
        lv = height[l]
        rv = height[r]
        temp_area = min(lv, rv) * (r - l)
        if (temp_area > area):
            area = temp_area
        
        if (lv >= rv):
            r -= 1
        else:
            l +=1

    return area