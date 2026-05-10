"""
File: dogworld.py
-----------------
Provides an example of using the Dog class.
"""

from dog import Dog


def main():
    simba = Dog('pomeranian')
    juno = Dog('great dane')

    simba.bark()
    juno.bark()
    simba.bark()

    print('simba', simba.__dict__)
    print('juno',  juno.__dict__)


if __name__ == '__main__':
    main()
