#Autor: MikeSrz
#
#Descripción: Hacer un histograma de la frequencia de las letras que aparecen en un texto.

#Me falta ajustar y aumentar el rango de los replace() y generar un gráfico.

from pprint import pprint

def trim_text(txt):
    return text.lower().replace(",","").replace(".","").replace("\"","").replace("¿","").replace("¡","").replace("?","").replace("!","").replace("“","").replace("”","").replace("á","a").replace("ó","o").replace("é","e").replace("í","i").replace("ú","u").replace("-","").replace("_","").replace("{","").replace("}","").replace("(","").replace(")","").replace("—","").split()

def genchar_frequency(words_list):
    char_frequency = {}
    for word in words_list:
       for i in range (len(word)):
            char_frequency[word[i]] = char_frequency.get(word[i], 0) +1
    return char_frequency

def freq_to_percentage(counters):
    total = sum(counters.values())
    for k, v in counters.items():
         counters[k]= (v/total)*100

text = """"Un cuento no tiene más utilidad que hacernos vivir un momento emocionante. Sin embargo,
aquellos que son realmente buenos, como es el caso de “El Ratón Pérez tiene problemas”, no se
quedan en este propósito. Van mucho más allá, al trabajar por la felicidad.
Un momento emocionante nos hace vibrar y experimentar sensaciones, nos lleva hacia la vivencia de los sueños. Pero no todos los sueños son fabricados con la materia prima del amor.
Esto es sencillo de entender; Me pueden hacer soñar con un reinado, con un bosque encantado
o con un coro de animales de diferentes colores, pero si debajo de la historia no encontramos el
respeto a la naturaleza de cada quien, a sus decisiones, a su forma de hacer y de ser en el mundo…
la emoción será una fuente de engaño, una fábrica de ignorancia.
Chicos y chicas debemos aportar, colaborar, cuidarnos, respetarnos, disfrutarnos, entendernos
en nuestras diferencias en lo que las haya… pero sobre todo… COMPARTIR.
Dar lo mejor y aprender a recibir. Libertad para ser y para elegir. Y para ser libres, hombres y mujeres por igual, debemos disponer de los mismos tiempos. Los mismos tiempos para la obligación y
el descanso.
No tenemos por qué enfocar un trabajo de la misma manera, ni un hombre igual que una mujer,
ni una mujer igual que otra por el hecho de serlo. Eso sí… si tenemos el mismo derecho a la felicidad,
tenemos el mismo derecho al tiempo. Cada quien para lo que decida.
Compartamos, conciliemos, para poder ser libres y felices hombres y mujeres. Gracias Lidia, por
contribuir a hacer una infancia más consciente. Me alegra saber que una maestra como tú, cuenta
cuentos llenos de sensibilidad y de respeto además de ilusión. Qué importante es lo que nos cuentan en el cole. Sigue escribiendo cuentos para el corazón, cuentos para la igualdad. Muchas gracias.
Que todos los cuentos nos enseñen a ser libres y felices en igualdad de condiciones, en igualdad
de tiempos.
María José Aceituno Hinojosa
Concejala de Servicios Sociales e Igualdad.
5
ISABEL PADILLA VÍLCHEZ
Ilustradora.
isa_kalua@hotmail.com
isabelpadillav82@gmail.com
LYDIA PÉREZ HORCAS
Nacida en Baena (Córdoba) en el año
1978. Es diplomada en lengua extranjera: Inglés (1999) y diplomada en educación Infantil
(2004) por la Escuela Universitaria Sagrada Familia de Úbeda (Jaén). Desde que tiene uso
de razón tiene claro que quiere ser maestra,
es una apasionada por la lectura y la escritura.
Con 11 años gana su primer concurso de
poesía, al que se presenta gracias a su profesor de Ciencias Sociales, Don Ricardo Morales.
A los 13 años, influenciada por las novelas de
Corín Tellado que leía su madre, escribe su primera novela corta. En el año 2015 publica “Las
almas de Marina”, con el fin de donar todos
los beneficios de su venta a la asociación baenense de atención temprana “Adibae”.
En 2016 se le concede el segundo premio en
el VI concurso de relato corto por la Fundación
FAMA-COCEMFE de Albacete con el relato
“En el fondo del Mar” y su relato “Anisa la morita” es elegido para ser publicado dentro del
III Certamen de relato corto de los cursos de
verano de la UNED de Alcalá la Real.
Además de dedicarse a la escritura creativa,
colabora desde el 2015 en los periódicos del
grupo JOLY (Diario de Huelva, Europa Sur…),
bajo el título de “Diario de una maestra rural”
con artículos de opinión referentes a educación.
Su trabajo, como maestra en la fundación
SAFA de Alcalá la Real y de Baena, le brinda
la oportunidad de inventar cuentos constantemente. Lydia considera que “los cuentos
tradicionales no reflejan las necesidades de la
sociedad actual y mucho menos apuestan por
la igualdad de género. En la etapa de Infantil, en especial en el último año, la figura del
Ratoncito Pérez cobra un especial interés.” Y
es por sus alumnos, alumnas, su hijo Nacho y
su hija Inés, que decide dar a este rey de los
dientes la oportunidad de modernizarse y verlo
desde una perspectiva más igualitaria, procurando siempre mantener la ilusión.
6
Para todos los ratoncitos y todas las ratoncitas
que desde el anonimato, alimentan la ilusión que
mantiene vivo al Ratoncito Pérez.
Para todos esos dientes extraviados, tragados y
perdidos…
Para Nacho e Inés.
EL RATÓN PÉREZ
TIENE PROBLEMAS
Los niños y las niñas creéis que sabéis toda la historia del Ratoncito Pérez, pero si
de verdad queréis saberlo todo, todo, todo, no os perdáis este cuento.
Antes de empezar, he de enseñaros unas palabras mágicas que tienen un gran
poder. Debéis aprenderlas bien para poder utilizarlas cuando sea necesario, este
conjuro lo repetiréis tres veces, la primera vez con la voz muy bajita, la segunda
un poco más alto y la tercera muy alto, muy alto, muy alto. Estas son las palabras
poderosas ¡hagamos una prueba!:
Si no quieres perder tu diente
Da una palmada y tócate la frente.
Bevi es una niña muy inquieta. Le encanta jugar al fútbol y a los bloques de
construcción. El año pasado ganó el concurso de apilar bloques, consiguió
amontonar doce, uno encima de otro. A Paquito, su mejor amigo, le costaba
mucho entender cómo Bevi había podido ganar. Para él era imposible que una
niña pudiera ganar a ese juego.
9
10
“-Las niñas juegan a las muñecas Bevi—decía Paquito a su amiga cada vez que
ésta intentaba algo diferente”.
Pero a ella no le importaba lo que dijera Paquito, no le gustaba jugar con
muñecas, ni a la cocinita, a ella le apasionaba todo lo que se desmontaba.
Bevi y Paquito se conocieron en la escuela de fútbol, ella era la única niña,
conectaron desde el principio, aunque a Paquito le costaba aceptar que Bevi
pudiera correr y chutar con la misma fuerza y resistencia que él. No había un solo
día que después de los entrenamientos, cuando el monitor ordenaba recoger el
material, Paquito no acudiera a ayudar a Bevi:
“-Bevi, déjame que te ayude, los niños tenemos más fuerza que las niñas”.
Un día Bevi se sentía muy triste, se le había caído su tercer diente mientras jugaba
a los relevos y le fue imposible encontrarlo. Rastrillaron aquella pista de arena con
las manos, pero nada, aquel dientecito se confundía con los granos y el polvo del
suelo. Bevi se puso a llorar.
“-¿Qué voy a hacer sin mi diente Paquito?, el Ratón Pérez no me traerá
su moneda”.
” -No te preocupes Bevi, buscaremos una solución —dijo Paquito
a modo de palmadita en la espalda a la vez que pensaba en
una solución para su amiga— ¡Ya lo tengo! escríbele una carta al
Ratoncito Pérez, Bevi, explícale lo que ha pasado y para compensarlo
le ofreces un trocito de queso, seguro que lo entiende. Mi primo
Tonino se tragó un diente, le dejó una nota al Ratón y al día siguiente
tenía su moneda”.
11
Bevi aceptó aquella idea y quedaron por la tarde en su casa
para escribir la importantísima nota:
 Querido Ratón Pérez:
Esta mañana mientras jugaba a los relevos en la pista
del colegio ocurrió un desastre desastroso, se me cayó
un dientecito y no pude encontrarlo. Estoy muy triste
porque sin diente no me dejarás una moneda. ¿Tú
podrás encontrarlo?. Al final voy a creer a mi amigo
Paquito cada vez que me dice que las niñas tienen que
jugar a otras cosas. Por favor, encuentra mi dientecito,
te dejo un trocito de tarta de queso que ha hecho mi
papá. Muchas gracias, Bevi.
Cuando terminaron de escribirla, se dirigieron al
dormitorio de Bevi para colocarla debajo de la almohada,
pero… ¿quién podía imaginar lo que ocurriría justo cuando
levantaron la almohada?
“-¡Ahhhhh! —gritaron.”
El dormitorio se puso oscuro, la tarde se volvió
escalofriante… Paquito apretó la mano de Bevi,
empezó a respirar raro y notó como su piel se llenó
de bultitos, esos bultitos que salen cuando estas que
te mueres de miedo, ¡Tenía la piel de gallina!.
 “-¿Qué está pasando Bevi? —preguntó el niño
asustado.”
12
“-No sé Paquito… esto es… esto es… ¡Alucinante!.”
Bajo la almohada de Bevi no había NADA, había un
inmenso agujero gris desde el que se veía a una ratita
que los invitaba a entrar:
“-¡Venga! No tengo tiempo, el Ratoncito Pérez tiene
serios problemas, ya os explicaré por el camino —les
gritó la ratita.”
Bevi no se lo pensó y tiró de Paquito para saltar
al interior de aquel agujero. Era un agujero poco
profundo, como si atravesaran una puerta, que les
llevaba a un mundo mágico.
La ratita se presentó: “Soy Lucy Pérez, una de las hijas
del Ratón Pérez y necesito vuestra ayuda para salvar a
mi padre, a cambio yo os ayudaré a encontrar el diente
perdido”.
“-¿Tú? —preguntó Paquito—Tú no eres el
Ratón Pérez, eres una ratita, él es más veloz
que tú.”
“-¿Acaso me has visto correr a mí?
¿No crees que las chicas somos igual de
capaces que los chicos?.”
Paquito puso una de sus caras raras, él
cree que hay cosas solo para las chicas
y otras sólo para los chicos, pero no se
atrevió a contestar.
13
“-Como todas las personas saben, el Ratón Pérez es mágico y puede vivir toda la
vida, pero necesita la ILUSIÓN de niños y niñas para vivir, mientras haya ilusión, hay
vida para el Ratón Pérez. El problema, es que hay un duende malvado llamado
Tridente, que hace que se pierdan los dientecitos de niños y niñas, así el Ratón Pérez
no puede visitarlos y dejan de tener ilusión, dejan de creer y entonces, el Ratón
Pérez, se va debilitando- les contó Lucy-.”
“-Mientras mi padre se recupera yo me encargaré de recoger los dientes, pero
necesito curarlo cuanto antes.”
Bevi le contó a Lucy que ella había perdido su dientecito sin querer, que estaba
corriendo y cuando se dio cuenta el diente ya no estaba en su boca, le fue imposible
encontrarlo. Entonces Lucy les contó que los dientes no se pierden, que el duende
Tridente aprovecha el descuido de niños y niñas para llevárselos.
Bevi y Paquito decidieron ayudar a Lucy, así que ésta tocó un botón de su
chaqueta, era un botón mágico, y los hizo diminutos.
¡Estaban en el patio del colegio! ¡Tenían que encontrar el diente de Bevi antes de
que llegara la noche y se lo llevara Tridente!
Necesitaban ese diente como fuera, la ilusión tan grande que Bevi tenía sanaría
al Ratón Pérez.
Los tres empezaron a andar sobre aquellos granitos de tierra, que para ellos
ahora eran enormes, y muy cuidadosamente empezaron a explorar el patio del
colegio que parecía un patio de gigantes. Mientras, Lucy se encargaría de hacer
el trabajo de su padre. Aquel botón mágico de la chaqueta no sólo tenía el poder
de hacer las cosas grandes o pequeñas también avisaba a Lucy donde tenía que
ir a recoger los dientecitos.
14
Bevi recordó que estando en la raya de salida aún tenía el diente, recordaba
jugar con la lengua a balancearlo hacia adelante y hacia atrás mientras Miguelito
daba la señal para empezar a correr… si cuando llegó a la meta ya no lo tenía…,
sólo tendrían que revisar el trayecto de en medio. Así que empezaron a mirar granito
por granito, barrieron el terreno con los pies, tocaron todo lo que les parecía dudoso,
hasta que Paquito se sintió cansado y se sentó a descansar sobre una piedra plana
muy cómoda para poder recostarse. El diente no aparecía por ningún lado.
¡De pronto Bevi levantó a Paquito de su descansadero! y le gritó muy, muy, fuerte:
“-¡Paquito bájate de mi diente!.” Efectivamente aquella piedra era el diente de
Bevi, el diente perdido, el diente de la ilusión que tanto necesitaba el Ratón Pérez.
Cargaron el diente entre los dos y Paquito se dio cuenta, que ambos llevaban el
dienten por igual y que sin Bevi él no podría haberlo llevado solo, eran un equipo.
Lucy estaba esperando en el punto donde les dejó. De repente sintieron que sus
pies estaban duros como piedras. ¿Qué estaba pasando? Entonces escucharon
una risa fuerte, malvada, era… ¡Tridente!, el duende roba dientes. ¡No podían mover
los pies!.
Tridente le quitó el diente a Bevi, ¡con el trabajo que les había costado encontrarlo!
“-¡Noooooo!—gritaron Paquito y Bevi—¡Devuélvenos el diente!”.
Entonces Lucy tuvo una idea, hizo un conjuro mágico y tocó el botón de su
chaqueta,
“-¡Venga vamos! ¡Decid el conjuro que ya sabemos!”:
Si no quieres perder tu diente
Da una palmada y tócate la frente.
15
16
En ese instante, volvieron a sentir sus pies y Tridente comenzó a desaparecer.
Lucy cogió el diente y lo metió en una bolsita mágica y se dirigieron al palacio del
Ratón Pérez.
 Cuando llegaron al palacio del Ratón Perez, se quedaron boquiabiertos, era un
palacio precioso, reluciente, hecho de… ¿Sabéis de qué? ¿Os imagináis de qué
estaba hecho ese palacio? Pues no, no estaba hecho
de dientes sino de… ¡QUESO! El Ratón Pérez no se come
el queso que le ponen niños y niñas, sino que se lo lleva
para construir su castillo, porque su familia crece y crece.
Antes de llegar al dormitorio del Ratón Pérez, Lucy
llevó a Paquito y Bevi a visitar la zona de reciclaje y
almacenaje de dientes; allí ratoncitas y ratoncitos
trabajaban sin descanso, un grupo limpiaba y sacaba
brillo a los dientes, otro los seleccionaba: los incisivos
centrales por aquí, los incisivos laterales por allá, incisivos
de arriba, incisivos de abajo…. Bevi estaba alucinada,
aquello de apilar dientes, se parecía mucho a su juego
de construcción, Paquito por su parte, veía como la
tarea de limpiar los dientes no era sólo de las ratoncitas,
sino que había de ambos sexos en todas las secciones.
Incluso se atrevió a probar, Meticuloso un ratoncito de
la sección de abrillantado, le ofreció a Paquito uno de
los paños y frotando, frotando, aquel diente amarillento
empezó a brillar tanto que Paquito podía ver su cara
reflejada en él.
17
“-¡Ohhhhh! —exclamó el niño maravillado”.
Lucy sacó de su bolsa mágica los miles de dientes que había recogido por todo
el mundo y que pertenecían a niños y niñas que aún tenían ilusión, otros dientes se
quedaron perdidos, los que Tridente se había llevado. Había niños y niñas que no
ponían su diente bajo la almohada, que ya no creían y los dejaban tirados por ahí.
Esos dientes quitaban fuerza al Ratón Pérez y no ayudaban a conservar su magia.
Una vez realizada la descarga de los dientes, partieron hacia la habitación del
enfermo ratón y al llegar a su cama, el Ratón Pérez llamó a Bevi y a Paquito por su
nombre.
“-¡Por fin estáis aquí! —suspiró el fatigado ratón, no olvidéis que el Ratón Pérez es
un ratón mágico que conoce el nombre de todos los niños y niñas, bueno, el de
todos y todas no, sólo el nombre de quien lo llama”.
 Lucy, se apresuró a sacar de su bolsa el único diente que no había dejado en la
fábrica, el diente que salvaría a su padre, el dientecito perdido de Bevi. El Ratón Pérez
cogió el diente y con sus manos lo apretó contra su pecho. El dientecito empezó a
emitir una especie de destellos azulados que atravesaban las manos de aquel
ratoncito centenario, hasta convertirse en una bola de luz que iluminaba toda
la habitación. Aquel diente se fue deshaciendo y adentrando en el pecho del
Ratón Pérez hasta llegar directo a su corazón, allí donde se impulsa la vida, allí
donde reside la ilusión, porque la ilusión es lo que mantiene vivo.
El Ratón, empezó a recobrar movimiento, sus ojos se abrieron muy grandes,
estiró tanto los brazos que parecía que le iban a llegar al techo, se puso sus gafas,
de queso, y le dio un fuerte abrazo a Lucy: “Gracias hija, me has demostrado
ser una sustituta de honor, has recogido los dientes de la noche anterior y has
encontrado el de Bevi, sin ti me habría apagado. En recompensa por tu labor,
18
19
20
a partir de ahora recogeremos juntos todos los dientes que nos
ofrezcan con ilusión, colmillos, premolares y molares.” El Ratón
Pérez tocó el botón mágico de la chaqueta e hizo aparecer
otra nueva. Padre e hija tendrían su chaqueta, compartirían
el poder, entre los dos sería más fácil encontrar los dientes
perdidos antes que Tridente. Porque cuando se hacen las
cosas en equipo, los resultados son mejores. No importa
si son niños o niñas, lo importante es lo que cada cual
puede aportar, porque aprendemos de todas y de todos.
Paquito se quedó pensativo, se dio cuenta que el
Ratón Pérez tenía razón, se acordó de lo bien que se
lo había pasado abrillantando dientes, de que los dos
habían cargado el diente, de lo valiente que había
sido Bevi, de lo buena que era Bevi en el fútbol y con
las construcciones, y de lo mucho que a él le llamaba
la atención la cocinita de su hermana Lola… en cuanto
llegue a casa le pediré a Lola que me la preste, o mejor
dicho, le pediré que juguemos los dos juntos seguro que así
es mucho más divertido —planeó Paquito.
Bueno, la misión había terminado, habían encontrado el
diente antes de la noche, y podían regresar a casa. Pero Bevi
quiso hacer antes una pregunta:
“-Señor Pérez, he visto que su castillo es de queso, ¿para qué
quiere entonces los dientes?
21
22
23
“- Pues os voy a contar la verdad- dijo el Ratón Pérez-. Vais a conocerla en
primicia, Resulta que cuando un niño o niña te regala su diente al ponerlo debajo
de la almohada, sin saberlo está ayudando a otros niños y niñas. Con esos dientes
que nos llegan se fabrican otros nuevos para niños y niñas que no tienen una buena
alimentación y que por ese motivo no les saldrían los dientes. Yo, agradecido por el
regalo, dejo una recompensa.”
“-¡Vaya! —exclamó Bevi—. Pues a partir de ahora cuidaremos nuestros dientes,
los lavaremos más a menudo y comeremos menos chuches, para que tener unos
dientes mucho más fuertes. “
Bevi y Paquito se despidieron del Ratón Pérez y Lucy les acompañó al lugar en el
que se abrió el agujero gris que los trajo al mundo de Pérez, se tomaron de la mano
y se adentraron en él.
“¡Adiós Lucy ! —se despidieron Paquito y Bevi.”
“¡Adiós y recordad lo importante que es mantener la ilusión! —se despidió Lucy.”
Bevi y Paquito estaban de nuevo en el cuarto de Bevi, un cuarto que ya no
estaba oscuro, el agujero gris de debajo de la almohada se había cerrado y Bevi
tenía la satisfacción de haber encontrado su diente. A partir de ahora sería más
cuidosa y jamás olvidaría aquellas palabras mágicas, por si acaso.
Fue entonces cuando Paquito pidió perdón a Bevi por las veces que le había
dicho que las niñas juegan a otras cosas y que tienen menos fuerza que los niños.
“Gracias Paquito- dijo Bevi-. No me sentía bien cuando me decías esas cosas, ya
no nos volverá a pasar.” Se dieron un fuerte abrazo y rieron felices por la aventura
que acababan de vivir.
Cada persona tiene que jugar a lo que le guste, realizar las tareas de casa
también puede ser divertido. Las diferencias entre niños y niñas no son de verdad,
24
25
26
son inventadas, así que podemos cambiarlas cuando
queramos.
A la mañana siguiente, Bevi se despertó ansiosa,
miró debajo de su almohada y allí estaba su moneda.
Con los ojos aún pegados por el sueño se levantó
rápidamente para mirar en la banqueta que había
a los pies de su cama. Se sintió más feliz que nunca
al ver que el Ratoncito o la Ratoncita Pérez se habían
llevado, que no comido, un buen trozo de la tarta de
queso que había hecho el papá de Bevi.
Y colorín colorado este cuento se ha acabado y
cada vez que se te caiga un diente di las palabras
mágicas para que no se lo lleve Tridente.
27

Agradecimientos
A las personas que han formado parte del jurado, por su colaboración desinteresada y su sensibilidad
artística y en pos de la igualdad.
Mª Paz Lorenzo Álvarez. Representante de la comunidad educativa de Alcalá la Real.
Javier López Baeza. Ganador del VII Certamen de “Cuentos por la Igualdad” 2016.
Manuela Hidalgo López. Representante del movimiento asociativo de mujeres de Alcalá la Real.
Cristina Vera Peinado. Representante de los medios de comunicación.
María Serrano Canovaca. Representante del mundo cultural de Alcalá la Real.
A todas las personas que han participado con sus obras en el octavo Certamen de Cuentos por la Igualdad que ha organizado éste Ayuntamiento, vinculado al proyecto “Alcalá, Tiempos de Conciliación”."""

words_list = trim_text(text)
char_frequency = genchar_frequency(words_list)
freq_to_percentage(char_frequency)
pprint(char_frequency)


