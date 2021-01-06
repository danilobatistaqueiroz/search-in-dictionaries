import os
import urllib
import logging

from anki.hooks import addHook, wrap
from aqt.editor import Editor
from typing import List, Callable
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *

from . import collins
from . import macmillan
from . import babla

from .config import setup_synced_config

dictionaries = ['collins','macmillan','babla']

ADDON_PATH = os.path.dirname(__file__)
ICON_PATH = os.path.join(ADDON_PATH, "icons", "dict.ico")
CONFIG = mw.addonManager.getConfig(__name__)

select_elm = ("""<select onchange='pycmd("Dictionary:" +"""
              """ this.selectedOptions[0].text)' """
              """style='vertical-align: top;'>{}</select>""")

def paste_definitions(editor: Editor) -> None:

    note = editor.note

    try:
        word = note[CONFIG["WORD_FIELD"]]
    except KeyError:
        showInfo(f"Field '{CONFIG['WORD_FIELD']}' doesn't exist.")
        return
    logging.debug(f"Field text: {word}")

    word = word.lower()

    language = CONFIG["DESTINATION_LANGUAGE"]
    abrv_language = CONFIG["DESTINATION_ABRV_LANGUAGE"]

    if editor.dic == 'collins':
        results = collins.search(word)
    elif editor.dic == 'macmillan':
        results = macmillan.search(word)
    elif editor.dic == 'babla':
        results = babla.search(word, abrv_language, language)

    if len(results) == 0:
        showInfo(f"Word {word} not found.")
    elif results[0] == False:
        showInfo(f"Word {word} not found.")
    elif results[0].strip() == '':
        showInfo(f"Word {word} not found.")

    try:
        note[editor.dic+CONFIG["DEFINITIONS_FIELD"]] = f'{results[0]}'
    except KeyError:
        showInfo(f"Field '{CONFIG['DEFINITIONS_FIELD']}' doesn't exist.")
        return

    if len(results) >= 2:
        try:
            note[editor.dic+CONFIG["IPA_FIELD"]] = f'{results[1]}'
        except KeyError:
            showInfo(f"Field '{CONFIG['IPA_FIELD']}' doesn't exist.")
            return

    if len(results) == 3:
        try:
            note[editor.dic+CONFIG["PHRASES_FIELD"]] = f'{results[1]}'
        except KeyError:
            showInfo(f"Field '{CONFIG['PHRASES_FIELD']}' doesn't exist.")
            return

    # update editor
    editor.loadNote()
    editor.web.setFocus()
    editor.web.eval("focusField(%d);" % editor.currentField)

def on_setup_buttons(buttons: List[str], editor: Editor) -> List[str]:

    button = editor.addButton(ICON_PATH, "myad", paste_definitions)
    buttons.append(button)

    previous_dic = get_default_dictionary(mw)
    options = [f"""<option>{previous_dic}</option>"""]  # first entry is the last selection
    options += [
        f"""<option>{dic}</option>"""
        for dic in dictionaries
        if dic != previous_dic
    ]
    combo = select_elm.format("".join(options))
    buttons.append(combo)

    return buttons


def get_deck_name(main_window: mw) -> str:
    """ Get the name of the current deck.

    :param main_window: main window of Anki
    :return: name of selected deck
    """
    try:
        deck_name = main_window.col.decks.current()['name']
    except AttributeError:
        # No deck opened?
        deck_name = None
    return deck_name

def get_default_dictionary(main_window: mw) -> str:
    """ Get the default dictionary.

    :param main_window: main window of Anki
    :return: default dictionary for Anki or Anki deck
    """
    config = mw.col.conf['anki_dics_conf']
    dic = config['dic']
    if config['defaultdicperdeck']:
        deck_name = get_deck_name(main_window)
        if deck_name and deck_name in config['deckdefaultdic']:
            dic = config['deckdefaultdic'][deck_name]
    return dic

def set_default_dictionary(main_window: mw, dic: str) -> None:
    """ Set new default dictionary.

    :param main_window: main window of Anki
    :param dic: new default dictionary
    """
    config = mw.col.conf['anki_dics_conf']
    config['dic'] = dic  # Always update the overall default
    if config['defaultdicperdeck']:
        deck_name = get_deck_name(main_window)
        if deck_name:
            config['deckdefaultdic'][deck_name] = dic


def on_dictionary_select(editor: Editor, dic: str) -> None:
    """ Set new default dictionary.

    :param editor: Anki editor window
    :param dic: name of selected dictionary
    """
    set_default_dictionary(mw, dic)
    editor.dic = dic


def init_dic(editor: Editor, *args, **kwargs) -> None:
    """ Get the last selected/default dictionary.

    :param editor: Anki editor window
    """
    previous_dic = get_default_dictionary(mw)
    editor.dic = previous_dic


def on_bridge_cmd(editor: Editor, command: str, _old: Callable) -> None:
    """ React when new combobox selection is made.

    :param editor: Anki editor window
    :param command: editor command (e.g. own Dictionary or focus, blur, key, ...)
    :param _old: old editor.onBridgeCmd method
    """
    # old commands are executed like before
    if not command.startswith("Dictionary"):
        _old(editor, command)
    # new dictionary gets selected in the combobox
    else:
        _, dic = command.split(":")
        on_dictionary_select(editor, dic)


addHook("profileLoaded", setup_synced_config)

addHook("setupEditorButtons", on_setup_buttons)

Editor.onBridgeCmd = wrap(Editor.onBridgeCmd, on_bridge_cmd, "around")
Editor.__init__ = wrap(Editor.__init__, init_dic)