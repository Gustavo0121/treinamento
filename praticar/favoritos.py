"""
Página de ajuda.

"""

import flet as ft


def main(page: ft.Page):
    """Run this app."""
    page.title = 'Favoritos'

    page.appbar = ft.AppBar(
        title=ft.Text(
        'Favoritos', weight=ft.FontWeight.BOLD, color='white'
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

    conteudo1=ft.Text(
        value="Você pode guardar o texto das legislações na sua lista de"
        " favoritos.\n\nBasta arrastar o nome da legislação para a direita na"
        " tela de resultados da busca.\n",
        size=30
    )

    icon=ft.icons.MOBILE_SCREEN_SHARE

    conteudo2=ft.Text(
        value="\nUma vez favoritada, a legislação fica listada aqui e pode ser"
        " acessada em modo offline.\n\nPara retirar a legislação da lista,"
        " arraste o nome para a esquerda.",
        size=30
    )

    page.add(
        conteudo1,
        conteudo2,
    )


ft.app(target=main)