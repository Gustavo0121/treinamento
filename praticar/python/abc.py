"""Página de busca avançada."""

import flet as ft

def main(page: ft.Page):

    page.appbar = ft.AppBar(
        title=ft.Text(
        "Planalto Legis", weight=ft.FontWeight.BOLD, color="black"
        ),
        bgcolor="blue",
        center_title=True,
        actions=[ft.IconButton(ft.icons.MENU, tooltip="Menu", icon_color="black")]
    )

    campos = ft.Container(
        content=ft.Column([
            ft.TextField(label="Termo"),
            ft.ResponsiveRow(
                columns=4,
                controls=(ft.TextField(label="Ano", col=2), ft.TextField(label="Número", col=2))
            ),
            ft.Dropdown(
                width="max",
                label="Tipo",
                options=[
            ft.dropdown.Option('CONSTITUIÇÃO'),
            ft.dropdown.Option('DECRETO'),
            ft.dropdown.Option('DECRETO EXECUTIVO'),
            ft.dropdown.Option('DECRETO NÃO NUMERADO'),
            ft.dropdown.Option('DECRETO-LEI'),
            ft.dropdown.Option('EMENDA CONSTITUCIONAL'),
            ft.dropdown.Option('LEI'),
            ft.dropdown.Option('LEI COMPLEMENTAR'),
            ft.dropdown.Option('LEI ORDINÁRIA'),
            ft.dropdown.Option('MEDIDA PROVISÓRIA'),
            ft.dropdown.Option('RESOLUÇÃO'),
            ],
            ),
            ft.Dropdown(
                width="max",
                label="Situação",
                options=[
            ft.dropdown.Option('NÃO CONSTA REVOGAÇÃO EXPRESSA'),
            ft.dropdown.Option('REVOGADO'),
                ],
            )
        ]
        )
    )

    btn=ft.Row(
          controls=(
                ft.ElevatedButton(
                      text="BUSCAR",
                      icon=ft.icons.SEARCH
                ),
            ),
            alignment=ft.MainAxisAlignment.CENTER
        )

    resultados=ft.Text(value="Resultados: 0", text_align="right")

    page.add(
        campos,
        btn,
        resultados
        )

ft.app(target=main)