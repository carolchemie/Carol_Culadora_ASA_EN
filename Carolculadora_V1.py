class bcolors:
    red = '\033[91m'
    green = '\033[92m'
    bold = '\033[1m'
    reset = '\033[0m'
r1 = str('y').upper()
r2 = str('n').upper()
print(' ')
print(
    f'{bcolors.bold} CAROLCULADORA -  THEORETICAL YIELD CALCULATOR FOR THE SYNTHESIS OF ACETYLSALICYLIC ACID {bcolors.reset}')
print(" ")

asa = float(input('Type the required final yield of ASA "in g": '))
print("\t" + 'Calculating to ', asa, "g of ASA.", 'Correct? Type ',
      f"{bcolors.green}(Y) {bcolors.reset}" 'to continue or '
      ''f"{bcolors.green}(N) {bcolors.reset}" 'to type again.')
c = str(input("\t" + 'Type (Y/N): ')).upper()

while c == r2:
    asa = float(input('Type the required final yield of ASA "in g": '))
    print("\t" + 'Calculating to ', asa, "g of ASA.", 'Correct? Type ',
          f"{bcolors.green}(Y) {bcolors.reset}" 'to continue or '
          ''f"{bcolors.green}(N) {bcolors.reset}" 'to type again.')
    c = str(input("\t" + 'Type (Y/N): ')).upper()
print(' ')
print('RESULT: ')

for r1 in c:
    x = round(asa) / 180.158
    d = x * (138.121)
    print('Salicilic acid: ', round(d), 'g')
    z = (x * 3) * 94.527
    print('Acetic anhydride: ', round(z), 'mL')
    w = (x / 4) * 53.595
    print('H2SO4: ', round(w), 'mL, or', round(w * 20), 'drops')
    print("\t" + 'Create a report? Type' f"{bcolors.green}(Y) {bcolors.reset}" 'to continue or '
          ''f"{bcolors.green}(N) {bcolors.reset}" 'to finish.')
cc = str(input("\t" + 'Type (Y/N): ')).upper()

if cc == r1:
    print(' ')
    print('REPORT:')
    print(round(d), ('g'), round(x), ('mols of salicylic acid is added an Erlenmeyer flask. After this'), round(z), ('mL'), round(x*3), ('mols of acetic\n '
        'anhydride, followed by'), round(w), ('mL or'), round(w*20), ('drops of conc. H2SO4 use a dropper, H2SO4 is highly corrosive and \n'
        'swirl the flask gently until the salicylic acid dissolves. Heat the flask gently on the steam bath for\n '
        'at least 10 minutes. Allow the flask to cool to room temperature. If acetylsalicylic acid does not\n '
        'begin to crystallize out, scratch the walls of the flask with a glass rod. Cool the mixture slightly in\n '
        'an ice bath until crystallization is completed. The product will appear as a solid mass when crystallization is completed.'))
    print(' ')
    print(
        f'{bcolors.red}The theoretical yield is referred to in this calculation. Practical results may vary. {bcolors.reset}')
    print(' ')
    print('REFERENCE:')
    print('Palleros DR (2000). Experimental organic chemistry. New York: John Wiley & Sons. p. 494. ISBN 978-0-471-28250-1.')
    print('Created by @carol.chemie')

if cc == r2:
    print(' ')
    print(
        f'{bcolors.red}The theoretical yield is referred to in this calculation. Practical results may vary. {bcolors.reset}')
    print(' ')
    print('REFERENCE:')
    print('Palleros DR (2000). Experimental organic chemistry. New York: John Wiley & Sons. p. 494. ISBN 978-0-471-28250-1.')
    print('Created by @carol.chemie on 07/2022')

elif cc!= r1 and cc != r2:
    print("ERROR!")
