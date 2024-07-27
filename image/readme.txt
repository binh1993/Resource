									GamingSync Network 
										 Presents
						DDTank 3.0 English server files, with 3.1/3.2 items
								 Friday, June 29th, 2012
								 
								 
-----------------
Table of Contents
-----------------
1. Introduction
2. Features
3. Friendly Notes
4. Credits

---------------
1. Introduction
---------------

Hello everyone, this is Keith from RaGEZONE.
I just wanted to release this to the public, because me and some friends worked very hard on it.
But because of lack of time, and interest I am now releasing this to you...I have added notes on how to get the latest items and english translations.
I hope you enjoy the server files, and such.

-----------
2. Features
-----------

1. 98% translated files, including item shop, interface, and quests.
*Note: mob translations are not done, I got tired of working on them, but they are half way done, you can continue if you want. Some buttons are not translated and just the normal stuff I did not want to pick through at the time.
2. All functions work..it seems anyway, if there is a bug, well sorry, you got fix it.
3. Databases are optimized and truncated, and secured. This gives you the opportunity to start right off with a fresh database with no conflicts, and no extra SQL users. (Except mine, which you can delete)
4. You will need to get a fresh copy of the wwwroot from the default install, I was working on customizing mine and well too lazy to restore original.

-----------------
3. Friendly Notes
-----------------

If you want to get more translations, all I can say is, look at the official server config.xml, Hint: (http://res6.ddt.game321.com/flash/) and request Resources from them, aka for example Request/TemplateAllist.xml contains the item names and descriptions and stats (you can add custom items this way).
The database does not pull any information to the server, so what off servers do is insert content into the database.
Then run the associated aspx file in /Request/ then it generates the .xml. You can do a simple .html file and do <a href="http://website.com/Request/xmlfilehere.xml">Download</a>, right click it and save link. 
This is how we were able to get the English names and latest items easily..along with the images.
* I was able to pull the SWF files from the server using an addon for Firefox (I cannot remember the name but it has something to do with swf, just google it or search for it)

----------
4. Credits
----------

Keith (http://forum.ragezone.com/members/73484.html)
ADMZePekeno (http://forum.ragezone.com/members/1333387678.html) 
Original releaser: welington (http://forum.ragezone.com/members/1333340439.html) 
Topic: http://forum.ragezone.com/f111/ddtank-3-0-server-client-847354/
		