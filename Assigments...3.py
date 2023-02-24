# Index Number: 6942721


# This shows the different type of brands available and its corresponding number
Car_brands = {1:'Toyota', 2 :'Nissan', 3:'Kia', 4:'Audi', 5:'Mistubishi',\
6:'BMW', 7:'Ford', 8:'Honda', 9:'Hyundai', 10:'Mercedes'}

# it shows you all the models of Car brands available and its prices
Toyota = {'Avalon': 50000, 'Camry':40000, 'Corolla':50000}
Nissan = {'Juke':30000, 'Qashqai':485855, 'Navara':505943}
Kia = {'Sportage':30000, 'Optimal':606796, 'Morning':500578}
Audi = {'Q7':47473, 'A3':34753,'Q4':40000}
Mistubishi = {'L200':4868359, 'Pajero':500000, 'Outlander':50000}
BMW = {'i7':50000, 'X4':30000, 'XM':40000}
Ford = {'Ranger':90000, 'Explorer':40000, 'Fusion':50000}
Honda = {'Civic':50000, 'CRV':50000, 'Accord':603545}
Hyundai = {'Elantra':50000, 'Sonata':40000, 'Santa fe':40000}
Mercedes ={'G-Wagon':400000, 'CLS300':590000, 'E300':402044}

# It allows the user/customer to input numbers from 1 to 10  of the
# available car brands i.e. each number corresponds to a car brand
car_preference = input('Hello, welcome to MNT Limited!\n\n\
What car would you like to purchase?\n\
1.  Toyota\n2.  Nissan\n3.  Kia\n4.  Audi\n5.  Mistubishi\n6.  BMW\n\
7.  Ford\n8.  Honda\n9.  Hyundai\n10. Mercedes\n\n\
Select the number that corresponds to your car brand of interest: ')


if car_preference == '1':
    Toyota_preference = input('Which model of Toyota would you like to \
purchase?\n\
a. Avalon\nb. Camry\nc. Corolla\n\n\
Please choose the letter that corresponds to your model of interest: ')
    if Toyota_preference == 'a':
        print('\n\nPerfect Choice! The price of Avalon is GHS '\
+ str( Toyota['Avalon']))
    elif Toyota_preference == 'b':
         print('\n\nPerfect Choice! The price of Camry is GHS '\
+ str( Toyota['Camry']))
    elif Toyota_preference == 'c':
         print('\n\nPerfect Choice! The price of Corolla is GHS '\
+ str( Toyota['Corolla']))
    else:
        print('\n\nWe are sorry for the inconvinience but your input is \
invalid. Please try again!!')
    
elif car_preference == '2':
    Nissan_preference = input('Which model of Nissan would you like to \
purchase?\n\
a. Juke\nb. Qashqai \nc. Navara\n\n\
Please choose the letter that corresponds to your model of interest: ')
    if Nissan_preference == 'a':
        print('\n\nPerfect Choice! The price of Juke is GHS '\
+ str( Nissan['Juke'])) 
    elif Nissan_preference == 'b':
        print('\n\nPerfect Choice! The price of Qashqai is GHS '\
+ str( Nissan['Qashqai']))
    elif Nissan_preference == 'c':
        print('\n\nPerfect Choice! The price of Navara is GHS '\
+ str( Nissan['Navara']))
    else:
        print('\n\nWe are sorry for the inconvinience but your input is \
invalid. Please try again!!')


elif car_preference == '3':  
    Kia_preference = input('Which model of Kia would you like to \
purchase?\n\
a. Sportage\nb. Optimal\nc. Morning\n\n\
Please choose the letter that corresponds to your model of interest: ')
    if Kia_preference == 'a':
        print('\n\nPerfect Choice! The price of Sportage is GHS '\
+ str( Kia['Sportage']))
    elif Kia_preference == 'b':
        print('\n\nPerfect Choice! The price of Optimal is GHS '\
+ str( Kia['Optimal']))
    elif Kia_preference == 'c':
        print('\n\nPerfect Choice! The price of Morning is GHS '\
+ str( Kia['Morning']))
    else:
        print('\n\nWe are sorry for the inconvinience but your input is \
invalid. Please try again!!')

elif car_preference == '4': 
    Audi_preference = input('Which model of Audi would you like to \
purchase?\n\
a. Q7 \nb. A3 \nc. Q4\n\n\
Please choose the letter that corresponds to your model of interest: ')
    if Audi_preference == 'a':
        print('\n\nPerfect Choice! The price of Q7 is GHS '\
+ str( Audi['Q7']))
    elif Audi_preference == 'b':
        print('\n\nPerfect Choice! The price of A3 is GHS '\
+ str( Audi['A3']))
    elif Audi_preference == 'c':
        print('\n\nPerfect Choice! The price of Q4 is GHS '\
+ str( Audi['Q4']))
    else:
        print('\n\nWe are sorry for the inconvinience but your input is \
invalid. Please try again!!')


elif car_preference == '5':  
    Mistubishi_preference = input('Which model of Mitsubishi would you like to \
purchase?\n\
a. L200 \nb. Pajero \nc. Outlander\n\n\
Please choose the letter that corresponds to your model of interest: ')
    if Mistubishi_preference == 'a':
        print('\n\nPerfect Choice! The price of L200 is GHS '\
+ str( Mistubishi['L200']))
    elif Mistubishi_preference == 'b':
        print('\n\nPerfect Choice! The price of Pajero is GHS '\
+ str( Mistubishi['Pajero']))
    elif Mistubishi_preference == 'c':
        print('\n\nPerfect Choice! The price of Outlander is GHS '\
+ str( Mistubishi['Outlander']))
    else:
        print('\n\nWe are sorry for the inconvinience but your input is \
invalid. Please try again!!')
        
elif car_preference == '6':
    BMW_preference = input('Which model of BMW would you like to \
purchase?\n\
a. i7 \nb. X4 \nc. XM\n\n\
Please choose the letter that corresponds to your model of interest: ')
    if BMW_preference == 'a':
        print('\n\nPerfect Choice! The price of i7 is GHS '\
+ str( BMW['i7']))
    elif BMW_preference == 'b':
        print('\n\nPerfect Choice! The price of X4 is GHS '\
+ str( BMW['X4']))
    elif BMW_preference == 'c':
        print('\n\nPerfect Choice! The price of XM is GHS '\
+ str( BMW['XM']))
    else:
        print('\n\nWe are sorry for the inconvinience but your input is \
invalid. Please try again!!')
        
elif car_preference == '7':
    Ford_preference = input('Which model of Ford would you like to \
purchase?\n\
a. Ranger \nb. Explorer \nc. Fusion\n\n\
Please choose the letter that corresponds to your model of interest: ')
    if Ford_preference == 'a':
        print('\n\nPerfect Choice! The price of Ranger is GHS '\
+ str( Ford['Ranger']))
    elif Ford_preference == 'b':
        print('\n\nPerfect Choice! The price of Explorer is GHS '\
+ str( Ford['Explorer']))
    elif Ford_preference == 'c':
        print('\n\nPerfect Choice! The price of Fusion is GHS '\
+ str( Ford['Fusion']))
    else:
        print('\n\nWe are sorry for the inconvinience but your input is \
invalid. Please try again!!')

elif car_preference == '8':
    Honda_preference = input('Which model of Honda would you like to \
purchase?\n\
a. Civic \nb. CRV \nc. Accord\n\n\
Please choose the letter that corresponds to your model of interest: ')
    if Honda_preference == 'a':
        print('\n\nPerfect Choice! The price of Civic is GHS '\
+ str( Honda['Civic']))
    elif Honda_preference == 'b':
        print('\n\nPerfect Choice! The price of CRV is GHS '\
+ str( Honda['CRV']))
    elif Honda_preference == 'c':
        print('\n\nPerfect Choice! The price of Accord is GHS '\
+ str( Honda['Accord']))
    else:
        print('\n\nWe are sorry for the inconvinience but your input is \
invalid. Please try again!!')

elif car_preference == '9':
    Hyundai_preference = input('Which model of Hyundai would you like to \
purchase?\n\
a. Elantra \nb. Sonata \nc. Santa fe\n\n\
Please choose the letter that corresponds to your model of interest: ')
    if Hyundai_preference == 'a':
        print('\n\nPerfect Choice! The price of Elantra is GHS '\
+ str( Hyundai['Elantra']))
    elif Hyundai_preference == 'b':
        print('\n\nPerfect Choice! The price of Sonata is GHS '\
+ str( Hyundai['Sonata']))
    elif Hyundai_preference == 'c':
        print('\n\nPerfect Choice! The price of Santa fe is GHS '\
+ str( Hyundai['Santa fe']))
    else:
        print('\n\nWe are sorry for the inconvinience but your input is \
invalid. Please try again!!')

elif car_preference == '10':
    
    Mercedes_preference = input('Which model of Mercedes would you like to \
purchase?\n\
a. G-Wagon \nb. CLS300 \nc. E300\n\n\
Please choose the letter that corresponds to your model of interest: ')
    if Mercedes_preference == 'a':
        print('\n\nPerfect Choice! The price of G-Wagon is GHS '\
+ str( Mercedes['G-Wagon']))
    elif Mercedes_preference == 'b':
        print('\n\nPerfect Choice! The price of CLS300 is GHS '\
+ str( Mercedes['CLS300']))
    elif Mercedes_preference == 'c':
        print('\n\nPerfect Choice! The price of E300 is GHS '\
+ str( Mercedes['E300']))
    else:
        print('\n\nWe are sorry for the inconvinience but your input is \
invalid. Please try again!!')
        
else:
    print('\n\nWe are sorry for the inconvinience but your input is \
invalid. Please try again ! !')

#Github Account : github.com/mntiamoah546/Data-Structures
        