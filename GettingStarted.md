# Using Microdetector Middleware #

Using microdetector is very simple. Simply place the microdetector package into your project's path, and then add:

`microdetector.Middleware`

to your `MIDDLEWARE_CLASSES` tuple in your settings.py

Then in your view you can check `request.mobile` - if it's `True` then treat it like a small screen device. If it's `False` then it's probably a desktop browser, or a spider or something else.

# Not using the Middleware #

If you only have certain views that need the distinction, you can choose not to search every request you receive. All you need to do is wrap the relevant views like this:

```
from microdetector import detect_mobile

@detect_mobile
def my_mobile_view(request):
    if request.mobile:
        #do something with mobile
```