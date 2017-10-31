class JS:

    @staticmethod
    def width():
        js_width = 'return document.getElementById("lst-ib").offsetWidth;'
        return js_width

    @staticmethod
    def high_scroll():
        js_scroll = 'return window.screen.height;'
        return js_scroll

    @staticmethod
    def high():
        js_high = 'return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight, ' \
                  ' document.body.offsetHeight, document.documentElement.offsetHeight,  document.body.clientHeight,' \
                  ' document.documentElement.clientHeight);'
        return js_high

    @staticmethod
    def delete_cursor():
        js_readonly = 'return document.getElementById("lst-ib").readOnly = true;'
        return js_readonly

    @staticmethod
    def wait_page():
        js_wait_page = 'return document.readyState;'
        return js_wait_page