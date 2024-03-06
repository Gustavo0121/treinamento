"""Page Estatutos."""

import logging
from pathlib import Path
import flet as ft

BLUE = '#0060B5'
def main(page: ft.Page) -> None:
    """Run this app."""
    page.title = 'Estatutos'

    page.scroll = ft.ScrollMode.AUTO
    
    page.appbar = ft.AppBar(
        bgcolor=BLUE,
        color=ft.colors.WHITE,
        leading=ft.Image(
            src=Path('images', 'icons', 'icon-nobg-1024.png').as_posix(),
        ),
        leading_width=40,
        title=ft.Text('Estatutos', weight=ft.FontWeight.W_500),
        center_title=True,
        actions=[
            ft.PopupMenuButton(
                visible=True,
                icon=ft.icons.MENU,
                items=[
                    ft.PopupMenuItem(),
                    ft.Divider(),
                    ft.PopupMenuItem(
                        text='Busca Avançada',
                        on_click=lambda _: logging.debug('busca avançada'),
                    ),
                    ft.PopupMenuItem(
                        text='Constituição',
                        on_click=lambda _: logging.debug('constituição'),
                    ),
                    ft.PopupMenuItem(
                        text='Códigos',
                        on_click=lambda _: logging.debug('códigos'),
                    ),
                    ft.PopupMenuItem(
                        text='Estatutos',
                        on_click=lambda _: logging.debug('estatutos'),
                    ),
                    ft.PopupMenuItem(
                        text='Favoritos',
                        on_click=lambda _: logging.debug('favoritos'),
                    ),
                    ft.PopupMenuItem(
                        text='Resenha',
                        on_click=lambda _: logging.debug('resenha'),
                    ),
                    ft.PopupMenuItem(
                        text='Ajuda',
                        on_click=lambda _: logging.debug('ajuda'),
                    ),
                ],
            ),
        ],
    )

    page.navigation_bar = ft.NavigationBar(
        visible=True,
        bgcolor=BLUE,
        surface_tint_color=ft.colors.WHITE,
        shadow_color=ft.colors.PURPLE_100,
        indicator_color=ft.colors.BLUE,
        selected_index=1,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                tooltip='Resenha diária',
                label='RESENHA',
            ),
            ft.NavigationDestination(
                icon=ft.icons.SEARCH,
                tooltip='Busca avançada',
                label='BUSCA',
            ),
            ft.NavigationDestination(
                icon=ft.icons.STAR_PURPLE500_OUTLINED,
                tooltip='Atos Favoritos',
                label='FAVORITOS',
            ),
            ft.NavigationDestination(
                icon=ft.icons.HELP,
                label='AJUDA',
            ),
        ],
    )

    conteudo=ft.Container(
        content=(
            ft.Column(
                [
                    ft.Text(value='Estatuto da Advocacia e da Ordem dos Advogados do Brasil', color=BLUE, size=35),
                    ft.Text(value='LEI N° 8.906, DE 4 DE JULHO DE 1994.', size=25),
                    ft.Divider(),
                    ft.Text(value='Estatuto da Criança e do Adolescente', color=BLUE, size=35),
                    ft.Text(value='LEI N° 8.069, DE 13 DE JULHO DE 1990.', size=25),
                    ft.Divider(),
                    ft.Text(value='Estatuto da Cidade', color=BLUE, size=35),
                    ft.Text(value='LEI N° 10.257, DE 10 DE JULHO DE 2001.', size=25),
                    ft.Divider(),
                    ft.Text(value='Estatuto de Defesa do Torcedor', color=BLUE, size=35),
                    ft.Text(value='LEI N° 10.671, DE 15 DE MAIO DE 2003.', size=25),
                    ft.Divider(),
                    ft.Text(value='Estatuto do Desarmamento', color=BLUE, size=35),
                    ft.Text(value='LEI N° 10.826, DE 22 DE DEZEMBRO DE 2003.', size=25),
                    ft.Divider(),
                    ft.Text(value='Estatuto do Estrangeiro', color=BLUE, size=35),
                    ft.Text(value='LEI N° 13.445, DE 24 DE MAIO DE 2017.', size=25),
                    ft.Divider(),
                ]
            )
        )
    )

    page.add(
        conteudo
    )

ft.app(target=main)
