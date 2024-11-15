import streamlit as st
import requests
 # Change this URL to the one of your API
API_URL = " https://my-api-app-ltqnoxdklq-ew.a.run.app/"

st.title("Belgian Real Estate Price Predictor")
st.write("You can estimate the price of a property in Belgium by entering the info below: ")

bedrooms = st.slider('How many bedrooms?', min_value=0, max_value=8, value=1, step=1)

building_condition = st.selectbox("Building condition: Please choose one of the following conditions?",
    ('Good', 'As new', 'Just renovated', 'To renovate', 'To be done up',
       'To restore'))
construction_year =st.number_input('Construction year: Please input construction year?',min_value=1850,max_value=2023,step=1)
#double_glazing =st.number_input("Double glazing: Please input one of the following conditions? 1: yes, 0:No",format="%0f"),

double_glazing =st.selectbox("Double glazing: Please input one of the following conditions? 1: yes, 0:No",(1, 0)),


energy_class = st.selectbox("Energy Class: Please choose one of the following conditions?",('A++','A+','A','B',
                                                                              'C','D','E','F','G','Not specified', 'C_B')),

furnished =st.selectbox("Furnished: Please enter your response? 1: yes, 0:No",(1, 0)),


surface_of_the_plot  =st.number_input('Total surface of plot: Please input Surface area of the plot in m2?',min_value=5,max_value=5000,step=1)

tenement_building =st.selectbox("Is the property part of a tenement building? Please choose one? 1: yes, 0:No",(1, 0)),

toilets = st.slider('Toilets: How many Toilets?',  min_value=0, max_value=8, value=1, step=1)

city = st.selectbox("City: Please choose city of your choice from the following?",('Ronse', 'Wingene', 'Antwerpen', 'Brugge', 'Wavre', 'Braives',
       'Hotton', 'Oosterzele', 'Marche-en-Famenne', 'nan', 'Oupeye',
       'Waterloo', 'Tienen', 'Kraainem', 'Brussel', 'Gent', 'Lede', 'Huy',
       'Woluwe-St.-Lambert', 'Seraing', 'Jabbeke', 'Dilbeek', 'Waregem',
       'Rixensart', 'Uccle', 'Ganshoren', 'Kapelle-op-den-Bos',
       'Neufchâteau', 'Aalst', 'Gembloux', 'Libin', 'Woluwe-Saint-Pierre',
       'Puurs-Sint-Amands', 'Liège', 'Knokke-Heist', 'Bierbeek',
       'Hoeilaart', 'Harelbeke', 'Arlon', 'Libramont-Chevigny',
       'Profondeville', 'Trooz', 'Pont-à-Celles', 'Schaerbeek',
       'Nivelles', 'Leuven', 'Mechelen', 'Halle', 'Chaumont-Gistoux',
       'Braine-le-Château', 'Herent', 'Tournai', 'Bertrix', 'Genappe',
       'Wetteren', 'Dendermonde', 'Ninove', 'Bruxelles', 'Zaventem',
       'Geraardsbergen', 'Beveren', 'Saint-Gilles', 'Auderghem',
       'Vilvoorde', 'Beauraing', 'Oud-Heverlee', 'Sint-Genesius-Rode',
       'Schilde', 'Londerzeel', 'Ixelles', 'La Louvière', 'Anderlecht',
       'Brasschaat', 'Stekene', 'Bonheiden', 'Namur', 'Virton', 'Eeklo',
       'Aalter', 'Durbuy', 'Kortrijk', 'Nandrin', 'Linkebeek',
       'Frasnes-lez-Gosselies', 'Andenne', 'Herstal', 'Oudenaarde',
       'Willebroek', 'Lessines', 'Mont-Saint-Guibert', 'Jette',
       'Berchem-Sainte-Agathe', 'Etterbeek', 'Oostende', 'Haacht',
       'Zottegem', 'Aubange', 'Sint-Pieters-Leeuw', 'Herentals', 'Putte',
       'Tubize', 'Gooik', 'Watermael-Boitsfort', 'Avelgem', 'Ieper',
       'Machelen', 'Deinze', 'Poperinge', 'Aywaille', 'Grimbergen',
       'Wezembeek-Oppem', 'Sombreffe', 'Meise', 'Spa', 'Zedelgem',
       'Sambreville', 'Écaussinnes', 'Lochristi', 'Chaudfontaine',
       'Grez-Doiceau', 'Roeselare', 'Evergem', 'Sint-Gillis-Waas',
       'Saint-Léger', 'Schoten', 'Diepenbeek', 'Ternat', 'Silly',
       'Steenokkerzeel', 'Ham-sur-Heure-Nalinnes', 'Orp-Jauche',
       'Frameries', 'Sint-Martens-Latem', 'Sint-Niklaas', 'Incourt',
       'Blankenberge', 'Heist-op-den-Berg', 'Saint-Ghislain', 'Fleurus',
       'Ans', "Braine-l'Alleud", 'Merelbeke', 'Bastogne', 'De Haan',
       'Hechtel-Eksel', 'Charleroi', 'Hasselt', 'Bouillon', 'Rochefort',
       'Manage', 'Destelbergen', 'Borgloon', 'Izegem', 'Middelkerke',
       'Overijse', 'Maldegem', 'Châtelet', 'Diksmuide', 'Lasne', 'Amay',
       'Wevelgem', 'Nieuwpoort', 'Hamme', 'Oostkamp', 'Anzegem',
       'Frasnes-lez-Anvaing', 'Estaimpuis', 'Assenede', 'Wellin', 'Awans',
       'Wanze', 'Opwijk', 'Tielt', 'Affligem', 'Brussels', 'Temse', 'Ath',
       'Hannut', 'Lendelede', 'Binche', 'Rebecq', 'Rijkevorsel',
       'La Hulpe', 'Mouscron', 'Hoegaarden', 'Koekelberg', 'Pittem',
       'Geel', 'Stabroek', 'Honnelles', 'Evere', 'Flémalle', 'Dinant',
       'Deerlijk', 'Sprimont', 'Zonhoven', 'Sint-Truiden',
       'Ottignies-Louvain-la-Neuve', 'Morlanwelz', 'Verviers', 'Herne',
       'Asse', 'Boechout', 'Tessenderlo', 'Keerbergen', 'Paliseul',
       'Wijnegem', 'Bornem', 'Mons', 'Boussu', 'Bredene', 'Pepinster',
       'Seneffe', 'Lokeren', 'Kortemark', 'Sint-Laureins', 'Herzele',
       'Liedekerke', 'Leeuw-Saint-Pierre', 'Messancy',
       'Court-St.-Étienne', 'Bergen', 'Lebbeke', 'Gavere', 'Wemmel',
       'Ciney', 'Dour', 'Lievegem', 'Gerpinnes', 'Lier', 'Torhout',
       'Buggenhout', 'Melle', 'Damme', 'Galmaarden', 'Zelzate', 'Neupré',
       'Dessel', 'Somme-Leuze', 'Esneux', 'Tielt-Winge', 'Lobbes',
       'Ingelmunster', 'Vielsalm', 'Enghien', 'Koerich', 'Zemst'))

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

st.markdown(f"### The estimated price is  {formatted_r} Euro.")
