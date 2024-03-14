"""
Página de ajuda.

"""

import flet as ft
from pathlib import Path

def main(page: ft.Page):
    """Run this app."""
    page.title = 'Favoritos'

    page.appbar = ft.AppBar(
        title=ft.Text(
        'Favoritos', weight=ft.FontWeight.BOLD, color='white'
        ),
        bgcolor='#3b65ad',
        center_title=True,
        leading=ft.Image(src=Path(__file__).parent.joinpath('icons/swiperight.png').as_posix()),
        leading_width=40,
        actions=[
            ft.IconButton(
                ft.icons.MENU,
                tooltip='Menu',
                icon_color='black',
                on_click=lambda e: print(Path(__file__).parent.joinpath('icons/swiperight.png')),
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

    icon_right=ft.ResponsiveRow(
            [
                ft.Image(
                src='/images/swiperight.png', height=100, col=5
                ),
            ],
            columns=10
        )

    icon_left=ft.ResponsiveRow(
            [
                ft.Image(
                src='/images/swipeleft.png', height=100, col=5
                ),
            ],
            columns=10
        )

    conteudo2=ft.Text(
        value="\nUma vez favoritada, a legislação fica listada aqui e pode ser"
        " acessada em modo offline.\n\nPara retirar a legislação da lista,"
        " arraste o nome para a esquerda.",
        size=30
    )

    page.add(
        conteudo1,
        # ft.Image(src="/images/swipeleft.png"),
        icon_right,
        conteudo2,
        icon_left
    )


ft.app(target=main)