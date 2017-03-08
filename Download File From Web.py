from urllib import request

pdf_url='http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv'

def downloadPdf(url):
    response=request.urlopen(url)   #Store the connection to the webpage url in response
    pdf=response.read()            #read from response and store the text in pdf variable
    pdf_str=str(pdf)               #convert data read from url to string

    lines=pdf_str.split('\\n')
    dest_url=r'Saved File.txt'
    fx=open(dest_url,'w')
    for a in lines:
        fx.write(a+'\n')
    fx.close()

downloadPdf(pdf_url)
