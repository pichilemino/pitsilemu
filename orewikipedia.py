# -*- coding: utf-8 -*-
mes={	"january":1,
	"february":2,
	"march":3,
	"april":4,
	"may":5,
	"june":6,
	"july":7,
	"august":8,
	"september":9,
	"october":10,
	"november":11,
	"december":12,
	}
i_mes={
	1:"january",
	2:"february",
	3:"march",
	4:"april",
	5:"may",
	6:"june",
	7:"july",
	8:"august",
	9:"september",
	10:"october",
	11:"november",
	12:"december",
	}

statuspage={"ca":"Estat","es":"Estado", "en":"Status"}

wikipro={
u"w" : "wikipedia",
u"wikipedia" : "wikipedia",
u"b" : "wikibooks",
u"wikibooks" : "wikibooks",
u"q" : "wikiquote",
u"wikiquote" : "wikiquote",
u"n" : "wikinews",
u"wikinews" : "wikinews",
u"s" : "wikisource",
u"wikisource" : "wikisource",
u"v" : "wikiversity",
u"wikiversity" : "wikiversity",
u"wikt" : "wiktionary",
u"wiktionary" : "wiktionary",
#Proyectos sin derivaciones idiomÃ¡ticas
u"m" : "meta",
u"meta" : "meta",
u"metawikipedia" : "meta",
u"commons" : "commons",
u"wikispecies" : "species",
u"incubator" : "incubator",
u"wmania" : "mania",
u"wikimedia" : "foundation",
u"foundation" : "foundation",
}

specialwikipro={
u"meta" : "meta.wikimedia.org",
u"commons" : "commons.wikimedia.org",
u"species" : "species.wikimedia.org",
u"incubator" : "incubator.wikimedia.org",
u"mania" : "wikimania.wikimedia.org",
u"foundation" : "wikimediafoundation.org",
}

"""
Especial:SiteMatrix
<tr><td><a id="(?P<cod>.*?)" name="(?P=cod)"></a><strong>(?P<idi>.*?)</strong></td><td><a href="http://(?P=cod).wikipedia.org/"(?P<w> class="new")?>(?P=cod)</a></td><td><a href="http://(?P=cod).wiktionary.org/"(?P<wikt> class="new")?>fy</a></td><td><a href="http://(?P=cod).wikibooks.org/"(?P<b> class="new")?>fy</a></td><td><a href="http://(?P=cod).wikinews.org/"(?P<n> class="new")?>fy</a></td><td><a href="http://(?P=cod).wikiquote.org/"(?P<q> class="new")?>fy</a></td><td><a href="http://(?P=cod).wikisource.org/"(?P<s> class="new")?>fy</a></td><td><a href="http://(?P=cod).wikiversity.org/"(?P<v> class="new")?>fy</a></td></tr><tr><td><a id="(?P<cod>.*?)" name="(?P=cod)"></a><strong>(?P<idi>.*?)</strong></td><td><a href="http://(?P=cod).wikinews.org/"(?P<w> class="new")?>(?P=cod)</a></td><td><a href="http://(?P=cod).wiktionary.org/"(?P<wikt> class="new")?>(?P=cod)</a></td><td><a href="http://(?P=cod).wikibooks.org/"(?P<b> class="new")?>(?P=cod)</a></td><td><a href="http://(?P=cod).wikinews.org/"(?P<n> class="new")?>(?P=cod)</a></td><td><a href="http://(?P=cod).wikiquote.org/"(?P<q> class="new")?>(?P=cod)</a></td><td><a href="http://(?P=cod).wikisource.org/"(?P<s> class="new")?>(?P=cod)</a></td><td><a href="http://(?P=cod).wikiversity.org/"(?P<v> class="new")?>(?P=cod)</a></td></tr>
"""
#a e i n o u
#Ã¡Ã©Ã­ Ã±Ã³Ãº
wikimap={
u"aa": u"Afar",
u"ab": u"Abkhaz",
u"ace": u"Aceh",
u"af": u"Afrikaans",
u"ak": u"Akan",
u"aln": u"Gegh Albanian",
u"als": u"Alemannic",
u"am": u"Amharic",
u"an": u"Aragonese",
u"ang": u"Old English",
u"ar": u"Arabic",
u"arc": u"Aramaic",
u"arn": u"Mapudungun or Araucanian",
u"arz": u"Egyptian Spoken Arabic",
u"as": u"Assamese",
u"ast": u"Asturian",
u"av": u"Avar",
u"avk": u"Kotava",
u"ay": u"Aymara",
u"az": u"Azerbaijani",
u"ba": u"Bashkir",
u"bar": u"Bavarian - Austro-Bavarian and South Tyrolean",
u"bat-smg": u"Samogitian",
u"bcc": u"Southern Balochi",
u"bcl": u"Bikol - Central Bicolano",
u"be": u"Belarusian normative",
u"be-tarask": u"Belarusian in Taraskievica orthography",
u"be-x-old": u"Belarusian in Taraskievica ortography, compat link",
u"bg": u"Bulgarian",
u"bh": u"Bhojpuri",
u"bi": u"Bislama",
u"bm": u"Bambara",
u"bn": u"Bengali",
u"bo": u"Tibetan",
u"bpy": u"Bishnupriya Manipuri",
u"bqi": u"Bakthiari",
u"br": u"Breton",
u"bs": u"Bosnian",
u"bug": u"Bugis",
u"bxr": u"Buryar (Russia)",
u"ca": u"Catalan",
u"cbk-zam": u"Chavacano de Zamboanga - Zamboanga Chavacano",
u"cdo": u"Min Dong",
u"ce": u"Chechen",
u"ceb": u"Cebuano",
u"ch": u"Chamorro",
u"cho": u"Choctaw",
u"chr": u"Cherokee",
u"chy": u"Cheyenne",
u"ckb": u"Sorani",
u"co": u"Corsican",
u"cr": u"Cree",
u"crh": u"Crimean Tatar",
u"cs": u"Czech",
u"csb": u"Cassubian",
u"cu": u"Old Church Slavonic (ancient language)",
u"cv": u"Chuvash",
u"cy": u"Welsh",
u"da": u"Danish",
u"de": u"German",
u"de-at": u"Austrian German",
u"de-ch": u"Swiss Standard German",
u"de-formal": u"Formal German (Sie-Form)",
u"diq": u"Zazaki",
u"dk": u"Danish",
u"dsb": u"Lower Sorbian",
u"dv": u"Dhivehi",
u"dz": u"Bhutani",
u"ee": u"Eeegbe",
u"el": u"Greek",
u"eml": u"Emiliano-Romagnolo / Sammarinese",
u"en": u"English",
u"en-gb": u"British English",
u"eo": u"Esperanto",
u"es": u"Spanish",
u"et": u"Estonian",
u"eu": u"Basque / Euskara",
u"ext": u"Extremaduran",
u"fa": u"Persian",
u"ff": u"Fulfulde / Maasina",
u"fi": u"Finnish",
u"fiu-vro": u"Viro",
u"fj": u"Fijian",
u"fo": u"Faroese",
u"fr": u"French",
u"frc": u"Cajun French",
u"frp": u"Arpitan / Franco-Provencal",
u"frr": u"North Frisian",
u"fur": u"Friulian",
u"fy": u"Frisian",
u"ga": u"Irish",
u"gag": u"Gagauz",
u"gan": u"Gan",
u"gan-hans": u"Gan (Simplified Han)",
u"gan-hant": u"Gan (Traditional Han)",
u"gd": u"Scots Gaelic",
u"gl": u"Galician",
u"glk": u"Gilaki",
u"gn": u"Guarani / Paraguayan",
u"got": u"Gothic",
u"grc": u"Ancient Greek",
u"gsw": u"Alemannic",
u"gu": u"Gujarati",
u"gv": u"Manx",
u"ha": u"Hausa",
u"hak": u"Hakka",
u"haw": u"Hawaiian",
u"he": u"Hebrew",
u"hi": u"Hindi",
u"hif": u"Fijian Hindi",
u"hif-deva": u"Fijian Hindi / Devangari",
u"hif-latn": u"Fijian Hindi",
u"hil": u"Hiligaynon / Ilonggo",
u"ho": u"Hiri Motu",
u"hr": u"Croatian",
u"hsb": u"Upper Sorbian",
u"ht" : u"Haitian Creole French",
u"hu": u"Hungarian",
u"hy": u"Armenian",
u"hz": u"Herero",
u"ia": u"Interlingua",
u"id": u"Indonesian",
u"ie": u"Interlingue",
u"ig": u"Igbo",
u"ii": u"Sichuan Yi",
u"ik": u"Inupiak / Inupiatun",
u"ike-cans": u"Inuktitut / Eastern Canadian / Eskimo",
u"ike-latn": u"inuktitut / Eastern Canadian (Latin script)",
u"ilo": u"Ilokano",
u"inh": u"Ingush",
u"io": u"Ido",
u"is": u"Icelandic",
u"it": u"Italian",
u"iu": u"Inuktitut",
u"ja": u"Japanese",
u"jbo": u"Lojban",
u"jut": u"Jutlandic",
u"jv": u"Javanese",
u"ka": u"Georgian",
u"kaa": u"Karakalpak / Qaraqalpaqsha",
u"kab": u"Kabyle",
u"kg": u"Kongo / KiKongo / KiKoongo",
u"ki": u"Gikuyu",
u"kiu": u"Kirmanjki",
u"kj": u"Kwanyama",
u"kk": u"Kazakh",
u"kk-arab": u"Kazakh Arabic",
u"kk-cyrl": u"Kazakh Cyrillic",
u"kk-latn": u"Kazakh Latin",
u"kk-cn": u"Kazakh (China)",
u"kk-kz": u"Kazakh (Kazakhstan)",
u"kk-tr": u"Kazakh (Turkey)",
u"kl": u"Kalaallisut / Kal",
u"km": u"Khmer, Central",
u"kn": u"Kannada",
u"ko": u"Korean",
u"ko-kp": u"Korean (DPRK)",
u"kr": u"Kanuri",
u"krc": u"Karachay-Balkar",
u"kri": u"Krio",
u"krj": u"Kinaray-a",
u"ks": u"Kashmiri",
u"ksh": u"Ripuarian",
u"ku" : u"Kurdish",
u"ku-latn": u"Northern Kurdish Latin script",
u"ku-arab": u"Northern Kurdish Arabic script",
u"kv": u"Komi-Zyrian",
u"kw": u"Kernowek",
u"ky": u"Kirghiz",
u"la": u"Latin",
u"lad": u"Ladino"
}
wikimap2={
u"lb": u"Luxemburguish",
u"lbe": u"Lak",
u"lez": u"Lezgi",
u"lfn": u"Lingua Franca Nova",
u"li": u"Limburgian",
u"lij": u"Ligurian",
u"lmo": u"Lombard",
u"ln": u"Lingala",
u"lo": u"Laotian",
u"loz": u"Lozi",
u"lt": u"Lithuanian",
u"lv": u"Latvian",
u"lzh": u"Literary Chinese",
u"mai": u"Maithili",
u"map-bms": u"Banyumasan",
u"mdf": u"Moksha",
u"mg": u"Malagasy",
u"mh": u"Ebon / Marshallese",
u"mhr": u"Eastern Mari",
u"mi": u"Maori",
u"mk": u"Macedonian",
u"ml": u"Malayalam",
u"mn": u"Halh Mongolian (Cyrillic)",
u"mo": u"Moldovan",
u"mr": u"Marathi",
u"ms": u"Malay",
u"mt": u"Maltese",
u"mus": u"Muskogee/Creek",
u"mwl": u"Mirandese",
u"my": u"Burmese",
u"myv": u"Erzya",
u"mzn": u"Mazanderani",
u"na": u"Dorerin Naoero / Nauruan",
u"nah": u"Nahuatl / Nahuatlahtolli / Nahuatel",
u"nan": u"Min-nan",
u"nap": u"Neapolitan",
u"nb": u"Norwegian (Bokmal)",
u"nds": u"Low German or Low Saxon",
u"nds-nl": u"Dutch Low Saxon",
u"ne": u"Nepali",
u"new": u"Newar / Nepal Bhasa",
u"ng": u"Oshiwambo / Ndonga",
u"niu": u"Niuean",
u"nl": u"Dutch / Nederlands",
u"nn": u"Norwegian (Nynorsk)",
u"no": u"Norwegian",
u"nov": u"Novial",
u"nrm": u"Nouormand",
u"nso": u"Northern Sotho",
u"nv": u"Navajo",
u"ny": u"Chi-Chewa",
u"oc": u"Occitan",
u"om": u"Oromo / Oromoo",
u"or": u"Oriya",
u"os": u"Ossetic",
u"pa": u"Eastern Punjabi",
u"pag": u"Pangasinan",
u"pam": u"Kapampangan / Pampanga",
u"pap": u"Papiamentu",
u"pcd": u"Picard",
u"pdc": u"Pennsylvania German / Deitsch",
u"pdt": u"Plautdietsch / Mennonite Low German",
u"pfl": u"Palatinate German",
u"pi": u"Pali",
u"pih": u"Norfuk / Pitkern / Norfolk",
u"pl": u"Polish",
u"pms": u"Piedmontese",
u"pnb": u"Western Punjabi",
u"pnt": u"Pontic / Pontic Greek",
u"ps": u"Pashto, Northern/Paktu/Pakhtu/Pakhtoo/Afghan/Pakhto/Pashtu/Pushto/Yusufzai Pashto",
u"pt": u"Portuguese",
u"pt-br": u"Brazilian Portuguese",
u"qu": u"Quechua / Runa Simi",
u"rgn": u"Romagnol / Rumagnol",
u"rif": u"Tarifit",
u"rm": u"Raeto-Romance",
u"rmy": u"Vlax Romany / Romani",
u"rn": u"Kirundi",
u"ro": u"Romanian",
u"roa-rup": u"Aromanian",
u"roa-tara": u"Tarantino",
u"ru": u"Russian",
u"ruq": u"Megleno-Romanian",
u"ruq-cyrl": u"Megleno-Romanian (Cyrillic script)",
u"ruq-grek": u"Megleno-Romanian (Greek script)",
u"ruq-latn": u"Megleno-Romanian (Latin script)",
u"rw": u"Kinyarwanda / Kinyarwandi",
u"sa": u"Sanskrit",
u"sah": u"Sakha",
u"sc": u"Sardu / Sardinian",
u"scn": u"Sicilian",
u"sco": u"Scots",
u"sd": u"Sindhi",
u"sdc": u"Sassaresu / Sassarese",
u"se": u"Northern Sami",
u"sei": u"Seri / Cmique Itom",
u"sg": u"Sango / Sangho",
u"sh": u"Serbocroatian",
u"shi": u"Tachelhit",
u"si": u"Sinhalese",
u"simple": u"Simple English",
u"sk": u"Slovak",
u"sl": u"Slovenian",
u"sli": u"Lower Selisian",
u"sm": u"Samoan",
u"sma": u"Southern Sami",
u"sn": u"Shona / chiShona",
u"so": u"Somali",
u"sq": u"Albanian",
u"sr": u"Serbian",
u"sr-ec": u"Serbian Cyrillic ekavian",
u"sr-el": u"Serbian Latin ekavian",
u"srn": u"Sranan Tongo",
u"ss": u"Swati / SiSwati",
u"st": u"Southern Sotho / Sesotho",
u"stq": u"Saterland Frisian",
u"su": u"Sundanese / Basa Sunda",
u"sv": u"Swedish",
u"sw": u"Swahili / Kiswahili",
u"szl": u"Silesian",
u"ta": u"Tamil",
u"tcy": u"Tulu",
u"te": u"Telugu",
u"tet": u"Tetun",
u"tg": u"Tajiki",
u"tg-cyrl": u"Tajiki (Cyrllic script)",
u"tg-latn": u"Tajiki (Latin script)",
u"th": u"Thai",
u"ti": u"Tigrinya",
u"tk": u"Turkmen",
u"tl": u"Tagalo / Tagalog",
u"tlh": u"Klingon",
u"tn": u"Setswana",
u"to": u"Tonga / lea faka-Tonga",
u"tokipona": u"Toki Pona",
u"tp": u"Toki Pona",
u"tpi": u"Tok Pisin",
u"tr": u"Turkish",
u"ts": u"Tsonga / Xitsonga",
u"tt": u"Tatar",
u"tt-cyrl": u"Tatar (Cyrillic script)",
u"tt-latn": u"Tatar (Latin script)",
u"tum": u"chiTumbuka",
u"tw": u"Twi",
u"ty": u"Tahitian",
u"tyv": u"Tyvan",
u"udm": u"Udmurt",
u"ug": u"Uyghur",
u"ug-arab": u"Uyghur (Arabic script)",
u"ug-latn": u"Uyghur (Latin script)",
u"uk": u"Ukrainian",
u"ur": u"Urdu",
u"uz": u"Uzbek",
u"ve": u"Venda / Tshivenda",
u"vec": u"Venetian",
u"vep": u"Vepsan / Veps",
u"vi": u"Vietnamese",
u"vls": u"West Flemish / West-Vlams",
u"vo": u"Volapuk",
u"vro": u"Viro",
u"wa": u"Walono",
u"war": u"Winaray / Waray-Waray",
u"wo": u"Wolof",
u"wuu": u"Wu Chinese",
u"xal": u"Kalmyk-Oirat / Kalmuk / Kalmuck / Kalmack / Qalmaq / Kalmytskii Jazyk / Khalmag / Oirat / Volga Oirat / European Oirat / Western Mongolian",
u"xh": u"Xhosan / isiXhosa",
u"xmf": u"Mingrelian",
u"yi": u"Yiddish",
u"yo": u"Yoruba",
u"yue": u"Cantonese",
u"za": u"Zhuang",
u"zea": u"Zeeuws / Zeaws",
u"zh": u"Chinese",
u"zh-classical": u"Classical Chinese / Literary Chinese",
u"zh-cn": u"Chinese (PRC)",
u"zh-hans": u"Chinese written using the Simplified Chinese script",
u"zh-hant": u"Chinese written using the Traditional Chinese script",
u"zh-hk": u"Chinese (Hong Kong)",
u"zh-min-nan": u"Min-nan",
u"zh-mo": u"Chinese (Macau)",
u"zh-my": u"Chinese (Malaysia)",
u"zh-sg": u"Chinese (Singapore)",
u"zh-tw": u"Chinese (Taiwan)",
u"zh-yue": u"Cantonese",
u"zu": u"Zulu / isiZulu",
}