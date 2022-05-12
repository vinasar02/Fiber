
class Login:
    login_usrname = 'username'
    login_pass = 'password'
    login_button = '//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/form/div[3]/button'

class Dashboard:
    decline = '/html/body/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/h5'
    progress ='//*[@id="main-content"]/div[2]/div[2]/div[2]/div/div/div/div[2]'
    inspection = '//*[@id="main-content"]/div[2]/div[2]/div[3]/div/div/div/div[2]'
    submitted = '//*[@id="main-content"]/div[2]/div[2]/div[4]/div/div/div/div[2]'
    unassigned = '//*[@id="main-content"]/div[2]/div[2]/div[5]/div/div/div/div[2]'
    fibercut  = '//*[@id="main-content"]/div[2]/div[2]/div[6]/div/div/div/div[2]'
    regiondrop = '/html/body/div/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div/select'
    statedrop = '/html/body/div/div/div[2]/div[3]/div[1]/div/div[1]/div[4]/div/select'
    wilayahdrop = '/html/body/div/div/div[2]/div[3]/div[1]/div/div[1]/div[5]/div/select'
    zonedrop = '/html/body/div/div/div[2]/div[3]/div[1]/div/div[1]/div[6]/div/select'
    chartdrop = '//*[@id="chart_type"]'
    activities = '//*[@id="main-content"]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/ul/li[1]/div/div/span[1]'
    backbutton = '//*[@id="main-content"]/div[2]/div/div/div/div[1]/div/div[2]/button'
    alerts = '//*[@id="main-content"]/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/ul/li[1]'

class Navigation:
    reportmenu = "//*[@id=\"sidenav-main\"]/div/div/ul[1]/div[1]/li/a"
    worklistnav = '//*[@id="sidenav-main"]/div/div/ul[1]/div[1]/li/div/ul/li[3]/a'

class Worklist:
    toggleView = '//*[@id="main-content"]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/button[2]'
    filtericon = '/html/body/div/div[2]/nav/div/div[1]/button'
    filterstatus = '/html/body/div/div[1]/div/div/form/div[1]/div[5]/div/select'
    inprogress = '//*[@id="alert_status"]/option[3]'
    applyfilter = '/html/body/div/div[1]/div/div/form/div[2]/div/button/span[2]'
    ##Development
    #tndetail = '//*[@id="main-content"]/div[2]/div[2]/div/div/div[2]/div[4]/div[1]/div/div[3]/div[2]/button'
    ##Production
    tndetail = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[4]/div/div/div[2]/div[2]/button'
    tncheckbox = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/div/input'
    markinvalid = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/div/div[2]/button'
    showmore = '//*[@id="main-content"]/div[2]/div[2]/div/div/div[2]/div[5]/div/button'
    searchbar = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/input'
    searchbtn = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/button'
    enlargeimg = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[4]/div[1]/div/img'
    ##Use to get alert from List View based on row, accept value 1-10
    def Listalert(j):
        listalert = '//*[@id="user-table"]/tbody/tr['+str(j)+']'
        return listalert
    
    ##Use to get alert from Thumbnail View based on row, accept value 1-8 (Can accept more if show more is clicked) 
    def Thumbnailalert(i):
        tnalert = '//*[@id="main-content"]/div[2]/div[2]/div/div/div[2]/div[4]/div['+str(i)+']'
        return tnalert

class Inspectioninfo:
    backbutton = '/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button'
    