while True:
 Mot_de_passe= input("Entrez votre mot de passe")
 Caracteres_speciaux=["@","#","$","*","%","!","?"]
 Contient_special=False
 for lettre in Mot_de_passe:
     if lettre in Caracteres_speciaux:
        Contient_special=True
 if len (Mot_de_passe)< 8:
    print("Mot de passe trop court !")
 elif Contient_special==False:
    print ("Mot de passe insuffisant")
 else:
    print("Mot de passe validée !")
    break