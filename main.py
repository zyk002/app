import flet as ft

def main(page: ft.Page):
    page.title = "闰年查询"
    
    year_input = ft.TextField(label="请输入年份")
    result = ft.Text()
    
    def check(e):
        try:
            i = int(year_input.value)
            if (i%4==0 and i%100!=0) or (i%400==0):
                result.value = f"{i}年 是闰年 ✅"
            else:
                result.value = f"{i}年 是平年 ❌"
            page.update()
        except:
            result.value = "请输入正确年份！⚠️"
            page.update()
    
    page.add(
        year_input,
        ft.ElevatedButton("判断", on_click=check),
        result
    )

ft.app(target=main)