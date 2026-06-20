from PICSimLab_rcontrol import PICSimLab_rcontrol

try:
        with PICSimLab_rcontrol(5000) as rc:
            rc.debug=1
                  
            rc.cmd_blist()
            #print(rc.get_cmd_response())

            rc.cmd_buclist()

            rc.cmd_help()

            rc.cmd_version()

            rc.cmd_info()
  
            rc.cmd_reset()
            
            #rc.cmd_loadhex("/tmp/invalid.hex")

            rc.cmd_clk(8)
            rc.cmd_clk()
            rc.cmd_clk(16)
 
 
            rc.cmd_dumpe(0x00,32)
            rc.cmd_dumpf(0x00,32)
            rc.cmd_dumpr(0x00,32)
            
            rc.cmd_pins()

            rc.cmd_pinsl()

            rc.cmd_splist()

            rc.cmd_sync()

            rc.cmd_sim()

            rc.cmd_info() 

            rc.cmd_get("board.out[01]")

            rc.cmd_set("part[02].in[00]",1)

            rc.cmd_oscshow(0)

            rc.cmd_spshow(0)
   
            rc.cmd_quit()

            #rc.cmd_exit()


  #get ob       - get object value
  #set ob vl    - set object with value
  #sim [cmd]    - show simulation status or execute cmd start/stop
  #spadd "pname" xpos ypos - adds the named spare part
  #sprdcfg pid  - read spare part configuration
  #spwrcfg pid "cfg" - write spare part configuration


except ConnectionError as e:
        print(e)
       