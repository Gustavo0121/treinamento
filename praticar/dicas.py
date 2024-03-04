"""
Página de dica.

"""

import flet as ft



class Dicas(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Column(
            controls=(
                ft.Text(value="Dicas de Pesquisa", color="#3b65ad", size=60),
                ft.Text(
                    value="Preencha os campos desejados e clique"
                    "no botão buscar. Os documentos que possuírem"
                    "todos os dados serão retornados.",
                    size=30,
                    ),
                ft.Text(
                    value='Para refinar a pesquisa acrescente aspas'
                    'duplas no início e fim do termo pesquisado.'
                    'Exemplo: “marco civil da internet”',
                    size=30
                ),
            ),
            spacing=50
        )


def main(page: ft.Page):
    """"""
    page.title = 'Dicas'

    page.appbar = ft.AppBar(
        title=ft.Text(
        "Dicas", weight=ft.FontWeight.BOLD, color="white"
        ),
        bgcolor="#3b65ad",
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
        bgcolor="#3b65ad",
    )

    page.add(Dicas())


ft.app(target=main)