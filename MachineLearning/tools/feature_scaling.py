### FYI the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why ould you rescale it? or even use it at all?

def featureScaling(arr):
    lb = min(arr)
    ub = max(arr)
    x = float(ub-lb)
    if x==0:
        return "Error: Max and min values are the same. No need to rescale"
    else:
        arr_scaled = []
        for i in arr:
            arr_scaled.append((i - lb)/x)
        return arr_scaled
    
# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)


