import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import requests

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# local_css("style.css")

API_URL = " https://my-api-app-ltqnoxdklq-ew.a.run.app/"

st.write("""
# 🏘️ Belgian House Price Prediction

This app predicts the **Belgian House Price**!
""")
st.write('---')

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')
# st.sidebar.markdown("*Streamlit* is **really** ***cool***.")
# st.sidebar.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors] and :red-background[highlight] text.''')
city = st.sidebar.selectbox("**City** :cityscape: ",('Aalst', 'Aalter',
'Affligem',
'Amay',
'Andenne',
'Anderlecht',
'Ans',
'Antwerpen',
'Anzegem',
'Arlon',
'Asse',
'Assenede',
'Ath',
'Aubange',
'Auderghem',
'Avelgem',
'Awans',
'Aywaille',
'Bastogne',
'Beauraing',
'Berchem-Sainte-Agathe',
'Bergen',
'Bertrix',
'Beveren',
'Bierbeek',
'Binche',
'Blankenberge',
'Boechout',
'Bonheiden',
'Borgloon',
'Bornem',
'Bouillon',
'Boussu',
"Braine-l'Alleud",
'Braine-le-Château',
'Braives',
'Brasschaat',
'Bredene',
'Brugge',
'Brussel',
'Brussels',
'Bruxelles',
'Buggenhout',
'Charleroi',
'Chaudfontaine',
'Chaumont-Gistoux',
'Châtelet',
'Ciney',
'Court-St.-Étienne',
'Damme',
'De Haan',
'Deerlijk',
'Deinze',
'Dendermonde',
'Dessel',
'Destelbergen',
'Diepenbeek',
'Diksmuide',
'Dilbeek',
'Dinant',
'Dour',
'Durbuy',
'Eeklo',
'Enghien',
'Esneux',
'Estaimpuis',
'Etterbeek',
'Evere',
'Evergem',
'Fleurus',
'Flémalle',
'Frameries',
'Frasnes-lez-Anvaing',
'Frasnes-lez-Gosselies',
'Galmaarden',
'Ganshoren',
'Gavere',
'Geel',
'Gembloux',
'Genappe',
'Gent',
'Geraardsbergen',
'Gerpinnes',
'Gooik',
'Grez-Doiceau',
'Grimbergen',
'Haacht',
'Halle',
'Ham-sur-Heure-Nalinnes',
'Hamme',
'Hannut',
'Harelbeke',
'Hasselt',
'Hechtel-Eksel',
'Heist-op-den-Berg',
'Herent',
'Herentals',
'Herne',
'Herstal',
'Herzele',
'Hoegaarden',
'Hoeilaart',
'Honnelles',
'Hotton',
'Huy',
'Ieper',
'Incourt',
'Ingelmunster',
'Ixelles',
'Izegem',
'Jabbeke',
'Jette',
'Kapelle-op-den-Bos',
'Keerbergen',
'Knokke-Heist',
'Koekelberg',
'Koerich',
'Kortemark',
'Kortrijk',
'Kraainem',
'La Hulpe',
'La Louvière',
'Lasne',
'Lebbeke',
'Lede',
'Leeuw-Saint-Pierre',
'Lendelede',
'Lessines',
'Leuven',
'Libin',
'Libramont-Chevigny',
'Liedekerke',
'Lier',
'Lievegem',
'Linkebeek',
'Liège',
'Lobbes',
'Lochristi',
'Lokeren',
'Londerzeel',
'Machelen',
'Maldegem',
'Manage',
'Marche-en-Famenne',
'Mechelen',
'Meise',
'Melle',
'Merelbeke',
'Messancy',
'Middelkerke',
'Mons',
'Mont-Saint-Guibert',
'Morlanwelz',
'Mouscron',
'Namur',
'Nandrin',
'Neufchâteau',
'Neupré',
'Nieuwpoort',
'Ninove',
'Nivelles',
'Oostende',
'Oosterzele',
'Oostkamp',
'Opwijk',
'Orp-Jauche',
'Ottignies-Louvain-la-Neuve',
'Oud-Heverlee',
'Oudenaarde',
'Oupeye',
'Overijse',
'Paliseul',
'Pepinster',
'Pittem',
'Pont-à-Celles',
'Poperinge',
'Profondeville',
'Putte',
'Puurs-Sint-Amands',
'Rebecq',
'Rijkevorsel',
'Rixensart',
'Rochefort',
'Roeselare',
'Ronse',
'Saint-Ghislain',
'Saint-Gilles',
'Saint-Léger',
'Sambreville',
'Schaerbeek',
'Schilde',
'Schoten',
'Seneffe',
'Seraing',
'Silly',
'Sint-Genesius-Rode',
'Sint-Gillis-Waas',
'Sint-Laureins',
'Sint-Martens-Latem',
'Sint-Niklaas',
'Sint-Pieters-Leeuw',
'Sint-Truiden',
'Sombreffe',
'Somme-Leuze',
'Spa',
'Sprimont',
'Stabroek',
'Steenokkerzeel',
'Stekene',
'Temse',
'Ternat',
'Tessenderlo',
'Tielt',
'Tielt-Winge',
'Tienen',
'Torhout',
'Tournai',
'Trooz',
'Tubize',
'Uccle',
'Verviers',
'Vielsalm',
'Vilvoorde',
'Virton',
'Wanze',
'Waregem',
'Waterloo',
'Watermael-Boitsfort',
'Wavre',
'Wellin',
'Wemmel',
'Wetteren',
'Wevelgem',
'Wezembeek-Oppem',
'Wijnegem',
'Willebroek',
'Wingene',
'Woluwe-Saint-Pierre',
'Woluwe-St.-Lambert',
'Zaventem',
'Zedelgem',
'Zelzate',
'Zemst',
'Zonhoven',
'Zottegem',
'nan',
'Écaussinnes'))
building_condition = st.sidebar.selectbox("**Building condition** :derelict_house_building:",
('Good', 'As new', 'Just renovated', 'To renovate', 'To be done up',
'To restore')),
energy_class = st.sidebar.selectbox("**Energy Class** :bulb:",('A++','A+','A','B','C','D','E','F','G','Not specified', 'C_B')),

surface_of_the_plot  =st.sidebar.number_input('**Total Surface Area**(m2) 	:large_brown_square:',min_value=5,max_value=5000,step=1),
construction_year =st.sidebar.number_input('**Construction year** :calendar:',min_value=1850,max_value=2023,step=1),
bedrooms = st.sidebar.slider('**Number of bedrooms** :sleeping_accommodation:', min_value=0, max_value=8, value=1, step=1)
toilets = st.sidebar.slider('**No. of Toilets** :toilet:',  min_value=1, max_value=8, value=1, step=1)
# furnished =st.sidebar.selectbox("Furnished: 1: yes, 0:No",(1, 0)),
checkbox_value_1 = st.sidebar.checkbox("**Furnished** :couch_and_lamp:")
furnished = 1 if checkbox_value_1 else 0,
# tenement_building =st.sidebar.selectbox("Is the property part of a tenement building? 1: yes, 0: No",(1, 0)),
checkbox_value_2 = st.sidebar.checkbox("**Tenement_building** :derelict_house_building:")
tenement_building = 1 if checkbox_value_2 else 0,
# double_glazing =st.sidebar.selectbox("Double glazing: 1: yes, 0: No",(1, 0)),
checkbox_value = st.sidebar.checkbox("**Double Glazing** :window:")
double_glazing = 1 if checkbox_value else 0,

Avg_price_city = {'Aalst': 439540.54054054053,
 'Aalter': 441300.0,
 'Affligem': 407611.1111111111,
 'Amay': 269500.0,
 'Andenne': 444000.0,
 'Anderlecht': 516333.3333333333,
 'Ans': 249000.0,
 'Antwerpen': 553377.358490566,
 'Anzegem': 434209.5238095238,
 'Arlon': 489680.8510638298,
 'Asse': 548375.0,
 'Assenede': 479000.0,
 'Ath': 497521.73913043475,
 'Aubange': 287357.14285714284,
 'Auderghem': 672416.6666666666,
 'Avelgem': 334666.6666666667,
 'Awans': 169000.0,
 'Aywaille': 268245.8333333333,
 'Bastogne': 352400.0,
 'Beauraing': 435000.0,
 'Berchem-Sainte-Agathe': 359500.0,
 'Bergen': 334166.6666666667,
 'Bertrix': 185966.66666666666,
 'Beveren': 448555.55555555556,
 'Bierbeek': 389666.6666666667,
 'Binche': 285909.0909090909,
 'Blankenberge': 438750.0,
 'Boechout': 682000.0,
 'Bonheiden': 448795.45454545453,
 'Borgloon': 650000.0,
 'Bornem': 372666.6666666667,
 'Bouillon': 515833.3333333333,
 'Boussu': 245300.0,
 "Braine-l'Alleud": 463833.3333333333,
 'Braine-le-Château': 414562.5,
 'Braives': 330882.35294117645,
 'Brasschaat': 896036.8421052631,
 'Bredene': 303288.5,
 'Brugge': 800332.3529411765,
 'Brussel': 354500.0,
 'Brussels': 647000.0,
 'Bruxelles': 802193.2116788321,
 'Buggenhout': 432500.0,
 'Charleroi': 236111.11111111112,
 'Chaudfontaine': 332961.53846153844,
 'Chaumont-Gistoux': 636111.1111111111,
 'Châtelet': 319823.8095238095,
 'Ciney': 236666.66666666666,
 'Court-St.-Étienne': 485000.0,
 'Damme': 482000.0,
 'De Haan': 612285.7142857143,
 'Deerlijk': 239000.0,
 'Deinze': 489818.1818181818,
 'Dendermonde': 588023.8095238095,
 'Dessel': 559000.0,
 'Destelbergen': 694727.2727272727,
 'Diepenbeek': 349000.0,
 'Diksmuide': 336826.0869565217,
 'Dilbeek': 523956.97826086957,
 'Dinant': 393071.4285714286,
 'Dour': 400000.0,
 'Durbuy': 263562.5,
 'Eeklo': 392090.9090909091,
 'Enghien': 495000.0,
 'Esneux': 350000.0,
 'Estaimpuis': 219000.0,
 'Etterbeek': 993250.0,
 'Evere': 546714.2857142857,
 'Evergem': 420500.0,
 'Fleurus': 259364.86486486485,
 'Flémalle': 234777.77777777778,
 'Frameries': 681200.0,
 'Frasnes-lez-Anvaing': 281666.6666666667,
 'Frasnes-lez-Gosselies': 225000.0,
 'Galmaarden': 301500.0,
 'Ganshoren': 504532.6666666667,
 'Gavere': 375000.0,
 'Geel': 355653.3333333333,
 'Gembloux': 362653.76923076925,
 'Genappe': 484226.1904761905,
 'Gent': 478714.0633802817,
 'Geraardsbergen': 462500.0,
 'Gerpinnes': 191666.66666666666,
 'Gooik': 424575.0,
 'Grez-Doiceau': 647294.1176470588,
 'Grimbergen': 544500.0,
 'Haacht': 452866.6666666667,
 'Halle': 486625.0,
 'Ham-sur-Heure-Nalinnes': 380000.0,
 'Hamme': 998000.0,
 'Hannut': 331413.7931034483,
 'Harelbeke': 326277.77777777775,
 'Hasselt': 302780.0,
 'Hechtel-Eksel': 592500.0,
 'Heist-op-den-Berg': 396065.2173913043,
 'Herent': 601441.1764705882,
 'Herentals': 492583.3333333333,
 'Herne': 344500.0,
 'Herstal': 319452.38095238095,
 'Herzele': 159000.0,
 'Hoegaarden': 210000.0,
 'Hoeilaart': 2267500.0,
 'Honnelles': 276458.3333333333,
 'Hotton': 247880.0,
 'Huy': 275276.59574468085,
 'Ieper': 295600.0,
 'Incourt': 367499.5,
 'Ingelmunster': 219000.0,
 'Ixelles': 1258566.0377358492,
 'Izegem': 373272.7272727273,
 'Jabbeke': 471615.3846153846,
 'Jette': 644818.1818181818,
 'Kapelle-op-den-Bos': 519111.1111111111,
 'Keerbergen': 795000.0,
 'Knokke-Heist': 3078772.6515151514,
 'Koekelberg': 494500.0,
 'Koerich': 910000.0,
 'Kortemark': 920000.0,
 'Kortrijk': 374596.77419354836,
 'Kraainem': 1046499.9833333333,
 'La Hulpe': 830384.6153846154,
 'La Louvière': 235589.2857142857,
 'Lasne': 2290833.3333333335,
 'Lebbeke': 370000.0,
 'Lede': 449408.6538461539,
 'Leeuw-Saint-Pierre': 299000.0,
 'Lendelede': 222000.0,
 'Lessines': 441750.0,
 'Leuven': 587814.5,
 'Libin': 272438.46153846156,
 'Libramont-Chevigny': 320976.6666666667,
 'Liedekerke': 285000.0,
 'Lier': 423333.3333333333,
 'Lievegem': 345000.0,
 'Linkebeek': 659062.5,
 'Liège': 353349.6453900709,
 'Lobbes': 199000.0,
 'Lochristi': 6950000.0,
 'Lokeren': 445666.6666666667,
 'Londerzeel': 538545.4545454546,
 'Machelen': 539666.6666666666,
 'Maldegem': 326458.3333333333,
 'Manage': 284083.3333333333,
 'Marche-en-Famenne': 298663.9344262295,
 'Mechelen': 565437.5,
 'Meise': 482945.9459459459,
 'Melle': 695000.0,
 'Merelbeke': 427400.0,
 'Messancy': 299000.0,
 'Middelkerke': 539312.5,
 'Mons': 329750.0,
 'Mont-Saint-Guibert': 448035.71428571426,
 'Morlanwelz': 390000.0,
 'Mouscron': 301200.0,
 'Namur': 415917.01960784313,
 'Nandrin': 285102.0408163265,
 'Neufchâteau': 229500.0,
 'Neupré': 425000.0,
 'Nieuwpoort': 555923.0769230769,
 'Ninove': 498196.9696969697,
 'Nivelles': 438882.35294117645,
 'Oostende': 355131.5789473684,
 'Oosterzele': 503000.0,
 'Oostkamp': 430500.0,
 'Opwijk': 403000.0,
 'Orp-Jauche': 528000.0,
 'Ottignies-Louvain-la-Neuve': 367500.0,
 'Oud-Heverlee': 521200.0,
 'Oudenaarde': 545692.3076923077,
 'Oupeye': 337322.8947368421,
 'Overijse': 559928.5714285715,
 'Paliseul': 388500.0,
 'Pepinster': 241833.33333333334,
 'Pittem': 344754.54545454547,
 'Pont-à-Celles': 247088.7323943662,
 'Poperinge': 293272.7272727273,
 'Profondeville': 355250.0,
 'Putte': 483913.04347826086,
 'Puurs-Sint-Amands': 369125.0,
 'Rebecq': 405000.0,
 'Rijkevorsel': 795000.0,
 'Rixensart': 552536.5853658536,
 'Rochefort': 349000.0,
 'Roeselare': 307333.3333333333,
 'Ronse': 355297.78761061945,
 'Saint-Ghislain': 212395.0,
 'Saint-Gilles': 1436176.4705882352,
 'Saint-Léger': 305444.44444444444,
 'Sambreville': 230230.76923076922,
 'Schaerbeek': 559928.5714285715,
 'Schilde': 1041055.5555555555,
 'Schoten': 469600.0,
 'Seneffe': 485000.0,
 'Seraing': 204300.51020408163,
 'Silly': 210600.0,
 'Sint-Genesius-Rode': 564222.2222222222,
 'Sint-Gillis-Waas': 381375.0,
 'Sint-Laureins': 442500.0,
 'Sint-Martens-Latem': 871748.7857142857,
 'Sint-Niklaas': 482111.1111111111,
 'Sint-Pieters-Leeuw': 537400.0,
 'Sint-Truiden': 421666.6666666667,
 'Sombreffe': 409800.0,
 'Somme-Leuze': 499000.0,
 'Spa': 256100.0,
 'Sprimont': 504714.28571428574,
 'Stabroek': 420000.0,
 'Steenokkerzeel': 552333.3333333334,
 'Stekene': 478055.55555555556,
 'Temse': 959000.0,
 'Ternat': 477090.9090909091,
 'Tessenderlo': 467200.0,
 'Tielt': 257666.66666666666,
 'Tielt-Winge': 369000.0,
 'Tienen': 375552.63157894736,
 'Torhout': 399000.0,
 'Tournai': 305875.0,
 'Trooz': 241120.0,
 'Tubize': 268428.5714285714,
 'Uccle': 1211305.0847457626,
 'Verviers': 433933.3333333333,
 'Vielsalm': 450000.0,
 'Vilvoorde': 612515.2173913043,
 'Virton': 278638.8888888889,
 'Wanze': 356000.0,
 'Waregem': 430213.23529411765,
 'Waterloo': 706303.3707865168,
 'Watermael-Boitsfort': 2326500.0,
 'Wavre': 489402.55102040817,
 'Wellin': 259333.33333333334,
 'Wemmel': 452000.0,
 'Wetteren': 460529.4117647059,
 'Wevelgem': 301833.3333333333,
 'Wezembeek-Oppem': 344000.0,
 'Wijnegem': 1695000.0,
 'Willebroek': 326111.1111111111,
 'Wingene': 388200.0,
 'Woluwe-Saint-Pierre': 752897.7272727273,
 'Woluwe-St.-Lambert': 744570.7070707071,
 'Zaventem': 502666.6666666667,
 'Zedelgem': 479764.70588235295,
 'Zelzate': 414500.0,
 'Zemst': 960000.0,
 'Zonhoven': 377000.0,
 'Zottegem': 367074.0740740741,
 'Écaussinnes': 268000.0}

data = {'city':city,
    'condition': building_condition,
    'energy_class': energy_class,
    'surface_of_the_plot':surface_of_the_plot,
    'const_year': construction_year,
    'bedroom': bedrooms,
    'toilets':toilets,
    'furnished':furnished,
    'tenement_building':tenement_building,
    'double_glazing': double_glazing,
    }
features = pd.DataFrame(data, index=[0])

# Main Panel

# Print specified input parameters
st.header('	:clipboard: Input Summary')
st.dataframe(features)
st.write('---')

# Build Regression Model
url = f"{API_URL}/predict"
params = {
    'bedrooms': bedrooms,
    'building_condition': building_condition,
    'construction_year': construction_year,
    'double_glazing':double_glazing,
    'energy_class':energy_class,
    'furnished':furnished,
    'surface_of_the_plot': surface_of_the_plot,
    'tenement_building': tenement_building,
    'toilets':toilets,
    'city':city
}
response = requests.get(url, params=params).json()

r = response['prediction']

formatted_r = str("{:,.0f}".format(r))

if st.button('Calculate Price'):
    st.header(':moneybag: Predicted Price')
    st.markdown(f"#### The estimated price is  {formatted_r} Euro.")
    avg_price_city = Avg_price_city.get(city)
    formatted_avg = str("{:,.0f}".format(avg_price_city))

    if avg_price_city is not None:
        st.markdown(f"The average price for a property in {city} is {formatted_avg} Euro.")

    else:
        st.write("No data available")
st.write('---')

# # Explaining the model's predictions using SHAP values
# # https://github.com/slundberg/shap
# explainer = shap.TreeExplainer(model)
# shap_values = explainer.shap_values(X)

# st.header('Feature Importance')
# plt.title('Feature importance based on SHAP values')
# shap.summary_plot(shap_values, X)
# st.pyplot(bbox_inches='tight')
# st.write('---')

# plt.title('Feature importance based on SHAP values (Bar)')
# shap.summary_plot(shap_values, X, plot_type="bar")
# st.pyplot(bbox_inches='tight')
