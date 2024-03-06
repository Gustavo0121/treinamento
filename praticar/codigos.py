"""
Página de ajuda.

"""
from pathlib import Path
import logging
import flet as ft

BLUE = '#0060B5'

def main(page: ft.Page):
    """Run this app."""
    page.title = 'Planalto Legis'

    page.scroll = ft.ScrollMode.AUTO
    
    page.appbar = ft.AppBar(
        bgcolor=BLUE,
        color=ft.colors.WHITE,
        leading=ft.Image(
            src=Path('images', 'icons', 'icon-nobg-1024.png').as_posix(),
        ),
        leading_width=40,
        title=ft.Text('Códigos', weight=ft.FontWeight.W_500),
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
                    ft.Text(value='Reúnem, em uma única Lei, normas de um mesmo ramo de direito.', size=25),
                    ft.Text(value='Código Civil', color=BLUE, size=35),
                    ft.Text(value='LEI N° 10.406, DE 10 DE JANEIRO DE 2002.', size=25),
                    ft.Divider(),
                    ft.Text(value='Código de Processo Civil', color=BLUE, size=35),
                    ft.Text(value='LEI N° 5.869, DE 11 DE JANEIRO DE 1973.', size=25),
                    ft.Divider(),
                    ft.Text(value='Código de Processo Civil', color=BLUE, size=35),
                    ft.Text(value='LEI N° 13.105, DE 16 DE MARÇO DE 2015.', size=25),
                    ft.Divider(),
                    ft.Text(value='Código Penal', color=BLUE, size=35),
                    ft.Text(value='DECRETO-LEI N° 2.848, DE 7 DE DEZEMBRO DE 1940.', size=25),
                    ft.Divider(),
                    ft.Text(value='Código de Processo Penal', color=BLUE, size=35),
                    ft.Text(value='DECRETO-LEI N° 3.689, DE 3 DE OUTUBRO DE 1941.', size=25),
                    ft.Divider(),
                    ft.Text(value='Código Tributário Nacional', color=BLUE, size=35),
                    ft.Text(value='LEI N° 5.172, DE 25 DE OUTUBRO DE 1966.', size=25),
                    ft.Divider(),
                ]
            )
        )
    )

    page.add(conteudo)


ft.app(target=main)