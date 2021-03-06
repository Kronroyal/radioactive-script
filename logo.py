class bcolors:
    BLACK='\u001b[30m'
    RED = '\u001b[31m'
    GREEN='\u001b[92m'
    BLUE='\u001b[94m'
    YELLOW='\u001b[93m'
    RESET='\u001b[0m'

def print_logo1():   #found on :  http://www.ascii-art.de/ascii/s/skull.txt
    icon=""
    icon+="                               ...----....\n"
    icon+="                         ..-:"''         ''"-..\n"
    icon+="                      .-'                      '-.\n"
    icon+="                    .'              .     .       '.\n"
    icon+="                  .'   .          .    .      .    .''.\n"
    icon+="                .'  .    .       .   .   .     .   . ..:.\n"
    icon+="              .' .   . .  .       .   .   ..  .   . ....::.\n"
    icon+="             ..   .   .      .  .    .     .  ..  . ....:IA.\n"
    icon+="            .:  .   .    .    .  .  .    .. .  .. .. ....:IA.\n"
    icon+="           .: .   .   ..   .    .     . . .. . ... ....:.:VHA.\n"
    icon+="           '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.\n"
    icon+="          .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.\n"
    icon+="         .:.... .   . .''::'''.. .   .  . .:.:.:II;,. .. ..:IHIMMA\n"
    icon+="         ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM\n"
    icon+="        .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM\n"
    icon+="       .:.:V.:IVHHHHHHHMHMHHH::..:" ".:HIHHHHHHHHHHHHHMHHA. .VMMM.\n"
    icon+="       :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI\n"
    icon+="       ::V..:VIHHHHHHMMMHHHHHH. .   .I :IIMHHMMHHHHHHHHHHHAPI:WMM\n"
    icon+="       ::'. .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM\n"
    icon+="       :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW\n"
    icon+="       '.  ..:..:.:IHHHHHMMHV' .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV\n"
    icon+="        :.  .:...:'.:.:TPP'   .AVMMHMMA.:. 'VMMHHHP.:... .. :IVAI\n"
    icon+="       .:.   '... .:''   .   ..HMMMHMMMA::. .VHHI:::....  .:.IHW \n"
    icon+="       ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM\n"
    icon+="     : .   .' .-:.V.. .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::..P:HM.\n"
    icon+="     :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV':T::I::.'.:IHIMA\n"
    icon+="     'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH\n"
    icon+="       'IHH:.II:.. .:. .  . . . ' :HB' . . ..PI:.::.:::..:IHHMMV\n"
    icon+="        :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM'\n"
    icon+="        :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM\n"
    icon+="        :'VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI\n"
    icon+="        :.VIIHHMMA:..  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI\n"
    icon+="        :..VIHIHMMMI...::.,:.,:!'I:!'I!'I!'V:AI:VAMMMMMMHMMMMMM'\n"
    icon+="        ':.:HIHIMHHA:'!!'I.:AXXXVVXXXXXXXA:.'HPHIMMMMHHMHMMMMMV\n"
    icon+="          V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM\n"
    icon+="            'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'''\n"
    icon+="             I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI\n"
    icon+="           .I::. 'H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'\n"
    icon+="            :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM\n"
    icon+="            :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM\n"
    icon+="            ::.I:.  ':'SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.\n"
    icon+="            ::.I:. . ..:'BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI\n"
    icon+="            :..::.  . ..::':BBBBBSSBBBMMMB:MMMMHHII::IHHMI\n"
    icon+="            ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV'\n"
    icon+="              'V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'\n"
    icon+="                ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM'\n"
    icon+="                 '::....::.:::..:..::IIIIIHHHHMMMHHMV'\n"
    icon+="                   '::.::.. .. .  ...:::IIHHMMMMHMV'\n"
    icon+="                     'V::... . .I::IHHMMV''\n"
    icon+="                       ''VHVHHHAHHHHMMV:''\n"
    print(f"{bcolors.RED}Script made by Kronroyal\n")
    print(icon)

def print_logo2():
    icon=""
    icon+="                      __    _\n"
    icon+="                    _wr''        '-q__\n"
    icon+="                 _dP                 9m_\n"
    icon+="               _#P                     9#_\n"
    icon+="              d#@                       9#m\n"
    icon+="             d##                         ###\n"
    icon+="            J###                         ###L\n"
    icon+="            {###K                       J###K\n"
    icon+="            ]####K      ___aaa___      J####F\n"
    icon+="        __gmM######_  w#P''   ''9#m  _d#####Mmw__\n"
    icon+="     _g##############mZ_         __g##############m_\n"
    icon+="   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_\n"
    icon+="  a###""          ,Z'#####@' '######'\g          ''M##m\n"
    icon+=" J#@'             0L  '*##     ##@'  J#              *#K\n"
    icon+=" #'               '#    '_gmwgm_~    dF               `#_\n"
    icon+="7F                 '#_   ]#####F   _dK                 JE\n"
    icon+="]                    *m__ ##### __g@                    F\n"
    icon+="                       'PJ#####LP\n"
    icon+=" `                       0######_                      '\n"
    icon+="                       _0########_\n"
    icon+="     .               _d#####^#####m__              ,\n"
    icon+="       *w_________am#####P'   ~9#####mw_________w*\n"
    icon+="          ''9@#####@M''           ''P@#####@M''\n"
    print(f"\t\t{bcolors.YELLOW}Script made by Kronroyal\n")
    print(icon)
    print("\n\n\n\n")

print("")