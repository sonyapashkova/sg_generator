# Генератор комбинирования с помощью псевдослучайных прореживаний. SG-генератор

LFSR-генератор _G<sub>1</sub>_ порождает "элеметарную" двоичную последовательность __{a<sub>t</sub>}__, а LFSR-генератор _G<sub>2</sub>_ порождает двоичную "селектирующую" последовательность __{s<sub>t</sub>}__. С помощью этих двух последовательностей __{a<sub>t</sub>}__, __{s<sub>t</sub>}__ строится выходная последовательность __{x<sub>t</sub>}__, включающая те биты __{a<sub>t</sub>}__, для которых
соответствующее значение селектора __s<sub>t</sub>__ = 1; если __s<sub>t</sub>__ = 0, то значение __a<sub>t</sub>__ игнорируется. На выходе алгоритма получаем псевдослучайную двойчную последовательность. 

Файлы `state.txt` и `polynomials.txt` служат для хранения начальных состояний и полиномов, которые требуются при инициализации генераторов LFSR. В файле `result.txt` сохраняется сгенерированная псевдослучайная последовательноть и ее характеристики (период, критерий Пирсона).