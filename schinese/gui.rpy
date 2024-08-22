define config.font_name_map["twKai"] = FontGroup().add("AR_PL_KaitiM_GB.TTF", 0x3001, 0x3002).add("AR_PL_KaitiM_GB.TTF", 0xff01, 0xff01).add("AR_PL_KaitiM_GB.TTF", 0xff0c, 0xff0c).add("AR_PL_KaitiM_GB.TTF", 0x2014, 0x201f).add("TW-Kai-98_1.ttf", 0x2E80, 0xffff).add("garamond.ttf", 0x0000, 0xffff)

translate schinese python:
    gui.language = "japanese-normal"

    gui.system_font = "Source_Han_Sans_CN-Regular.otf"

    gui.text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = FontGroup().add("AR_PL_KaitiM_Big5.ttf", 0x5187, 0x5187).add("AR_PL_KaitiM_Big5.ttf", 0x5463, 0x5463).add("AR_PL_KaitiM_Big5.ttf", 0x5c44, 0x5c44).add("AR_PL_KaitiM_Big5.ttf", 0x5c4c, 0x5c4c).add("AR_PL_KaitiM_Big5.ttf", 0x808f, 0x808f).add("AR_PL_KaitiM_Big5.ttf", 0x6294, 0x6294).add("AR_PL_KaitiM_Big5.TTF", 0x77ad, 0x77ad).add("AR_PL_KaitiM_GB.TTF", 0x2014, 0x201f).add("AR_PL_KaitiM_GB.TTF", 0x2E80, 0xffff).add("garamond.ttf", 0x0000, 0xffff)

    gui.name_text_font = "LXGWWenKaiLite-Bold.ttf"

    gui.text_size = 32

    gui.name_text_size = 48

    gui.headline_text_font = FontGroup().add("Source_Han_Serif_CN-Bold.otf", 0x2E80, 0xffff).add("kingthing.ttf", 0x0000, 0xffff)

    @gui.variant
    def small():
        gui.text_size = 48
        gui.name_text_size = 42

translate schinese style book_style:
    font "nzgrKangxi.ttf"

translate schinese style pling_button_text:
    font gui.text_font

translate schinese style screen_title_text:
    font gui.headline_text_font

translate schinese style screen_content_button_text:
    font gui.headline_text_font

translate schinese style screen_content_text:
    font gui.headline_text_font

translate schinese style page_button_text:
    font gui.headline_text_font

translate schinese style click_button_text:
    font gui.headline_text_font

translate schinese style footstep_button_text:
    font gui.headline_text_font

translate schinese style stash_button_text:
    font gui.headline_text_font

translate schinese style screen_title_text:
    font gui.headline_text_font

translate schinese style screen_content_text:
    font gui.headline_text_font

translate schinese style screen_content_white_text:
    font gui.text_font

translate schinese style screen_content_yellow_text:
    font gui.text_font

translate schinese style quest_title_text:
    font gui.text_font

translate schinese style quest_line_breaker_text:
    font gui.text_font

translate schinese style stats_label_text:
    font gui.text_font

translate schinese style vitals_label_text:
    font gui.text_font

translate schinese style ruby_style is default:
    size 24
    yoffset -32

translate schinese style say_dialogue:
    ruby_style style.ruby_style
    ruby_line_leading 12

translate schinese style history_text:
    ruby_style style.ruby_style
