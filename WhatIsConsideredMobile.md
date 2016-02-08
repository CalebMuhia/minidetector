# What's Considered "mobile" #

Mobile will be true for the following things:

  * Anything using [Opera Mini](http://www.operamini.com/)
  * Anything that claims to accept [WAP](http://en.wikipedia.org/wiki/Wireless_Application_Protocol)
  * Mobile Telephones (Cellphones)
  * **Most** PDAs (I have omitted a few older ones that probably aren't on the web anyway)
  * Consoles such as the PSP, Playstation, and Wii, under the general impression that they don't handle normal web browsing very well.
  * Mobile web scrapers, such as [AvantGo](http://avantgo.com/) and [Plucker](http://plkr.org/)
  * Anything that specifically cloaks itself to look like one of the above

The following things are **not** considered mobile:

  * "Internet Tablets" such as the N700, N800 and N810, and anything using Windows XP Tablet Edition or Vista, as they tend to cope fine with most normal pages
  * Anything running standard desktop browsers
  * Links, Lynx and the like, they have their own coping mechanisms
  * Web spiders. For the moment I haven't decided to detect them, as doing so will slow down detection, the good ones respect [robots.txt](http://robotstxt.org/) anyway, and the bad ones will either be lame or cloak themselves. If enough people moan at me on an issue, then I'll consider adding it.


The full list of user agents are in [tests/mobile\_useragents.txt](http://minidetector.googlecode.com/svn/trunk/minidetector/tests/mobile_useragents.txt) and [tests/other\_useragents.txt](http://minidetector.googlecode.com/svn/trunk/minidetector/tests/other_useragents.txt) and they are tested as part of the full test suite.

The latest version of this code is always being run on http://AmIOnACellphone.com/ - feel free to check there from a browser to see if it is correctly detected.

If you've found a user agent that works incorrectly, please [raise an issue,](http://code.google.com/p/minidetector/issues/list) and I'll review it to see if I can get the app to work with it.