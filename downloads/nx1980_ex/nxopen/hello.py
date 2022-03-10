# NX 11.0.2.7
# Journal created by UGPerson for use on NX Journaling
#Python Version 3.4
 
 
import NXOpen
 
 
def main() :
 
 
 
    theSession  = NXOpen.Session.GetSession()#: :type theSession: NXOpen.Session
    workPart = theSession.Parts.Work#: :type workPart: NXOpen.BasePart
    displayPart = theSession.Parts.Display#: :type displayPart: NXOpen.BasePart
    lw = theSession.ListingWindow#: :type lw: NXOpen.ListingWindow
 
 
    lw.Open()
    lw.WriteLine("Hello World")
 
 
if __name__ == '__main__':
    main()