from tkinter import*
import math,random,os
from tkinter import messagebox
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
       
        

class Bill_App:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1280x800+0+0")
        self.root.title("Billing Software by Naveen Kumawat")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        
        
        
        #=======================================var for man============================================================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_oil=IntVar()
        self.hair_color=IntVar()
        self.hair_gel=IntVar()
        
        
        #=======================================var for woman=========================================================================
        self.body_loaton=IntVar()
        self.blush=IntVar()
        self.eyeliner=IntVar()
        self.lipistic=IntVar()
        self.primer=IntVar()
        self.eyeshadow=IntVar()
        
        #============================================combo================================================================
        self.body_l_com=IntVar()
        self.hair_oil_col_com=IntVar()
        self.face_cream_com=IntVar()
        self.lipistic_p_com=IntVar()
        self.eyeshadow_e_com=IntVar()
        self.gel_sp_com=IntVar()
        
        
        
        #============================================total & tax=============================================
        self.total_man=StringVar()
        self.total_woman=StringVar()
        self.total_combo=StringVar()
        
        
        self.total_man_tax=StringVar()
        self.total_woman_tax=StringVar()
        self.total_combo_tax=StringVar()
        
        
        
        
        
        
        #=========================================Customer=======================================================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        
        
        
        
        
        #===============================================co=========detailes=====================================
        
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        
        
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("time new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        
        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("time new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        c_bill_lbl=Label(F1,text="Bill No.",bg=bg_color,fg="white",font=("time new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        
        
        bill_btn=Button(F1,text="Search",fg="black",width=10,bd=7,font="arial 12 bold",textvariable=self.search_bill).grid(row=0,column=6,pady=10,padx=10)
        
        
        
        
        
        
        
        
        
        
        
        #===============================Costmetics Man =====================================================
        F2=LabelFrame(self.root,text="Man Costmetics Item",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=185,width=330,height=380)
        
        
        
        bath_libl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky=W)
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        face_wash_libl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky=W)
        face_wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        face_cream_libl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky=W)
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        hair_oil_libl=Label(F2,text="Hair Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky=W)
        hair_oil_txt=Entry(F2,width=10,textvariable=self.hair_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        hair_color_libl=Label(F2,text="Hair Color",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky=W)
        hair_color_txt=Entry(F2,width=10,textvariable=self.hair_color,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        hair_gel_libl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky=W)
        hair_gel_txt=Entry(F2,width=10,textvariable=self.hair_gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
        
        
        #===============================Costmetics Woman =====================================================
        F3=LabelFrame(self.root,text="Woman Costmetics Item",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=345,y=185,width=330,height=380)
        
        
        
        body_l_libl=Label(F3,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky=W)
        body_l_txt=Entry(F3,width=10,textvariable=self.body_loaton,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        blush_libl=Label(F3,text="Blush",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky=W)
        blush_txt=Entry(F3,width=10,textvariable=self.blush,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        eyeliner_libl=Label(F3,text="Eyeliner",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky=W)
        eyeliner_txt=Entry(F3,width=10,textvariable=self.eyeliner,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        eyeshadow_libl=Label(F3,text="Eyeshadow",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky=W)
        eyeshadow_txt=Entry(F3,width=10,textvariable=self.eyeshadow,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        lipistic_libl=Label(F3,text="Lipistic",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky=W)
        lipistic_txt=Entry(F3,width=10,textvariable=self.lipistic,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        primer_libl=Label(F3,text="Primer",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky=W)
        primer_txt=Entry(F3,width=10,textvariable=self.primer,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
        
        #===============================Costmetics Combo =====================================================
        F4=LabelFrame(self.root,text="Combo",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=685,y=185,width=420,height=380)
        
        
        
        body_l_com_libl=Label(F4,text="Body Lotion Combo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky=W)
        body_l_com_txt=Entry(F4,width=10,textvariable=self.body_l_com,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        hair_oil_col_com_libl=Label(F4,text="Hair Oil + Hair Color",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky=W)
        hair_oil_col_com_txt=Entry(F4,width=10,textvariable=self.hair_oil_col_com,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        face_cream_com_libl=Label(F4,text="Face Wash + Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky=W)
        face_cream_com_txt=Entry(F4,width=10,textvariable=self.face_cream_com,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        eyeshadow_e_com_libl=Label(F4,text="Eyeshadow + Eyeliner",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky=W)
        eyeshadow_e_com_txt=Entry(F4,width=10,textvariable=self.eyeshadow_e_com,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        lipistic_p_com_libl=Label(F4,text="Lipistic + Primer",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky=W)
        lipistic_p_com_txt=Entry(F4,width=10,textvariable=self.lipistic_p_com,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        gel_sp_com_libl=Label(F4,text="Gel + Sparey",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky=W)
        gel_sp_com_txt=Entry(F4,width=10,textvariable=self.gel_sp_com,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
        
        #===============bill area============
        
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1115,y=185,width=415,height=380)
        bill_title=Label(F5,text="Bill Recepit",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        
        
        
        #=============================button fram===========================================================
        
        F6=LabelFrame(self.root,text="Bill Details",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=235)
        
        
        total_man_libl=Label(F6,text="Total Man Costmatic Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=1,sticky=W)
        total_man_txt=Entry(F6,width=18,textvariable=self.total_man,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,pady=1,padx=10)
        
        total_woman_libl=Label(F6,text="Total Woman Costmatic Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=1,sticky=W)
        total_woman_txt=Entry(F6,width=18,textvariable=self.total_woman,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,pady=1,padx=10)
        
        total_combo_libl=Label(F6,text="Total Combo Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=1,sticky=W)
        total_combo_txt=Entry(F6,width=18,textvariable=self.total_combo,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,pady=1,padx=10)
        
        
        
        
        total_man_tax_libl=Label(F6,text="Man Costmatic Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=10,pady=1,sticky=W)
        total_man_tax_txt=Entry(F6,width=18,textvariable=self.total_man_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,pady=1,padx=10)
        
        total_woman_tax_libl=Label(F6,text="Woman Costmatic Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=1,column=2,padx=10,pady=10,sticky=W)
        total_woman_tax_txt=Entry(F6,width=18,textvariable=self.total_woman_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,pady=1,padx=10)
        
        total_combo_tax_libl=Label(F6,text="Combo Costmatic Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=2,column=2,padx=10,pady=1,sticky=W)
        total_combo_tax_txt=Entry(F6,width=18,textvariable=self.total_combo_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,pady=1,padx=10)
        
        
        
        
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=850,width=650,height=115)
        
        
        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=12,bd=5,font="arial 12 bold").grid(row=0,column=0,padx=10,pady=15)
        gbill_btn=Button(btn_F,text="G-Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,width=12,bd=5,font="arial 12 bold").grid(row=0,column=1,padx=10,pady=15)
        clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",pady=15,width=12,bd=5,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=15)
        exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",pady=15,width=12,bd=5,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=15)
        
        self.welcome_bill()
        
        
        
        
        
    def total(self):
        self.c_m_s_p=self.soap.get()*40
        self.c_m_fc_p=self.face_cream.get()*194
        self.c_m_fw_p=self.face_wash.get()*96
        self.c_m_ho_p=self.hair_oil.get()*120
        self.c_m_hc_p=self.hair_color.get()*20
        self.c_m_hg_p=self.hair_gel.get()*80
        self.total_costmatic_man_price=float(
            self.c_m_s_p+
            self.c_m_fc_p+
            self.c_m_fw_p+
            self.c_m_ho_p+
            self.c_m_hc_p+
            self.c_m_hg_p
           
        )
        self.total_man.set("Rs. "+str(self.total_costmatic_man_price))
        self.c_man_tax=round((self.total_costmatic_man_price*0.06),4)
        self.total_man_tax.set("Rs. "+str(self.c_man_tax))
        
        
        
        
        self.c_wm_b_p=self.blush.get()*384
        self.c_wm_el_p=self.eyeliner.get()*56
        self.c_wm_l_p=self.lipistic.get()*190
        self.c_wm_p_p=self.primer.get()*80
        self.c_wm_es_p=self.eyeshadow.get()*220
        self.c_wm_bl_p=self.body_loaton.get()*240
        
        self.total_costmatic_woman_price=float(
            self.c_wm_bl_p+
            self.c_wm_b_p+
            self.c_wm_el_p+
            self.c_wm_es_p+
            self.c_wm_p_p+
            self.c_wm_l_p
        )
        self.total_woman.set("Rs. "+str(self.total_costmatic_woman_price))
        self.c_woman_tax=round((self.total_costmatic_woman_price*0.08),4)
        self.total_woman_tax.set("Rs. "+str(self.c_woman_tax))
        
        
        self.c_c_bl_C_p=self.body_l_com.get()*380
        self.c_c_h_c_c_p=self.hair_oil_col_com.get()*128
        self.c_c_f_c_c_p=self.face_cream_com.get()*256
        self.c_c_l_p_c_P=self.lipistic_p_com.get()*260
        self.c_c_e_e_c_p=self.eyeshadow_e_com.get()*270
        self.c_c_g_s_c_p=self.gel_sp_com.get()*190
        
        self.total_costmatic_combo_price=float(
            self.c_c_bl_C_p+
            self.c_c_e_e_c_p+
            self.c_c_f_c_c_p+
            self.c_c_g_s_c_p+
            self.c_c_l_p_c_P+
            self.c_c_h_c_c_p
        )
        self.total_combo.set("Rs. "+str(self.total_costmatic_combo_price))
        self.C_combo_tax=round((self.total_costmatic_combo_price*0.07),4)
        self.total_combo_tax.set("Rs. "+str(self.C_combo_tax))
        
        
        
        
        self.Total_Bill=float(round((self.total_costmatic_man_price+
                              self.total_costmatic_woman_price+
                              self.total_costmatic_combo_price+
                              self.c_man_tax+
                              self.c_woman_tax+
                              self.C_combo_tax),3))
        
        
        
        
        
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\tWelcome In Store\n")
        
        self.txtarea.insert(END,f"\n Bill No. : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone No. :{self.c_phon.get()}")
        self.txtarea.insert(END,f"\n==============================================")
        
        self.txtarea.insert(END,f"\n Product\t\t Qty.\t\tPrice")
        
        
        self.txtarea.insert(END,f"\n==============================================")
        
        
        
        
        
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details emapty")
        else:
             
            self.welcome_bill()
        
            #================================man========================================
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_m_s_p}")
        
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_m_fc_p}")
            
            if self.hair_oil.get()!=0:
                self.txtarea.insert(END,f"\n Hair Oil\t\t{self.hair_oil.get()}\t\t{self.self.c_m_ho_p}")
            
            if self.hair_color.get()!=0:
                self.txtarea.insert(END,f"\n Hair Color\t\t{self.hair_color.get()}\t\t{self.c_m_hc_p}")
            
            if self.hair_gel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.hair_gel.get()}\t\t{self.c_m_hg_p}")
            
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_m_fw_p}")
            
            
            
            #===========================================================woman============================================================
            
            if self.blush.get()!=0:
                self.txtarea.insert(END,f"\n Blush\t\t{self.blush.get()}\t\t{self.c_wm_b_p}")
          
            if self.eyeliner.get()!=0:
                self.txtarea.insert(END,f"\n Eyeliner\t\t{self.eyeliner.get()}\t\t{self.c_wm_el_p}")
          
            if self.lipistic.get()!=0:
                self.txtarea.insert(END,f"\n Lipistic\t\t{self.lipistic.get()}\t\t{self.c_wm_l_p}")
          
            if self.primer.get()!=0:
                self.txtarea.insert(END,f"\n Primer\t\t{self.primer.get()}\t\t{self.c_wm_p_p}")
          
            if self.eyeshadow.get()!=0:
                self.txtarea.insert(END,f"\n Eyeshadow\t\t{self.eyeshadow.get()}\t\t{self.c_wm_es_p}")
          
            if self.body_loaton.get()!=0:
                self.txtarea.insert(END,f"\n Body Loation\t\t{self.body_loaton.get()}\t\t{self.c_wm_bl_p}")
            
            
            #===========================================================Combo============================================================
             
            if self.body_l_com.get()!=0:
                self.txtarea.insert(END,f"\n Body Loation\t\t{self.body_l_com.get()}\t\t{self.c_c_bl_C_p}")
          
            if self.hair_oil_col_com.get()!=0:
                self.txtarea.insert(END,f"\n Hair Oil + Color Combo\t\t{self.hair_oil_col_com.get()}\t\t{self.c_c_h_c_c_p}")
          
            if self.face_cream_com.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream + Wash Combo\t\t{self.face_cream_com.get()}\t\t{self.c_c_f_c_c_p}")
          
            if self.lipistic_p_com.get()!=0:
                self.txtarea.insert(END,f"\n Lipistac + Primer Combo\t\t{self.lipistic_p_com.get()}\t\t{self.c_c_l_p_c_P}")
          
            if self.eyeshadow_e_com.get()!=0:
                self.txtarea.insert(END,f"\n Eyeshadow + Eyeliner Combo\t\t{self.eyeshadow_e_com.get()}\t\t{self.c_c_e_e_c_p}")
          
            if self.gel_sp_com.get()!=0:
                self.txtarea.insert(END,f"\n Gel + Speray Combo\t\t{self.gel_sp_com.get()}\t\t{self.c_c_g_s_c_p}")
            
            
            
              
            self.txtarea.insert(END,f"\n----------------------------------------------")
        
            if self.total_man_tax.get()!="Rs. 0.0":
        
                self.txtarea.insert(END,f"\n Man Costmetics Item Tax\t\t\t{self.total_man_tax.get()}")
            if self.total_woman_tax.get()!="Rs. 0.0":
            
                self.txtarea.insert(END,f"\n Woman Costmetics Item Tax\t\t\t{self.total_woman_tax.get()}")
            if self.total_combo_tax.get()!="Rs. 0.0":
        
                self.txtarea.insert(END,f"\n Man Costmetics Item Tax\t\t\t{self.total_combo_tax.get()}")
            
            self.txtarea.insert(END,f"\n----------------------------------------------")
        
            self.txtarea.insert(END,f"\n Total Bill Pay\t\t\t Rs.\t{self.Total_Bill}")
        
            self.txtarea.insert(END,f"\n----------------------------------------------")
            
            
            self.save_bill()
        
        
        
           
        
    def save_bill(self):
        op=messagebox.askyesno("Save Bill", "Do you want to save bill ?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)    
            f1=open("Bill_Print/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill {self.bill_no.get()} saved successfully")
            
        else:
            return
        
        
        
    def find_bill(self):
        for i in os.listdir("Bill_Print/"):
            print(i)
        
        
        
        
        
        
        
        
        
        
    
    
root=Tk()
obj=Bill_App(root)
root.mainloop()