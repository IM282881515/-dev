#!/usr/bin/env python
# coding: utf-8
import web
 


render = web.template.render('templates')

web.config.debug = True

config = web.storage(
    site_name = '任务跟踪',
    site_desc = '一个基础练手项目',
    static = '/static',
)

#config可以在没模板系统中使用 将模板内需要访问的变量以map形式赋值给模板类中的globals
web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render 




