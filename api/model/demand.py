# -*- coding: utf-8 -*-
'''需求管理操作

@author: Gao Le
'''
from flask import jsonify
from .db import Demand, Activity
from .role import identity
from playhouse.shortcuts import JOIN


# @identity.check_permission("create", 'demand')
def create_demand(demand):
    '''新建需求'''

    return Demand.get_or_create(
        title=demand['title'],
        defaults={
            'detail': demand['detail'],
            'level': demand['level'],
            'projectId': demand['projectId']
        })


def demand_detail(demandId):
    '''获取需求详情'''
    return Demand.select(Demand, Activity.title.alias('activityTittle')).join(
        Activity,
        on=(Demand.activityId == Activity.id)).where(Demand.id == demandId).get()


# @identity.check_permission("update", 'demand')
def update_demands(demand):
    Demand.update(
        title=demand['title'],
        detail=demand['detail'],
        level=demand['level']
        ).where(Demand.id == demand['id']).execute()
    return Demand.getOne(Demand.id == demand['id'])


def find_one_demand_by_title(title):
    return Demand.getOne(Demand.title == title)
