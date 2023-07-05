'''This is for a test that simulates a $-based or ohter-based substitute'''
import re

__all__ = ['Template']


class Template:
    judge_char = '$'
    idpattern = '\w+'

    def __init__(self, string):
        self.__string = string
        self.__processing_identifier()

    def __processing_identifier(self):
        self.identifier = re.findall(
            f'\{self.judge_char}({self.idpattern})', self.__string)

    def substitute(self, mapping, **kwargs):
        if type(mapping) != dict:
            raise ValueError(
                f'parameter mapping should be a <dict> not a {type(mapping)}')
        mapping.update(kwargs)

        for name in mapping:
            if name in self.identifier:
                self.__string = re.sub(
                    f'\{self.judge_char}{name}', str(mapping[name]), self.__string)
                self.identifier.remove(name)

        if self.identifier:
            raise KeyError(f'The key: {", ".join(self.identifier)} is missing')

    @property
    def pattern(self):
        return self.idpattern

    @pattern.setter
    def pattern(self, new_pattern):
        self.idpattern = new_pattern

    def __str__(self):
        return self.__string

    def __repr__(self):
        return f'<{self.__class__.__name__} object>: {self.__string}'


if __name__ == '__main__':
    test = Template(
        'I got a book: $bookname and I paid $money buy it')

    test.substitute({'bookname': 'The Art of War'}, money='$3.99')
    print(test)
