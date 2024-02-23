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
                label="Tipo"
            ),
            ft.Dropdown(
                width="max",
                label="Situação"
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

    resultados=ft.Container(
        ft.Row(
            controls=(
                ft.Text(value="Resultados: 0"),
                ),
        ),
    )

    page.add(
        campos,
        btn,
        resultados
        )

ft.app(target=main)