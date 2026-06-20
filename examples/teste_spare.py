
from PICSimLab_rcontrol import PICSimLab_rcontrol

try:
        with PICSimLab_rcontrol(5000) as rc:
            rc.debug=1
                  
            rc.cmd_splist()

            rc.cmd_spshow(1)
            rc.cmd_spdel("all")

            rc.cmd_spadd("LEDs",10,10)
            rc.cmd_spadd("LEDs",10,150)
            rc.cmd_spadd("LEDs",10,300)

            rc.cmd_sprdcfg(0)

            rc.cmd_spwrcfg(0,"14,15,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,2")
        
            rc.cmd_spdel(1)
            rc.cmd_spdel(1)

            rc.cmd_quit()


            
except ConnectionError as e:
        print(e)            

   
