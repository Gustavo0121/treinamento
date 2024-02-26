import flet as ft

def main(page: ft.Page):

    # page.bgcolor = "#328ba8"

    page2 = ft.Container(
        ft.Column(
            controls=[
                ft.Text(value="Busca Avançada", size=25, text_align="left"), 
                ft.Text(value="Constituição", size=25, text_align="left"),
                ft.Text(value="Códigos", size=25, text_align="left"),
                ft.Text(value="Estatutos", size=25, text_align="left"),
                ft.Text(value="Favoritos", size=25, text_align="left"),
                ft.Text(value="Resenha", size=25, text_align="left"),
                ft.Text(value="Ajuda", size=25, text_align="left"),
                ],
                spacing=30),
        ft.AppBar(
                    title=ft.Text(
                        "Acesso Rápido",
                        weight=ft.FontWeight.BOLD,
                        color="black",
                                ),
                        bgcolor="blue",
                        center_title=True),
        width=500,
        height=950,
        bgcolor="blue",
        border_radius=10,
        offset=ft.transform.Offset(4, 0),
        animate_offset=ft.animation.Animation(600),
    )

    def animate(e):
        if page2.offset == ft.Offset(x=3, y=0):
            page2.offset = ft.transform.Offset(4, 0)
        else:
            page2.offset = ft.transform.Offset(3, 0)
        page2.update()

    page.appbar = ft.AppBar(
        title=ft.Text(
        "Planalto Legis", weight=ft.FontWeight.BOLD, color="black"
        ),
        bgcolor="blue",
        center_title=True,
        actions=[ft.IconButton(ft.icons.MENU, tooltip="Menu", icon_color="black", on_click=animate)]
    )

    page.add(page2)

ft.app(target=main)