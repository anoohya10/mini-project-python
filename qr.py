import pyqrcode
import png
def qrcode():
    q=pyqrcode.create(input())
    q.png("qrcode.png",scale=5)
    print('QR generated')
if __name__=='__main__':
    qrcode()