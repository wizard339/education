def make_averager():
    series = [] # свободная переменная
    
    def averager(new_value):
        # замыкание averager расширяет область видимости функции, включая в нее привязку свободной переменной series
        series.append(new_value) 
        total = sum(series)
        return total/len(series)
    
    return averager
    
    
if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
