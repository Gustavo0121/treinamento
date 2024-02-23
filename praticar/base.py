"""
Página de ajuda.

"""

import flet as ft


def main(page: ft.Page):
    """"""
    page.title = 'Help'

    page.appbar = ft.AppBar(
        title=ft.Text(
        "Ajuda", weight=ft.FontWeight.BOLD, color="white"
        ),
        bgcolor="#144696",
        center_title=True,
        actions=[ft.IconButton(ft.icons.MENU, tooltip="Menu", icon_color="black")]
    )

    page.navigation_bar = ft.NavigationBar(
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
        bgcolor="#144696",
    )

    page.add(ft.Text('Corpo de Aplicacao'))


ft.app(target=main)