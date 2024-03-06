"""
Página de ajuda.

"""

import flet as ft

BLUE = '#0060B5'


class Navbar(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.CALENDAR_MONTH_ROUNDED, label='RESENHA'
            ),
            ft.NavigationDestination(icon=ft.icons.LOUPE, label='BUSCA'),
            ft.NavigationDestination(
                icon=ft.icons.STAR_PURPLE500_OUTLINED, label='FAVORITOS'
            ),
            ft.NavigationDestination(icon=ft.icons.HELP, label='AJUDA'),
        ],
        bgcolor=ft.colors.WHITE,
    )


def main(page: ft.Page):
    """Run this app."""
    page.title = 'Planalto Legis'

    page.appbar = ft.AppBar(
        title=ft.Text(
        'Ajuda', weight=ft.FontWeight.BOLD, color='white'
        ),
        bgcolor='#3b65ad',
        center_title=True,
        actions=[ft.IconButton(
            ft.icons.MENU,
            tooltip='Menu',
            icon_color='black',
            ),
            ]
    )


    page.navigation_bar = Navbar()

    page.add(ft.Text('Corpo de Aplicacao'))


ft.app(target=main)