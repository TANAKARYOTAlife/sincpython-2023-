#import
import os
import zipfile
import Sinc_Your_Book_Title

#Enter_Your_Title
Your_Title = Sinc_Your_Book_Title.Sinc_Your_Book_Title()


desktop_path = os.path.expanduser('~/Desktop')
print(os.getcwd() + '1')
print('2' + desktop_path)


def Sinc_Not_Zip_mimetype() :
    with zipfile.ZipFile( Your_Title + '.epub' , 
                        'w' ,
                        zipfile.ZIP_STORED,) as Your_Book_Not_Zip_EPUB :
        Your_Book_Not_Zip_EPUB.write('mimetype')

def Sinc_Zip_EPUB_File():
    with zipfile.ZipFile( Your_Title + '.epub' , 
                        'a' ,
                        zipfile.ZIP_DEFLATED,
                        allowZip64 = True ) as Your_Book_Zip_EPUB:
        for dirpath , dirnames , filenames in os.walk( './' ):
            Your_Book_Zip_EPUB.write(dirpath)
            for Sinz_Zip_file in filenames:
                Your_Book_Zip_EPUB.write(os.path.join(dirpath,file))

Sinc_Not_Zip_mimetype()
