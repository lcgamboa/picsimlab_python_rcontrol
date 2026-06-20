import time

from PICSimLab_rcontrol import PICSimLab_rcontrol

try:
        with PICSimLab_rcontrol(5000) as rc:
          rc.debug=1

          for i in range(5000):
            rc.cmd_info()

            rc.cmd_oscshow(1)

            rc.cmd_oscrdcfg()

            rc.cmd_oscwrcfg(0, "osc_cfg,502,458,0:10.000000,0.000000,1,1,2.500000,3,2,0,7,8")
            rc.cmd_oscwrcfg(1, "osc_ch1,0,0,0:2.000000,0.000000,1,#FF0000,0,16  PB2/~10")
            rc.cmd_oscwrcfg(2, "osc_ch2,0,0,0:2.000000,-6.000000,1,#00FF00,0,15  PB1/~9")


            #time.sleep(2)
            rc.cmd_oscmeasures(1)
            val=rc.get_cmd_response()

            pcyc=float((val.split('\n')[7]).split()[1]) 
            ncyc=float((val.split('\n')[8]).split()[1]) 

            print(pcyc)
            print(ncyc)

            #rc.cmd_oscshow(0)

        rc.cmd_quit()


            
except ConnectionError as e:
        print(e)            

   
