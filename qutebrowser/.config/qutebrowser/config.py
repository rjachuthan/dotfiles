# Autogenerated config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

c.content.autoplay = False

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
# config.set('content.notifications', False, 'https://www.reddit.com')

# When a hint can be automatically followed without pressing Enter.
# Type: String
# Valid values:
#   - always: Auto-follow whenever there is only a single hint on a page.
#   - unique-match: Auto-follow whenever there is a unique non-empty match in either the hint string (word mode) or filter (number mode).
#   - full-match: Follow the hint when the user typed the whole hint (letter, word or number mode) or the element's text (only in number mode).
#   - never: The user will always need to press Enter to follow a hint.
c.hints.auto_follow = 'always'

# Characters used for hint strings.
# Type: UniqueCharString
c.hints.chars = 'arstdhneiowfpluy'

# Timeout (in milliseconds) for partially typed key bindings. If the
# current input forms only partial matches, the keystring will be
# cleared after this time. If set to 0, partially typed bindings are
# never cleared.
# Type: Int
c.input.partial_timeout = 0

# Time (in milliseconds) from pressing a key to seeing the keyhint
# dialog.
# Type: Int
c.keyhint.delay = 250

# When/how to show the scrollbar.
# Type: String
# Valid values:
#   - always: Always show the scrollbar.
#   - never: Never show the scrollbar.
#   - when-searching: Show the scrollbar when searching for text in the webpage. With the QtWebKit backend, this is equal to `never`.
#   - overlay: Show an overlay scrollbar. On macOS, this is unavailable and equal to `when-searching`; with the QtWebKit backend, this is equal to `never`. Enabling/disabling overlay scrollbars requires a restart.
c.scrolling.bar = 'never'

# Open new tabs (middleclick/ctrl+click) in the background.
# Type: Bool
c.tabs.background = True

# Position of new tabs which are not opened from another tab. See
# `tabs.new_position.stacking` for controlling stacking behavior.
# Type: NewTabPosition
# Valid values:
#   - prev: Before the current tab.
#   - next: After the current tab.
#   - first: At the beginning.
#   - last: At the end.
c.tabs.new_position.unrelated = 'next'

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'prev'


# Format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: Percentage as a string like `[10%]`. *
# `{perc_raw}`: Raw percentage, e.g. `10`. * `{current_title}`: Title of
# the current web page. * `{title_sep}`: The string `" - "` if a title
# is set, empty otherwise. * `{index}`: Index of this tab. *
# `{aligned_index}`: Index of this tab padded with spaces to have the
# same   width. * `{id}`: Internal tab ID of this tab. * `{scroll_pos}`:
# Page scroll position. * `{host}`: Host of the current web page. *
# `{backend}`: Either `webkit` or `webengine` * `{private}`: Indicates
# when private mode is enabled. * `{current_url}`: URL of the current
# web page. * `{protocol}`: Protocol (http/https/...) of the current web
# page. * `{audio}`: Indicator for audio/mute status.
# Type: FormatString
c.tabs.title.format = '{index:>02}'
c.tabs.position = "left"
c.tabs.favicons.scale = 1.1
c.tabs.indicator.padding = {"top": 0, "right": 0, "bottom": 0, "left": 0}
c.tabs.indicator.width = 0
c.tabs.padding = {"top": 2, "right": 2, "bottom": 2, "left": 2}
c.tabs.width = 35


c.url.open_base_url = True
c.zoom.default = "80%"


# URL Search Engines
c.url.searchengines = {
        "DEFAULT": "https://search.brave.com/search?q={}",
        'd': 'http://duckduckgo.com/?q={}',
        'am': 'https://amazon.in/s?k={}',
        'gh': 'http://github.com/search?q={}',
        'r': 'http://www.reddit.com/r/{}/',
        'rt': 'http://www.rottentomatoes.com/search/?search={}',
        'y': 'http://www.youtube.com/results?search_query={}',
        'g': 'https://google.com/search?q={}',
        'gdr': 'https://www.goodreads.com/search?q={}',
        'gen': 'http://libgen.li/search.php?req={}',
    }

# Default zoom level.
# Type: Perc
c.zoom.default = 75

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 247, 133, 1), stop:1 rgba(255, 197, 66, 1))'

# Setting dark mode
config.set("colors.webpage.darkmode.enabled", True)

# Bindings for normal mode
config.bind(',p', 'open -p')
# config.bind(',y', 'spawn --detach mpv "{url}"')
config.bind(',y', 'hint links spawn --detach yt-dlp "{url}"')

config.bind(',s', "config-source")

config.bind('M', 'hint links spawn ~/scripts/youtube "{hint-url}"')
config.bind('Z', 'hint links spawn alacrity -e youtube-dl {hint-url}')
config.bind('t', 'set-cmd-text -s :open -t')
config.bind('PB', 'hint links run open -p {hint-url}')
config.bind('xb', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')

# Downloads
c.downloads.position = 'bottom'
c.downloads.location.directory = "~/Downloads"
c.downloads.location.prompt = False


# Content
# sudo pacman -S python-adblock
c.content.blocking.adblock.lists = [
        'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt',
        'https://easylist.to/easylist/easylist.txt',
        'https://easylist.to/easylist/easyprivacy.txt'
    ]
c.content.blocking.method = 'both'
c.content.notifications.enabled = False
c.content.cookies.accept = 'all'
c.content.tls.certificate_errors = 'load-insecurely'
c.content.fullscreen.window = True
c.content.geolocation = 'ask'
c.content.webgl = True
c.scrolling.smooth = True


c.editor.command = ["urxvt", "-e", "nvim", "{}"]

# c.fonts.default_family = "sans-serif"
c.fonts.default_size = "8pt"
# c.fonts.contextmenu = 'Comic Sans MS'
# c.fonts.default_family = 'Comic Sans MS'



# DOWNLOAD KEYS
c.downloads.location.directory = "~/Downloads"
c.downloads.location.prompt = False
config.bind(",d", "set downloads.location.directory ~/Downloads/;; hint links download")
config.bind(",i", "set downloads.location.directory ~/Pictures/;; hint images download")


# COLORS
# Background color of the completion widget category headers.
c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #888888, stop:1 #505050)'

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = 'black'

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = 'black'

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = 'white'

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = '#333333'

# Text color of the completion widget.
c.colors.completion.fg = 'white'

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = '#e8c000'

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = '#bbbb00'

# Top border color of the completion widget category headers.
c.colors.completion.item.selected.border.top = '#bbbb00'

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = 'black'

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = '#ff4444'

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = '#444444'

# Color of the scrollbar in completion view
c.colors.completion.scrollbar.bg = '#333333'

# Color of the scrollbar handle in completion view.
c.colors.completion.scrollbar.fg = 'white'

# Background color for the download bar.
c.colors.downloads.bar.bg = 'black'

# Background color for downloads with errors.
c.colors.downloads.error.bg = 'red'

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = 'white'

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = '#0000aa'

# Color gradient start for download text.
c.colors.downloads.start.fg = 'white'

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = '#00aa00'

# Color gradient end for download text.
c.colors.downloads.stop.fg = 'white'

# Color gradient interpolation system for download backgrounds.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'rgb'

# Color gradient interpolation system for download text.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.fg = 'rgb'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = 'rgba(0,0,0,128)'

# Font color for hints.
c.colors.hints.fg = 'white'

# Font color for the matched part of hints.
c.colors.hints.match.fg = 'rgba(0,0,0,128)'

# Background color of the keyhint widget.
c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'

# Text color for the keyhint widget.
c.colors.keyhint.fg = '#FFFFFF'

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = '#FFFF00'

# Background color of an error message.
c.colors.messages.error.bg = 'red'

# Border color of an error message.
c.colors.messages.error.border = '#bb0000'

# Foreground color of an error message.
c.colors.messages.error.fg = 'white'

# Background color of an info message.
c.colors.messages.info.bg = 'black'

# Border color of an info message.
c.colors.messages.info.border = '#333333'

# Foreground color an info message.
c.colors.messages.info.fg = 'white'

# Background color of a warning message.
c.colors.messages.warning.bg = 'darkorange'

# Border color of a warning message.
c.colors.messages.warning.border = '#d47300'

# Foreground color a warning message.
c.colors.messages.warning.fg = 'white'

# Background color for prompts.
c.colors.prompts.bg = '#444444'

# Border used around UI elements in prompts.
c.colors.prompts.border = '1px solid gray'

# Foreground color for prompts.
c.colors.prompts.fg = 'white'

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = 'grey'

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = 'purple'

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = 'white'

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = '#a12dff'

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = 'white'

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = 'black'

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = 'white'

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = 'black'

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = 'white'

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = 'darkgreen'

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = 'white'

# Background color of the statusbar.
c.colors.statusbar.normal.bg = 'black'

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = 'white'

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = '#666666'

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = 'white'

# Background color of the progress bar.
c.colors.statusbar.progress.bg = 'white'

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = 'orange'

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = 'white'

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = 'aqua'

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = 'white'

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = 'lime'

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = 'yellow'

# Background color of the tab bar.
c.colors.tabs.bar.bg =  'black' #  '#555555'

# Background color of unselected even tabs.
c.colors.tabs.even.bg = 'darkgrey'

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = 'white'

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = '#ff0000'

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = '#0000aa'

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = '#00aa00'

# Color gradient interpolation system for the tab indicator.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'rgb'

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = 'grey'

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = 'white'

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = 'black'

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = 'white'

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = 'black'

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = 'grey'

# Background color for webpages if unset (or empty to use the theme's
# color)
c.colors.webpage.bg = 'white'
