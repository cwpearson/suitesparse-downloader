import sys

# matrices which are integer datatypes
INTEGER_MATS = {
	"08blocks",
    "Alemdar",
	"Andrews",
	"CAG_mat1916",
	"CAG_mat364",
	"CAG_mat72",
	"Cities",
	"CollegeMsg",
	"D6-6",
	"D_10",
	"D_11",
	"D_5",
	"D_6",
	"D_7",
	"D_8",
	"D_9",
	"EAT_RS",
	"EAT_SR",
	"EternityII_A",
	"EternityII_E",
	"EternityII_Etilde",
	"FX_March2010",
	"Franz1",
	"Franz10",
	"Franz11",
	"Franz2",
	"Franz3",
	"Franz4",
	"Franz5",
	"Franz6",
	"Franz7",
	"Franz8",
	"Franz9",
	"G10",
	"G11",
	"G12",
	"G13",
	"G18",
	"G19",
	"G20",
	"G21",
	"G27",
	"G28",
	"G29",
	"G30",
	"G31",
	"G32",
	"G33",
	"G34",
	"G39",
	"G40",
	"G41",
	"G42",
	"G56",
	"G57",
	"G59",
	"G6",
	"G61",
	"G62",
	"G64",
	"G65",
	"G66",
	"G67",
	"G7",
	"G8",
	"G9",
	"GAP-kron",
	"GAP-road",
	"GAP-twitter",
	"GAP-urand",
	"GAP-web",
	"GD00_c",
	"GD01_Acap",
	"GD01_a",
	"GD01_c",
	"GD96_a",
	"GD97_c",
	"GD99_b",
	"GL6_D_10",
	"GL6_D_6",
	"GL6_D_7",
	"GL6_D_8",
	"GL6_D_9",
	"GL7d10",
	"GL7d11",
	"GL7d12",
	"GL7d13",
	"GL7d14",
	"GL7d15",
	"GL7d16",
	"GL7d17",
	"GL7d18",
	"GL7d19",
	"GL7d20",
	"GL7d21",
	"GL7d22",
	"GL7d23",
	"GL7d24",
	"GL7d25",
	"GL7d26",
	"Hardesty1",
	"IG5-10",
	"IG5-11",
	"IG5-12",
	"IG5-13",
	"IG5-14",
	"IG5-15",
	"IG5-16",
	"IG5-17",
	"IG5-18",
	"IG5-6",
	"IG5-7",
	"IG5-8",
	"IG5-9",
	"Journals",
	"Lederberg",
	"Linux_call_graph",
	"N_biocarta",
	"N_pid",
	"N_reactome",
	"ODLIS",
	"PGPgiantcompo",
	"Ragusa16",
	"Ragusa18",
	"Reuters911",
	"Sandi_authors",
	"SciMet",
	"SmaGri",
	"SmallW",
	"Stranke94",
	"TF10",
	"TF11",
	"TF12",
	"TF13",
	"TF14",
	"TF15",
	"TF16",
	"TF17",
	"TF18",
	"TF19",
	"Trec10",
	"Trec11",
	"Trec12",
	"Trec13",
	"Trec14",
	"Trec4",
	"Trec5",
	"Trec6",
	"Trec7",
	"Trec8",
	"Trec9",
	"Trefethen_150",
	"Trefethen_20",
	"Trefethen_200",
	"Trefethen_2000",
	"Trefethen_20000",
	"Trefethen_20000b",
	"Trefethen_200b",
	"Trefethen_20b",
	"Trefethen_300",
	"Trefethen_500",
	"Trefethen_700",
	"Wordnet3",
	"WorldCities",
	"Zewail",
	"abtaha1",
	"abtaha2",
	"aircraft",
	"ak2010",
	"al2010",
	"ar2010",
	"as-caida",
	"atmosmodm",
    "aug2dc",
    "aug2d",
    "aug3d",
	"az2010",
	"bas1lp",
	"bcsstm01",
	"big",
	"c8_mat11",
	"c8_mat11_I",
	"ca2010",
	"celegans_metabolic",
	"celegansneural",
	"ch3-3-b1",
	"ch3-3-b2",
	"ch4-4-b1",
	"ch4-4-b2",
	"ch4-4-b3",
	"ch5-5-b1",
	"ch5-5-b2",
	"ch5-5-b3",
	"ch5-5-b4",
	"ch6-6-b1",
	"ch6-6-b2",
	"ch6-6-b3",
	"ch6-6-b4",
	"ch6-6-b5",
	"ch7-6-b1",
	"ch7-6-b2",
	"ch7-6-b3",
	"ch7-6-b4",
	"ch7-6-b5",
	"ch7-7-b1",
	"ch7-7-b2",
	"ch7-7-b5",
	"ch7-8-b1",
	"ch7-8-b2",
	"ch7-8-b3",
	"ch7-8-b4",
	"ch7-8-b5",
	"ch7-9-b1",
	"ch7-9-b2",
	"ch7-9-b3",
	"ch7-9-b4",
	"ch7-9-b5",
	"ch8-8-b1",
	"ch8-8-b2",
	"ch8-8-b3",
	"ch8-8-b4",
	"ch8-8-b5",
	"cis-n4c6-b13",
	"cis-n4c6-b14",
	"cis-n4c6-b15",
	"cis-n4c6-b1cis-n4c6-b1",
	"cis-n4c6-b1",
    "cis-n4c6-b2",
	"cis-n4c6-b3",
	"cis-n4c6-b4",
	"co2010",
	"complex",
	"ct2010",
    "cyl6",
	"dbic1",
	"dbir1",
	"dbir2",
	"de2010",
	"e18",
	"email-Eu-core-temporal",
    "engine",
	"f855_mat9",
	"f855_mat9_I",
	"farm",
	"fl2010",
	"foldoc",
	"fome20",
	"fome21",
	"football",
	"ga2010",
	"geom",
	"gr_30_30",
	"hi2010",
	"ia2010",
	"id2010",
	"il2010",
	"in2010",
	"internet",
	"jazz",
	"jpwh_991",
	"kleemin",
	"klein-b1",
	"klein-b2",
	"kron_g500-logn16",
	"kron_g500-logn17",
	"kron_g500-logn18",
	"kron_g500-logn19",
	"kron_g500-logn20",
	"kron_g500-logn21",
	"ks2010",
	"ky2010",
	"la2010",
	"lesmis",
	"lp22",
	"lp_d6cube",
	"lp_degen2",
	"lp_degen3",
	"lp_ken_07",
	"lp_ken_11",
	"lp_ken_13",
	"lp_ken_18",
	"lp_nug05",
	"lp_nug06",
	"lp_nug07",
	"lp_nug08",
	"lp_nug12",
	"lp_nug15",
	"lp_nug20",
	"lp_nug30",
	"lp_pds_02",
	"lp_pds_06",
	"lp_pds_10",
	"lp_pds_20",
	"lp_qap12",
	"lp_qap15",
	"lp_qap8",
	"lp_sctap1",
	"lp_sctap2",
	"lp_sctap3",
	"lp_shell",
	"lp_sierra",
	"lpi_bgprtr",
	"lpi_box1",
	"lpi_ceria3d",
	"lpi_ex72a",
	"lpi_ex73a",
	"lpi_galenet",
	"lpi_klein1",
	"lpi_klein2",
	"lpi_klein3",
	"lpi_mondou2",
	"lpi_woodinfe",
	"lpl2",
	"lpl3",
	"lutz30-23-b6",
	"m133-b3",
	"ma2010",
	"mawi_201512012345",
	"mawi_201512020000",
	"mawi_201512020030",
	"mawi_201512020130",
	"mawi_201512020330",
    "mc2depi",
	"md2010",
	"me2010",
	"mi2010",
	"mk10-b1",
	"mk10-b2",
	"mk10-b3",
	"mk10-b4",
	"mk11-b1",
	"mk11-b2",
	"mk11-b3",
	"mk11-b4",
	"mk11-b4b",
	"mk12-b1",
	"mk12-b2",
	"mk12-b3",
	"mk12-b4",
	"mk12-b5",
	"mk13-b5",
	"mk9-b1",
	"mk9-b2",
	"mk9-b3",
	"mn2010",
	"mo2010",
	"ms2010",
	"mt2010",
	"n2c6-b1",
	"n2c6-b10",
	"n2c6-b2",
	"n2c6-b3",
	"n2c6-b4",
	"n2c6-b5",
	"n2c6-b6",
	"n2c6-b7",
	"n2c6-b8",
	"n2c6-b9",
	"n3c4-b1",
	"n3c4-b2",
	"n3c4-b3",
	"n3c4-b4",
	"n3c5-b1",
	"n3c5-b2",
	"n3c5-b3",
	"n3c5-b4",
	"n3c5-b5",
	"n3c5-b6",
	"n3c5-b7",
	"n3c6-b1",
	"n3c6-b10",
	"n3c6-b11",
	"n3c6-b2",
	"n3c6-b3",
	"n3c6-b4",
	"n3c6-b5",
	"n3c6-b6",
	"n3c6-b7",
	"n3c6-b8",
	"n3c6-b9",
	"n4c5-b1",
	"n4c5-b10",
	"n4c5-b11",
	"n4c5-b2",
	"n4c5-b3",
	"n4c5-b4",
	"n4c5-b5",
	"n4c5-b6",
	"n4c5-b7",
	"n4c5-b8",
	"n4c5-b9",
	"n4c6-b1",
	"n4c6-b10",
	"n4c6-b11",
	"n4c6-b12",
	"n4c6-b13",
	"n4c6-b14",
	"n4c6-b15",
	"n4c6-b2",
	"n4c6-b3",
	"n4c6-b4",
	"n4c6-b5",
	"n4c6-b6",
	"n4c6-b7",
	"n4c6-b8",
	"n4c6-b9",
	"nc2010",
	"nd2010",
	"ne2010",
	"neos1",
	"neos2",
	"neos3",
	"nh2010",
	"nj2010",
	"nm2010",
	"nopoly",
	"nos1",
	"nsct",
	"nsic",
	"nsir",
	"nug08-3rd",
	"nv2010",
	"ny2010",
	"oh2010",
	"ok2010",
	"or2010",
	"p0033",
	"p0040",
	"p0201",
	"p0282",
	"p0548",
	"p2756",
	"p6000",
	"pa2010",
	"pcb1000",
	"pcb3000",
	"pds-100",
	"pds-30",
	"pds-40",
	"pds-50",
	"pds-60",
	"pds-70",
	"pds-80",
	"pds-90",
	"pesa",
	"pgp2",
	"pltexpa",
	"polblogs",
	"primagaz",
	"problem",
	"psmigr_1",
	"rail2586",
	"rail4284",
	"rail507",
	"rail516",
	"rail582",
	"rbsa480",
	"rbsb480",
	"rel3",
	"rel4",
	"rel5",
	"rel6",
	"rel7",
	"rel8",
	"rel9",
	"relat3",
	"relat4",
	"relat5",
	"relat6",
	"relat7",
	"relat7b",
	"relat8",
	"relat9",
	"ri2010",
	"rkat7_mat5",
	"rlfddd",
	"rlfdual",
	"rlfprim",
	"robot24c1_mat5",
	"robot24c1_mat5_J",
	"rosen1",
	"rosen10",
	"rosen2",
	"rosen7",
	"rosen8",
	"sc2010",
	"sctap1-2b",
	"sctap1-2c",
	"sctap1-2r",
	"sd2010",
	"seymourl",
	"sgpf5y6",
	"shar_te2-b1",
	"shar_te2-b2",
	"shar_te2-b3",
	"shl_0",
	"shl_200",
	"shl_400",
	"soc-sign-Slashdot081106",
	"soc-sign-Slashdot090216",
	"soc-sign-Slashdot090221",
	"soc-sign-bitcoin-alpha",
	"soc-sign-bitcoin-otc",
	"soc-sign-epinions",
	"stoch_aircraft",
	"sx-askubuntu",
	"sx-mathoverflow",
	"sx-stackoverflow",
	"sx-superuser",
	"t2em",
    "t520",
	"tn2010",
    "tube2",
	"tx2010",
	"ut2010",
	"va2010",
	"vt2010",
	"wa2010",
	"wi2010",
	"wiki-RfA",
	"wiki-talk-temporal",
	"wv2010",
	"wy2010"
}
