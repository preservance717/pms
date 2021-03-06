# -*- coding: utf-8 -*-
'''用户管理操作

@author: Wang Jianhui
'''

from .db import User, UserBase


def findOneById(userid):
    '''按 id 查询用户'''
    return User.sget(User.id == userid)


def findOneByName(username):
    '''按 username 查询用户'''
    return User.sget(User.username == username)


def findOneByEmail(email):
    '''按 email 查询用户'''
    return User.sget(User.email == email)


def save(user):
    '''添加用户并返回用户信息'''
    return UserBase.create(
        username=user['username'],
        email=user['email'],
        password=user['password'])


def update(user):
    '''更新用户信息'''
    User.update(
        username=user['username'],
        email=user['email']).where(User.id == user['id']).execute()


def change_password(userid, password):
    '''更新用户密码'''
    User.update(password=password).where(User.id == userid).execute()
