from tkinter import *
window = Tk()
window.configure(background="black")

def click():
    wn = Tk()
    wn.title("Chemistry")
    wn.configure(background="black")
    
    def OrganicCommand():
        window1 = Tk()
        window1.configure(background="black")
        
        def SubmitButton():
            entered_text = textentry.get()
            output.delete(0.0, END)
            try:
                Word = Words[entered_text]
            except:
                Word = "Sorry we don't have the definition to that word"
            output.insert(END, Word)
        
        MT = Label(window1, text="CHEMISTRY", bg="black", fg="white", font="castellar 20 bold")
        MT.pack()
        
        LT = Label(window1, text="\nORGANIC", bg="black", fg="white", font="castellar 15 bold")
        LT.pack()
        
        term = Label(window1, text="\nTERM:", bg="black", fg="white", font="none 14 bold")
        term.pack()
        
        textentry = Entry(window1, width=30, bg="white")
        textentry.pack()
        
        Submit = Button(window1, text="Submit", width=6, command=SubmitButton)
        Submit.pack()
        
        definition = Label(window1, text="\nDEFINITION", bg="black", fg="white", font="none 14 bold")
        definition.pack()
        
        output = Text(window1, width=80, height=6, wrap=WORD, background="white")
        output.pack()
        
        Words = {
            "Hydrocarbon":"Organic compounds that consists of hydrogen and carbon only", "Homologous series":"A series of organic compounds that can be described by the same general formula OR in whch one member differs from the next with a CH2 group", "Saturated compounds":"Compounds in which there are no multiple bonds between C atoms in their hydrocarbon chain", "Unsaturated compounds":"Compounds with one or more multiple bonds between C atoms in their hydrocarbon chain", "Functional group":"A bond or an atom or a group of atoms that determine the physical and chemical properties of a group of organic compounds", "Structural isomer":"Organic molecules with the same molecular formula but different structural formulae", "Chain isomer":"Same molecular formula but different types of chains formulae", "Position isomer":"Same molecular formular but different positions of the side chain, substituents of functional groups on the parent chain", "Functional isomer":"Same molecular formula but different functional groups"
            }
    
    def ReactionsCommand():
        window2 = Tk()
        window2.configure(background="black")
        
        def SubmitButton():
            entered_text = textentry.get()
            output.delete(0.0, END)
            try:
                Word = Words[entered_text]
            except:
                Word = "Sorry we don't have the definition to that word"
            output.insert(END, Word)
            
        MT = Label(window2, text="CHEMISTRY", bg="black", fg="white", font="castellar 20 bold")
        MT.pack()
            
        LT = Label(window2, text="\nREACTIONS", bg="black", fg="white", font="castellar 15 bold")
        LT.pack()
            
        term = Label(window2, text="\nTERM:", bg="black", fg="white", font="none 14 bold")
        term.pack()
            
        textentry = Entry(window2, width=30, bg="white")
        textentry.pack()
        
        Submit = Button(window2, text="Submit", width=6, command=SubmitButton)
        Submit.pack()
        
        definition = Label(window2, text="\nDEFINITION", bg="black", fg="white", font="none 14 bold")
        definition.pack()
        
        output = Text(window2, width=80, height=6, wrap=WORD, background="white")
        output.pack()
        
        Words = {
            "Reaction rate":"The change in the concentration of reactants or products per unit time", "Collision theory":"A model that explains reaction rate as the result of particles colliding with a certain minimum energy to form products", "Catalyst":"A substance that increases the rate of a chemical reaction without itself undergoing change", "Open system":"A system that continuously interacts with environment","Closed system":"A system that is isolated from its surroundings","Reverse reaction":"A reaction that is reversible when products can be converted back to reactants","Chemical equilibrium":"It is a dynamic equilibrium when the rate of the forward reaction equals the rate of the reverse reaction","LeChatelier's principle":"When the equilibrium in a closed system is disturbed, the system will re-instate a new equilibrium by favouring the reaction that will oppose the disturbance","Acid":"Arrhenius theory: A substance that produces hydrogen ions in water. \nLowry.Bronsted theory:A proton donor.","Base":"Arrhenius:A substance that produces hydroxide ions in water.\nLowryBronsted:A proton acceptor.","Kw":"The equilibrium constant for the ionisation of water-the ionic product of water"
            }
    def ChemistryCommand():
        window3 = Tk()
        window3.configure(background="black")
        
        def SubmitButton():
            entered_text = textentry.get()
            output.delete(0.0, END)
            try:
                Word = Words[entered_text]
            except:
                Word = "Sorry we don't have the definition to that word"
            output.insert(END, Word)
        
        MT = Label(window3, text="CHEMISTRY", bg="black", fg="white", font="castellar 20 bold")
        MT.pack()
        
        LT = Label(window3, text="\nREACTIONS", bg="black", fg="white", font="castellar 15 bold")
        LT.pack()
        
        term = Label(window3, text="\nTERM:", bg="black", fg="white", font="none 14 bold")
        term.pack()
        
        textentry = Entry(window3, width=30, bg="white")
        textentry.pack()
        
        Submit = Button(window3, text="Submit", width=6, command=SubmitButton)
        Submit.pack()
        
        definition = Label(window3, text="\nDEFINITION", bg="black", fg="white", font="none 14 bold")
        definition.pack()
        
        output = Text(window3, width=80, height=6, wrap=WORD, background="white")
        output.pack()
        
        Words = {
            "Galvanic cell":"A cell in which chemical energy is converted into electrical energy","Electrolytic cell":"A cell in which electrical energy is converted into chemical energy","Oxidation":"Loss of electrons \nIncrease in oxidation number","Reduction":"Gain of electrons\nDecrease in oxidation number","Anode":"The electrode where oxidation takes place","Cathode":"The elecrode where reduction takes place","electrolyte":"A substance of which the aqueous solution contains ions or \nA substance that dissolves in water to give a solution that conducts electricity","Electrolysis":"The chemical process in which electrical energy is converted to chemical energy OR \nThe use of electrical energy to produce a chemical change"
            }
        
    def IndustryCommand():
        window4 = Tk()
        window4.configure(background="black")
        
        def SubmitButton():
            entered_text = textentry.get()
            output.delete(0.0, END)
            try:
                Word = Words[entered_text]
            except:
                Word = "Sorry we don't have the definition to that word"
            output.insert(END, Word)
            
        MT = Label(window4, text="CHEMISTRY", bg="black", fg="white", font="castellar 20 bold")
        MT.pack()
        
        LT = Label(window4, text="\nREACTIONS", bg="black", fg="white", font="castellar 15 bold")
        LT.pack()
        
        term = Label(window4, text="\nTERM:", bg="black", fg="white", font="none 14 bold")
        term.pack()
        
        textentry = Entry(window4, width=30, bg="white")
        textentry.pack()
        
        Submit = Button(window4, text="Submit", width=6, command=SubmitButton)
        Submit.pack()
        
        definition = Label(window4, text="\nDEFINITION", bg="black", fg="white", font="none 14 bold")
        definition.pack()
        
        output = Text(window4, width=80, height=6, wrap=WORD, background="white")
        output.pack()
        
        Words = {
            "Eutrophication":"The process by which an ecosystem becomes enriched with inorganic plant nutrients resulting in excessive plant growth"
            }
        
    organic = Button(wn, text="Organic", width=7, command=OrganicCommand)
    organic.pack()
    Reactions = Button(wn, text="Reactions", width=9, command=ReactionsCommand)
    Reactions.pack()
    ElectroChemistry = Button(wn, text="ElectroChemistry", width=16, command=ChemistryCommand)
    ElectroChemistry.pack()
    Industry = Button(wn, text="Industry", width=8, command=IndustryCommand)
    Industry.pack()
    
def flick():
    wnd = Tk()
    wnd.title("Physics")
    wnd.configure(background="black")
    
    def MomentumButton():
        wnd1 = Tk()
        wnd1.title("Physics")
        wnd1.configure(background="black")
        
        def SubmitButton():
            entered_text = textentry.get()
            output.delete(0.0, END)
            
            try:
                Word = Words[entered_text]
            except:
                Word = "Sorry we do not have the definition for your term"
            output.insert(END, Word)
        
        MT = Label(wnd1, text="Physics", bg="black", fg="white", font="castellar 20 bold")
        MT.pack()
        
        LT = Label(wnd1, text="MOMENTUM", bg="black", fg="white", font="castellar 15 bold")
        LT.pack()
        
        Term = Label(wnd1, text="\nTERM:", bg="black", fg="white", font="castellar 14 bold")
        Term.pack()
        
        textentry = Entry(wnd1, width=80, bg="white")
        textentry.pack()
        
        Submit = Button(wnd1, text="Submit", width=6, command=SubmitButton)
        Submit.pack()
        
        Definition = Label(wnd1, text="Definition:", width=10, bg="black", fg="white", font="castellar 14 bold")
        Definition.pack()
        
        output = Text(wnd1, width=80, height=5, wrap=WORD, background="white")
        output.pack()
        
        Words = {
            "Momentum":"The product of of an objets mass and velocity","Newton's second law":"In terms of momentum Newton's second law states that the net force acting on an object is equal to the rate of change of the momentum of the object in the direction of the net force","Impulse":"The product of the net force on an object and the time the net force acts o the object","Conservation of linear momentum":"The total linear momentum of an isolated system remains constant"
            }
        
    def WorkButton():
        wnd2 = Tk()
        wnd2.title("Physics")
        wnd2.configure(background="black")
            
        def SubmitButton():
            entered_text = textentry.get()
            output.delete(0.0, END)
            
            try:
                Word = Words[entered_text]
            except:
                Word = "Sorry we do not have the definition for your term"
            output.insert(END, Word)
                
        MT = Label(wnd2, text="Physics", bg="black", fg="white", font="castellar 20 bold")
        MT.pack()
        
        LT = Label(wnd2, text="Work", bg="black", fg="white", font="castellar 15 bold")
        LT.pack()
        
        Term = Label(wnd2, text="\nTERM:", bg="black", fg="white", font="castellar 14 bold")
        Term.pack()
        
        textentry = Entry(wnd2, width=80, bg="white")
        textentry.pack()
        
        Submit = Button(wnd2, text="Submit", width=6, command=SubmitButton)
        Submit.pack()
        
        Definition = Label(wnd2, text="Definition:", width=10, bg="black", fg="white", font="castellar 14 bold")
        Definition.pack()
        
        output = Text(wnd2, width=80, height=5, wrap=WORD, background="white")
        output.pack()
        
        Words = {
            "Work-energy theorem":"The work done on an object by a net force is equal to the change in the object's kinetic energy","Work":"The constant force F as F xcos0, where F is the magnitude of the force, x is the magnitue of the displacement and 0 the angle between the force and the dispalcement.","Conservative force":"The force for which the work done in a moving object between two points is independent of the path taken","Non-conservative force":"The force for which work is done in a moving object between two points depends on the path taken","Principle of conservation of mechanical energy":"The total mechanical energy in an isolated system remains constant","Power":"The rate at which work is done or energy is expended"
            }

    def ElectricityButton():
        wnd3 = Tk()
        wnd3.title("Physics")
        wnd3.configure(background="black")
            
        def SubmitButton():
            entered_text = textentry.get()
            output.delete(0.0, END)
            
            try:
                Word = Words[entered_text]
            except:
                Word = "Sorry we do not have the definition for your term"
            output.insert(END, Word)
                
        MT = Label(wnd3, text="Physics", bg="black", fg="white", font="castellar 20 bold")
        MT.pack()
        
        LT = Label(wnd3, text="Electricity", bg="black", fg="white", font="castellar 15 bold")
        LT.pack()
        
        Term = Label(wnd3, text="\nTERM:", bg="black", fg="white", font="castellar 14 bold")
        Term.pack()
        
        textentry = Entry(wnd3, width=80, bg="white")
        textentry.pack()
        
        Submit = Button(wnd3, text="Submit", width=6, command=SubmitButton)
        Submit.pack()
        
        Definition = Label(wnd3, text="Definition:", width=10, bg="black", fg="white", font="castellar 14 bold")
        Definition.pack()
        
        output = Text(wnd3, width=80, height=5, wrap=WORD, background="white")
        output.pack()
        
        Words = {
            "Coulomb's law":"The magnitude of the electrostatic force exerted by one point charge on another point charge is directly proportional to the magnitudes of the charges and inversely proportional to the square distance between them","Electric field at a point":"The electric field at a point is the electrostatic force experienced per unit charge placed at that point","Ohm's law":"The potential difference across a conductor is directly proportional to the current in the conductor at constant temperature","Power":"The rate at which work is done","rms":"The rms value of AC is the direct current/voltage which dissipitates the same amount of energy as AC"
            }
        
    def WavesButton():
        wnd4 = Tk()
        wnd4.title("Physics")
        wnd4.configure(background="black")
            
        def SubmitButton():
            entered_text = textentry.get()
            output.delete(0.0, END)
            
            try:
                Word = Words[entered_text]
            except:
                Word = "Sorry we do not have the definition for your term"
            output.insert(END, Word)
                
        MT = Label(wnd4, text="Physics", bg="black", fg="white", font="castellar 20 bold")
        MT.pack()
        
        LT = Label(wnd4, text="Waves", bg="black", fg="white", font="castellar 15 bold")
        LT.pack()
        
        Term = Label(wnd4, text="\nTERM:", bg="black", fg="white", font="castellar 14 bold")
        Term.pack()
        
        textentry = Entry(wnd4, width=80, bg="white")
        textentry.pack()
        
        Submit = Button(wnd4, text="Submit", width=6, command=SubmitButton)
        Submit.pack()
        
        Definition = Label(wnd4, text="Definition:", width=10, bg="black", fg="white", font="castellar 14 bold")
        Definition.pack()
        
        output = Text(wnd4, width=80, height=5, wrap=WORD, background="white")
        output.pack()
        
        Words = {
            "Doppler effect":"The change in frequency of the sound detected by a listener because the sound source and the listener have different velocities relative to the medium of the sound propagation"
            }
    def OpticsButton():
        wnd5 = Tk()
        wnd5.title("Physics")
        wnd5.configure(background="black")
            
        def SubmitButton():
            entered_text = textentry.get()
            output.delete(0.0, END)
            
            try:
                Word = Words[entered_text]
            except:
                Word = "Sorry we do not have the definition for your term"
            output.insert(END, Word)
                
        MT = Label(wnd5, text="Physics", bg="black", fg="white", font="castellar 20 bold")
        MT.pack()
        
        LT = Label(wnd5, text="Optics", bg="black", fg="white", font="castellar 15 bold")
        LT.pack()
        
        Term = Label(wnd5, text="\nTERM:", bg="black", fg="white", font="castellar 14 bold")
        Term.pack()
        
        textentry = Entry(wnd5, width=80, bg="white")
        textentry.pack()
        
        Submit = Button(wnd5, text="Submit", width=6, command=SubmitButton)
        Submit.pack()
        
        Definition = Label(wnd5, text="Definition:", width=10, bg="black", fg="white", font="castellar 14 bold")
        Definition.pack()
        
        output = Text(wnd5, width=80, height=5, wrap=WORD, background="white")
        output.pack()
        
        Words = {
            "Photoelectric effect":"The process whereby electrons are ejected from a metal surface when light of suitable frequency is incident on that surface","Threshold frequency":"The minimum frequency of light needed to emit electrons from a certain metal surface","Work function":"The work function of a metal is the minimum energy that an electron in the metal needs to be emitted from a meatl surface"
            }
    
    Momentum = Button(wnd, text="Momentum", width=8, command=MomentumButton)
    Momentum.pack()
    
    Work = Button(wnd, text="Work", width=4, command=WorkButton)
    Work.pack()
    
    Electricity = Button(wnd, text="Electricity", width=11, command=ElectricityButton)
    Electricity.pack()
    
    Waves = Button(wnd,text="Waves", width=5, command=WavesButton)
    Waves.pack()
    
    Optics = Button(wnd, text="Optics", width=6, command=OpticsButton)
    Optics.pack()
    

label = Label(window, text="PHYSICS DICTIONARY", bg="black", fg="yellow", font="castellar 20 bold")
label.pack()

chembutton = Button(window, text="Chemistry", width=10, command=click)
chembutton.pack()

phybutton = Button(window, text="Physics", width=7, command=flick)
phybutton.pack()