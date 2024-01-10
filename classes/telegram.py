from .conn import Connection
import requests

class Telegram:
    """Send messages via Telegram with python.
    
    Methods
    -------
    send_text : message, str
        send a plain text message.
        
    send_html : message, str
        send a html formatted message
        
    send_md : message, str
        send a markdown formatted message
        
    send_md2 : message, str
        send a morkdownV2 formatted message"""

    def __init__(self):
        self.conn = Connection()
        self.TOKEN = self.conn.TELEGRAM_TOKEN
        self.CHAT_ID = self.conn.TELEGRAM_CHAT_ID
    
    def send_text(self, message:str) -> bool:
        """
        Send a plain text message.
        
        Parameters
        ----------
        message : str
            plain text message
            
        Returns
        -------
        bool"""

        url = f"https://api.telegram.org/bot{self.TOKEN}/sendMessage?chat_id={self.CHAT_ID}&text={message}"
        r = requests.get(url).json()
        if r["ok"]:
            return True
        else:
            print("message could not be sent")
            print(r)
            return False
    
    def send_html(self, message:str) -> bool:
        """
        Send a html formatted text message.
        
        i.e.: A text in <b>HTML</b>.
        Read More --> https://core.telegram.org/bots/api#html-style
        
        Parameters
        ----------
        message : str
            html formatted text message
        
        Returns
        -------
        bool"""
        
        url = f"https://api.telegram.org/bot{self.TOKEN}/sendMessage?chat_id={self.CHAT_ID}&parse_mode=HTML&text={message}"
        r = requests.get(url).json()
        if r["ok"]:
            return True
        else:
            print("message could not be sent")
            return False
    
    def send_md(self, message:str) -> bool:
        """
        Send a markdown formatted text message.
        
        i.e.: A text in *markdown*.
        Read More --> https://core.telegram.org/bots/api#markdown-style
        
        Parameters
        ----------
        message : str
            markdown formatted text message
        
        Returns
        -------
        bool"""

        url = f"https://api.telegram.org/bot{self.TOKEN}/sendMessage?chat_id={self.CHAT_ID}&parse_mode=Markdown&text={message}"
        r = requests.get(url).json()
        if r["ok"]:
            return True
        else:
            print("message could not be sent")
            return False
    
    def send_md2(self, message:str) -> bool:
        """
        Send a markdownV2 formatted text message.
        
        i.e.: A text in *markdownV2*.
        Read More --> https://core.telegram.org/bots/api#markdownv2-style
        
        Parameters
        ----------
        message : str
            markdown formatted text message
        
        Returns
        -------
        bool"""
        url = f"https://api.telegram.org/bot{self.TOKEN}/sendMessage?chat_id={self.CHAT_ID}&parse_mode=MarkdownV2&text={message}"
        r = requests.get(url).json()
        if r["ok"]:
            return True
        else:
            print("message could not be sent")
            return False