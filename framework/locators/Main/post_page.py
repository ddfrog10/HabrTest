"""Локаторы на странице написания поста"""


class PostScreen:
    field_text = '//*[@class="ProseMirror"]'
    header_text = '//*[@class="title__wrapper is-empty is-editor-empty"]'
    write_text = '//*[@class="ProseMirror-trailingBreak"]'
    button_restore = '//*[@class="tm-publication__restore-button"]'
    header_text_full = '//h1[@class="title"]'
    write_text_full = '//p[1]/text()'
    save_text = '//*[@class="tm-publication__bottom-time"]'
