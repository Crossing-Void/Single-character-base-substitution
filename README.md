# char-based simulates

## Preface

This is a simulation of template string in python built-in modules `string.py`

# Modules

## template_string

> This modules only contain a class `Template`,
> <span class="sa">class</span> Template(string)  
> > **judge_char**: use this variable to control which to be treated to a pattern later will be substituted default is '$'
> > **idpattern**: a regular expression, default \w+, so a identifier is `f"\{self.judge_char}({self.idpattern})"`
> > **identifier**: a list contain all identifiers
> > **substitute(self, mapping, kwargs)**: use this funtion to change the value, example:  
```python
test = Template(
        'I got a book: $bookname and I paid $money buy it.')
    
    test.substitute({'bookname': 'The Art of War'}, money='$3.99')
    print(test)
``` 
