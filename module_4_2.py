def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

    
# При вызове inner_function() вне test_function() будет ошибка,
# т.к. inner_function() не находится в объемлющей области видимости функции test_function
