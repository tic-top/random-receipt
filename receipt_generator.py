from random_address import real_random_address
import random
import string
import uuid
from datetime import datetime, timedelta
from random_words import RandomWords

SEP_LIST = ["*"*20,"-"*20,"="*20,"."*20,"'"*20,'"'*20]
BEGIN = ["****COPY****"]
ENDING = ["****Thank you. Please Come Again****","Goods Sold ARE NOT Returnable & Refundable","Thank you for your purchase!","We appreciate your business!","Hope to see you again soon!","Thank you for shopping with us!","Have a great day!","Visit us again for more great deals!","Thank you for choosing our store!","We look forward to serving you again!","Your satisfaction is our priority!","Thank you! Come back soon!","Thank you for your support!","We hope you enjoyed your shopping experience!","Your business means a lot to us!","Thank you for being a valued customer!","We hope to see you again!","Thank you for stopping by!","We appreciate your patronage!","Come back and see us again!","Thanks for choosing us!","We hope to see you again soon!","Thank you for your continued support!","We value your feedback!","Thank you for your loyalty!","Your satisfaction is important to us!","We are grateful for your business!","Thank you for shopping here!","We hope you enjoyed your visit!","Looking forward to your next visit!","Thank you for being a loyal customer!","We appreciate your visit!","Thank you! Have a wonderful day!","Come back soon for more great products!","We value your business!","Thank you for your trust!","We hope you found what you were looking for!","Thank you for your purchase! See you next time!","Thank you for your order!","We appreciate your custom!","Have a great day and come back soon!","Thank you for being part of our community!","We look forward to serving you again soon!","Thank you! We hope to see you again!","We appreciate your visit and your business!","Thank you for choosing us!","Thank you for your purchase and support!","We hope you had a great shopping experience!","Thank you for your visit and come back soon!","Thank you for being a great customer!","We appreciate your business and your loyalty!","Thank you! We value your feedback!","Have a great day and thank you for visiting!","We hope to see you again soon! Thank you!","Thank you for your business! Have a great day!","Thank you for your visit! We hope to see you again!","Thank you for shopping with us! Have a wonderful day!","We appreciate your support! Thank you!","Thank you for being a valued customer! See you soon!","Thank you for your loyalty and support!","We hope you enjoyed your visit! Come back soon!","Thank you for your business! We appreciate it!","We value your patronage! Thank you!","Thank you for your visit! Have a great day!","We look forward to seeing you again! Thank you!","Thank you for choosing us! Have a great day!","Thank you for your support! We appreciate it!","We hope you had a great experience! Thank you!","Thank you for your trust and business!","We appreciate your custom! Come back soon!","Thank you for shopping with us! See you next time!","We hope you found everything you needed! Thank you!","Thank you for being a loyal customer! Come back soon!","We appreciate your visit and your support!","Thank you for your purchase! Have a wonderful day!","We look forward to serving you again! Thank you!","Thank you for your visit! We hope to see you again soon!","We appreciate your business! Thank you!","Thank you for your support and loyalty!","We hope you had a pleasant shopping experience! Thank you!","Thank you for shopping here! Have a great day!","We value your business and your feedback! Thank you!","Thank you for choosing our store! Have a great day!","We appreciate your visit! Thank you!","Thank you for your business! See you again soon!","We hope you had a great shopping experience! Thank you!","Thank you for your support! We look forward to your next visit!","Thank you for your loyalty and your business!","We appreciate your custom and your feedback! Thank you!","Thank you for shopping with us! Come back soon!","We hope to see you again soon! Thank you for your visit!","Thank you for your purchase! Have a great day!","We value your business and your support! Thank you!","Thank you for choosing our store! See you next time!","We appreciate your business and your loyalty! Thank you!"]
MAIL_END=['ucdavis.edu','cornell.edu','emory.edu','uw.edu','cmu.edu','mit.edu','gatech.edu','rice.edu','indiana.edu','usc.edu','vanderbilt.edu','ucla.edu','ufl.edu','utexas.edu','northwestern.edu','brown.edu','umich.edu','duke.edu','northeastern.edu','washington.edu','columbia.edu','rpi.edu','ncsu.edu','dartmouth.edu','uiuc.edu','harvard.edu','umass.edu','psu.edu','ucsb.edu','iu.edu','wisc.edu','bc.edu','fiu.edu','osu.edu','purdue.edu','uga.edu','msu.edu','yale.edu','uci.edu','ucsd.edu','princeton.edu','berkeley.edu','nyu.edu','uchicago.edu','upenn.edu','buffalo.edu','tulane.edu','jhu.edu','stanford.edu','bu.edu','caltech.edu','illinois.edu','utah.edu','me.my','tiscali.es','hotmail.no','gmx.net','gmail.sk','yahoo.nl','mail.pt','tiscali.at','europe.com','mindspring.com','fastmail.co.uk','earthlink.net','zoho.sk','zoho.co','hotmail.ie','icloud.my','outlook.ru','aol.cz','gmx.dk','yahoo.ch','me.hu','zoho.ua','fastmail.co','hushmail.fi','outlook.jp','tiscali.gr','aol.ru','dodo.com.au','seznam.cz','tiscali.com','aol.ca','gmx.lv','mac.rs','email.de','africa.com','zoho.se','hush.ai','gmx.co','me.tr','msn.gr','tiscali.ua','hotmail.lt','hushmail.co.za','icloud.lt','gmail.ua','myrambler.ru','blueyonder.co.uk','inbox.fr','fastmail.at','zoho.be','hotmail.fi','tin.it','aol.gr','zoho.lt','mail.com.au','zoho.ro','yahoo.ca','live.co','outlook.my','rediff.ro','tiscali.ro','zoho.fi','cox.net','me.nz','fastmail.nl','yandex.se','rediff.lv','fastmail.my','aol.si','fastmail.fi','gmail.be','home.pl','aol.se','rediff.pt','mail.dk','mac.vn','poczta.eu','yandex.cz','yahoo.ua','att.net','live.ca','mac.co.za','elisanet.fi','gmx.no','rediff.gr','gmx.ie','msn.lt','aol.be','hushmail.lt','live.com.au','gmail.tr','yandex.ru','mail.cz','mail.hu','fastmail.co.za','gmx.ca','hushmail.nl','internode.on.net','aol.my','fastmail.cz','amorki.pl','icloud.tr','onet.eu','icloud.at','sfr.fr','aol.ro','hotmail.my','me.co.za','me.ie','rediff.ie','gmx.be','hotmail.ch','aon.at','t-online.de','hushmail.no','wp.eu','outlook.com.au','2com.eu','hushmail.se','icloud.is','msn.no','libero.it','bluewin.ch','fastmail.be','gmx.com','vodamail.co.za','atlas.sk','mail.co','yandex.hu','gmx.fi','inbox.sk','zoho.at','rediff.be','fastmail.es','tiscali.kr','icloud.cz','yandex.dk','scientist.com','icloud.de','me.co','autograf.eu','icloud.co','gmail.it','tiscali.pt','me.lt','mac.my','in.com','icloud.si','autograf.pl','hushmail.pl','rediff.hu','hushmail.sk','outlook.lv','icloud.uk','lycos.com','email.com','fastmail.com','nm.ru','inbox.nl','icloud.es','hotmail.kr','yahoo.fi','gmx.pl','hushmail.ie','me.at','gmx.hu','onet.pl','virgilio.it','yandex.co.za','hushmail.ua','wp.pl','gazeta.pl','mac.se','volny.cz','rediff.jp','hushmail.fr','mail.lt','inode.at','apollo.lv','inbox.fi','suomi24.fi','icloud.jp','gmx.my','outlook.si','yahoo.uk','mac.com.au','mail.no','outlook.it','opera.com','zoho.dk','yahoo.lt','icloud.ru','hushmail.nz','gmail.fi','chello.eu','zoho.gr','yahoo.eu','tiscali.my','yahoo.no','rediff.com.au','zoho.ie','outlook.dk','aol.ua','front.ru','aol.tr','outlook.rs','outlook.no','gmail.pl','yandex.nl','gmx.es','gmx.is','aol.fr','yandex.be','gmail.jp','icloud.no','outlook.is','fastmail.sk','aol.de','hushmail.ro','usa.net','zoho.cz','zoho.de','techie.com','tiscali.it','me.pl','rediff.at','list.ru','yahoo.pl','me.gr','inbox.co.za','usa.com','yahoo.lv','gmx.si','prokonto.eu','yahoo.ru','tiscali.vn','yahoo.my','neostrada.eu','mail.at','accountant.com','int.eu','icloud.ie','rediff.fr','mail.my','tiscali.si','live.co.uk','inbox.gr','gazeta.eu','tiscali.lv','rediff.si','msn.sk','fastmail.com.au','me.com','hushmail.tr','yandex.no','bigpond.com','bellsouth.net','fastmail.ro','hushmail.kr','orange.net','hushmail.co.uk','gmx.sk','msn.is','rbcmail.ru','live.fr','gmx.cz','rambler.ru','mail.nz','zoho.no','zonnet.nl','me.ua','yandex.co.uk','ntlworld.com','gmx.vn','gmail.lt','zoho.com.au','inbox.ie','tiscali.jp','mac.lt','mail.uk','alice.de','op.eu','fastmail.kr','gmx.pt','centrum.sk','freenet.de','rediff.my','mail.rs','inbox.se','gmail.ie','mac.sk','protonmail.com','interia.eu','centrum.cz','gmx.ru','hotmail.tr','care2.com','gmx.uk','hotmail.de','tlen.eu','yahoo.com.au','zoho.com','msn.si','mac.nz','inbox.co.uk','sbcglobal.net','gmail.vn','o2.pl','gmail.se','gmx.se','lenta.ru','outlook.kr','fastmail.lv','yahoo.co.jp','gmx.fr','fastmail.pt','gmx.co.za','me.es','yahoo.ie','gmx.rs','aol.jp','hotmail.ua','rediff.uk','yandex.co','inbox.pt','fastmail.is','socialworker.net','hotmail.co','fastmail.hu','vp.pl','icloud.hu','rediff.is','zoho.lv','hushmail.lv','icloud.co.uk','aol.hu','tiscali.uk','verizon.net','icloud.ca','neuf.fr','aol.ie','icloud.nl','gmail.uk','yandex.tr','zoho.pl','outlook.ua','gmx.kr','musician.org','numericable.fr','tiscali.ru','mac.fr','tiscali.fi','aol.sk','live.co.za','mac.hu','yandex.si','fastmail.gr','tiscali.sk','icloud.kr','qq.com','engineer.com','icloud.lv','me.fi','zoho.nz','live.com','inbox.pl','mac.pt','zoho.co.za','me.cz','zoznam.sk','mail.ie','outlook.com','hotmail.es','inbox.at','icloud.rs','voila.fr','hotmail.nz','inbox.nz','fastwebnet.it','yahoo.co.za','fastmail.ru','hotmail.uk','icloud.ua','hotmail.vn','icloud.co.za','mail.kr','yahoo.vn','hotmail.rs','outlook.tr','me.vn','interia.pl','aol.eu','tiscali.se','angelfire.com','icloud.it','msn.cz','tiscali.be','mac.si','msn.vn','o2.eu','optonline.net','mail.ua','rediff.ua','hushmail.com.au','aol.vn','swissonline.ch','yandex.sk','tiscali.is','msn.pt','post.cz','aol.co.uk','yahoo.kr','aol.it','icloud.gr','hotmail.sk','mac.lv','zoho.my','free.fr','hushmail.dk','yahoo.tr','yandex.vn','gmail.rs','yandex.es','inbox.tr','yahoo.com','post.com','yandex.is','mail.pl','hushmail.si','outlook.at','fastmail.tr','zoho.kr','rediff.lt','op.pl','yandex.fi','aol.co.za','tiscali.hu','frontier.com','hushmail.es','zoho.si','rediff.tr','home.eu','outlook.uk','icloud.sk','gmail.at','zoho.is','yandex.uk','outlook.nz','me.ro','yahoo.rs','hotmail.si','aol.nl','mail.si','hotmail.pt','rediff.cz','poczta.fm','yahoo.be','mac.uk','2com.pl','gmail.is','bredband.net','yandex.jp','protonmail.co','rediff.kr','tiscali.rs','tiscali.no','hushmail.at','rediff.nz','me.kr','protonmail.com.au','hotmail.lv','icloud.fr','aol.es','windstream.net','gmx.jp','inbox.my','hispeed.ch','zoho.jp','me.uk','webmail.co.za','fastmail.fr','zoho.fr','gmail.pt','hushmail.be','mac.ua','msn.jp','hotmail.cz','tlen.pl','alice.it','gmail.co','freeserve.co.uk','inbox.ru','zoho.ca','me.si','virgin.net','inbox.si','gmail.com','hotmail.be','telia.com','tiscali.nl','hotmail.se','mail.com','gmx.co.uk','optusnet.com.au','zoho.es','hushmail.co','zoho.it','me.pt','hushmail.com','hushmail.my','zoho.tr','aol.at','hotmail.fr','gmail.eu','inbox.uk','gmx.ro','vp.eu','gmx.com.au','me.sk','msn.fi','me.se','icloud.com.au','outlook.co.za','live.ch','msn.lv','aol.no','hotmail.nl','msn.at','gmail.kr','gmail.nz','inbox.jp','msn.tr','lawyer.com','cfl.rr.com','inbox.ua','mail.ca','hotmail.com','mail.es','yandex.com.au','yandex.fr','yahoo.se','yahoo.it','outlook.de','yandex.ie','mail.jp','msn.se','hotmail.jp','mac.ro','excite.com','hotmail.eu','gmail.nl','mac.jp','icloud.fi','gmx.nz','fastmail.pl','aol.fi','msn.es','yahoo.hu','mail.se','orange.pl','me.ru','me.nl','aol.dk','yandex.my','rediff.vn','outlook.lt','hotmail.at','hotmail.pl','aol.pt','comcast.net','mail.gr','rediff.rs','internet.ru','me.no','me.dk','orange.fr','aliceadsl.fr','icloud.pt','sunrise.ch','msn.ru','me.is','hushmail.ca','msn.dk','rediff.dk','yandex.at','msn.my','mail.sk','msn.com.au','fastmail.uk','yandex.ca','gmail.lv','mac.ru','yahoo.jp','msn.ro','mac.gr','swipnet.se','icloud.se','amorki.eu','me.fr','quick.cz','rediff.sk','outlook.es','gmx.ua','gmail.no','yandex.pl','teacher.com','msn.be','gmx.at','hotmail.com.au','zoho.vn','atlas.cz','mac.dk','int.pl','mac.ie','me.be','me.rs','freenet.ru','icloud.ro','fastmail.jp','icloud.nz','outlook.hu','chello.at','outlook.cz','fastmail.rs','yandex.lt','protonmail.de','zoho.rs','hotmail.hu','aol.uk','yahoo.nz','yahoo.sk','inbox.kr','gmail.hu','fastmail.si','yahoo.es','mac.co','tiscali.co.uk','rediff.se','aol.is','yandex.com','rediff.pl','aol.lt','msn.kr','zoho.co.uk','hushmail.cz','me.jp','mail.co.za','iinet.net.au','mail.fr','mac.be','hotmail.gr','inbox.co','msn.ie','gmx.tr','hotmail.co.uk','orange.eu','mac.at','zoho.uk','online.de','inbox.ro','tiscali.tr','mac.no','hushmail.jp','posteo.de','msn.hu','web.de','tiscali.pl','gmx.de','rediff.co','icloud.be','yahoo.at','tiscali.nz','hetnet.nl','hushmail.gr','inbox.ca','msn.fr','yahoo.ro','tiscali.ie','mail.co.uk','aol.co','msn.rs','outlook.vn','hotmail.ro','mail.ru','rediff.no','aol.pl','outlook.ro','gmx.ch','gmx.nl','yahoo.dk','yahoo.cz','pisem.net','ro.ru','yahoo.co.uk','yandex.nz','mail.is','outlook.fr','inbox.hu','laposte.net','inbox.cz','kpnmail.nl','icloud.pl','aol.lv','msn.pl','outlook.se','inbox.dk','tiscali.fr','yandex.kr','outlook.sk','saunalahti.fi','icloud.dk','yahoo.pt','hushmail.vn','inbox.be','gmail.ru','inbox.vn','mweb.co.za','inbox.es','tiscali.co','mac.es','outlook.nl','yahoo.co','email.cz','mail.tr','yahoo.si','rediff.es','rediff.nl','fastmail.se','hotmail.it','outlook.ch','outlook.be','fastmail.ie','hushmail.hu','icloud.com','mail.nl','zoho.pt','tut.by','yandex.rs','yandex.pt','hushmail.uk','yandex.gr','gmail.ro','yahoo.is','bk.ru','dr.com','mail.lv','mac.cz','hushmail.ru','inbox.com','qip.ru','prokonto.pl','aol.com.au','skynet.be','me.lv','telenet.be','aol.kr','charter.net','msn.nz','outlook.co','inbox.rs','msn.uk','yahoo.gr','ilebi.com','hushmail.is','totalise.co.uk','gmail.dk','cs.com','consultant.com','outlook.ie','fastmail.ca','mac.kr','tiscali.cz','rediff.ru','yahoo.fr','mail.be','mail.ro','bigfoot.com','mac.nl','tiscali.dk','asia.com','hushmail.rs','inbox.is','netscape.net','neostrada.pl','gmx.lt','msn.co.za','aol.nz','rediff.fi','zoho.ru','zoho.nl','gmx.gr','bbox.fr','gmail.si','protonmail.ch','hushmail.pt','msn.nl','outlook.pt','mac.fi','outlook.fi','aol.rs','hotmail.dk','icloud.vn','outlook.pl','rediff.co.za','fastmail.ua','msn.co','inbox.lt','me.com.au','gmail.my','yahoo.co.in','mail.vn','chello.pl','email.it','inbox.no','gmail.es','yandex.ro','hotmail.is','mac.is','hotmail.ru','fastmail.vn','fastmail.nz','gmail.gr','inbox.lv','rediffmail.com','fastmail.lt','gmail.cz','fastmail.dk','westnet.com.au','zoho.hu','mac.tr','mail.fi','fastmail.no','outlook.gr','mac.pl','autorambler.ru','msn.ua','tiscali.lt','live.cz','yandex.lv','yandex.ua','aol.com','inbox.com.au']

class receipt_json_generator:
    """
    pip install RandomWords
    pip install random-address
    """
    def __init__(self) -> None:
        self.rw = RandomWords()
    def random_email(self):
        prefix_length = random.randint(5, 10)
        prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=prefix_length))
        
        return prefix + '@' + random.choice(MAIL_END)
    def random_phone(self):
        country_code = random.choice(['+1', '+86'])  # Choose country code randomly
        if country_code == '+1':  # US phone number
            area_code = random.randint(100, 999)
            exchange_code = random.randint(100, 999)
            subscriber_number = random.randint(1000, 9999)
            phone_number = f"{country_code} ({area_code}) {exchange_code}-{subscriber_number}"
        elif country_code == '+86':  # Chinese phone number
            area_code = random.choice(['10', '21', '29', '20', '22'])  # Sample area codes
            subscriber_number = ''.join(random.choices('0123456789', k=8))  # 8-digit subscriber number
            phone_number = f"{country_code} {area_code} {subscriber_number}"
        else:
            # Add more elif branches for other countries as needed
            phone_number = "Unknown country code"
        return phone_number
    def random_fax(self):
        area_code = random.randint(100, 999)  # Generate a random 3-digit area code
        first_three_digits = random.randint(100, 999)  # Generate a random 3-digit number
        last_four_digits = random.randint(1000, 9999)  # Generate a random 4-digit number
        
        fax_number = f"{area_code}-{first_three_digits}-{last_four_digits}"
        return fax_number
    def random_date(self):
        # Define a range of dates you want to generate between
        start_date = datetime(1900, 1, 1)
        end_date = datetime(2024, 12, 31)

        # Generate a random datetime between start_date and end_date
        random_datetime = start_date + \
            timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
        # Return the random date as a string in a suitable format (e.g., "YYYY-MM-DD")
        return random_datetime.strftime("%Y-%m-%d")
    def random_visa_number(self):
        # Generate a random 15-digit number (excluding the check digit)
        partial_card_number = ''.join(random.choices('0123456789', k=15))
        
        # Calculate the check digit using Luhn algorithm
        check_digit = self._calculate_luhn_check_digit('4' + partial_card_number)
        
        # Concatenate the partial card number and the check digit
        visa_number = '4' + partial_card_number + str(check_digit)
        
        return visa_number
    def _calculate_luhn_check_digit(self, card_number):
        # Reverse the card number and convert it to integers
        digits = [int(digit) for digit in str(card_number)][::-1]
        
        # Double every second digit
        doubled_digits = [(digit * 2) if idx % 2 == 1 else digit for idx, digit in enumerate(digits)]
        
        # Subtract 9 from any results that are greater than 9
        subtracted_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]
        
        # Calculate the sum of all digits
        sum_digits = sum(subtracted_digits)
        
        # Find the check digit that makes the sum a multiple of 10
        check_digit = (10 - (sum_digits % 10)) % 10
        
        return check_digit
    def random_time(self):
        random_hour = random.randint(0, 23)
        random_minute = random.randint(0, 59)
        random_second = random.randint(0, 59)
        random_datetime = datetime.now().replace(hour=random_hour, minute=random_minute, second=random_second)
        return random_datetime.strftime("%H:%M:%S")
    def random_sep(self):
        return random.choice(SEP_LIST)
    def random_item(self, num=2):
        return ' '.join(self.rw.random_words(count=num))
    def random_address(self):
        return real_random_address()
    def random_small_item_price(self):
        price = round(random.uniform(1, 100), 2)
        return price
    def random_large_item_price(self):
        price = round(random.uniform(1000, 100000))
        return price

    def invoice_number(self):
        # 使用UUID生成唯一的发票号码
        unique_id = uuid.uuid4().hex[:8].upper()
        # 使用当前日期
        date_str = self.random_date().replace("-",'')
        # 组合日期和唯一ID作为发票号码
        invoice_num = f"{date_str}-{unique_id}"
        k = random.randint(10,15)
        return invoice_num[-k:]

    def random_cart(self):
        # item_name/desription, (qty), price/rm/dolloar(货币单位), amount/
        unit = random.choice(["RM", "Dollar", "Yuan", "Pound", "Euro", "Rupee", "Yen", "Won", "Franc", "Krone", "Real", "Peso", "Lira", "Ruble", "Baht", "Dinar", "Dirham", "Rial", "Pula", "Kwacha", "Leu", "Lev", "Forint", "Kuna", "Koruna", "Zloty", "Rand", "Ringgit", "Riyal", "Rupiah", "Shekel"])
        num_of_item = random.randint(1, 20)
        cart = []
        large_item = random.choice([True, False])
        total = 0
        for _ in range(num_of_item):
            item = self.random_item()
            qty = random.randint(1, 10)
            if large_item:
                price= self.random_large_item_price()
            else:
                price= self.random_small_item_price()
            amount = qty * price
            total += amount
            cart.append((item, qty, price, amount))
        # tax ratio
        ratio = random.randint(0,20)
        tax = total * ratio / 100.0
        return {
            "unit": unit,
            "items": cart,
            "large_item": large_item,
            "Total Exclude GST": total,
            f"Total GST @{ratio}%": tax,
            "Total Inclusive GST": total+tax,
            "Round Amt": total+tax
        }

    def __call__(self):
        cart = self.random_cart()
        date = self.random_date()
        object = {
            "name": self.random_item(3),
            "Address": self.random_address(),
            "ROC NO": self.invoice_number(),
            "Invoice No": self.invoice_number(),
            "Company Reg No": self.invoice_number(),
            "GST Reg No": self.invoice_number(),
            "TEL": self.random_phone(),
            "fax": self.random_fax(),
            "email": self.random_email(),
            "date": date,
            "cashier": self.random_item(3),
            "Sales Persor": self.random_item(1),
            "Bill To": self.random_item(3),
            "cart": cart,
            "Approval Code": random.randint(100, 999),
            "VISA CARD": self.random_visa_number(),
            "ending": random.choice(ENDING),
            "sep": self.random_sep()
        }
        return object

class receipt_image_generator:
    



if __name__ == "__main__":
    rec = receipt_json_generator()
    print(rec())

