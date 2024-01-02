```python
%pip install pandas
```

    Defaulting to user installation because normal site-packages is not writeableNote: you may need to restart the kernel to use updated packages.
    
    Requirement already satisfied: pandas in c:\users\mukul.bindal\appdata\roaming\python\python312\site-packages (2.1.4)
    Requirement already satisfied: numpy<2,>=1.26.0 in c:\users\mukul.bindal\appdata\roaming\python\python312\site-packages (from pandas) (1.26.2)
    Requirement already satisfied: python-dateutil>=2.8.2 in c:\users\mukul.bindal\appdata\roaming\python\python312\site-packages (from pandas) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in c:\users\mukul.bindal\appdata\roaming\python\python312\site-packages (from pandas) (2023.3.post1)
    Requirement already satisfied: tzdata>=2022.1 in c:\users\mukul.bindal\appdata\roaming\python\python312\site-packages (from pandas) (2023.4)
    Requirement already satisfied: six>=1.5 in c:\users\mukul.bindal\appdata\roaming\python\python312\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
    

    
    [notice] A new release of pip is available: 23.2.1 -> 23.3.2
    [notice] To update, run: python.exe -m pip install --upgrade pip
    


```python
import pandas as pd
```


```python
# Read data from CSV file
df = pd.read_csv('pokemon.csv')
df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>318</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>405</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>525</td>
      <td>80</td>
      <td>82</td>
      <td>83</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>625</td>
      <td>80</td>
      <td>100</td>
      <td>123</td>
      <td>122</td>
      <td>120</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Charmander</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>309</td>
      <td>39</td>
      <td>52</td>
      <td>43</td>
      <td>60</td>
      <td>50</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>795</th>
      <td>719</td>
      <td>Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>600</td>
      <td>50</td>
      <td>100</td>
      <td>150</td>
      <td>100</td>
      <td>150</td>
      <td>50</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>796</th>
      <td>719</td>
      <td>DiancieMega Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>700</td>
      <td>50</td>
      <td>160</td>
      <td>110</td>
      <td>160</td>
      <td>110</td>
      <td>110</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>797</th>
      <td>720</td>
      <td>HoopaHoopa Confined</td>
      <td>Psychic</td>
      <td>Ghost</td>
      <td>600</td>
      <td>80</td>
      <td>110</td>
      <td>60</td>
      <td>150</td>
      <td>130</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>798</th>
      <td>720</td>
      <td>HoopaHoopa Unbound</td>
      <td>Psychic</td>
      <td>Dark</td>
      <td>680</td>
      <td>80</td>
      <td>160</td>
      <td>60</td>
      <td>170</td>
      <td>130</td>
      <td>80</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>799</th>
      <td>721</td>
      <td>Volcanion</td>
      <td>Fire</td>
      <td>Water</td>
      <td>600</td>
      <td>80</td>
      <td>110</td>
      <td>120</td>
      <td>130</td>
      <td>90</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 13 columns</p>
</div>




```python
# Read data from xls file
df_xls = pd.read_excel('pokemon.xls')
df_xls

# Read data from tab separated file
df_tab = pd.read_csv('pokemon.tsv', delimiter='\t')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[14], line 2
          1 # Read data from xls file
    ----> 2 df_xls = pd.read_excel('pokemon.csv')
          3 df_xls
    

    File ~\AppData\Roaming\Python\Python312\site-packages\pandas\io\excel\_base.py:504, in read_excel(io, sheet_name, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, parse_dates, date_parser, date_format, thousands, decimal, comment, skipfooter, storage_options, dtype_backend, engine_kwargs)
        502 if not isinstance(io, ExcelFile):
        503     should_close = True
    --> 504     io = ExcelFile(
        505         io,
        506         storage_options=storage_options,
        507         engine=engine,
        508         engine_kwargs=engine_kwargs,
        509     )
        510 elif engine and engine != io.engine:
        511     raise ValueError(
        512         "Engine should not be specified when passing "
        513         "an ExcelFile - ExcelFile already has the engine set"
        514     )
    

    File ~\AppData\Roaming\Python\Python312\site-packages\pandas\io\excel\_base.py:1567, in ExcelFile.__init__(self, path_or_buffer, engine, storage_options, engine_kwargs)
       1563     ext = inspect_excel_format(
       1564         content_or_path=path_or_buffer, storage_options=storage_options
       1565     )
       1566     if ext is None:
    -> 1567         raise ValueError(
       1568             "Excel file format cannot be determined, you must specify "
       1569             "an engine manually."
       1570         )
       1572 engine = config.get_option(f"io.excel.{ext}.reader", silent=True)
       1573 if engine == "auto":
    

    ValueError: Excel file format cannot be determined, you must specify an engine manually.



```python
# Reading first 5 and last 5 rows
df.head(5), df.tail(5)
```




    (   #                   Name Type 1  Type 2  Total  HP  Attack  Defense  \
     0  1              Bulbasaur  Grass  Poison    318  45      49       49   
     1  2                Ivysaur  Grass  Poison    405  60      62       63   
     2  3               Venusaur  Grass  Poison    525  80      82       83   
     3  3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123   
     4  4             Charmander   Fire     NaN    309  39      52       43   
     
        Sp. Atk  Sp. Def  Speed  Generation  Legendary  
     0       65       65     45           1      False  
     1       80       80     60           1      False  
     2      100      100     80           1      False  
     3      122      120     80           1      False  
     4       60       50     65           1      False  ,
            #                 Name   Type 1 Type 2  Total  HP  Attack  Defense  \
     795  719              Diancie     Rock  Fairy    600  50     100      150   
     796  719  DiancieMega Diancie     Rock  Fairy    700  50     160      110   
     797  720  HoopaHoopa Confined  Psychic  Ghost    600  80     110       60   
     798  720   HoopaHoopa Unbound  Psychic   Dark    680  80     160       60   
     799  721            Volcanion     Fire  Water    600  80     110      120   
     
          Sp. Atk  Sp. Def  Speed  Generation  Legendary  
     795      100      150     50           6       True  
     796      160      110    110           6       True  
     797      150      130     70           6       True  
     798      170      130     80           6       True  
     799      130       90     70           6       True  )




```python
# Read Headers
df.columns
```




    Index(['#', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense',
           'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary'],
          dtype='object')




```python
# Read each column
df['Name']
df.Name
```




    0                  Bulbasaur
    1                    Ivysaur
    2                   Venusaur
    3      VenusaurMega Venusaur
    4                 Charmander
                   ...          
    795                  Diancie
    796      DiancieMega Diancie
    797      HoopaHoopa Confined
    798       HoopaHoopa Unbound
    799                Volcanion
    Name: Name, Length: 800, dtype: object




```python
# Reading multiple columns
df[['Name', 'Attack', 'HP']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Attack</th>
      <th>HP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bulbasaur</td>
      <td>49</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ivysaur</td>
      <td>62</td>
      <td>60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Venusaur</td>
      <td>82</td>
      <td>80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>VenusaurMega Venusaur</td>
      <td>100</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Charmander</td>
      <td>52</td>
      <td>39</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>795</th>
      <td>Diancie</td>
      <td>100</td>
      <td>50</td>
    </tr>
    <tr>
      <th>796</th>
      <td>DiancieMega Diancie</td>
      <td>160</td>
      <td>50</td>
    </tr>
    <tr>
      <th>797</th>
      <td>HoopaHoopa Confined</td>
      <td>110</td>
      <td>80</td>
    </tr>
    <tr>
      <th>798</th>
      <td>HoopaHoopa Unbound</td>
      <td>160</td>
      <td>80</td>
    </tr>
    <tr>
      <th>799</th>
      <td>Volcanion</td>
      <td>110</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 3 columns</p>
</div>




```python
# Reading specific rows in a column --> supports slicing
df['Name'][4:12:3]
df[['Name', 'HP', 'Attack']][10:50:5]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>HP</th>
      <th>Attack</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>Wartortle</td>
      <td>59</td>
      <td>63</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Butterfree</td>
      <td>60</td>
      <td>45</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Pidgey</td>
      <td>40</td>
      <td>45</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Raticate</td>
      <td>55</td>
      <td>81</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Pikachu</td>
      <td>35</td>
      <td>55</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Nidorina</td>
      <td>70</td>
      <td>62</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Clefairy</td>
      <td>70</td>
      <td>45</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Wigglytuff</td>
      <td>140</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reading a specific row only
df.iloc[10], type(df.iloc[10])
```




    (#                     8
     Name          Wartortle
     Type 1            Water
     Type 2              NaN
     Total               405
     HP                   59
     Attack               63
     Defense              80
     Sp. Atk              65
     Sp. Def              80
     Speed                58
     Generation            1
     Legendary         False
     Name: 10, dtype: object,
     pandas.core.series.Series)




```python
# Reading rows with slicing
df.iloc[10:40:8]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>8</td>
      <td>Wartortle</td>
      <td>Water</td>
      <td>NaN</td>
      <td>405</td>
      <td>59</td>
      <td>63</td>
      <td>80</td>
      <td>65</td>
      <td>80</td>
      <td>58</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>18</th>
      <td>15</td>
      <td>Beedrill</td>
      <td>Bug</td>
      <td>Poison</td>
      <td>395</td>
      <td>65</td>
      <td>90</td>
      <td>40</td>
      <td>45</td>
      <td>80</td>
      <td>75</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>26</th>
      <td>21</td>
      <td>Spearow</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>262</td>
      <td>40</td>
      <td>60</td>
      <td>30</td>
      <td>31</td>
      <td>31</td>
      <td>70</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>34</th>
      <td>29</td>
      <td>Nidoran♀</td>
      <td>Poison</td>
      <td>NaN</td>
      <td>275</td>
      <td>55</td>
      <td>47</td>
      <td>52</td>
      <td>40</td>
      <td>40</td>
      <td>41</td>
      <td>1</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reading value at a specific row, column
df.iloc[2, 3]
```




    'Poison'




```python
# Looping in a dataframe
for index, row in df.iterrows():
    # print(index, row)
    # row is a Series object which is kind of dictionary
    print(index, row['Name'], row['HP'])
```

    0 Bulbasaur 45
    1 Ivysaur 60
    2 Venusaur 80
    3 VenusaurMega Venusaur 80
    4 Charmander 39
    5 Charmeleon 58
    6 Charizard 78
    7 CharizardMega Charizard X 78
    8 CharizardMega Charizard Y 78
    9 Squirtle 44
    10 Wartortle 59
    11 Blastoise 79
    12 BlastoiseMega Blastoise 79
    13 Caterpie 45
    14 Metapod 50
    15 Butterfree 60
    16 Weedle 40
    17 Kakuna 45
    18 Beedrill 65
    19 BeedrillMega Beedrill 65
    20 Pidgey 40
    21 Pidgeotto 63
    22 Pidgeot 83
    23 PidgeotMega Pidgeot 83
    24 Rattata 30
    25 Raticate 55
    26 Spearow 40
    27 Fearow 65
    28 Ekans 35
    29 Arbok 60
    30 Pikachu 35
    31 Raichu 60
    32 Sandshrew 50
    33 Sandslash 75
    34 Nidoran♀ 55
    35 Nidorina 70
    36 Nidoqueen 90
    37 Nidoran♂ 46
    38 Nidorino 61
    39 Nidoking 81
    40 Clefairy 70
    41 Clefable 95
    42 Vulpix 38
    43 Ninetales 73
    44 Jigglypuff 115
    45 Wigglytuff 140
    46 Zubat 40
    47 Golbat 75
    48 Oddish 45
    49 Gloom 60
    50 Vileplume 75
    51 Paras 35
    52 Parasect 60
    53 Venonat 60
    54 Venomoth 70
    55 Diglett 10
    56 Dugtrio 35
    57 Meowth 40
    58 Persian 65
    59 Psyduck 50
    60 Golduck 80
    61 Mankey 40
    62 Primeape 65
    63 Growlithe 55
    64 Arcanine 90
    65 Poliwag 40
    66 Poliwhirl 65
    67 Poliwrath 90
    68 Abra 25
    69 Kadabra 40
    70 Alakazam 55
    71 AlakazamMega Alakazam 55
    72 Machop 70
    73 Machoke 80
    74 Machamp 90
    75 Bellsprout 50
    76 Weepinbell 65
    77 Victreebel 80
    78 Tentacool 40
    79 Tentacruel 80
    80 Geodude 40
    81 Graveler 55
    82 Golem 80
    83 Ponyta 50
    84 Rapidash 65
    85 Slowpoke 90
    86 Slowbro 95
    87 SlowbroMega Slowbro 95
    88 Magnemite 25
    89 Magneton 50
    90 Farfetch'd 52
    91 Doduo 35
    92 Dodrio 60
    93 Seel 65
    94 Dewgong 90
    95 Grimer 80
    96 Muk 105
    97 Shellder 30
    98 Cloyster 50
    99 Gastly 30
    100 Haunter 45
    101 Gengar 60
    102 GengarMega Gengar 60
    103 Onix 35
    104 Drowzee 60
    105 Hypno 85
    106 Krabby 30
    107 Kingler 55
    108 Voltorb 40
    109 Electrode 60
    110 Exeggcute 60
    111 Exeggutor 95
    112 Cubone 50
    113 Marowak 60
    114 Hitmonlee 50
    115 Hitmonchan 50
    116 Lickitung 90
    117 Koffing 40
    118 Weezing 65
    119 Rhyhorn 80
    120 Rhydon 105
    121 Chansey 250
    122 Tangela 65
    123 Kangaskhan 105
    124 KangaskhanMega Kangaskhan 105
    125 Horsea 30
    126 Seadra 55
    127 Goldeen 45
    128 Seaking 80
    129 Staryu 30
    130 Starmie 60
    131 Mr. Mime 40
    132 Scyther 70
    133 Jynx 65
    134 Electabuzz 65
    135 Magmar 65
    136 Pinsir 65
    137 PinsirMega Pinsir 65
    138 Tauros 75
    139 Magikarp 20
    140 Gyarados 95
    141 GyaradosMega Gyarados 95
    142 Lapras 130
    143 Ditto 48
    144 Eevee 55
    145 Vaporeon 130
    146 Jolteon 65
    147 Flareon 65
    148 Porygon 65
    149 Omanyte 35
    150 Omastar 70
    151 Kabuto 30
    152 Kabutops 60
    153 Aerodactyl 80
    154 AerodactylMega Aerodactyl 80
    155 Snorlax 160
    156 Articuno 90
    157 Zapdos 90
    158 Moltres 90
    159 Dratini 41
    160 Dragonair 61
    161 Dragonite 91
    162 Mewtwo 106
    163 MewtwoMega Mewtwo X 106
    164 MewtwoMega Mewtwo Y 106
    165 Mew 100
    166 Chikorita 45
    167 Bayleef 60
    168 Meganium 80
    169 Cyndaquil 39
    170 Quilava 58
    171 Typhlosion 78
    172 Totodile 50
    173 Croconaw 65
    174 Feraligatr 85
    175 Sentret 35
    176 Furret 85
    177 Hoothoot 60
    178 Noctowl 100
    179 Ledyba 40
    180 Ledian 55
    181 Spinarak 40
    182 Ariados 70
    183 Crobat 85
    184 Chinchou 75
    185 Lanturn 125
    186 Pichu 20
    187 Cleffa 50
    188 Igglybuff 90
    189 Togepi 35
    190 Togetic 55
    191 Natu 40
    192 Xatu 65
    193 Mareep 55
    194 Flaaffy 70
    195 Ampharos 90
    196 AmpharosMega Ampharos 90
    197 Bellossom 75
    198 Marill 70
    199 Azumarill 100
    200 Sudowoodo 70
    201 Politoed 90
    202 Hoppip 35
    203 Skiploom 55
    204 Jumpluff 75
    205 Aipom 55
    206 Sunkern 30
    207 Sunflora 75
    208 Yanma 65
    209 Wooper 55
    210 Quagsire 95
    211 Espeon 65
    212 Umbreon 95
    213 Murkrow 60
    214 Slowking 95
    215 Misdreavus 60
    216 Unown 48
    217 Wobbuffet 190
    218 Girafarig 70
    219 Pineco 50
    220 Forretress 75
    221 Dunsparce 100
    222 Gligar 65
    223 Steelix 75
    224 SteelixMega Steelix 75
    225 Snubbull 60
    226 Granbull 90
    227 Qwilfish 65
    228 Scizor 70
    229 ScizorMega Scizor 70
    230 Shuckle 20
    231 Heracross 80
    232 HeracrossMega Heracross 80
    233 Sneasel 55
    234 Teddiursa 60
    235 Ursaring 90
    236 Slugma 40
    237 Magcargo 50
    238 Swinub 50
    239 Piloswine 100
    240 Corsola 55
    241 Remoraid 35
    242 Octillery 75
    243 Delibird 45
    244 Mantine 65
    245 Skarmory 65
    246 Houndour 45
    247 Houndoom 75
    248 HoundoomMega Houndoom 75
    249 Kingdra 75
    250 Phanpy 90
    251 Donphan 90
    252 Porygon2 85
    253 Stantler 73
    254 Smeargle 55
    255 Tyrogue 35
    256 Hitmontop 50
    257 Smoochum 45
    258 Elekid 45
    259 Magby 45
    260 Miltank 95
    261 Blissey 255
    262 Raikou 90
    263 Entei 115
    264 Suicune 100
    265 Larvitar 50
    266 Pupitar 70
    267 Tyranitar 100
    268 TyranitarMega Tyranitar 100
    269 Lugia 106
    270 Ho-oh 106
    271 Celebi 100
    272 Treecko 40
    273 Grovyle 50
    274 Sceptile 70
    275 SceptileMega Sceptile 70
    276 Torchic 45
    277 Combusken 60
    278 Blaziken 80
    279 BlazikenMega Blaziken 80
    280 Mudkip 50
    281 Marshtomp 70
    282 Swampert 100
    283 SwampertMega Swampert 100
    284 Poochyena 35
    285 Mightyena 70
    286 Zigzagoon 38
    287 Linoone 78
    288 Wurmple 45
    289 Silcoon 50
    290 Beautifly 60
    291 Cascoon 50
    292 Dustox 60
    293 Lotad 40
    294 Lombre 60
    295 Ludicolo 80
    296 Seedot 40
    297 Nuzleaf 70
    298 Shiftry 90
    299 Taillow 40
    300 Swellow 60
    301 Wingull 40
    302 Pelipper 60
    303 Ralts 28
    304 Kirlia 38
    305 Gardevoir 68
    306 GardevoirMega Gardevoir 68
    307 Surskit 40
    308 Masquerain 70
    309 Shroomish 60
    310 Breloom 60
    311 Slakoth 60
    312 Vigoroth 80
    313 Slaking 150
    314 Nincada 31
    315 Ninjask 61
    316 Shedinja 1
    317 Whismur 64
    318 Loudred 84
    319 Exploud 104
    320 Makuhita 72
    321 Hariyama 144
    322 Azurill 50
    323 Nosepass 30
    324 Skitty 50
    325 Delcatty 70
    326 Sableye 50
    327 SableyeMega Sableye 50
    328 Mawile 50
    329 MawileMega Mawile 50
    330 Aron 50
    331 Lairon 60
    332 Aggron 70
    333 AggronMega Aggron 70
    334 Meditite 30
    335 Medicham 60
    336 MedichamMega Medicham 60
    337 Electrike 40
    338 Manectric 70
    339 ManectricMega Manectric 70
    340 Plusle 60
    341 Minun 60
    342 Volbeat 65
    343 Illumise 65
    344 Roselia 50
    345 Gulpin 70
    346 Swalot 100
    347 Carvanha 45
    348 Sharpedo 70
    349 SharpedoMega Sharpedo 70
    350 Wailmer 130
    351 Wailord 170
    352 Numel 60
    353 Camerupt 70
    354 CameruptMega Camerupt 70
    355 Torkoal 70
    356 Spoink 60
    357 Grumpig 80
    358 Spinda 60
    359 Trapinch 45
    360 Vibrava 50
    361 Flygon 80
    362 Cacnea 50
    363 Cacturne 70
    364 Swablu 45
    365 Altaria 75
    366 AltariaMega Altaria 75
    367 Zangoose 73
    368 Seviper 73
    369 Lunatone 70
    370 Solrock 70
    371 Barboach 50
    372 Whiscash 110
    373 Corphish 43
    374 Crawdaunt 63
    375 Baltoy 40
    376 Claydol 60
    377 Lileep 66
    378 Cradily 86
    379 Anorith 45
    380 Armaldo 75
    381 Feebas 20
    382 Milotic 95
    383 Castform 70
    384 Kecleon 60
    385 Shuppet 44
    386 Banette 64
    387 BanetteMega Banette 64
    388 Duskull 20
    389 Dusclops 40
    390 Tropius 99
    391 Chimecho 65
    392 Absol 65
    393 AbsolMega Absol 65
    394 Wynaut 95
    395 Snorunt 50
    396 Glalie 80
    397 GlalieMega Glalie 80
    398 Spheal 70
    399 Sealeo 90
    400 Walrein 110
    401 Clamperl 35
    402 Huntail 55
    403 Gorebyss 55
    404 Relicanth 100
    405 Luvdisc 43
    406 Bagon 45
    407 Shelgon 65
    408 Salamence 95
    409 SalamenceMega Salamence 95
    410 Beldum 40
    411 Metang 60
    412 Metagross 80
    413 MetagrossMega Metagross 80
    414 Regirock 80
    415 Regice 80
    416 Registeel 80
    417 Latias 80
    418 LatiasMega Latias 80
    419 Latios 80
    420 LatiosMega Latios 80
    421 Kyogre 100
    422 KyogrePrimal Kyogre 100
    423 Groudon 100
    424 GroudonPrimal Groudon 100
    425 Rayquaza 105
    426 RayquazaMega Rayquaza 105
    427 Jirachi 100
    428 DeoxysNormal Forme 50
    429 DeoxysAttack Forme 50
    430 DeoxysDefense Forme 50
    431 DeoxysSpeed Forme 50
    432 Turtwig 55
    433 Grotle 75
    434 Torterra 95
    435 Chimchar 44
    436 Monferno 64
    437 Infernape 76
    438 Piplup 53
    439 Prinplup 64
    440 Empoleon 84
    441 Starly 40
    442 Staravia 55
    443 Staraptor 85
    444 Bidoof 59
    445 Bibarel 79
    446 Kricketot 37
    447 Kricketune 77
    448 Shinx 45
    449 Luxio 60
    450 Luxray 80
    451 Budew 40
    452 Roserade 60
    453 Cranidos 67
    454 Rampardos 97
    455 Shieldon 30
    456 Bastiodon 60
    457 Burmy 40
    458 WormadamPlant Cloak 60
    459 WormadamSandy Cloak 60
    460 WormadamTrash Cloak 60
    461 Mothim 70
    462 Combee 30
    463 Vespiquen 70
    464 Pachirisu 60
    465 Buizel 55
    466 Floatzel 85
    467 Cherubi 45
    468 Cherrim 70
    469 Shellos 76
    470 Gastrodon 111
    471 Ambipom 75
    472 Drifloon 90
    473 Drifblim 150
    474 Buneary 55
    475 Lopunny 65
    476 LopunnyMega Lopunny 65
    477 Mismagius 60
    478 Honchkrow 100
    479 Glameow 49
    480 Purugly 71
    481 Chingling 45
    482 Stunky 63
    483 Skuntank 103
    484 Bronzor 57
    485 Bronzong 67
    486 Bonsly 50
    487 Mime Jr. 20
    488 Happiny 100
    489 Chatot 76
    490 Spiritomb 50
    491 Gible 58
    492 Gabite 68
    493 Garchomp 108
    494 GarchompMega Garchomp 108
    495 Munchlax 135
    496 Riolu 40
    497 Lucario 70
    498 LucarioMega Lucario 70
    499 Hippopotas 68
    500 Hippowdon 108
    501 Skorupi 40
    502 Drapion 70
    503 Croagunk 48
    504 Toxicroak 83
    505 Carnivine 74
    506 Finneon 49
    507 Lumineon 69
    508 Mantyke 45
    509 Snover 60
    510 Abomasnow 90
    511 AbomasnowMega Abomasnow 90
    512 Weavile 70
    513 Magnezone 70
    514 Lickilicky 110
    515 Rhyperior 115
    516 Tangrowth 100
    517 Electivire 75
    518 Magmortar 75
    519 Togekiss 85
    520 Yanmega 86
    521 Leafeon 65
    522 Glaceon 65
    523 Gliscor 75
    524 Mamoswine 110
    525 Porygon-Z 85
    526 Gallade 68
    527 GalladeMega Gallade 68
    528 Probopass 60
    529 Dusknoir 45
    530 Froslass 70
    531 Rotom 50
    532 RotomHeat Rotom 50
    533 RotomWash Rotom 50
    534 RotomFrost Rotom 50
    535 RotomFan Rotom 50
    536 RotomMow Rotom 50
    537 Uxie 75
    538 Mesprit 80
    539 Azelf 75
    540 Dialga 100
    541 Palkia 90
    542 Heatran 91
    543 Regigigas 110
    544 GiratinaAltered Forme 150
    545 GiratinaOrigin Forme 150
    546 Cresselia 120
    547 Phione 80
    548 Manaphy 100
    549 Darkrai 70
    550 ShayminLand Forme 100
    551 ShayminSky Forme 100
    552 Arceus 120
    553 Victini 100
    554 Snivy 45
    555 Servine 60
    556 Serperior 75
    557 Tepig 65
    558 Pignite 90
    559 Emboar 110
    560 Oshawott 55
    561 Dewott 75
    562 Samurott 95
    563 Patrat 45
    564 Watchog 60
    565 Lillipup 45
    566 Herdier 65
    567 Stoutland 85
    568 Purrloin 41
    569 Liepard 64
    570 Pansage 50
    571 Simisage 75
    572 Pansear 50
    573 Simisear 75
    574 Panpour 50
    575 Simipour 75
    576 Munna 76
    577 Musharna 116
    578 Pidove 50
    579 Tranquill 62
    580 Unfezant 80
    581 Blitzle 45
    582 Zebstrika 75
    583 Roggenrola 55
    584 Boldore 70
    585 Gigalith 85
    586 Woobat 55
    587 Swoobat 67
    588 Drilbur 60
    589 Excadrill 110
    590 Audino 103
    591 AudinoMega Audino 103
    592 Timburr 75
    593 Gurdurr 85
    594 Conkeldurr 105
    595 Tympole 50
    596 Palpitoad 75
    597 Seismitoad 105
    598 Throh 120
    599 Sawk 75
    600 Sewaddle 45
    601 Swadloon 55
    602 Leavanny 75
    603 Venipede 30
    604 Whirlipede 40
    605 Scolipede 60
    606 Cottonee 40
    607 Whimsicott 60
    608 Petilil 45
    609 Lilligant 70
    610 Basculin 70
    611 Sandile 50
    612 Krokorok 60
    613 Krookodile 95
    614 Darumaka 70
    615 DarmanitanStandard Mode 105
    616 DarmanitanZen Mode 105
    617 Maractus 75
    618 Dwebble 50
    619 Crustle 70
    620 Scraggy 50
    621 Scrafty 65
    622 Sigilyph 72
    623 Yamask 38
    624 Cofagrigus 58
    625 Tirtouga 54
    626 Carracosta 74
    627 Archen 55
    628 Archeops 75
    629 Trubbish 50
    630 Garbodor 80
    631 Zorua 40
    632 Zoroark 60
    633 Minccino 55
    634 Cinccino 75
    635 Gothita 45
    636 Gothorita 60
    637 Gothitelle 70
    638 Solosis 45
    639 Duosion 65
    640 Reuniclus 110
    641 Ducklett 62
    642 Swanna 75
    643 Vanillite 36
    644 Vanillish 51
    645 Vanilluxe 71
    646 Deerling 60
    647 Sawsbuck 80
    648 Emolga 55
    649 Karrablast 50
    650 Escavalier 70
    651 Foongus 69
    652 Amoonguss 114
    653 Frillish 55
    654 Jellicent 100
    655 Alomomola 165
    656 Joltik 50
    657 Galvantula 70
    658 Ferroseed 44
    659 Ferrothorn 74
    660 Klink 40
    661 Klang 60
    662 Klinklang 60
    663 Tynamo 35
    664 Eelektrik 65
    665 Eelektross 85
    666 Elgyem 55
    667 Beheeyem 75
    668 Litwick 50
    669 Lampent 60
    670 Chandelure 60
    671 Axew 46
    672 Fraxure 66
    673 Haxorus 76
    674 Cubchoo 55
    675 Beartic 95
    676 Cryogonal 70
    677 Shelmet 50
    678 Accelgor 80
    679 Stunfisk 109
    680 Mienfoo 45
    681 Mienshao 65
    682 Druddigon 77
    683 Golett 59
    684 Golurk 89
    685 Pawniard 45
    686 Bisharp 65
    687 Bouffalant 95
    688 Rufflet 70
    689 Braviary 100
    690 Vullaby 70
    691 Mandibuzz 110
    692 Heatmor 85
    693 Durant 58
    694 Deino 52
    695 Zweilous 72
    696 Hydreigon 92
    697 Larvesta 55
    698 Volcarona 85
    699 Cobalion 91
    700 Terrakion 91
    701 Virizion 91
    702 TornadusIncarnate Forme 79
    703 TornadusTherian Forme 79
    704 ThundurusIncarnate Forme 79
    705 ThundurusTherian Forme 79
    706 Reshiram 100
    707 Zekrom 100
    708 LandorusIncarnate Forme 89
    709 LandorusTherian Forme 89
    710 Kyurem 125
    711 KyuremBlack Kyurem 125
    712 KyuremWhite Kyurem 125
    713 KeldeoOrdinary Forme 91
    714 KeldeoResolute Forme 91
    715 MeloettaAria Forme 100
    716 MeloettaPirouette Forme 100
    717 Genesect 71
    718 Chespin 56
    719 Quilladin 61
    720 Chesnaught 88
    721 Fennekin 40
    722 Braixen 59
    723 Delphox 75
    724 Froakie 41
    725 Frogadier 54
    726 Greninja 72
    727 Bunnelby 38
    728 Diggersby 85
    729 Fletchling 45
    730 Fletchinder 62
    731 Talonflame 78
    732 Scatterbug 38
    733 Spewpa 45
    734 Vivillon 80
    735 Litleo 62
    736 Pyroar 86
    737 Flabébé 44
    738 Floette 54
    739 Florges 78
    740 Skiddo 66
    741 Gogoat 123
    742 Pancham 67
    743 Pangoro 95
    744 Furfrou 75
    745 Espurr 62
    746 MeowsticMale 74
    747 MeowsticFemale 74
    748 Honedge 45
    749 Doublade 59
    750 AegislashBlade Forme 60
    751 AegislashShield Forme 60
    752 Spritzee 78
    753 Aromatisse 101
    754 Swirlix 62
    755 Slurpuff 82
    756 Inkay 53
    757 Malamar 86
    758 Binacle 42
    759 Barbaracle 72
    760 Skrelp 50
    761 Dragalge 65
    762 Clauncher 50
    763 Clawitzer 71
    764 Helioptile 44
    765 Heliolisk 62
    766 Tyrunt 58
    767 Tyrantrum 82
    768 Amaura 77
    769 Aurorus 123
    770 Sylveon 95
    771 Hawlucha 78
    772 Dedenne 67
    773 Carbink 50
    774 Goomy 45
    775 Sliggoo 68
    776 Goodra 90
    777 Klefki 57
    778 Phantump 43
    779 Trevenant 85
    780 PumpkabooAverage Size 49
    781 PumpkabooSmall Size 44
    782 PumpkabooLarge Size 54
    783 PumpkabooSuper Size 59
    784 GourgeistAverage Size 65
    785 GourgeistSmall Size 55
    786 GourgeistLarge Size 75
    787 GourgeistSuper Size 85
    788 Bergmite 55
    789 Avalugg 95
    790 Noibat 40
    791 Noivern 85
    792 Xerneas 126
    793 Yveltal 126
    794 Zygarde50% Forme 108
    795 Diancie 50
    796 DiancieMega Diancie 50
    797 HoopaHoopa Confined 80
    798 HoopaHoopa Unbound 80
    799 Volcanion 80
    


```python
# Querying data
# We can use df.loc[] with our boolean conditions
df['Type 1'] == 'Fire'   #This is our condition just like numpy

# Get all rows where Type 1 is Fire
df.loc[df['Type 1'] == 'Fire']\
    .loc[df['HP'] > 80]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>64</th>
      <td>59</td>
      <td>Arcanine</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>555</td>
      <td>90</td>
      <td>110</td>
      <td>80</td>
      <td>100</td>
      <td>80</td>
      <td>95</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>158</th>
      <td>146</td>
      <td>Moltres</td>
      <td>Fire</td>
      <td>Flying</td>
      <td>580</td>
      <td>90</td>
      <td>100</td>
      <td>90</td>
      <td>125</td>
      <td>85</td>
      <td>90</td>
      <td>1</td>
      <td>True</td>
    </tr>
    <tr>
      <th>263</th>
      <td>244</td>
      <td>Entei</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>580</td>
      <td>115</td>
      <td>115</td>
      <td>85</td>
      <td>90</td>
      <td>75</td>
      <td>100</td>
      <td>2</td>
      <td>True</td>
    </tr>
    <tr>
      <th>270</th>
      <td>250</td>
      <td>Ho-oh</td>
      <td>Fire</td>
      <td>Flying</td>
      <td>680</td>
      <td>106</td>
      <td>130</td>
      <td>90</td>
      <td>110</td>
      <td>154</td>
      <td>90</td>
      <td>2</td>
      <td>True</td>
    </tr>
    <tr>
      <th>542</th>
      <td>485</td>
      <td>Heatran</td>
      <td>Fire</td>
      <td>Steel</td>
      <td>600</td>
      <td>91</td>
      <td>90</td>
      <td>106</td>
      <td>130</td>
      <td>106</td>
      <td>77</td>
      <td>4</td>
      <td>True</td>
    </tr>
    <tr>
      <th>558</th>
      <td>499</td>
      <td>Pignite</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>418</td>
      <td>90</td>
      <td>93</td>
      <td>55</td>
      <td>70</td>
      <td>55</td>
      <td>55</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>559</th>
      <td>500</td>
      <td>Emboar</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>528</td>
      <td>110</td>
      <td>123</td>
      <td>65</td>
      <td>100</td>
      <td>65</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>615</th>
      <td>555</td>
      <td>DarmanitanStandard Mode</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>480</td>
      <td>105</td>
      <td>140</td>
      <td>55</td>
      <td>30</td>
      <td>55</td>
      <td>95</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>616</th>
      <td>555</td>
      <td>DarmanitanZen Mode</td>
      <td>Fire</td>
      <td>Psychic</td>
      <td>540</td>
      <td>105</td>
      <td>30</td>
      <td>105</td>
      <td>140</td>
      <td>105</td>
      <td>55</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>692</th>
      <td>631</td>
      <td>Heatmor</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>484</td>
      <td>85</td>
      <td>97</td>
      <td>66</td>
      <td>105</td>
      <td>66</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>736</th>
      <td>668</td>
      <td>Pyroar</td>
      <td>Fire</td>
      <td>Normal</td>
      <td>507</td>
      <td>86</td>
      <td>68</td>
      <td>72</td>
      <td>109</td>
      <td>66</td>
      <td>106</td>
      <td>6</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Note that each operation that returns a dataframe, can be chained further with dataframe operations
# Get first 10 rows where HP > 200 and Type 1 = Fire
df.loc[df['HP'] > 80 ].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22</th>
      <td>18</td>
      <td>Pidgeot</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>479</td>
      <td>83</td>
      <td>80</td>
      <td>75</td>
      <td>70</td>
      <td>70</td>
      <td>101</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>23</th>
      <td>18</td>
      <td>PidgeotMega Pidgeot</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>579</td>
      <td>83</td>
      <td>80</td>
      <td>80</td>
      <td>135</td>
      <td>80</td>
      <td>121</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>36</th>
      <td>31</td>
      <td>Nidoqueen</td>
      <td>Poison</td>
      <td>Ground</td>
      <td>505</td>
      <td>90</td>
      <td>92</td>
      <td>87</td>
      <td>75</td>
      <td>85</td>
      <td>76</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>39</th>
      <td>34</td>
      <td>Nidoking</td>
      <td>Poison</td>
      <td>Ground</td>
      <td>505</td>
      <td>81</td>
      <td>102</td>
      <td>77</td>
      <td>85</td>
      <td>75</td>
      <td>85</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>41</th>
      <td>36</td>
      <td>Clefable</td>
      <td>Fairy</td>
      <td>NaN</td>
      <td>483</td>
      <td>95</td>
      <td>70</td>
      <td>73</td>
      <td>95</td>
      <td>90</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>44</th>
      <td>39</td>
      <td>Jigglypuff</td>
      <td>Normal</td>
      <td>Fairy</td>
      <td>270</td>
      <td>115</td>
      <td>45</td>
      <td>20</td>
      <td>45</td>
      <td>25</td>
      <td>20</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>45</th>
      <td>40</td>
      <td>Wigglytuff</td>
      <td>Normal</td>
      <td>Fairy</td>
      <td>435</td>
      <td>140</td>
      <td>70</td>
      <td>45</td>
      <td>85</td>
      <td>50</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>64</th>
      <td>59</td>
      <td>Arcanine</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>555</td>
      <td>90</td>
      <td>110</td>
      <td>80</td>
      <td>100</td>
      <td>80</td>
      <td>95</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>67</th>
      <td>62</td>
      <td>Poliwrath</td>
      <td>Water</td>
      <td>Fighting</td>
      <td>510</td>
      <td>90</td>
      <td>95</td>
      <td>95</td>
      <td>70</td>
      <td>90</td>
      <td>70</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>74</th>
      <td>68</td>
      <td>Machamp</td>
      <td>Fighting</td>
      <td>NaN</td>
      <td>505</td>
      <td>90</td>
      <td>130</td>
      <td>80</td>
      <td>65</td>
      <td>85</td>
      <td>55</td>
      <td>1</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Getting the statistics about the data
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>800.000000</td>
      <td>800.00000</td>
      <td>800.000000</td>
      <td>800.000000</td>
      <td>800.000000</td>
      <td>800.000000</td>
      <td>800.000000</td>
      <td>800.000000</td>
      <td>800.00000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>362.813750</td>
      <td>435.10250</td>
      <td>69.258750</td>
      <td>79.001250</td>
      <td>73.842500</td>
      <td>72.820000</td>
      <td>71.902500</td>
      <td>68.277500</td>
      <td>3.32375</td>
    </tr>
    <tr>
      <th>std</th>
      <td>208.343798</td>
      <td>119.96304</td>
      <td>25.534669</td>
      <td>32.457366</td>
      <td>31.183501</td>
      <td>32.722294</td>
      <td>27.828916</td>
      <td>29.060474</td>
      <td>1.66129</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>180.00000</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>10.000000</td>
      <td>20.000000</td>
      <td>5.000000</td>
      <td>1.00000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>184.750000</td>
      <td>330.00000</td>
      <td>50.000000</td>
      <td>55.000000</td>
      <td>50.000000</td>
      <td>49.750000</td>
      <td>50.000000</td>
      <td>45.000000</td>
      <td>2.00000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>364.500000</td>
      <td>450.00000</td>
      <td>65.000000</td>
      <td>75.000000</td>
      <td>70.000000</td>
      <td>65.000000</td>
      <td>70.000000</td>
      <td>65.000000</td>
      <td>3.00000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>539.250000</td>
      <td>515.00000</td>
      <td>80.000000</td>
      <td>100.000000</td>
      <td>90.000000</td>
      <td>95.000000</td>
      <td>90.000000</td>
      <td>90.000000</td>
      <td>5.00000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>721.000000</td>
      <td>780.00000</td>
      <td>255.000000</td>
      <td>190.000000</td>
      <td>230.000000</td>
      <td>194.000000</td>
      <td>230.000000</td>
      <td>180.000000</td>
      <td>6.00000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Sorting 
# Sort by Name
df.sort_values('Name')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>510</th>
      <td>460</td>
      <td>Abomasnow</td>
      <td>Grass</td>
      <td>Ice</td>
      <td>494</td>
      <td>90</td>
      <td>92</td>
      <td>75</td>
      <td>92</td>
      <td>85</td>
      <td>60</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>511</th>
      <td>460</td>
      <td>AbomasnowMega Abomasnow</td>
      <td>Grass</td>
      <td>Ice</td>
      <td>594</td>
      <td>90</td>
      <td>132</td>
      <td>105</td>
      <td>132</td>
      <td>105</td>
      <td>30</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>68</th>
      <td>63</td>
      <td>Abra</td>
      <td>Psychic</td>
      <td>NaN</td>
      <td>310</td>
      <td>25</td>
      <td>20</td>
      <td>15</td>
      <td>105</td>
      <td>55</td>
      <td>90</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>392</th>
      <td>359</td>
      <td>Absol</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>465</td>
      <td>65</td>
      <td>130</td>
      <td>60</td>
      <td>75</td>
      <td>60</td>
      <td>75</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>393</th>
      <td>359</td>
      <td>AbsolMega Absol</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>565</td>
      <td>65</td>
      <td>150</td>
      <td>60</td>
      <td>115</td>
      <td>60</td>
      <td>115</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>632</th>
      <td>571</td>
      <td>Zoroark</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>510</td>
      <td>60</td>
      <td>105</td>
      <td>60</td>
      <td>120</td>
      <td>60</td>
      <td>105</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>631</th>
      <td>570</td>
      <td>Zorua</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>330</td>
      <td>40</td>
      <td>65</td>
      <td>40</td>
      <td>80</td>
      <td>40</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>46</th>
      <td>41</td>
      <td>Zubat</td>
      <td>Poison</td>
      <td>Flying</td>
      <td>245</td>
      <td>40</td>
      <td>45</td>
      <td>35</td>
      <td>30</td>
      <td>40</td>
      <td>55</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>695</th>
      <td>634</td>
      <td>Zweilous</td>
      <td>Dark</td>
      <td>Dragon</td>
      <td>420</td>
      <td>72</td>
      <td>85</td>
      <td>70</td>
      <td>65</td>
      <td>70</td>
      <td>58</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>794</th>
      <td>718</td>
      <td>Zygarde50% Forme</td>
      <td>Dragon</td>
      <td>Ground</td>
      <td>600</td>
      <td>108</td>
      <td>100</td>
      <td>121</td>
      <td>81</td>
      <td>95</td>
      <td>95</td>
      <td>6</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 13 columns</p>
</div>




```python
# Sort by Name in descending order
df.sort_values('Name', ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>794</th>
      <td>718</td>
      <td>Zygarde50% Forme</td>
      <td>Dragon</td>
      <td>Ground</td>
      <td>600</td>
      <td>108</td>
      <td>100</td>
      <td>121</td>
      <td>81</td>
      <td>95</td>
      <td>95</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>695</th>
      <td>634</td>
      <td>Zweilous</td>
      <td>Dark</td>
      <td>Dragon</td>
      <td>420</td>
      <td>72</td>
      <td>85</td>
      <td>70</td>
      <td>65</td>
      <td>70</td>
      <td>58</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>46</th>
      <td>41</td>
      <td>Zubat</td>
      <td>Poison</td>
      <td>Flying</td>
      <td>245</td>
      <td>40</td>
      <td>45</td>
      <td>35</td>
      <td>30</td>
      <td>40</td>
      <td>55</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>631</th>
      <td>570</td>
      <td>Zorua</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>330</td>
      <td>40</td>
      <td>65</td>
      <td>40</td>
      <td>80</td>
      <td>40</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>632</th>
      <td>571</td>
      <td>Zoroark</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>510</td>
      <td>60</td>
      <td>105</td>
      <td>60</td>
      <td>120</td>
      <td>60</td>
      <td>105</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>393</th>
      <td>359</td>
      <td>AbsolMega Absol</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>565</td>
      <td>65</td>
      <td>150</td>
      <td>60</td>
      <td>115</td>
      <td>60</td>
      <td>115</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>392</th>
      <td>359</td>
      <td>Absol</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>465</td>
      <td>65</td>
      <td>130</td>
      <td>60</td>
      <td>75</td>
      <td>60</td>
      <td>75</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>68</th>
      <td>63</td>
      <td>Abra</td>
      <td>Psychic</td>
      <td>NaN</td>
      <td>310</td>
      <td>25</td>
      <td>20</td>
      <td>15</td>
      <td>105</td>
      <td>55</td>
      <td>90</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>511</th>
      <td>460</td>
      <td>AbomasnowMega Abomasnow</td>
      <td>Grass</td>
      <td>Ice</td>
      <td>594</td>
      <td>90</td>
      <td>132</td>
      <td>105</td>
      <td>132</td>
      <td>105</td>
      <td>30</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>510</th>
      <td>460</td>
      <td>Abomasnow</td>
      <td>Grass</td>
      <td>Ice</td>
      <td>494</td>
      <td>90</td>
      <td>92</td>
      <td>75</td>
      <td>92</td>
      <td>85</td>
      <td>60</td>
      <td>4</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 13 columns</p>
</div>




```python
# Sorting based on multiple columns
# Sort by HP in ascending order, Name in descending order

df.sort_values(['HP', 'Name'], ascending=[True, False])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>316</th>
      <td>292</td>
      <td>Shedinja</td>
      <td>Bug</td>
      <td>Ghost</td>
      <td>236</td>
      <td>1</td>
      <td>90</td>
      <td>45</td>
      <td>30</td>
      <td>30</td>
      <td>40</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>55</th>
      <td>50</td>
      <td>Diglett</td>
      <td>Ground</td>
      <td>NaN</td>
      <td>265</td>
      <td>10</td>
      <td>55</td>
      <td>25</td>
      <td>35</td>
      <td>45</td>
      <td>95</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>230</th>
      <td>213</td>
      <td>Shuckle</td>
      <td>Bug</td>
      <td>Rock</td>
      <td>505</td>
      <td>20</td>
      <td>10</td>
      <td>230</td>
      <td>10</td>
      <td>230</td>
      <td>5</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>186</th>
      <td>172</td>
      <td>Pichu</td>
      <td>Electric</td>
      <td>NaN</td>
      <td>205</td>
      <td>20</td>
      <td>40</td>
      <td>15</td>
      <td>35</td>
      <td>35</td>
      <td>60</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>487</th>
      <td>439</td>
      <td>Mime Jr.</td>
      <td>Psychic</td>
      <td>Fairy</td>
      <td>310</td>
      <td>20</td>
      <td>25</td>
      <td>45</td>
      <td>70</td>
      <td>90</td>
      <td>60</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>655</th>
      <td>594</td>
      <td>Alomomola</td>
      <td>Water</td>
      <td>NaN</td>
      <td>470</td>
      <td>165</td>
      <td>75</td>
      <td>80</td>
      <td>40</td>
      <td>45</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>351</th>
      <td>321</td>
      <td>Wailord</td>
      <td>Water</td>
      <td>NaN</td>
      <td>500</td>
      <td>170</td>
      <td>90</td>
      <td>45</td>
      <td>90</td>
      <td>45</td>
      <td>60</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>217</th>
      <td>202</td>
      <td>Wobbuffet</td>
      <td>Psychic</td>
      <td>NaN</td>
      <td>405</td>
      <td>190</td>
      <td>33</td>
      <td>58</td>
      <td>33</td>
      <td>58</td>
      <td>33</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>121</th>
      <td>113</td>
      <td>Chansey</td>
      <td>Normal</td>
      <td>NaN</td>
      <td>450</td>
      <td>250</td>
      <td>5</td>
      <td>5</td>
      <td>35</td>
      <td>105</td>
      <td>50</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>261</th>
      <td>242</td>
      <td>Blissey</td>
      <td>Normal</td>
      <td>NaN</td>
      <td>540</td>
      <td>255</td>
      <td>10</td>
      <td>10</td>
      <td>75</td>
      <td>135</td>
      <td>55</td>
      <td>2</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 13 columns</p>
</div>




```python
# Making changes to the data

# Adding a new column
# We can use the rows in order to create a new column

# Example: Create a new column AttDef - which is sum of attack and defense
df['AttDef'] = df['Attack'] + df['Defense']
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>318</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
      <td>98</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>405</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
      <td>125</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>525</td>
      <td>80</td>
      <td>82</td>
      <td>83</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>165</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>625</td>
      <td>80</td>
      <td>100</td>
      <td>123</td>
      <td>122</td>
      <td>120</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>223</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Charmander</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>309</td>
      <td>39</td>
      <td>52</td>
      <td>43</td>
      <td>60</td>
      <td>50</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
      <td>95</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>795</th>
      <td>719</td>
      <td>Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>600</td>
      <td>50</td>
      <td>100</td>
      <td>150</td>
      <td>100</td>
      <td>150</td>
      <td>50</td>
      <td>6</td>
      <td>True</td>
      <td>250</td>
    </tr>
    <tr>
      <th>796</th>
      <td>719</td>
      <td>DiancieMega Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>700</td>
      <td>50</td>
      <td>160</td>
      <td>110</td>
      <td>160</td>
      <td>110</td>
      <td>110</td>
      <td>6</td>
      <td>True</td>
      <td>270</td>
    </tr>
    <tr>
      <th>797</th>
      <td>720</td>
      <td>HoopaHoopa Confined</td>
      <td>Psychic</td>
      <td>Ghost</td>
      <td>600</td>
      <td>80</td>
      <td>110</td>
      <td>60</td>
      <td>150</td>
      <td>130</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
      <td>170</td>
    </tr>
    <tr>
      <th>798</th>
      <td>720</td>
      <td>HoopaHoopa Unbound</td>
      <td>Psychic</td>
      <td>Dark</td>
      <td>680</td>
      <td>80</td>
      <td>160</td>
      <td>60</td>
      <td>170</td>
      <td>130</td>
      <td>80</td>
      <td>6</td>
      <td>True</td>
      <td>220</td>
    </tr>
    <tr>
      <th>799</th>
      <td>721</td>
      <td>Volcanion</td>
      <td>Fire</td>
      <td>Water</td>
      <td>600</td>
      <td>80</td>
      <td>110</td>
      <td>120</td>
      <td>130</td>
      <td>90</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
      <td>230</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 14 columns</p>
</div>




```python
# Create a new column Summary - which describes each row
df['Summary'] = df['Name'] + ' is a '+ df['Type 1'] + ' pokemon which ' + ('is Legendary' if str(df['Legendary']) == 'True' else 'is not Legendary')
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>318</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
      <td>98</td>
      <td>Bulbasaur is a Grass pokemon which is not Lege...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>405</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
      <td>125</td>
      <td>Ivysaur is a Grass pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>525</td>
      <td>80</td>
      <td>82</td>
      <td>83</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>165</td>
      <td>Venusaur is a Grass pokemon which is not Legen...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>625</td>
      <td>80</td>
      <td>100</td>
      <td>123</td>
      <td>122</td>
      <td>120</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>223</td>
      <td>VenusaurMega Venusaur is a Grass pokemon which...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Charmander</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>309</td>
      <td>39</td>
      <td>52</td>
      <td>43</td>
      <td>60</td>
      <td>50</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
      <td>95</td>
      <td>Charmander is a Fire pokemon which is not Lege...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>795</th>
      <td>719</td>
      <td>Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>600</td>
      <td>50</td>
      <td>100</td>
      <td>150</td>
      <td>100</td>
      <td>150</td>
      <td>50</td>
      <td>6</td>
      <td>True</td>
      <td>250</td>
      <td>Diancie is a Rock pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>796</th>
      <td>719</td>
      <td>DiancieMega Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>700</td>
      <td>50</td>
      <td>160</td>
      <td>110</td>
      <td>160</td>
      <td>110</td>
      <td>110</td>
      <td>6</td>
      <td>True</td>
      <td>270</td>
      <td>DiancieMega Diancie is a Rock pokemon which is...</td>
    </tr>
    <tr>
      <th>797</th>
      <td>720</td>
      <td>HoopaHoopa Confined</td>
      <td>Psychic</td>
      <td>Ghost</td>
      <td>600</td>
      <td>80</td>
      <td>110</td>
      <td>60</td>
      <td>150</td>
      <td>130</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
      <td>170</td>
      <td>HoopaHoopa Confined is a Psychic pokemon which...</td>
    </tr>
    <tr>
      <th>798</th>
      <td>720</td>
      <td>HoopaHoopa Unbound</td>
      <td>Psychic</td>
      <td>Dark</td>
      <td>680</td>
      <td>80</td>
      <td>160</td>
      <td>60</td>
      <td>170</td>
      <td>130</td>
      <td>80</td>
      <td>6</td>
      <td>True</td>
      <td>220</td>
      <td>HoopaHoopa Unbound is a Psychic pokemon which ...</td>
    </tr>
    <tr>
      <th>799</th>
      <td>721</td>
      <td>Volcanion</td>
      <td>Fire</td>
      <td>Water</td>
      <td>600</td>
      <td>80</td>
      <td>110</td>
      <td>120</td>
      <td>130</td>
      <td>90</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
      <td>230</td>
      <td>Volcanion is a Fire pokemon which is not Legen...</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 15 columns</p>
</div>




```python
type(df['Legendary'][0])
```




    numpy.bool_




```python
# Remove a column
# Remove df['AttDef']
df.drop(columns=['AttDef', 'Total'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
      <td>Bulbasaur is a Grass pokemon which is not Lege...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
      <td>Ivysaur is a Grass pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>82</td>
      <td>83</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>Venusaur is a Grass pokemon which is not Legen...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>100</td>
      <td>123</td>
      <td>122</td>
      <td>120</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>VenusaurMega Venusaur is a Grass pokemon which...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Charmander</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>39</td>
      <td>52</td>
      <td>43</td>
      <td>60</td>
      <td>50</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
      <td>Charmander is a Fire pokemon which is not Lege...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>795</th>
      <td>719</td>
      <td>Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>50</td>
      <td>100</td>
      <td>150</td>
      <td>100</td>
      <td>150</td>
      <td>50</td>
      <td>6</td>
      <td>True</td>
      <td>Diancie is a Rock pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>796</th>
      <td>719</td>
      <td>DiancieMega Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>50</td>
      <td>160</td>
      <td>110</td>
      <td>160</td>
      <td>110</td>
      <td>110</td>
      <td>6</td>
      <td>True</td>
      <td>DiancieMega Diancie is a Rock pokemon which is...</td>
    </tr>
    <tr>
      <th>797</th>
      <td>720</td>
      <td>HoopaHoopa Confined</td>
      <td>Psychic</td>
      <td>Ghost</td>
      <td>80</td>
      <td>110</td>
      <td>60</td>
      <td>150</td>
      <td>130</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
      <td>HoopaHoopa Confined is a Psychic pokemon which...</td>
    </tr>
    <tr>
      <th>798</th>
      <td>720</td>
      <td>HoopaHoopa Unbound</td>
      <td>Psychic</td>
      <td>Dark</td>
      <td>80</td>
      <td>160</td>
      <td>60</td>
      <td>170</td>
      <td>130</td>
      <td>80</td>
      <td>6</td>
      <td>True</td>
      <td>HoopaHoopa Unbound is a Psychic pokemon which ...</td>
    </tr>
    <tr>
      <th>799</th>
      <td>721</td>
      <td>Volcanion</td>
      <td>Fire</td>
      <td>Water</td>
      <td>80</td>
      <td>110</td>
      <td>120</td>
      <td>130</td>
      <td>90</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
      <td>Volcanion is a Fire pokemon which is not Legen...</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 13 columns</p>
</div>




```python
# Using aggregarions - 
# Create the total column with sum of columns from 4 to 9 inclusive
# This method is not preferred because it might insert column in between and then we will get incorrect data next time
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>481</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
      <td>98</td>
      <td>Bulbasaur is a Grass pokemon which is not Lege...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>610</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
      <td>125</td>
      <td>Ivysaur is a Grass pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>790</td>
      <td>80</td>
      <td>82</td>
      <td>83</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>165</td>
      <td>Venusaur is a Grass pokemon which is not Legen...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>970</td>
      <td>80</td>
      <td>100</td>
      <td>123</td>
      <td>122</td>
      <td>120</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>223</td>
      <td>VenusaurMega Venusaur is a Grass pokemon which...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Charmander</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>438</td>
      <td>39</td>
      <td>52</td>
      <td>43</td>
      <td>60</td>
      <td>50</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
      <td>95</td>
      <td>Charmander is a Fire pokemon which is not Lege...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>795</th>
      <td>719</td>
      <td>Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>950</td>
      <td>50</td>
      <td>100</td>
      <td>150</td>
      <td>100</td>
      <td>150</td>
      <td>50</td>
      <td>6</td>
      <td>True</td>
      <td>250</td>
      <td>Diancie is a Rock pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>796</th>
      <td>719</td>
      <td>DiancieMega Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>1070</td>
      <td>50</td>
      <td>160</td>
      <td>110</td>
      <td>160</td>
      <td>110</td>
      <td>110</td>
      <td>6</td>
      <td>True</td>
      <td>270</td>
      <td>DiancieMega Diancie is a Rock pokemon which is...</td>
    </tr>
    <tr>
      <th>797</th>
      <td>720</td>
      <td>HoopaHoopa Confined</td>
      <td>Psychic</td>
      <td>Ghost</td>
      <td>930</td>
      <td>80</td>
      <td>110</td>
      <td>60</td>
      <td>150</td>
      <td>130</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
      <td>170</td>
      <td>HoopaHoopa Confined is a Psychic pokemon which...</td>
    </tr>
    <tr>
      <th>798</th>
      <td>720</td>
      <td>HoopaHoopa Unbound</td>
      <td>Psychic</td>
      <td>Dark</td>
      <td>1070</td>
      <td>80</td>
      <td>160</td>
      <td>60</td>
      <td>170</td>
      <td>130</td>
      <td>80</td>
      <td>6</td>
      <td>True</td>
      <td>220</td>
      <td>HoopaHoopa Unbound is a Psychic pokemon which ...</td>
    </tr>
    <tr>
      <th>799</th>
      <td>721</td>
      <td>Volcanion</td>
      <td>Fire</td>
      <td>Water</td>
      <td>970</td>
      <td>80</td>
      <td>110</td>
      <td>120</td>
      <td>130</td>
      <td>90</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
      <td>230</td>
      <td>Volcanion is a Fire pokemon which is not Legen...</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 15 columns</p>
</div>




```python
# Getting all column names in a list
df.columns.values
```




    array(['#', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack',
           'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation',
           'Legendary', 'AttDef', 'Summary'], dtype=object)




```python
%pip install openpyxl
```

    Defaulting to user installation because normal site-packages is not writeableNote: you may need to restart the kernel to use updated packages.
    
    Collecting openpyxl
      Downloading openpyxl-3.1.2-py2.py3-none-any.whl (249 kB)
         ---------------------------------------- 0.0/250.0 kB ? eta -:--:--
         --------------------- ---------------- 143.4/250.0 kB 4.3 MB/s eta 0:00:01
         --------------------- ---------------- 143.4/250.0 kB 4.3 MB/s eta 0:00:01
         ----------------------- -------------- 153.6/250.0 kB 1.3 MB/s eta 0:00:01
         ------------------------------- ------ 204.8/250.0 kB 1.1 MB/s eta 0:00:01
         -------------------------------------  245.8/250.0 kB 1.3 MB/s eta 0:00:01
         -------------------------------------- 250.0/250.0 kB 1.0 MB/s eta 0:00:00
    Collecting et-xmlfile (from openpyxl)
      Downloading et_xmlfile-1.1.0-py3-none-any.whl (4.7 kB)
    Installing collected packages: et-xmlfile, openpyxl
    Successfully installed et-xmlfile-1.1.0 openpyxl-3.1.2
    

    
    [notice] A new release of pip is available: 23.2.1 -> 23.3.2
    [notice] To update, run: python.exe -m pip install --upgrade pip
    


```python
# Saving the dataframe to a file
df.to_csv('new_data.csv', index=False)   # index=False to ignore the extra rownumber column
df.to_excel('new_data.xlsx')
```


```python
# Advanced Filtering Data
# Find all the Electric Pokemons
df.loc[df['Type 1'] == 'Electric']

# Find all Grass Type and Fighting pokemons
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Fighting')]    # Note that we need to add proper paranthesis
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>310</th>
      <td>286</td>
      <td>Breloom</td>
      <td>Grass</td>
      <td>Fighting</td>
      <td>720</td>
      <td>60</td>
      <td>130</td>
      <td>80</td>
      <td>60</td>
      <td>60</td>
      <td>70</td>
      <td>3</td>
      <td>False</td>
      <td>210</td>
      <td>Breloom is a Grass pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>701</th>
      <td>640</td>
      <td>Virizion</td>
      <td>Grass</td>
      <td>Fighting</td>
      <td>815</td>
      <td>91</td>
      <td>90</td>
      <td>72</td>
      <td>90</td>
      <td>129</td>
      <td>108</td>
      <td>5</td>
      <td>True</td>
      <td>162</td>
      <td>Virizion is a Grass pokemon which is not Legen...</td>
    </tr>
    <tr>
      <th>720</th>
      <td>652</td>
      <td>Chesnaught</td>
      <td>Grass</td>
      <td>Fighting</td>
      <td>857</td>
      <td>88</td>
      <td>107</td>
      <td>122</td>
      <td>74</td>
      <td>75</td>
      <td>64</td>
      <td>6</td>
      <td>False</td>
      <td>229</td>
      <td>Chesnaught is a Grass pokemon which is not Leg...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Find all Fire type pokemons with HP > 100
df.loc[(df['Type 1'] == 'Fire') & (df['HP'] > 100)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>263</th>
      <td>244</td>
      <td>Entei</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>885</td>
      <td>115</td>
      <td>115</td>
      <td>85</td>
      <td>90</td>
      <td>75</td>
      <td>100</td>
      <td>2</td>
      <td>True</td>
      <td>200</td>
      <td>Entei is a Fire pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>270</th>
      <td>250</td>
      <td>Ho-oh</td>
      <td>Fire</td>
      <td>Flying</td>
      <td>1026</td>
      <td>106</td>
      <td>130</td>
      <td>90</td>
      <td>110</td>
      <td>154</td>
      <td>90</td>
      <td>2</td>
      <td>True</td>
      <td>220</td>
      <td>Ho-oh is a Fire pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>559</th>
      <td>500</td>
      <td>Emboar</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>861</td>
      <td>110</td>
      <td>123</td>
      <td>65</td>
      <td>100</td>
      <td>65</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
      <td>188</td>
      <td>Emboar is a Fire pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>615</th>
      <td>555</td>
      <td>DarmanitanStandard Mode</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>715</td>
      <td>105</td>
      <td>140</td>
      <td>55</td>
      <td>30</td>
      <td>55</td>
      <td>95</td>
      <td>5</td>
      <td>False</td>
      <td>195</td>
      <td>DarmanitanStandard Mode is a Fire pokemon whic...</td>
    </tr>
    <tr>
      <th>616</th>
      <td>555</td>
      <td>DarmanitanZen Mode</td>
      <td>Fire</td>
      <td>Psychic</td>
      <td>865</td>
      <td>105</td>
      <td>30</td>
      <td>105</td>
      <td>140</td>
      <td>105</td>
      <td>55</td>
      <td>5</td>
      <td>False</td>
      <td>135</td>
      <td>DarmanitanZen Mode is a Fire pokemon which is ...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# In above example, notice how the index is still the same. We can reset it
new_df = df.loc[(df['Type 1'] == 'Fire') & (df['HP'] > 100)]
new_df.reset_index(drop=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>244</td>
      <td>Entei</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>885</td>
      <td>115</td>
      <td>115</td>
      <td>85</td>
      <td>90</td>
      <td>75</td>
      <td>100</td>
      <td>2</td>
      <td>True</td>
      <td>200</td>
      <td>Entei is a Fire pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>1</th>
      <td>250</td>
      <td>Ho-oh</td>
      <td>Fire</td>
      <td>Flying</td>
      <td>1026</td>
      <td>106</td>
      <td>130</td>
      <td>90</td>
      <td>110</td>
      <td>154</td>
      <td>90</td>
      <td>2</td>
      <td>True</td>
      <td>220</td>
      <td>Ho-oh is a Fire pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>2</th>
      <td>500</td>
      <td>Emboar</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>861</td>
      <td>110</td>
      <td>123</td>
      <td>65</td>
      <td>100</td>
      <td>65</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
      <td>188</td>
      <td>Emboar is a Fire pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>3</th>
      <td>555</td>
      <td>DarmanitanStandard Mode</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>715</td>
      <td>105</td>
      <td>140</td>
      <td>55</td>
      <td>30</td>
      <td>55</td>
      <td>95</td>
      <td>5</td>
      <td>False</td>
      <td>195</td>
      <td>DarmanitanStandard Mode is a Fire pokemon whic...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>555</td>
      <td>DarmanitanZen Mode</td>
      <td>Fire</td>
      <td>Psychic</td>
      <td>865</td>
      <td>105</td>
      <td>30</td>
      <td>105</td>
      <td>140</td>
      <td>105</td>
      <td>55</td>
      <td>5</td>
      <td>False</td>
      <td>135</td>
      <td>DarmanitanZen Mode is a Fire pokemon which is ...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Filter all the Mega Pokemons
df.loc[df['Name'].str.contains('Mega')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>970</td>
      <td>80</td>
      <td>100</td>
      <td>123</td>
      <td>122</td>
      <td>120</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>223</td>
      <td>VenusaurMega Venusaur is a Grass pokemon which...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6</td>
      <td>CharizardMega Charizard X</td>
      <td>Fire</td>
      <td>Dragon</td>
      <td>983</td>
      <td>78</td>
      <td>130</td>
      <td>111</td>
      <td>130</td>
      <td>85</td>
      <td>100</td>
      <td>1</td>
      <td>False</td>
      <td>241</td>
      <td>CharizardMega Charizard X is a Fire pokemon wh...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>6</td>
      <td>CharizardMega Charizard Y</td>
      <td>Fire</td>
      <td>Flying</td>
      <td>953</td>
      <td>78</td>
      <td>104</td>
      <td>78</td>
      <td>159</td>
      <td>115</td>
      <td>100</td>
      <td>1</td>
      <td>False</td>
      <td>182</td>
      <td>CharizardMega Charizard Y is a Fire pokemon wh...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>9</td>
      <td>BlastoiseMega Blastoise</td>
      <td>Water</td>
      <td>NaN</td>
      <td>989</td>
      <td>79</td>
      <td>103</td>
      <td>120</td>
      <td>135</td>
      <td>115</td>
      <td>78</td>
      <td>1</td>
      <td>False</td>
      <td>223</td>
      <td>BlastoiseMega Blastoise is a Water pokemon whi...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>15</td>
      <td>BeedrillMega Beedrill</td>
      <td>Bug</td>
      <td>Poison</td>
      <td>620</td>
      <td>65</td>
      <td>150</td>
      <td>40</td>
      <td>15</td>
      <td>80</td>
      <td>145</td>
      <td>1</td>
      <td>False</td>
      <td>190</td>
      <td>BeedrillMega Beedrill is a Bug pokemon which i...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>18</td>
      <td>PidgeotMega Pidgeot</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>836</td>
      <td>83</td>
      <td>80</td>
      <td>80</td>
      <td>135</td>
      <td>80</td>
      <td>121</td>
      <td>1</td>
      <td>False</td>
      <td>160</td>
      <td>PidgeotMega Pidgeot is a Normal pokemon which ...</td>
    </tr>
    <tr>
      <th>71</th>
      <td>65</td>
      <td>AlakazamMega Alakazam</td>
      <td>Psychic</td>
      <td>NaN</td>
      <td>785</td>
      <td>55</td>
      <td>50</td>
      <td>65</td>
      <td>175</td>
      <td>95</td>
      <td>150</td>
      <td>1</td>
      <td>False</td>
      <td>115</td>
      <td>AlakazamMega Alakazam is a Psychic pokemon whi...</td>
    </tr>
    <tr>
      <th>87</th>
      <td>80</td>
      <td>SlowbroMega Slowbro</td>
      <td>Water</td>
      <td>Psychic</td>
      <td>1040</td>
      <td>95</td>
      <td>75</td>
      <td>180</td>
      <td>130</td>
      <td>80</td>
      <td>30</td>
      <td>1</td>
      <td>False</td>
      <td>255</td>
      <td>SlowbroMega Slowbro is a Water pokemon which i...</td>
    </tr>
    <tr>
      <th>102</th>
      <td>94</td>
      <td>GengarMega Gengar</td>
      <td>Ghost</td>
      <td>Poison</td>
      <td>845</td>
      <td>60</td>
      <td>65</td>
      <td>80</td>
      <td>170</td>
      <td>95</td>
      <td>130</td>
      <td>1</td>
      <td>False</td>
      <td>145</td>
      <td>GengarMega Gengar is a Ghost pokemon which is ...</td>
    </tr>
    <tr>
      <th>124</th>
      <td>115</td>
      <td>KangaskhanMega Kangaskhan</td>
      <td>Normal</td>
      <td>NaN</td>
      <td>880</td>
      <td>105</td>
      <td>125</td>
      <td>100</td>
      <td>60</td>
      <td>100</td>
      <td>100</td>
      <td>1</td>
      <td>False</td>
      <td>225</td>
      <td>KangaskhanMega Kangaskhan is a Normal pokemon ...</td>
    </tr>
    <tr>
      <th>137</th>
      <td>127</td>
      <td>PinsirMega Pinsir</td>
      <td>Bug</td>
      <td>Flying</td>
      <td>900</td>
      <td>65</td>
      <td>155</td>
      <td>120</td>
      <td>65</td>
      <td>90</td>
      <td>105</td>
      <td>1</td>
      <td>False</td>
      <td>275</td>
      <td>PinsirMega Pinsir is a Bug pokemon which is no...</td>
    </tr>
    <tr>
      <th>141</th>
      <td>130</td>
      <td>GyaradosMega Gyarados</td>
      <td>Water</td>
      <td>Dark</td>
      <td>988</td>
      <td>95</td>
      <td>155</td>
      <td>109</td>
      <td>70</td>
      <td>130</td>
      <td>81</td>
      <td>1</td>
      <td>False</td>
      <td>264</td>
      <td>GyaradosMega Gyarados is a Water pokemon which...</td>
    </tr>
    <tr>
      <th>154</th>
      <td>142</td>
      <td>AerodactylMega Aerodactyl</td>
      <td>Rock</td>
      <td>Flying</td>
      <td>835</td>
      <td>80</td>
      <td>135</td>
      <td>85</td>
      <td>70</td>
      <td>95</td>
      <td>150</td>
      <td>1</td>
      <td>False</td>
      <td>220</td>
      <td>AerodactylMega Aerodactyl is a Rock pokemon wh...</td>
    </tr>
    <tr>
      <th>163</th>
      <td>150</td>
      <td>MewtwoMega Mewtwo X</td>
      <td>Psychic</td>
      <td>Fighting</td>
      <td>1200</td>
      <td>106</td>
      <td>190</td>
      <td>100</td>
      <td>154</td>
      <td>100</td>
      <td>130</td>
      <td>1</td>
      <td>True</td>
      <td>290</td>
      <td>MewtwoMega Mewtwo X is a Psychic pokemon which...</td>
    </tr>
    <tr>
      <th>164</th>
      <td>150</td>
      <td>MewtwoMega Mewtwo Y</td>
      <td>Psychic</td>
      <td>NaN</td>
      <td>1160</td>
      <td>106</td>
      <td>150</td>
      <td>70</td>
      <td>194</td>
      <td>120</td>
      <td>140</td>
      <td>1</td>
      <td>True</td>
      <td>220</td>
      <td>MewtwoMega Mewtwo Y is a Psychic pokemon which...</td>
    </tr>
    <tr>
      <th>168</th>
      <td>154</td>
      <td>Meganium</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>790</td>
      <td>80</td>
      <td>82</td>
      <td>100</td>
      <td>83</td>
      <td>100</td>
      <td>80</td>
      <td>2</td>
      <td>False</td>
      <td>182</td>
      <td>Meganium is a Grass pokemon which is not Legen...</td>
    </tr>
    <tr>
      <th>196</th>
      <td>181</td>
      <td>AmpharosMega Ampharos</td>
      <td>Electric</td>
      <td>Dragon</td>
      <td>1020</td>
      <td>90</td>
      <td>95</td>
      <td>105</td>
      <td>165</td>
      <td>110</td>
      <td>45</td>
      <td>2</td>
      <td>False</td>
      <td>200</td>
      <td>AmpharosMega Ampharos is a Electric pokemon wh...</td>
    </tr>
    <tr>
      <th>224</th>
      <td>208</td>
      <td>SteelixMega Steelix</td>
      <td>Steel</td>
      <td>Ground</td>
      <td>1065</td>
      <td>75</td>
      <td>125</td>
      <td>230</td>
      <td>55</td>
      <td>95</td>
      <td>30</td>
      <td>2</td>
      <td>False</td>
      <td>355</td>
      <td>SteelixMega Steelix is a Steel pokemon which i...</td>
    </tr>
    <tr>
      <th>229</th>
      <td>212</td>
      <td>ScizorMega Scizor</td>
      <td>Bug</td>
      <td>Steel</td>
      <td>950</td>
      <td>70</td>
      <td>150</td>
      <td>140</td>
      <td>65</td>
      <td>100</td>
      <td>75</td>
      <td>2</td>
      <td>False</td>
      <td>290</td>
      <td>ScizorMega Scizor is a Bug pokemon which is no...</td>
    </tr>
    <tr>
      <th>232</th>
      <td>214</td>
      <td>HeracrossMega Heracross</td>
      <td>Bug</td>
      <td>Fighting</td>
      <td>945</td>
      <td>80</td>
      <td>185</td>
      <td>115</td>
      <td>40</td>
      <td>105</td>
      <td>75</td>
      <td>2</td>
      <td>False</td>
      <td>300</td>
      <td>HeracrossMega Heracross is a Bug pokemon which...</td>
    </tr>
    <tr>
      <th>248</th>
      <td>229</td>
      <td>HoundoomMega Houndoom</td>
      <td>Dark</td>
      <td>Fire</td>
      <td>880</td>
      <td>75</td>
      <td>90</td>
      <td>90</td>
      <td>140</td>
      <td>90</td>
      <td>115</td>
      <td>2</td>
      <td>False</td>
      <td>180</td>
      <td>HoundoomMega Houndoom is a Dark pokemon which ...</td>
    </tr>
    <tr>
      <th>268</th>
      <td>248</td>
      <td>TyranitarMega Tyranitar</td>
      <td>Rock</td>
      <td>Dark</td>
      <td>1138</td>
      <td>100</td>
      <td>164</td>
      <td>150</td>
      <td>95</td>
      <td>120</td>
      <td>71</td>
      <td>2</td>
      <td>False</td>
      <td>314</td>
      <td>TyranitarMega Tyranitar is a Rock pokemon whic...</td>
    </tr>
    <tr>
      <th>275</th>
      <td>254</td>
      <td>SceptileMega Sceptile</td>
      <td>Grass</td>
      <td>Dragon</td>
      <td>885</td>
      <td>70</td>
      <td>110</td>
      <td>75</td>
      <td>145</td>
      <td>85</td>
      <td>145</td>
      <td>3</td>
      <td>False</td>
      <td>185</td>
      <td>SceptileMega Sceptile is a Grass pokemon which...</td>
    </tr>
    <tr>
      <th>279</th>
      <td>257</td>
      <td>BlazikenMega Blaziken</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>980</td>
      <td>80</td>
      <td>160</td>
      <td>80</td>
      <td>130</td>
      <td>80</td>
      <td>100</td>
      <td>3</td>
      <td>False</td>
      <td>240</td>
      <td>BlazikenMega Blaziken is a Fire pokemon which ...</td>
    </tr>
    <tr>
      <th>283</th>
      <td>260</td>
      <td>SwampertMega Swampert</td>
      <td>Water</td>
      <td>Ground</td>
      <td>1020</td>
      <td>100</td>
      <td>150</td>
      <td>110</td>
      <td>95</td>
      <td>110</td>
      <td>70</td>
      <td>3</td>
      <td>False</td>
      <td>260</td>
      <td>SwampertMega Swampert is a Water pokemon which...</td>
    </tr>
    <tr>
      <th>306</th>
      <td>282</td>
      <td>GardevoirMega Gardevoir</td>
      <td>Psychic</td>
      <td>Fairy</td>
      <td>901</td>
      <td>68</td>
      <td>85</td>
      <td>65</td>
      <td>165</td>
      <td>135</td>
      <td>100</td>
      <td>3</td>
      <td>False</td>
      <td>150</td>
      <td>GardevoirMega Gardevoir is a Psychic pokemon w...</td>
    </tr>
    <tr>
      <th>327</th>
      <td>302</td>
      <td>SableyeMega Sableye</td>
      <td>Dark</td>
      <td>Ghost</td>
      <td>805</td>
      <td>50</td>
      <td>85</td>
      <td>125</td>
      <td>85</td>
      <td>115</td>
      <td>20</td>
      <td>3</td>
      <td>False</td>
      <td>210</td>
      <td>SableyeMega Sableye is a Dark pokemon which is...</td>
    </tr>
    <tr>
      <th>329</th>
      <td>303</td>
      <td>MawileMega Mawile</td>
      <td>Steel</td>
      <td>Fairy</td>
      <td>765</td>
      <td>50</td>
      <td>105</td>
      <td>125</td>
      <td>55</td>
      <td>95</td>
      <td>50</td>
      <td>3</td>
      <td>False</td>
      <td>230</td>
      <td>MawileMega Mawile is a Steel pokemon which is ...</td>
    </tr>
    <tr>
      <th>333</th>
      <td>306</td>
      <td>AggronMega Aggron</td>
      <td>Steel</td>
      <td>NaN</td>
      <td>1080</td>
      <td>70</td>
      <td>140</td>
      <td>230</td>
      <td>60</td>
      <td>80</td>
      <td>50</td>
      <td>3</td>
      <td>False</td>
      <td>370</td>
      <td>AggronMega Aggron is a Steel pokemon which is ...</td>
    </tr>
    <tr>
      <th>336</th>
      <td>308</td>
      <td>MedichamMega Medicham</td>
      <td>Fighting</td>
      <td>Psychic</td>
      <td>735</td>
      <td>60</td>
      <td>100</td>
      <td>85</td>
      <td>80</td>
      <td>85</td>
      <td>100</td>
      <td>3</td>
      <td>False</td>
      <td>185</td>
      <td>MedichamMega Medicham is a Fighting pokemon wh...</td>
    </tr>
    <tr>
      <th>339</th>
      <td>310</td>
      <td>ManectricMega Manectric</td>
      <td>Electric</td>
      <td>NaN</td>
      <td>800</td>
      <td>70</td>
      <td>75</td>
      <td>80</td>
      <td>135</td>
      <td>80</td>
      <td>135</td>
      <td>3</td>
      <td>False</td>
      <td>155</td>
      <td>ManectricMega Manectric is a Electric pokemon ...</td>
    </tr>
    <tr>
      <th>349</th>
      <td>319</td>
      <td>SharpedoMega Sharpedo</td>
      <td>Water</td>
      <td>Dark</td>
      <td>845</td>
      <td>70</td>
      <td>140</td>
      <td>70</td>
      <td>110</td>
      <td>65</td>
      <td>105</td>
      <td>3</td>
      <td>False</td>
      <td>210</td>
      <td>SharpedoMega Sharpedo is a Water pokemon which...</td>
    </tr>
    <tr>
      <th>354</th>
      <td>323</td>
      <td>CameruptMega Camerupt</td>
      <td>Fire</td>
      <td>Ground</td>
      <td>975</td>
      <td>70</td>
      <td>120</td>
      <td>100</td>
      <td>145</td>
      <td>105</td>
      <td>20</td>
      <td>3</td>
      <td>False</td>
      <td>220</td>
      <td>CameruptMega Camerupt is a Fire pokemon which ...</td>
    </tr>
    <tr>
      <th>366</th>
      <td>334</td>
      <td>AltariaMega Altaria</td>
      <td>Dragon</td>
      <td>Fairy</td>
      <td>915</td>
      <td>75</td>
      <td>110</td>
      <td>110</td>
      <td>110</td>
      <td>105</td>
      <td>80</td>
      <td>3</td>
      <td>False</td>
      <td>220</td>
      <td>AltariaMega Altaria is a Dragon pokemon which ...</td>
    </tr>
    <tr>
      <th>387</th>
      <td>354</td>
      <td>BanetteMega Banette</td>
      <td>Ghost</td>
      <td>NaN</td>
      <td>877</td>
      <td>64</td>
      <td>165</td>
      <td>75</td>
      <td>93</td>
      <td>83</td>
      <td>75</td>
      <td>3</td>
      <td>False</td>
      <td>240</td>
      <td>BanetteMega Banette is a Ghost pokemon which i...</td>
    </tr>
    <tr>
      <th>393</th>
      <td>359</td>
      <td>AbsolMega Absol</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>840</td>
      <td>65</td>
      <td>150</td>
      <td>60</td>
      <td>115</td>
      <td>60</td>
      <td>115</td>
      <td>3</td>
      <td>False</td>
      <td>210</td>
      <td>AbsolMega Absol is a Dark pokemon which is not...</td>
    </tr>
    <tr>
      <th>397</th>
      <td>362</td>
      <td>GlalieMega Glalie</td>
      <td>Ice</td>
      <td>NaN</td>
      <td>880</td>
      <td>80</td>
      <td>120</td>
      <td>80</td>
      <td>120</td>
      <td>80</td>
      <td>100</td>
      <td>3</td>
      <td>False</td>
      <td>200</td>
      <td>GlalieMega Glalie is a Ice pokemon which is no...</td>
    </tr>
    <tr>
      <th>409</th>
      <td>373</td>
      <td>SalamenceMega Salamence</td>
      <td>Dragon</td>
      <td>Flying</td>
      <td>1070</td>
      <td>95</td>
      <td>145</td>
      <td>130</td>
      <td>120</td>
      <td>90</td>
      <td>120</td>
      <td>3</td>
      <td>False</td>
      <td>275</td>
      <td>SalamenceMega Salamence is a Dragon pokemon wh...</td>
    </tr>
    <tr>
      <th>413</th>
      <td>376</td>
      <td>MetagrossMega Metagross</td>
      <td>Steel</td>
      <td>Psychic</td>
      <td>1070</td>
      <td>80</td>
      <td>145</td>
      <td>150</td>
      <td>105</td>
      <td>110</td>
      <td>110</td>
      <td>3</td>
      <td>False</td>
      <td>295</td>
      <td>MetagrossMega Metagross is a Steel pokemon whi...</td>
    </tr>
    <tr>
      <th>418</th>
      <td>380</td>
      <td>LatiasMega Latias</td>
      <td>Dragon</td>
      <td>Psychic</td>
      <td>1030</td>
      <td>80</td>
      <td>100</td>
      <td>120</td>
      <td>140</td>
      <td>150</td>
      <td>110</td>
      <td>3</td>
      <td>True</td>
      <td>220</td>
      <td>LatiasMega Latias is a Dragon pokemon which is...</td>
    </tr>
    <tr>
      <th>420</th>
      <td>381</td>
      <td>LatiosMega Latios</td>
      <td>Dragon</td>
      <td>Psychic</td>
      <td>1060</td>
      <td>80</td>
      <td>130</td>
      <td>100</td>
      <td>160</td>
      <td>120</td>
      <td>110</td>
      <td>3</td>
      <td>True</td>
      <td>230</td>
      <td>LatiosMega Latios is a Dragon pokemon which is...</td>
    </tr>
    <tr>
      <th>426</th>
      <td>384</td>
      <td>RayquazaMega Rayquaza</td>
      <td>Dragon</td>
      <td>Flying</td>
      <td>1230</td>
      <td>105</td>
      <td>180</td>
      <td>100</td>
      <td>180</td>
      <td>100</td>
      <td>115</td>
      <td>3</td>
      <td>True</td>
      <td>280</td>
      <td>RayquazaMega Rayquaza is a Dragon pokemon whic...</td>
    </tr>
    <tr>
      <th>476</th>
      <td>428</td>
      <td>LopunnyMega Lopunny</td>
      <td>Normal</td>
      <td>Fighting</td>
      <td>794</td>
      <td>65</td>
      <td>136</td>
      <td>94</td>
      <td>54</td>
      <td>96</td>
      <td>135</td>
      <td>4</td>
      <td>False</td>
      <td>230</td>
      <td>LopunnyMega Lopunny is a Normal pokemon which ...</td>
    </tr>
    <tr>
      <th>494</th>
      <td>445</td>
      <td>GarchompMega Garchomp</td>
      <td>Dragon</td>
      <td>Ground</td>
      <td>1121</td>
      <td>108</td>
      <td>170</td>
      <td>115</td>
      <td>120</td>
      <td>95</td>
      <td>92</td>
      <td>4</td>
      <td>False</td>
      <td>285</td>
      <td>GarchompMega Garchomp is a Dragon pokemon whic...</td>
    </tr>
    <tr>
      <th>498</th>
      <td>448</td>
      <td>LucarioMega Lucario</td>
      <td>Fighting</td>
      <td>Steel</td>
      <td>956</td>
      <td>70</td>
      <td>145</td>
      <td>88</td>
      <td>140</td>
      <td>70</td>
      <td>112</td>
      <td>4</td>
      <td>False</td>
      <td>233</td>
      <td>LucarioMega Lucario is a Fighting pokemon whic...</td>
    </tr>
    <tr>
      <th>511</th>
      <td>460</td>
      <td>AbomasnowMega Abomasnow</td>
      <td>Grass</td>
      <td>Ice</td>
      <td>1023</td>
      <td>90</td>
      <td>132</td>
      <td>105</td>
      <td>132</td>
      <td>105</td>
      <td>30</td>
      <td>4</td>
      <td>False</td>
      <td>237</td>
      <td>AbomasnowMega Abomasnow is a Grass pokemon whi...</td>
    </tr>
    <tr>
      <th>527</th>
      <td>475</td>
      <td>GalladeMega Gallade</td>
      <td>Psychic</td>
      <td>Fighting</td>
      <td>901</td>
      <td>68</td>
      <td>165</td>
      <td>95</td>
      <td>65</td>
      <td>115</td>
      <td>110</td>
      <td>4</td>
      <td>False</td>
      <td>260</td>
      <td>GalladeMega Gallade is a Psychic pokemon which...</td>
    </tr>
    <tr>
      <th>591</th>
      <td>531</td>
      <td>AudinoMega Audino</td>
      <td>Normal</td>
      <td>Fairy</td>
      <td>864</td>
      <td>103</td>
      <td>60</td>
      <td>126</td>
      <td>80</td>
      <td>126</td>
      <td>50</td>
      <td>5</td>
      <td>False</td>
      <td>186</td>
      <td>AudinoMega Audino is a Normal pokemon which is...</td>
    </tr>
    <tr>
      <th>796</th>
      <td>719</td>
      <td>DiancieMega Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>1070</td>
      <td>50</td>
      <td>160</td>
      <td>110</td>
      <td>160</td>
      <td>110</td>
      <td>110</td>
      <td>6</td>
      <td>True</td>
      <td>270</td>
      <td>DiancieMega Diancie is a Rock pokemon which is...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Filter all the non - Mega Pokemons
df.loc[~df['Name'].str.contains('Mega')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>481</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
      <td>98</td>
      <td>Bulbasaur is a Grass pokemon which is not Lege...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>610</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
      <td>125</td>
      <td>Ivysaur is a Grass pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>790</td>
      <td>80</td>
      <td>82</td>
      <td>83</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>165</td>
      <td>Venusaur is a Grass pokemon which is not Legen...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Charmander</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>438</td>
      <td>39</td>
      <td>52</td>
      <td>43</td>
      <td>60</td>
      <td>50</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
      <td>95</td>
      <td>Charmander is a Fire pokemon which is not Lege...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Charmeleon</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>585</td>
      <td>58</td>
      <td>64</td>
      <td>58</td>
      <td>80</td>
      <td>65</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>122</td>
      <td>Charmeleon is a Fire pokemon which is not Lege...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>794</th>
      <td>718</td>
      <td>Zygarde50% Forme</td>
      <td>Dragon</td>
      <td>Ground</td>
      <td>915</td>
      <td>108</td>
      <td>100</td>
      <td>121</td>
      <td>81</td>
      <td>95</td>
      <td>95</td>
      <td>6</td>
      <td>True</td>
      <td>221</td>
      <td>Zygarde50% Forme is a Dragon pokemon which is ...</td>
    </tr>
    <tr>
      <th>795</th>
      <td>719</td>
      <td>Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>950</td>
      <td>50</td>
      <td>100</td>
      <td>150</td>
      <td>100</td>
      <td>150</td>
      <td>50</td>
      <td>6</td>
      <td>True</td>
      <td>250</td>
      <td>Diancie is a Rock pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>797</th>
      <td>720</td>
      <td>HoopaHoopa Confined</td>
      <td>Psychic</td>
      <td>Ghost</td>
      <td>930</td>
      <td>80</td>
      <td>110</td>
      <td>60</td>
      <td>150</td>
      <td>130</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
      <td>170</td>
      <td>HoopaHoopa Confined is a Psychic pokemon which...</td>
    </tr>
    <tr>
      <th>798</th>
      <td>720</td>
      <td>HoopaHoopa Unbound</td>
      <td>Psychic</td>
      <td>Dark</td>
      <td>1070</td>
      <td>80</td>
      <td>160</td>
      <td>60</td>
      <td>170</td>
      <td>130</td>
      <td>80</td>
      <td>6</td>
      <td>True</td>
      <td>220</td>
      <td>HoopaHoopa Unbound is a Psychic pokemon which ...</td>
    </tr>
    <tr>
      <th>799</th>
      <td>721</td>
      <td>Volcanion</td>
      <td>Fire</td>
      <td>Water</td>
      <td>970</td>
      <td>80</td>
      <td>110</td>
      <td>120</td>
      <td>130</td>
      <td>90</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
      <td>230</td>
      <td>Volcanion is a Fire pokemon which is not Legen...</td>
    </tr>
  </tbody>
</table>
<p>751 rows × 15 columns</p>
</div>




```python
# Using regex for filtering data
# Find all pokemons of Type Fire or Grass using regex
import re

df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>481</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
      <td>98</td>
      <td>Bulbasaur is a Grass pokemon which is not Lege...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>610</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
      <td>125</td>
      <td>Ivysaur is a Grass pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>790</td>
      <td>80</td>
      <td>82</td>
      <td>83</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>165</td>
      <td>Venusaur is a Grass pokemon which is not Legen...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>970</td>
      <td>80</td>
      <td>100</td>
      <td>123</td>
      <td>122</td>
      <td>120</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>223</td>
      <td>VenusaurMega Venusaur is a Grass pokemon which...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Charmander</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>438</td>
      <td>39</td>
      <td>52</td>
      <td>43</td>
      <td>60</td>
      <td>50</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
      <td>95</td>
      <td>Charmander is a Fire pokemon which is not Lege...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>735</th>
      <td>667</td>
      <td>Litleo</td>
      <td>Fire</td>
      <td>Normal</td>
      <td>540</td>
      <td>62</td>
      <td>50</td>
      <td>58</td>
      <td>73</td>
      <td>54</td>
      <td>72</td>
      <td>6</td>
      <td>False</td>
      <td>108</td>
      <td>Litleo is a Fire pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>736</th>
      <td>668</td>
      <td>Pyroar</td>
      <td>Fire</td>
      <td>Normal</td>
      <td>736</td>
      <td>86</td>
      <td>68</td>
      <td>72</td>
      <td>109</td>
      <td>66</td>
      <td>106</td>
      <td>6</td>
      <td>False</td>
      <td>140</td>
      <td>Pyroar is a Fire pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>740</th>
      <td>672</td>
      <td>Skiddo</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>539</td>
      <td>66</td>
      <td>65</td>
      <td>48</td>
      <td>62</td>
      <td>57</td>
      <td>52</td>
      <td>6</td>
      <td>False</td>
      <td>113</td>
      <td>Skiddo is a Grass pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>741</th>
      <td>673</td>
      <td>Gogoat</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>845</td>
      <td>123</td>
      <td>100</td>
      <td>62</td>
      <td>97</td>
      <td>81</td>
      <td>68</td>
      <td>6</td>
      <td>False</td>
      <td>162</td>
      <td>Gogoat is a Grass pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>799</th>
      <td>721</td>
      <td>Volcanion</td>
      <td>Fire</td>
      <td>Water</td>
      <td>970</td>
      <td>80</td>
      <td>110</td>
      <td>120</td>
      <td>130</td>
      <td>90</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
      <td>230</td>
      <td>Volcanion is a Fire pokemon which is not Legen...</td>
    </tr>
  </tbody>
</table>
<p>122 rows × 15 columns</p>
</div>




```python
# Find all pokemons where name starts with Pi, case insensitive
df.loc[df['Name'].str.contains('^Pi[a-z]', flags=re.I, regex=True)]

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20</th>
      <td>16</td>
      <td>Pidgey</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>355</td>
      <td>40</td>
      <td>45</td>
      <td>40</td>
      <td>35</td>
      <td>35</td>
      <td>56</td>
      <td>1</td>
      <td>False</td>
      <td>85</td>
      <td>Pidgey is a Normal pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>21</th>
      <td>17</td>
      <td>Pidgeotto</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>506</td>
      <td>63</td>
      <td>60</td>
      <td>55</td>
      <td>50</td>
      <td>50</td>
      <td>71</td>
      <td>1</td>
      <td>False</td>
      <td>115</td>
      <td>Pidgeotto is a Normal pokemon which is not Leg...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>18</td>
      <td>Pidgeot</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>686</td>
      <td>83</td>
      <td>80</td>
      <td>75</td>
      <td>70</td>
      <td>70</td>
      <td>101</td>
      <td>1</td>
      <td>False</td>
      <td>155</td>
      <td>Pidgeot is a Normal pokemon which is not Legen...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>18</td>
      <td>PidgeotMega Pidgeot</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>836</td>
      <td>83</td>
      <td>80</td>
      <td>80</td>
      <td>135</td>
      <td>80</td>
      <td>121</td>
      <td>1</td>
      <td>False</td>
      <td>160</td>
      <td>PidgeotMega Pidgeot is a Normal pokemon which ...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>25</td>
      <td>Pikachu</td>
      <td>Electric</td>
      <td>NaN</td>
      <td>410</td>
      <td>35</td>
      <td>55</td>
      <td>40</td>
      <td>50</td>
      <td>50</td>
      <td>90</td>
      <td>1</td>
      <td>False</td>
      <td>95</td>
      <td>Pikachu is a Electric pokemon which is not Leg...</td>
    </tr>
    <tr>
      <th>136</th>
      <td>127</td>
      <td>Pinsir</td>
      <td>Bug</td>
      <td>NaN</td>
      <td>760</td>
      <td>65</td>
      <td>125</td>
      <td>100</td>
      <td>55</td>
      <td>70</td>
      <td>85</td>
      <td>1</td>
      <td>False</td>
      <td>225</td>
      <td>Pinsir is a Bug pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>137</th>
      <td>127</td>
      <td>PinsirMega Pinsir</td>
      <td>Bug</td>
      <td>Flying</td>
      <td>900</td>
      <td>65</td>
      <td>155</td>
      <td>120</td>
      <td>65</td>
      <td>90</td>
      <td>105</td>
      <td>1</td>
      <td>False</td>
      <td>275</td>
      <td>PinsirMega Pinsir is a Bug pokemon which is no...</td>
    </tr>
    <tr>
      <th>186</th>
      <td>172</td>
      <td>Pichu</td>
      <td>Electric</td>
      <td>NaN</td>
      <td>255</td>
      <td>20</td>
      <td>40</td>
      <td>15</td>
      <td>35</td>
      <td>35</td>
      <td>60</td>
      <td>2</td>
      <td>False</td>
      <td>55</td>
      <td>Pichu is a Electric pokemon which is not Legen...</td>
    </tr>
    <tr>
      <th>219</th>
      <td>204</td>
      <td>Pineco</td>
      <td>Bug</td>
      <td>NaN</td>
      <td>515</td>
      <td>50</td>
      <td>65</td>
      <td>90</td>
      <td>35</td>
      <td>35</td>
      <td>15</td>
      <td>2</td>
      <td>False</td>
      <td>155</td>
      <td>Pineco is a Bug pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>239</th>
      <td>221</td>
      <td>Piloswine</td>
      <td>Ice</td>
      <td>Ground</td>
      <td>740</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>60</td>
      <td>60</td>
      <td>50</td>
      <td>2</td>
      <td>False</td>
      <td>180</td>
      <td>Piloswine is a Ice pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>438</th>
      <td>393</td>
      <td>Piplup</td>
      <td>Water</td>
      <td>NaN</td>
      <td>492</td>
      <td>53</td>
      <td>51</td>
      <td>53</td>
      <td>61</td>
      <td>56</td>
      <td>40</td>
      <td>4</td>
      <td>False</td>
      <td>104</td>
      <td>Piplup is a Water pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>558</th>
      <td>499</td>
      <td>Pignite</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>671</td>
      <td>90</td>
      <td>93</td>
      <td>55</td>
      <td>70</td>
      <td>55</td>
      <td>55</td>
      <td>5</td>
      <td>False</td>
      <td>148</td>
      <td>Pignite is a Fire pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>578</th>
      <td>519</td>
      <td>Pidove</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>412</td>
      <td>50</td>
      <td>55</td>
      <td>50</td>
      <td>36</td>
      <td>30</td>
      <td>43</td>
      <td>5</td>
      <td>False</td>
      <td>105</td>
      <td>Pidove is a Normal pokemon which is not Legendary</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Updating the dataframe
# Change the Type 1 to Flame wherever it is Fire
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flame'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[120], line 6
          3 df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flame'
          5 # Change the Type 2 to Dragon wherever it is NaN
    ----> 6 df.loc[~df['Type 2'].bool]
    

    TypeError: bad operand type for unary ~: 'method'



```python
df.sort_values('HP', ascending=False).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>261</th>
      <td>242</td>
      <td>Blissey</td>
      <td>Normal</td>
      <td>NaN</td>
      <td>835</td>
      <td>255</td>
      <td>10</td>
      <td>10</td>
      <td>75</td>
      <td>135</td>
      <td>55</td>
      <td>2</td>
      <td>False</td>
      <td>20</td>
      <td>Blissey is a Normal pokemon which is not Legen...</td>
    </tr>
    <tr>
      <th>121</th>
      <td>113</td>
      <td>Chansey</td>
      <td>Normal</td>
      <td>NaN</td>
      <td>695</td>
      <td>250</td>
      <td>5</td>
      <td>5</td>
      <td>35</td>
      <td>105</td>
      <td>50</td>
      <td>1</td>
      <td>False</td>
      <td>10</td>
      <td>Chansey is a Normal pokemon which is not Legen...</td>
    </tr>
    <tr>
      <th>217</th>
      <td>202</td>
      <td>Wobbuffet</td>
      <td>Psychic</td>
      <td>NaN</td>
      <td>686</td>
      <td>190</td>
      <td>33</td>
      <td>58</td>
      <td>33</td>
      <td>58</td>
      <td>33</td>
      <td>2</td>
      <td>False</td>
      <td>91</td>
      <td>Wobbuffet is a Psychic pokemon which is not Le...</td>
    </tr>
    <tr>
      <th>351</th>
      <td>321</td>
      <td>Wailord</td>
      <td>Water</td>
      <td>NaN</td>
      <td>835</td>
      <td>170</td>
      <td>90</td>
      <td>45</td>
      <td>90</td>
      <td>45</td>
      <td>60</td>
      <td>3</td>
      <td>False</td>
      <td>135</td>
      <td>Wailord is a Water pokemon which is not Legendary</td>
    </tr>
    <tr>
      <th>655</th>
      <td>594</td>
      <td>Alomomola</td>
      <td>Water</td>
      <td>NaN</td>
      <td>765</td>
      <td>165</td>
      <td>75</td>
      <td>80</td>
      <td>40</td>
      <td>45</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
      <td>155</td>
      <td>Alomomola is a Water pokemon which is not Lege...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Aggregation
# Get mean of all attributes group by Type 1
df.groupby(['Type 1'])[['HP', 'Attack', 'Defense', 'Speed']].mean().sort_values('Speed', ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Speed</th>
    </tr>
    <tr>
      <th>Type 1</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Flying</th>
      <td>70.750000</td>
      <td>78.750000</td>
      <td>66.250000</td>
      <td>102.500000</td>
    </tr>
    <tr>
      <th>Electric</th>
      <td>59.795455</td>
      <td>69.090909</td>
      <td>66.295455</td>
      <td>84.500000</td>
    </tr>
    <tr>
      <th>Dragon</th>
      <td>83.312500</td>
      <td>112.125000</td>
      <td>86.375000</td>
      <td>83.031250</td>
    </tr>
    <tr>
      <th>Psychic</th>
      <td>70.631579</td>
      <td>71.456140</td>
      <td>67.684211</td>
      <td>81.491228</td>
    </tr>
    <tr>
      <th>Dark</th>
      <td>66.806452</td>
      <td>88.387097</td>
      <td>70.225806</td>
      <td>76.161290</td>
    </tr>
    <tr>
      <th>Flame</th>
      <td>69.903846</td>
      <td>84.769231</td>
      <td>67.769231</td>
      <td>74.442308</td>
    </tr>
    <tr>
      <th>Normal</th>
      <td>77.275510</td>
      <td>73.469388</td>
      <td>59.846939</td>
      <td>71.551020</td>
    </tr>
    <tr>
      <th>Fighting</th>
      <td>69.851852</td>
      <td>96.777778</td>
      <td>65.925926</td>
      <td>66.074074</td>
    </tr>
    <tr>
      <th>Water</th>
      <td>72.062500</td>
      <td>74.151786</td>
      <td>72.946429</td>
      <td>65.964286</td>
    </tr>
    <tr>
      <th>Ghost</th>
      <td>64.437500</td>
      <td>73.781250</td>
      <td>81.187500</td>
      <td>64.343750</td>
    </tr>
    <tr>
      <th>Ground</th>
      <td>73.781250</td>
      <td>95.750000</td>
      <td>84.843750</td>
      <td>63.906250</td>
    </tr>
    <tr>
      <th>Poison</th>
      <td>67.250000</td>
      <td>74.678571</td>
      <td>68.821429</td>
      <td>63.571429</td>
    </tr>
    <tr>
      <th>Ice</th>
      <td>72.000000</td>
      <td>72.750000</td>
      <td>71.416667</td>
      <td>63.458333</td>
    </tr>
    <tr>
      <th>Grass</th>
      <td>67.271429</td>
      <td>73.214286</td>
      <td>70.800000</td>
      <td>61.928571</td>
    </tr>
    <tr>
      <th>Bug</th>
      <td>56.884058</td>
      <td>70.971014</td>
      <td>70.724638</td>
      <td>61.681159</td>
    </tr>
    <tr>
      <th>Rock</th>
      <td>65.363636</td>
      <td>92.863636</td>
      <td>100.795455</td>
      <td>55.909091</td>
    </tr>
    <tr>
      <th>Steel</th>
      <td>65.222222</td>
      <td>92.703704</td>
      <td>126.370370</td>
      <td>55.259259</td>
    </tr>
    <tr>
      <th>Fairy</th>
      <td>74.117647</td>
      <td>61.529412</td>
      <td>65.705882</td>
      <td>48.588235</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Get count of all attributes group by Type 1
df.groupby(['Type 1']).count().sort_values('Name')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 2</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>AttDef</th>
      <th>Summary</th>
    </tr>
    <tr>
      <th>Type 1</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Flying</th>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Fairy</th>
      <td>17</td>
      <td>17</td>
      <td>2</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
    </tr>
    <tr>
      <th>Ice</th>
      <td>24</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
    </tr>
    <tr>
      <th>Fighting</th>
      <td>27</td>
      <td>27</td>
      <td>7</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
    </tr>
    <tr>
      <th>Steel</th>
      <td>27</td>
      <td>27</td>
      <td>22</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
      <td>27</td>
    </tr>
    <tr>
      <th>Poison</th>
      <td>28</td>
      <td>28</td>
      <td>13</td>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>28</td>
    </tr>
    <tr>
      <th>Dark</th>
      <td>31</td>
      <td>31</td>
      <td>21</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Ghost</th>
      <td>32</td>
      <td>32</td>
      <td>22</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
    </tr>
    <tr>
      <th>Dragon</th>
      <td>32</td>
      <td>32</td>
      <td>21</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
    </tr>
    <tr>
      <th>Ground</th>
      <td>32</td>
      <td>32</td>
      <td>19</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
    </tr>
    <tr>
      <th>Electric</th>
      <td>44</td>
      <td>44</td>
      <td>17</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
    </tr>
    <tr>
      <th>Rock</th>
      <td>44</td>
      <td>44</td>
      <td>35</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44</td>
    </tr>
    <tr>
      <th>Flame</th>
      <td>52</td>
      <td>52</td>
      <td>24</td>
      <td>52</td>
      <td>52</td>
      <td>52</td>
      <td>52</td>
      <td>52</td>
      <td>52</td>
      <td>52</td>
      <td>52</td>
      <td>52</td>
      <td>52</td>
      <td>52</td>
    </tr>
    <tr>
      <th>Psychic</th>
      <td>57</td>
      <td>57</td>
      <td>19</td>
      <td>57</td>
      <td>57</td>
      <td>57</td>
      <td>57</td>
      <td>57</td>
      <td>57</td>
      <td>57</td>
      <td>57</td>
      <td>57</td>
      <td>57</td>
      <td>57</td>
    </tr>
    <tr>
      <th>Bug</th>
      <td>69</td>
      <td>69</td>
      <td>52</td>
      <td>69</td>
      <td>69</td>
      <td>69</td>
      <td>69</td>
      <td>69</td>
      <td>69</td>
      <td>69</td>
      <td>69</td>
      <td>69</td>
      <td>69</td>
      <td>69</td>
    </tr>
    <tr>
      <th>Grass</th>
      <td>70</td>
      <td>70</td>
      <td>37</td>
      <td>70</td>
      <td>70</td>
      <td>70</td>
      <td>70</td>
      <td>70</td>
      <td>70</td>
      <td>70</td>
      <td>70</td>
      <td>70</td>
      <td>70</td>
      <td>70</td>
    </tr>
    <tr>
      <th>Normal</th>
      <td>98</td>
      <td>98</td>
      <td>37</td>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>98</td>
    </tr>
    <tr>
      <th>Water</th>
      <td>112</td>
      <td>112</td>
      <td>53</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Loading Dataframe in chunks
for df_chunk in pd.read_csv('pokemon.csv', chunksize=5):
    print(df_chunk)
```

       #                   Name Type 1  Type 2  Total  HP  Attack  Defense  \
    0  1              Bulbasaur  Grass  Poison    318  45      49       49   
    1  2                Ivysaur  Grass  Poison    405  60      62       63   
    2  3               Venusaur  Grass  Poison    525  80      82       83   
    3  3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123   
    4  4             Charmander   Fire     NaN    309  39      52       43   
    
       Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    0       65       65     45           1      False  
    1       80       80     60           1      False  
    2      100      100     80           1      False  
    3      122      120     80           1      False  
    4       60       50     65           1      False  
       #                       Name Type 1  Type 2  Total  HP  Attack  Defense  \
    5  5                 Charmeleon   Fire     NaN    405  58      64       58   
    6  6                  Charizard   Fire  Flying    534  78      84       78   
    7  6  CharizardMega Charizard X   Fire  Dragon    634  78     130      111   
    8  6  CharizardMega Charizard Y   Fire  Flying    634  78     104       78   
    9  7                   Squirtle  Water     NaN    314  44      48       65   
    
       Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    5       80       65     80           1      False  
    6      109       85    100           1      False  
    7      130       85    100           1      False  
    8      159      115    100           1      False  
    9       50       64     43           1      False  
         #                     Name Type 1  Type 2  Total  HP  Attack  Defense  \
    10   8                Wartortle  Water     NaN    405  59      63       80   
    11   9                Blastoise  Water     NaN    530  79      83      100   
    12   9  BlastoiseMega Blastoise  Water     NaN    630  79     103      120   
    13  10                 Caterpie    Bug     NaN    195  45      30       35   
    14  11                  Metapod    Bug     NaN    205  50      20       55   
    
        Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    10       65       80     58           1      False  
    11       85      105     78           1      False  
    12      135      115     78           1      False  
    13       20       20     45           1      False  
    14       25       25     30           1      False  
         #                   Name Type 1  Type 2  Total  HP  Attack  Defense  \
    15  12             Butterfree    Bug  Flying    395  60      45       50   
    16  13                 Weedle    Bug  Poison    195  40      35       30   
    17  14                 Kakuna    Bug  Poison    205  45      25       50   
    18  15               Beedrill    Bug  Poison    395  65      90       40   
    19  15  BeedrillMega Beedrill    Bug  Poison    495  65     150       40   
    
        Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    15       90       80     70           1      False  
    16       20       20     50           1      False  
    17       25       25     35           1      False  
    18       45       80     75           1      False  
    19       15       80    145           1      False  
         #                 Name  Type 1  Type 2  Total  HP  Attack  Defense  \
    20  16               Pidgey  Normal  Flying    251  40      45       40   
    21  17            Pidgeotto  Normal  Flying    349  63      60       55   
    22  18              Pidgeot  Normal  Flying    479  83      80       75   
    23  18  PidgeotMega Pidgeot  Normal  Flying    579  83      80       80   
    24  19              Rattata  Normal     NaN    253  30      56       35   
    
        Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    20       35       35     56           1      False  
    21       50       50     71           1      False  
    22       70       70    101           1      False  
    23      135       80    121           1      False  
    24       25       35     72           1      False  
         #      Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    25  20  Raticate  Normal     NaN    413  55      81       60       50   
    26  21   Spearow  Normal  Flying    262  40      60       30       31   
    27  22    Fearow  Normal  Flying    442  65      90       65       61   
    28  23     Ekans  Poison     NaN    288  35      60       44       40   
    29  24     Arbok  Poison     NaN    438  60      85       69       65   
    
        Sp. Def  Speed  Generation  Legendary  
    25       70     97           1      False  
    26       31     70           1      False  
    27       61    100           1      False  
    28       54     55           1      False  
    29       79     80           1      False  
         #       Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    30  25    Pikachu  Electric     NaN    320  35      55       40       50   
    31  26     Raichu  Electric     NaN    485  60      90       55       90   
    32  27  Sandshrew    Ground     NaN    300  50      75       85       20   
    33  28  Sandslash    Ground     NaN    450  75     100      110       45   
    34  29   Nidoran♀    Poison     NaN    275  55      47       52       40   
    
        Sp. Def  Speed  Generation  Legendary  
    30       50     90           1      False  
    31       80    110           1      False  
    32       30     40           1      False  
    33       55     65           1      False  
    34       40     41           1      False  
         #       Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    35  30   Nidorina  Poison     NaN    365  70      62       67       55   
    36  31  Nidoqueen  Poison  Ground    505  90      92       87       75   
    37  32   Nidoran♂  Poison     NaN    273  46      57       40       40   
    38  33   Nidorino  Poison     NaN    365  61      72       57       55   
    39  34   Nidoking  Poison  Ground    505  81     102       77       85   
    
        Sp. Def  Speed  Generation  Legendary  
    35       55     56           1      False  
    36       85     76           1      False  
    37       40     50           1      False  
    38       55     65           1      False  
    39       75     85           1      False  
         #        Name  Type 1 Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    40  35    Clefairy   Fairy    NaN    323   70      45       48       60   
    41  36    Clefable   Fairy    NaN    483   95      70       73       95   
    42  37      Vulpix    Fire    NaN    299   38      41       40       50   
    43  38   Ninetales    Fire    NaN    505   73      76       75       81   
    44  39  Jigglypuff  Normal  Fairy    270  115      45       20       45   
    
        Sp. Def  Speed  Generation  Legendary  
    40       65     35           1      False  
    41       90     60           1      False  
    42       65     65           1      False  
    43      100    100           1      False  
    44       25     20           1      False  
         #        Name  Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    45  40  Wigglytuff  Normal   Fairy    435  140      70       45       85   
    46  41       Zubat  Poison  Flying    245   40      45       35       30   
    47  42      Golbat  Poison  Flying    455   75      80       70       65   
    48  43      Oddish   Grass  Poison    320   45      50       55       75   
    49  44       Gloom   Grass  Poison    395   60      65       70       85   
    
        Sp. Def  Speed  Generation  Legendary  
    45       50     45           1      False  
    46       40     55           1      False  
    47       75     90           1      False  
    48       65     30           1      False  
    49       75     40           1      False  
         #       Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    50  45  Vileplume  Grass  Poison    490  75      80       85      110   
    51  46      Paras    Bug   Grass    285  35      70       55       45   
    52  47   Parasect    Bug   Grass    405  60      95       80       60   
    53  48    Venonat    Bug  Poison    305  60      55       50       40   
    54  49   Venomoth    Bug  Poison    450  70      65       60       90   
    
        Sp. Def  Speed  Generation  Legendary  
    50       90     50           1      False  
    51       55     25           1      False  
    52       80     30           1      False  
    53       55     45           1      False  
    54       75     90           1      False  
         #     Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    55  50  Diglett  Ground     NaN    265  10      55       25       35       45   
    56  51  Dugtrio  Ground     NaN    405  35      80       50       50       70   
    57  52   Meowth  Normal     NaN    290  40      45       35       40       40   
    58  53  Persian  Normal     NaN    440  65      70       60       65       65   
    59  54  Psyduck   Water     NaN    320  50      52       48       65       50   
    
        Speed  Generation  Legendary  
    55     95           1      False  
    56    120           1      False  
    57     90           1      False  
    58    115           1      False  
    59     55           1      False  
         #       Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    60  55    Golduck     Water     NaN    500  80      82       78       95   
    61  56     Mankey  Fighting     NaN    305  40      80       35       35   
    62  57   Primeape  Fighting     NaN    455  65     105       60       60   
    63  58  Growlithe      Fire     NaN    350  55      70       45       70   
    64  59   Arcanine      Fire     NaN    555  90     110       80      100   
    
        Sp. Def  Speed  Generation  Legendary  
    60       80     85           1      False  
    61       45     70           1      False  
    62       70     95           1      False  
    63       50     60           1      False  
    64       80     95           1      False  
         #       Name   Type 1    Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    65  60    Poliwag    Water       NaN    300  40      50       40       40   
    66  61  Poliwhirl    Water       NaN    385  65      65       65       50   
    67  62  Poliwrath    Water  Fighting    510  90      95       95       70   
    68  63       Abra  Psychic       NaN    310  25      20       15      105   
    69  64    Kadabra  Psychic       NaN    400  40      35       30      120   
    
        Sp. Def  Speed  Generation  Legendary  
    65       40     90           1      False  
    66       50     90           1      False  
    67       90     70           1      False  
    68       55     90           1      False  
    69       70    105           1      False  
         #                   Name    Type 1  Type 2  Total  HP  Attack  Defense  \
    70  65               Alakazam   Psychic     NaN    500  55      50       45   
    71  65  AlakazamMega Alakazam   Psychic     NaN    590  55      50       65   
    72  66                 Machop  Fighting     NaN    305  70      80       50   
    73  67                Machoke  Fighting     NaN    405  80     100       70   
    74  68                Machamp  Fighting     NaN    505  90     130       80   
    
        Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    70      135       95    120           1      False  
    71      175       95    150           1      False  
    72       35       35     35           1      False  
    73       50       60     45           1      False  
    74       65       85     55           1      False  
         #        Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    75  69  Bellsprout  Grass  Poison    300  50      75       35       70   
    76  70  Weepinbell  Grass  Poison    390  65      90       50       85   
    77  71  Victreebel  Grass  Poison    490  80     105       65      100   
    78  72   Tentacool  Water  Poison    335  40      40       35       50   
    79  73  Tentacruel  Water  Poison    515  80      70       65       80   
    
        Sp. Def  Speed  Generation  Legendary  
    75       30     40           1      False  
    76       45     55           1      False  
    77       70     70           1      False  
    78      100     70           1      False  
    79      120    100           1      False  
         #      Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    80  74   Geodude   Rock  Ground    300  40      80      100       30       30   
    81  75  Graveler   Rock  Ground    390  55      95      115       45       45   
    82  76     Golem   Rock  Ground    495  80     120      130       55       65   
    83  77    Ponyta   Fire     NaN    410  50      85       55       65       65   
    84  78  Rapidash   Fire     NaN    500  65     100       70       80       80   
    
        Speed  Generation  Legendary  
    80     20           1      False  
    81     35           1      False  
    82     45           1      False  
    83     90           1      False  
    84    105           1      False  
         #                 Name    Type 1   Type 2  Total  HP  Attack  Defense  \
    85  79             Slowpoke     Water  Psychic    315  90      65       65   
    86  80              Slowbro     Water  Psychic    490  95      75      110   
    87  80  SlowbroMega Slowbro     Water  Psychic    590  95      75      180   
    88  81            Magnemite  Electric    Steel    325  25      35       70   
    89  82             Magneton  Electric    Steel    465  50      60       95   
    
        Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    85       40       40     15           1      False  
    86      100       80     30           1      False  
    87      130       80     30           1      False  
    88       95       55     45           1      False  
    89      120       70     70           1      False  
         #        Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    90  83  Farfetch'd  Normal  Flying    352  52      65       55       58   
    91  84       Doduo  Normal  Flying    310  35      85       45       35   
    92  85      Dodrio  Normal  Flying    460  60     110       70       60   
    93  86        Seel   Water     NaN    325  65      45       55       45   
    94  87     Dewgong   Water     Ice    475  90      70       80       70   
    
        Sp. Def  Speed  Generation  Legendary  
    90       62     60           1      False  
    91       35     75           1      False  
    92       60    100           1      False  
    93       70     45           1      False  
    94       95     70           1      False  
         #      Name  Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    95  88    Grimer  Poison     NaN    325   80      80       50       40   
    96  89       Muk  Poison     NaN    500  105     105       75       65   
    97  90  Shellder   Water     NaN    305   30      65      100       45   
    98  91  Cloyster   Water     Ice    525   50      95      180       85   
    99  92    Gastly   Ghost  Poison    310   30      35       30      100   
    
        Sp. Def  Speed  Generation  Legendary  
    95       50     25           1      False  
    96      100     50           1      False  
    97       25     40           1      False  
    98       45     70           1      False  
    99       35     80           1      False  
          #               Name   Type 1  Type 2  Total  HP  Attack  Defense  \
    100  93            Haunter    Ghost  Poison    405  45      50       45   
    101  94             Gengar    Ghost  Poison    500  60      65       60   
    102  94  GengarMega Gengar    Ghost  Poison    600  60      65       80   
    103  95               Onix     Rock  Ground    385  35      45      160   
    104  96            Drowzee  Psychic     NaN    328  60      48       45   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    100      115       55     95           1      False  
    101      130       75    110           1      False  
    102      170       95    130           1      False  
    103       30       45     70           1      False  
    104       43       90     42           1      False  
           #       Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    105   97      Hypno   Psychic     NaN    483  85      73       70       73   
    106   98     Krabby     Water     NaN    325  30     105       90       25   
    107   99    Kingler     Water     NaN    475  55     130      115       50   
    108  100    Voltorb  Electric     NaN    330  40      30       50       55   
    109  101  Electrode  Electric     NaN    480  60      50       70       80   
    
         Sp. Def  Speed  Generation  Legendary  
    105      115     67           1      False  
    106       25     50           1      False  
    107       50     75           1      False  
    108       55    100           1      False  
    109       80    140           1      False  
           #       Name    Type 1   Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    110  102  Exeggcute     Grass  Psychic    325  60      40       80       60   
    111  103  Exeggutor     Grass  Psychic    520  95      95       85      125   
    112  104     Cubone    Ground      NaN    320  50      50       95       40   
    113  105    Marowak    Ground      NaN    425  60      80      110       50   
    114  106  Hitmonlee  Fighting      NaN    455  50     120       53       35   
    
         Sp. Def  Speed  Generation  Legendary  
    110       45     40           1      False  
    111       65     55           1      False  
    112       50     35           1      False  
    113       80     45           1      False  
    114      110     87           1      False  
           #        Name    Type 1 Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    115  107  Hitmonchan  Fighting    NaN    455  50     105       79       35   
    116  108   Lickitung    Normal    NaN    385  90      55       75       60   
    117  109     Koffing    Poison    NaN    340  40      65       95       60   
    118  110     Weezing    Poison    NaN    490  65      90      120       85   
    119  111     Rhyhorn    Ground   Rock    345  80      85       95       30   
    
         Sp. Def  Speed  Generation  Legendary  
    115      110     76           1      False  
    116       75     30           1      False  
    117       45     35           1      False  
    118       70     60           1      False  
    119       30     25           1      False  
           #                       Name  Type 1 Type 2  Total   HP  Attack  \
    120  112                     Rhydon  Ground   Rock    485  105     130   
    121  113                    Chansey  Normal    NaN    450  250       5   
    122  114                    Tangela   Grass    NaN    435   65      55   
    123  115                 Kangaskhan  Normal    NaN    490  105      95   
    124  115  KangaskhanMega Kangaskhan  Normal    NaN    590  105     125   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    120      120       45       45     40           1      False  
    121        5       35      105     50           1      False  
    122      115      100       40     60           1      False  
    123       80       40       80     90           1      False  
    124      100       60      100    100           1      False  
           #     Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    125  116   Horsea  Water     NaN    295  30      40       70       70   
    126  117   Seadra  Water     NaN    440  55      65       95       95   
    127  118  Goldeen  Water     NaN    320  45      67       60       35   
    128  119  Seaking  Water     NaN    450  80      92       65       65   
    129  120   Staryu  Water     NaN    340  30      45       55       70   
    
         Sp. Def  Speed  Generation  Legendary  
    125       25     60           1      False  
    126       45     85           1      False  
    127       50     63           1      False  
    128       80     68           1      False  
    129       55     85           1      False  
           #        Name    Type 1   Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    130  121     Starmie     Water  Psychic    520  60      75       85      100   
    131  122    Mr. Mime   Psychic    Fairy    460  40      45       65      100   
    132  123     Scyther       Bug   Flying    500  70     110       80       55   
    133  124        Jynx       Ice  Psychic    455  65      50       35      115   
    134  125  Electabuzz  Electric      NaN    490  65      83       57       95   
    
         Sp. Def  Speed  Generation  Legendary  
    130       85    115           1      False  
    131      120     90           1      False  
    132       80    105           1      False  
    133       95     95           1      False  
    134       85    105           1      False  
           #               Name  Type 1  Type 2  Total  HP  Attack  Defense  \
    135  126             Magmar    Fire     NaN    495  65      95       57   
    136  127             Pinsir     Bug     NaN    500  65     125      100   
    137  127  PinsirMega Pinsir     Bug  Flying    600  65     155      120   
    138  128             Tauros  Normal     NaN    490  75     100       95   
    139  129           Magikarp   Water     NaN    200  20      10       55   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    135      100       85     93           1      False  
    136       55       70     85           1      False  
    137       65       90    105           1      False  
    138       40       70    110           1      False  
    139       15       20     80           1      False  
           #                   Name  Type 1  Type 2  Total   HP  Attack  Defense  \
    140  130               Gyarados   Water  Flying    540   95     125       79   
    141  130  GyaradosMega Gyarados   Water    Dark    640   95     155      109   
    142  131                 Lapras   Water     Ice    535  130      85       80   
    143  132                  Ditto  Normal     NaN    288   48      48       48   
    144  133                  Eevee  Normal     NaN    325   55      55       50   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    140       60      100     81           1      False  
    141       70      130     81           1      False  
    142       85       95     60           1      False  
    143       48       48     48           1      False  
    144       45       65     55           1      False  
           #      Name    Type 1 Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    145  134  Vaporeon     Water    NaN    525  130      65       60      110   
    146  135   Jolteon  Electric    NaN    525   65      65       60      110   
    147  136   Flareon      Fire    NaN    525   65     130       60       95   
    148  137   Porygon    Normal    NaN    395   65      60       70       85   
    149  138   Omanyte      Rock  Water    355   35      40      100       90   
    
         Sp. Def  Speed  Generation  Legendary  
    145       95     65           1      False  
    146       95    130           1      False  
    147      110     65           1      False  
    148       75     40           1      False  
    149       55     35           1      False  
           #                       Name Type 1  Type 2  Total  HP  Attack  \
    150  139                    Omastar   Rock   Water    495  70      60   
    151  140                     Kabuto   Rock   Water    355  30      80   
    152  141                   Kabutops   Rock   Water    495  60     115   
    153  142                 Aerodactyl   Rock  Flying    515  80     105   
    154  142  AerodactylMega Aerodactyl   Rock  Flying    615  80     135   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    150      125      115       70     55           1      False  
    151       90       55       45     55           1      False  
    152      105       65       70     80           1      False  
    153       65       60       75    130           1      False  
    154       85       70       95    150           1      False  
           #      Name    Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    155  143   Snorlax    Normal     NaN    540  160     110       65       65   
    156  144  Articuno       Ice  Flying    580   90      85      100       95   
    157  145    Zapdos  Electric  Flying    580   90      90       85      125   
    158  146   Moltres      Fire  Flying    580   90     100       90      125   
    159  147   Dratini    Dragon     NaN    300   41      64       45       50   
    
         Sp. Def  Speed  Generation  Legendary  
    155      110     30           1      False  
    156      125     85           1       True  
    157       90    100           1       True  
    158       85     90           1       True  
    159       50     50           1      False  
           #                 Name   Type 1    Type 2  Total   HP  Attack  Defense  \
    160  148            Dragonair   Dragon       NaN    420   61      84       65   
    161  149            Dragonite   Dragon    Flying    600   91     134       95   
    162  150               Mewtwo  Psychic       NaN    680  106     110       90   
    163  150  MewtwoMega Mewtwo X  Psychic  Fighting    780  106     190      100   
    164  150  MewtwoMega Mewtwo Y  Psychic       NaN    780  106     150       70   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    160       70       70     70           1      False  
    161      100      100     80           1      False  
    162      154       90    130           1       True  
    163      154      100    130           1       True  
    164      194      120    140           1       True  
           #       Name   Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    165  151        Mew  Psychic     NaN    600  100     100      100      100   
    166  152  Chikorita    Grass     NaN    318   45      49       65       49   
    167  153    Bayleef    Grass     NaN    405   60      62       80       63   
    168  154   Meganium    Grass     NaN    525   80      82      100       83   
    169  155  Cyndaquil     Fire     NaN    309   39      52       43       60   
    
         Sp. Def  Speed  Generation  Legendary  
    165      100    100           1      False  
    166       65     45           2      False  
    167       80     60           2      False  
    168      100     80           2      False  
    169       50     65           2      False  
           #        Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    170  156     Quilava   Fire     NaN    405  58      64       58       80   
    171  157  Typhlosion   Fire     NaN    534  78      84       78      109   
    172  158    Totodile  Water     NaN    314  50      65       64       44   
    173  159    Croconaw  Water     NaN    405  65      80       80       59   
    174  160  Feraligatr  Water     NaN    530  85     105      100       79   
    
         Sp. Def  Speed  Generation  Legendary  
    170       65     80           2      False  
    171       85    100           2      False  
    172       48     43           2      False  
    173       63     58           2      False  
    174       83     78           2      False  
           #      Name  Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    175  161   Sentret  Normal     NaN    215   35      46       34       35   
    176  162    Furret  Normal     NaN    415   85      76       64       45   
    177  163  Hoothoot  Normal  Flying    262   60      30       30       36   
    178  164   Noctowl  Normal  Flying    442  100      50       50       76   
    179  165    Ledyba     Bug  Flying    265   40      20       30       40   
    
         Sp. Def  Speed  Generation  Legendary  
    175       45     20           2      False  
    176       55     90           2      False  
    177       56     50           2      False  
    178       96     70           2      False  
    179       80     55           2      False  
           #      Name  Type 1    Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    180  166    Ledian     Bug    Flying    390  55      35       50       55   
    181  167  Spinarak     Bug    Poison    250  40      60       40       40   
    182  168   Ariados     Bug    Poison    390  70      90       70       60   
    183  169    Crobat  Poison    Flying    535  85      90       80       70   
    184  170  Chinchou   Water  Electric    330  75      38       38       56   
    
         Sp. Def  Speed  Generation  Legendary  
    180      110     85           2      False  
    181       40     30           2      False  
    182       60     40           2      False  
    183       80    130           2      False  
    184       56     67           2      False  
           #       Name    Type 1    Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    185  171    Lanturn     Water  Electric    460  125      58       58       76   
    186  172      Pichu  Electric       NaN    205   20      40       15       35   
    187  173     Cleffa     Fairy       NaN    218   50      25       28       45   
    188  174  Igglybuff    Normal     Fairy    210   90      30       15       40   
    189  175     Togepi     Fairy       NaN    245   35      20       65       40   
    
         Sp. Def  Speed  Generation  Legendary  
    185       76     67           2      False  
    186       35     60           2      False  
    187       55     15           2      False  
    188       20     15           2      False  
    189       65     20           2      False  
           #     Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    190  176  Togetic     Fairy  Flying    405  55      40       85       80   
    191  177     Natu   Psychic  Flying    320  40      50       45       70   
    192  178     Xatu   Psychic  Flying    470  65      75       70       95   
    193  179   Mareep  Electric     NaN    280  55      40       40       65   
    194  180  Flaaffy  Electric     NaN    365  70      55       55       80   
    
         Sp. Def  Speed  Generation  Legendary  
    190      105     40           2      False  
    191       45     70           2      False  
    192       70     95           2      False  
    193       45     35           2      False  
    194       60     45           2      False  
           #                   Name    Type 1  Type 2  Total   HP  Attack  \
    195  181               Ampharos  Electric     NaN    510   90      75   
    196  181  AmpharosMega Ampharos  Electric  Dragon    610   90      95   
    197  182              Bellossom     Grass     NaN    490   75      80   
    198  183                 Marill     Water   Fairy    250   70      20   
    199  184              Azumarill     Water   Fairy    420  100      50   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    195       85      115       90     55           2      False  
    196      105      165      110     45           2      False  
    197       95       90      100     50           2      False  
    198       50       20       50     40           2      False  
    199       80       60       80     50           2      False  
           #       Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    200  185  Sudowoodo   Rock     NaN    410  70     100      115       30   
    201  186   Politoed  Water     NaN    500  90      75       75       90   
    202  187     Hoppip  Grass  Flying    250  35      35       40       35   
    203  188   Skiploom  Grass  Flying    340  55      45       50       45   
    204  189   Jumpluff  Grass  Flying    460  75      55       70       55   
    
         Sp. Def  Speed  Generation  Legendary  
    200       65     30           2      False  
    201      100     70           2      False  
    202       55     50           2      False  
    203       65     80           2      False  
    204       95    110           2      False  
           #      Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    205  190     Aipom  Normal     NaN    360  55      70       55       40   
    206  191   Sunkern   Grass     NaN    180  30      30       30       30   
    207  192  Sunflora   Grass     NaN    425  75      75       55      105   
    208  193     Yanma     Bug  Flying    390  65      65       45       75   
    209  194    Wooper   Water  Ground    210  55      45       45       25   
    
         Sp. Def  Speed  Generation  Legendary  
    205       55     85           2      False  
    206       30     30           2      False  
    207       85     30           2      False  
    208       45     95           2      False  
    209       25     15           2      False  
           #      Name   Type 1   Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    210  195  Quagsire    Water   Ground    430  95      85       85       65   
    211  196    Espeon  Psychic      NaN    525  65      65       60      130   
    212  197   Umbreon     Dark      NaN    525  95      65      110       60   
    213  198   Murkrow     Dark   Flying    405  60      85       42       85   
    214  199  Slowking    Water  Psychic    490  95      75       80      100   
    
         Sp. Def  Speed  Generation  Legendary  
    210       65     35           2      False  
    211       95    110           2      False  
    212      130     65           2      False  
    213       42     91           2      False  
    214      110     30           2      False  
           #        Name   Type 1   Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    215  200  Misdreavus    Ghost      NaN    435   60      60       60       85   
    216  201       Unown  Psychic      NaN    336   48      72       48       72   
    217  202   Wobbuffet  Psychic      NaN    405  190      33       58       33   
    218  203   Girafarig   Normal  Psychic    455   70      80       65       90   
    219  204      Pineco      Bug      NaN    290   50      65       90       35   
    
         Sp. Def  Speed  Generation  Legendary  
    215       85     85           2      False  
    216       48     48           2      False  
    217       58     33           2      False  
    218       65     85           2      False  
    219       35     15           2      False  
           #                 Name  Type 1  Type 2  Total   HP  Attack  Defense  \
    220  205           Forretress     Bug   Steel    465   75      90      140   
    221  206            Dunsparce  Normal     NaN    415  100      70       70   
    222  207               Gligar  Ground  Flying    430   65      75      105   
    223  208              Steelix   Steel  Ground    510   75      85      200   
    224  208  SteelixMega Steelix   Steel  Ground    610   75     125      230   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    220       60       60     40           2      False  
    221       65       65     45           2      False  
    222       35       65     85           2      False  
    223       55       65     30           2      False  
    224       55       95     30           2      False  
           #               Name Type 1  Type 2  Total  HP  Attack  Defense  \
    225  209           Snubbull  Fairy     NaN    300  60      80       50   
    226  210           Granbull  Fairy     NaN    450  90     120       75   
    227  211           Qwilfish  Water  Poison    430  65      95       75   
    228  212             Scizor    Bug   Steel    500  70     130      100   
    229  212  ScizorMega Scizor    Bug   Steel    600  70     150      140   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    225       40       40     30           2      False  
    226       60       60     45           2      False  
    227       55       55     85           2      False  
    228       55       80     65           2      False  
    229       65      100     75           2      False  
           #                     Name  Type 1    Type 2  Total  HP  Attack  \
    230  213                  Shuckle     Bug      Rock    505  20      10   
    231  214                Heracross     Bug  Fighting    500  80     125   
    232  214  HeracrossMega Heracross     Bug  Fighting    600  80     185   
    233  215                  Sneasel    Dark       Ice    430  55      95   
    234  216                Teddiursa  Normal       NaN    330  60      80   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    230      230       10      230      5           2      False  
    231       75       40       95     85           2      False  
    232      115       40      105     75           2      False  
    233       55       35       75    115           2      False  
    234       50       50       50     40           2      False  
           #       Name  Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    235  217   Ursaring  Normal     NaN    500   90     130       75       75   
    236  218     Slugma    Fire     NaN    250   40      40       40       70   
    237  219   Magcargo    Fire    Rock    410   50      50      120       80   
    238  220     Swinub     Ice  Ground    250   50      50       40       30   
    239  221  Piloswine     Ice  Ground    450  100     100       80       60   
    
         Sp. Def  Speed  Generation  Legendary  
    235       75     55           2      False  
    236       40     20           2      False  
    237       80     30           2      False  
    238       30     50           2      False  
    239       60     50           2      False  
           #       Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    240  222    Corsola  Water    Rock    380  55      55       85       65   
    241  223   Remoraid  Water     NaN    300  35      65       35       65   
    242  224  Octillery  Water     NaN    480  75     105       75      105   
    243  225   Delibird    Ice  Flying    330  45      55       45       65   
    244  226    Mantine  Water  Flying    465  65      40       70       80   
    
         Sp. Def  Speed  Generation  Legendary  
    240       85     35           2      False  
    241       35     65           2      False  
    242       75     45           2      False  
    243       45     75           2      False  
    244      140     70           2      False  
           #                   Name Type 1  Type 2  Total  HP  Attack  Defense  \
    245  227               Skarmory  Steel  Flying    465  65      80      140   
    246  228               Houndour   Dark    Fire    330  45      60       30   
    247  229               Houndoom   Dark    Fire    500  75      90       50   
    248  229  HoundoomMega Houndoom   Dark    Fire    600  75      90       90   
    249  230                Kingdra  Water  Dragon    540  75      95       95   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    245       40       70     70           2      False  
    246       80       50     65           2      False  
    247      110       80     95           2      False  
    248      140       90    115           2      False  
    249       95       95     85           2      False  
           #      Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    250  231    Phanpy  Ground     NaN    330  90      60       60       40   
    251  232   Donphan  Ground     NaN    500  90     120      120       60   
    252  233  Porygon2  Normal     NaN    515  85      80       90      105   
    253  234  Stantler  Normal     NaN    465  73      95       62       85   
    254  235  Smeargle  Normal     NaN    250  55      20       35       20   
    
         Sp. Def  Speed  Generation  Legendary  
    250       40     40           2      False  
    251       60     50           2      False  
    252       95     60           2      False  
    253       65     85           2      False  
    254       45     75           2      False  
           #       Name    Type 1   Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    255  236    Tyrogue  Fighting      NaN    210  35      35       35       35   
    256  237  Hitmontop  Fighting      NaN    455  50      95       95       35   
    257  238   Smoochum       Ice  Psychic    305  45      30       15       85   
    258  239     Elekid  Electric      NaN    360  45      63       37       65   
    259  240      Magby      Fire      NaN    365  45      75       37       70   
    
         Sp. Def  Speed  Generation  Legendary  
    255       35     35           2      False  
    256      110     70           2      False  
    257       65     65           2      False  
    258       55     95           2      False  
    259       55     83           2      False  
           #     Name    Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    260  241  Miltank    Normal     NaN    490   95      80      105       40   
    261  242  Blissey    Normal     NaN    540  255      10       10       75   
    262  243   Raikou  Electric     NaN    580   90      85       75      115   
    263  244    Entei      Fire     NaN    580  115     115       85       90   
    264  245  Suicune     Water     NaN    580  100      75      115       90   
    
         Sp. Def  Speed  Generation  Legendary  
    260       70    100           2      False  
    261      135     55           2      False  
    262      100    115           2       True  
    263       75    100           2       True  
    264      115     85           2       True  
           #                     Name   Type 1  Type 2  Total   HP  Attack  \
    265  246                 Larvitar     Rock  Ground    300   50      64   
    266  247                  Pupitar     Rock  Ground    410   70      84   
    267  248                Tyranitar     Rock    Dark    600  100     134   
    268  248  TyranitarMega Tyranitar     Rock    Dark    700  100     164   
    269  249                    Lugia  Psychic  Flying    680  106      90   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    265       50       45       50     41           2      False  
    266       70       65       70     51           2      False  
    267      110       95      100     61           2      False  
    268      150       95      120     71           2      False  
    269      130       90      154    110           2       True  
           #      Name   Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    270  250     Ho-oh     Fire  Flying    680  106     130       90      110   
    271  251    Celebi  Psychic   Grass    600  100     100      100      100   
    272  252   Treecko    Grass     NaN    310   40      45       35       65   
    273  253   Grovyle    Grass     NaN    405   50      65       45       85   
    274  254  Sceptile    Grass     NaN    530   70      85       65      105   
    
         Sp. Def  Speed  Generation  Legendary  
    270      154     90           2       True  
    271      100    100           2      False  
    272       55     70           3      False  
    273       65     95           3      False  
    274       85    120           3      False  
           #                   Name Type 1    Type 2  Total  HP  Attack  Defense  \
    275  254  SceptileMega Sceptile  Grass    Dragon    630  70     110       75   
    276  255                Torchic   Fire       NaN    310  45      60       40   
    277  256              Combusken   Fire  Fighting    405  60      85       60   
    278  257               Blaziken   Fire  Fighting    530  80     120       70   
    279  257  BlazikenMega Blaziken   Fire  Fighting    630  80     160       80   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    275      145       85    145           3      False  
    276       70       50     45           3      False  
    277       85       60     55           3      False  
    278      110       70     80           3      False  
    279      130       80    100           3      False  
           #                   Name Type 1  Type 2  Total   HP  Attack  Defense  \
    280  258                 Mudkip  Water     NaN    310   50      70       50   
    281  259              Marshtomp  Water  Ground    405   70      85       70   
    282  260               Swampert  Water  Ground    535  100     110       90   
    283  260  SwampertMega Swampert  Water  Ground    635  100     150      110   
    284  261              Poochyena   Dark     NaN    220   35      55       35   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    280       50       50     40           3      False  
    281       60       70     50           3      False  
    282       85       90     60           3      False  
    283       95      110     70           3      False  
    284       30       30     35           3      False  
           #       Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    285  262  Mightyena    Dark     NaN    420  70      90       70       60   
    286  263  Zigzagoon  Normal     NaN    240  38      30       41       30   
    287  264    Linoone  Normal     NaN    420  78      70       61       50   
    288  265    Wurmple     Bug     NaN    195  45      45       35       20   
    289  266    Silcoon     Bug     NaN    205  50      35       55       25   
    
         Sp. Def  Speed  Generation  Legendary  
    285       60     70           3      False  
    286       41     60           3      False  
    287       61    100           3      False  
    288       30     20           3      False  
    289       25     15           3      False  
           #       Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    290  267  Beautifly    Bug  Flying    395  60      70       50      100   
    291  268    Cascoon    Bug     NaN    205  50      35       55       25   
    292  269     Dustox    Bug  Poison    385  60      50       70       50   
    293  270      Lotad  Water   Grass    220  40      30       30       40   
    294  271     Lombre  Water   Grass    340  60      50       50       60   
    
         Sp. Def  Speed  Generation  Legendary  
    290       50     65           3      False  
    291       25     15           3      False  
    292       90     65           3      False  
    293       50     30           3      False  
    294       70     50           3      False  
           #      Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    295  272  Ludicolo   Water   Grass    480  80      70       70       90   
    296  273    Seedot   Grass     NaN    220  40      40       50       30   
    297  274   Nuzleaf   Grass    Dark    340  70      70       40       60   
    298  275   Shiftry   Grass    Dark    480  90     100       60       90   
    299  276   Taillow  Normal  Flying    270  40      55       30       30   
    
         Sp. Def  Speed  Generation  Legendary  
    295      100     70           3      False  
    296       30     30           3      False  
    297       40     60           3      False  
    298       60     80           3      False  
    299       30     85           3      False  
           #      Name   Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    300  277   Swellow   Normal  Flying    430  60      85       60       50   
    301  278   Wingull    Water  Flying    270  40      30       30       55   
    302  279  Pelipper    Water  Flying    430  60      50      100       85   
    303  280     Ralts  Psychic   Fairy    198  28      25       25       45   
    304  281    Kirlia  Psychic   Fairy    278  38      35       35       65   
    
         Sp. Def  Speed  Generation  Legendary  
    300       50    125           3      False  
    301       30     85           3      False  
    302       70     65           3      False  
    303       35     40           3      False  
    304       55     50           3      False  
           #                     Name   Type 1  Type 2  Total  HP  Attack  \
    305  282                Gardevoir  Psychic   Fairy    518  68      65   
    306  282  GardevoirMega Gardevoir  Psychic   Fairy    618  68      85   
    307  283                  Surskit      Bug   Water    269  40      30   
    308  284               Masquerain      Bug  Flying    414  70      60   
    309  285                Shroomish    Grass     NaN    295  60      40   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    305       65      125      115     80           3      False  
    306       65      165      135    100           3      False  
    307       32       50       52     65           3      False  
    308       62       80       82     60           3      False  
    309       60       40       60     35           3      False  
           #      Name  Type 1    Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    310  286   Breloom   Grass  Fighting    460   60     130       80       60   
    311  287   Slakoth  Normal       NaN    280   60      60       60       35   
    312  288  Vigoroth  Normal       NaN    440   80      80       80       55   
    313  289   Slaking  Normal       NaN    670  150     160      100       95   
    314  290   Nincada     Bug    Ground    266   31      45       90       30   
    
         Sp. Def  Speed  Generation  Legendary  
    310       60     70           3      False  
    311       35     30           3      False  
    312       55     90           3      False  
    313       65    100           3      False  
    314       30     40           3      False  
           #      Name  Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    315  291   Ninjask     Bug  Flying    456   61      90       45       50   
    316  292  Shedinja     Bug   Ghost    236    1      90       45       30   
    317  293   Whismur  Normal     NaN    240   64      51       23       51   
    318  294   Loudred  Normal     NaN    360   84      71       43       71   
    319  295   Exploud  Normal     NaN    490  104      91       63       91   
    
         Sp. Def  Speed  Generation  Legendary  
    315       50    160           3      False  
    316       30     40           3      False  
    317       23     28           3      False  
    318       43     48           3      False  
    319       73     68           3      False  
           #      Name    Type 1 Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    320  296  Makuhita  Fighting    NaN    237   72      60       30       20   
    321  297  Hariyama  Fighting    NaN    474  144     120       60       40   
    322  298   Azurill    Normal  Fairy    190   50      20       40       20   
    323  299  Nosepass      Rock    NaN    375   30      45      135       45   
    324  300    Skitty    Normal    NaN    260   50      45       45       35   
    
         Sp. Def  Speed  Generation  Legendary  
    320       30     25           3      False  
    321       60     50           3      False  
    322       40     20           3      False  
    323       90     30           3      False  
    324       35     50           3      False  
           #                 Name  Type 1 Type 2  Total  HP  Attack  Defense  \
    325  301             Delcatty  Normal    NaN    380  70      65       65   
    326  302              Sableye    Dark  Ghost    380  50      75       75   
    327  302  SableyeMega Sableye    Dark  Ghost    480  50      85      125   
    328  303               Mawile   Steel  Fairy    380  50      85       85   
    329  303    MawileMega Mawile   Steel  Fairy    480  50     105      125   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    325       55       55     70           3      False  
    326       65       65     50           3      False  
    327       85      115     20           3      False  
    328       55       55     50           3      False  
    329       55       95     50           3      False  
           #               Name    Type 1   Type 2  Total  HP  Attack  Defense  \
    330  304               Aron     Steel     Rock    330  50      70      100   
    331  305             Lairon     Steel     Rock    430  60      90      140   
    332  306             Aggron     Steel     Rock    530  70     110      180   
    333  306  AggronMega Aggron     Steel      NaN    630  70     140      230   
    334  307           Meditite  Fighting  Psychic    280  30      40       55   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    330       40       40     30           3      False  
    331       50       50     40           3      False  
    332       60       60     50           3      False  
    333       60       80     50           3      False  
    334       40       55     60           3      False  
           #                     Name    Type 1   Type 2  Total  HP  Attack  \
    335  308                 Medicham  Fighting  Psychic    410  60      60   
    336  308    MedichamMega Medicham  Fighting  Psychic    510  60     100   
    337  309                Electrike  Electric      NaN    295  40      45   
    338  310                Manectric  Electric      NaN    475  70      75   
    339  310  ManectricMega Manectric  Electric      NaN    575  70      75   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    335       75       60       75     80           3      False  
    336       85       80       85    100           3      False  
    337       40       65       40     65           3      False  
    338       60      105       60    105           3      False  
    339       80      135       80    135           3      False  
           #      Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    340  311    Plusle  Electric     NaN    405  60      50       40       85   
    341  312     Minun  Electric     NaN    405  60      40       50       75   
    342  313   Volbeat       Bug     NaN    400  65      73       55       47   
    343  314  Illumise       Bug     NaN    400  65      47       55       73   
    344  315   Roselia     Grass  Poison    400  50      60       45      100   
    
         Sp. Def  Speed  Generation  Legendary  
    340       75     95           3      False  
    341       85     95           3      False  
    342       75     85           3      False  
    343       75     85           3      False  
    344       80     65           3      False  
           #                   Name  Type 1 Type 2  Total   HP  Attack  Defense  \
    345  316                 Gulpin  Poison    NaN    302   70      43       53   
    346  317                 Swalot  Poison    NaN    467  100      73       83   
    347  318               Carvanha   Water   Dark    305   45      90       20   
    348  319               Sharpedo   Water   Dark    460   70     120       40   
    349  319  SharpedoMega Sharpedo   Water   Dark    560   70     140       70   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    345       43       53     40           3      False  
    346       73       83     55           3      False  
    347       65       20     65           3      False  
    348       95       40     95           3      False  
    349      110       65    105           3      False  
           #                   Name Type 1  Type 2  Total   HP  Attack  Defense  \
    350  320                Wailmer  Water     NaN    400  130      70       35   
    351  321                Wailord  Water     NaN    500  170      90       45   
    352  322                  Numel   Fire  Ground    305   60      60       40   
    353  323               Camerupt   Fire  Ground    460   70     100       70   
    354  323  CameruptMega Camerupt   Fire  Ground    560   70     120      100   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    350       70       35     60           3      False  
    351       90       45     60           3      False  
    352       65       45     35           3      False  
    353      105       75     40           3      False  
    354      145      105     20           3      False  
           #      Name   Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    355  324   Torkoal     Fire     NaN    470  70      85      140       85   
    356  325    Spoink  Psychic     NaN    330  60      25       35       70   
    357  326   Grumpig  Psychic     NaN    470  80      45       65       90   
    358  327    Spinda   Normal     NaN    360  60      60       60       60   
    359  328  Trapinch   Ground     NaN    290  45     100       45       45   
    
         Sp. Def  Speed  Generation  Legendary  
    355       70     20           3      False  
    356       80     60           3      False  
    357      110     80           3      False  
    358       60     60           3      False  
    359       45     10           3      False  
           #      Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    360  329   Vibrava  Ground  Dragon    340  50      70       50       50   
    361  330    Flygon  Ground  Dragon    520  80     100       80       80   
    362  331    Cacnea   Grass     NaN    335  50      85       40       85   
    363  332  Cacturne   Grass    Dark    475  70     115       60      115   
    364  333    Swablu  Normal  Flying    310  45      40       60       40   
    
         Sp. Def  Speed  Generation  Legendary  
    360       50     70           3      False  
    361       80    100           3      False  
    362       40     35           3      False  
    363       60     55           3      False  
    364       75     50           3      False  
           #                 Name  Type 1   Type 2  Total  HP  Attack  Defense  \
    365  334              Altaria  Dragon   Flying    490  75      70       90   
    366  334  AltariaMega Altaria  Dragon    Fairy    590  75     110      110   
    367  335             Zangoose  Normal      NaN    458  73     115       60   
    368  336              Seviper  Poison      NaN    458  73     100       60   
    369  337             Lunatone    Rock  Psychic    440  70      55       65   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    365       70      105     80           3      False  
    366      110      105     80           3      False  
    367       60       60     90           3      False  
    368      100       60     65           3      False  
    369       95       85     70           3      False  
           #       Name Type 1   Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    370  338    Solrock   Rock  Psychic    440   70      95       85       55   
    371  339   Barboach  Water   Ground    288   50      48       43       46   
    372  340   Whiscash  Water   Ground    468  110      78       73       76   
    373  341   Corphish  Water      NaN    308   43      80       65       50   
    374  342  Crawdaunt  Water     Dark    468   63     120       85       90   
    
         Sp. Def  Speed  Generation  Legendary  
    370       65     70           3      False  
    371       41     60           3      False  
    372       71     60           3      False  
    373       35     35           3      False  
    374       55     55           3      False  
           #     Name  Type 1   Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    375  343   Baltoy  Ground  Psychic    300  40      40       55       40   
    376  344  Claydol  Ground  Psychic    500  60      70      105       70   
    377  345   Lileep    Rock    Grass    355  66      41       77       61   
    378  346  Cradily    Rock    Grass    495  86      81       97       81   
    379  347  Anorith    Rock      Bug    355  45      95       50       40   
    
         Sp. Def  Speed  Generation  Legendary  
    375       70     55           3      False  
    376      120     75           3      False  
    377       87     23           3      False  
    378      107     43           3      False  
    379       50     75           3      False  
           #      Name  Type 1 Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    380  348   Armaldo    Rock    Bug    495  75     125      100       70   
    381  349    Feebas   Water    NaN    200  20      15       20       10   
    382  350   Milotic   Water    NaN    540  95      60       79      100   
    383  351  Castform  Normal    NaN    420  70      70       70       70   
    384  352   Kecleon  Normal    NaN    440  60      90       70       60   
    
         Sp. Def  Speed  Generation  Legendary  
    380       80     45           3      False  
    381       55     80           3      False  
    382      125     81           3      False  
    383       70     70           3      False  
    384      120     40           3      False  
           #                 Name Type 1  Type 2  Total  HP  Attack  Defense  \
    385  353              Shuppet  Ghost     NaN    295  44      75       35   
    386  354              Banette  Ghost     NaN    455  64     115       65   
    387  354  BanetteMega Banette  Ghost     NaN    555  64     165       75   
    388  355              Duskull  Ghost     NaN    295  20      40       90   
    389  356             Dusclops  Ghost     NaN    455  40      70      130   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    385       63       33     45           3      False  
    386       83       63     65           3      False  
    387       93       83     75           3      False  
    388       30       90     25           3      False  
    389       60      130     25           3      False  
           #             Name   Type 1  Type 2  Total  HP  Attack  Defense  \
    390  357          Tropius    Grass  Flying    460  99      68       83   
    391  358         Chimecho  Psychic     NaN    425  65      50       70   
    392  359            Absol     Dark     NaN    465  65     130       60   
    393  359  AbsolMega Absol     Dark     NaN    565  65     150       60   
    394  360           Wynaut  Psychic     NaN    260  95      23       48   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    390       72       87     51           3      False  
    391       95       80     65           3      False  
    392       75       60     75           3      False  
    393      115       60    115           3      False  
    394       23       48     23           3      False  
           #               Name Type 1 Type 2  Total  HP  Attack  Defense  \
    395  361            Snorunt    Ice    NaN    300  50      50       50   
    396  362             Glalie    Ice    NaN    480  80      80       80   
    397  362  GlalieMega Glalie    Ice    NaN    580  80     120       80   
    398  363             Spheal    Ice  Water    290  70      40       50   
    399  364             Sealeo    Ice  Water    410  90      60       70   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    395       50       50     50           3      False  
    396       80       80     80           3      False  
    397      120       80    100           3      False  
    398       55       50     25           3      False  
    399       75       70     45           3      False  
           #       Name Type 1 Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    400  365    Walrein    Ice  Water    530  110      80       90       95   
    401  366   Clamperl  Water    NaN    345   35      64       85       74   
    402  367    Huntail  Water    NaN    485   55     104      105       94   
    403  368   Gorebyss  Water    NaN    485   55      84      105      114   
    404  369  Relicanth  Water   Rock    485  100      90      130       45   
    
         Sp. Def  Speed  Generation  Legendary  
    400       90     65           3      False  
    401       55     32           3      False  
    402       75     52           3      False  
    403       75     52           3      False  
    404       65     55           3      False  
           #                     Name  Type 1  Type 2  Total  HP  Attack  Defense  \
    405  370                  Luvdisc   Water     NaN    330  43      30       55   
    406  371                    Bagon  Dragon     NaN    300  45      75       60   
    407  372                  Shelgon  Dragon     NaN    420  65      95      100   
    408  373                Salamence  Dragon  Flying    600  95     135       80   
    409  373  SalamenceMega Salamence  Dragon  Flying    700  95     145      130   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    405       40       65     97           3      False  
    406       40       30     50           3      False  
    407       60       50     50           3      False  
    408      110       80    100           3      False  
    409      120       90    120           3      False  
           #                     Name Type 1   Type 2  Total  HP  Attack  Defense  \
    410  374                   Beldum  Steel  Psychic    300  40      55       80   
    411  375                   Metang  Steel  Psychic    420  60      75      100   
    412  376                Metagross  Steel  Psychic    600  80     135      130   
    413  376  MetagrossMega Metagross  Steel  Psychic    700  80     145      150   
    414  377                 Regirock   Rock      NaN    580  80     100      200   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    410       35       60     30           3      False  
    411       55       80     50           3      False  
    412       95       90     70           3      False  
    413      105      110    110           3      False  
    414       50      100     50           3       True  
           #               Name  Type 1   Type 2  Total  HP  Attack  Defense  \
    415  378             Regice     Ice      NaN    580  80      50      100   
    416  379          Registeel   Steel      NaN    580  80      75      150   
    417  380             Latias  Dragon  Psychic    600  80      80       90   
    418  380  LatiasMega Latias  Dragon  Psychic    700  80     100      120   
    419  381             Latios  Dragon  Psychic    600  80      90       80   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    415      100      200     50           3       True  
    416       75      150     50           3       True  
    417      110      130    110           3       True  
    418      140      150    110           3       True  
    419      130      110    110           3       True  
           #                   Name  Type 1   Type 2  Total   HP  Attack  Defense  \
    420  381      LatiosMega Latios  Dragon  Psychic    700   80     130      100   
    421  382                 Kyogre   Water      NaN    670  100     100       90   
    422  382    KyogrePrimal Kyogre   Water      NaN    770  100     150       90   
    423  383                Groudon  Ground      NaN    670  100     150      140   
    424  383  GroudonPrimal Groudon  Ground     Fire    770  100     180      160   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    420      160      120    110           3       True  
    421      150      140     90           3       True  
    422      180      160     90           3       True  
    423      100       90     90           3       True  
    424      150       90     90           3       True  
           #                   Name   Type 1   Type 2  Total   HP  Attack  \
    425  384               Rayquaza   Dragon   Flying    680  105     150   
    426  384  RayquazaMega Rayquaza   Dragon   Flying    780  105     180   
    427  385                Jirachi    Steel  Psychic    600  100     100   
    428  386     DeoxysNormal Forme  Psychic      NaN    600   50     150   
    429  386     DeoxysAttack Forme  Psychic      NaN    600   50     180   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    425       90      150       90     95           3       True  
    426      100      180      100    115           3       True  
    427      100      100      100    100           3       True  
    428       50      150       50    150           3       True  
    429       20      180       20    150           3       True  
           #                 Name   Type 1  Type 2  Total  HP  Attack  Defense  \
    430  386  DeoxysDefense Forme  Psychic     NaN    600  50      70      160   
    431  386    DeoxysSpeed Forme  Psychic     NaN    600  50      95       90   
    432  387              Turtwig    Grass     NaN    318  55      68       64   
    433  388               Grotle    Grass     NaN    405  75      89       85   
    434  389             Torterra    Grass  Ground    525  95     109      105   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    430       70      160     90           3       True  
    431       95       90    180           3       True  
    432       45       55     31           4      False  
    433       55       65     36           4      False  
    434       75       85     56           4      False  
           #       Name Type 1    Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    435  390   Chimchar   Fire       NaN    309  44      58       44       58   
    436  391   Monferno   Fire  Fighting    405  64      78       52       78   
    437  392  Infernape   Fire  Fighting    534  76     104       71      104   
    438  393     Piplup  Water       NaN    314  53      51       53       61   
    439  394   Prinplup  Water       NaN    405  64      66       68       81   
    
         Sp. Def  Speed  Generation  Legendary  
    435       44     61           4      False  
    436       52     81           4      False  
    437       71    108           4      False  
    438       56     40           4      False  
    439       76     50           4      False  
           #       Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    440  395   Empoleon   Water   Steel    530  84      86       88      111   
    441  396     Starly  Normal  Flying    245  40      55       30       30   
    442  397   Staravia  Normal  Flying    340  55      75       50       40   
    443  398  Staraptor  Normal  Flying    485  85     120       70       50   
    444  399     Bidoof  Normal     NaN    250  59      45       40       35   
    
         Sp. Def  Speed  Generation  Legendary  
    440      101     60           4      False  
    441       30     60           4      False  
    442       40     80           4      False  
    443       60    100           4      False  
    444       40     31           4      False  
           #        Name    Type 1 Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    445  400     Bibarel    Normal  Water    410  79      85       60       55   
    446  401   Kricketot       Bug    NaN    194  37      25       41       25   
    447  402  Kricketune       Bug    NaN    384  77      85       51       55   
    448  403       Shinx  Electric    NaN    263  45      65       34       40   
    449  404       Luxio  Electric    NaN    363  60      85       49       60   
    
         Sp. Def  Speed  Generation  Legendary  
    445       60     71           4      False  
    446       41     25           4      False  
    447       51     65           4      False  
    448       34     45           4      False  
    449       49     60           4      False  
           #       Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    450  405     Luxray  Electric     NaN    523  80     120       79       95   
    451  406      Budew     Grass  Poison    280  40      30       35       50   
    452  407   Roserade     Grass  Poison    515  60      70       65      125   
    453  408   Cranidos      Rock     NaN    350  67     125       40       30   
    454  409  Rampardos      Rock     NaN    495  97     165       60       65   
    
         Sp. Def  Speed  Generation  Legendary  
    450       79     70           4      False  
    451       70     55           4      False  
    452      105     90           4      False  
    453       30     58           4      False  
    454       50     58           4      False  
           #                 Name Type 1  Type 2  Total  HP  Attack  Defense  \
    455  410             Shieldon   Rock   Steel    350  30      42      118   
    456  411            Bastiodon   Rock   Steel    495  60      52      168   
    457  412                Burmy    Bug     NaN    224  40      29       45   
    458  413  WormadamPlant Cloak    Bug   Grass    424  60      59       85   
    459  413  WormadamSandy Cloak    Bug  Ground    424  60      79      105   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    455       42       88     30           4      False  
    456       47      138     30           4      False  
    457       29       45     36           4      False  
    458       79      105     36           4      False  
    459       59       85     36           4      False  
           #                 Name    Type 1  Type 2  Total  HP  Attack  Defense  \
    460  413  WormadamTrash Cloak       Bug   Steel    424  60      69       95   
    461  414               Mothim       Bug  Flying    424  70      94       50   
    462  415               Combee       Bug  Flying    244  30      30       42   
    463  416            Vespiquen       Bug  Flying    474  70      80      102   
    464  417            Pachirisu  Electric     NaN    405  60      45       70   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    460       69       95     36           4      False  
    461       94       50     66           4      False  
    462       30       42     70           4      False  
    463       80      102     40           4      False  
    464       45       90     95           4      False  
           #      Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    465  418    Buizel  Water     NaN    330  55      65       35       60   
    466  419  Floatzel  Water     NaN    495  85     105       55       85   
    467  420   Cherubi  Grass     NaN    275  45      35       45       62   
    468  421   Cherrim  Grass     NaN    450  70      60       70       87   
    469  422   Shellos  Water     NaN    325  76      48       48       57   
    
         Sp. Def  Speed  Generation  Legendary  
    465       30     85           4      False  
    466       50    115           4      False  
    467       53     35           4      False  
    468       78     85           4      False  
    469       62     34           4      False  
           #       Name  Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    470  423  Gastrodon   Water  Ground    475  111      83       68       92   
    471  424    Ambipom  Normal     NaN    482   75     100       66       60   
    472  425   Drifloon   Ghost  Flying    348   90      50       34       60   
    473  426   Drifblim   Ghost  Flying    498  150      80       44       90   
    474  427    Buneary  Normal     NaN    350   55      66       44       44   
    
         Sp. Def  Speed  Generation  Legendary  
    470       82     39           4      False  
    471       66    115           4      False  
    472       44     70           4      False  
    473       54     80           4      False  
    474       56     85           4      False  
           #                 Name  Type 1    Type 2  Total   HP  Attack  Defense  \
    475  428              Lopunny  Normal       NaN    480   65      76       84   
    476  428  LopunnyMega Lopunny  Normal  Fighting    580   65     136       94   
    477  429            Mismagius   Ghost       NaN    495   60      60       60   
    478  430            Honchkrow    Dark    Flying    505  100     125       52   
    479  431              Glameow  Normal       NaN    310   49      55       42   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    475       54       96    105           4      False  
    476       54       96    135           4      False  
    477      105      105    105           4      False  
    478      105       52     71           4      False  
    479       42       37     85           4      False  
           #       Name   Type 1   Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    480  432    Purugly   Normal      NaN    452   71      82       64       64   
    481  433  Chingling  Psychic      NaN    285   45      30       50       65   
    482  434     Stunky   Poison     Dark    329   63      63       47       41   
    483  435   Skuntank   Poison     Dark    479  103      93       67       71   
    484  436    Bronzor    Steel  Psychic    300   57      24       86       24   
    
         Sp. Def  Speed  Generation  Legendary  
    480       59    112           4      False  
    481       50     45           4      False  
    482       41     74           4      False  
    483       61     84           4      False  
    484       86     23           4      False  
           #      Name   Type 1   Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    485  437  Bronzong    Steel  Psychic    500   67      89      116       79   
    486  438    Bonsly     Rock      NaN    290   50      80       95       10   
    487  439  Mime Jr.  Psychic    Fairy    310   20      25       45       70   
    488  440   Happiny   Normal      NaN    220  100       5        5       15   
    489  441    Chatot   Normal   Flying    411   76      65       45       92   
    
         Sp. Def  Speed  Generation  Legendary  
    485      116     33           4      False  
    486       45     10           4      False  
    487       90     60           4      False  
    488       65     30           4      False  
    489       42     91           4      False  
           #                   Name  Type 1  Type 2  Total   HP  Attack  Defense  \
    490  442              Spiritomb   Ghost    Dark    485   50      92      108   
    491  443                  Gible  Dragon  Ground    300   58      70       45   
    492  444                 Gabite  Dragon  Ground    410   68      90       65   
    493  445               Garchomp  Dragon  Ground    600  108     130       95   
    494  445  GarchompMega Garchomp  Dragon  Ground    700  108     170      115   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    490       92      108     35           4      False  
    491       40       45     42           4      False  
    492       50       55     82           4      False  
    493       80       85    102           4      False  
    494      120       95     92           4      False  
           #                 Name    Type 1 Type 2  Total   HP  Attack  Defense  \
    495  446             Munchlax    Normal    NaN    390  135      85       40   
    496  447                Riolu  Fighting    NaN    285   40      70       40   
    497  448              Lucario  Fighting  Steel    525   70     110       70   
    498  448  LucarioMega Lucario  Fighting  Steel    625   70     145       88   
    499  449           Hippopotas    Ground    NaN    330   68      72       78   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    495       40       85      5           4      False  
    496       35       40     60           4      False  
    497      115       70     90           4      False  
    498      140       70    112           4      False  
    499       38       42     32           4      False  
           #       Name  Type 1    Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    500  450  Hippowdon  Ground       NaN    525  108     112      118       68   
    501  451    Skorupi  Poison       Bug    330   40      50       90       30   
    502  452    Drapion  Poison      Dark    500   70      90      110       60   
    503  453   Croagunk  Poison  Fighting    300   48      61       40       61   
    504  454  Toxicroak  Poison  Fighting    490   83     106       65       86   
    
         Sp. Def  Speed  Generation  Legendary  
    500       72     47           4      False  
    501       55     65           4      False  
    502       75     95           4      False  
    503       40     50           4      False  
    504       65     85           4      False  
           #       Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    505  455  Carnivine  Grass     NaN    454  74     100       72       90   
    506  456    Finneon  Water     NaN    330  49      49       56       49   
    507  457   Lumineon  Water     NaN    460  69      69       76       69   
    508  458    Mantyke  Water  Flying    345  45      20       50       60   
    509  459     Snover  Grass     Ice    334  60      62       50       62   
    
         Sp. Def  Speed  Generation  Legendary  
    505       72     46           4      False  
    506       61     66           4      False  
    507       86     91           4      False  
    508      120     50           4      False  
    509       60     40           4      False  
           #                     Name    Type 1 Type 2  Total   HP  Attack  \
    510  460                Abomasnow     Grass    Ice    494   90      92   
    511  460  AbomasnowMega Abomasnow     Grass    Ice    594   90     132   
    512  461                  Weavile      Dark    Ice    510   70     120   
    513  462                Magnezone  Electric  Steel    535   70      70   
    514  463               Lickilicky    Normal    NaN    515  110      85   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    510       75       92       85     60           4      False  
    511      105      132      105     30           4      False  
    512       65       45       85    125           4      False  
    513      115      130       90     60           4      False  
    514       95       80       95     50           4      False  
           #        Name    Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    515  464   Rhyperior    Ground    Rock    535  115     140      130       55   
    516  465   Tangrowth     Grass     NaN    535  100     100      125      110   
    517  466  Electivire  Electric     NaN    540   75     123       67       95   
    518  467   Magmortar      Fire     NaN    540   75      95       67      125   
    519  468    Togekiss     Fairy  Flying    545   85      50       95      120   
    
         Sp. Def  Speed  Generation  Legendary  
    515       55     40           4      False  
    516       50     50           4      False  
    517       85     95           4      False  
    518       95     83           4      False  
    519      115     80           4      False  
           #       Name  Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    520  469    Yanmega     Bug  Flying    515   86      76       86      116   
    521  470    Leafeon   Grass     NaN    525   65     110      130       60   
    522  471    Glaceon     Ice     NaN    525   65      60      110      130   
    523  472    Gliscor  Ground  Flying    510   75      95      125       45   
    524  473  Mamoswine     Ice  Ground    530  110     130       80       70   
    
         Sp. Def  Speed  Generation  Legendary  
    520       56     95           4      False  
    521       65     95           4      False  
    522       95     65           4      False  
    523       75     95           4      False  
    524       60     80           4      False  
           #                 Name   Type 1    Type 2  Total  HP  Attack  Defense  \
    525  474            Porygon-Z   Normal       NaN    535  85      80       70   
    526  475              Gallade  Psychic  Fighting    518  68     125       65   
    527  475  GalladeMega Gallade  Psychic  Fighting    618  68     165       95   
    528  476            Probopass     Rock     Steel    525  60      55      145   
    529  477             Dusknoir    Ghost       NaN    525  45     100      135   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    525      135       75     90           4      False  
    526       65      115     80           4      False  
    527       65      115    110           4      False  
    528       75      150     40           4      False  
    529       65      135     45           4      False  
           #              Name    Type 1 Type 2  Total  HP  Attack  Defense  \
    530  478          Froslass       Ice  Ghost    480  70      80       70   
    531  479             Rotom  Electric  Ghost    440  50      50       77   
    532  479   RotomHeat Rotom  Electric   Fire    520  50      65      107   
    533  479   RotomWash Rotom  Electric  Water    520  50      65      107   
    534  479  RotomFrost Rotom  Electric    Ice    520  50      65      107   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    530       80       70    110           4      False  
    531       95       77     91           4      False  
    532      105      107     86           4      False  
    533      105      107     86           4      False  
    534      105      107     86           4      False  
           #            Name    Type 1  Type 2  Total  HP  Attack  Defense  \
    535  479  RotomFan Rotom  Electric  Flying    520  50      65      107   
    536  479  RotomMow Rotom  Electric   Grass    520  50      65      107   
    537  480            Uxie   Psychic     NaN    580  75      75      130   
    538  481         Mesprit   Psychic     NaN    580  80     105      105   
    539  482           Azelf   Psychic     NaN    580  75     125       70   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    535      105      107     86           4      False  
    536      105      107     86           4      False  
    537       75      130     95           4       True  
    538      105      105     80           4       True  
    539      125       70    115           4       True  
           #                   Name  Type 1  Type 2  Total   HP  Attack  Defense  \
    540  483                 Dialga   Steel  Dragon    680  100     120      120   
    541  484                 Palkia   Water  Dragon    680   90     120      100   
    542  485                Heatran    Fire   Steel    600   91      90      106   
    543  486              Regigigas  Normal     NaN    670  110     160      110   
    544  487  GiratinaAltered Forme   Ghost  Dragon    680  150     100      120   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    540      150      100     90           4       True  
    541      150      120    100           4       True  
    542      130      106     77           4       True  
    543       80      110    100           4       True  
    544      100      120     90           4       True  
           #                  Name   Type 1  Type 2  Total   HP  Attack  Defense  \
    545  487  GiratinaOrigin Forme    Ghost  Dragon    680  150     120      100   
    546  488             Cresselia  Psychic     NaN    600  120      70      120   
    547  489                Phione    Water     NaN    480   80      80       80   
    548  490               Manaphy    Water     NaN    600  100     100      100   
    549  491               Darkrai     Dark     NaN    600   70      90       90   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    545      120      100     90           4       True  
    546       75      130     85           4      False  
    547       80       80     80           4      False  
    548      100      100    100           4      False  
    549      135       90    125           4       True  
           #               Name   Type 1  Type 2  Total   HP  Attack  Defense  \
    550  492  ShayminLand Forme    Grass     NaN    600  100     100      100   
    551  492   ShayminSky Forme    Grass  Flying    600  100     103       75   
    552  493             Arceus   Normal     NaN    720  120     120      120   
    553  494            Victini  Psychic    Fire    600  100     100      100   
    554  495              Snivy    Grass     NaN    308   45      45       55   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    550      100      100    100           4       True  
    551      120       75    127           4       True  
    552      120      120    120           4       True  
    553      100      100    100           5       True  
    554       45       55     63           5      False  
           #       Name Type 1    Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    555  496    Servine  Grass       NaN    413   60      60       75       60   
    556  497  Serperior  Grass       NaN    528   75      75       95       75   
    557  498      Tepig   Fire       NaN    308   65      63       45       45   
    558  499    Pignite   Fire  Fighting    418   90      93       55       70   
    559  500     Emboar   Fire  Fighting    528  110     123       65      100   
    
         Sp. Def  Speed  Generation  Legendary  
    555       75     83           5      False  
    556       95    113           5      False  
    557       45     45           5      False  
    558       55     55           5      False  
    559       65     65           5      False  
           #      Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    560  501  Oshawott   Water     NaN    308  55      55       45       63   
    561  502    Dewott   Water     NaN    413  75      75       60       83   
    562  503  Samurott   Water     NaN    528  95     100       85      108   
    563  504    Patrat  Normal     NaN    255  45      55       39       35   
    564  505   Watchog  Normal     NaN    420  60      85       69       60   
    
         Sp. Def  Speed  Generation  Legendary  
    560       45     45           5      False  
    561       60     60           5      False  
    562       70     70           5      False  
    563       39     42           5      False  
    564       69     77           5      False  
           #       Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    565  506   Lillipup  Normal     NaN    275  45      60       45       25   
    566  507    Herdier  Normal     NaN    370  65      80       65       35   
    567  508  Stoutland  Normal     NaN    500  85     110       90       45   
    568  509   Purrloin    Dark     NaN    281  41      50       37       50   
    569  510    Liepard    Dark     NaN    446  64      88       50       88   
    
         Sp. Def  Speed  Generation  Legendary  
    565       45     55           5      False  
    566       65     60           5      False  
    567       90     80           5      False  
    568       37     66           5      False  
    569       50    106           5      False  
           #      Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    570  511   Pansage  Grass     NaN    316  50      53       48       53   
    571  512  Simisage  Grass     NaN    498  75      98       63       98   
    572  513   Pansear   Fire     NaN    316  50      53       48       53   
    573  514  Simisear   Fire     NaN    498  75      98       63       98   
    574  515   Panpour  Water     NaN    316  50      53       48       53   
    
         Sp. Def  Speed  Generation  Legendary  
    570       48     64           5      False  
    571       63    101           5      False  
    572       48     64           5      False  
    573       63    101           5      False  
    574       48     64           5      False  
           #       Name   Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    575  516   Simipour    Water     NaN    498   75      98       63       98   
    576  517      Munna  Psychic     NaN    292   76      25       45       67   
    577  518   Musharna  Psychic     NaN    487  116      55       85      107   
    578  519     Pidove   Normal  Flying    264   50      55       50       36   
    579  520  Tranquill   Normal  Flying    358   62      77       62       50   
    
         Sp. Def  Speed  Generation  Legendary  
    575       63    101           5      False  
    576       55     24           5      False  
    577       95     29           5      False  
    578       30     43           5      False  
    579       42     65           5      False  
           #        Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    580  521    Unfezant    Normal  Flying    488  80     115       80       65   
    581  522     Blitzle  Electric     NaN    295  45      60       32       50   
    582  523   Zebstrika  Electric     NaN    497  75     100       63       80   
    583  524  Roggenrola      Rock     NaN    280  55      75       85       25   
    584  525     Boldore      Rock     NaN    390  70     105      105       50   
    
         Sp. Def  Speed  Generation  Legendary  
    580       55     93           5      False  
    581       32     76           5      False  
    582       63    116           5      False  
    583       25     15           5      False  
    584       40     20           5      False  
           #       Name   Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    585  526   Gigalith     Rock     NaN    515   85     135      130       60   
    586  527     Woobat  Psychic  Flying    313   55      45       43       55   
    587  528    Swoobat  Psychic  Flying    425   67      57       55       77   
    588  529    Drilbur   Ground     NaN    328   60      85       40       30   
    589  530  Excadrill   Ground   Steel    508  110     135       60       50   
    
         Sp. Def  Speed  Generation  Legendary  
    585       80     25           5      False  
    586       43     72           5      False  
    587       55    114           5      False  
    588       45     68           5      False  
    589       65     88           5      False  
           #               Name    Type 1 Type 2  Total   HP  Attack  Defense  \
    590  531             Audino    Normal    NaN    445  103      60       86   
    591  531  AudinoMega Audino    Normal  Fairy    545  103      60      126   
    592  532            Timburr  Fighting    NaN    305   75      80       55   
    593  533            Gurdurr  Fighting    NaN    405   85     105       85   
    594  534         Conkeldurr  Fighting    NaN    505  105     140       95   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    590       60       86     50           5      False  
    591       80      126     50           5      False  
    592       25       35     35           5      False  
    593       40       50     40           5      False  
    594       55       65     45           5      False  
           #        Name    Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    595  535     Tympole     Water     NaN    294   50      50       40       50   
    596  536   Palpitoad     Water  Ground    384   75      65       55       65   
    597  537  Seismitoad     Water  Ground    509  105      95       75       85   
    598  538       Throh  Fighting     NaN    465  120     100       85       30   
    599  539        Sawk  Fighting     NaN    465   75     125       75       30   
    
         Sp. Def  Speed  Generation  Legendary  
    595       40     64           5      False  
    596       55     69           5      False  
    597       75     74           5      False  
    598       85     45           5      False  
    599       75     85           5      False  
           #        Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    600  540    Sewaddle    Bug   Grass    310  45      53       70       40   
    601  541    Swadloon    Bug   Grass    380  55      63       90       50   
    602  542    Leavanny    Bug   Grass    500  75     103       80       70   
    603  543    Venipede    Bug  Poison    260  30      45       59       30   
    604  544  Whirlipede    Bug  Poison    360  40      55       99       40   
    
         Sp. Def  Speed  Generation  Legendary  
    600       60     42           5      False  
    601       80     42           5      False  
    602       80     92           5      False  
    603       39     57           5      False  
    604       79     47           5      False  
           #        Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    605  545   Scolipede    Bug  Poison    485  60     100       89       55   
    606  546    Cottonee  Grass   Fairy    280  40      27       60       37   
    607  547  Whimsicott  Grass   Fairy    480  60      67       85       77   
    608  548     Petilil  Grass     NaN    280  45      35       50       70   
    609  549   Lilligant  Grass     NaN    480  70      60       75      110   
    
         Sp. Def  Speed  Generation  Legendary  
    605       69    112           5      False  
    606       50     66           5      False  
    607       75    116           5      False  
    608       50     30           5      False  
    609       75     90           5      False  
           #        Name  Type 1 Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    610  550    Basculin   Water    NaN    460  70      92       65       80   
    611  551     Sandile  Ground   Dark    292  50      72       35       35   
    612  552    Krokorok  Ground   Dark    351  60      82       45       45   
    613  553  Krookodile  Ground   Dark    519  95     117       80       65   
    614  554    Darumaka    Fire    NaN    315  70      90       45       15   
    
         Sp. Def  Speed  Generation  Legendary  
    610       55     98           5      False  
    611       35     65           5      False  
    612       45     74           5      False  
    613       70     92           5      False  
    614       45     50           5      False  
           #                     Name Type 1   Type 2  Total   HP  Attack  \
    615  555  DarmanitanStandard Mode   Fire      NaN    480  105     140   
    616  555       DarmanitanZen Mode   Fire  Psychic    540  105      30   
    617  556                 Maractus  Grass      NaN    461   75      86   
    618  557                  Dwebble    Bug     Rock    325   50      65   
    619  558                  Crustle    Bug     Rock    475   70      95   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    615       55       30       55     95           5      False  
    616      105      140      105     55           5      False  
    617       67      106       67     60           5      False  
    618       85       35       35     55           5      False  
    619      125       65       75     45           5      False  
           #        Name   Type 1    Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    620  559     Scraggy     Dark  Fighting    348  50      75       70       35   
    621  560     Scrafty     Dark  Fighting    488  65      90      115       45   
    622  561    Sigilyph  Psychic    Flying    490  72      58       80      103   
    623  562      Yamask    Ghost       NaN    303  38      30       85       55   
    624  563  Cofagrigus    Ghost       NaN    483  58      50      145       95   
    
         Sp. Def  Speed  Generation  Legendary  
    620       70     48           5      False  
    621      115     58           5      False  
    622       80     97           5      False  
    623       65     30           5      False  
    624      105     30           5      False  
           #        Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    625  564    Tirtouga   Water    Rock    355  54      78      103       53   
    626  565  Carracosta   Water    Rock    495  74     108      133       83   
    627  566      Archen    Rock  Flying    401  55     112       45       74   
    628  567    Archeops    Rock  Flying    567  75     140       65      112   
    629  568    Trubbish  Poison     NaN    329  50      50       62       40   
    
         Sp. Def  Speed  Generation  Legendary  
    625       45     22           5      False  
    626       65     32           5      False  
    627       45     70           5      False  
    628       65    110           5      False  
    629       62     65           5      False  
           #      Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    630  569  Garbodor  Poison     NaN    474  80      95       82       60   
    631  570     Zorua    Dark     NaN    330  40      65       40       80   
    632  571   Zoroark    Dark     NaN    510  60     105       60      120   
    633  572  Minccino  Normal     NaN    300  55      50       40       40   
    634  573  Cinccino  Normal     NaN    470  75      95       60       65   
    
         Sp. Def  Speed  Generation  Legendary  
    630       82     75           5      False  
    631       40     65           5      False  
    632       60    105           5      False  
    633       40     75           5      False  
    634       60    115           5      False  
           #        Name   Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    635  574     Gothita  Psychic     NaN    290  45      30       50       55   
    636  575   Gothorita  Psychic     NaN    390  60      45       70       75   
    637  576  Gothitelle  Psychic     NaN    490  70      55       95       95   
    638  577     Solosis  Psychic     NaN    290  45      30       40      105   
    639  578     Duosion  Psychic     NaN    370  65      40       50      125   
    
         Sp. Def  Speed  Generation  Legendary  
    635       65     45           5      False  
    636       85     55           5      False  
    637      110     65           5      False  
    638       50     20           5      False  
    639       60     30           5      False  
           #       Name   Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    640  579  Reuniclus  Psychic     NaN    490  110      65       75      125   
    641  580   Ducklett    Water  Flying    305   62      44       50       44   
    642  581     Swanna    Water  Flying    473   75      87       63       87   
    643  582  Vanillite      Ice     NaN    305   36      50       50       65   
    644  583  Vanillish      Ice     NaN    395   51      65       65       80   
    
         Sp. Def  Speed  Generation  Legendary  
    640       85     30           5      False  
    641       50     55           5      False  
    642       63     98           5      False  
    643       60     44           5      False  
    644       75     59           5      False  
           #        Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    645  584   Vanilluxe       Ice     NaN    535  71      95       85      110   
    646  585    Deerling    Normal   Grass    335  60      60       50       40   
    647  586    Sawsbuck    Normal   Grass    475  80     100       70       60   
    648  587      Emolga  Electric  Flying    428  55      75       60       75   
    649  588  Karrablast       Bug     NaN    315  50      75       45       40   
    
         Sp. Def  Speed  Generation  Legendary  
    645       95     79           5      False  
    646       50     75           5      False  
    647       70     95           5      False  
    648       60    103           5      False  
    649       45     60           5      False  
           #        Name Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    650  589  Escavalier    Bug   Steel    495   70     135      105       60   
    651  590     Foongus  Grass  Poison    294   69      55       45       55   
    652  591   Amoonguss  Grass  Poison    464  114      85       70       85   
    653  592    Frillish  Water   Ghost    335   55      40       50       65   
    654  593   Jellicent  Water   Ghost    480  100      60       70       85   
    
         Sp. Def  Speed  Generation  Legendary  
    650      105     20           5      False  
    651       55     15           5      False  
    652       80     30           5      False  
    653       85     40           5      False  
    654      105     60           5      False  
           #        Name Type 1    Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    655  594   Alomomola  Water       NaN    470  165      75       80       40   
    656  595      Joltik    Bug  Electric    319   50      47       50       57   
    657  596  Galvantula    Bug  Electric    472   70      77       60       97   
    658  597   Ferroseed  Grass     Steel    305   44      50       91       24   
    659  598  Ferrothorn  Grass     Steel    489   74      94      131       54   
    
         Sp. Def  Speed  Generation  Legendary  
    655       45     65           5      False  
    656       50     65           5      False  
    657       60    108           5      False  
    658       86     10           5      False  
    659      116     20           5      False  
           #       Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    660  599      Klink     Steel     NaN    300  40      55       70       45   
    661  600      Klang     Steel     NaN    440  60      80       95       70   
    662  601  Klinklang     Steel     NaN    520  60     100      115       70   
    663  602     Tynamo  Electric     NaN    275  35      55       40       45   
    664  603  Eelektrik  Electric     NaN    405  65      85       70       75   
    
         Sp. Def  Speed  Generation  Legendary  
    660       60     30           5      False  
    661       85     50           5      False  
    662       85     90           5      False  
    663       40     60           5      False  
    664       70     40           5      False  
           #        Name    Type 1 Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    665  604  Eelektross  Electric    NaN    515  85     115       80      105   
    666  605      Elgyem   Psychic    NaN    335  55      55       55       85   
    667  606    Beheeyem   Psychic    NaN    485  75      75       75      125   
    668  607     Litwick     Ghost   Fire    275  50      30       55       65   
    669  608     Lampent     Ghost   Fire    370  60      40       60       95   
    
         Sp. Def  Speed  Generation  Legendary  
    665       80     50           5      False  
    666       55     30           5      False  
    667       95     40           5      False  
    668       55     20           5      False  
    669       60     55           5      False  
           #        Name  Type 1 Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    670  609  Chandelure   Ghost   Fire    520  60      55       90      145   
    671  610        Axew  Dragon    NaN    320  46      87       60       30   
    672  611     Fraxure  Dragon    NaN    410  66     117       70       40   
    673  612     Haxorus  Dragon    NaN    540  76     147       90       60   
    674  613     Cubchoo     Ice    NaN    305  55      70       40       60   
    
         Sp. Def  Speed  Generation  Legendary  
    670       90     80           5      False  
    671       40     57           5      False  
    672       50     67           5      False  
    673       70     97           5      False  
    674       40     40           5      False  
           #       Name  Type 1    Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    675  614    Beartic     Ice       NaN    485   95     110       80       70   
    676  615  Cryogonal     Ice       NaN    485   70      50       30       95   
    677  616    Shelmet     Bug       NaN    305   50      40       85       40   
    678  617   Accelgor     Bug       NaN    495   80      70       40      100   
    679  618   Stunfisk  Ground  Electric    471  109      66       84       81   
    
         Sp. Def  Speed  Generation  Legendary  
    675       80     50           5      False  
    676      135    105           5      False  
    677       65     25           5      False  
    678       60    145           5      False  
    679       99     32           5      False  
           #       Name    Type 1 Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    680  619    Mienfoo  Fighting    NaN    350  45      85       50       55   
    681  620   Mienshao  Fighting    NaN    510  65     125       60       95   
    682  621  Druddigon    Dragon    NaN    485  77     120       90       60   
    683  622     Golett    Ground  Ghost    303  59      74       50       35   
    684  623     Golurk    Ground  Ghost    483  89     124       80       55   
    
         Sp. Def  Speed  Generation  Legendary  
    680       50     65           5      False  
    681       60    105           5      False  
    682       90     48           5      False  
    683       50     35           5      False  
    684       80     55           5      False  
           #        Name  Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    685  624    Pawniard    Dark   Steel    340   45      85       70       40   
    686  625     Bisharp    Dark   Steel    490   65     125      100       60   
    687  626  Bouffalant  Normal     NaN    490   95     110       95       40   
    688  627     Rufflet  Normal  Flying    350   70      83       50       37   
    689  628    Braviary  Normal  Flying    510  100     123       75       57   
    
         Sp. Def  Speed  Generation  Legendary  
    685       40     60           5      False  
    686       70     70           5      False  
    687       95     55           5      False  
    688       50     60           5      False  
    689       75     80           5      False  
           #       Name Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    690  629    Vullaby   Dark  Flying    370   70      55       75       45   
    691  630  Mandibuzz   Dark  Flying    510  110      65      105       55   
    692  631    Heatmor   Fire     NaN    484   85      97       66      105   
    693  632     Durant    Bug   Steel    484   58     109      112       48   
    694  633      Deino   Dark  Dragon    300   52      65       50       45   
    
         Sp. Def  Speed  Generation  Legendary  
    690       65     60           5      False  
    691       95     80           5      False  
    692       66     65           5      False  
    693       48    109           5      False  
    694       50     38           5      False  
           #       Name Type 1    Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    695  634   Zweilous   Dark    Dragon    420  72      85       70       65   
    696  635  Hydreigon   Dark    Dragon    600  92     105       90      125   
    697  636   Larvesta    Bug      Fire    360  55      85       55       50   
    698  637  Volcarona    Bug      Fire    550  85      60       65      135   
    699  638   Cobalion  Steel  Fighting    580  91      90      129       90   
    
         Sp. Def  Speed  Generation  Legendary  
    695       70     58           5      False  
    696       90     98           5      False  
    697       55     60           5      False  
    698      105    100           5      False  
    699       72    108           5       True  
           #                      Name    Type 1    Type 2  Total  HP  Attack  \
    700  639                 Terrakion      Rock  Fighting    580  91     129   
    701  640                  Virizion     Grass  Fighting    580  91      90   
    702  641   TornadusIncarnate Forme    Flying       NaN    580  79     115   
    703  641     TornadusTherian Forme    Flying       NaN    580  79     100   
    704  642  ThundurusIncarnate Forme  Electric    Flying    580  79     115   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    700       90       72       90    108           5       True  
    701       72       90      129    108           5       True  
    702       70      125       80    111           5       True  
    703       80      110       90    121           5       True  
    704       70      125       80    111           5       True  
           #                     Name    Type 1    Type 2  Total   HP  Attack  \
    705  642   ThundurusTherian Forme  Electric    Flying    580   79     105   
    706  643                 Reshiram    Dragon      Fire    680  100     120   
    707  644                   Zekrom    Dragon  Electric    680  100     150   
    708  645  LandorusIncarnate Forme    Ground    Flying    600   89     125   
    709  645    LandorusTherian Forme    Ground    Flying    600   89     145   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    705       70      145       80    101           5       True  
    706      100      150      120     90           5       True  
    707      120      120      100     90           5       True  
    708       90      115       80    101           5       True  
    709       90      105       80     91           5       True  
           #                  Name  Type 1    Type 2  Total   HP  Attack  Defense  \
    710  646                Kyurem  Dragon       Ice    660  125     130       90   
    711  646    KyuremBlack Kyurem  Dragon       Ice    700  125     170      100   
    712  646    KyuremWhite Kyurem  Dragon       Ice    700  125     120       90   
    713  647  KeldeoOrdinary Forme   Water  Fighting    580   91      72       90   
    714  647  KeldeoResolute Forme   Water  Fighting    580   91      72       90   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    710      130       90     95           5       True  
    711      120       90     95           5       True  
    712      170      100     95           5       True  
    713      129       90    108           5      False  
    714      129       90    108           5      False  
           #                     Name  Type 1    Type 2  Total   HP  Attack  \
    715  648       MeloettaAria Forme  Normal   Psychic    600  100      77   
    716  648  MeloettaPirouette Forme  Normal  Fighting    600  100     128   
    717  649                 Genesect     Bug     Steel    600   71     120   
    718  650                  Chespin   Grass       NaN    313   56      61   
    719  651                Quilladin   Grass       NaN    405   61      78   
    
         Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    715       77      128      128     90           5      False  
    716       90       77       77    128           5      False  
    717       95      120       95     99           5      False  
    718       65       48       45     38           6      False  
    719       95       56       58     57           6      False  
           #        Name Type 1    Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    720  652  Chesnaught  Grass  Fighting    530  88     107      122       74   
    721  653    Fennekin   Fire       NaN    307  40      45       40       62   
    722  654     Braixen   Fire       NaN    409  59      59       58       90   
    723  655     Delphox   Fire   Psychic    534  75      69       72      114   
    724  656     Froakie  Water       NaN    314  41      56       40       62   
    
         Sp. Def  Speed  Generation  Legendary  
    720       75     64           6      False  
    721       60     60           6      False  
    722       70     73           6      False  
    723      100    104           6      False  
    724       44     71           6      False  
           #        Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    725  657   Frogadier   Water     NaN    405  54      63       52       83   
    726  658    Greninja   Water    Dark    530  72      95       67      103   
    727  659    Bunnelby  Normal     NaN    237  38      36       38       32   
    728  660   Diggersby  Normal  Ground    423  85      56       77       50   
    729  661  Fletchling  Normal  Flying    278  45      50       43       40   
    
         Sp. Def  Speed  Generation  Legendary  
    725       56     97           6      False  
    726       71    122           6      False  
    727       36     57           6      False  
    728       77     78           6      False  
    729       38     62           6      False  
           #         Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    730  662  Fletchinder   Fire  Flying    382  62      73       55       56   
    731  663   Talonflame   Fire  Flying    499  78      81       71       74   
    732  664   Scatterbug    Bug     NaN    200  38      35       40       27   
    733  665       Spewpa    Bug     NaN    213  45      22       60       27   
    734  666     Vivillon    Bug  Flying    411  80      52       50       90   
    
         Sp. Def  Speed  Generation  Legendary  
    730       52     84           6      False  
    731       69    126           6      False  
    732       25     35           6      False  
    733       30     29           6      False  
    734       50     89           6      False  
           #     Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    735  667   Litleo   Fire  Normal    369  62      50       58       73   
    736  668   Pyroar   Fire  Normal    507  86      68       72      109   
    737  669  Flabébé  Fairy     NaN    303  44      38       39       61   
    738  670  Floette  Fairy     NaN    371  54      45       47       75   
    739  671  Florges  Fairy     NaN    552  78      65       68      112   
    
         Sp. Def  Speed  Generation  Legendary  
    735       54     72           6      False  
    736       66    106           6      False  
    737       79     42           6      False  
    738       98     52           6      False  
    739      154     75           6      False  
           #     Name    Type 1 Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    740  672   Skiddo     Grass    NaN    350   66      65       48       62   
    741  673   Gogoat     Grass    NaN    531  123     100       62       97   
    742  674  Pancham  Fighting    NaN    348   67      82       62       46   
    743  675  Pangoro  Fighting   Dark    495   95     124       78       69   
    744  676  Furfrou    Normal    NaN    472   75      80       60       65   
    
         Sp. Def  Speed  Generation  Legendary  
    740       57     52           6      False  
    741       81     68           6      False  
    742       48     43           6      False  
    743       71     58           6      False  
    744       90    102           6      False  
           #            Name   Type 1 Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    745  677          Espurr  Psychic    NaN    355  62      48       54       63   
    746  678    MeowsticMale  Psychic    NaN    466  74      48       76       83   
    747  678  MeowsticFemale  Psychic    NaN    466  74      48       76       83   
    748  679         Honedge    Steel  Ghost    325  45      80      100       35   
    749  680        Doublade    Steel  Ghost    448  59     110      150       45   
    
         Sp. Def  Speed  Generation  Legendary  
    745       60     68           6      False  
    746       81    104           6      False  
    747       81    104           6      False  
    748       37     28           6      False  
    749       49     35           6      False  
           #                   Name Type 1 Type 2  Total   HP  Attack  Defense  \
    750  681   AegislashBlade Forme  Steel  Ghost    520   60     150       50   
    751  681  AegislashShield Forme  Steel  Ghost    520   60      50      150   
    752  682               Spritzee  Fairy    NaN    341   78      52       60   
    753  683             Aromatisse  Fairy    NaN    462  101      72       72   
    754  684                Swirlix  Fairy    NaN    341   62      48       66   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    750      150       50     60           6      False  
    751       50      150     60           6      False  
    752       63       65     23           6      False  
    753       99       89     29           6      False  
    754       59       57     49           6      False  
           #        Name Type 1   Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    755  685    Slurpuff  Fairy      NaN    480  82      80       86       85   
    756  686       Inkay   Dark  Psychic    288  53      54       53       37   
    757  687     Malamar   Dark  Psychic    482  86      92       88       68   
    758  688     Binacle   Rock    Water    306  42      52       67       39   
    759  689  Barbaracle   Rock    Water    500  72     105      115       54   
    
         Sp. Def  Speed  Generation  Legendary  
    755       75     72           6      False  
    756       46     45           6      False  
    757       75     73           6      False  
    758       56     50           6      False  
    759       86     68           6      False  
           #        Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    760  690      Skrelp    Poison   Water    320  50      60       60       60   
    761  691    Dragalge    Poison  Dragon    494  65      75       90       97   
    762  692   Clauncher     Water     NaN    330  50      53       62       58   
    763  693   Clawitzer     Water     NaN    500  71      73       88      120   
    764  694  Helioptile  Electric  Normal    289  44      38       33       61   
    
         Sp. Def  Speed  Generation  Legendary  
    760       60     30           6      False  
    761      123     44           6      False  
    762       63     44           6      False  
    763       89     59           6      False  
    764       43     70           6      False  
           #       Name    Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  \
    765  695  Heliolisk  Electric  Normal    481   62      55       52      109   
    766  696     Tyrunt      Rock  Dragon    362   58      89       77       45   
    767  697  Tyrantrum      Rock  Dragon    521   82     121      119       69   
    768  698     Amaura      Rock     Ice    362   77      59       50       67   
    769  699    Aurorus      Rock     Ice    521  123      77       72       99   
    
         Sp. Def  Speed  Generation  Legendary  
    765       94    109           6      False  
    766       45     48           6      False  
    767       59     71           6      False  
    768       63     46           6      False  
    769       92     58           6      False  
           #      Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    770  700   Sylveon     Fairy     NaN    525  95      65       65      110   
    771  701  Hawlucha  Fighting  Flying    500  78      92       75       74   
    772  702   Dedenne  Electric   Fairy    431  67      58       57       81   
    773  703   Carbink      Rock   Fairy    500  50      50      150       50   
    774  704     Goomy    Dragon     NaN    300  45      50       35       55   
    
         Sp. Def  Speed  Generation  Legendary  
    770      130     60           6      False  
    771       63    118           6      False  
    772       67    101           6      False  
    773      150     50           6      False  
    774       75     40           6      False  
           #       Name  Type 1 Type 2  Total  HP  Attack  Defense  Sp. Atk  \
    775  705    Sliggoo  Dragon    NaN    452  68      75       53       83   
    776  706     Goodra  Dragon    NaN    600  90     100       70      110   
    777  707     Klefki   Steel  Fairy    470  57      80       91       80   
    778  708   Phantump   Ghost  Grass    309  43      70       48       50   
    779  709  Trevenant   Ghost  Grass    474  85     110       76       65   
    
         Sp. Def  Speed  Generation  Legendary  
    775      113     60           6      False  
    776      150     80           6      False  
    777       87     75           6      False  
    778       60     38           6      False  
    779       82     56           6      False  
           #                   Name Type 1 Type 2  Total  HP  Attack  Defense  \
    780  710  PumpkabooAverage Size  Ghost  Grass    335  49      66       70   
    781  710    PumpkabooSmall Size  Ghost  Grass    335  44      66       70   
    782  710    PumpkabooLarge Size  Ghost  Grass    335  54      66       70   
    783  710    PumpkabooSuper Size  Ghost  Grass    335  59      66       70   
    784  711  GourgeistAverage Size  Ghost  Grass    494  65      90      122   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    780       44       55     51           6      False  
    781       44       55     56           6      False  
    782       44       55     46           6      False  
    783       44       55     41           6      False  
    784       58       75     84           6      False  
           #                 Name Type 1 Type 2  Total  HP  Attack  Defense  \
    785  711  GourgeistSmall Size  Ghost  Grass    494  55      85      122   
    786  711  GourgeistLarge Size  Ghost  Grass    494  75      95      122   
    787  711  GourgeistSuper Size  Ghost  Grass    494  85     100      122   
    788  712             Bergmite    Ice    NaN    304  55      69       85   
    789  713              Avalugg    Ice    NaN    514  95     117      184   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    785       58       75     99           6      False  
    786       58       75     69           6      False  
    787       58       75     54           6      False  
    788       32       35     28           6      False  
    789       44       46     28           6      False  
           #              Name  Type 1  Type 2  Total   HP  Attack  Defense  \
    790  714            Noibat  Flying  Dragon    245   40      30       35   
    791  715           Noivern  Flying  Dragon    535   85      70       80   
    792  716           Xerneas   Fairy     NaN    680  126     131       95   
    793  717           Yveltal    Dark  Flying    680  126     131       95   
    794  718  Zygarde50% Forme  Dragon  Ground    600  108     100      121   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    790       45       40     55           6      False  
    791       97       80    123           6      False  
    792      131       98     99           6       True  
    793      131       98     99           6       True  
    794       81       95     95           6       True  
           #                 Name   Type 1 Type 2  Total  HP  Attack  Defense  \
    795  719              Diancie     Rock  Fairy    600  50     100      150   
    796  719  DiancieMega Diancie     Rock  Fairy    700  50     160      110   
    797  720  HoopaHoopa Confined  Psychic  Ghost    600  80     110       60   
    798  720   HoopaHoopa Unbound  Psychic   Dark    680  80     160       60   
    799  721            Volcanion     Fire  Water    600  80     110      120   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    795      100      150     50           6       True  
    796      160      110    110           6       True  
    797      150      130     70           6       True  
    798      170      130     80           6       True  
    799      130       90     70           6       True  
    


```python

```
