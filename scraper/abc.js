0 ["[data-gallery-role=gallery-placeholder]"]["mage/gallery/gallery"]["data"]
    {

        
        "[data-gallery-role=gallery-placeholder]": {
            "mage/gallery/gallery": {
                "mixins":["magnifier/magnify"],
                "magnifierOpts": {"fullscreenzoom":"5","top":"","left":"","width":"","height":"","eventType":"hover","enabled":false},
                "data": [{"thumb":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/6360e336b2a70951114dbd37294096ee\/f\/1\/f18m30303_1_.jpg","img":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/9d08971813a040f8f96067a40f75c615\/f\/1\/f18m30303_1_.jpg","full":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/74c1057f7991b4edb2bc7bdaa94de933\/f\/1\/f18m30303_1_.jpg","caption":"F18M30303 | Beige | CAMBRIC","position":"1","isMain":true,"type":"image","videoUrl":null},
                {"thumb":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/6360e336b2a70951114dbd37294096ee\/f\/1\/f18m30303_3_.jpg","img":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/9d08971813a040f8f96067a40f75c615\/f\/1\/f18m30303_3_.jpg","full":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/74c1057f7991b4edb2bc7bdaa94de933\/f\/1\/f18m30303_3_.jpg","caption":"F18M30303 | Beige | CAMBRIC","position":"2","isMain":false,"type":"image","videoUrl":null},
                {"thumb":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/6360e336b2a70951114dbd37294096ee\/f\/1\/f18m30303_2_.jpg","img":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/9d08971813a040f8f96067a40f75c615\/f\/1\/f18m30303_2_.jpg","full":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/74c1057f7991b4edb2bc7bdaa94de933\/f\/1\/f18m30303_2_.jpg","caption":"F18M30303 | Beige | CAMBRIC","position":"3","isMain":false,"type":"image","videoUrl":null},
                {"thumb":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/6360e336b2a70951114dbd37294096ee\/f\/1\/f18m30303_4_.jpg","img":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/9d08971813a040f8f96067a40f75c615\/f\/1\/f18m30303_4_.jpg","full":"https:\/\/www.zellbury.com\/media\/catalog\/product\/cache\/74c1057f7991b4edb2bc7bdaa94de933\/f\/1\/f18m30303_4_.jpg","caption":"F18M30303 | Beige | CAMBRIC","position":"4","isMain":false,"type":"image","videoUrl":null}],
                "options": {
                    "nav": "thumbs",
                    "loop": 1,
                    "keyboard": 1,
                    "arrows": 1,
                    "allowfullscreen": false,
                    "showCaption": 0,
                    "width": 467,
                    "thumbwidth": 75,
                    "thumbheight": 112.41970021413,
                                        "height": 700,
                                        "transitionduration": 500,
                    "transition": "slide",
                    "navarrows": 1,
                    "navtype": "slides",
                    "navdir": "vertical"
                },
                "fullscreen": {
                    "nav": "thumbs",
                    "loop": 1,
                    "navdir": "horizontal",
                    "arrows": 0,
                    "showCaption": 0,
                    "transitionduration": 500,
                    "transition": "dissolve"
                },
                "breakpoints": {"mobile":{"conditions":{"max-width":"767px"},"options":{"options":{"nav":"dots"}}}}            }
        }
    }
Traceback (most recent call last):
  File "C:\Users\Alizar\Documents\GitHub\FYP\scraper\Zellbury1.py", line 194, in <module>

<class 'bs4.element.Tag'>
    khadiS()
  File "C:\Users\Alizar\Documents\GitHub\FYP\scraper\Zellbury1.py", line 182, in khadiS
    main(url)
  File "C:\Users\Alizar\Documents\GitHub\FYP\scraper\Zellbury1.py", line 128, in main
    k = getRawText(i)
  File "C:\Users\Alizar\Documents\GitHub\FYP\scraper\Zellbury1.py", line 38, in getRawText
    c= c.find('div', class_ = "fotorama__wrap fotorama__wrap--css3 fotorama__wrap--slide fotorama__wrap--toggle-arrows fotorama__wrap--no-controls")
AttributeError: 'NoneType' object has no attribute 'find'
[Finished in 8.1s with exit code 1]
[shell_cmd: python -u "C:\Users\Alizar\Documents\GitHub\FYP\scraper\Zellbury1.py"]
[dir: C:\Users\Alizar\Documents\GitHub\FYP\scraper]
[path: C:\Program Files\Microsoft MPI\Bin\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\Program Files\nodejs\;C:\Program Files\Git\cmd;C:\Program Files\dotnet\;C:\Program Files (x86)\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\;C:\Program Files (x86)\Microsoft SQL Server\140\Tools\Binn\;C:\Program Files (x86)\Microsoft SQL Server\140\DTS\Binn\;C:\Program Files (x86)\Microsoft SQL Server\140\Tools\Binn\ManagementStudio\;C:\Program Files (x86)\QuickTime\QTSystem\;C:\Program Files (x86)\IVI Foundation\VISA\WinNT\Bin\;C:\Program Files\IVI Foundation\VISA\Win64\Bin\;C:\Program Files (x86)\IVI Foundation\VISA\WinNT\Bin;C:\Program Files\Microsoft SQL Server\140\Tools\Binn\;C:\Program Files\Microsoft SQL Server\140\DTS\Binn\;C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\MATLAB\R2011b\runtime\win64;C:\Program Files\MATLAB\R2011b\bin;C:\Users\Alizar\.cargo\bin;C:\Users\Alizar\AppData\Local\Programs\Python\Python35-32\Scripts\;C:\Users\Alizar\AppData\Local\Programs\Python\Python35-32\;C:\Users\Alizar\AppData\Local\Microsoft\WindowsApps;C:\Program Files\heroku\bin;C:\Users\Alizar\AppData\Roaming\npm;C:\modeltech_6.5c\win32;C:\Users\Alizar\AppData\Local\Programs\Microsoft VS Code\bin;]