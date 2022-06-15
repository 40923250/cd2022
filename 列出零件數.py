import NXOpen
   
def main():
    # 取得目前開啟的工作階段
    theSession = NXOpen.Session.GetSession()
    # 建立 ListingWindow
    listWin= theSession.ListingWindow
    # 開啟零件檔案
    try:
        basePart1 = theSession.Parts.OpenBaseDisplay("Y:/mdecycu/cd2022_guide/downloads/cd2022_uarm/uArmSwiftPro_UP1300_3D_assembly.prt")
    except:
        # 零件已經開啟
        pass
     
    # 開啟 Listing Window
    listWin.Open()
    # 將已經開啟的零件對應至 displayPart
    displayPart = theSession.Parts.Display
    # 計算引用零件數目
    partNumber = 0
    # 存放個別零件名稱的數列
    partList = []
    # 利用組立組件的根組件 GetChildren 方法逐一列出各子組件的名稱
    for child in displayPart.ComponentAssembly.RootComponent.GetChildren():
        listWin.WriteLine(child.DisplayName)
        # 個別零件數列不計入重複引用的零件
        if child.DisplayName not in partList:
            partList.append(child.DisplayName)
        # 引用零件數累計
        partNumber += 1
    # 在 Listing Window 中列出相關資訊
    listWin.WriteLine("總共引用 " + str(partNumber) + " 個子零件.")
    listWin.WriteLine("其中個別零件總數為" + str(len(partList)))
                             
if __name__ == "__main__":
    main()