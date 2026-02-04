import time

def dec_times_backoff(times, backoff_time):
    def dec_backoff(func):
        def wrapper(*args, **kwargs):
            
            backoff = backoff_time
            raise_error = times

            for t in range(0, times+1):
                try:
                    ans = func(*args, **kwargs)
                    
                    if(raise_error):
                        raise_error -= 1
                        raise RuntimeError("Some error occures")
                    
                except Exception as err:
                    print("error occured", err)
                    print("Retrying.....")
                    time.sleep(backoff)
                    backoff **= (t+1)
                    # backoff_time = backoff_time**(t+2)

                else:
                    return ans
                
        return wrapper
    return dec_backoff



@dec_times_backoff(3, 2)
def add(a,b):
    return a+b

print(add(2,3))

