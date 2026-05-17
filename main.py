import flet as ft

def main(page: ft.Page):
    page.title = "简约闰年查询"
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    year_input = ft.TextField(
        label="请输入年份",
        width=300,
        text_align=ft.TextAlign.CENTER,
        bgcolor=ft.colors.BLUE_GREY_800,
        color=ft.colors.WHITE,
        label_style=ft.TextStyle(color=ft.colors.BLUE_200),
        border_color=ft.colors.BLUE_400,
        focused_border_color=ft.colors.BLUE_200,
        text_size=20,
    )

    result = ft.Text(
        size=22,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE,
    )

    def check(e):
        try:
            i = int(year_input.value)
            if (i%4==0 and i%100!=0) or (i%400==0):
                result.value = f"{i}年 是闰年 ✅"
                result.color = ft.colors.GREEN_300
            else:
                result.value = f"{i}年 是平年 ❌"
                result.color = ft.colors.RED_300
            page.update()
        except:
            result.value = "请输入正确年份！⚠️"
            result.color = ft.colors.YELLOW_300
            page.update()

    page.add(
        ft.Text(
            "🗓️ 简约闰年查询",
            size=36,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLUE_200,
        ),
        ft.Divider(color=ft.colors.BLUE_400),
        ft.Container(height=20),
        year_input,
        ft.Container(height=10),
        ft.ElevatedButton(
            "判 断",
            on_click=check,
            width=300,
            height=50,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.BLUE_600,
                color=ft.colors.WHITE,
            )
        ),
        ft.Container(height=20),
        result,
    )

ft.app(target=main)