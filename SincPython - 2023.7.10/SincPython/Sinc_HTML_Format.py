def Sinc_HTML_Read():
    with open( '' + '.html',
                'r',
                encoding='UTF-8') as Sinc_HTML_Format:
        Sinc_Your_Html = Sinc_HTML_Format.read()
        return Sinc_Your_Html
    
def Sinc_HTML_Write():
    with open( 'page-content' + '.html',
                'w',
                encoding='UTF-8') as Sinc_HTML_Element:
        Sinc_Your_Book_Html = Sinc_HTML_Read().format( Your_Title = '' )
        Sinc_HTML_Element.write(Sinc_Your_Book_Html)
