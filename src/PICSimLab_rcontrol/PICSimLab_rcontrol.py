"""
   ########################################################################

   PICSimLab - Programmable IC Simulator Laboratory

   ########################################################################

   Copyright (c) : 2025-2026  Luis Claudio Gambôa Lopes <lcgamboa@yahoo.com>

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

   For e-mail suggestions :  lcgamboa@yahoo.com
   ######################################################################## 
 """ 

import socket


class PICSimLab_rcontrol:
    """
    PICSimLab rcontrol (Remote Control) interface library
    """
    def __init__(self, port="5000", host="127.0.0.1"):
        """
        Connect with PICSimlab using TCP/IP rcontrol commands
        """
        self.response = ""
        self.debug = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.sock.connect((host,port))

            # discard initial server message
            self.sock.recv(200)

        except OSError as e:
            self.sock.close()
            raise ConnectionError(f" Connection error: {e}\n Verify if PICSimLab is running.")

    def send_cmd(self, cmd):
        """
        Send one rcontrol command and read the response 
        """
        if self.debug:
            print(f"===========================\n<{cmd}")

        try:
            self.sock.sendall(cmd.encode("utf-8"))
            self.sock.sendall(b"\r\n")
        except OSError as e:
            print(f"send error: {e}")
            return None

        buff = bytearray()

        while True:
            try:
                data = self.sock.recv(1)
            except OSError as e:
                print(f"recv error: {e}")
                return None

            if not data:
                print("Connection closed")
                return None

            buff.extend(data)

            if buff.endswith(b"Ok\r\n>") or buff.endswith(b"ERROR\r\n>"):
                break
        self.response = buff.decode(errors="ignore") 
        if self.debug:
            print(self.response)

        ret = not buff.endswith(b"Ok\r\n>") 

        if(ret):
            print (f"Error on command [{cmd}]!")
        return ret
    
    def close(self):
        """
        Close the rcontrol connection with PICSimLab
        """
        if self.sock:
            self.sock.close()
            self.sock = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def get_cmd_response(self):    
        """ 
        Get the last commmand response.
        """
        return  self.response

    #commands
        
    def cmd_blist(self):    
        """
        blist                - list supported boards
        """
        return  self.send_cmd("blist")

    def cmd_buclist(self):    
        """
        buclist              - list board supported MCus
        """
        return  self.send_cmd("buclist")
    

    def cmd_clk(self, val=0):    
        """
        clk [val MHz]        - show or set simulation clock
        """
        if val > 0:
            cmd = f"clk {val}"
        else:
            cmd = "clk"
        return  self.send_cmd(cmd)
    

    def cmd_dumpe(self, addr=-1, count=-1):    
        """
        dumpe [addr] [count] - dump internal EEPROM memory
        """
        if addr < 0:
            cmd = "dumpe"
        else:
            if count < 0:
                cmd = f"dumpe {addr}"
            else:
                cmd = f"dumpe {addr} {count}"        
        return  self.send_cmd(cmd)
    

    def cmd_dumpf(self, addr=-1, count=-1):    
        """
        dumpf [addr] [count] - dump Flash memory
        """
        if addr < 0:
            cmd = "dumpf"
        else:
            if count < 0:
                cmd = f"dumpf {addr}"
            else:
                cmd = f"dumpf {addr} {count}"        
        return  self.send_cmd(cmd)
    

    def cmd_dumpr(self, addr=-1, count=-1):    
        """
        dumpr [addr] [count] - dump RAM memory
        """
        if addr < 0:
            cmd = "dumpr"
        else:
            if count < 0:
                cmd = f"dumpr {addr}"
            else:
                cmd = f"dumpr {addr} {count}"        
        return  self.send_cmd(cmd)

    def cmd_exit(self):    
        """
        exit                 - shutdown PICSimLab
        """
        return  self.send_cmd("exit")
    
    def cmd_get(self,obj):    
        """ 
        get obj              - get object value    
        """
        return  self.send_cmd(f"get {obj}")

    def cmd_help(self):    
        """
        help                 - show this message
        """
        return  self.send_cmd("help")

    def cmd_info(self):    
        """
        info                 - show actual setup info and objs
        """
        return  self.send_cmd("info")
    
    def cmd_loadhex(self,fname):
        """
        loadhex file         - load hex/bin file (full path)
        """
        cmd = f"loadhex {fname}"
        return  self.send_cmd(cmd)
    
    def cmd_oscmeasures(self, ch):
        """
        oscmeasures ch       - read osc channel 1 or 2 measures
        """
        return self.send_cmd(f"oscmeasures {ch}")
    
    def cmd_oscrdcfg(self):
        """
        oscrdcfg             - read osc configuration
        """
        return self.send_cmd("oscrdcfg")
    
    def cmd_oscwrcfg(self, idx, scfg):
        """
        oscwrcfg idx "cfg"   - write osc configuration
        """
        return self.send_cmd(f"oscwrcfg {idx} \"{scfg}\"")

    def cmd_oscshow(self, show=-1):
        """
        oscshow [0/1]        - show status or toggle osc window
        """
        if show == -1:
            cmd = "oscshow"
        else:
            cmd = f"oscshow {show}"
        return self.send_cmd(cmd)

    def cmd_pins(self):    
        """
        pins                 - show pins directions and values
        """
        return  self.send_cmd("pins")

    def cmd_pinsl(self):    
        """
        pinsl                - show pins formatted info
        """
        return  self.send_cmd("pinsl")
    
    def cmd_quit(self):    
        """
        quit                 - quit remote control interface
        """
        return  self.send_cmd("quit")
    
    def cmd_reset(self):    
        """
        reset                - reset the board
        """
        return  self.send_cmd("reset")
    
    def cmd_set(self, obj, value):    
        """
        set obj value        - set object with value
        """
        return  self.send_cmd(f"set {obj} {value}")

    def cmd_sim(self, simcmd=-1):
        """
        sim [start/stop]     - show status or start/stop sim
        """
        if simcmd == -1:
            cmd = "sim"
        else:
            cmd = f"sim {simcmd}"
        return self.send_cmd(cmd)
    
    def cmd_spadd(self, pname, x ,y):
        """
        spadd "pname" x y    - adds the named spare part
        """
        return self.send_cmd(f"spadd \"{pname}\" {x} {y}")
    
    def cmd_spdel(self, pid):
        """
        spdel pid/all        - delete one spare part or all
        """
        return self.send_cmd(f"spdel {pid}")
    
    def cmd_sprdcfg(self, pid):
        """
        sprdcfg pid          - read spare part configuration
        """
        return self.send_cmd(f"sprdcfg {pid}")
    
    def cmd_spwrcfg(self, pid,scfg):
        """
        spwrcfg pid "cfg"    - write spare part configuration
        """
        return self.send_cmd(f"spwrcfg {pid} \"{scfg}\"")
    
    def cmd_splist(self):    
        """
        splist               - list supported spare parts
        """
        return  self.send_cmd("splist")   
    
    def cmd_spshow(self, show=-1):
        """
        spshow [0/1]         - show status or toggle sp window
        """
        if show == -1:
            cmd = "spshow"
        else:
            cmd = f"spshow {show}"
        return self.send_cmd(cmd)

    def cmd_sync(self):    
        """
        sync                 - wait to sync with timer event
        """
        return  self.send_cmd("sync")   

    def cmd_version(self):    
        """
        version              - show PICSimLab version
        """
        return  self.send_cmd("version")   

           


