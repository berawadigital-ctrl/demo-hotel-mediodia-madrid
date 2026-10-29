# Contenido de la demo Hotel Mediodía (Madrid) (es/ca/en/fr). Hechos de mediodiahotel.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Estándar cama matrimonio','Doble Superior','Estándar 2 camas + 2 camas extra'],'ca':['Estàndard llit de matrimoni','Doble Superior','Estàndard 2 llits + 2 llits extra'],'en':['Standard double bed','Superior Double','Standard 2 beds + 2 extra beds'],'fr':['Standard lit double','Double supérieure','Standard 2 lits + 2 lits supplémentaires']}
RD={
'es':['De 12 a 14 metros cuadrados, interior a patio de luces o exterior con balcón.','Habitaciones de 19 metros cuadrados, exteriores con vistas y balcón.','Hasta 4 personas, con balcón o ventanas al exterior; ideal para familias.'],
'ca':['De 12 a 14 metres quadrats, interior a pati de llums o exterior amb balcó.','Habitacions de 19 metres quadrats, exteriors amb vistes i balcó.','Fins a 4 persones, amb balcó o finestres a l\'exterior; ideal per a famílies.'],
'en':['12 to 14 square metres, facing the light well or exterior with a balcony.','Rooms of 19 square metres, exterior with views and a balcony.','Up to 4 guests, with a balcony or exterior windows; ideal for families.'],
'fr':['De 12 à 14 mètres carrés, sur cour de lumière ou côté rue avec balcon.','Chambres de 19 mètres carrés, côté rue avec vue et balcon.','Jusqu\'à 4 personnes, avec balcon ou fenêtres sur rue ; idéale pour les familles.']}
ART={
'hero':('columns',2961,['#efe6d6','#f6efe2','#b8893e','#2f5d50','#1a3a31']),
'intro':('arches',2962,['#efe6d6','#d9b98a','#a8743c','#2f5d50','#1a3a31']),
'r1':('columns',2971,['#eee5d4','#f5eee0','#bb8c42','#35665a','#1c3f35']),
'r2':('skyline',2972,['#2c4a44','#e48a5f','#f9d19b','#2b4842','#203631','#152522']),
'r3':('arches',2973,['#eee4d3','#d6b483','#a6703a','#2f5d50','#1a3a31']),
'g1':('columns',2981,['#efe6d5','#f6efe1','#c08c40','#2f5d50','#1a3a31']),
'g2':('skyline',2982,['#3d3a52','#e8935f','#fbd9a0','#3c3950','#2c2a3c','#1d1c28']),
'g3':('arches',2983,['#efe5d4','#d8b787','#a9733d','#336155','#1b3c33']),
'g4':('hills',2984,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g5':('columns',2985,['#ede4d3','#f4ede0','#bd8a3f','#2f5d50','#1a3a31']),
'g6':('skyline',2986,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Mediodía · Hotel histórico frente a la estación de Atocha, Madrid',see_rooms='Ver habitaciones',hero_k='Madrid · Atocha',hero_t='Donde empieza el viaje',hero_s='Un hotel levantado en 1914 frente a la estación de Atocha, junto al Museo Reina Sofía.',
 intro_t='Un hotel con historia en pleno centro',intro_p1='El Hotel Mediodía fue levantado en 1914 bajo la influencia del neoclasicismo francés, con vidrieras originales de la Casa Maumejean.',
 intro_p2='Su nombre rinde homenaje a la antigua Estación del Mediodía, hoy Atocha. Tiene 167 habitaciones de 7 tipos; algunas con vistas al Museo Reina Sofía o a la Plaza del Emperador Carlos V.',
 stats=['Desde 1914','167 habitaciones','Recepción 24h','Frente a Atocha'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de los siete tipos de habitación del hotel.',
 svcs=['Recepción 24h','Wifi gratis','Cafetería (7-11h)','Desayuno continental','Salón social','Lavandería y planchado (de pago)','Ascensores','Acceso para movilidad reducida'],
 loc_p='Plaza del Emperador Carlos V, 8 · 28012 Madrid. Metro Estación del Arte a 75 m y estación de Madrid Atocha (Renfe) a 215 m.',
 chips=['¿Qué habitaciones tiene?','¿Hay parking?','¿Dónde está?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Mediodía · Hotel històric davant de l\'estació d\'Atocha, Madrid',see_rooms='Veure habitacions',hero_k='Madrid · Atocha',hero_t='On comença el viatge',hero_s='Un hotel aixecat el 1914 davant de l\'estació d\'Atocha, al costat del Museu Reina Sofía.',
 intro_t='Un hotel amb història en ple centre',intro_p1='L\'Hotel Mediodía es va aixecar el 1914 sota la influència del neoclassicisme francès, amb vitralls originals de la Casa Maumejean.',
 intro_p2='El seu nom ret homenatge a l\'antiga Estación del Mediodía, avui Atocha. Té 167 habitacions de 7 tipus; algunes amb vistes al Museu Reina Sofía o a la plaça de l\'Emperador Carles V.',
 stats=['Des de 1914','167 habitacions','Recepció 24h','Davant d\'Atocha'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres dels set tipus d\'habitació de l\'hotel.',
 svcs=['Recepció 24h','Wifi gratuïta','Cafeteria (7-11h)','Esmorzar continental','Saló social','Bugaderia i planxa (de pagament)','Ascensors','Accés per a mobilitat reduïda'],
 loc_p='Plaza del Emperador Carlos V, 8 · 28012 Madrid. Metro Estación del Arte a 75 m i estació de Madrid Atocha (Renfe) a 215 m.',
 chips=['Quines habitacions té?','Hi ha pàrquing?','On és?','Com es reserva?']),
'en':dict(title='Hotel Mediodía · Historic hotel opposite Atocha station, Madrid',see_rooms='See the rooms',hero_k='Madrid · Atocha',hero_t='Where the journey begins',hero_s='A hotel built in 1914 opposite Atocha station, next to the Reina Sofía Museum.',
 intro_t='A historic hotel in the city centre',intro_p1='Hotel Mediodía was built in 1914 under the influence of French neoclassicism, with original stained glass by Casa Maumejean.',
 intro_p2='Its name pays tribute to the former Estación del Mediodía, today Atocha. It has 167 rooms of 7 types; some overlook the Reina Sofía Museum or Plaza del Emperador Carlos V.',
 stats=['Since 1914','167 rooms','24h reception','Opposite Atocha'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the hotel\'s seven room types.',
 svcs=['24h reception','Free wifi','Café (7-11h)','Continental breakfast','Lounge','Laundry and ironing (paid)','Lifts','Access for reduced mobility'],
 loc_p='Plaza del Emperador Carlos V, 8 · 28012 Madrid. Estación del Arte metro 75 m away and Madrid Atocha (Renfe) station 215 m away.',
 chips=['What rooms does it have?','Is there parking?','Where is it?','How do I book?']),
'fr':dict(title='Hotel Mediodía · Hôtel historique face à la gare d\'Atocha, Madrid',see_rooms='Voir les chambres',hero_k='Madrid · Atocha',hero_t='Là où commence le voyage',hero_s='Un hôtel construit en 1914 face à la gare d\'Atocha, à côté du musée Reina Sofía.',
 intro_t='Un hôtel historique en plein centre',intro_p1='L\'Hotel Mediodía a été construit en 1914 sous l\'influence du néoclassicisme français, avec des vitraux originaux de la Casa Maumejean.',
 intro_p2='Son nom rend hommage à l\'ancienne Estación del Mediodía, aujourd\'hui Atocha. Il compte 167 chambres de 7 types ; certaines donnent sur le musée Reina Sofía ou la place de l\'Empereur Charles Quint.',
 stats=['Depuis 1914','167 chambres','Réception 24h','Face à Atocha'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des sept types de chambre de l\'hôtel.',
 svcs=['Réception 24h','Wifi gratuit','Cafétéria (7-11h)','Petit-déjeuner continental','Salon','Blanchisserie et repassage (payant)','Ascenseurs','Accès pour personnes à mobilité réduite'],
 loc_p='Plaza del Emperador Carlos V, 8 · 28012 Madrid. Métro Estación del Arte à 75 m et gare de Madrid Atocha (Renfe) à 215 m.',
 chips=['Quelles chambres a-t-il ?','Y a-t-il un parking ?','Où est-il ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='recepcion@mediodiahotel.com')
D=dict(name='Hotel Mediodía',ac='#2f5d50',ac2='#b8893e',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='Plaza del Emperador Carlos V, 8 · 28012 Madrid',phones=['915 273 060'],emails=['recepcion@mediodiahotel.com'],maps='Hotel Mediodía, Plaza del Emperador Carlos V 8, Madrid',t=T)
META=dict(repo='demo-hotel-mediodia-madrid',name='Hotel Mediodía',legal_name='INMOBILIARIA MEDIODIA S.A.',registry_ids=['NIF A28013829'],
 url='https://www.mediodiahotel.com/',domain='mediodiahotel.com',municipality='Madrid',province='Madrid',sector='hotel histórico frente a la estación de Atocha',
 read_at='2026-10-29T08:00:00+01:00',created_at='2026-10-29T08:25:00+01:00',built_at='2026-10-29T08:25:00+01:00',audit_date='2026-10-29T07:41:00+01:00',
 rating=dict(value=4.2,coincide=['telefono','web'],date='2026-10-29T06:50:23+01:00',url='https://www.google.com/maps/place/Hotel+Mediod%C3%ADa/@40.4084225,-3.6930039,17z/data=!4m9!3m8!1s0xd4226260494268d:0x25a7477d01c1dc75!5m2!4m1!1i2!8m2!3d40.4084225!4d-3.6930039!16s%2Fg%2F1tg9t_6z'),
 book=dict(mode='mail',email='recepcion@mediodiahotel.com',note='La web del negocio reserva con un buscador de Mirai cargado por JavaScript sin URL publica estable; la demo usa el correo de informacion y reservas publicado y el telefono.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Qué equipamiento tienen las habitaciones?','K02'),('¿Hay desayuno?','K03'),('¿Hay parking?','K04'),('¿A qué hora es el check-in?','K05'),('¿Admiten mascotas?','K06'),('¿Dónde está el hotel?','K07'),('¿Cómo llego desde el aeropuerto?','K08'),('¿Qué historia tiene el edificio?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el teléfono?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Tienen gimnasio?',None),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Quin equipament tenen les habitacions?','K02'),('Hi ha esmorzar?','K03'),('Hi ha pàrquing?','K04'),('A quina hora és el check-in?','K05'),('Admeteu mascotes?','K06'),('On és l\'hotel?','K07'),('Com hi arribo des de l\'aeroport?','K08'),('Quina història té l\'edifici?','K09'),('Com reservo?','K10'),('Quin és el telèfon?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Teniu gimnàs?',None),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('What equipment do the rooms have?','K02'),('Is there breakfast?','K03'),('Is there parking?','K04'),('What time is check-in?','K05'),('Are pets allowed?','K06'),('Where is the hotel?','K07'),('How do I get there from the airport?','K08'),('What history does the building have?','K09'),('How do I book?','K10'),('What is the phone number?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Do you have a gym?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Quel équipement ont les chambres ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('Y a-t-il un parking ?','K04'),('À quelle heure est le check-in ?','K05'),('Les animaux sont-ils admis ?','K06'),('Où est l\'hôtel ?','K07'),('Comment venir depuis l\'aéroport ?','K08'),('Quelle histoire a le bâtiment ?','K09'),('Comment réserver ?','K10'),('Quel est le téléphone ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Avez-vous une salle de sport ?',None),('Y a-t-il une piscine ?',None)]}
