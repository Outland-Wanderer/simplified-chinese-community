translate schinese python:
    gui.language = "japanese-strict"

    gui.text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = FontGroup().add("AR_PL_KaitiM_Big5.ttf", 0x5187, 0x5187).add("AR_PL_KaitiM_Big5.ttf", 0x5463, 0x5463).add("AR_PL_KaitiM_Big5.ttf", 0x5c44, 0x5c44).add("AR_PL_KaitiM_Big5.ttf", 0x5c4c, 0x5c4c).add("AR_PL_KaitiM_Big5.ttf", 0x808f, 0x808f).add("AR_PL_KaitiM_GB.TTF", 0x2014, 0x201F).add("AR_PL_KaitiM_GB.TTF", 0x2E80, 0xffff).add("garamond.ttf", 0x0000, 0xffff)

    gui.name_text_font = "LXGWWenKaiLite-Bold.ttf"

    gui.text_size = 32

    gui.name_text_size = 48

translate schinese style ruby_style is default:
    size 24
    yoffset -32

translate schinese style say_dialogue:
    ruby_style style.ruby_style

translate schinese style history_text:
    ruby_style style.ruby_style
