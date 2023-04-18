#pylint:disable=C0116
#pylint:disable=W0311
import numpy as nu
import math
import copy
import datetime as dtime

class StellarObj():
    zaehler=0 
    
    def __init__(self, name, durchmesser, entfernung):
        StellarObj.zaehler+=1
        self.name=name
        self.durchmesser=durchmesser
        self.d_unit="km"
        self.entfernung=entfernung
        self.e_unit="km"
        
        
class UserControl():
           
    def __init__(self):
        # Voyager Entfernungsrechnung
        nowday=dtime.date.today()
        print(nowday)
        orgday=dtime.date(2021,8,1)
        difday=nowday-orgday
        AE=149597870.700 # km AstronomischeEinheit
        orgdis_voy=153.06626*AE
        velos_voy=61198.154139 # km/h Voyager 1 Geschwindigkeit
        now_dis_voy=orgdis_voy+(velos_voy*24*difday.days)
        
        self.unit_list=["km","m","mm","um","nm","pm","fm"]
        self.lij=9.46e12
        self.obj_list=[]
        # Name, Größe/km, Abstand/km
        self.obj_list.append(StellarObj("Sonne", 1392684, 0))
        self.obj_list.append(StellarObj("Merkur",4879,57.9e6))
        self.obj_list.append(StellarObj("Venus",12104,108.2e6))
        self.obj_list.append(StellarObj("Erde",12756,149.6e6))
        self.obj_list.append(StellarObj("Mond", 3474, 384400))
        self.obj_list.append(StellarObj("Mars", 6792, 229e6))
        self.obj_list.append(StellarObj("Jupiter", 142984, 778.5e6))
        self.obj_list.append(StellarObj("Saturn", 120536, 1433.4e6))
        self.obj_list.append(StellarObj("Uranus", 51118, 2872e6))
        self.obj_list.append(StellarObj("Neptun", 49528, 4495e6))
        self.obj_list.append(StellarObj("Pluto", 2374, 5906e6))
        self.obj_list.append(StellarObj("Proxima Centauri", 214473,4e13))
        self.obj_list.append(StellarObj("Voyager 1",0,now_dis_voy))
        self.doit = "start"
        self.start()
    
    def start(self):
        print("Programm zur Skalierung Stellarer und Interstellarer Objekt\n"
        "Folgende Objekte sind gespeichert:")
        for obj in self.obj_list:
            print(obj.name, end=", ")
        print("\nBeenden mit 'exit', Hilfe unter 'help', "
        "'Zahl' berechnet Skalierung der genannten "
        "Objekte z.b. 1e12.\nZur Skalierung nach Zielgröße eines Objekts "
        "oder einer Entfernung kann z.B. der folgende Code "
        "verwendet werden:\nSonne,d,2,mm für "
        "Objekt,Eigenschaft,Zielgröße,Einheit\n"
        "Eigenschaft: d für Durchmesser und e für Entfernung.\n"
        "Einheiten: {}".format(self.unit_list))
        self.user_input()
        
    def user_input(self):
        while self.doit != "exit":
            self.doit=input("\n>")
            input_list=self.doit.split(sep=",", maxsplit=3)
            if len(input_list)==4:
                self.doit=self.scale_obj(input_list)
            elif self.doit == "help":
                    self.start()
            elif self.doit=="exit":
                    pass
            try:
                self.doit=float(self.doit)
            except:
                print("Eingabe nicht erkannt")
            if type(self.doit)==float:
                    self.scale()
    
    def scale_obj(self, input_list):
        for objm in self.obj_list:
            to_scale_obj="fehler"
            if objm.name==input_list[0]:
                if input_list[1]=="e":
                    to_scale_obj=objm.entfernung
                    break
                elif input_list[1]=="d":
                    to_scale_obj=objm.durchmesser
                    break
                else:
                    to_scale_obj="fehler"
                    break
        if to_scale_obj!="fehler":
            try:
                scale_fact=float(input_list[2])
            except:
                to_scale_obj="fehler"
        if to_scale_obj!="fehler":
            uni_num=-1
            num_test="fehler"
            for unitm in self.unit_list:
                uni_num+=1
                if unitm == input_list[3]:
                    num_test="ok"
                    break
            if num_test=="ok":
                    try:
                        scale_fact=scale_fact/(1e3**uni_num)
                        self.doit=to_scale_obj/scale_fact
                    except:
                        self.doit="Fehler"
        return self.doit
                              
    def scale(self):
            obj_list_scale=copy.deepcopy(self.obj_list)
            print("Skalierung um Faktor {}".format(self.doit))    
            for objs in obj_list_scale:
                try:
                    objs.durchmesser=objs.durchmesser/self.doit
                    objs.d_unit, objs.durchmesser=self.unit(objs.d_unit, objs.durchmesser)
                    objs.entfernung=objs.entfernung/self.doit
                    objs.e_unit, objs.entfernung=self.unit(objs.e_unit, objs.entfernung)
                    print("{} hat einen Durchmesser von {:.2f} {}\nund eine Entfernung von {:.2f} {}".format(objs.name, objs.durchmesser, objs.d_unit, objs.entfernung, objs.e_unit))
                except:
                    print("Durch Null kann nicht geteilt werden!")
                    break
                
    def unit(self, uniti, obji):
            unit_num=0
            while obji<1:
                unit_num+=1
                obji=obji*1000
                if unit_num>=6:
                    break
            if unit_num==0:
                pass
            elif unit_num==1:
                uniti="m"
            elif unit_num==2:
                uniti="mm"
            elif unit_num==3:
                uniti="um"
            elif unit_num==4:
                uniti="nm"
            elif unit_num==5:
                uniti="pm"
            elif unit_num==6:
                uniti="fm"
            else:
                print("error")
            return uniti, obji
  
                    
if __name__ == "__main__":
    
    user=UserControl()
    
    