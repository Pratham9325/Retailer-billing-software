from tkinter import *
from tkinter import messagebox
import random,os,tempfile
from tkinter import filedialog
import subprocess

def clear(bathsoapEntry, facecreamEntry, facewashEntry, hairspartEntry, hairgelEntry, bodylotionEntry, riceEntry, oilEntry, daalEntry, aataEntry, MundalEntry, MilkEntry, mazaEntry, PepsiEntry, SpriteEntry, CocaColaEntry, FantaEntry, limkhaEntry,  phoneEntry, nameEntry ,billnumnerEntry):
    bathsoapEntry.delete(0, END)
    facecreamEntry.delete(0, END)
    facewashEntry.delete(0, END)
    hairspartEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    bodylotionEntry.delete(0, END)
    riceEntry.delete(0, END)
    oilEntry.delete(0, END)
    daalEntry.delete(0, END)
    aataEntry.delete(0, END)
    MundalEntry.delete(0, END)
    MilkEntry.delete(0, END)
    mazaEntry.delete(0, END)
    PepsiEntry.delete(0, END)
    SpriteEntry.delete(0, END)
    CocaColaEntry.delete(0, END)
    FantaEntry.delete(0, END)
    limkhaEntry.delete(0, END)
    
    # Insert '0' in each entry
    bathsoapEntry.insert(0, '0')
    facecreamEntry.insert(0, '0')
    facewashEntry.insert(0, '0')
    hairspartEntry.insert(0, '0')
    hairgelEntry.insert(0, '0')
    bodylotionEntry.insert(0, '0')
    riceEntry.insert(0, '0')
    oilEntry.insert(0, '0')
    daalEntry.insert(0, '0')
    aataEntry.insert(0, '0')
    MundalEntry.insert(0, '0')
    MilkEntry.insert(0, '0')
    mazaEntry.insert(0, '0')
    PepsiEntry.insert(0, '0')
    SpriteEntry.insert(0, '0')
    CocaColaEntry.insert(0, '0')
    FantaEntry.insert(0, '0')
    limkhaEntry.insert(0, '0')
    
    groceryEntry.delete(0,END)
    drinkEntry.delete(0,END)
    cosmeticsEntry.delete(0,END)
    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    drinktaxEntry.delete(0,END)
    phoneEntry.delete(0,END)
    nameEntry.delete(0,END)
    billnumnerEntry.delete(0,END)
    textarea.delete(1.0,END)
    

def exit_program(root):
    root.destroy()
    
    
    
def print_bill():
    entered_text = textarea.get("1.0", "end-1c")  # Get text from textarea without the last newline character

    if not entered_text.strip():
        messagebox.showerror("Error", "Bill is empty. Please enter some text.")
        return

    # Ask the user to choose a location to save the PDF file
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return  # User canceled the save dialog

    # Save the bill as a PDF file
    try:
        from fpdf import FPDF
        
        class PDF(FPDF):
            def header(self):
                self.set_font('Arial', 'B', 12)
                self.cell(0, 10, 'Bill', 0, 1, 'C')

            def footer(self):
                self.set_y(-15)
                self.set_font('Arial', 'I', 8)
                self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=entered_text)
        pdf.output(file_path)
        messagebox.showinfo("Success", f"Bill saved as PDF: {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save bill as PDF: {str(e)}")
# ##### Search button functionality start##############
def search_bill(billnumnerEntry):
    found = False
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumnerEntry.get():
            found = True
            with open(f'bills/{i}','r') as f:
                textarea.delete(1.0, END)
                for data in f:
                    textarea.insert(END, data)
            break
    
    if not found:
        messagebox.showerror('Error', 'Invalid bill number')

    if not os.path.exists('bills'):
        os.mkdir('bills')
        
     # ##### Search button functionality end Call dysfunction from the printer, so I'll check if it is empty or not if it is empty, simply display is empty in case we will create a temporary file and will add the bill and will print that file area##############   

####### bill #################
def bill_area(nameEntry, phoneEntry,cosmeticsEntry,groceryEntry,drinkEntry,bathsoapEntry,facecreamEntry,facewashEntry,hairspartEntry,
              bodylotionEntry ,riceEntry,oilEntry,daalEntry,aataEntry,hairgelEntry,MundalEntry,MilkEntry,mazaEntry,PepsiEntry,SpriteEntry,CocaColaEntry
              ,FantaEntry,limkhaEntry,cosmetictaxEntry,grocerytaxEntry,drinktaxEntry,totalbill ):

    if nameEntry.get() == '' or phoneEntry.get() == "":
        messagebox.showwarning('Error', 'Customer Details Are Required')
    elif cosmeticsEntry.get() == '' and groceryEntry.get() == "" and drinkEntry.get() == '':
        messagebox.showwarning('Error', 'No Products are Selected')
    elif cosmeticsEntry.get() == '0 Rs' and groceryEntry.get() == "0 Rs" and drinkEntry.get() == '0 Rs':   
        messagebox.showerror('Error', 'No Products are Selected')
    else:
          global billnumbe
          billnumber = random.randint(100, 1000)
          textarea.delete(1.0,END)
          textarea.insert(END,'\t \t \t **Welcome Customer**\n')
          textarea.insert(END, f'Bill Number: {billnumber}\n')
          textarea.insert(END, f'Customer Name: {  nameEntry.get()}\n')
          textarea.insert(END, f'Customer Phone Number: { phoneEntry.get()}\n')
          textarea.insert(END, '\n================================================================================\n')
          textarea.insert(END, 'Product\t\t\t\t\tQunatity\t\t\t\tPrice')
          textarea.insert(END, '\n================================================================================\n')
          if bathsoapEntry.get()!='0':
             textarea.insert(END,f'Bath Soap\t\t\t\t\t{bathsoapEntry.get()}\t\t\t\t{soapprice} Rs\n')
          if facecreamEntry.get()!='0':
             textarea.insert(END,f'Face cream\t\t\t\t\t{facecreamEntry.get()}\t\t\t\t{ facecreamprice} Rs\n')
          if facewashEntry.get()!='0':
             textarea.insert(END,f'face wash\t\t\t\t\t{facewashEntry.get()}\t\t\t\t{facewashprice} Rs\n')
          if hairspartEntry.get()!='0':
             textarea.insert(END,f'hair spray\t\t\t\t\t{hairspartEntry.get()}\t\t\t\t{hairspratprice} Rs\n')
          if bodylotionEntry.get()!='0':
             textarea.insert(END,f'body lotion\t\t\t\t\t{bodylotionEntry.get()}\t\t\t\t{ bodylotionprice} Rs\n')
          if hairgelEntry.get()!='0':
             textarea.insert(END,f'Hair Gail\t\t\t\t\t{hairgelEntry.get()}\t\t\t\t{ bodylotionprice} Rs\n')
             
          if riceEntry.get()!='0':
             textarea.insert(END,f'Rice\t\t\t\t\t{riceEntry.get()}\t\t\t\t{ ricepraic } Rs\n')       
          if oilEntry.get()!='0':
             textarea.insert(END,f'Oil\t\t\t\t\t{oilEntry.get()}\t\t\t\t{ oilpraic } Rs\n')          
          if daalEntry.get()!='0':
             textarea.insert(END,f'Daal\t\t\t\t\t{daalEntry.get()}\t\t\t\t{  daalpraic  } Rs\n')       
          if aataEntry.get()!='0':
             textarea.insert(END,f'Aata\t\t\t\t\t{aataEntry.get()}\t\t\t\t{   aatapraic  } Rs\n')       
          if MundalEntry.get()!='0':
             textarea.insert(END,f'Mugdaal\t\t\t\t\t{MundalEntry.get()}\t\t\t\t{  mundapraic } Rs\n')   
          if MundalEntry.get()!='0':
             textarea.insert(END,f'Mugdaal\t\t\t\t\t{MundalEntry.get()}\t\t\t\t{  mundapraic } Rs\n')    
          if MilkEntry.get()!='0':
             textarea.insert(END,f'Milk\t\t\t\t\t{MilkEntry.get()}\t\t\t\t{    milkpraic } Rs\n')         
             
             
          if mazaEntry.get()!='0':
             textarea.insert(END,f'Maza\t\t\t\t\t{mazaEntry.get()}\t\t\t\t{   mazapraic} Rs\n')       
          if PepsiEntry.get()!='0':
             textarea.insert(END,f'Pepsi\t\t\t\t\t{PepsiEntry.get()}\t\t\t\t{ pepsipraic  } Rs\n')          
          if SpriteEntry.get()!='0':
             textarea.insert(END,f'Sprite\t\t\t\t\t{SpriteEntry.get()}\t\t\t\t{     spritrpraic  } Rs\n')       
          if CocaColaEntry.get()!='0':
             textarea.insert(END,f'Cocacola\t\t\t\t\t{CocaColaEntry.get()}\t\t\t\t{   CocaColapraic  } Rs\n')       
          if FantaEntry.get()!='0':
             textarea.insert(END,f'Fanta\t\t\t\t\t{FantaEntry.get()}\t\t\t\t{  fantaprac } Rs\n')   
          if limkhaEntry.get()!='0':
             textarea.insert(END,f'Limkha\t\t\t\t\t{limkhaEntry.get()}\t\t\t\t{limkhpraic} Rs\n')    
          textarea.insert(END, '\n--------------------------------------------------------------------------------')          
          if cosmetictaxEntry.get()!='0.0 Rs':
             textarea.insert(END,f'\nCosmetic Tax\t\t\t\t\t\t{cosmetictaxEntry.get()}')     
          if grocerytaxEntry.get()!='0.0 Rs':
             textarea.insert(END,f'\nGrocery Tax\t\t\t\t\t\t{grocerytaxEntry.get()}')       
          if  drinktaxEntry.get()!='0.0 Rs':
              textarea.insert(END,f'\nDrink Tax\t\t\t\t\t\t{ drinktaxEntry.get()}')  
          textarea.insert(END, '\n--------------------------------------------------------------------------------')            
          textarea.insert(END,f'\n \nTotal Bill \t\t\t\t\t{ totalbill}') 
          textarea.insert(END, '\n--------------------------------------------------------------------------------')   
          result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
          if result:
    # Write bill content to a file
                  with open(f'bills/{billnumber}.txt', 'w') as file:
                    file.write(textarea.get(1.0, END))
                  messagebox.showinfo("Success", f' Bill number {billnumber} Is saved successfully')
          else:
                  messagebox.showinfo("Information", "Bill not saved.")
                
# Cosmetic price calculate start
def total(bathsoapEntry, facecreamEntry, facewashEntry, hairspartEntry, hairgelEntry, bodylotionEntry, riceEntry,
          oilEntry, daalEntry, aataEntry, MundalEntry, MilkEntry, cosmeticsEntry, groceryEntry, mazaEntry, PepsiEntry,  SpriteEntry,CocaColaEntry, FantaEntry,limkhaEntry,cosmetictaxEntry,grocerytaxEntr
          ,drinktaxEntry):
   
   
   
    global soapprice, facecreamprice,facewashprice,hairspratprice, bodylotionprice,ricepraic ,oilpraic,  daalpraic , aatapraic,mundapraic,  milkpraic
    global  mazapraic,pepsipraic ,   spritrpraic,CocaColapraic,fantaprac,limkhpraic,totalbill
    # Calculate cosmetics prices
    soapprice = int(bathsoapEntry.get()) * 20
    facecreamprice = int(facecreamEntry.get()) * 50
    facewashprice = int(facewashEntry.get()) * 100
    hairspratprice = int(hairspartEntry.get()) * 150
    hairgelprice = int(hairgelEntry.get()) * 70
    bodylotionprice = int(bodylotionEntry.get()) * 60
    total_cosmetic_price = soapprice + facecreamprice + facewashprice + hairspratprice + hairgelprice + bodylotionprice

    # Insert total cosmetics price into cosmeticsEntry
    cosmeticsEntry.delete(0, END)
    cosmeticsEntry.insert(0, f"{total_cosmetic_price} Rs")
    # Calculate cosmetics tax
    cosmetictax = total_cosmetic_price * 0.12
    cosmetictaxEntry.delete(0, END)
    cosmetictaxEntry.insert(0, f"{cosmetictax} Rs")
    

    # Calculate groceries prices
    ricepraic = int(riceEntry.get()) * 200
    oilpraic = int(oilEntry.get()) * 30
    daalpraic = int(daalEntry.get()) * 36
    aatapraic = int(aataEntry.get()) * 100
    mundapraic = int(MundalEntry.get()) * 36
    milkpraic = int(MilkEntry.get()) * 25
    total_groceries = ricepraic + oilpraic + daalpraic + aatapraic + mundapraic + milkpraic
   

    # Insert total groceries price into groceryEntry
    groceryEntry.delete(0, END)
    groceryEntry.insert(0, f"{total_groceries} Rs")
   
     # Calculate grocerytextax
    grocerytex = total_groceries * 0.05
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, f"{grocerytex} Rs")
    
   # calculated drinks
    mazapraic = int(mazaEntry.get()) * 50
    pepsipraic = int(PepsiEntry.get()) * 30
    spritrpraic = int(SpriteEntry.get()) * 40
    CocaColapraic = int(CocaColaEntry.get()) * 40
    fantaprac = int(FantaEntry.get()) * 70
    limkhpraic = int(limkhaEntry.get()) * 40
    total_drinks = mazapraic + pepsipraic + spritrpraic + CocaColapraic + fantaprac + limkhpraic
    drinkEntry.delete(0, END)
    drinkEntry.insert(0, f"{total_drinks} Rs")
    
        # Calculate grocerytextax
    drinktix = total_drinks* 0.08
    drinktaxEntry.delete(0, END)
    drinktaxEntry.insert(0, f"{drinktix} Rs")
    
    totalbill = total_cosmetic_price+total_groceries+ total_drinks
    
def main():
    global cosmeticsEntry
    global groceryEntry
    global drinkEntry
    global  cosmetictaxEntry
    global grocerytaxEntry
    global drinktaxEntry
    global textarea
    root = Tk()  # Create the root window
    root.title("Retail Billing System")
    root.geometry('2560x1600')
    root.iconbitmap('icon.ico')
    root.attributes('-fullscreen', True)

    # Your GUI code here...
    headinglabel = Label(root, text="Retail Billing System", font=('times new roman', 30, 'bold'), bg="#074463", fg='gold', bd=16, relief=GROOVE)
    headinglabel.pack(side=TOP, fill=X)

    customer_details_frame=LabelFrame(root,text='Customer Deatils',font=('times new roman',18 ,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='#074463')
    customer_details_frame.pack(side=TOP, fill=X, padx=5, pady=5)


    namelabel=Label(customer_details_frame,text='Name',font=('times new roman',18,'bold')
                ,bg='#074463',fg='#fff')

    namelabel.grid(row=0,column=0,pady=2)


    nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=25)

    nameEntry.grid(row=0,column=1,padx=8)




    phonelabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',18,'bold')
                ,bg='#074463',fg='#fff')

    phonelabel.grid(row=0,column=2,padx=20,pady=2)

    phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=25)

    phoneEntry.grid(row=0,column=3,padx=8)




    billnumnerlabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',18,'bold')
                ,bg='#074463',fg='#fff')

    billnumnerlabel.grid(row=0,column=4,padx=20,pady=2)

    billnumnerEntry=Entry(customer_details_frame,font=('arial',15),bd=7, width=25)

    billnumnerEntry.grid(row=0,column=5,padx=8)



    searchButton=Button(customer_details_frame,text='Search',command=lambda:search_bill(billnumnerEntry) ,font=('arial',12,'bold')
                    ,bd=7,width=15)
    searchButton.grid(row=0,column=6,padx=20,pady=8)


    productsFrame = Frame(root)
    productsFrame.pack(side=TOP, fill=X)
    
    
    cosmeticsFrame = LabelFrame(productsFrame, text='Cosmetics', font=('times new roman', 18, 'bold'),
                                fg='gold', bd=8, relief=GROOVE, bg='#074463', width=25)
    cosmeticsFrame.grid(row=0, column=0)
    
    bathsoapLabel = Label(cosmeticsFrame, text='Bath soap', font=('times new roman', 18, 'bold'),
                          bg='#074463', fg='#fff')
    bathsoapLabel.grid(row=0, column=0, pady=9, padx=10)
    bathsoapEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    bathsoapEntry.grid(row=0, column=1, pady=9, padx=10, sticky='W')
    bathsoapEntry.insert(0,0)


    facecreamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 18, 'bold'),
                           bg='#074463', fg='#fff')
    facecreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky='W')
    facecreamEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    facecreamEntry.grid(row=1, column=1, pady=9, padx=10)
    facecreamEntry.insert(0,0)


    facewashLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 18, 'bold'),
                          bg='#074463', fg='#fff')
    facewashLabel.grid(row=2, column=0, pady=9, padx=10 )
    facewashEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    facewashEntry.grid(row=2, column=1, pady=9, padx=10, sticky='w')
    facewashEntry.insert(0,0)


    hairspratLabel = Label(cosmeticsFrame, text='Hair Sprat', font=('times new roman', 18, 'bold'),
                           bg='#074463', fg='#fff')
    hairspratLabel.grid(row=3, column=0, pady=9, padx=10)
    hairspartEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    hairspartEntry.grid(row=3, column=1, pady=9, padx=10, sticky='w')
    hairspartEntry.insert(0,0)


    hairgelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 18, 'bold'),
                          bg='#074463', fg='#fff')
    hairgelLabel.grid(row=4, column=0, pady=9, padx=10)
    hairgelEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    hairgelEntry.grid(row=4, column=1, pady=9, padx=10, sticky='w')
    hairgelEntry.insert(0,0)

    
    bodylotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 18, 'bold'),
                            bg='#074463', fg='#fff')
    bodylotionLabel.grid(row=5, column=0, pady=9, padx=10)
    bodylotionEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    bodylotionEntry.grid(row=5, column=1, pady=9, padx=10, sticky='w')
    bodylotionEntry.insert(0,0)
    
    
    groceryFrame = LabelFrame(productsFrame, text='Grocery', font=('times new roman', 18, 'bold'),
                              fg='gold', bd=8, relief=GROOVE, bg='#074463', width=40)
    groceryFrame.grid(row=0, column=1)
    
    
    
    riceLabel = Label(groceryFrame, text='Rice', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    riceLabel.grid(row=0, column=0, pady=9, padx=10)
    riceEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    riceEntry.grid(row=0, column=1, pady=9, padx=10, sticky='w')
    riceEntry.insert(0,0)


    oilLabel = Label(groceryFrame, text='Oil', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    oilLabel.grid(row=1, column=0, pady=9, padx=10)
    oilEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    oilEntry.grid(row=1, column=1, pady=9, padx=10, sticky='w')
    oilEntry.insert(0,0)
    
    
    daalLabel = Label(groceryFrame, text='Daal', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    daalLabel.grid(row=2, column=0, pady=9, padx=10)
    daalEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    daalEntry.grid(row=2, column=1, pady=9, padx=10, sticky='w')
    daalEntry.insert(0,0)
    
    aataLabel = Label(groceryFrame, text='Aata', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    aataLabel.grid(row=3, column=0, pady=9, padx=10)
    aataEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    aataEntry.grid(row=3, column=1, pady=9, padx=10, sticky='w')
    aataEntry.insert(0,0)
    
    MundalLabel = Label(groceryFrame, text='Mundal', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    MundalLabel.grid(row=4, column=0, pady=9, padx=10)
    MundalEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    MundalEntry.grid(row=4, column=1, pady=9, padx=10, sticky='w')
    MundalEntry.insert(0,0)
    
    MilkLabel = Label(groceryFrame, text='Milk', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    MilkLabel.grid(row=5, column=0, pady=9, padx=10)
    MilkEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    MilkEntry.grid(row=5, column=1, pady=9, padx=10, sticky='w')
    MilkEntry.insert(0,0)
    
    
    
      
      ############################################### #######################################
      #                              Drink frame start                                       #
      ####################################################################################### 
    ColddrinkFrame = LabelFrame(productsFrame, text=' Cold drink', font=('times new roman', 18, 'bold'),
                              fg='gold', bd=8, relief=GROOVE, bg='#074463', width=40)
    ColddrinkFrame.grid(row=0, column=2)
    
    
    
    mazaLabel = Label(  ColddrinkFrame, text='Maza', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    mazaLabel.grid(row=0, column=0, pady=9, padx=10)
    mazaEntry = Entry(ColddrinkFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    mazaEntry.grid(row=0, column=1, pady=9, padx=10, sticky='w')
    mazaEntry.insert(0,0)


    PepsiLabel = Label(ColddrinkFrame, text='Pepsi', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    PepsiLabel.grid(row=1, column=0, pady=9, padx=10)
    PepsiEntry = Entry(ColddrinkFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    PepsiEntry.grid(row=1, column=1, pady=9, padx=10, sticky='w')
    PepsiEntry.insert(0,0)
    
    
    SpriteLabel = Label(ColddrinkFrame, text='Sprite', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    SpriteLabel.grid(row=2, column=0, pady=9, padx=10)
    SpriteEntry = Entry(ColddrinkFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    SpriteEntry.grid(row=2, column=1, pady=9, padx=10, sticky='w')
    SpriteEntry.insert(0,0)
    
    
    CocaColaLabel = Label(ColddrinkFrame, text='CocaCola', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    CocaColaLabel.grid(row=3, column=0, pady=9, padx=10)
    CocaColaEntry = Entry(ColddrinkFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    CocaColaEntry.grid(row=3, column=1, pady=9, padx=10, sticky='w')
    CocaColaEntry.insert(0,0)
    
    
    FantaLabel = Label(ColddrinkFrame, text='Fanta', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    FantaLabel.grid(row=4, column=0, pady=9, padx=10)
    FantaEntry = Entry(ColddrinkFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    FantaEntry.grid(row=4, column=1, pady=9, padx=10, sticky='w')
    FantaEntry.insert(0,0)

    
    limkhaLabel = Label(ColddrinkFrame, text='  limkha', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    limkhaLabel.grid(row=5, column=0, pady=9, padx=10)
    limkhaEntry = Entry(ColddrinkFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    limkhaEntry.grid(row=5, column=1, pady=9, padx=10, sticky='w')
    limkhaEntry.insert(0,0)
      
      ############################################### #######################################
     #                              Drink frame end                                     #
      #######################################################################################
      
      
      
      
      ############################################### #######################################
      #                              Bill area start                                      #
      #######################################################################################
      
    billframe = Frame(productsFrame, bd=8, relief=GROOVE)
    billframe.grid(row=0, column=3,padx=10)

    billareaLabel = Label(billframe, text='Bill Area', font=('times new roman', 18, 'bold'), bd=7, relief=GROOVE)
    billareaLabel.pack(fill=X)

    scrollbar = Scrollbar(billframe, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)
    textarea = Text(billframe, height=22, width=80,yscrollcommand=scrollbar.set)
    textarea.pack() 
    scrollbar.config(command=textarea.yview)
    
        ############################################### #######################################
      #                              Bill area end                                      #
      #######################################################################################
      
         ############################################### #######################################
      #                               Bill menu start                                    #
      #######################################################################################
    
    billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 18, 'bold'),
                   fg='gold', bd=8, relief=GROOVE, bg='#074463', width=100)
    billmenuFrame.pack( pady=5)
    
  
      
     
      
      
    
    cosmeticsLabel= Label(billmenuFrame, text='Cosmetics Price', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff',width=20)
    cosmeticsLabel.grid(row=0, column=0, pady=9, padx=10,)
    cosmeticsEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    cosmeticsEntry.grid(row=0, column=1, pady=9, padx=10, sticky='w')

    
    groceryLabel= Label(billmenuFrame, text='Grocery Price', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff',width=20)
    groceryLabel.grid(row=1, column=0, pady=9, padx=10)
    groceryEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    groceryEntry.grid(row=1, column=1, pady=9, padx=10, sticky='w')


    drinkLabel= Label(billmenuFrame, text='drink Price', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff',width=20)
    drinkLabel.grid(row=2, column=0, pady=9, padx=10)
    drinkEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    drinkEntry.grid(row=2, column=1, pady=9, padx=10, sticky='w')



    cosmetictaxLabel= Label(billmenuFrame, text='Cosmetics  Tax', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    cosmetictaxLabel.grid(row=0, column=2, pady=9, padx=10)
    cosmetictaxEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    cosmetictaxEntry.grid(row=0, column=3, pady=9, padx=10, sticky='w')

    
    grocerytaxLabel= Label(billmenuFrame, text='Grocery Tax', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    grocerytaxLabel.grid(row=1, column=2, pady=9, padx=10)
    grocerytaxEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    grocerytaxEntry.grid(row=1, column=3, pady=9, padx=10, sticky='w')


    drinktaxLabel= Label(billmenuFrame, text='drinktax Tax', font=('times new roman', 18, 'bold'),
                      bg='#074463', fg='#fff')
    drinktaxLabel.grid(row=2, column=2, pady=9, padx=10)
    drinktaxEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
    drinktaxEntry.grid(row=2, column=3, pady=9, padx=10, sticky='w')
    
    
         ############################################### #######################################
      #                               Bill menu End                                  #
      #######################################################################################
    
    
    
    
    
    
    buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
    buttonFrame.grid(row=0,column=4,rowspan=3)
    
    totalButton = Button(buttonFrame, command=lambda: total(bathsoapEntry, facecreamEntry, facewashEntry, hairspartEntry, hairgelEntry, bodylotionEntry, riceEntry, oilEntry, daalEntry, aataEntry, MundalEntry, MilkEntry, cosmeticsEntry, groceryEntry,mazaEntry, PepsiEntry,  SpriteEntry,CocaColaEntry, FantaEntry,limkhaEntry, cosmetictaxEntry,grocerytaxEntry,drinktaxEntry), text="Total", font=('arial', 16, 'bold'), bg='#57a1f8', fg='black', bd=5, width=8, pady=10)
    totalButton.grid(row=0, column=0, pady=20, padx=5)
   
    billlButton = Button(buttonFrame, text="Bill", font=('arial', 16, 'bold'),
                     bg='#57a1f8', fg='black',bd=5,width=8,pady=10,command=lambda: bill_area(nameEntry, phoneEntry,cosmeticsEntry,groceryEntry,drinkEntry,bathsoapEntry,facecreamEntry,facewashEntry,hairspartEntry,bodylotionEntry,riceEntry,oilEntry,daalEntry,aataEntry,hairgelEntry,MundalEntry,MilkEntry,mazaEntry,PepsiEntry,SpriteEntry,CocaColaEntry
              ,FantaEntry,limkhaEntry,cosmetictaxEntry,grocerytaxEntry,drinktaxEntry, totalbill))
    billlButton.grid(row=0, column=1,pady=20,padx=5)
    
    
    emailButton = Button(buttonFrame, text="Email", font=('arial', 16, 'bold'),
                     bg='#57a1f8', fg='black',bd=5,width=8,pady=10)
    emailButton.grid(row=0, column=2,pady=20,padx=5)
    
    printButton = Button(buttonFrame, text="Print",command=print_bill, font=('arial', 16, 'bold'),
                     bg='#57a1f8', fg='black',bd=5,width=8,pady=10)
    printButton.grid(row=0, column=3,pady=20,padx=5)
    
    clerButton = Button(buttonFrame, text="Cler",font=('arial', 16, 'bold'),
                     bg='#57a1f8',command=lambda:clear(bathsoapEntry, facecreamEntry, facewashEntry, hairspartEntry, hairgelEntry, bodylotionEntry, riceEntry, oilEntry, daalEntry, aataEntry, MundalEntry, MilkEntry, mazaEntry, PepsiEntry, SpriteEntry, CocaColaEntry, FantaEntry, limkhaEntry,phoneEntry, nameEntry ,billnumnerEntry), fg='black',bd=5,width=8,pady=10)
    clerButton.grid(row=0, column=4,pady=20,padx=5)
    
    exitButton = Button(buttonFrame, text="Exit",command=lambda:exit_program(root), font=('arial', 16, 'bold'),
                     bg='#57a1f8', fg='black',bd=5,width=8,pady=10)
    exitButton.grid(row=0, column=5,pady=20,padx=5)
    
    
    copyrightlabel = Label(root, text="Copyright © 2024 Develop by ", font=('times new roman', 20, 'bold'), bg="#074463", fg='gold', bd=16, relief=GROOVE,height=30)
    copyrightlabel.pack(side=TOP, fill=X)

    root.mainloop()
    
    if __name__ == "__main__":
     main()