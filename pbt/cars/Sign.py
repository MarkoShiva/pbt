# -*- coding: utf-8 -*-

from os import getenv, getuid

from pbt.core import Car


class SignCar(Car):
    default_root_bg = getenv('PBT_CAR_BG', 'default')
    default_root_fg = getenv('PBT_CAR_FG', 'default')
    default_root_fm = getenv('PBT_CAR_FM', 'none')
    default_symbol_bg = default_root_bg
    default_symbol_fg = default_root_fg
    default_symbol_fm = 'bold'
    default_user_bg = default_root_bg
    default_user_fm = default_symbol_fm
    default_admin_bg = default_root_bg
    default_admin_fm = default_symbol_fm

    model = {
        'root': {
            'bg': getenv('PBT_CAR_SIGN_BG', default_root_bg),
            'fg': getenv('PBT_CAR_SIGN_FG', default_root_fg),
            'fm': getenv('PBT_CAR_SIGN_FM', default_root_fm),
            'text': getenv('PBT_CAR_SIGN_FORMAT', ' {{ Symbol }} '),
        },
        'Symbol': {
            'bg': getenv(
                'PBT_CAR_SIGN_SYMBOL_BG', getenv(
                    'PBT_CAR_SIGN_BG', default_symbol_bg)),
            'fg': getenv(
                'PBT_CAR_SIGN_SYMBOL_FG', getenv(
                    'PBT_CAR_SIGN_FG', default_symbol_fg)),
            'fm': getenv(
                'PBT_CAR_SIGN_SYMBOL_FM', getenv(
                    'PBT_CAR_SIGN_FM', default_symbol_fm)),
            'text': getenv(
                'PBT_CAR_SIGN_SYMBOL_FORMAT',
                '{{ %s }}' % ('Admin' if getuid() == 0 else 'User')),
        },
        'User': {
            'bg': getenv(
                'PBT_CAR_SIGN_USER_BG', getenv(
                    'PBT_CAR_SIGN_SYMBOL_BG', getenv(
                        'PBT_CAR_SIGN_BG', default_user_bg))),
            'fg': getenv('PBT_CAR_SIGN_USER_FG', 'light_green'),
            'fm': getenv(
                'PBT_CAR_SIGN_USER_FM', getenv(
                    'PBT_CAR_SIGN_SYMBOL_FM', getenv(
                        'PBT_CAR_SIGN_FM', default_user_fm))),
            'text': getenv('PBT_CAR_SIGN_USER_TEXT', '$'),
        },
        'Admin': {
            'bg': getenv(
                'PBT_CAR_SIGN_ADMIN_BG', getenv(
                    'PBT_CAR_SIGN_SYMBOL_BG', getenv(
                        'PBT_CAR_SIGN_BG', default_user_bg))),
            'fg': getenv('PBT_CAR_SIGN_ADMIN_FG', 'red'),
            'fm': getenv(
                'PBT_CAR_SIGN_ADMIN_FM', getenv(
                    'PBT_CAR_SIGN_SYMBOL_FM', getenv(
                        'PBT_CAR_SIGN_FM', default_admin_fm))),
            'text': getenv('PBT_CAR_SIGN_ADMIN_TEXT', '#'),
        },
    }

    display = getenv('PBT_CAR_SIGN_DISPLAY', True)
    wrap = getenv('PBT_CAR_SIGN_WRAP', False)
    sep = getenv('PBT_CAR_SIGN_SEP', None)
