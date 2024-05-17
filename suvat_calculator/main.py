import flet as ft
from utils import calculateSUVAT
from math import trunc

def mainApp(page: ft.Page):
    page.title = "Suvatastic"
    page.fonts = {"Outfit": "/assets/fonts/Outfit-Regular.ttf"}
    page.horizontal_alignment = "center"
    page.theme = ft.Theme(font_family="Outfit")
    page.appbar = ft.AppBar(
        title=ft.Text(
            "SUVATastic", color=ft.colors.LIGHT_BLUE, weight=ft.FontWeight.W_700
        ),
        center_title=True,
        bgcolor=ft.colors.TRANSPARENT,
        leading_width=40,
    )
    page.update()

    def openSnackbar(msg):
        page.snack_bar = ft.SnackBar(
            ft.Text(f"{msg}"),
            duration=3500)
        page.snack_bar.open = True
        page.update()

    page.drawer = ft.NavigationDrawer(
        controls=[
            # TODO
            ft.Container(height=30),
            ft.NavigationDrawerDestination(
                label="Suvatastic",
                icon=ft.icons.HOME,
            ),
            ft.Container(height=20),
            ft.Divider(thickness=2),
            ft.Container(height=20),

            ft.Container(height=20),
            ft.Text(
                spans=[
                    ft.TextSpan(
                        text="Docs", url="https://niko.super.site/suvatastic"
                    ),
                    ft.TextSpan(" (click)"),
                ],
                text_align=ft.TextAlign.CENTER,
                size=16,
                color=ft.colors.LIGHT_BLUE_100,
            ),
            ft.Container(height=200),
            ft.Text("Developed by Nik",text_align=ft.TextAlign.CENTER,)
        ],
    )

    s = ft.TextField(
        label="Displacement (m)", 
        width=180, 
        keyboard_type=ft.KeyboardType.NUMBER,
        disabled=True
    )
    u = ft.TextField(
        label="Initial Velocity (ms-1)",
        width=180,
        keyboard_type=ft.KeyboardType.NUMBER,
        disabled=True
    )
    v = ft.TextField(
        label="Final Velocity (ms-1)",
        width=180,
        keyboard_type=ft.KeyboardType.NUMBER,
        disabled=True
    )
    a = ft.TextField(
        label="Acceleration (ms-2)",
        width=180,
        keyboard_type=ft.KeyboardType.NUMBER,
        disabled=True
    )
    t = ft.TextField(
        label="Time taken (s)",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER,
        disabled=True
    )

    BTNcalculate = ft.FilledButton(
        text="Calculate",
        width=150,
        height=60,
        disabled=True,
        adaptive=True,
    )
    BTNclear = ft.TextButton(
        text="Clear",
        width=100,
        disabled=False,
        adaptive=True,
    )
    rounding = 2
    TFrounding = ft.TextField(value=rounding, 
                              label="Round (d.p.)", 
                              width=100, 
                              text_align=ft.TextAlign.CENTER,
                              max_length=2,
                              keyboard_type=ft.KeyboardType.NUMBER,
                              enable_suggestions=False,
                              border=ft.InputBorder.UNDERLINE,                       
                              )

    def clearFields(e):
        s.disabled = False
        u.disabled = False
        v.disabled = False
        a.disabled = False
        t.disabled = False

        
        s.value = ""
        u.value = ""
        v.value = ""
        a.value = ""
        t.value = ""

        s.disabled = True
        u.disabled = True
        v.disabled = True
        a.disabled = True
        t.disabled = True
        BTNcalculate.disabled = True

        page.update()

    BTNclear.on_click = clearFields

    def displayResults(e) -> None:

        try:

            rounding = trunc(float(TFrounding.value))

            if rounding < 1:
                rounding = 2
                TFrounding.value = '2'
            else: 
                TFrounding.value = rounding

        except Exception:
            rounding = 2
            TFrounding.value = '2'

        # Predefined snack_bar messages
        msg_four_values = "Only three fields should be filled"
        msg_impos_result = "Make sure you inputted the correct values. \tUnexpected value were returned."
        
        s_value = str(s.value).strip()
        u_value = str(u.value).strip()
        v_value = str(v.value).strip()
        a_value = str(a.value).strip()
        t_value = str(t.value).strip()
        try:
            # Checks if Displacement field is disabled (s)
            if s.disabled:
                
                if u_value != '' and v_value != '' and a_value != '' and t_value != '':
                    openSnackbar(msg=msg_four_values)

                elif v_value != "" and a_value != "" and t_value != "":
                    s.disabled = False
                    s.value = str(
                        round(
                            calculateSUVAT("n", "n", v_value, a_value, t_value, "s"),
                            ndigits=rounding
                              )
                    )
                    s.disabled = True

                elif u_value != "" and a_value != "" and t_value != "":
                    s.disabled = False
                    s.value = str(
                        round(
                            calculateSUVAT("n", u_value, "n", a_value, t_value, "s"),
                            ndigits=rounding,
                        )
                    )
                    s.disabled = True

                elif u_value != "" and v_value != "" and t_value != "":
                    s.disabled = False
                    result = str(
                        round(
                            calculateSUVAT("n", u_value, v_value, "n", t_value, "s"),
                            ndigits=rounding,
                        )
                    )
                    s.value = result
                    s.disabled = True

                elif v_value != "" and u_value != "" and a_value != "":
                    s.disabled = False
                    s.value = str(
                        round(
                            calculateSUVAT("n", u_value, v_value, a_value, "n", "s"),
                            rounding,
                        )
                    )
                    s.disabled = True
                else:
                    pass
            # Checks if FINAL field is  disabled
            elif u.disabled:

                if s_value != '' and v_value != '' and a_value != '' and t_value != '':
                    openSnackbar(msg=msg_four_values)

                elif v_value != "" and a_value != "" and t_value != "":
                    u.disabled = False
                    u.value = str(
                        round(
                            calculateSUVAT("n", "n", v_value, a_value, t_value, "u"),
                            rounding,
                        )
                    )
                    u.disabled = True

                elif v_value != "" and a_value != "" and s_value != "":
                    u.disabled = False
                    result = str(
                        round(
                            calculateSUVAT(s_value, "n", v_value, a_value, "n", "u"),
                            rounding,
                        )
                    )
                    u.value = f'±{result}'
                    u.disabled = True

                elif s_value != "" and v_value != "" and t_value != "":
                    u.disabled = False
                    u.value = str(
                        round(
                            calculateSUVAT(s_value, "n", v_value,'n', t_value, "u"),
                            rounding,
                        )
                    )
                    u.disabled = True

                elif s_value != "" and a_value != "" and t_value != "":
                    u.disabled = False
                    u.value = str(
                        round(
                            calculateSUVAT(s_value, "n", "n", a_value, t_value, "u"),
                            rounding,
                        )
                    )
                    u.disabled = True
                else:
                    pass
            # Checks if final velocity field is disabled (v)
            elif v.disabled:

                if s_value != '' and u_value != '' and a_value != '' and t_value != '':
                    openSnackbar(msg=msg_four_values)

                elif u_value != "" and a_value != "" and t_value != "":
                    v.disabled = False
                    v.value = str(
                        round(
                            calculateSUVAT("n", u_value, "n", a_value, t_value, "v"),
                            rounding,
                        )
                    )
                    v.disabled = True
                elif u_value != "" and a_value != "" and s_value != "":
                    v.disabled = False
                    v.value = str(
                        round(
                            calculateSUVAT(s_value, u_value, "n", a_value, "n", "v"),
                            rounding,
                        )
                    )
                    v.disabled = True

                elif s_value != "" and u_value != "" and t_value != "":
                    v.disabled = False
                    v.value = str(
                        round(
                            calculateSUVAT(s_value, u_value, "n", "n", t_value, "v"),
                            rounding,
                        )
                    )
                    v.disabled = True

                elif s_value != "" and a_value != "" and t_value != "":
                    v.disabled = False
                    v.value = str(
                        round(
                            calculateSUVAT(s_value, "n", "n", a_value, t_value, "v"),
                            rounding,
                        )
                    )
                    v.disabled = True
            # Checks if acceleration field is disabled (a)
            elif a.disabled:

                if s_value != '' and u_value != '' and v_value != '' and t_value != '':
                    openSnackbar(msg=msg_four_values)

                elif s_value != "" and u_value != "" and v_value != "":
                    a.disabled = False
                    result = str(
                        round(
                            calculateSUVAT(s_value, u_value, v_value, "n", "n", toFind="a"),
                            rounding
                            )
                    )
                    a.value = result
                    a.disabled = True

                elif s_value != '' and u_value != '' and t != '':
                    a.disabled = False
                    result = round(
                        calculateSUVAT(s_value, u_value, 'n', 'n', t_value, toFind='a'),
                        rounding
                        )
                    a.value = str(result)
                    a.disabled = True

                elif s_value != '' and v_value != '' and t_value != '':
                    result = round(
                        calculateSUVAT(s_value, 'n', v_value, 'n', t_value, toFind='a'),
                        rounding
                        )
                    a.value = str(result)
                    a.disabled = True

                elif u_value != '' and v_value != '' and t_value != '':
                    result = round(
                        calculateSUVAT('n', u_value, v_value, 'n', t_value, toFind='a'),
                        rounding
                        )
                    a.value = str(result)
                    a.disabled = True

            elif t.disabled:

                if s_value != '' and u_value != '' and v_value != '' and a_value != '':
                    openSnackbar(msg=msg_four_values)

                elif s_value != "" and u_value != "" and v_value != "":
                    t.disabled = False
                    t.value = str(
                        round(
                            calculateSUVAT(s_value, u_value, v_value, "n", "n", "t"),
                            rounding,
                        )
                    )
                    t.disabled = True

                elif a_value != "" and u_value != "" and v_value != "":
                    t.disabled = False
                    t.value = str(
                        round(
                            calculateSUVAT("n", u_value, v_value, a_value, "n", "t"),
                            rounding,
                        )
                    )
                    t.disabled = True

                elif a_value != "" and s_value != "" and v_value != "":

                    result = calculateSUVAT(s_value, "n", v_value, a_value, "n", "t")
                    if result[0] > 0 or result[1] > 0:
                        t.disabled = False
                        text_res = str(round(result[0], rounding))
                        text_res2 = str(round(result[1], rounding))
                        if result[1] <= 0:
                            t.value = text_res
                        elif result[0] <= 0:
                            t.value = text_res2
                        else:
                            t.value = text_res + ' or ' + text_res2
                        t.disabled = True
                    else:
                        openSnackbar(msg="Results are negative. Impossible!")

                elif s_value != "" and a_value != "" and u_value != "":
                    result = calculateSUVAT(s_value, u_value, "n", a_value, "n", "t")
                    if result[0] >= result[1]:
                        t.disabled = False
                        t.value = str(round(result[0], rounding))
                        t.disabled = True

                    else:
                        openSnackbar(msg="Time turned out to be negative. Impossible!")
                        page.update()

                    t.disabled = True


            page.update()

        except Exception as e:
            if e == ValueError or str(e) == "math domain error":
                clearFields(e)
                openSnackbar(msg=msg_impos_result)
                page.update()

            else:
                openSnackbar(msg='Input must be a decimal value')

    def onSelection(e):

        COLOR = ft.colors.LIGHT_BLUE

        if e.control.value:
            BTNcalculate.disabled = False
            s.color = ft.colors.WHITE
            u.color = ft.colors.WHITE
            v.color = ft.colors.WHITE
            a.color = ft.colors.WHITE
            t.color = ft.colors.WHITE

        if e.control.value == "s":
            s.disabled = True
            s.color = COLOR
            u.disabled = False
            v.disabled = False
            a.disabled = False
            t.disabled = False
            page.update()

        elif e.control.value == "u":
            u.color = COLOR
            s.disabled = False
            u.disabled = True
            v.disabled = False
            a.disabled = False
            t.disabled = False
            page.update()

        elif e.control.value == "v":
            v.color = COLOR
            s.disabled = False
            u.disabled = False
            v.disabled = True
            a.disabled = False
            t.disabled = False
            page.update()

        elif e.control.value == "a":
            a.color = COLOR
            s.disabled = False
            u.disabled = False
            v.disabled = False
            a.disabled = True
            t.disabled = False
            page.update()

        elif e.control.value == "t":
            t.color = COLOR
            s.disabled = False
            u.disabled = False
            v.disabled = False
            a.disabled = False
            t.disabled = True
            page.update()

    SUVATselection = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="s", label="Displacement"),
                ft.Radio(value="u", label="Initial Velocity"),
                ft.Radio(value="v", label="Final Velocity"),
                ft.Radio(value="a", label="Acceleration"),
                ft.Radio(value="t", label="Time"),
            ],
            run_spacing=20,
            scroll=True,
        ),
        on_change=onSelection,
    )
    BTNcalculate.on_click = displayResults

    page.add(
        ft.Text("Select what do you want to find: "),
        SUVATselection,
    )
    page.add(
        ft.SafeArea(
            ft.Row(
                [
                    s,
                    u,
                    v,
                    a,
                    t,
                ],
                spacing=10,
                run_spacing=10,
                wrap=True,
                alignment=ft.MainAxisAlignment.CENTER,
                
            ),
        )
    )
    page.add(TFrounding, BTNcalculate, BTNclear)
    page.update()


ft.app(mainApp)
