target_id = [
  {   # 君悅
    'hotel_name':'GrandHyattTaipei',
    'hotels':120725,
    'booking':'grand-hyatt-taipei-taipei50',
    'agoda':736992
  },
  {   # 凱撒
    'hotel_name':'CaesarParkTaipei',
    'hotels':113094,
    'booking':'caesarpark-taipei',
    'agoda':1368
  },
  {   # 圓山
    'hotel_name':'GrandHotelTaipei',
    'hotels':143924,
    'booking':'grand-hotel-taipei',
    'agoda':1885
  },
  {   # 大倉久和
    'hotel_name':'OkuraPrestigeTaipei',
    'hotels':415060,
    'booking':'the-okura-prestige-taipei',
    'agoda':400142
  },
  {   # W
    'hotel_name':'W-Taipei',
    'hotels':369485,
    'booking':'w-taipei',
    'agoda':335043
  },
  {   # 晶華
    'hotel_name':'RegentTaipei',
    'hotels':121325,
    'booking':'the-regent-taipei',
    'agoda':5718
  },
  {   # 老爺
    'hotel_name':'RoyalNikkoTaipei',
    'hotels':126702,
    'booking':'royal-taipei',
    'agoda':8885
  },
  {   # 君品
    'hotel_name':'PalaisDeChineHotel',
    'hotels':352321,
    'booking':'palais-de-chine',
    'agoda':186460
  },
  {   # 香格里拉
    'hotel_name':'EasternPlazaHotelTaipei',
    'hotels':134169,
    'booking':'shangri-la-s-far-eastern-plaza-taipei',
    'agoda':7767
  },
  {   # 喜來登
    'hotel_name':'SheratonGrandTaipei',
    'hotels':105536,
    'booking':'sheraton-taipei',
    'agoda':149
  }
]
target_crawl = ['hotels','booking','agoda']

for crawl_ in target_crawl:
  for id in range(0,10):
    print (id)
    print (target_id[id][crawl_])
    print (target_id[id]['hotel_name'])