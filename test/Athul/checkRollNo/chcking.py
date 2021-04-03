brsc = Barcodedata    #Brsc holds the entire data scanned by barcode scanner 
ans = True
#since I don't know the form of data we are going to recieve through the barcode scanner lets be abstract for the time being 

if brsc.barCodeType != 'Code 128':
     ans = False

#roll nos are from is in the form of 1602-yy-BRN-RNO 
# yy - year; BRN - branch id; RNO - roll number

rollno=brsc.data.split('-')
#splits roll no to list for easier checking

known = [ 1602, [20,19,18,17], [ 732, 733, 734, 735, 736, 737 ] ]
#The inital data...or the range in which the data should be

for i in range(4):
    if i == 3 :
        if rollno[i] < 0 or rollno[i] > 180:
            ans = False
            break
    if ans == False :
        break
    if rollno[i] not in known[i]:
        ans = False

if ( ans == False  ):
    #rerun the barcode
    #return ans 
    # if ans is true
    # proceed for check distance function
