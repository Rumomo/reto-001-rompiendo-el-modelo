# RETO \#001 \- Rompiendo el modelo

No hay mejor forma de celebrar el lanzamiento del Laboratorio que lanzando el un reto para toda la comunidad, así que aquí os traigo el primero de los que, espero, sean muchos.&nbsp;

&nbsp;

Eso sí, ¡no penséis que porque es el primero va a ser sencillo\! Pretendo exprimir vuestros cerebros todo lo que pueda.

&nbsp;

Entonces, ¿cuál es la premisa de este reto? Pues \*\*demostrar que eres capaz de hacer que un modelo de inteligencia artificial sea capaz de fallar sistemáticamente al resolver un problema, y demostrarlo con datos\*\*.

&nbsp;

Cuando hablamos de LLMs, agentes y arneses, solemos evaluar sus capacidades a través de aquello que son capaces de hacer, pero estudiar las condiciones en las que falla también ofrece información muy valiosa. Para encontrar sus limitaciones, muchas veces ni siquiera necesitamos plantear demasiado complejos, sino que experimentos simples nos pueden dar pistas de cuáles son sus puntos de fallo.

&nbsp;

En este reto, tu objetivo será diseñar un experimento, maximizar la tasa de error de un modelo de lenguaje y defender tus resultados con evidencias verificables.&nbsp;

&nbsp;

Tranqui, ahora te doy detalles más concretos, pero antes de nada \*\*qué puedes ganar participando en este reto, además del inestimable conocimiento, la experiencia?\*\*

&nbsp;

Pues...

\- Para quien se lleve el \*\*primer premio\*\*: Una tarjeta de regalo de Amazon de 200€, una suscripción anual a este Laboratorio, un certificado para que puedas fardar en LinkedIn de tu flamante victoria y, por supuesto, un logro que refleje que has sido el primer campeón en el primer reto de este Laboratorio.

\- Para quien obtenga el \*\*segundo premio\*\*: Una tarjeta de amazon de 50€, una suscripción anual a este Laboratorio y, por supuesto, un certificado que refleje tu posición en el podio.

\- Para quien obtenga el \*\*tercer premio\*\*: Una suscripción anual a este Laboratorio y el certificado de rigor de lo que has conseguido.

&nbsp;

Para el resto de participantes, tranquilos, si completáis el proyecto pero no recibís ninguno de estos premios no os llevaréis únicamente la satisfacción de haber sido capaz de llegar hasta el final, también tendréis un certificado que refleje vuestro trabajo y lo que habéis conseguido.

&nbsp;

Ahora sí, vamos a ver \*\*qué debes hacer para participar y optar a los premios y certificados\*\*.

&nbsp;

\#\# El problema

Con este reto, lo que buscamos es medir los límites de los modelos de inteligencia artificial de una forma rigurosa, que pueda verificarse y replicarse.

&nbsp;

Para conseguirlo, todos los participantes vamos a trabajar con un problema de conteo de apariciones de un determinado patrón dentro de una cadena de caracteres, incluyendo aquellas que se solapan.

&nbsp;

Un ejemplo:

\- Cadena: ABABACABAC

\- Patrón: ABA

\- Resultado correcto: 3

&nbsp;

Este problema es determinista, fácil de entender y podemos verificar la solución con un algoritmo muy sencillo. Pero, ¿qué características podría tener una cadena de este tipo para que un modelo de lenguaje fuese incapaz de resolver este problema correctamente? ¿Podemos identificar alguna estructura que provoque errores de forma sistemática? ¿Somos capaces de predecir cuándo va a fallar?

&nbsp;

Eso es precisamente lo que queremos investigar.

&nbsp;

\#\# El objetivo

Teniendo en cuenta el problema al que nos enfrentamos, lo que debemos hacer es diseñar una estrategia de construcción de cadenas y patrones que maximice la tasa de error de un modelo de lenguaje al resolver el problema planteado.&nbsp;

&nbsp;

No se trata encontrar una única cadena que provoque un error puntual, sino encontrar un sistema que permita generar nuevos casos de prueba en los que el modelo falle de forma consistente.

&nbsp;

Esto implica que debéis construir vuestra propia metodología experimental, recopilar datos, analizar los resultados y defender vuestras conclusiones.

&nbsp;

Conseguir el objetivo es importante, pero lo que se valorará especialmente no es tanto si se logra o no, sino la capacidad de formular hipótesis y contrastarlas para conseguir explicar porqué pasa lo que pasa, o lo que no pasa.

&nbsp;

\#\# Condiciones del reto

Para garantizar que todos trabajamos sobre un problema comparable, estas son las condiciones que se deben cumplir para considerar una participación valida:

1\. Las cadenas generadas deben tener entre 10 y 50 caracteres.

2\. Las cadenas generadas estarán formadas por combinaciones de las letras A, B y C. No se utilizará ningún otro caracter.

3\. Los patrones a localizar en las cadenas generadas tendrán entre 2 y 4 caracteres.

4\. Se contabilizarán todas las apariciones de los patrones a localizar, incluyendo aquellas solapadas.

5\. Se proporcionará un prompt sobre el que únicamente será necesario modificar la cadena y el patrón, y es obligatorio que los experimentos principales se hagan con este prompt. Sin embargo, si alguien decide utilizar otros prompts y estudiar otras casuísticas que puedan provocar fallos, registrando los resultados por separado y respaldando estos experimentos con evidencias, esto se valorará muy positivamente a la hora de elegir los ganadores.

6\. Se proporcionará un código para poder verificar de forma determinista si las cadenas se han evaluado correctamente y el número de patrones encontrados es el correcto. También se proporcionará un código para generar cadenas, pero este es simplemente una referencia y es parte del reto que creéis vuestro propio código generador.

7\. Se puede utilizar cualquier modelo, de hecho se recomienda hacer los experimentos con varios distintos, pero el modelo no podrá utilizar herramientas externas, ejecutar código ni consultar fuentes de información.

8\. No se pueden utilizar instrucciones engañosas, alterar el significado del problema ni proporcionar de forma deliberada información incorrecta al modelo.

9\. Se deben registrar evidencias de las ejecuciones y calcular la tasa de error (tasa de error (%) \= (respuestas incorrectas / respuestas totales) \* 100). Si no hay evidencias que demuestren de dónde sale tu tasa de error, no se dará por válida.

10\. Se debe adjuntar en las conclusiones un archivo csv con la estructura de la plantilla, que encontraréis en la carpeta con los documentos proporcionados para llevar a cabo el reto.

11\. Para garantizar un mínimo de rigor experimental, se deberán evaluar al menos 10 casos de prueba diferentes, realizando un mínimo de 3 ejecuciones independientes y sin contexto previo por cada caso. Todas las ejecuciones, independientemente de su resultado, deberán quedar registradas en la plantilla proporcionada, cumplimentando los campos correspondientes al modelo, su configuración, los resultados y las evidencias obtenidas.

&nbsp;

Aquí podéis encontrar todos los ficheros necesarios: https\://drive.google.com/drive/u/7/folders/1JgEdpIpkYKWec2fASnDQyIvJEWik-hAU

&nbsp;

Para participar:

\- Se debe crear un post en el apartado de Retos de este Laboratorio, con título RETO \#001 \- \<lo que quieras\>. Importante lo de RETO \#001 para identificar fácilmente las participaciones a revisar, no se revisará ninguna entrada que no incluya este título.

\- En el post creado se deben hacer mínimo 3 publicaciones:&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;\- Una con el planteamiento inicial, indicando la hipótesis y la metodología a utilizar, durante la primera semana.&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;\- Otra con el desarrollo, durante la segunda o la tercera semana.&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;\- Una última con las conclusiones, durante la cuarta semana. Las conclusiones deben empezar con un resumen que incluya los siguientes apartados, aunque posteriormente podéis añadir todo lo que queráis:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Hipótesis investigada:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Estrategia desarrollada:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Modelo y configuración:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Número de casos de prueba:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Número total de ejecuciones:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Tasa de error obtenida:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Principales descubrimientos:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Posible explicación de los fallos:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Limitaciones del experimento:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- CSV de resultados y código utilizado:

&nbsp;&nbsp;&nbsp;&nbsp;\- Se pueden hacer más publicaciones en el medio, y se valorará positivamente cualquier contribución y detalle que aporte más información sobre lo que se está haciendo, cómo y porqué.

&nbsp;

Para lo demás, se puede utilizar cualquier lenguaje de programación, librería o herramienta para generar los casos de prueba, automatizar la evaluación y analizar los resultados. También se pueden utilizar otras métricas además de la tasa de error.

&nbsp;

\#\# Fechas&nbsp;

El reto empieza oficialmente el día \*\*18/11/2026\*\* y termina el \*\*18/12/2026\*\*, ¡tenéis un mes entero para completarlo\!

&nbsp;

Los ganadores se anunciarán el 28/12/2026, y nos pondremos en contacto con todos ellos para enviar los premios.&nbsp;

&nbsp;

En cuanto a fechas, siempre tomaremos como referencia la hora peninsular española.

&nbsp;

\#\# Normas generales

\- La participación es individual y gratuita.

\- No es necesario disponer de una suscripción de pago al Laboratorio.

\- Se permite utilizar IA como herramienta de apoyo para desarrollar código, diseñar experimentos y analizar datos, pero cada participante deberá ser capaz de defender su propia investigación.

\- Se permite colaborar con otros participantes, siempre que se reconozcan sus aportaciones.

\- No se permite fabricar, manipular, ocultar ni seleccionar interesadamente los resultados experimentales.

\- No se admitirán investigaciones copiadas sin atribución.

\- Se podrá solicitar información adicional o reproducir cualquier experimento presentado.

\- El incumplimiento de las reglas podrá suponer la descalificación.

&nbsp;

\#\# Preguntas y dudas

&nbsp;

Dejo este apartado para registrar las preguntas que me planteéis sobre el reto y que puedan ser útiles para otros participantes.

&nbsp;

\--&nbsp;

&nbsp;

Con esto quedan oficialmente inaugurados los retos del Laboratorio. ¡Espero vuestras propuestas\!

&nbsp;