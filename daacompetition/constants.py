__author__ = 'kaloyan'
from enum import Enum


class Register(Enum):
    ALL_FIELDS_REQ = 'VSICHKI POLETA SA ZADALJITELNI'
    PASSWORDS_NOT_MATCH = 'PAROLITE NE SAVPADAT'
    ALLOWED_CHARACTERS = 'USERNAME-a moje da sadarja samo slednite: _ [0-9] [a-z] [A-Z]'
    USERNAME_EXISTS = 'IMA VECHE TAKAV POTREBITEl'


class Login(Enum):
    LOGIN_FAILED = 'Failed login'


class SubmtiTask(Enum):
    EMPTY_SOLUTION = 'PRAZNO RESHENIE'
    TIME_EXPIRES = 'MINA VREMETO ZA PREDAVENE'
    MISCHIEVOUS_CODE = 'MISCHIEVOUS PIECE OF CODE^^'
