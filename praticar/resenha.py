"""
Página de ajuda.

"""

import flet as ft
import datetime

def main(page: ft.Page):
    """Run this app."""
    page.title = 'Resenha'

    page.appbar = ft.AppBar(
        title=ft.Text(
        'Resenha', weight=ft.FontWeight.BOLD, color='white'
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

    def msg_sem_pub(e):
        page.add(ft.Text(
            value='Não há publicações registradas até o momento.',
            color='red',
            size=30,
            )
        )

    date_picker = ft.DatePicker(
        on_change=msg_sem_pub,
        first_date=datetime.datetime(2000, 1, 1),
        last_date=datetime.date.today(),
    )

    page.overlay.append(date_picker)

    date_button = ft.ElevatedButton(
        str(datetime.date.today()),
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda e: date_picker.pick_date(),
        right=5,
        top=10,
    )

    page.add(ft.Stack(
        controls=(
                ft.TextField(label="Data"),
                date_button,
                )
            ),
        )

ft.app(target=main)