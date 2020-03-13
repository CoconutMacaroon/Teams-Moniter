import Xlib.display
display = Xlib.display.Display()
window = display.get_input_focus().focus
wmname = window.get_wm_name()
wmclass = window.get_wm_class()
if wmclass is None and wmname is None:
    window = window.query_tree().parent
    wmname = window.get_wm_name()
print "WM Name: %s" % ( wmname, )