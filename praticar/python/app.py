"""App com flet."""

import flet as ft
from pathlib import Path

def main(page: ft.Page):

    page.bgcolor = '#00529e'

    i = ft.Image(src=Path('praticar','logo.png').as_posix(), width=150, height=150)
    a = ft.Image(src="https://www.cenariomt.com.br/wp-content/uploads/2024/01/palacio-do-planalto-sera-reaberto-para-visitas-guiadas-capa-2024-01-12-2024-01-12-1153885692-1600x1067.jpg", opacity=0.1, width=150, height=150)
    
    page.add(
        ft.Text(value="Planalto Legis", color="white", style="Impact", size=50),
        i
    )

ft.app(target=main)