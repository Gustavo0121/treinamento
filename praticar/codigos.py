"""
Página de ajuda.

"""

import flet as ft


def main(page: ft.Page):
    """Run this app."""
    page.title = 'Planalto Legis'

    page.appbar = ft.AppBar(
        title=ft.Text(
        'Códigos', weight=ft.FontWeight.BOLD, color='white'
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

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.CALENDAR_MONTH_ROUNDED, label='RESENHA',
            ),
            ft.NavigationDestination(icon=ft.icons.LOUPE, label='BUSCA'),
            ft.NavigationDestination(
                icon=ft.icons.STAR_PURPLE500_OUTLINED, label='FAVORITOS',
            ),
            ft.NavigationDestination(icon=ft.icons.HELP, label='AJUDA'),
        ],
        bgcolor='#3b65ad',
    )

    page.add(ft.Text('Corpo de Aplicacao'))


ft.app(target=main)