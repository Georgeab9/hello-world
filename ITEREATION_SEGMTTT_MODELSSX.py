Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import math
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> df=pd.read_excel('/Users/georgeabouassi/Desktop/Online Retail.xlsx')
>>> pd.set_option('display.max_columns', None)
>>> pd.set_option('display.width', 1000)
>>> df.head(7)
  InvoiceNo StockCode                          Description  Quantity         InvoiceDate  UnitPrice  CustomerID         Country
0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6 2010-12-01 08:26:00       2.55     17850.0  United Kingdom
1    536365     71053                  WHITE METAL LANTERN         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom
2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8 2010-12-01 08:26:00       2.75     17850.0  United Kingdom
3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom
4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom
5    536365     22752         SET 7 BABUSHKA NESTING BOXES         2 2010-12-01 08:26:00       7.65     17850.0  United Kingdom
6    536365     21730    GLASS STAR FROSTED T-LIGHT HOLDER         6 2010-12-01 08:26:00       4.25     17850.0  United Kingdom
>>> df.shape
(541909, 8)
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 541909 entries, 0 to 541908
Data columns (total 8 columns):
 #   Column       Non-Null Count   Dtype         
---  ------       --------------   -----         
 0   InvoiceNo    541909 non-null  object        
 1   StockCode    541909 non-null  object        
 2   Description  540455 non-null  object        
 3   Quantity     541909 non-null  int64         
 4   InvoiceDate  541909 non-null  datetime64[ns]
 5   UnitPrice    541909 non-null  float64       
 6   CustomerID   406829 non-null  float64       
 7   Country      541909 non-null  object        
dtypes: datetime64[ns](1), float64(2), int64(1), object(4)
memory usage: 33.1+ MB
>>> df.describe()
            Quantity      UnitPrice     CustomerID
count  541909.000000  541909.000000  406829.000000
mean        9.552250       4.611114   15287.690570
std       218.081158      96.759853    1713.600303
min    -80995.000000  -11062.060000   12346.000000
25%         1.000000       1.250000   13953.000000
50%         3.000000       2.080000   15152.000000
75%        10.000000       4.130000   16791.000000
max     80995.000000   38970.000000   18287.000000
>>> df.skew()
Quantity       -0.264076
UnitPrice     186.506972
CustomerID      0.029835
dtype: float64
>>> df.kurt()
Quantity      119769.160031
UnitPrice      59005.719097
CustomerID        -1.179982
dtype: float64
>>> distincts = df.apply(lambda x: x.unique().shape[0])
>>> >>> print(distincts)
SyntaxError: invalid syntax
>>> print(distincts)
InvoiceNo      25900
StockCode       4070
Description     4224
Quantity         722
InvoiceDate    23260
UnitPrice       1630
CustomerID      4373
Country           38
dtype: int64
>>> # from the above we recognize x problems in data: a) Price and Qtty have <0 values  b) CustomerID and Description have x NaN values   c) StockCode and Descr not =
>>> df[(df.Quantity < 0) & (df.UnitPrice <0)].shape[0]==0
True
>>> df[(df.Quantity <=0) & (df.UnitPrice <=0)].shape[0]==0
False
>>> df[(df.Quantity <=0) & (df.UnitPrice <=0)].shape[0]
1336
>>> # 1336 rows where Qtty and Price and <=0
>>> df.query('Quantity<=0 & UnitPrice<=0')
       InvoiceNo StockCode Description  Quantity         InvoiceDate  UnitPrice  CustomerID         Country
2406      536589     21777         NaN       -10 2010-12-01 16:50:00        0.0         NaN  United Kingdom
4347      536764    84952C         NaN       -38 2010-12-02 14:42:00        0.0         NaN  United Kingdom
7188      536996     22712         NaN       -20 2010-12-03 15:30:00        0.0         NaN  United Kingdom
7189      536997     22028         NaN       -20 2010-12-03 15:30:00        0.0         NaN  United Kingdom
7190      536998     85067         NaN        -6 2010-12-03 15:30:00        0.0         NaN  United Kingdom
...          ...       ...         ...       ...                 ...        ...         ...             ...
535333    581210     23395       check       -26 2011-12-07 18:36:00        0.0         NaN  United Kingdom
535335    581212     22578        lost     -1050 2011-12-07 18:38:00        0.0         NaN  United Kingdom
535336    581213     22576       check       -30 2011-12-07 18:38:00        0.0         NaN  United Kingdom
536908    581226     23090     missing      -338 2011-12-08 09:56:00        0.0         NaN  United Kingdom
538919    581422     23169     smashed      -235 2011-12-08 15:24:00        0.0         NaN  United Kingdom

[1336 rows x 8 columns]
>>> df.loc[(df.Quantity <=0) & (df.UnitPrice <=0), ['CustomerID']].CustomerID.unique()
array([nan])
>>> # Qtty<=0 and Price<=0 at CustomerId = NaN
>>> df.query('Quantity<0 & CustomerID.notna()')
       InvoiceNo StockCode                       Description  Quantity         InvoiceDate  UnitPrice  CustomerID         Country
141      C536379         D                          Discount        -1 2010-12-01 09:41:00      27.50     14527.0  United Kingdom
154      C536383    35004C   SET OF 3 COLOURED  FLYING DUCKS        -1 2010-12-01 09:49:00       4.65     15311.0  United Kingdom
235      C536391     22556    PLASTERS IN TIN CIRCUS PARADE        -12 2010-12-01 10:24:00       1.65     17548.0  United Kingdom
236      C536391     21984  PACK OF 12 PINK PAISLEY TISSUES        -24 2010-12-01 10:24:00       0.29     17548.0  United Kingdom
237      C536391     21983  PACK OF 12 BLUE PAISLEY TISSUES        -24 2010-12-01 10:24:00       0.29     17548.0  United Kingdom
...          ...       ...                               ...       ...                 ...        ...         ...             ...
540449   C581490     23144   ZINC T-LIGHT HOLDER STARS SMALL       -11 2011-12-09 09:57:00       0.83     14397.0  United Kingdom
541541   C581499         M                            Manual        -1 2011-12-09 10:28:00     224.69     15498.0  United Kingdom
541715   C581568     21258        VICTORIAN SEWING BOX LARGE        -5 2011-12-09 11:57:00      10.95     15311.0  United Kingdom
541716   C581569     84978  HANGING HEART JAR T-LIGHT HOLDER        -1 2011-12-09 11:58:00       1.25     17315.0  United Kingdom
541717   C581569     20979     36 PENCILS TUBE RED RETROSPOT        -5 2011-12-09 11:58:00       1.25     17315.0  United Kingdom

[8905 rows x 8 columns]
>>> # All invoices where Qtty <0 and ID notna start with letter C
>>> (df[(df.UnitPrice < 0)]).head()
       InvoiceNo StockCode      Description  Quantity         InvoiceDate  UnitPrice  CustomerID         Country
299983   A563186         B  Adjust bad debt         1 2011-08-12 14:51:00  -11062.06         NaN  United Kingdom
299984   A563187         B  Adjust bad debt         1 2011-08-12 14:52:00  -11062.06         NaN  United Kingdom
>>> (df[(df.UnitPrice < 0)]).head(5)
       InvoiceNo StockCode      Description  Quantity         InvoiceDate  UnitPrice  CustomerID         Country
299983   A563186         B  Adjust bad debt         1 2011-08-12 14:51:00  -11062.06         NaN  United Kingdom
299984   A563187         B  Adjust bad debt         1 2011-08-12 14:52:00  -11062.06         NaN  United Kingdom
>>> # only 2 invoices have <0 Price
>>> df[(df.UnitPrice==0)  & ~(df.CustomerID.isnull())]     # Invoices with price=0 and customer ID not null
       InvoiceNo StockCode                          Description  Quantity         InvoiceDate  UnitPrice  CustomerID         Country
9302      537197     22841         ROUND CAKE TIN VINTAGE GREEN         1 2010-12-05 14:02:00        0.0     12647.0         Germany
33576     539263     22580         ADVENT CALENDAR GINGHAM SACK         4 2010-12-16 14:36:00        0.0     16560.0  United Kingdom
40089     539722     22423             REGENCY CAKESTAND 3 TIER        10 2010-12-21 13:45:00        0.0     14911.0            EIRE
47068     540372     22090              PAPER BUNTING RETROSPOT        24 2011-01-06 16:41:00        0.0     13081.0  United Kingdom
47070     540372     22553               PLASTERS IN TIN SKULLS        24 2011-01-06 16:41:00        0.0     13081.0  United Kingdom
56674     541109     22168        ORGANISER WOOD ANTIQUE WHITE          1 2011-01-13 15:10:00        0.0     15107.0  United Kingdom
86789     543599    84535B         FAIRY CAKES NOTEBOOK A6 SIZE        16 2011-02-10 13:08:00        0.0     17560.0  United Kingdom
130188    547417     22062  CERAMIC BOWL WITH LOVE HEART DESIGN        36 2011-03-23 10:25:00        0.0     13239.0  United Kingdom
139453    548318     22055   MINI CAKE STAND  HANGING STRAWBERY         5 2011-03-30 12:45:00        0.0     13113.0  United Kingdom
145208    548871     22162          HEART GARLAND RUSTIC PADDED         2 2011-04-04 14:42:00        0.0     14410.0  United Kingdom
157042    550188     22636   CHILDS BREAKFAST SET CIRCUS PARADE         1 2011-04-14 18:57:00        0.0     12457.0     Switzerland
187613    553000     47566                        PARTY BUNTING         4 2011-05-12 15:21:00        0.0     17667.0  United Kingdom
198383    554037     22619            SET OF 6 SOLDIER SKITTLES        80 2011-05-20 14:13:00        0.0     12415.0       Australia
279324    561284     22167           OVAL WALL MIRROR DIAMANTE          1 2011-07-26 12:24:00        0.0     16818.0  United Kingdom
282912    561669     22960             JAM MAKING SET WITH JARS        11 2011-07-28 17:09:00        0.0     12507.0           Spain
285657    561916         M                               Manual         1 2011-08-01 11:44:00        0.0     15581.0  United Kingdom
298054    562973     23157           SET OF 6 NATIVITY MAGNETS        240 2011-08-11 11:42:00        0.0     14911.0            EIRE
314745    564651     23270     SET OF 2 CERAMIC PAINTED HEARTS         96 2011-08-26 14:19:00        0.0     14646.0     Netherlands
314746    564651     23268  SET OF 2 CERAMIC CHRISTMAS REINDEER       192 2011-08-26 14:19:00        0.0     14646.0     Netherlands
314747    564651     22955             36 FOIL STAR CAKE CASES        144 2011-08-26 14:19:00        0.0     14646.0     Netherlands
314748    564651     21786                   POLKADOT RAIN HAT        144 2011-08-26 14:19:00        0.0     14646.0     Netherlands
358655    568158      PADS           PADS TO MATCH ALL CUSHIONS         1 2011-09-25 12:22:00        0.0     16133.0  United Kingdom
361825    568384         M                               Manual         1 2011-09-27 09:46:00        0.0     12748.0  United Kingdom
379913    569716     22778                   GLASS CLOCHE SMALL         2 2011-10-06 08:17:00        0.0     15804.0  United Kingdom
395529    571035         M                               Manual         1 2011-10-13 12:50:00        0.0     12446.0             RSA
420404    572893     21208          PASTEL COLOUR HONEYCOMB FAN         5 2011-10-26 14:36:00        0.0     18059.0  United Kingdom
436428    574138     23234        BISCUIT TIN VINTAGE CHRISTMAS       216 2011-11-03 11:26:00        0.0     12415.0       Australia
436597    574175     22065       CHRISTMAS PUDDING TRINKET POT         12 2011-11-03 11:47:00        0.0     14110.0  United Kingdom
436961    574252         M                               Manual         1 2011-11-03 13:24:00        0.0     12437.0          France
439361    574469     22385            JUMBO BAG SPACEBOY DESIGN        12 2011-11-04 11:55:00        0.0     12431.0       Australia
446125    574879     22625                   RED KITCHEN SCALES         2 2011-11-07 13:22:00        0.0     13014.0  United Kingdom
446793    574920     22899         CHILDREN'S APRON DOLLY GIRL          1 2011-11-07 16:34:00        0.0     13985.0  United Kingdom
446794    574920     23480       MINI LIGHTS WOODLAND MUSHROOMS         1 2011-11-07 16:34:00        0.0     13985.0  United Kingdom
454463    575579     22437        SET OF 9 BLACK SKULL BALLOONS        20 2011-11-10 11:49:00        0.0     13081.0  United Kingdom
454464    575579     22089        PAPER BUNTING VINTAGE PAISLEY        24 2011-11-10 11:49:00        0.0     13081.0  United Kingdom
479079    577129     22464          HANGING METAL HEART LANTERN         4 2011-11-17 19:52:00        0.0     15602.0  United Kingdom
479546    577168         M                               Manual         1 2011-11-18 10:42:00        0.0     12603.0         Germany
480649    577314     23407       SET OF 2 TRAYS HOME SWEET HOME         2 2011-11-18 13:23:00        0.0     12444.0          Norway
485985    577696         M                               Manual         1 2011-11-21 11:57:00        0.0     16406.0  United Kingdom
502122    578841     84826       ASSTD DESIGN 3D PAPER STICKERS     12540 2011-11-25 15:57:00        0.0     13256.0  United Kingdom
>>> df.query('CustomerID.isna()')
       InvoiceNo StockCode                      Description  Quantity         InvoiceDate  UnitPrice  CustomerID         Country
622       536414     22139                              NaN        56 2010-12-01 11:52:00       0.00         NaN  United Kingdom
1443      536544     21773  DECORATIVE ROSE BATHROOM BOTTLE         1 2010-12-01 14:32:00       2.51         NaN  United Kingdom
1444      536544     21774  DECORATIVE CATS BATHROOM BOTTLE         2 2010-12-01 14:32:00       2.51         NaN  United Kingdom
1445      536544     21786               POLKADOT RAIN HAT          4 2010-12-01 14:32:00       0.85         NaN  United Kingdom
1446      536544     21787            RAIN PONCHO RETROSPOT         2 2010-12-01 14:32:00       1.66         NaN  United Kingdom
...          ...       ...                              ...       ...                 ...        ...         ...             ...
541536    581498    85099B          JUMBO BAG RED RETROSPOT         5 2011-12-09 10:26:00       4.13         NaN  United Kingdom
541537    581498    85099C   JUMBO  BAG BAROQUE BLACK WHITE         4 2011-12-09 10:26:00       4.13         NaN  United Kingdom
541538    581498     85150    LADIES & GENTLEMEN METAL SIGN         1 2011-12-09 10:26:00       4.96         NaN  United Kingdom
541539    581498     85174                S/4 CACTI CANDLES         1 2011-12-09 10:26:00      10.79         NaN  United Kingdom
541540    581498       DOT                   DOTCOM POSTAGE         1 2011-12-09 10:26:00    1714.17         NaN  United Kingdom

[135080 rows x 8 columns]
>>> # There are no entries where Qtty and Price are <0 at the same time --> So no returns
>>> # There are entries where Qtty is negative and Price =0, however we have no CustomerId for these entries
>>> # so we can remove all entries with Qtty and Price <0 as well as entries with CustomerID.isna()
>>> df = df[~(df.CustomerID.isnull())]
>>> df= df[~(df.Quantity <0)]
>>> df = df[df.UnitPrice > 0]
>>> df.shape
(397884, 8)
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 397884 entries, 0 to 541908
Data columns (total 8 columns):
 #   Column       Non-Null Count   Dtype         
---  ------       --------------   -----         
 0   InvoiceNo    397884 non-null  object        
 1   StockCode    397884 non-null  object        
 2   Description  397884 non-null  object        
 3   Quantity     397884 non-null  int64         
 4   InvoiceDate  397884 non-null  datetime64[ns]
 5   UnitPrice    397884 non-null  float64       
 6   CustomerID   397884 non-null  float64       
 7   Country      397884 non-null  object        
dtypes: datetime64[ns](1), float64(2), int64(1), object(4)
memory usage: 27.3+ MB
>>> df.describe()
            Quantity      UnitPrice     CustomerID
count  397884.000000  397884.000000  397884.000000
mean       12.988238       3.116488   15294.423453
std       179.331775      22.097877    1713.141560
min         1.000000       0.001000   12346.000000
25%         2.000000       1.250000   13969.000000
50%         6.000000       1.950000   15159.000000
75%        12.000000       3.750000   16795.000000
max     80995.000000    8142.750000   18287.000000
>>> distincts = df.apply(lambda x: x.unique().shape[0])
>>> print(distincts)
InvoiceNo      18532
StockCode       3665
Description     3877
Quantity         301
InvoiceDate    17282
UnitPrice        440
CustomerID      4338
Country           37
dtype: int64
>>> # Description and StockCode are still not matching --> Description might have duplicates written in wrong format
>>> import datetime
>>> # check if there is 1 stockcode for multiple descriptions
>>> cat_des_df = df.groupby(["StockCode","Description"]).count().reset_index()
>>> cat_des_df.head()
  StockCode                   Description  InvoiceNo  Quantity  InvoiceDate  UnitPrice  CustomerID  Country
0     10002   INFLATABLE POLITICAL GLOBE          49        49           49         49          49       49
1     10080      GROOVY CACTUS INFLATABLE         21        21           21         21          21       21
2     10120                  DOGGY RUBBER         30        30           30         30          30       30
3     10125       MINI FUNKY DESIGN TAPES         64        64           64         64          64       64
4     10133  COLOURING PENCILS BROWN TUBE        124       124          124        124         124      124
>>> cat_des_df.head(7)
  StockCode                   Description  InvoiceNo  Quantity  InvoiceDate  UnitPrice  CustomerID  Country
0     10002   INFLATABLE POLITICAL GLOBE          49        49           49         49          49       49
1     10080      GROOVY CACTUS INFLATABLE         21        21           21         21          21       21
2     10120                  DOGGY RUBBER         30        30           30         30          30       30
3     10125       MINI FUNKY DESIGN TAPES         64        64           64         64          64       64
4     10133  COLOURING PENCILS BROWN TUBE        124       124          124        124         124      124
5     10135  COLOURING PENCILS BROWN TUBE        121       121          121        121         121      121
6     11001   ASSTD DESIGN RACING CAR PEN         64        64           64         64          64       64
>>> cat_des_df.StockCode.value_counts()[cat_des_df.StockCode.value_counts()>1].reset_index().head())
SyntaxError: unmatched ')'
>>> cat_des_df.StockCode.value_counts()[cat_des_df.StockCode.value_counts()>1].reset_index().head()
   index  StockCode
0  23236          4
1  23196          4
2  23240          3
3  22776          3
4  22937          3
>>> cat_des_df.StockCode.value_counts()[cat_des_df.StockCode.value_counts()>1].reset_index().head(7)
   index  StockCode
0  23236          4
1  23196          4
2  23240          3
3  22776          3
4  22937          3
5  23126          3
6  23413          3
>>> df[df['StockCode'] == cat_des_df.StockCode.value_counts()[cat_des_df.StockCode.value_counts()>1].reset_index()['index'][4]]['Description'].unique()
array(['BAKING MOULD CHOCOLATE CUPCAKES',
       'BAKING MOULD CHOCOLATE CUP CAKES',
       'BAKING MOULD CUPCAKE CHOCOLATE'], dtype=object)
>>> df[df['StockCode'] == cat_des_df.StockCode.value_counts()[cat_des_df.StockCode.value_counts()>1].reset_index()['index'][3]]['Description'].unique()
array(['SWEETHEART CAKESTAND 3 TIER', 'CAKESTAND, 3 TIER, LOVEHEART',
       'SWEETHEART 3 TIER CAKE STAND '], dtype=object)
>>> df[df['StockCode'] == cat_des_df.StockCode.value_counts()[cat_des_df.StockCode.value_counts()>1].reset_index()['index'][4]]['Description'].unique()
array(['BAKING MOULD CHOCOLATE CUPCAKES',
       'BAKING MOULD CHOCOLATE CUP CAKES',
       'BAKING MOULD CUPCAKE CHOCOLATE'], dtype=object)
>>> df[df['StockCode'] == cat_des_df.StockCode.value_counts()[cat_des_df.StockCode.value_counts()>1].reset_index()['index'][2]]['Description'].unique()
array(['SET OF 4 KNICK KNACK TINS DOILEY ',
       'SET OF 4 KNICK KNACK TINS DOILY ',
       'SET OF 4 KNICK KNACK TINS  DOILEY '], dtype=object)
>>> df[df['StockCode'] == cat_des_df.StockCode.value_counts()[cat_des_df.StockCode.value_counts()>1].reset_index()['index'][5]]['Description'].unique()
array(['DOLLCRAFT GIRL AMELIE KIT', 'FELTCRAFT GIRL AMELIE KIT',
       'DOLLCRAFT GIRL AMELIE'], dtype=object)
>>> # We can see that for the same item there are multiple descriptions
>>> unique_desc = df[["StockCode", "Description"]].groupby(by=["StockCode"]).apply(pd.DataFrame.mode).reset_index(drop=True)
>>> unique_desc.head()
  StockCode                   Description
0     10002   INFLATABLE POLITICAL GLOBE 
1     10080      GROOVY CACTUS INFLATABLE
2     10120                  DOGGY RUBBER
3     10125       MINI FUNKY DESIGN TAPES
4     10133  COLOURING PENCILS BROWN TUBE
>>> unique_desc.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3666 entries, 0 to 3665
Data columns (total 2 columns):
 #   Column       Non-Null Count  Dtype 
---  ------       --------------  ----- 
 0   StockCode    3665 non-null   object
 1   Description  3666 non-null   object
dtypes: object(2)
memory usage: 57.4+ KB
>>> unique_desc['Description'].duplicated()
0       False
1       False
2       False
3       False
4       False
        ...  
3661    False
3662    False
3663    False
3664    False
3665    False
Name: Description, Length: 3666, dtype: bool
>>> df['StockCode'].value_counts()
85123A    2035
22423     1723
85099B    1618
84879     1408
47566     1396
          ... 
90125E       1
90181A       1
90202A       1
90038C       1
85031C       1
Name: StockCode, Length: 3665, dtype: int64
>>> unique_desc['StockCode'].value_counts()
90108     1
21012     1
90042A    1
90003B    1
84952A    1
         ..
22570     1
22569     1
22568     1
22567     1
90114     1
Name: StockCode, Length: 3665, dtype: int64
>>> from pandasql import sqldf
>>> pysqldf = lambda q: sqldf(q, globals())
>>> q = '''
select df.InvoiceNo, df.StockCode, un.Description, df.Quantity, df.InvoiceDate,
       df.UnitPrice, df.CustomerID, df.Country
from df as df INNER JOIN 
     unique_desc as un on df.StockCode = un.StockCode
'''
>>> df['Description'].value_counts()
WHITE HANGING HEART T-LIGHT HOLDER    2028
REGENCY CAKESTAND 3 TIER              1723
JUMBO BAG RED RETROSPOT               1618
ASSORTED COLOUR BIRD ORNAMENT         1408
PARTY BUNTING                         1396
                                      ... 
TEA TIME BREAKFAST BASKET                1
HOT WATER BOTTLE BABUSHKA LARGE          1
PEG BAG APPLE DESIGN                     1
72 CAKE CASES VINTAGE CHRISTMAS          1
ENAMEL DINNER PLATE PANTRY               1
Name: Description, Length: 3877, dtype: int64
>>> unique_desc['Description'].value_counts()
METAL SIGN,CUPCAKE SINGLE HOOK        3
COLUMBIAN CANDLE ROUND                2
RETRO PLASTIC POLKA TRAY              2
RETRO PLASTIC DAISY TRAY              2
PINK FLOWERS RABBIT EASTER            2
                                     ..
WOOD 2 DRAWER CABINET WHITE FINISH    1
AMBER CHUNKY BEAD BRACELET W STRAP    1
CRYSTAL DIAMANTE EXPANDABLE RING      1
CAKE STAND LOVEBIRD 2 TIER WHITE      1
MINI JIGSAW BUNNIES                   1
Name: Description, Length: 3648, dtype: int64
>>> df = pysqldf(q)
>>> df['Description'].value_counts()
WHITE HANGING HEART T-LIGHT HOLDER    2035
REGENCY CAKESTAND 3 TIER              1723
JUMBO BAG RED RETROSPOT               1618
ASSORTED COLOUR BIRD ORNAMENT         1408
PARTY BUNTING                         1396
                                      ... 
SET OF 3 PINK FLYING DUCKS               1
WHITE WITH METAL BAG CHARM               1
FLOWER SHOP DESIGN MUG                   1
CROCHET DOG KEYRING                      1
PINK BAROQUE FLOCK CANDLE HOLDER         1
Name: Description, Length: 3647, dtype: int64
>>> df.InvoiceDate = pd.to_datetime(df.InvoiceDate)
>>> df['amount'] = df.Quantity * df.UnitPrice	# NEW COLUMNS WITH AMOUNT = QTTY x PRICE
>>> df.describe()
           InvoiceNo       Quantity      UnitPrice     CustomerID         amount
count  397884.000000  397884.000000  397884.000000  397884.000000  397884.000000
mean   560616.934451      12.988238       3.116488   15294.423453      22.397000
std     13106.117773     179.331775      22.097877    1713.141560     309.071041
min    536365.000000       1.000000       0.001000   12346.000000       0.001000
25%    549234.000000       2.000000       1.250000   13969.000000       4.680000
50%    561893.000000       6.000000       1.950000   15159.000000      11.800000
75%    572090.000000      12.000000       3.750000   16795.000000      19.800000
max    581587.000000   80995.000000    8142.750000   18287.000000  168469.600000
>>> df.CustomerID = df.CustomerID.astype('Int64')
>>> sns.set(style="ticks", color_codes=True, font_scale=1.5)
>>> color = sns.color_palette()
>>> sns.set_style('darkgrid')
>>> from mpl_toolkits.mplot3d import Axes3D
>>> import plotly as py
>>> import plotly.graph_objs as go

>>> # VISUALIZATION
>>> fig = plt.figure(figsize=(25, 7))
>>> f1 = fig.add_subplot(121)
>>> # PLOTING  AMOUNT SALES BY COUNTRY
>>> g = df.groupby(["Country"]).amount.sum().sort_values(ascending = False).plot(kind='bar', title='Amount Sales by Country')
>>> plt.show()
>>> import matplotlib.mlab as mlab
>>> import matplotlib.cm as cm
>>> fig = plt.figure(figsize=(25, 7))
>>> f1 = fig.add_subplot(121)
>>> g = df.groupby(["Country"]).amount.sum().sort_values(ascending = False).plot(kind='bar', title='Amount Sales by Country')
>>> plt.show()
>>> # GRAPH NEEDS TO BE ENHANCED
>>> f2 = fig.add_subplot(122)
>>> # PLOTTING % SALES BOTH INTERNAL (UK) AND GLOBAL
>>> market = df.groupby(["Internal"]).amount.sum().sort_values(ascending = False)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    market = df.groupby(["Internal"]).amount.sum().sort_values(ascending = False)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/frame.py", line 5801, in groupby
    return groupby_generic.DataFrameGroupBy(
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/groupby/groupby.py", line 403, in __init__
    grouper, exclusions, obj = get_grouper(
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/groupby/grouper.py", line 600, in get_grouper
    raise KeyError(gpr)
KeyError: 'Internal'
>>> df['Internal'] = df.Country.apply(lambda x: 'Yes' if x=='United Kingdom' else 'No' )
>>> market = df.groupby(["Internal"]).amount.sum().sort_values(ascending = False)
>>> g = plt.pie(market, labels=market.index, autopct='%1.1f%%', shadow=True, startangle=90)
>>> plt.title('Internal Market')
Text(0.5, 1.0, 'Internal Market')
>>> plt.show()
>>> # 82 % OF TOTAL SALES ARE INTERNAL FROM UK
>>> fig = plt.figure(figsize=(25, 7))
>>> # PLOTTING TOP 50 CUSTOMERS IN TOTAL SALES AMOUNT AND CHECKING WHAT % OF TOTAL SALES THESE 50 CUSTOMERS MAKE
>>> PercentSales =  np.round((df.groupby(["CustomerID"]).amount.sum().\   
                          sort_values(ascending = False)[:51].sum()/df.groupby(["CustomerID"]).\
                          amount.sum().sort_values(ascending = False).sum()) * 100, 2)
SyntaxError: unexpected character after line continuation character
>>> PercentSales =  np.round((df.groupby(["CustomerID"]).amount.sum().\sort_values(ascending = False)[:51].sum()/df.groupby(["CustomerID"]).amount.sum().sort_values(ascending = False).sum()) * 100, 2)
SyntaxError: unexpected character after line continuation character
>>> PercentSales =  np.round((df.groupby(["CustomerID"]).amount.sum().\sort_values(ascending = False)[:51].sum()/df.groupby(["CustomerID"]).amount.sum().sort_values(ascending = False).sum()) * 100, 2)
SyntaxError: unexpected character after line continuation character
>>> PercentSales =  np.round((df.groupby(["CustomerID"]).amount.sum().\
                          sort_values(ascending = False)[:51].sum()/df.groupby(["CustomerID"]).\
                          amount.sum().sort_values(ascending = False).sum()) * 100, 2)
>>> g = df.groupby(["CustomerID"]).amount.sum().sort_values(ascending = False)[:51].\
    plot(kind='bar', title='Top Customers: {:3.2f}% Sales Amount'.format(PercentSales))
>>> plt.show()
>>> # PLOTTING TOP 10 CUSTOMERS IN TOTAL SALES AND CHECKING WHAT % THESE 10 CUSTOMERS MAEK
>>> fig = plt.figure(figsize=(25, 7))
>>> f1 = fig.add_subplot(121)
>>> PercentSales =  np.round((df.groupby(["CustomerID"]).amount.sum().\
                          sort_values(ascending = False)[:10].sum()/df.groupby(["CustomerID"]).\
                          amount.sum().sort_values(ascending = False).sum()) * 100, 2)
>>> g = df.groupby(["CustomerID"]).amount.sum().sort_values(ascending = False)[:10]\
    .plot(kind='bar', title='Top 10 Customers: {:3.2f}% Sales Amont'.format(PercentSales))
>>> plt.show()
>>> plt.show()
>>> # TOP 10 CUSTOMERS MAKE 17.26% OF TOTAL SALES
>>> f1 = fig.add_subplot(122)
>>> # NOW PLOTTING TOP 10 CUSTOMERS IN TERMS OF NUMBERS OF PURCHASES AND THE % THEY REPRESENT
>>> PercentSales =  np.round((df.groupby(["CustomerID"]).amount.count().\
                          sort_values(ascending = False)[:10].sum()/df.groupby(["CustomerID"]).\
                          amount.count().sort_values(ascending = False).sum()) * 100, 2)
>>> g = df.groupby(["CustomerID"]).amount.count().sort_values(ascending = False)[:10].\
    plot(kind='bar', title='Top 10 Customers: {:3.2f}% Event Sales'.format(PercentSales))
>>> plt.show()
>>> # NOW LETS PLOT TOP PRODUCTS
>>> AmountSum = = df.groupby(["Description"]).amount.sum().sort_values(ascending = False)
SyntaxError: invalid syntax
>>> AmountSum =  df.groupby(["Description"]).amount.sum().sort_values(ascending = False)
>>> inv = df[["Description", "InvoiceNo"]].groupby(["Description"]).InvoiceNo.unique().agg(np.size).sort_values(ascending = False)
>>> fig = plt.figure(figsize=(25, 7))
>>> f1 = fig.add_subplot(121)
>>> Top10 = list(AmountSum[:10].index)
>>> PercentSales =  np.round((AmountSum[Top10].sum()/AmountSum.sum()) * 100, 2)
>>> PercentEvents = np.round((inv[Top10].sum()/inv.sum()) * 100, 2)
>>> g = AmoutSum[Top10].\
    plot(kind='bar', title='Top 10 Products in Sales Amount: {:3.2f}% of Amount and {:3.2f}% of Events'.format(PercentSales, PercentEvents))
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    g = AmoutSum[Top10].\
NameError: name 'AmoutSum' is not defined
>>> g = AmountSum[Top10].\
    plot(kind='bar', title='Top 10 Products in Sales Amount: {:3.2f}% of Amount and {:3.2f}% of Events'.format(PercentSales, PercentEvents))
>>> plt.show()
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/matplotlib/backends/backend_macosx.py", line 70, in _draw
    def _draw(self):
KeyboardInterrupt
>>> #TOP 10 PRODUCTS AMOUNT FOR 9.95% OF TOTAL SALES AND 2.68% OF TOTAL EVENTS
>>> #TOP 10 PRODUCTS IN SALES AMOUNT MAKE 9.95% OF TOTAL SALES AND 2.68% OF TOTAL EVENTS
>>> f1 = fig.add_subplot(122)
>>> Top10Ev = list(inv[:10].index)
>>> PercentSales =  np.round((AmountSum[Top10Ev].sum()/AmountSum.sum()) * 100, 2)
>>> PercentEvents = np.round((inv[Top10Ev].sum()/inv.sum()) * 100, 2)
>>> g = inv[Top10Ev].\
    plot(kind='bar', title='Events of top 10 most sold products: {:3.2f}% of Amount and {:3.2f}% of Events'.\
                       format(PercentSales, PercentEvents))
>>> plt.show()
>>> # TOP 10 PRODUCTS IN TERMS OF EVENTS (HOW MANY PURCHS) MAKE 7.28% OF TOTAL SALES AND 3.53% OF TOTAL EVENTS (PURCHS)
>>> fig = plt.figure(figsize=(25, 7))
>>> Top15ev = list(inv[:15].index)
>>> PercentSales =  np.round((AmoutSum[Top15ev].sum()/AmoutSum.sum()) * 100, 2)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    PercentSales =  np.round((AmoutSum[Top15ev].sum()/AmoutSum.sum()) * 100, 2)
NameError: name 'AmoutSum' is not defined
>>> PercentSales =  np.round((AmountSum[Top15ev].sum()/AmountSum.sum()) * 100, 2)
>>> PercentEvents = np.round((inv[Top15ev].sum()/inv.sum()) * 100, 2)
>>> g = AmountSum[Top15ev].sort_values(ascending = False).\
    plot(kind='bar', 
         title='Sales Amount of top 15 most sold products: {:3.2f}% of Amount and {:3.2f}% of Events'.\
         format(PercentSales, PercentEvents))
>>> plt.show()
>>> # TOP 15 MOST SOLD PDCTS MAKE 8.73% OF TOTAL AMOUNT AND 4.85% OF TOTAL EVENT
>>> fig = plt.figure(figsize=(25, 7))
>>> Top50 = list(AmoutSum[:50].index)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    Top50 = list(AmoutSum[:50].index)
NameError: name 'AmoutSum' is not defined
>>> Top50 = list(AmountSum[:50].index)
>>> PercentSales =  np.round((AmountSum[Top50].sum()/AmountSum.sum()) * 100, 2)
>>> PercentEvents = np.round((inv[Top50].sum()/inv.sum()) * 100, 2)
>>> g = AmountSum[Top50].\
    plot(kind='bar', 
         title='Top 50 Products in Sales Amount: {:3.2f}% of Amount and {:3.2f}% of Events'.\
         format(PercentSales, PercentEvents))
>>> plt.show()
>>> # TOP 50 PRODUCTS MAKE 22.98% of TOTAL AMOUNT AND 10.11% OF EVENTS
>>> fig = plt.figure(figsize=(25, 7))
>>> Top50Ev = list(inv[:50].index)
>>> PercentSales =  np.round((AmountSum[Top50Ev].sum()/AmountSum.sum()) * 100, 2)
>>> PercentEvents = np.round((inv[Top50Ev].sum()/inv.sum()) * 100, 2)
>>> g = inv[Top50Ev].\
    plot(kind='bar', title='Top 50 most sold products: {:3.2f}% of Amount and {:3.2f}% of Events'.\
                       format(PercentSales, PercentEvents))
>>> plt.show()
>>> # TOP 50 MOST SOLD PRODUCTS MAKE 17.19% OF TOTAL AMOUNT AND 12.37% OF EVENTS
>>> # FOR THIS SEGMENTATION PROBLEM, WE ONLY HAVE SALES RECORD (NO DEMOGRAPHICS, PERSONAL INFO...)   SO WE CAN USE RFM MODEL (RECENCY, FREQUENCY, MONETARY VALUE)
>>> # FOR RECENCY WE WILL ASSIGN A REFERENCE DATE (LAST TRANSACTION + 1 DAY) THEN CONSTRUCT RECENCY VAR AS AS NBR OF DAYS BEFORE REFRENCE DATE SINCE CUST MADE PURCHS
>>> refrence_date = df.InvoiceDate.max() + datetime.timedelta(days = 1)
>>> print('Reference Date:', refrence_date)
Reference Date: 2011-12-10 12:50:00
>>> df['days_since_last_purchase'] = (refrence_date - df.InvoiceDate).astype('timedelta64[D]')     # NEW COL FOR DAYS SINCE LAST PURCHS
>>> customer_history_df =  df[['CustomerID', 'days_since_last_purchase']].groupby("CustomerID").min().reset_index()
>>> customer_history_df.head()
   CustomerID  days_since_last_purchase
0       12346                     326.0
1       12347                       2.0
2       12348                      75.0
3       12349                      19.0
4       12350                     310.0
>>> customer_history_df.days_since_last_purchase.min()
1.0
>>> customer_history_df.loc[(customer_history_df.days_since_last_purchase.min()), ['days_since_last_purchase']].days_since_last_purchase
2.0
>>> customer_history_df.loc[(customer_history_df.days_since_last_purchase.min()), ['CustomerID']].CustomerID
12347.0
>>> customer_history_df.rename(columns={'days_since_last_purchase':'recency'}, inplace=True)
>>> customer_history_df.describe().transpose()
             count          mean          std      min       25%      50%       75%      max
CustomerID  4338.0  15300.408022  1721.808492  12346.0  13813.25  15299.5  16778.75  18287.0
recency     4338.0     92.536422   100.014169      1.0     18.00     51.0    142.00    374.0
>>> customer_history_df.loc[(customer_history_df.days_since_last_purchase == 2), ['CustomerID']].CustomerID
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    customer_history_df.loc[(customer_history_df.days_since_last_purchase == 2), ['CustomerID']].CustomerID
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pandas/core/generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'days_since_last_purchase'
>>> customer_history_df.loc[(customer_history_df.recency == 2), ['CustomerID']].CustomerID
1       12347
11      12358
75      12437
100     12471
177     12569
        ...  
4033    17870
4193    18092
4206    18109
4279    18210
4328    18273
Name: CustomerID, Length: 86, dtype: int64
>>> customer_history_df.loc[(customer_history_df.recency == 1), ['CustomerID']].CustomerID
61      12423
71      12433
137     12518
144     12526
258     12662
        ...  
3894    17675
3954    17754
3955    17757
4093    17949
4201    18102
Name: CustomerID, Length: 93, dtype: int64
>>> df.loc[(df.CustomerID==12423), ['Country']].Country
25320     Belgium
25321     Belgium
25322     Belgium
25323     Belgium
25324     Belgium
           ...   
397450    Belgium
397451    Belgium
397452    Belgium
397453    Belgium
397454    Belgium
Name: Country, Length: 125, dtype: object
>>> df.loc[(df.CustomerID==12423), ['Country']].Country.unique()
array(['Belgium'], dtype=object)
>>> from scipy.stats import skew, norm, probplot, boxcox
>>> from sklearn import preprocessing
>>> from sklearn.cluster import KMeans
>>> def QQ_plot(data, measure):
    fig = plt.figure(figsize=(20,7))

    #Get the fitted parameters used by the function
    (mu, sigma) = norm.fit(data)

    #Kernel Density plot
    fig1 = fig.add_subplot(121)
    sns.distplot(data, fit=norm)
    fig1.set_title(measure + ' Distribution ( mu = {:.2f} and sigma = {:.2f} )'.format(mu, sigma), loc='center')
    fig1.set_xlabel(measure)
    fig1.set_ylabel('Frequency')

    #QQ plot
    fig2 = fig.add_subplot(122)
    res = probplot(data, plot=fig2)
    fig2.set_title(measure + ' Probability Plot (skewness: {:.6f} and kurtosis: {:.6f} )'.format(data.skew(), data.kurt()), loc='center')

    plt.tight_layout()
    plt.show()

    
>>> QQ_plot(customer_history_df.recency, 'Recency')
>>> # From the first graph above we can see that sales recency distribution is skewed, has a peak on the left and a long tail to the right. It deviates from normal distribution and is positively biased.
From the Probability Plot, we could see that sales recency also does not align with the diagonal red line which represent normal distribution. The form of its distribution confirm that is a skewed right.   
SyntaxError: invalid syntax
>>> #From the first graph above we can see that sales recency distribution is skewed, has a peak on the left and a long tail to the right. It deviates from normal distribution and is positively biased.
#From the Probability Plot, we could see that sales recency also does not align with the diagonal red line which represent normal distribution. The form of its distribution confirm that is a skewed right.																		              # With skewness positive of 1.25, we confirm the lack of symmetry and indicate that sales recency are skewed right, as we can see too at the Sales Distribution plot, skewed right means that the right tail is long relative to the left tail. The skewness for a normal distribution is zero, and any symmetric data should have a skewness near zero. A distribution, or data set, is symmetric if it looks the same to the left and right of the center point.

# Kurtosis is a measure of whether the data are heavy-tailed or light-tailed relative to a normal distribution. That is, data sets with high kurtosis tend to have heavy tails, or outliers, and positive kurtosis indicates a heavy-tailed distribution and negative kurtosis indicates a light tailed distribution. So, with 0.43 of positive kurtosis sales recency are heavy-tailed and has some outliers.
>>> print('NOW FREQUENCY')
NOW FREQUENCY
>>> customer_freq = (df[['CustomerID', 'InvoiceNo']].groupby(["CustomerID", 'InvoiceNo']).count().reset_index()).\
                groupby(["CustomerID"]).count().reset_index()
>>> customer_freq.rename(columns={'InvoiceNo':'frequency'},inplace=True)
>>> customer_history_df = customer_history_df.merge(customer_freq)
>>> customer_history_df.head()
   CustomerID  recency  frequency
0       12346    326.0          1
1       12347      2.0          7
2       12348     75.0          4
3       12349     19.0          1
4       12350    310.0          1
>>> QQ_plot(customer_history_df.frequency, 'Frequency')
>>> #From the first graph above we can see that sales frequency distribution is skewed, has a peak on the left and a long tail to the right. It deviates from normal distribution and is positively biased.
>>> #From the Probability Plot, we could see that sales frequency also does **not align with the diagonal and confirm that is a skewed right.
>>> #With skewness positive of 12.1, we confirm the high lack of symmetry and with 249 Kurtosis indicates that is a heavy-tailed distribution and has outliers.
>>> print('NOW MONETARY VALUE')
NOW MONETARY VALUE
>>> customer_monetary_val = df[['CustomerID', 'amount']].groupby("CustomerID").sum().reset_index()
>>> customer_history_df = customer_history_df.merge(customer_monetary_val)
>>> customer_history_df.head()
   CustomerID  recency  frequency    amount
0       12346    326.0          1  77183.60
1       12347      2.0          7   4310.00
2       12348     75.0          4   1797.24
3       12349     19.0          1   1757.55
4       12350    310.0          1    334.40
>>> customer_history_df.loc[(customer_history_df.recency.min()) & (customer_history_df.frequency.max()) & (customer_history_df.amount.max()), ['CustomerID']].CustomerID.unique()
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    customer_history_df.loc[(customer_history_df.recency.min()) & (customer_history_df.frequency.max()) & (customer_history_df.amount.max()), ['CustomerID']].CustomerID.unique()
TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
>>> mask=(customer_history_df.recency.min()) & (customer_history_df.frequency.max()) & (customer_history_df.amount.max())
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    mask=(customer_history_df.recency.min()) & (customer_history_df.frequency.max()) & (customer_history_df.amount.max())
TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
>>> mask=(customer_history_df.recency.min()) & (customer_history_df.frequency.max())
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    mask=(customer_history_df.recency.min()) & (customer_history_df.frequency.max())
TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
>>> QQ_plot(customer_history_df.amount, 'Amount')
>>> #From the first graph above we can see that sales amount distribution is skewed, has a peak on the left and a long tail to the right. It deviates from normal distribution and is positively biased.
>>> #From the Probability Plot, we could see that sales amount also does not align with the diagonal, special on the right.
>>> With skewness positive of 19.3, we confirm the high lack of symmetry and with 478 Kurtosis indicates that is a too heavy-tailed distribution and has outliers, surely more than 10 very extreme.
SyntaxError: invalid syntax
>>> #With skewness positive of 19.3, we confirm the high lack of symmetry and with 478 Kurtosis indicates that is a too heavy-tailed distribution and has outliers, surely more than 10 very extreme.
>>> customer_history_df.describe()
         CustomerID      recency    frequency         amount
count   4338.000000  4338.000000  4338.000000    4338.000000
mean   15300.408022    92.536422     4.272015    2054.266460
std     1721.808492   100.014169     7.697998    8989.230441
min    12346.000000     1.000000     1.000000       3.750000
25%    13813.250000    18.000000     1.000000     307.415000
50%    15299.500000    51.000000     2.000000     674.485000
75%    16778.750000   142.000000     5.000000    1661.740000
max    18287.000000   374.000000   209.000000  280206.020000
>>> customer_history_df.recency.min()
1.0
>>> # Requirments of K-Means clustering: Mean centering  Mean centering of a variable value means that we will replace the actual value of the variable with a standardized value, so that the variable has a mean of 0 and variance of 1. This ensures that all the variables are in the same range and the difference in ranges of values doesn't cause the algorithm to not perform well. This is akin to feature scaling.
>>> # Other Requirements: huge range of values each variable can take. This problem is particularly noticeable for the monetary amount variable. To take care of this problem, we will transform all the variables on the log scale. This transformation, along with the standardization, will ensure that the input to our algorithm is a homogenous set of scaled and transformed values.
>>> # In our case, we will have the clustering results in terms of the log transformed and scaled variable. But to make inferences in terms of the original data, we will need to reverse transform all the variable so that we get back the actual RFM figures
>>> customer_history_df['recency_log'] = customer_history_df['recency'].apply(math.log)
>>> customer_history_df['frequency_log'] = customer_history_df['frequency'].apply(math.log)
>>> customer_history_df['amount_log'] = customer_history_df['amount'].apply(math.log)
>>> feature_vector = ['amount_log', 'recency_log','frequency_log']
>>> X_subset = customer_history_df[feature_vector]
>>> scaler = preprocessing.StandardScaler().fit(X_subset)
>>> X_scaled = scaler.transform(X_subset)
>>> pd.DataFrame(X_scaled, columns=X_subset.columns).describe().T
                count          mean       std       min       25%       50%       75%       max
amount_log     4338.0  6.551800e-18  1.000115 -4.179280 -0.684183 -0.060942  0.654244  4.721395
recency_log    4338.0 -1.048288e-16  1.000115 -2.630445 -0.612424  0.114707  0.829652  1.505796
frequency_log  4338.0 -9.991495e-17  1.000115 -1.048610 -1.048610 -0.279044  0.738267  4.882714
>>> fig = plt.figure(figsize=(20,14))
>>> f1 = fig.add_subplot(221); sns.regplot(x='recency', y='amount', data=customer_history_df,scatter_kws={"color": "blue"}, line_kws={"color": "red"})
<matplotlib.axes._subplots.AxesSubplot object at 0x7f97a1c5cc70>
>>> f1 = fig.add_subplot(222); sns.regplot(x='frequency', y='amount', data=customer_history_df)
<matplotlib.axes._subplots.AxesSubplot object at 0x7f97af9e8b50>
>>> f1 = fig.add_subplot(223); sns.regplot(x='recency_log', y='amount_log', data=customer_history_df)
<matplotlib.axes._subplots.AxesSubplot object at 0x7f97a28afac0>
>>> f1 = fig.add_subplot(224); sns.regplot(x='frequency_log', y='amount_log', data=customer_history_df, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
<matplotlib.axes._subplots.AxesSubplot object at 0x7f97b008eeb0>
>>> from mpl_toolkits.mplot3d import Axes3D
>>> fig = plt.figure(figsize=(15, 10))
>>> ax = fig.add_subplot(111, projection='3d')
>>> xs =customer_history_df.recency_log
>>> ys = customer_history_df.frequency_log
>>> zs = customer_history_df.amount_log
>>> ax.scatter(xs, ys, zs, s=5)
<mpl_toolkits.mplot3d.art3d.Path3DCollection object at 0x7f97a205aca0>
>>> ax.set_xlabel('Recency')
Text(0.5, 0, 'Recency')
>>> ax.set_ylabel('Frequency')
Text(0.5, 0, 'Frequency')
>>> ax.set_zlabel('Monetary')
Text(0.5, 0, 'Monetary')
>>> plt.show()
>>> #The obvious patterns we can see from the plots above is that costumers who buy with a higher frequency and more recency tend to spend more based on the increasing trend in Monetary (amount value) with a corresponding increasing and decreasing trend for Frequency and Recency, respectively.
>>> cl = 30  # number of clusters init
>>> for k in range (1, cl+1):
	model = KMeans(n_clusters=k, init='k-means++', n_init=10,max_iter=300,tol=1e-04,random_state=101)
	model=model.fit(X_scaled)
	labels=model.labels_
	interia = model.inertia_
	if (K_best == cl) and (((anterior - interia)/anterior) < corte):
		K_best = k - 1
		cost.append(interia)
		anterior = interia

		
Traceback (most recent call last):
  File "<pyshell#253>", line 6, in <module>
    if (K_best == cl) and (((anterior - interia)/anterior) < corte):
NameError: name 'K_best' is not defined
>>> K_best= cl
>>> corte = 0.1
>>> anterior = 100000000000000
>>> cost=[]
>>> for k in range (1, cl+1):
	model = KMeans(n_clusters=k, init='k-means++', n_init=10,max_iter=300,tol=1e-04,random_state=101)
	model=model.fit(X_scaled)
	labels=model.labels_
	interia = model.inertia_
	if (K_best == cl) and (((anterior - interia)/anterior) < corte):
		K_best = k - 1
		cost.append(interia)
		anterior = interia
plt.figure(figsize=(8, 6))
SyntaxError: invalid syntax
>>> for k in range (1, cl+1):
	model = KMeans(n_clusters=k, init='k-means++', n_init=10,max_iter=300,tol=1e-04,random_state=101)
	model=model.fit(X_scaled)
	labels=model.labels_
	interia = model.inertia_
	if (K_best == cl) and (((anterior - interia)/anterior) < corte):
		K_best = k - 1
		cost.append(interia)
		anterior = interia

		

plt.figure(figsize=(8, 6))
>>> plt.scatter(range (1, cl+1), cost, c='red')
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    plt.scatter(range (1, cl+1), cost, c='red')
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/matplotlib/pyplot.py", line 2811, in scatter
    __ret = gca().scatter(
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/matplotlib/__init__.py", line 1565, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/matplotlib/cbook/deprecation.py", line 358, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/matplotlib/axes/_axes.py", line 4380, in scatter
    raise ValueError("x and y must be the same size")
ValueError: x and y must be the same size
>>> cl = 50
>>> corte = 0.1
>>> anterior = 100000000000000
>>> cost = []
>>> K_best = cl
>>> for k in range (1, cl+1):
    # Create a kmeans model on our data, using k clusters.  random_state helps ensure that the algorithm returns the same results each time.
    model = KMeans(
        n_clusters=k, 
        init='k-means++', #'random',
        n_init=10,
        max_iter=300,
        tol=1e-04,
        random_state=101)

    model = model.fit(X_scaled)

    # These are our fitted labels for clusters -- the first cluster has label 0, and the second has label 1.
    labels = model.labels_
 
    # Sum of distances of samples to their closest cluster center
    interia = model.inertia_
    if (K_best == cl) and (((anterior - interia)/anterior) < corte): K_best = k - 1
    cost.append(interia)
    anterior = interia

plt.figure(figsize=(8, 6))
plt.scatter(range (1, cl+1), cost, c='red')
plt.show()
SyntaxError: invalid syntax
>>> for k in range (1, cl+1):
    # Create a kmeans model on our data, using k clusters.  random_state helps ensure that the algorithm returns the same results each time.
    model = KMeans(
        n_clusters=k, 
        init='k-means++', #'random',
        n_init=10,
        max_iter=300,
        tol=1e-04,
        random_state=101)

    model = model.fit(X_scaled)

    # These are our fitted labels for clusters -- the first cluster has label 0, and the second has label 1.
    labels = model.labels_
 
    # Sum of distances of samples to their closest cluster center
    interia = model.inertia_
    if (K_best == cl) and (((anterior - interia)/anterior) < corte): K_best = k - 1
    cost.append(interia)
    anterior = interia

    
>>> plt.figure()
<Figure size 640x480 with 0 Axes>
>>> plt.plot(range (1, cl+1), cost, c='red')
[<matplotlib.lines.Line2D object at 0x7f97a4041a30>]
>>> plt.show()
>>> plt.scatter(range (1, cl+1), cost, c='red')
<matplotlib.collections.PathCollection object at 0x7f97a10bbb80>
>>> plt.show()
>>> print('The best K sugest: ',K_best)
The best K sugest:  7
>>> model = KMeans(n_clusters=K_best, init='k-means++', n_init=10,max_iter=300, tol=1e-04, random_state=101)
>>> model = model.fit(X_scaled)
>>> labels = model.labels_
>>> fig = plt.figure(figsize=(20,5))
>>> ax = fig.add_subplot(121)
>>> plt.scatter(x = X_scaled[:,1], y = X_scaled[:,0], c=model.labels_.astype(float))
<matplotlib.collections.PathCollection object at 0x7f979d6c8250>
>>> ax.set_xlabel(feature_vector[1])
Text(0.5, 0, 'recency_log')
>>> ax.set_ylabel(feature_vector[0])
Text(0, 0.5, 'amount_log')
>>> ax = fig.add_subplot(122)
>>> plt.scatter(x = X_scaled[:,2], y = X_scaled[:,0], c=model.labels_.astype(float))
<matplotlib.collections.PathCollection object at 0x7f979db84190>
>>> ax.set_xlabel(feature_vector[2])
Text(0.5, 0, 'frequency_log')
>>> ax.set_ylabel(feature_vector[0])
Text(0, 0.5, 'amount_log')
>>> plt.show()
>>> 