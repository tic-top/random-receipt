import random
import string
import uuid
import fitz
from io import BytesIO
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
from datetime import datetime, timedelta
from random_words import RandomWords
from random_address import real_random_address

def get_color():
    bgg_list = [(0.3984375 , 0.23046875, 0.09765625)]
    bgg_color = random.choice(bgg_list)
    bg_list = [(0.6484375 , 0.6796875 , 0.69140625),
                (0.9296875 , 0.89453125, 0.875     ),
                (0.76171875, 0.76953125, 0.765625  ),
                (1,1,1)]
    background_color = random.choice(bg_list)
    # background_color = bg_list[-1]
    tx_list  = [(0.650, 0.65, 0.65), (0,0,0)]
    text_color = random.choice(tx_list)

    background_color = (1, 1, 1)
    text_color = (0,0,0)
    return background_color, text_color, bgg_color

def blur(img, box: tuple):
    blurred_image = img.filter(ImageFilter.GaussianBlur(10))
    img.paste(blurred_image.crop(box), box)
    return img

import random

def dark(img, degree = 0):
    def upward_gradient_func(y):
        return int(degree * (y / img.height))
    def downward_gradient_func(y):
        return int(degree * (1 - y / img.height))
    def leftward_gradient_func(x):
        return int(degree * (x / img.width))
    def rightward_gradient_func(x):
        return int(degree * (1 - x / img.width))

    direction = random.choice(["horizontal", "vertical"])
    if direction == "horizontal":
        gradient = Image.new('L', (img.width, 1), color=0xFF)
        gradient_func = random.choice([leftward_gradient_func, rightward_gradient_func])
        for x in range(img.width):
            gradient.putpixel((x, 0), gradient_func(x))
    else:    
        # Create a gradient that will darken the image from top to bottom
        gradient = Image.new('L', (1, img.height), color=0xFF)
        gradient_func = random.choice([upward_gradient_func, downward_gradient_func])
        for y in range(img.height):
            gradient.putpixel((0, y), gradient_func(y))

    # Resize the gradient to match the width of the image
    alpha = gradient.resize(img.size)

    # Convert the image to 'RGBA' to add the alpha channel
    img = img.convert('RGBA')

    # Create a black image the same size as the original
    black_image = Image.new('RGBA', img.size, color=(0, 0, 0, 255))

    # Composite the images together using the alpha mask
    darkened_image = Image.composite(black_image, img, alpha)
    
    return darkened_image

width_constant, height_constant = 0.5560000283377511, 1.3739991869245256
BASE_FONTNAME = fitz.Base14_fontdict.keys()
BASE_FONTNAME = [
    "courier",
    "courier-oblique",
    "courier-bold",
    "courier-boldoblique",
    "helvetica",
    "helvetica-oblique",
    "helvetica-bold",
    "helvetica-boldoblique",
    "times-roman",
    "times-italic",
    "times-bold",
    "helv",
    "heit",
    "hebo",
    "hebi",
]
BASE_FONTNAME = ["courier"]
SEP_LIST = [r"*", r"-", r"=", r".", r"'", r'"']
SEP_LIST = [r"-"]
BEGIN = ["****COPY****"]
ENDING = [
    "Goods Sold Only Exchangeable Within 1 Days",
    "Goods Sold Only Exchangeable Within 2 Days",
    "Goods Sold Only Exchangeable Within 3 Days",
    "Goods Sold Only Exchangeable Within 4 Days",
    "Goods Sold Only Exchangeable Within 5 Days",
    "Goods Sold Only Exchangeable Within 6 Days",
    "Goods Sold Only Exchangeable Within 7 Days",
    "****Thank you. Please Come Again****",
    "Goods Sold ARE NOT Returnable & Refundable",
    "Thank you for your purchase!",
    "We appreciate your business!",
    "Hope to see you again soon!",
    "Thank you for shopping with us!",
    "Have a great day!",
    "Visit us again for more great deals!",
    "Thank you for choosing our store!",
    "We look forward to serving you again!",
    "Your satisfaction is our priority!",
    "Thank you! Come back soon!",
    "Thank you for your support!",
    "We hope you enjoyed your shopping experience!",
    "Your business means a lot to us!",
    "Thank you for being a valued customer!",
    "We hope to see you again!",
    "Thank you for stopping by!",
    "We appreciate your patronage!",
    "Come back and see us again!",
    "Thanks for choosing us!",
    "We hope to see you again soon!",
    "Thank you for your continued support!",
    "We value your feedback!",
    "Thank you for your loyalty!",
    "Your satisfaction is important to us!",
    "We are grateful for your business!",
    "Thank you for shopping here!",
    "We hope you enjoyed your visit!",
    "Looking forward to your next visit!",
    "Thank you for being a loyal customer!",
    "We appreciate your visit!",
    "Thank you! Have a wonderful day!",
    "Come back soon for more great products!",
    "We value your business!",
    "Thank you for your trust!",
    "We hope you found what you were looking for!",
    "Thank you for your purchase! See you next time!",
    "Thank you for your order!",
    "We appreciate your custom!",
    "Have a great day and come back soon!",
    "Thank you for being part of our community!",
    "We look forward to serving you again soon!",
    "Thank you! We hope to see you again!",
    "We appreciate your visit and your business!",
    "Thank you for choosing us!",
    "Thank you for your purchase and support!",
    "We hope you had a great shopping experience!",
    "Thank you for your visit and come back soon!",
    "Thank you for being a great customer!",
    "We appreciate your business and your loyalty!",
    "Thank you! We value your feedback!",
    "Have a great day and thank you for visiting!",
    "We hope to see you again soon! Thank you!",
    "Thank you for your business! Have a great day!",
    "Thank you for your visit! We hope to see you again!",
    "Thank you for shopping with us! Have a wonderful day!",
    "We appreciate your support! Thank you!",
    "Thank you for being a valued customer! See you soon!",
    "Thank you for your loyalty and support!",
    "We hope you enjoyed your visit! Come back soon!",
    "Thank you for your business! We appreciate it!",
    "We value your patronage! Thank you!",
    "Thank you for your visit! Have a great day!",
    "We look forward to seeing you again! Thank you!",
    "Thank you for choosing us! Have a great day!",
    "Thank you for your support! We appreciate it!",
    "We hope you had a great experience! Thank you!",
    "Thank you for your trust and business!",
    "We appreciate your custom! Come back soon!",
    "Thank you for shopping with us! See you next time!",
    "We hope you found everything you needed! Thank you!",
    "Thank you for being a loyal customer! Come back soon!",
    "We appreciate your visit and your support!",
    "Thank you for your purchase! Have a wonderful day!",
    "We look forward to serving you again! Thank you!",
    "Thank you for your visit! We hope to see you again soon!",
    "We appreciate your business! Thank you!",
    "Thank you for your support and loyalty!",
    "We hope you had a pleasant shopping experience! Thank you!",
    "Thank you for shopping here! Have a great day!",
    "We value your business and your feedback! Thank you!",
    "Thank you for choosing our store! Have a great day!",
    "We appreciate your visit! Thank you!",
    "Thank you for your business! See you again soon!",
    "We hope you had a great shopping experience! Thank you!",
    "Thank you for your support! We look forward to your next visit!",
    "Thank you for your loyalty and your business!",
    "We appreciate your custom and your feedback! Thank you!",
    "Thank you for shopping with us! Come back soon!",
    "We hope to see you again soon! Thank you for your visit!",
    "Thank you for your purchase! Have a great day!",
    "We value your business and your support! Thank you!",
    "Thank you for choosing our store! See you next time!",
    "We appreciate your business and your loyalty! Thank you!",
]
MAIL_END = [
    "ucdavis.edu",
    "cornell.edu",
    "emory.edu",
    "uw.edu",
    "cmu.edu",
    "mit.edu",
    "gatech.edu",
    "rice.edu",
    "indiana.edu",
    "usc.edu",
    "vanderbilt.edu",
    "ucla.edu",
    "ufl.edu",
    "utexas.edu",
    "northwestern.edu",
    "brown.edu",
    "umich.edu",
    "duke.edu",
    "northeastern.edu",
    "washington.edu",
    "columbia.edu",
    "rpi.edu",
    "ncsu.edu",
    "dartmouth.edu",
    "uiuc.edu",
    "harvard.edu",
    "umass.edu",
    "psu.edu",
    "ucsb.edu",
    "iu.edu",
    "wisc.edu",
    "bc.edu",
    "fiu.edu",
    "osu.edu",
    "purdue.edu",
    "uga.edu",
    "msu.edu",
    "yale.edu",
    "uci.edu",
    "ucsd.edu",
    "princeton.edu",
    "berkeley.edu",
    "nyu.edu",
    "uchicago.edu",
    "upenn.edu",
    "buffalo.edu",
    "tulane.edu",
    "jhu.edu",
    "stanford.edu",
    "bu.edu",
    "caltech.edu",
    "illinois.edu",
    "utah.edu",
    "me.my",
    "tiscali.es",
    "hotmail.no",
    "gmx.net",
    "gmail.sk",
    "yahoo.nl",
    "mail.pt",
    "tiscali.at",
    "europe.com",
    "mindspring.com",
    "fastmail.co.uk",
    "earthlink.net",
    "zoho.sk",
    "zoho.co",
    "hotmail.ie",
    "icloud.my",
    "outlook.ru",
    "aol.cz",
    "gmx.dk",
    "yahoo.ch",
    "me.hu",
    "zoho.ua",
    "fastmail.co",
    "hushmail.fi",
    "outlook.jp",
    "tiscali.gr",
    "aol.ru",
    "dodo.com.au",
    "seznam.cz",
    "tiscali.com",
    "aol.ca",
    "gmx.lv",
    "mac.rs",
    "email.de",
    "africa.com",
    "zoho.se",
    "hush.ai",
    "gmx.co",
    "me.tr",
    "msn.gr",
    "tiscali.ua",
    "hotmail.lt",
    "hushmail.co.za",
    "icloud.lt",
    "gmail.ua",
    "myrambler.ru",
    "blueyonder.co.uk",
    "inbox.fr",
    "fastmail.at",
    "zoho.be",
    "hotmail.fi",
    "tin.it",
    "aol.gr",
    "zoho.lt",
    "mail.com.au",
    "zoho.ro",
    "yahoo.ca",
    "live.co",
    "outlook.my",
    "rediff.ro",
    "tiscali.ro",
    "zoho.fi",
    "cox.net",
    "me.nz",
    "fastmail.nl",
    "yandex.se",
    "rediff.lv",
    "fastmail.my",
    "aol.si",
    "fastmail.fi",
    "gmail.be",
    "home.pl",
    "aol.se",
    "rediff.pt",
    "mail.dk",
    "mac.vn",
    "poczta.eu",
    "yandex.cz",
    "yahoo.ua",
    "att.net",
    "live.ca",
    "mac.co.za",
    "elisanet.fi",
    "gmx.no",
    "rediff.gr",
    "gmx.ie",
    "msn.lt",
    "aol.be",
    "hushmail.lt",
    "live.com.au",
    "gmail.tr",
    "yandex.ru",
    "mail.cz",
    "mail.hu",
    "fastmail.co.za",
    "gmx.ca",
    "hushmail.nl",
    "internode.on.net",
    "aol.my",
    "fastmail.cz",
    "amorki.pl",
    "icloud.tr",
    "onet.eu",
    "icloud.at",
    "sfr.fr",
    "aol.ro",
    "hotmail.my",
    "me.co.za",
    "me.ie",
    "rediff.ie",
    "gmx.be",
    "hotmail.ch",
    "aon.at",
    "t-online.de",
    "hushmail.no",
    "wp.eu",
    "outlook.com.au",
    "2com.eu",
    "hushmail.se",
    "icloud.is",
    "msn.no",
    "libero.it",
    "bluewin.ch",
    "fastmail.be",
    "gmx.com",
    "vodamail.co.za",
    "atlas.sk",
    "mail.co",
    "yandex.hu",
    "gmx.fi",
    "inbox.sk",
    "zoho.at",
    "rediff.be",
    "fastmail.es",
    "tiscali.kr",
    "icloud.cz",
    "yandex.dk",
    "scientist.com",
    "icloud.de",
    "me.co",
    "autograf.eu",
    "icloud.co",
    "gmail.it",
    "tiscali.pt",
    "me.lt",
    "mac.my",
    "in.com",
    "icloud.si",
    "autograf.pl",
    "hushmail.pl",
    "rediff.hu",
    "hushmail.sk",
    "outlook.lv",
    "icloud.uk",
    "lycos.com",
    "email.com",
    "fastmail.com",
    "nm.ru",
    "inbox.nl",
    "icloud.es",
    "hotmail.kr",
    "yahoo.fi",
    "gmx.pl",
    "hushmail.ie",
    "me.at",
    "gmx.hu",
    "onet.pl",
    "virgilio.it",
    "yandex.co.za",
    "hushmail.ua",
    "wp.pl",
    "gazeta.pl",
    "mac.se",
    "volny.cz",
    "rediff.jp",
    "hushmail.fr",
    "mail.lt",
    "inode.at",
    "apollo.lv",
    "inbox.fi",
    "suomi24.fi",
    "icloud.jp",
    "gmx.my",
    "outlook.si",
    "yahoo.uk",
    "mac.com.au",
    "mail.no",
    "outlook.it",
    "opera.com",
    "zoho.dk",
    "yahoo.lt",
    "icloud.ru",
    "hushmail.nz",
    "gmail.fi",
    "chello.eu",
    "zoho.gr",
    "yahoo.eu",
    "tiscali.my",
    "yahoo.no",
    "rediff.com.au",
    "zoho.ie",
    "outlook.dk",
    "aol.ua",
    "front.ru",
    "aol.tr",
    "outlook.rs",
    "outlook.no",
    "gmail.pl",
    "yandex.nl",
    "gmx.es",
    "gmx.is",
    "aol.fr",
    "yandex.be",
    "gmail.jp",
    "icloud.no",
    "outlook.is",
    "fastmail.sk",
    "aol.de",
    "hushmail.ro",
    "usa.net",
    "zoho.cz",
    "zoho.de",
    "techie.com",
    "tiscali.it",
    "me.pl",
    "rediff.at",
    "list.ru",
    "yahoo.pl",
    "me.gr",
    "inbox.co.za",
    "usa.com",
    "yahoo.lv",
    "gmx.si",
    "prokonto.eu",
    "yahoo.ru",
    "tiscali.vn",
    "yahoo.my",
    "neostrada.eu",
    "mail.at",
    "accountant.com",
    "int.eu",
    "icloud.ie",
    "rediff.fr",
    "mail.my",
    "tiscali.si",
    "live.co.uk",
    "inbox.gr",
    "gazeta.eu",
    "tiscali.lv",
    "rediff.si",
    "msn.sk",
    "fastmail.com.au",
    "me.com",
    "hushmail.tr",
    "yandex.no",
    "bigpond.com",
    "bellsouth.net",
    "fastmail.ro",
    "hushmail.kr",
    "orange.net",
    "hushmail.co.uk",
    "gmx.sk",
    "msn.is",
    "rbcmail.ru",
    "live.fr",
    "gmx.cz",
    "rambler.ru",
    "mail.nz",
    "zoho.no",
    "zonnet.nl",
    "me.ua",
    "yandex.co.uk",
    "ntlworld.com",
    "gmx.vn",
    "gmail.lt",
    "zoho.com.au",
    "inbox.ie",
    "tiscali.jp",
    "mac.lt",
    "mail.uk",
    "alice.de",
    "op.eu",
    "fastmail.kr",
    "gmx.pt",
    "centrum.sk",
    "freenet.de",
    "rediff.my",
    "mail.rs",
    "inbox.se",
    "gmail.ie",
    "mac.sk",
    "protonmail.com",
    "interia.eu",
    "centrum.cz",
    "gmx.ru",
    "hotmail.tr",
    "care2.com",
    "gmx.uk",
    "hotmail.de",
    "tlen.eu",
    "yahoo.com.au",
    "zoho.com",
    "msn.si",
    "mac.nz",
    "inbox.co.uk",
    "sbcglobal.net",
    "gmail.vn",
    "o2.pl",
    "gmail.se",
    "gmx.se",
    "lenta.ru",
    "outlook.kr",
    "fastmail.lv",
    "yahoo.co.jp",
    "gmx.fr",
    "fastmail.pt",
    "gmx.co.za",
    "me.es",
    "yahoo.ie",
    "gmx.rs",
    "aol.jp",
    "hotmail.ua",
    "rediff.uk",
    "yandex.co",
    "inbox.pt",
    "fastmail.is",
    "socialworker.net",
    "hotmail.co",
    "fastmail.hu",
    "vp.pl",
    "icloud.hu",
    "rediff.is",
    "zoho.lv",
    "hushmail.lv",
    "icloud.co.uk",
    "aol.hu",
    "tiscali.uk",
    "verizon.net",
    "icloud.ca",
    "neuf.fr",
    "aol.ie",
    "icloud.nl",
    "gmail.uk",
    "yandex.tr",
    "zoho.pl",
    "outlook.ua",
    "gmx.kr",
    "musician.org",
    "numericable.fr",
    "tiscali.ru",
    "mac.fr",
    "tiscali.fi",
    "aol.sk",
    "live.co.za",
    "mac.hu",
    "yandex.si",
    "fastmail.gr",
    "tiscali.sk",
    "icloud.kr",
    "qq.com",
    "engineer.com",
    "icloud.lv",
    "me.fi",
    "zoho.nz",
    "live.com",
    "inbox.pl",
    "mac.pt",
    "zoho.co.za",
    "me.cz",
    "zoznam.sk",
    "mail.ie",
    "outlook.com",
    "hotmail.es",
    "inbox.at",
    "icloud.rs",
    "voila.fr",
    "hotmail.nz",
    "inbox.nz",
    "fastwebnet.it",
    "yahoo.co.za",
    "fastmail.ru",
    "hotmail.uk",
    "icloud.ua",
    "hotmail.vn",
    "icloud.co.za",
    "mail.kr",
    "yahoo.vn",
    "hotmail.rs",
    "outlook.tr",
    "me.vn",
    "interia.pl",
    "aol.eu",
    "tiscali.se",
    "angelfire.com",
    "icloud.it",
    "msn.cz",
    "tiscali.be",
    "mac.si",
    "msn.vn",
    "o2.eu",
    "optonline.net",
    "mail.ua",
    "rediff.ua",
    "hushmail.com.au",
    "aol.vn",
    "swissonline.ch",
    "yandex.sk",
    "tiscali.is",
    "msn.pt",
    "post.cz",
    "aol.co.uk",
    "yahoo.kr",
    "aol.it",
    "icloud.gr",
    "hotmail.sk",
    "mac.lv",
    "zoho.my",
    "free.fr",
    "hushmail.dk",
    "yahoo.tr",
    "yandex.vn",
    "gmail.rs",
    "yandex.es",
    "inbox.tr",
    "yahoo.com",
    "post.com",
    "yandex.is",
    "mail.pl",
    "hushmail.si",
    "outlook.at",
    "fastmail.tr",
    "zoho.kr",
    "rediff.lt",
    "op.pl",
    "yandex.fi",
    "aol.co.za",
    "tiscali.hu",
    "frontier.com",
    "hushmail.es",
    "zoho.si",
    "rediff.tr",
    "home.eu",
    "outlook.uk",
    "icloud.sk",
    "gmail.at",
    "zoho.is",
    "yandex.uk",
    "outlook.nz",
    "me.ro",
    "yahoo.rs",
    "hotmail.si",
    "aol.nl",
    "mail.si",
    "hotmail.pt",
    "rediff.cz",
    "poczta.fm",
    "yahoo.be",
    "mac.uk",
    "2com.pl",
    "gmail.is",
    "bredband.net",
    "yandex.jp",
    "protonmail.co",
    "rediff.kr",
    "tiscali.rs",
    "tiscali.no",
    "hushmail.at",
    "rediff.nz",
    "me.kr",
    "protonmail.com.au",
    "hotmail.lv",
    "icloud.fr",
    "aol.es",
    "windstream.net",
    "gmx.jp",
    "inbox.my",
    "hispeed.ch",
    "zoho.jp",
    "me.uk",
    "webmail.co.za",
    "fastmail.fr",
    "zoho.fr",
    "gmail.pt",
    "hushmail.be",
    "mac.ua",
    "msn.jp",
    "hotmail.cz",
    "tlen.pl",
    "alice.it",
    "gmail.co",
    "freeserve.co.uk",
    "inbox.ru",
    "zoho.ca",
    "me.si",
    "virgin.net",
    "inbox.si",
    "gmail.com",
    "hotmail.be",
    "telia.com",
    "tiscali.nl",
    "hotmail.se",
    "mail.com",
    "gmx.co.uk",
    "optusnet.com.au",
    "zoho.es",
    "hushmail.co",
    "zoho.it",
    "me.pt",
    "hushmail.com",
    "hushmail.my",
    "zoho.tr",
    "aol.at",
    "hotmail.fr",
    "gmail.eu",
    "inbox.uk",
    "gmx.ro",
    "vp.eu",
    "gmx.com.au",
    "me.sk",
    "msn.fi",
    "me.se",
    "icloud.com.au",
    "outlook.co.za",
    "live.ch",
    "msn.lv",
    "aol.no",
    "hotmail.nl",
    "msn.at",
    "gmail.kr",
    "gmail.nz",
    "inbox.jp",
    "msn.tr",
    "lawyer.com",
    "cfl.rr.com",
    "inbox.ua",
    "mail.ca",
    "hotmail.com",
    "mail.es",
    "yandex.com.au",
    "yandex.fr",
    "yahoo.se",
    "yahoo.it",
    "outlook.de",
    "yandex.ie",
    "mail.jp",
    "msn.se",
    "hotmail.jp",
    "mac.ro",
    "excite.com",
    "hotmail.eu",
    "gmail.nl",
    "mac.jp",
    "icloud.fi",
    "gmx.nz",
    "fastmail.pl",
    "aol.fi",
    "msn.es",
    "yahoo.hu",
    "mail.se",
    "orange.pl",
    "me.ru",
    "me.nl",
    "aol.dk",
    "yandex.my",
    "rediff.vn",
    "outlook.lt",
    "hotmail.at",
    "hotmail.pl",
    "aol.pt",
    "comcast.net",
    "mail.gr",
    "rediff.rs",
    "internet.ru",
    "me.no",
    "me.dk",
    "orange.fr",
    "aliceadsl.fr",
    "icloud.pt",
    "sunrise.ch",
    "msn.ru",
    "me.is",
    "hushmail.ca",
    "msn.dk",
    "rediff.dk",
    "yandex.at",
    "msn.my",
    "mail.sk",
    "msn.com.au",
    "fastmail.uk",
    "yandex.ca",
    "gmail.lv",
    "mac.ru",
    "yahoo.jp",
    "msn.ro",
    "mac.gr",
    "swipnet.se",
    "icloud.se",
    "amorki.eu",
    "me.fr",
    "quick.cz",
    "rediff.sk",
    "outlook.es",
    "gmx.ua",
    "gmail.no",
    "yandex.pl",
    "teacher.com",
    "msn.be",
    "gmx.at",
    "hotmail.com.au",
    "zoho.vn",
    "atlas.cz",
    "mac.dk",
    "int.pl",
    "mac.ie",
    "me.be",
    "me.rs",
    "freenet.ru",
    "icloud.ro",
    "fastmail.jp",
    "icloud.nz",
    "outlook.hu",
    "chello.at",
    "outlook.cz",
    "fastmail.rs",
    "yandex.lt",
    "protonmail.de",
    "zoho.rs",
    "hotmail.hu",
    "aol.uk",
    "yahoo.nz",
    "yahoo.sk",
    "inbox.kr",
    "gmail.hu",
    "fastmail.si",
    "yahoo.es",
    "mac.co",
    "tiscali.co.uk",
    "rediff.se",
    "aol.is",
    "yandex.com",
    "rediff.pl",
    "aol.lt",
    "msn.kr",
    "zoho.co.uk",
    "hushmail.cz",
    "me.jp",
    "mail.co.za",
    "iinet.net.au",
    "mail.fr",
    "mac.be",
    "hotmail.gr",
    "inbox.co",
    "msn.ie",
    "gmx.tr",
    "hotmail.co.uk",
    "orange.eu",
    "mac.at",
    "zoho.uk",
    "online.de",
    "inbox.ro",
    "tiscali.tr",
    "mac.no",
    "hushmail.jp",
    "posteo.de",
    "msn.hu",
    "web.de",
    "tiscali.pl",
    "gmx.de",
    "rediff.co",
    "icloud.be",
    "yahoo.at",
    "tiscali.nz",
    "hetnet.nl",
    "hushmail.gr",
    "inbox.ca",
    "msn.fr",
    "yahoo.ro",
    "tiscali.ie",
    "mail.co.uk",
    "aol.co",
    "msn.rs",
    "outlook.vn",
    "hotmail.ro",
    "mail.ru",
    "rediff.no",
    "aol.pl",
    "outlook.ro",
    "gmx.ch",
    "gmx.nl",
    "yahoo.dk",
    "yahoo.cz",
    "pisem.net",
    "ro.ru",
    "yahoo.co.uk",
    "yandex.nz",
    "mail.is",
    "outlook.fr",
    "inbox.hu",
    "laposte.net",
    "inbox.cz",
    "kpnmail.nl",
    "icloud.pl",
    "aol.lv",
    "msn.pl",
    "outlook.se",
    "inbox.dk",
    "tiscali.fr",
    "yandex.kr",
    "outlook.sk",
    "saunalahti.fi",
    "icloud.dk",
    "yahoo.pt",
    "hushmail.vn",
    "inbox.be",
    "gmail.ru",
    "inbox.vn",
    "mweb.co.za",
    "inbox.es",
    "tiscali.co",
    "mac.es",
    "outlook.nl",
    "yahoo.co",
    "email.cz",
    "mail.tr",
    "yahoo.si",
    "rediff.es",
    "rediff.nl",
    "fastmail.se",
    "hotmail.it",
    "outlook.ch",
    "outlook.be",
    "fastmail.ie",
    "hushmail.hu",
    "icloud.com",
    "mail.nl",
    "zoho.pt",
    "tut.by",
    "yandex.rs",
    "yandex.pt",
    "hushmail.uk",
    "yandex.gr",
    "gmail.ro",
    "yahoo.is",
    "bk.ru",
    "dr.com",
    "mail.lv",
    "mac.cz",
    "hushmail.ru",
    "inbox.com",
    "qip.ru",
    "prokonto.pl",
    "aol.com.au",
    "skynet.be",
    "me.lv",
    "telenet.be",
    "aol.kr",
    "charter.net",
    "msn.nz",
    "outlook.co",
    "inbox.rs",
    "msn.uk",
    "yahoo.gr",
    "ilebi.com",
    "hushmail.is",
    "totalise.co.uk",
    "gmail.dk",
    "cs.com",
    "consultant.com",
    "outlook.ie",
    "fastmail.ca",
    "mac.kr",
    "tiscali.cz",
    "rediff.ru",
    "yahoo.fr",
    "mail.be",
    "mail.ro",
    "bigfoot.com",
    "mac.nl",
    "tiscali.dk",
    "asia.com",
    "hushmail.rs",
    "inbox.is",
    "netscape.net",
    "neostrada.pl",
    "gmx.lt",
    "msn.co.za",
    "aol.nz",
    "rediff.fi",
    "zoho.ru",
    "zoho.nl",
    "gmx.gr",
    "bbox.fr",
    "gmail.si",
    "protonmail.ch",
    "hushmail.pt",
    "msn.nl",
    "outlook.pt",
    "mac.fi",
    "outlook.fi",
    "aol.rs",
    "hotmail.dk",
    "icloud.vn",
    "outlook.pl",
    "rediff.co.za",
    "fastmail.ua",
    "msn.co",
    "inbox.lt",
    "me.com.au",
    "gmail.my",
    "yahoo.co.in",
    "mail.vn",
    "chello.pl",
    "email.it",
    "inbox.no",
    "gmail.es",
    "yandex.ro",
    "hotmail.is",
    "mac.is",
    "hotmail.ru",
    "fastmail.vn",
    "fastmail.nz",
    "gmail.gr",
    "inbox.lv",
    "rediffmail.com",
    "fastmail.lt",
    "gmail.cz",
    "fastmail.dk",
    "westnet.com.au",
    "zoho.hu",
    "mac.tr",
    "mail.fi",
    "fastmail.no",
    "outlook.gr",
    "mac.pl",
    "autorambler.ru",
    "msn.ua",
    "tiscali.lt",
    "live.cz",
    "yandex.lv",
    "yandex.ua",
    "aol.com",
    "inbox.com.au",
]
UNITS = [
    "RM",
    "Dollar",
    "Yuan",
    "Pound",
    "Euro",
    "Rupee",
    "Yen",
    "Won",
    "Franc",
    "Krone",
    "Real",
    "Peso",
    "Lira",
    "Ruble",
    "Baht",
    "Dinar",
    "Dirham",
    "Rial",
    "Pula",
    "Kwacha",
    "Leu",
    "Lev",
    "Forint",
    "Kuna",
    "Koruna",
    "Zloty",
    "Rand",
    "Ringgit",
    "Riyal",
    "Rupiah",
    "Shekel",
]


class ReceiptJsonGenerator:
    """
    pip install RandomWords
    pip install random-address
    """

    def __init__(self) -> None:
        self.rw = RandomWords()

    def random_email(self):
        prefix_length = random.randint(5, 10)
        prefix = "".join(
            random.choices(
                string.ascii_letters.lower() + string.digits, k=prefix_length
            )
        )
        return prefix + "@" + random.choice(MAIL_END)

    def random_phone(self):
        country_code = random.choice(["+1", "+86"])  # Choose country code randomly
        if country_code == "+1":  # US phone number
            area_code = random.randint(100, 999)
            exchange_code = random.randint(100, 999)
            subscriber_number = random.randint(1000, 9999)
            phone_number = (
                f"{country_code} ({area_code}) {exchange_code}-{subscriber_number}"
            )
        elif country_code == "+86":  # Chinese phone number
            area_code = random.choice(
                ["10", "21", "29", "20", "22"]
            )  # Sample area codes
            subscriber_number = "".join(
                random.choices("0123456789", k=8)
            )  # 8-digit subscriber number
            phone_number = f"{country_code} {area_code} {subscriber_number}"
        else:
            # Add more elif branches for other countries as needed
            phone_number = "Unknown country code"
        return phone_number

    def random_fax(self):
        area_code = random.randint(100, 999)  # Generate a random 3-digit area code
        first_three_digits = random.randint(
            100, 999
        )  # Generate a random 3-digit number
        last_four_digits = random.randint(
            1000, 9999
        )  # Generate a random 4-digit number

        fax_number = f"{area_code}-{first_three_digits}-{last_four_digits}"
        return fax_number

    def random_date(self):
        # Define a range of dates you want to generate between
        start_date = datetime(1900, 1, 1)
        end_date = datetime(2024, 12, 31)

        # Generate a random datetime between start_date and end_date
        random_datetime = start_date + timedelta(
            seconds=random.randint(0, int((end_date - start_date).total_seconds()))
        )
        # Return the random date as a string in a suitable format (e.g., "YYYY-MM-DD")
        return random_datetime.strftime("%Y/%m/%d") #-

    def random_visa_number(self):
        # Generate a random 15-digit number (excluding the check digit)
        partial_card_number = "".join(random.choices("0123456789", k=15))

        # Calculate the check digit using Luhn algorithm
        check_digit = self._calculate_luhn_check_digit("4" + partial_card_number)

        # Concatenate the partial card number and the check digit
        visa_number = "4" + partial_card_number + str(check_digit)

        return visa_number

    def _calculate_luhn_check_digit(self, card_number):
        # Reverse the card number and convert it to integers
        digits = [int(digit) for digit in str(card_number)][::-1]

        # Double every second digit
        doubled_digits = [
            (digit * 2) if idx % 2 == 1 else digit for idx, digit in enumerate(digits)
        ]

        # Subtract 9 from any results that are greater than 9
        subtracted_digits = [
            digit - 9 if digit > 9 else digit for digit in doubled_digits
        ]

        # Calculate the sum of all digits
        sum_digits = sum(subtracted_digits)

        # Find the check digit that makes the sum a multiple of 10
        check_digit = (10 - (sum_digits % 10)) % 10

        return check_digit

    def random_time(self):
        random_hour = random.randint(0, 23)
        random_minute = random.randint(0, 59)
        random_second = random.randint(0, 59)
        random_datetime = datetime.now().replace(
            hour=random_hour, minute=random_minute, second=random_second
        )
        return random_datetime.strftime("%H:%M:%S")

    def random_sep(self):
        return random.choice(SEP_LIST)

    def random_item(self, num=1):
        return " ".join(self.rw.random_words(count=num))

    def random_address(self):
        return real_random_address()

    def random_small_item_price(self):
        price = round(random.uniform(1, 5), 2)
        return price

    def random_large_item_price(self):
        price = round(random.uniform(1000, 100000))
        return price

    def invoice_number(self):
        # 使用UUID生成唯一的发票号码
        unique_id = uuid.uuid4().hex[:8].upper()
        # 使用当前日期
        date_str = self.random_date().replace("-", "")
        # 组合日期和唯一ID作为发票号码
        invoice_num = f"{date_str}-{unique_id}"
        k = random.randint(10, 15)
        return invoice_num[-k:]
    
    def random_grocery(self):
        i = random.randint(10, 100)
        j = random.randint(10, 100)
        # if random.random() > 0.5:
        #     return f"{i}x{j} {self.random_item()[:6].upper()}"
        # # make the first letter uppercase
        
        new1 =  self.random_item(2)[:12]
        new2 = self.random_item()[:3]
        new2 = f"{new1}({new2})".upper()
        new3 = self.random_item(3)[:20].upper()
        new3 = "AP-17 " + "NICR ALUBAKA AJWE ANSWER AYDEW"
        new4 = "911 TAPE DISPENSER"
        return random.choice([new3, new2, new4])

    def random_cart(self):
        unit = random.choice(UNITS)
        num_of_item = random.randint(1, 20)
        num_of_item = 9
        cart = []
        large_item = random.choice([True, False])
        large_item = False
        total = 0
        for _ in range(num_of_item):
            item = self.random_grocery()
            qty = random.randint(1, 10)
            qty = 1
            if large_item:
                price = self.random_large_item_price()
            else:
                price = self.random_small_item_price()
            amount = qty * price
            total += amount
            cart.append((item, qty, price, amount))
        
        cart = [
            ("200SHEET COMPACT SERVING(NTE)", 1, 3.30, 3.30),
            ('1.5" RUBBER BAND', 1, 3.6, 3.6),
            ("PP 3x5 04", 1, 2.5, 2.5),
            ("18MMX90Y OPP TAPE", 1, 1.6, 1.6),
            ("911 TAPE DISPENSER", 1, 8.6, 8.6),
            ("PSI-890 PENSONIC DRY IRON WITH SPRAY", 1, 49.9, 49.9),
            ("AP-17 APRON PLAIN CLOTH", 20, 10.90, 218),
            ("TALI UNTUK", 1, 1.00, 1),
            ("CC-100 100PC CITE CANDLE", 1, 22.9, 22.9),
            ("F1502 SCISSOR 08C (CH)(TLC)", 6, 6.00, 36),
            ("2KG HC KITCHEN SCALE", 1, 19.90, 19.90)
        ]
        # tax ratio
        ratio = random.randint(0, 20)
        tax = total * ratio / 100.0
        return {
            "unit": unit,
            "items": cart,
            "ratio": ratio,
            "large_item": large_item,
            "t_wo_gst": total,
            "gst": tax,
            "t_w_gst": total + tax,
        }
    def deal(self,cart):
        # randomly select deal1,2,3
        return self.deal3(cart)
        return random.choice([self.deal1, self.deal2, self.deal3])(cart)
        
    def deal2(self, cart):
        pass

    def deal3(self, cart):
        # remember we have different type of table to represent the cart
        """
        'cart': {'unit': 'Riyal',
                'items': [('schedule legs', 5, 50.94, 254.7),
                ('helmsman mint', 10, 19.38, 193.79999999999998),
                ('levels corks', 10, 71.57, 715.6999999999999),
                ('print span', 1, 97.3, 97.3),
                ('collision accountabilities', 10, 39.4, 394.0),
                ('view rescue', 2, 47.48, 94.96),
                ('tools store', 1, 28.04, 28.04),
                ('employees kilograms', 6, 49.0, 294.0),
                ('console energizers', 4, 97.64, 390.56),
                ('contacts parameter', 3, 44.48, 133.44),
                ('assemblies spacer', 2, 26.67, 53.34),
                ('shift animal', 6, 41.49, 248.94),
                ('recordkeeping preserver', 2, 5.56, 11.12),
                ('stomachs trade', 3, 53.16, 159.48),
                ('heights place', 7, 9.3, 65.10000000000001)],
                'large_item': False,
                "t_wo_gst": total,
                "gst": tax,
                "ratio": ratio,
                "t_w_gst": total + tax,
                "r_t_w_gst": total + tax,}
        """
        # item_name/desription, (qty), price, amount
        def format(price):
            if cart["large_item"]:
                return f"{price:,.0f}"
            else:
                return f"{price:,.2f}"

        op = random.choice(["x", "*", " "])
        op = "*"
        item_alias = ["Description", "Item", "Item name", "Item/Desc."]
        item_alias = ["DESC"]
        qty_alis = ["QTY"]
        price_alias = ["Price", cart["unit"]]
        amount_alias = ["Amount", "Amt."]
        it_units = ["PC", "200G"]
        bar_format = random.randint(1, 4)
        bar_format = 3

        def add_sep(lines):
            if random.random() > 0:
                return [["<SEP>"]] + lines + [["<SEP>"]]
            return lines
        # case format
        if bar_format == 1:
            lines = [
                [
                    random.choice(item_alias),
                    random.choice(qty_alis),
                    random.choice(price_alias),
                    random.choice(amount_alias),
                ]
            ]
            lines = add_sep(lines)
            for item in cart["items"]:
                lines.append([item[0], str(item[1]), format(item[2]), format(item[3])])
                lines.append(
                    ["Total Qty :", str(item[1])]
                )
        elif bar_format == 2:
            lines = [
                [
                    random.choice(item_alias),
                    random.choice(price_alias),
                    random.choice(amount_alias),
                ]
            ]
            lines = add_sep(lines)
            for item in cart["items"]:
                lines.append(
                    [
                        str(item[1]) + f" {op}  " + item[0],
                        format(item[2]),
                        format(item[3]),
                    ]
                )
        elif bar_format == 3:
            lines = [
                [
                    random.choice(item_alias),
                    "U."+random.choice(price_alias).upper(),
                    "Disc",
                    "AMOUNT ",
                    "TAX "
                ],
                [   
                    random.choice(qty_alis),
                    random.choice(price_alias),
                    "",
                    random.choice(price_alias),
                    "CODE"
                ]
            ]
            lines = add_sep(lines)
            disc = random.choice([0.0])
            for item in cart["items"]:
                discount = item[2] * disc
                lines.append([item[0]])
                # stris item[0]倒叙
                # ii = item[0][::-1]
                # lines.append([ii])
                xx = str(item[1])+f" {random.choice(it_units)}"
                lines.append([xx, op, format(item[2]), format(discount), format(item[3])+" SR"])
        
        elif bar_format == 4:
            lines = [
                [random.choice(item_alias), random.choice(amount_alias)],
            ]
            lines = add_sep(lines)
            for item in cart["items"]:
                lines.append([str(item[1])+' '+ item[0], format(item[3])])


        t_wo_gst_alis = ["Total w/o GST", "Total Exclude GST"]
        t_gst_alis = [f"Total Exclude GST @{cart['ratio']}%"]
        t_w_gst_alis = [f"Total Include GST"]
        r_t_w_gst_alis = ["Round Amt"]
        if random.random() > 0.5:
            lines.append([random.choice(t_wo_gst_alis), "", "", format(cart["t_wo_gst"])])
            lines.append([random.choice(t_gst_alis), "", "", format(cart["gst"])])
            lines.append([random.choice(t_w_gst_alis), "", "", format(cart["t_w_gst"])])
            lines.append([random.choice(r_t_w_gst_alis), "", "", format(cart["t_w_gst"])])
        
        lines.append(["TOTAL", "", format(cart["t_w_gst"])])
        # cash is the number which is closest to the total and is the multiply of 10
        cash = (round(cart["t_w_gst"] / 10)+1) * 10.0
        change = cash - cart["t_w_gst"]
        lines.append(["CASH", "", format(cash)])
        lines.append(["CHANGE", "", format(change)])
        return lines

    def __call__(self):
        cart = self.random_cart()
        date = self.random_date()
        time = self.random_time()
        if random.random() > 0.5:
            detail_time = date + " " + time
        else:
            detail_time = date
        detail_time = date + " " + time
        finish = False
        while finish == False:
            address = self.random_address()
            if "address1" in address:
                addr1 = address["address1"]
            else:
                addr1 = self.random_item(2)

            if "city" in address:
                city = address["city"]
            else:
                city = self.random_item(1)

            if "state" in address:
                state = address["state"]
            else:
                state = self.random_item(1)

            if "postalCode" in address:
                postalCode = address["postalCode"]
            else:
                postalCode = self.randomint(10000, 99999)

            address_string = [
                [addr1.upper()],
                [str(postalCode) + " " + city.upper() + ", " + state.upper()],
            ]
            address_string = [
                [""],
                ["GREAT ZONE HOUSEHOLD CENTRE SDN BHD"],
                ["(801049-U)"],
                ["60 & 62. Jalan Ciku,"],
                ['86000,KLUANG']
            ]
            finish = True
        header = [["ROC NO", ": " + str(self.invoice_number())],
                ["Invoice No", ": " + self.invoice_number()],
                ["Company Reg No", ": " + self.invoice_number()],
                ["TEL" + ": " + self.random_phone()],
                ["FAX" + ": " + self.random_fax()],
                ["Email" + ": " + self.random_email()],
                ["Date", ": " + detail_time],
                # ['Member:', ""],
                # ["Lover:", ""],
                ["Cashier", ": " + self.random_item(2).upper()],
                ["Sales Persor", ": " + self.random_item(1).upper()],
                ["Bill To", ": " + self.random_item(2).upper()]]
        # randomly choose 5 of the header
        header = random.sample(header, 5)

        header = [
            ["Document No.:", "KLG0201130227"],
            ["Date:", detail_time],
            ["Debtor:", ""],
            ['Member:', ""],
            ["Terminal:", "KLG0201"],
            ["Cashier:", "KLG2"],
        ]
        content = (
            [["Tax Invoice"]]
            + [[""]]
            # +[[self.random_item(3).upper()]]
            + address_string
            + [[""]]
            + [["GST Reg No.: 00184408280"]]
            + [["<SEP>"]]
            + header
            + self.deal(cart)
            + [["<SEP>"]]
            + [
                ["Approval Code", ": " + str(random.randint(100, 999))],
                ["VISA CARD", ": " + self.random_visa_number()],
                [random.choice(ENDING)],
            ]
        )
        # max_length
        max_len = max([len(" ".join(i)) for i in content])
        object = {
            "content": content,
            "sep": self.random_sep(),
            "max_length": max_len,
        }
        return object

class ReceiptImgGenerator:
    def __init__(self) -> None:
        self.font_type = random.choice(BASE_FONTNAME)

    def block(
        self,
        texts: list = [],
        intervals: list = None,
        height: int = 0,
        width: int = 0,
    ):
        # empty line
        if height == 0 or width == 0:
            raise ValueError("Height and width should be greater than 0.")
        if len(texts) == 0:
            raise ValueError("Texts should not be empty.")

        # check if the number of texts and intervals are the same
        if intervals is None:
            intervals = [2] + [1] * (len(texts) - 1)
        if len(texts) == 2:
            intervals = [1, 2]
        # print(texts[2])
        if len(texts) == 5 and texts[1] == '*':
            intervals = [1, 0.5, 1, 1, 1.5]
        if len(texts) == 5 and texts[1] != '*':
            intervals = [1, 1.5, 1, 1, 0.50]
        total_interval = sum(intervals)
        text_widths = [int(width * interval / total_interval) for interval in intervals]
        last_x = 0
        font_size = int(height / height_constant)
        ans = []
        for i, text in enumerate(texts):
            ans.append(
                (
                    last_x,
                    0,
                    last_x + text_widths[i],
                    height,
                    text,
                    font_size,
                    random.choice(BASE_FONTNAME)
                    # self.font_type,
                )
            )
            last_x += text_widths[i]
        return ans

    def __call__(
        self,
        rec: dict,
        min_width=404,
        max_width=404,
        min_ratio=2.05,
        max_ratio=2.05,
        min_w_edge_dist=0.07,
        max_w_edge_dist=0.07,
        min_h_edge_dist=0.01,
        max_h_edge_dist=0.05,
        base_font=11,
    ):
        # better estimation is needed
        width = random.randint(min_width, max_width)
        height = int(width * random.uniform(min_ratio, max_ratio))

        w_edge_dist = random.uniform(min_w_edge_dist, max_w_edge_dist)
        h_edge_dist = random.uniform(min_h_edge_dist, max_h_edge_dist)

        min_x = int(w_edge_dist * width)
        max_x = int((1 - w_edge_dist) * width)
        min_y = int(h_edge_dist * height)
        max_y = int((1 - h_edge_dist) * height)

        max_cols = int((max_x - min_x) / (width_constant * base_font))
        num_rows = int((max_y - min_y) / (height_constant * base_font))
        while (num_rows >= len(rec["content"])) and (rec['max_length'] <= max_cols):
            base_font += 1
            # print("Make the font larger:", base_font)
            max_cols = int((max_x - min_x) / (width_constant * base_font))
            num_rows = int((max_y - min_y) / (height_constant * base_font))
        
        base_font += 1
        print(base_font)
        base_font = 16

        doc = fitz.open()
        background_color, text_color, bgg = get_color()

        # delta_w =  random.choice([0, int(random.random()/2 * width)])
        # delta_h =  random.choice([0, int(random.random()/2 * height)])

        delta_w = delta_h = 0
        new_w = width + delta_w
        new_h = height + delta_h
        min_x = min_x + delta_w // 2
        max_x = max_x + delta_w // 2
        min_y = min_y + delta_h // 2
        max_y = max_y + delta_h // 2

        page = doc.new_page(width=new_w, height=new_h)
        # import glob, os
        # font_path = "/home/yilinjia/mycontainer/tengchao/dataset/kosmos_d/handwritten_fonts/"
        # font_files = glob.glob(os.path.join(font_path, "*.ttf"))
        # print(font_files)
        # cur_font = random.choice(font_files)
        cur_font = "/home/yilinjia/MambaOCR/SimSun.ttf"
        cur_font = "/home/yilinjia/MambaOCR/DOTMATRI.TTF"
        cur_font = "/home/yilinjia/MambaOCR/Arial.ttf"
        page.insert_font(fontfile=cur_font, fontname="F0")
        page.draw_rect(
            fitz.Rect(0, 0, new_w, new_h),
            color=bgg,
            fill=bgg,
            overlay=True,
        )
        page.draw_rect(
            fitz.Rect(delta_w//2, delta_h//2, width+delta_w//2, height+delta_h//2),
            color=background_color,
            fill=background_color,
            overlay=True,
        )

        # now add text to the image
        cnt = 0
        last_x, last_y = min_x, min_y
        sep = rec['sep']
        tmp_width = max_x - min_x
        tmp_height = 0
        print(rec["content"])
        for info in rec["content"]:
            if info ==  ["<SEP>"] or info == [""]:
                last_y = last_y - tmp_height * 0.3
            if cnt == 0:
                delta = 2
            else:
                # delta = random.uniform(1, 1.1)
                delta = 1.2
            cnt += delta
            tmp_height = int(delta * base_font * height_constant)
            blocks = self.block(info, height=tmp_height, width=tmp_width)
            align = 0
            for x0, y0, x1, y1, txt, font_size, font_name in blocks:
                rect = fitz.Rect(last_x + x0, last_y + y0, last_x + x1, last_y + y1)
                fs = font_size
                rc = -1
                if len(info) == 5:
                    align = 2
                    if info[1] != '*':
                        fs = 14
                while rc < 0 and fs > 6:
                    # width , width constant, fs
                    if '<SEP>' in txt:
                        n = int(1.5 * tmp_width / (fs * width_constant))
                        txt = sep * n
                    rc = page.insert_textbox(
                        rect,
                        txt,
                        fontsize=fs,
                        fontname="F0", #font_name,
                        align=align,
                        color=text_color,
                    )
                    # cur_font=random.choice(self.fonts)

                    fs -= 1
                print(txt)
                if rc < 0:
                    print(txt)
                
            if info ==  ["<SEP>"]:
                last_y = last_y + tmp_height * 0.5
            else:
                last_y = last_y + tmp_height * 0.9
            if last_y + tmp_height > max_y:
                break
        # crop the image to last_y
        # page.set_cropbox(fitz.Rect(0, 0, width, last_y))
        # convert to image
        pix = page.get_pixmap()
        pix_bytes = pix.tobytes(output="png")
        pix = Image.open(BytesIO(pix_bytes)).convert("RGB")

        # factor = random.uniform(0.9, 1.1)  # 调整因子范围0.5到1.5之间
        # enhancer = ImageEnhance.Brightness(pix)
        # pix = enhancer.enhance(factor)
        # extract info
        text_extract = []
        bboxs = []
        for block in page.get_text("dict")["blocks"]:
            for line in block["lines"]:
                cur_line = []
                for span in line["spans"]:
                    text = span["text"].strip()
                    if len(text) == 0:
                        continue
                    cur_line.append(text)

                if len(cur_line) == 0:
                    continue
                cur_line = " ".join(cur_line).strip()
                if len(cur_line) > 30 and cur_line[25] in SEP_LIST:
                    continue
                x0, y0, x1, y1 = (
                    line["bbox"][0] / width,
                    line["bbox"][1] / height,
                    line["bbox"][2] / width,
                    line["bbox"][3] / height,
                )
                try:
                    assert 0 <= x0 <= 1, f"x0: {x0} " + cur_line
                    assert 0 <= y0 <= 1, f"y0: {y0} " + cur_line
                    assert 0 <= x1 <= 1, f"x1: {x1} " + cur_line
                    assert 0 <= y1 <= 1, f"y1: {y1} " + cur_line
                    if len(cur_line) == 0:
                        continue
                    if random.random() < 0.01:
                        box = line["bbox"]
                        # box is a tuple, make all the things in the box be int
                        box = [int(i) for i in box]
                        pix = blur(pix,box)
                        continue
                    bboxs.append([x0, y0, x1, y1])
                    text_extract.append(cur_line)
                except Exception as e:
                    print(e)
                    # print(line["bbox"])
                    # return pix
                    
        degree = random.choice([0, 16, 32, 64])
        pix = dark(pix)
        return {
            "lines": text_extract,
            "bboxs": bboxs,
            "image": pix,
        }


if __name__ == "__main__":
    rec = ReceiptJsonGenerator()
    gen = ReceiptImgGenerator()

    rc = rec()
    receipt = gen(rc)
    img = receipt["image"]
    img.save("test.png")
    print(receipt["lines"])

    # sep don't predict
