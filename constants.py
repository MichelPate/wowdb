EFFECT_TYPES = {
    0: "None",
    1: "Instant Kill",
    2: "School Damage",
    3: "Dummy",
    4: "Portal Teleport",
    5: "Teleport Units",
    6: "Apply Aura",
    7: "Environmental Damage",
    8: "Power Drain",
    9: "Health Leech",
    10: "Direct Heal",
    11: "Bind",
    12: "Portal",
    13: "Ritual Base",
    14: "Ritual Specialize",
    15: "Ritual Activate",
    16: "Quest Complete",
    17: "Weapon Damage",
    18: "Resurrect",
    19: "Extra Attacks",
    20: "Dodge",
    21: "Evade",
    22: "Parry",
    23: "Block",
    24: "Create Item",
    25: "Weapon Type",
    26: "Defense",
    27: "Persistent Area Aura",
    28: "Summon",
    29: "Leap",
    30: "Energize Power",
    31: "Weapon Damage%",
    32: "Trigger Missiles",
    33: "Open Lock",
    34: "Summon Item",
    35: "Apply Party Aura",
    36: "Learn Spell",
    37: "Spell Defense",
    38: "Dispel",
    39: "Language",
    40: "Dual Wield",
    42: "Jump Behind Target",
    48: "Stealth",
    49: "Detect",
    52: "Guaranteed Hit",
    53: "Enchant Item",
    56: "Summon Pet",
    58: "Weapon Damage",
    62: "Power Burn",
    63: "Threat",
    64: "Trigger Spell",
    65: "Apply Raid Aura",
    68: "Interrupt Cast",
    69: "Distract",
    70: "Pull",
    71: "Pick Pocket",
    77: "Server Side Script",
    78: "Attack",
    80: "Add Combo Points",
    85: "Summon Player",
    86: "Open Object",
    91: "Threat All",
    94: "Self Resurrect",
    96: "Charge",
    97: "Summon All Totems",
    98: "Knock Back",
    101: "Feed Pet",
    102: "Dismiss Pet",
    109: "Summon Dead Pet",
    110: "Destroy All Totems",
    113: "Resurrect",
    119: "Apply Pet Area Aura",
    121: "Normalized Weapon Damage",
    124: "Pull Player",
    125: "Modify Threat",
    126: "Steal Beneficial Aura",
    128: "Apply Friendly Area Aura",
    129: "Apply Enemy Area Aura",
    130: "Redirect Threat",
    135: "Call Pet",
    136: "Direct Heal%",
    137: "Energize Power%",
    138: "Leap Back",
    140: "Trigger Spell from Target with Caster as Target",
    142: "Trigger Spell w/ Value",
    143: "Apply Owner Area Aura",
    146: "Activate Rune",
    151: "Trigger Spell",
    154: "Teach Flight Path",
    155: "Titan Grip",
    156: "Add Socket",
    157: "Create Item",
    179: "Create Area Trigger",
    202: "Apply Player/Pet Aura"
}

SUBEFFECT_TYPES = {
    0: "None",
    2: "Possess",
    3: "Periodic Damage",
    4: "Dummy",
    5: "Confuse",
    6: "Charm",
    7: "Fear",
    8: "Periodic Heal",
    9: "Attack Speed",
    10: "Threat",
    11: "Taunt",
    12: "Stun",
    13: "Damage Done",
    14: "Damage Taken",
    15: "Damage Shield",
    16: "Stealth",
    17: "Stealth Detection",
    18: "Invisibility",
    19: "Invisibility Detection",
    20: "Periodic Heal%",
    21: "Periodic Power% Regen",
    22: "Resistance",
    23: "Periodic Trigger Spell",
    24: "Periodic Energize Power",
    25: "Pacify",
    26: "Root",
    27: "Silence",
    28: "Spell Reflection",
    29: "Mod Stat",
    30: "Skill",
    31: "Increase Speed%",
    32: "Increase Mounted Speed%",
    33: "Decrease Movement Speed%",
    34: "Increase Health",
    35: "Increase Energy",
    36: "Shapeshift",
    37: "Immunity Against External Movement",
    39: "School Immunity",
    40: "Damage Immunity",
    41: "Disable Stealth",
    42: "Proc Trigger Spell",
    43: "Proc Trigger Damage",
    44: "Track Creatures",
    47: "Modify Parry%",
    49: "Modify Dodge%",
    50: "Modify Critical Heal Bonus",
    51: "Modify Block%",
    52: "Modify Crit%",
    53: "Periodic Health Leech",
    54: "Modify Hit%",
    55: "Modify Spell Hit%",
    56: "Change Model",
    57: "Modify Spell Crit%",
    60: "Pacify Silence",
    61: "Scale% (Stacking)",
    63: "Modify Max Cost",
    64: "Periodic Mana Leech",
    65: "Modify Spell Speed%",
    66: "Feign Death",
    67: "Disarm",
    68: "Stalked",
    69: "Absorb Damage",
    72: "Modify Power Cost%",
    73: "Modify Power Cost",
    74: "Reflect Spells",
    77: "Mechanic Immunity",
    79: "Modify Damage Done%",
    80: "Modify Attribute%",
    81: "Transfer Damage%",
    84: "Restore Health",
    85: "Restore Power",
    87: "Modify Damage Taken%",
    88: "Modify Health Regeneration%",
    89: "Periodic Max Health% Damage",
    99: "Modify Attack Power",
    101: "Modify Armor%",
    102: "Modify Melee Attack Power vs Race",
    103: "Temporary Thread Reduction",
    104: "Modify Attack Power",
    106: "Levitate",
    107: "Modifies [EffectMiscValue]",
    108: "Add Percent Modifier",
    110: "Modify Power Regen",
    115: "Modify Healing Received",
    116: "Combat Health Regen%",
    117: "Mechanic Resistance",
    118: "Modify Healing Recevied%",
    123: "Modify Target Resistance",
    124: "Modify Ranged Attack Power",
    129: "Increase Movement Speed% (Stacking)",
    130: "Increase Mount Speed% (Stacking)",
    131: "Modify Ranged Attack Power vs Race",
    132: "Modify Max Resource%",
    133: "Modify Max Health%",
    135: "Modify Healing Power",
    136: "Modify Healing% Done",
    137: "Modify Total Stat%",
    138: "Modify Melee Haste%",
    140: "Modify Ranged Haste%",
    142: "Modify Base Resistance",
    143: "Modify Cooldown Recharge Rate",
    144: "Reduce Fall Damage",
    149: "Modify Casting Pushback",
    150: "Modify Block Effectiveness",
    152: "Modify Aggro Distance",
    157: "Modify Absorb% Done",
    163: "Modify Crit Damage Done%",
    166: "Modify Melee Attack Power%",
    167: "Modify Ranged Attack Power%",
    168: "Modify Damage Done% vs Race",
    172: "Increase Mounted Speed%",
    177: "Charmed",
    178: "Modify Max Mana%",
    180: "Modify Spell Damage vs Race",
    184: "Modify Attacker Melee Hit Chance",
    185: "Modify Attacker Ranged Hit Chance",
    186: "Modify Attacker Spell Hit Chance",
    187: "Modify Attacker Melee Crit Chance",
    189: "Modify Rating",
    192: "Modify Ranged and Melee Haste%",
    193: "Modify All Haste%",
    197: "Modify Attacker Crit Chance",
    200: "Modify Experience Gained from Kills",
    216: "Modify Casting Speed",
    218: "Apply Percent Modifier w/ Label",
    224: "Grant Talent",
    226: "Periodic Dummy",
    228: "Stealth Detection",
    229: "Modify AoE Damage Taken%",
    231: "Trigger Spell with Value",
    232: "Modify Mechanic Duration% (Stacking)",
    234: "Modify Mechanic Duration%",
    239: "Scale%",
    240: "Modify Expertise%",
    241: "Forced Movement",
    244: "Comprehend Language",
    245: "Modify Debuff Duration%",
    247: "Copy Appearance",
    250: "Increase Max Health (Stacking)",
    253: "Modify Critical Block Chance",
    259: "Modify Periodic Healing Recevied%",
    260: "Change Model",
    262: "Enable Abilities",
    263: "Disable Abilities",
    268: "Modify Armor by Primary Stat%",
    269: "Modify Damage Done% to Caster",
    270: "Modify Damage Taken% from Caster",
    271: "Modify Damage Taken% from Caster's Spells",
    283: "Modify Healing Taken% from Caster's Spells",
    290: "Modify Critical Strike%",
    291: "Modify Experience Gained from Quests",
    301: "Absorb Healing",
    305: "Modify Min Speed%",
    308: "Modify Crit Chance% from Caster's Spells",
    318: "Modify Mastery%",
    319: "Modify Melee Attack Speed%",
    320: "Modify Ranged Attack Speed%",
    321: "??",
    329: "Modify Resource Generation%",
    330: "Cast while Moving (Whitelist)",
    334: "Modify Auto Attack Critical Chance",
    342: "Modify Ranged and Melee Attack Speed%",
    343: "Modify Auto Attack Damage Taken% from Caster",
    344: "Modify Auto Attack Damage Done%",
    345: "Ignore Armor%",
    354: "Modify Healing% Based on Target Health%",
    360: "Duplicate Ability",
    361: "Override Auto-Attack with Spell",
    366: "Override Spell Power per Attack Power%",
    374: "Reduce Fall Damage%",
    377: "Cast while Moving",
    379: "Modify Mana Regen%",
    383: "Ignore Spell Cooldown",
    404: "Override Attack Power per Spell Power%",
    405: "Modify Combat Rating Multiplier",
    409: "Slow Fall",
    411: "Modify Cooldown Charge (Category)",
    416: "Hasted Cooldown Duration",
    417: "Hasted Global Cooldown",
    418: "Modify Max Resource",
    419: "Modify Mana Pool%",
    421: "Modify Absorb% Done",
    422: "Modify Absorb% Done",
    429: "Modify Pet Damage Done%",
    441: "Modify Multistrike%",
    443: "Modify Leech%",
    453: "Modify Recharge Time (Category)",
    454: "Modify Recharge Time% (Category)",
    455: "Root",
    457: "Hasted Cooldown Duration (Category)",
    465: "Increase Armor",
    468: "Trigger Spell Based on Health%",
    471: "Modify Versatility%",
    483: "?? (Aura #483)",
    485: "Resist Forced Movement%"
}
SCHOOL_MASKS = {
    0: "None",
    1: "Physical",
    2: "Holy",
    4: "Fire",
    5: "Flamestrike (Fire, Physical)",
    6: "Radiant (Fire, Holy)",
    8: "Nature",
    12: "Firestorm (Fire, Nature)",
    16: "Frost",
    28: "Elemental (Fire, Frost, Nature)",
    32: "Shadow",
    34: "Twilight (Holy, Shadow)",
    40: "Plague (Nature, Shadow)",
    64: "Arcane",
    72: "Astral (Arcane, Nature)",
    124: "Chromatic",
    125: "Shadowflame (Fire, Shadow)",
    127: "Chaos (All)"
}
SPELLS_FLAGS = {
    0: 'Unk0',
    1: 'Ranged Ability',
    2: 'On Next Swing',
    3: 'Is Replenishment',
    4: 'Ability',
    5: 'Tradeskill ability',
    6: 'Passive',
    7: 'Hidden',
    8: 'Hide In Combat Log',
    9: 'Target Mainhand Item',
    10: 'On Next Swing 2',
    11: 'Unk11',
    12: 'Daytime Only',
    13: 'Night Only',
    14: 'Indoors Only',
    15: 'Outdoors Only',
    16: 'Cannot be used while shapeshifted',
    17: 'Requires stealth',
    18: 'Don\'t Affect Stealth State',
    19: 'Level Damage Calculation',
    20: 'Stop attacks',
    21: 'Cannot dodge/parry/block',
    22: 'Cast Track Target',
    23: 'Castable While Dead',
    24: 'Castable While Mounted',
    25: 'Disabled While Active',
    26: 'Negative 1',
    27: 'Castable While Sitting',
    28: 'Cannot be used in combat',
    29: 'Unaffected By Invulnerability',
    30: 'Heartbeat Resist Check',
    31: 'Aura cannot be cancelled',
    32: 'Dismiss Pet',
    33: 'Drain All Power',
    34: 'Channeled',
    35: 'Cannot be redirected',
    36: 'Unk36',
    37: 'Does not break stealth',
    38: 'Channeled',
    39: 'Cannot be reflected',
    40: 'Can\'t Target In Combat',
    41: 'Starts auto-attack',
    42: 'Generates no threat',
    43: 'Unk43',
    44: 'Is Pickpocket',
    45: 'Farsight',
    46: 'Channel Track Target',
    47: 'Dispel Auras On Immunity',
    48: 'Unaffected By School Immune',
    49: 'Unautocastable By Pet',
    50: 'Unk50',
    51: 'Can\'t Target Self',
    52: 'Req Combo Points1',
    53: 'Unk53',
    54: 'Req Combo Points2',
    55: 'Unk55',
    56: 'Is Fishing',
    57: 'Unk57',
    58: 'Unk58',
    59: 'Unk59',
    60: 'Don\'t Display In Aura Bar',
    61: 'Channel Display Spell Name',
    62: 'Enable At Dodge',
    63: 'Unk63',
    64: 'Can Target Dead',
    65: 'Unk65',
    66: 'Cannot line of sight',
    67: 'Unk67',
    68: 'Display In Stance Bar',
    69: 'Autorepeat Flag',
    70: 'Can\'t Target Tapped',
    71: 'Unk71',
    72: 'Unk72',
    73: 'Unk73',
    74: 'Unk74',
    75: 'Health Funnel',
    76: 'Unk76',
    77: 'Preserve Enchant In Arena',
    78: 'Unk78',
    79: 'Unk79',
    80: 'Tame Beast',
    81: 'Not Reset Auto Actions',
    82: 'Req Dead Pet',
    83: 'Not Need Shapeshift',
    84: 'Unk84',
    85: 'Damage Reduced Shield',
    86: 'Unk86',
    87: 'Is Arcane Concentration',
    88: 'Unk88',
    89: 'Unk89',
    90: 'Unaffected by school immunity',
    91: 'Unk91',
    92: 'Does not engage target',
    93: 'Cannot crit',
    94: 'Triggered Can Trigger Proc',
    95: 'Food buff',
    96: 'Unk96',
    97: 'Unk97',
    98: 'Unk98',
    99: 'Blockable Spell',
    100: 'Ignore Resurrection Timer',
    101: 'Unk101',
    102: 'Unk102',
    103: 'Stack For Diff Casters',
    104: 'Only Target Players',
    105: 'Not a proc',
    106: 'Requires main-hand weapon',
    107: 'Battleground',
    108: 'Only Target Ghosts',
    109: 'Don\'t Display Channel Bar',
    110: 'Is Honorless Target',
    111: 'Autoshot',
    112: 'Disable player procs',
    113: 'Disable target procs',
    114: 'Always hits',
    115: 'Disable Proc',
    116: 'Persists through death',
    117: 'Unk117',
    118: 'Req Wand',
    119: 'Unk119',
    120: 'Requires off-hand weapon',
    121: 'Treat as periodic',
    122: 'Can Proc With Triggered',
    123: 'Drain Soul',
    124: 'Unk124',
    125: 'No Done Bonus',
    126: 'Don\'t Display Range',
    127: 'Unk127',
    128: 'Ignore Resistances',
    129: 'Proc Only On Caster',
    130: 'Unk130',
    131: 'Unk131',
    132: 'Unk132',
    133: 'Unk133',
    134: 'Not Stealable',
    135: 'Triggered',
    136: 'Fixed Damage',
    137: 'Trigger Activate',
    138: 'Spell Vs Extend Cost',
    139: 'Unk139',
    140: 'Unk140',
    141: 'Unk141',
    142: 'Damage Doesnt Break Auras',
    143: 'Unk143',
    144: 'Not Usable In Arena Or Rated Bg',
    145: 'Usable In Arena',
    146: 'Area Target Chain',
    147: 'Don\'t proc on absorb',
    148: 'Not Check Selfcast Power',
    149: 'Stance',
    150: 'Unk150',
    151: 'Disable weapon procs',
    152: 'Unk152',
    153: 'Is Pet Scaling',
    154: 'Cast Only In Outland',
    155: 'Unk155',
    156: 'Unk156',
    157: 'Unk157',
    158: 'Unk158',
    159: 'Unk159',
    160: 'Unk160',
    161: 'No Reagent While Prep',
    162: 'Unk162',
    163: 'Usable While Stunned',
    164: 'Unk164',
    165: 'Single Target Spell',
    166: 'Unk166',
    167: 'Unk167',
    168: 'Unk168',
    169: 'Tick on application',
    170: 'Hide Duration',
    171: 'Allow Target Of Target As Target',
    172: 'Unk172',
    173: 'Periodic effect affected by haste',
    174: 'Unk174',
    175: 'Unk175',
    176: 'Special Item Class Check',
    177: 'Usable While Feared',
    178: 'Usable While Confused',
    179: 'Don\'t Turn During Cast',
    180: 'Unk180',
    181: 'Unk181',
    182: 'Unk182',
    183: 'Unk183',
    184: 'Unk184',
    185: 'Unk185',
    186: 'Requires line of sight',
    187: 'Don\'t Show Aura If Self Cast',
    188: 'Don\'t Show Aura If Not Self Cast',
    189: 'Unk189',
    190: 'Unk190',
    191: 'Unk191',
    192: 'Don\'t Display Cooldown',
    193: 'Only In Arena',
    194: 'Ignore Caster Auras',
    195: 'Assist Ignore Immune Flag',
    196: 'Unk196',
    197: 'Unk197',
    198: 'Use Spell Cast Event',
    199: 'Unk199',
    200: 'Can\'t Target Crowd Controlled',
    201: 'Unk201',
    202: 'Can Target Possessed Friends',
    203: 'Not In Raid Instance',
    204: 'Castable While On Vehicle',
    205: 'Can Target Invisible',
    206: 'Unk206',
    207: 'Unk207',
    208: 'Unk208',
    209: 'Unk209',
    210: 'Cast By Charmer',
    211: 'Unk211',
    212: 'Only Visible To Caster',
    213: 'Client Ui Target Effects',
    214: 'Unk214',
    215: 'Unk215',
    216: 'Can Target Untargetable',
    217: 'Unk217',
    218: 'Unk218',
    219: 'Unk219',
    220: 'Unk220',
    221: 'Disable player multipliers',
    222: 'Unk222',
    223: 'Ignore Category Cooldown Mods',
    224: 'Unk224',
    225: 'Ignore Duration Mods',
    226: 'Reactivate At Resurrect',
    227: 'Is Cheat Spell',
    228: 'Unk228',
    229: 'Summon Totem',
    230: 'No Pushback On Damage',
    231: 'Unk231',
    232: 'Horde Only',
    233: 'Alliance Only',
    234: 'Dispel Charges',
    235: 'Interrupt Only Nonplayer',
    236: 'Unk236',
    237: 'Unk237',
    238: 'Unk238',
    239: 'Unk239',
    240: 'Can Restore Secondary Power',
    241: 'Unk241',
    242: 'Has Charge Effect',
    243: 'Zone Teleport',
    244: 'Unk244',
    245: 'Unk245',
    246: 'Unk246',
    247: 'Unk247',
    248: 'Unk248',
    249: 'Unk249',
    250: 'Unk250',
    251: 'Unk251',
    252: 'Consolidated Raid Buff',
    253: 'Unk253',
    254: 'Unk254',
    255: 'Client Indicator',
    256: 'Can\'t Miss',
    257: 'Unk257',
    258: 'Unk258',
    259: 'Unk259',
    260: 'Unk260',
    261: 'Unk261',
    262: 'Unk262',
    263: 'Unk263',
    264: 'Affect Party And Raid',
    265: 'Periodic effect can crit',
    266: 'Name Changed During Transform',
    267: 'Unk267',
    268: 'Aura Send Amount',
    269: 'Unk269',
    270: 'Unk270',
    271: 'Water Mount',
    272: 'Unk272',
    273: 'Unk273',
    274: 'Remember Spells',
    275: 'Use Combo Points On Any Target',
    276: 'Armor Specialization',
    277: 'Unk277',
    278: 'Unk278',
    279: 'Battle Resurrection',
    280: 'Healing Spell',
    281: 'Unk281',
    282: 'Raid Marker',
    283: 'Unk283',
    284: 'Not In Bg Or Arena',
    285: 'Mastery Specialization',
    286: 'Unk286',
    287: 'Attack Ignore Immune To Pc Flag',
    288: 'Unk288',
    289: 'Unk289',
    290: 'Restricted Flight Area',
    291: 'Unk291',
    292: 'Special Delay Calculation',
    293: 'Summon Player Totem',
    294: 'Unk294',
    295: 'Unk295',
    296: 'Aimed Shot',
    297: 'Not Usable In Arena',
    298: 'Unk298',
    299: 'Unk299',
    300: 'Unk300',
    301: 'Slam',
    302: 'Usable In Rated Battlegrounds',
    303: 'Unk303',
    304: 'Unk304',
    305: 'Unk305',
    306: 'Unk306',
    307: 'Unk307',
    308: 'Unk308',
    309: 'Unk309',
    310: 'Unk310',
    311: 'Unk311',
    312: 'Unk312',
    313: 'Unk313',
    314: 'Unk314',
    315: 'Unk315',
    316: 'Unk316',
    317: 'Unk317',
    318: 'Unk318',
    319: 'Unk319',
    320: 'Unk320',
    321: 'Unk321',
    322: 'Unk322',
    323: 'Unk323',
    324: 'Water Spout',
    325: 'Unk325',
    326: 'Unk326',
    327: 'Teleport Player',
    328: 'Unk328',
    329: 'Unk329',
    330: 'Unk330',
    331: 'Herb Gathering Mining',
    332: 'Unk332',
    333: 'Unk333',
    334: 'Unk334',
    335: 'Unk335',
    336: 'Unk336',
    337: 'Unk337',
    338: 'Unk338',
    339: 'Unk339',
    340: 'Unk340',
    341: 'Unk341',
    342: 'Unk342',
    343: 'Unk343',
    344: 'Unk344',
    345: 'Unk345',
    346: 'Unk346',
    347: 'Unk347',
    348: 'Unk348',
    349: 'Unk349',
    350: 'Unk350',
    351: 'Unk351',
    354: 'Scales with item level'
}

EFFECT_MISC_TYPES = {
    1: {
        1: 'Bind Sight'
    },
    2: {
        1: 'Possess'
    },
    3: {
        1: 'Periodic Damage'
    },
    4: {
        1: 'Dummy'
    },
    5: {
        1: 'Confuse'
    },
    6: {
        1: 'Charm'
    },
    7: {
        1: 'Fear'
    },
    8: {
        0: 'Periodic Heal'
    },
    9: {
        1: 'Mod Attack Speed'
    },
    10: {
        1: 'Mod Threat'
    },
    11: {
        1: 'Taunt'
    },
    12: {
        1: 'Stun'
    },
    13: {
        -1: 'Mod Damage Done (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        0: 'Mod Damage Done',
        1: 'Mod Damage Done (Physical)',
        2: 'Mod Damage Done (Holy)',
        4: 'Mod Damage Done (Fire)',
        8: 'Mod Damage Done (Nature)',
        16: 'Mod Damage Done (Frost)',
        32: 'Mod Damage Done (Shadow)',
        52: 'Mod Damage Done (Fire, Frost, Shadow)',
        64: 'Mod Damage Done (Arcane)',
        74: 'Mod Damage Done (Arcane, Holy, Nature)',
        126: 'Mod Damage Done (All)',
        127: 'Mod Damage Done (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        15105: 'Mod Damage Done (Physical)',
        161597: 'Mod Damage Done (Fire, Frost, Nature, Physical, Shadow)',
        917630: 'Mod Damage Done (Arcane, Fire, Frost, Holy, Nature, Shadow)'
    },
    14: {
        0: 'Mod Damage Taken',
        1: 'Mod Damage Taken (Physical)',
        2: 'Mod Damage Taken (Holy)',
        4: 'Mod Damage Taken (Fire)',
        8: 'Mod Damage Taken (Nature)',
        16: 'Mod Damage Taken (Frost)',
        32: 'Mod Damage Taken (Shadow)',
        36: 'Mod Damage Taken (Fire, Shadow)',
        64: 'Mod Damage Taken (Arcane)',
        126: 'Mod Damage Taken (All)',
        127: 'Mod Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        65568: 'Mod Damage Taken (Shadow)'
    },
    15: {
        1: 'Damage shield'
    },
    16: {
        1: 'Stealth'
    },
    17: {
        1: 'Stealth Detection'
    },
    18: {
        1: 'Invisibility'
    },
    19: {
        1: 'Invisibility Detection'
    },
    20: {
        1: 'Mod Total Health Regen %'
    },
    21: {
        0: 'Mod Total Power Regen % (Mana)',
        1: 'Mod Total Power Regen % (Rage)',
        2: 'Mod Total Power Regen % (Focus)',
        3: 'Mod Total Power Regen % (Energy)',
        4: 'Mod Total Power Regen % (Combo Point)',
        5: 'Mod Total Power Regen % (Rune)',
        6: 'Mod Total Power Regen % (Runic Power)',
        7: 'Mod Total Power Regen % (Soul Shard)',
        8: 'Mod Total Power Regen % (Astral Power)',
        9: 'Mod Total Power Regen % (Holy Power)',
        10: 'Mod Total Power Regen % (Alternate)',
        11: 'Mod Total Power Regen % (Maelstrom)',
        12: 'Mod Total Power Regen % (Chi)',
        13: 'Mod Total Power Regen % (Insanity)',
        14: 'Mod Total Power Regen % (Burning Ember)',
        15: 'Mod Total Power Regen % (Demonic Fury)',
        16: 'Mod Total Power Regen % (Arcane Charge)',
        17: 'Mod Total Power Regen % (Fury)',
        18: 'Mod Total Power Regen % (Pain)'
    },
    22: {
        0: 'Mod Resistance',
        1: 'Mod Resistance (Physical)',
        4: 'Mod Resistance (Fire)',
        8: 'Mod Resistance (Nature)',
        16: 'Mod Resistance (Frost)',
        20: 'Mod Resistance (Fire, Frost)',
        32: 'Mod Resistance (Shadow)',
        64: 'Mod Resistance (Arcane)',
        124: 'Mod Resistance (Arcane, Fire, Frost, Nature, Shadow)',
        126: 'Mod Resistance (All)',
        127: 'Mod Resistance (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        114689: 'Mod Resistance (Physical)',
        917505: 'Mod Resistance (Physical)',
        33554433: 'Mod Resistance (Physical)',
        268435457: 'Mod Resistance (Physical)'
    },
    23: {
        1: 'Periodically trigger spell'
    },
    24: {
        0: 'Periodically give power (Mana)',
        1: 'Periodically give power (Rage)',
        2: 'Periodically give power (Focus)',
        3: 'Periodically give power (Energy)',
        4: 'Periodically give power (Combo Point)',
        5: 'Periodically give power (Rune)',
        6: 'Periodically give power (Runic Power)',
        7: 'Periodically give power (Soul Shard)',
        8: 'Periodically give power (Astral Power)',
        9: 'Periodically give power (Holy Power)',
        10: 'Periodically give power (Alternate)',
        11: 'Periodically give power (Maelstrom)',
        12: 'Periodically give power (Chi)',
        13: 'Periodically give power (Insanity)',
        14: 'Periodically give power (Burning Ember)',
        15: 'Periodically give power (Demonic Fury)',
        18: 'Periodically give power (Pain)'
    },
    25: {
        1: 'Pacify'
    },
    26: {
        1: 'Root'
    },
    27: {
        1: 'Silence'
    },
    28: {
        1: 'Reflect All Spells'
    },
    29: {
        -2: 'Mod Stat (0)',
        -1: 'Mod Stat (All)',
        0: 'Mod Stat (Strength)',
        1: 'Mod Stat (Agility)',
        2: 'Mod Stat (Stamina)',
        3: 'Mod Stat (Intellect)',
        126: 'Mod Stat (0)',
        67108864: 'Mod Stat (0)'
    },
    30: {
        1: 'Mod Skill - Temporary'
    },
    31: {
        1: 'Increase Run Speed %'
    },
    32: {
        1: 'Mod Mounted Speed %'
    },
    33: {
        1: 'Decrease Run Speed %'
    },
    34: {
        0: 'Increase Max Health - Flat',
        127: 'Increase Max Health - Flat'
    },
    35: {
        0: 'Increase Max Power - Flat (Mana)',
        2: 'Increase Max Power - Flat (Focus)',
        3: 'Increase Max Power - Flat (Energy)',
        8: 'Increase Max Power - Flat (Astral Power)',
        11: 'Increase Max Power - Flat (Maelstrom)',
        12: 'Increase Max Power - Flat (Chi)'
    },
    36: {
        1: 'Shapeshift (Cat Form)',
        2: 'Shapeshift (Tree of Life Form)',
        3: 'Shapeshift (Travel Form)',
        4: 'Shapeshift (Aquatic Form)',
        5: 'Shapeshift (Bear Form)',
        10: "Shapeshift (Tharon'ja Skeleton)",
        11: 'Shapeshift (Darkmoon - Test of Strength)',
        14: 'Shapeshift (Creature - Bear)',
        15: 'Shapeshift (Creature - Cat)',
        16: 'Shapeshift (Ghost Wolf)',
        17: 'Shapeshift (Battle Stance)',
        18: 'Shapeshift (Defensive Stance)',
        19: 'Shapeshift (Berserker Stance)',
        21: 'Shapeshift (Zombie)',
        22: 'Shapeshift (Metamorphosis)',
        25: 'Shapeshift (Undead)',
        27: 'Shapeshift (Flight Form, Epic)',
        28: 'Shapeshift (Shadowform)',
        29: 'Shapeshift (Flight Form)',
        30: 'Shapeshift (Stealth)',
        31: 'Shapeshift (Moonkin Form)',
        32: 'Shapeshift (Spirit of Redemption)',
        35: 'Shapeshift (Moonkin Form)',
        36: 'Shapeshift (Treant Form)',
        37: 'Shapeshift (Spirit Owl Form)',
        38: 'Shapeshift (Spirit Owl Form)',
        39: 'Shapeshift (Wisp Form)',
        40: 'Shapeshift (Wisp Form)',
        41: 'Shapeshift (Soulshape)'
    },
    37: {
        1: 'Effect Immunity (Instakill)',
        5: 'Effect Immunity (Teleport)',
        6: 'Effect Immunity (Apply Aura)',
        9: 'Effect Immunity (Drain Health)',
        10: 'Effect Immunity (Heal)',
        30: 'Effect Immunity (Give Power)',
        62: 'Effect Immunity (Power Burn)',
        63: 'Effect Immunity (Threat)',
        67: 'Effect Immunity (Heal to Full)',
        68: 'Effect Immunity (Interrupt Cast)',
        85: 'Effect Immunity (Summon Player)',
        98: 'Effect Immunity (Knock Back)',
        114: 'Effect Immunity (Taunt)',
        124: 'Effect Immunity (Pull)',
        136: 'Effect Immunity (Heal for % of Total Health)',
        137: 'Effect Immunity (Give % of Total Power)',
        138: 'Effect Immunity (Jump)',
        144: 'Effect Immunity (Area Knockback)',
        145: 'Effect Immunity (Suspend Gravity)',
        178: 'Effect Immunity'
    },
    38: {
        7: 'State Immunity (Rooted)',
        11: 'State Immunity (Snared)',
        12: 'State Immunity (Stunned)',
        16: 'State Immunity (Healing)',
        18: 'State Immunity (Banished)',
        21: 'State Immunity (Mounted)',
        24: 'State Immunity (Horrified)',
        25: 'State Immunity (Invulnerable)',
        26: 'State Immunity (Interrupted)',
        27: 'State Immunity (Dazed)',
        31: 'State Immunity (Enraged)',
        33: 'State Immunity',
        53: 'State Immunity',
        56: 'State Immunity',
        61: 'State Immunity',
        118: 'State Immunity',
        127: 'State Immunity',
        239: 'State Immunity',
        321: 'State Immunity'
    },
    39: {
        1: 'Immunity (Physical)',
        2: 'Immunity (Holy)',
        4: 'Immunity (Fire)',
        8: 'Immunity (Nature)',
        16: 'Immunity (Frost)',
        32: 'Immunity (Shadow)',
        64: 'Immunity (Arcane)',
        125: 'Immunity (Arcane, Fire, Frost, Nature, Physical, Shadow)',
        126: 'Immunity (All)',
        127: 'Immunity (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        255: 'Immunity (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1919: 'Immunity (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        2047: 'Immunity (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        108415: 'Immunity (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    40: {
        -1: 'Immunity - Damage Only (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        0: 'Immunity - Damage Only',
        1: 'Immunity - Damage Only (Physical)',
        2: 'Immunity - Damage Only (Holy)',
        4: 'Immunity - Damage Only (Fire)',
        8: 'Immunity - Damage Only (Nature)',
        32: 'Immunity - Damage Only (Shadow)',
        64: 'Immunity - Damage Only (Arcane)',
        124: 'Immunity - Damage Only (Arcane, Fire, Frost, Nature, Shadow)',
        126: 'Immunity - Damage Only (All)',
        127: 'Immunity - Damage Only (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        772: 'Immunity - Damage Only (Fire)',
        895: 'Immunity - Damage Only (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1791: 'Immunity - Damage Only (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1919: 'Immunity - Damage Only (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        2047: 'Immunity - Damage Only (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        10111: 'Immunity - Damage Only (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        14079: 'Immunity - Damage Only (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        16877: 'Immunity - Damage Only (Arcane, Fire, Nature, Physical, Shadow)',
        84735: 'Immunity - Damage Only (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        109695: 'Immunity - Damage Only (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    41: {
        -1: 'Immunity - Debuffs Only',
        1: 'Immunity - Debuffs Only (Magic)',
        2: 'Immunity - Debuffs Only (Curse)',
        3: 'Immunity - Debuffs Only (Disease)',
        4: 'Immunity - Debuffs Only (Poison)',
        5: 'Immunity - Debuffs Only',
        6: 'Immunity - Debuffs Only'
    },
    42: {
        1: 'Proc Trigger Spell'
    },
    43: {
        1: 'Proc Trigger Damage'
    },
    44: {
        1: 'Track Creatures (Beast)',
        2: 'Track Creatures (Dragonkin)',
        3: 'Track Creatures (Demon)',
        4: 'Track Creatures (Elemental)',
        5: 'Track Creatures (Giant)',
        6: 'Track Creatures (Undead)',
        7: 'Track Creatures (Humanoid)',
        8: 'Track Creatures (Critter)',
        9: 'Track Creatures (Mechanical)',
        13: 'Track Creatures',
        14: 'Track Creatures'
    },
    45: {
        2: 'Track Resources (Herbalism)',
        3: 'Track Resources (Mining)',
        6: 'Track Resources',
        7: 'Track Resources',
        15: 'Track Resources',
        19: 'Track Resources',
        22: 'Track Resources',
        28: 'Track Resources',
        30: 'Track Resources',
        31: 'Track Resources'
    },
    46: {},
    47: {
        1: 'Mod Parry %'
    },
    48: {
        1: '?? (Aura #48)'
    },
    49: {
        1: 'Mod Dodge %'
    },
    50: {
        1: 'Mod Amount Healed by Critical Heals %'
    },
    51: {
        1: 'Mod Block %'
    },
    52: {
        1: 'Mod Melee & Ranged Crit %'
    },
    53: {
        1: 'Periodically Leech Health'
    },
    54: {
        1: 'Mod Melee & Ranged Hit Chance %'
    },
    55: {
        1: 'Mod Spell Hit Chance %'
    },
    56: {
        1: 'Change Model'
    },
    57: {
        1: 'Mod Spell Crit %'
    },
    58: {
        1: 'Increase Swim Speed %'
    },
    59: {
        0: 'Increase Physical Damage & Spell Damage',
        1: 'Increase Physical Damage & Spell Damage (Beast)',
        8: 'Increase Physical Damage & Spell Damage (Elemental)',
        32: 'Increase Physical Damage & Spell Damage (Undead)',
        64: 'Increase Physical Damage & Spell Damage (Humanoid)',
        16384: 'Increase Physical Damage & Spell Damage (Aberration)'
    },
    60: {
        0: 'Pacify & Silence'
    },
    61: {
        0: 'Mod Size %'
    },
    62: {
        1: 'Periodically Transfer Health'
    },
    63: {
        1: '?? (Aura #63)'
    },
    64: {
        0: 'Periodically Drain Power (Mana)',
        1: 'Periodically Drain Power (Rage)',
        3: 'Periodically Drain Power (Energy)'
    },
    65: {
        0: 'Mod Spell Haste %',
        1: 'Mod Spell Haste % (Physical)',
        4: 'Mod Spell Haste % (Fire)',
        7: 'Mod Spell Haste % (Fire, Holy, Physical)',
        10: 'Mod Spell Haste % (Holy, Nature)',
        126: 'Mod Spell Haste % (All)',
        127: 'Mod Spell Haste % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        137: 'Mod Spell Haste % (Nature, Physical)',
        842: 'Mod Spell Haste % (Arcane, Holy, Nature)',
        43922: 'Mod Spell Haste % (Frost, Holy)',
        524288: 'Mod Spell Haste %',
        917504: 'Mod Spell Haste %'
    },
    66: {
        1: 'Feign Death'
    },
    67: {
        1: 'Disarm'
    },
    68: {
        1: 'Stalked'
    },
    69: {
        -1: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        0: 'Absorb Damage',
        1: 'Absorb Damage (Physical)',
        2: 'Absorb Damage (Holy)',
        4: 'Absorb Damage (Fire)',
        5: 'Absorb Damage (Fire, Physical)',
        8: 'Absorb Damage (Nature)',
        16: 'Absorb Damage (Frost)',
        32: 'Absorb Damage (Shadow)',
        64: 'Absorb Damage (Arcane)',
        85: 'Absorb Damage (Arcane, Fire, Frost, Physical)',
        124: 'Absorb Damage (Arcane, Fire, Frost, Nature, Shadow)',
        126: 'Absorb Damage (All)',
        127: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        383: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        511: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        767: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1919: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        2303: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        6015: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        6783: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        16987: 'Absorb Damage (Arcane, Frost, Holy, Nature, Physical)',
        65663: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        72447: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        917631: 'Absorb Damage (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    70: {
        1: '?? (Aura #70)'
    },
    71: {
        1: 'Mod Spell Crit %'
    },
    72: {
        0: 'Mod Mana Cost %',
        2: 'Mod Mana Cost % (Holy)',
        32: 'Mod Mana Cost % (Shadow)',
        126: 'Mod Mana Cost % (All)',
        127: 'Mod Mana Cost % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    73: {
        10: 'Mod Mana Cost % (Holy, Nature)',
        16: 'Mod Mana Cost % (Frost)',
        126: 'Mod Mana Cost % (All)',
        127: 'Mod Mana Cost % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    74: {
        4: 'Reflect Spells (Fire)',
        8: 'Reflect Spells (Nature)',
        16: 'Reflect Spells (Frost)',
        20: 'Reflect Spells (Fire, Frost)',
        32: 'Reflect Spells (Shadow)',
        40: 'Reflect Spells (Nature, Shadow)',
        64: 'Reflect Spells (Arcane)',
        126: 'Reflect Spells (All)',
        127: 'Reflect Spells (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    75: {
        1: 'Force Language (Orcish)',
        6: 'Force Language (Dwarvish)',
        7: 'Force Language (Common)',
        8: 'Force Language (Demonic)',
        9: 'Force Language (Titan)',
        10: 'Force Language (Thalassian)',
        11: 'Force Language (Draconic)',
        36: 'Force Language (Zombie)',
        37: 'Force Language (Gnomish Binary)',
        38: 'Force Language (Goblin Binary)',
        178: "Force Language (Shath'Yar)",
        179: 'Force Language (Nerglish)',
        180: 'Force Language (Moonkin)'
    },
    76: {
        1: 'Far Sight'
    },
    77: {
        0: 'Immunity - Mechanic',
        1: 'Immunity - Mechanic (Charmed)',
        2: 'Immunity - Mechanic (Disoriented)',
        3: 'Immunity - Mechanic (Disarmed)',
        4: 'Immunity - Mechanic (Distracted)',
        5: 'Immunity - Mechanic (Fleeing)',
        6: 'Immunity - Mechanic (Gripped)',
        7: 'Immunity - Mechanic (Rooted)',
        9: 'Immunity - Mechanic (Silenced)',
        10: 'Immunity - Mechanic (Asleep)',
        11: 'Immunity - Mechanic (Snared)',
        12: 'Immunity - Mechanic (Stunned)',
        13: 'Immunity - Mechanic (Frozen)',
        14: 'Immunity - Mechanic (Incapacitated)',
        16: 'Immunity - Mechanic (Healing)',
        17: 'Immunity - Mechanic (Polymorphed)',
        18: 'Immunity - Mechanic (Banished)',
        19: 'Immunity - Mechanic (Shielded)',
        20: 'Immunity - Mechanic (Shackled)',
        21: 'Immunity - Mechanic (Mounted)',
        22: 'Immunity - Mechanic (Infected)',
        23: 'Immunity - Mechanic (Turned)',
        24: 'Immunity - Mechanic (Horrified)',
        25: 'Immunity - Mechanic (Invulnerable)',
        26: 'Immunity - Mechanic (Interrupted)',
        27: 'Immunity - Mechanic (Dazed)',
        29: 'Immunity - Mechanic (Invulnerable)',
        30: 'Immunity - Mechanic (Sapped)',
        33: 'Immunity - Mechanic',
        35: 'Immunity - Mechanic',
        36: 'Immunity - Mechanic',
        144: 'Immunity - Mechanic',
        1825: 'Immunity - Mechanic',
        2078: 'Immunity - Mechanic'
    },
    78: {
        1: 'Mounted'
    },
    79: {
        -124: 'Mod Damage Done % (Fire)',
        -112: 'Mod Damage Done % (Frost)',
        -64: 'Mod Damage Done % (Arcane)',
        -1: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        0: 'Mod Damage Done %',
        1: 'Mod Damage Done % (Physical)',
        2: 'Mod Damage Done % (Holy)',
        3: 'Mod Damage Done % (Holy, Physical)',
        4: 'Mod Damage Done % (Fire)',
        5: 'Mod Damage Done % (Fire, Physical)',
        8: 'Mod Damage Done % (Nature)',
        16: 'Mod Damage Done % (Frost)',
        20: 'Mod Damage Done % (Fire, Frost)',
        23: 'Mod Damage Done % (Fire, Frost, Holy, Physical)',
        28: 'Mod Damage Done % (Fire, Frost, Nature)',
        32: 'Mod Damage Done % (Shadow)',
        33: 'Mod Damage Done % (Physical, Shadow)',
        36: 'Mod Damage Done % (Fire, Shadow)',
        57: 'Mod Damage Done % (Frost, Nature, Physical, Shadow)',
        64: 'Mod Damage Done % (Arcane)',
        65: 'Mod Damage Done % (Arcane, Physical)',
        72: 'Mod Damage Done % (Arcane, Nature)',
        84: 'Mod Damage Done % (Arcane, Fire, Frost)',
        92: 'Mod Damage Done % (Arcane, Fire, Frost, Nature)',
        95: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical)',
        119: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Physical, Shadow)',
        126: 'Mod Damage Done % (All)',
        127: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        255: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        383: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        511: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        639: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        767: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        895: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1023: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1296: 'Mod Damage Done % (Frost)',
        1535: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1663: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1791: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1918: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Shadow)',
        2047: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        2815: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        3967: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        4223: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        11519: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        12031: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        16895: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        19327: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        27521: 'Mod Damage Done % (Physical)',
        33136: 'Mod Damage Done % (Arcane, Frost, Shadow)',
        65022: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Shadow)',
        85887: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        97663: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        98303: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        105343: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        160639: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        917631: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        33554468: 'Mod Damage Done % (Fire, Shadow)',
        33554559: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        34473855: 'Mod Damage Done % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    80: {
        -2: 'Mod Stat % (0)',
        -1: 'Mod Stat % (All)',
        0: 'Mod Stat % (Strength)',
        1: 'Mod Stat % (Agility)',
        2: 'Mod Stat % (Stamina)',
        3: 'Mod Stat % (Intellect)',
        7: 'Mod Stat % (0)'
    },
    81: {
        1: 'Split Damage % (Physical)',
        126: 'Split Damage % (All)',
        127: 'Split Damage % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    82: {
        1: 'Underwater Breathing'
    },
    83: {
        1: 'Mod Base Resistance Flat (Physical)',
        126: 'Mod Base Resistance Flat (All)'
    },
    84: {
        1: 'Health Regen'
    },
    85: {
        0: 'Power Regen (Mana)',
        2: 'Power Regen (Focus)',
        3: 'Power Regen (Energy)',
        13: 'Power Regen (Insanity)',
        17: 'Power Regen (Fury)'
    },
    86: {
        1: 'Create Item on Death'
    },
    87: {
        -127: 'Mod % Damage Taken (Physical)',
        -2: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Shadow)',
        -1: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        0: 'Mod % Damage Taken',
        1: 'Mod % Damage Taken (Physical)',
        2: 'Mod % Damage Taken (Holy)',
        4: 'Mod % Damage Taken (Fire)',
        8: 'Mod % Damage Taken (Nature)',
        9: 'Mod % Damage Taken (Nature, Physical)',
        10: 'Mod % Damage Taken (Holy, Nature)',
        16: 'Mod % Damage Taken (Frost)',
        17: 'Mod % Damage Taken (Frost, Physical)',
        20: 'Mod % Damage Taken (Fire, Frost)',
        24: 'Mod % Damage Taken (Frost, Nature)',
        28: 'Mod % Damage Taken (Fire, Frost, Nature)',
        32: 'Mod % Damage Taken (Shadow)',
        36: 'Mod % Damage Taken (Fire, Shadow)',
        40: 'Mod % Damage Taken (Nature, Shadow)',
        64: 'Mod % Damage Taken (Arcane)',
        65: 'Mod % Damage Taken (Arcane, Physical)',
        72: 'Mod % Damage Taken (Arcane, Nature)',
        84: 'Mod % Damage Taken (Arcane, Fire, Frost)',
        96: 'Mod % Damage Taken (Arcane, Shadow)',
        112: 'Mod % Damage Taken (Arcane, Frost, Shadow)',
        122: 'Mod % Damage Taken (Arcane, Frost, Holy, Nature, Shadow)',
        124: 'Mod % Damage Taken (Arcane, Fire, Frost, Nature, Shadow)',
        126: 'Mod % Damage Taken (All)',
        127: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        511: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        894: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Shadow)',
        1023: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1279: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1407: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1663: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        2047: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        2687: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        2815: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        2948: 'Mod % Damage Taken (Fire)',
        7423: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        11007: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        11647: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        12159: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        41736: 'Mod % Damage Taken (Nature)',
        43391: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        56959: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        70655: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        97663: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        130687: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        917631: 'Mod % Damage Taken (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    88: {
        1: 'Mod Health Regen %'
    },
    89: {
        1: 'Mod Periodic Damage %'
    },
    90: {
        1: '?? (Aura #90)'
    },
    91: {
        1: 'Mod Aggro Range'
    },
    92: {
        1: 'Cannot Flee'
    },
    93: {
        1: 'Unattackable'
    },
    94: {
        1: 'Interrupt Power Decay'
    },
    95: {
        1: 'Ghost'
    },
    96: {
        1: 'Magnet'
    },
    97: {
        1: 'Absorb Damage - Mana Shield (Physical)',
        64: 'Absorb Damage - Mana Shield (Arcane)',
        126: 'Absorb Damage - Mana Shield (All)',
        127: 'Absorb Damage - Mana Shield (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    98: {
        1: 'Mod Skill'
    },
    99: {
        1: 'Mod Melee Attack Power'
    },
    100: {
        1: 'Always Show Debuffs (Obsolete)'
    },
    101: {
        0: 'Mod Resistance %',
        1: 'Mod Resistance % (Physical)',
        4: 'Mod Resistance % (Fire)',
        5: 'Mod Resistance % (Fire, Physical)',
        8: 'Mod Resistance % (Nature)',
        48: 'Mod Resistance % (Frost, Shadow)',
        64: 'Mod Resistance % (Arcane)',
        127: 'Mod Resistance % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1916741503: 'Mod Resistance % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    102: {
        1: 'Mod Melee Attack Power vs Creature (Beast)',
        2: 'Mod Melee Attack Power vs Creature (Dragonkin)',
        4: 'Mod Melee Attack Power vs Creature (Demon)',
        8: 'Mod Melee Attack Power vs Creature (Elemental)',
        16: 'Mod Melee Attack Power vs Creature (Giant)',
        32: 'Mod Melee Attack Power vs Creature (Undead)',
        36: 'Mod Melee Attack Power vs Creature (Demon, Undead)',
        1064960: 'Mod Melee Attack Power vs Creature (Aberration)'
    },
    103: {
        1: 'Mod Threat Flat - Temporary'
    },
    104: {
        1: 'Water Walking'
    },
    105: {
        1: 'Slow Fall'
    },
    106: {
        1: 'Levitate / Hover'
    },
    107: {
        0: 'Modifies Damage/Healing Done',
        1: 'Modifies Buff Duration',
        2: 'Modifies Threat',
        3: "Modifies Effect #1's Value",
        4: 'Modifies Charges',
        5: 'Modifies Range',
        6: 'Modifies Radius',
        7: 'Modifies Critical Strike Chance',
        8: 'Modifies Spell Effectiveness',
        10: 'Modifies Cast Time',
        11: 'Modifies Cooldown',
        12: "Modifies Effect #2's Value",
        14: 'Modifies Power Cost',
        15: 'Modifies Critical Strike Damage',
        17: 'Modifies Jump Targets',
        18: 'Modifies Proc Chance',
        19: 'Modifies Time Between Ticks',
        20: 'Modifies Effectiveness After First Target',
        21: 'Modifies Global Cooldown',
        22: 'Modifies Periodic Damage/Healing Done',
        23: "Modifies Effect #3's Value",
        24: 'Add Modifier - Flat',
        31: 'Add Modifier - Flat',
        32: "Modifies Effect #4's Value",
        33: "Modifies Effect #5's Value",
        34: 'Add Modifier - Flat',
        35: 'Add Modifier - Flat',
        37: 'Add Modifier - Flat',
        1428: 'Add Modifier - Flat'
    },
    108: {
        0: 'Modifies Damage/Healing Done',
        1: 'Modifies Buff Duration',
        2: 'Modifies Threat',
        3: "Modifies Effect #1's Value",
        5: 'Modifies Range',
        6: 'Modifies Radius',
        7: 'Modifies Critical Strike Chance',
        8: 'Modifies Spell Effectiveness',
        9: 'Modifies Pushback Reduction',
        10: 'Modifies Cast Time',
        11: 'Modifies Cooldown',
        12: "Modifies Effect #2's Value",
        14: 'Modifies Power Cost',
        15: 'Modifies Critical Strike Damage',
        16: 'Modifies Hit Chance',
        18: 'Modifies Proc Chance',
        19: 'Modifies Time Between Ticks',
        20: 'Modifies Effectiveness After First Target',
        21: 'Modifies Global Cooldown',
        22: 'Modifies Periodic Damage/Healing Done',
        23: "Modifies Effect #3's Value",
        26: 'Add Modifier - %',
        27: 'Add Modifier - %',
        32: "Modifies Effect #4's Value",
        33: "Modifies Effect #5's Value",
        34: 'Add Modifier - %',
        35: 'Add Modifier - %',
        38: 'Add Modifier - %',
        39: 'Add Modifier - %'
    },
    109: {
        1: 'Proc Spell on Target'
    },
    110: {
        0: 'Mod Power Regen % (Mana)',
        2: 'Mod Power Regen % (Focus)',
        3: 'Mod Power Regen % (Energy)',
        4: 'Mod Power Regen % (Combo Point)',
        5: 'Mod Power Regen % (Rune)',
        6: 'Mod Power Regen % (Runic Power)',
        7: 'Mod Power Regen % (Soul Shard)',
        8: 'Mod Power Regen % (Astral Power)',
        9: 'Mod Power Regen % (Holy Power)',
        10: 'Mod Power Regen % (Alternate)',
        11: 'Mod Power Regen % (Maelstrom)',
        12: 'Mod Power Regen % (Chi)',
        13: 'Mod Power Regen % (Insanity)',
        16: 'Mod Power Regen % (Arcane Charge)',
        17: 'Mod Power Regen % (Fury)',
        18: 'Mod Power Regen % (Pain)'
    },
    111: {
        1: 'Intercept % of all Melee & Ranged Attacks'
    },
    112: {
        1: 'Override Class Script'
    },
    113: {
        1: 'Mod Ranged Damage Taken - Flat'
    },
    114: {
        1: 'Mod Ranged Damage Taken - %'
    },
    115: {
        0: 'Mod Healing Taken - Flat',
        126: 'Mod Healing Taken - Flat (All)',
        127: 'Mod Healing Taken - Flat (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    116: {
        1: 'Allow % of Health Regeneration to Continue in Combat'
    },
    117: {
        2: 'Give % Chance to Resist Mechanic (Snared)',
        5: 'Give % Chance to Resist Mechanic (Fleeing)',
        7: 'Give % Chance to Resist Mechanic (Rooted)',
        9: '',
        11: 'Give % Chance to Resist Mechanic (Snared)',
        12: 'Give % Chance to Resist Mechanic (Stunned)',
        26: 'Give % Chance to Resist Mechanic (Interrupted)'
    },
    118: {
        0: 'Mod Healing Taken - %',
        1: 'Mod Healing Taken - % (Physical)',
        4: 'Mod Healing Taken - % (Fire)',
        8: 'Mod Healing Taken - % (Nature)',
        126: 'Mod Healing Taken - % (All)',
        127: 'Mod Healing Taken - % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        383: 'Mod Healing Taken - % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1023: 'Mod Healing Taken - % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        2687: 'Mod Healing Taken - % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1879048192: 'Mod Healing Taken - %'
    },
    119: {
        1: '?? (Aura #119)'
    },
    120: {
        1: 'Untrackable'
    },
    121: {
        1: 'Beast Lore'
    },
    122: {
        1: 'Mod Off-Hand Damage Done %'
    },
    123: {
        1: 'Reduce Target Resistances - Flat (Physical)',
        4: 'Reduce Target Resistances - Flat (Fire)',
        124: 'Reduce Target Resistances - Flat (Arcane, Fire, Frost, Nature, Shadow)',
        126: 'Reduce Target Resistances - Flat (All)'
    },
    124: {
        1: 'Mod Ranged Attack Power'
    },
    125: {
        1: 'Mod Melee Damage Taken'
    },
    126: {
        1: 'Mod Melee Damage Taken - %'
    },
    127: {
        1: 'Mod Attacker Ranged Attack Power'
    },
    128: {
        1: 'Take Control of Pet'
    },
    129: {
        1: 'Increase Run Speed % - Stacks'
    },
    130: {
        1: 'Incerase Mounted Speed % - Stacks'
    },
    131: {
        1: 'Mod Ranged Attack Power vs Creature (Beast)',
        2: 'Mod Ranged Attack Power vs Creature (Dragonkin)',
        4: 'Mod Ranged Attack Power vs Creature (Demon)',
        8: 'Mod Ranged Attack Power vs Creature (Elemental)',
        16: 'Mod Ranged Attack Power vs Creature (Giant)',
        32: 'Mod Ranged Attack Power vs Creature (Undead)',
        36: 'Mod Ranged Attack Power vs Creature (Demon, Undead)',
        1064960: 'Mod Ranged Attack Power vs Creature (Aberration)'
    },
    132: {
        0: 'Mod Increase Maximum Power - % (Mana)',
        1: 'Mod Increase Maximum Power - % (Rage)',
        2: 'Mod Increase Maximum Power - % (Focus)',
        3: 'Mod Increase Maximum Power - % (Energy)',
        6: 'Mod Increase Maximum Power - % (Runic Power)'
    },
    133: {
        0: 'Mod Increase Maximum Health - %',
        2: 'Mod Increase Maximum Health - %',
        32: 'Mod Increase Maximum Health - %',
        127: 'Mod Increase Maximum Health - %',
        173: 'Mod Increase Maximum Health - %',
        895: 'Mod Increase Maximum Health - %',
        939: 'Mod Increase Maximum Health - %',
        72349: 'Mod Increase Maximum Health - %',
        73462: 'Mod Increase Maximum Health - %',
        34473728: 'Mod Increase Maximum Health - %'
    },
    134: {
        1: 'Allow % of Mana Regeneration to Continue in Combat'
    },
    135: {
        0: 'Mod Healing Power',
        2: 'Mod Healing Power (Holy)',
        126: 'Mod Healing Power (All)',
        127: 'Mod Healing Power (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    136: {
        -1: 'Mod Healing Power - % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        0: 'Mod Healing Power - %',
        1: 'Mod Healing Power - % (Physical)',
        2: 'Mod Healing Power - % (Holy)',
        4: 'Mod Healing Power - % (Fire)',
        8: 'Mod Healing Power - % (Nature)',
        10: 'Mod Healing Power - % (Holy, Nature)',
        12: 'Mod Healing Power - % (Fire, Nature)',
        16: 'Mod Healing Power - % (Frost)',
        32: 'Mod Healing Power - % (Shadow)',
        64: 'Mod Healing Power - % (Arcane)',
        126: 'Mod Healing Power - % (All)',
        127: 'Mod Healing Power - % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        895: 'Mod Healing Power - % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1023: 'Mod Healing Power - % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        12031: 'Mod Healing Power - % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    137: {
        -1: 'Mod Stat - % (Strength, Agility, Stamina, Intellect)',
        0: 'Mod Stat - %',
        1: 'Mod Stat - % (Strength, Agility, Intellect)',
        2: 'Mod Stat - % (Stamina)',
        3: 'Mod Stat - % (Strength, Agility, Intellect)',
        4: 'Mod Stat - % (Intellect)'
    },
    138: {
        1: 'Mod Melee Attack Speed - %'
    },
    139: {
        1: 'Force Reputation'
    },
    140: {
        0: 'Mod Ranged Attack Speed - %',
        12: 'Mod Ranged Attack Speed - %'
    },
    141: {
        1: 'Mod Ranged Attack Speed - % - Ammo Only'
    },
    142: {
        -127: 'Mod Base Resistance - % (Physical)',
        0: 'Mod Base Resistance - %',
        1: 'Mod Base Resistance - % (Physical)',
        4: 'Mod Base Resistance - % (Fire)',
        8: 'Mod Base Resistance - % (Nature)',
        16: 'Mod Base Resistance - % (Frost)',
        32: 'Mod Base Resistance - % (Shadow)',
        64: 'Mod Base Resistance - % (Arcane)'
    },
    143: {
        16: 'Mod Resistance - Flat - Does not Stack (Frost)',
        20: 'Mod Resistance - Flat - Does not Stack (Fire, Frost)',
        173: 'Mod Resistance - Flat - Does not Stack (Fire, Nature, Physical, Shadow)',
        174: 'Mod Resistance - Flat - Does not Stack (Fire, Holy, Nature, Shadow)',
        177: 'Mod Resistance - Flat - Does not Stack (Frost, Physical, Shadow)',
        183: 'Mod Resistance - Flat - Does not Stack (Fire, Frost, Holy, Physical, Shadow)',
        184: 'Mod Resistance - Flat - Does not Stack (Frost, Nature, Shadow)',
        189: 'Mod Resistance - Flat - Does not Stack (Fire, Frost, Nature, Physical, Shadow)',
        203: 'Mod Resistance - Flat - Does not Stack (Arcane, Holy, Nature, Physical)',
        219: 'Mod Resistance - Flat - Does not Stack (Arcane, Frost, Holy, Nature, Physical)',
        359: 'Mod Resistance - Flat - Does not Stack (Arcane, Fire, Holy, Physical, Shadow)'
    },
    144: {
        1: 'Reduce Falling Damage by %'
    },
    145: {
        1: 'Increase Pet Talent Points'
    },
    146: {
        1: 'Allow Exotic Pets Taming'
    },
    147: {
        95: 'Add Creature Immunity (?) (Charmed, Disarmed, Disoriented, Distracted, Fleeing, Rooted)',
        96: 'Add Creature Immunity (?) (Gripped, Rooted)',
        315: 'Add Creature Immunity (?) (Charmed, Gripped, Disoriented, Distracted, Fleeing, Silenced)',
        477: 'Add Creature Immunity (?) (Charmed, Disarmed, Distracted, Fleeing, Slowed, Rooted, Silenced)',
        679: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disarmed, Disoriented, Slowed)',
        878: 'Add Creature Immunity (?) (Asleep, Gripped, Disarmed, Disoriented, Distracted, Rooted, Silenced)',
        937: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Distracted, Slowed, Silenced)',
        1537: 'Add Creature Immunity (?) (Asleep, Charmed, Snared)',
        1557: 'Add Creature Immunity (?) (Asleep, Charmed, Disarmed, Snared, Fleeing)',
        1614: 'Add Creature Immunity (?) (Asleep, Disarmed, Disoriented, Distracted, Snared, Rooted)',
        1615: 'Add Creature Immunity (?) (Asleep, Charmed, Disarmed, Disoriented, Distracted, Snared, Rooted)',
        1630: 'Add Creature Immunity (?) (Asleep, Disarmed, Disoriented, Distracted, Snared, Fleeing, Rooted)',
        1632: 'Add Creature Immunity (?) (Asleep, Gripped, Snared, Rooted)',
        1636: 'Add Creature Immunity (?) (Asleep, Gripped, Disarmed, Snared, Rooted)',
        1664: 'Add Creature Immunity (?) (Asleep, Snared, Slowed)',
        1670: 'Add Creature Immunity (?) (Asleep, Disarmed, Disoriented, Snared, Slowed)',
        1676: 'Add Creature Immunity (?) (Asleep, Disarmed, Distracted, Snared, Slowed)',
        1682: 'Add Creature Immunity (?) (Asleep, Disoriented, Snared, Fleeing, Slowed)',
        1693: 'Add Creature Immunity (?) (Asleep, Charmed, Disarmed, Distracted, Snared, Fleeing, Slowed)',
        1694: 'Add Creature Immunity (?) (Asleep, Disarmed, Disoriented, Distracted, Snared, Fleeing, Slowed)',
        1700: 'Add Creature Immunity (?) (Asleep, Gripped, Disarmed, Snared, Slowed)',
        1701: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disarmed, Snared, Slowed)',
        1702: 'Add Creature Immunity (?) (Asleep, Gripped, Disarmed, Disoriented, Snared, Slowed)',
        1720: 'Add Creature Immunity (?) (Asleep, Gripped, Distracted, Snared, Fleeing, Slowed)',
        1733: 'Add Creature Immunity (?) (Asleep, Charmed, Disarmed, Snared, Slowed, Rooted)',
        1748: 'Add Creature Immunity (?) (Asleep, Disarmed, Snared, Fleeing, Slowed, Rooted)',
        1762: 'Add Creature Immunity (?) (Asleep, Gripped, Disoriented, Snared, Slowed, Rooted)',
        1765: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disarmed, Snared, Slowed, Rooted)',
        1771: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disoriented, Distracted, Snared, Slowed, Rooted)',
        1772: 'Add Creature Immunity (?) (Asleep, Gripped, Disarmed, Distracted, Snared, Slowed, Rooted)',
        1773: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disarmed, Distracted, Snared, Slowed, Rooted)',
        1774: 'Add Creature Immunity (?) (Asleep, Gripped, Disarmed, Disoriented, Distracted, Snared, Slowed, Rooted)',
        1791: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disarmed, Disoriented, Distracted, Snared, Fleeing, Slowed, Rooted)',
        1794: 'Add Creature Immunity (?) (Asleep, Disoriented, Snared, Silenced)',
        1799: 'Add Creature Immunity (?) (Asleep, Charmed, Disarmed, Disoriented, Snared, Silenced)',
        1800: 'Add Creature Immunity (?) (Asleep, Distracted, Snared, Silenced)',
        1803: 'Add Creature Immunity (?) (Asleep, Charmed, Disoriented, Distracted, Snared, Silenced)',
        1808: 'Add Creature Immunity (?) (Asleep, Snared, Fleeing, Silenced)',
        1810: 'Add Creature Immunity (?) (Asleep, Disoriented, Snared, Fleeing, Silenced)',
        1825: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Snared, Silenced)',
        1835: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disoriented, Distracted, Snared, Silenced)',
        1839: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disarmed, Disoriented, Distracted, Snared, Silenced)',
        1843: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disoriented, Snared, Fleeing, Silenced)',
        1869: 'Add Creature Immunity (?) (Asleep, Charmed, Disarmed, Distracted, Snared, Rooted, Silenced)',
        1874: 'Add Creature Immunity (?) (Asleep, Disoriented, Snared, Fleeing, Rooted, Silenced)',
        1877: 'Add Creature Immunity (?) (Asleep, Charmed, Disarmed, Snared, Fleeing, Rooted, Silenced)',
        1882: 'Add Creature Immunity (?) (Asleep, Disoriented, Distracted, Snared, Fleeing, Rooted, Silenced)',
        1887: 'Add Creature Immunity (?) (Asleep, Charmed, Disarmed, Disoriented, Distracted, Snared, Fleeing, Rooted, Silenced)',
        1892: 'Add Creature Immunity (?) (Asleep, Gripped, Disarmed, Snared, Rooted, Silenced)',
        1893: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disarmed, Snared, Rooted, Silenced)',
        1921: 'Add Creature Immunity (?) (Asleep, Charmed, Snared, Slowed, Silenced)',
        1928: 'Add Creature Immunity (?) (Asleep, Distracted, Snared, Slowed, Silenced)',
        1944: 'Add Creature Immunity (?) (Asleep, Distracted, Snared, Fleeing, Slowed, Silenced)',
        1955: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disoriented, Snared, Slowed, Silenced)',
        1964: 'Add Creature Immunity (?) (Asleep, Gripped, Disarmed, Distracted, Snared, Slowed, Silenced)',
        1971: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disoriented, Snared, Fleeing, Slowed, Silenced)',
        1980: 'Add Creature Immunity (?) (Asleep, Gripped, Disarmed, Distracted, Snared, Fleeing, Slowed, Silenced)',
        1984: 'Add Creature Immunity (?) (Asleep, Snared, Slowed, Rooted, Silenced)',
        1985: 'Add Creature Immunity (?) (Asleep, Charmed, Snared, Slowed, Rooted, Silenced)',
        1991: 'Add Creature Immunity (?) (Asleep, Charmed, Disarmed, Disoriented, Snared, Slowed, Rooted, Silenced)',
        1994: 'Add Creature Immunity (?) (Asleep, Disoriented, Distracted, Snared, Slowed, Rooted, Silenced)',
        2005: 'Add Creature Immunity (?) (Asleep, Charmed, Disarmed, Snared, Fleeing, Slowed, Rooted, Silenced)',
        2010: 'Add Creature Immunity (?) (Asleep, Disoriented, Distracted, Snared, Fleeing, Slowed, Rooted, Silenced)',
        2018: 'Add Creature Immunity (?) (Asleep, Gripped, Disoriented, Snared, Slowed, Rooted, Silenced)',
        2035: 'Add Creature Immunity (?) (Asleep, Charmed, Gripped, Disoriented, Snared, Fleeing, Slowed, Rooted, Silenced)',
        2053: 'Add Creature Immunity (?) (Charmed, Disarmed, Stunned)',
        2065: 'Add Creature Immunity (?) (Charmed, Fleeing, Stunned)',
        2071: 'Add Creature Immunity (?) (Charmed, Disarmed, Disoriented, Fleeing, Stunned)',
        2081: 'Add Creature Immunity (?) (Charmed, Gripped, Stunned)',
        2107: 'Add Creature Immunity (?) (Charmed, Gripped, Disoriented, Distracted, Fleeing, Stunned)',
        2125: 'Add Creature Immunity (?) (Charmed, Disarmed, Distracted, Rooted, Stunned)',
        2129: 'Add Creature Immunity (?) (Charmed, Fleeing, Rooted, Stunned)',
        2142: 'Add Creature Immunity (?) (Disarmed, Disoriented, Distracted, Fleeing, Rooted, Stunned)',
        2262: 'Add Creature Immunity (?) (Disarmed, Disoriented, Fleeing, Slowed, Rooted, Stunned)',
        2283: 'Add Creature Immunity (?) (Charmed, Gripped, Disoriented, Distracted, Slowed, Rooted, Stunned)',
        2299: 'Add Creature Immunity (?) (Charmed, Gripped, Disoriented, Distracted, Fleeing, Slowed, Rooted, Stunned)'
    },
    148: {
        1: 'Add Combo Points for 20 Seconds'
    },
    149: {
        0: 'Decrease Pushback Time by %',
        3: 'Decrease Pushback Time by % (Holy, Physical)',
        10: 'Decrease Pushback Time by % (Holy, Nature)',
        126: 'Decrease Pushback Time by % (All)',
        127: 'Decrease Pushback Time by % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    150: {
        1: 'Mod Block Value - %'
    },
    151: {
        1: 'Track Hidden'
    },
    152: {
        1: 'Mod Aggro Range of Mobs Against You'
    },
    153: {
        1: '?? (Aura #153)'
    },
    154: {
        1: 'Mod Stealth Effectiveness'
    },
    155: {
        1: 'Underwater Breathing'
    },
    156: {
        1: 'Mod All Reputation Gained by %'
    },
    157: {
        1: 'Mod All Pet Damage Taken'
    },
    158: {
        1: 'Mod Block Value'
    },
    159: {
        1: 'Worth No Honor'
    },
    160: {},
    161: {
        1: 'Regen Health - Works in Combat'
    },
    162: {
        0: 'Power Burn (Mana)',
        1: 'Power Burn (Rage)',
        2: 'Power Burn (Focus)',
        3: 'Power Burn (Energy)',
        6: 'Power Burn (Runic Power)',
        8: 'Power Burn (Astral Power)',
        10: 'Power Burn (Alternate)',
        11: 'Power Burn (Maelstrom)',
        13: 'Power Burn (Insanity)',
        17: 'Power Burn (Fury)',
        18: 'Power Burn (Pain)'
    },
    163: {
        0: 'Mod Melee Critical Damage %',
        1: 'Mod Melee Critical Damage % (Physical)',
        4: 'Mod Melee Critical Damage % (Fire)',
        126: 'Mod Melee Critical Damage % (All)',
        127: 'Mod Melee Critical Damage % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        895: 'Mod Melee Critical Damage % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        1879048319: 'Mod Melee Critical Damage % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    164: {
        1: '?? (Aura #164)'
    },
    165: {
        1: 'Marked by a Guard'
    },
    166: {
        1: 'Mod Melee Attack Power - %'
    },
    167: {
        1: 'Mod Ranged Attack Power - %'
    },
    168: {
        0: 'Mod All Damage Done Against Creature - %',
        1: 'Mod All Damage Done Against Creature - % (Beast)',
        2: 'Mod All Damage Done Against Creature - % (Dragonkin)',
        4: 'Mod All Damage Done Against Creature - % (Demon)',
        8: 'Mod All Damage Done Against Creature - % (Elemental)',
        16: 'Mod All Damage Done Against Creature - % (Giant)',
        24: 'Mod All Damage Done Against Creature - % (Elemental, Giant)',
        32: 'Mod All Damage Done Against Creature - % (Undead)',
        36: 'Mod All Damage Done Against Creature - % (Demon, Undead)',
        64: 'Mod All Damage Done Against Creature - % (Humanoid)',
        127: 'Mod All Damage Done Against Creature - % (Beast, Demon, Dragonkin, Elemental, Giant, Humanoid, Undead)',
        128: 'Mod All Damage Done Against Creature - % (Critter)',
        256: 'Mod All Damage Done Against Creature - % (Mechanical)',
        512: 'Mod All Damage Done Against Creature - % (Uncategorized)',
        16384: 'Mod All Damage Done Against Creature - % (Aberration)'
    },
    169: {
        1: '?? (Aura #169)'
    },
    170: {
        1: 'Make a Certain Object Visible'
    },
    171: {
        1: 'Mod Mounted Speed % - Stacks'
    },
    172: {
        1: "Mod Mounted Speed % - Doesn't Stack with Anything"
    },
    173: {
        1: '?? (Aura #173)',
        17: '?? (Aura #173)',
        180: '?? (Aura #173)',
        216: '?? (Aura #173)',
        1201: '?? (Aura #173)'
    },
    174: {
        1: 'Mod Spell Power by % of Stat (All)'
    },
    175: {
        1: 'Mod Healing Power by % of Stat (Intellect)'
    },
    176: {
        1: 'Spirit of Redemption'
    },
    177: {
        1: 'Mind Control (AoE only?)'
    },
    178: {
        1: 'Mod Debuff Resistance - %'
    },
    179: {
        0: 'Mod Attacker Crit Chance %',
        8: 'Mod Attacker Crit Chance % (Nature)',
        11: 'Mod Attacker Crit Chance % (Holy, Nature, Physical)',
        13: 'Mod Attacker Crit Chance % (Fire, Nature, Physical)',
        18: 'Mod Attacker Crit Chance % (Frost, Holy)'
    },
    180: {
        4: 'Mod Spell Power Against Creature (Demon)',
        32: 'Mod Spell Power Against Creature (Undead)',
        36: 'Mod Spell Power Against Creature (Demon, Undead)'
    },
    181: {
        1: '?? (Aura #181)'
    },
    182: {
        1: 'Mod Resistance by % of Stat'
    },
    183: {
        1: 'Mod Threat % of Critical Hits'
    },
    184: {
        1: 'Mod Attacker Melee Hit Chance - %'
    },
    185: {
        1: 'Mod Attacker Ranged Hit Chance - %'
    },
    186: {
        1: 'Mod Attacker Spell Hit Chance - %'
    },
    187: {
        1: 'Mod Attacker Melee Crit Chance - %'
    },
    188: {
        1: 'Mod Attacker Ranged Crit Chance - %'
    },
    189: {
        1: 'Mod Rating'
    },
    190: {
        1: 'Mod Reputation Gained %'
    },
    191: {
        1: 'Run Speed Limit %'
    },
    192: {
        1: 'Increase Attack Speed %'
    },
    193: {
        1: 'Decrease Attack Speed %'
    },
    194: {
        28: 'Bypass Damage Reduction Effects (Fire, Frost, Nature)',
        40: 'Bypass Damage Reduction Effects (Nature, Shadow)',
        127: 'Bypass Damage Reduction Effects (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    195: {
        16931: '?? (Aura #195) (Holy, Physical, Shadow)',
        169340: '?? (Aura #195) (Arcane, Fire, Frost, Nature, Shadow)',
        197524: '?? (Aura #195) (Fire, Frost)',
        295089: '?? (Aura #195) (Frost, Physical, Shadow)',
        295258: '?? (Aura #195) (Arcane, Frost, Holy, Nature)',
        299046: '?? (Aura #195) (Fire, Holy, Shadow)',
        299204: '?? (Aura #195) (Arcane, Fire)',
        304971: '?? (Aura #195) (Arcane, Holy, Nature, Physical)',
        306701: '?? (Aura #195) (Fire, Nature, Physical)',
        306830: '?? (Aura #195) (Fire, Holy, Nature)',
        307411: '?? (Aura #195) (Arcane, Frost, Holy, Physical)',
        307443: '?? (Aura #195) (Arcane, Frost, Holy, Physical, Shadow)',
        307865: '?? (Aura #195) (Frost, Nature, Physical)',
        308491: '?? (Aura #195) (Holy, Nature, Physical)',
        310454: '?? (Aura #195) (Fire, Frost, Holy, Shadow)',
        311291: '?? (Aura #195) (Arcane, Frost, Holy, Nature, Physical, Shadow)',
        312202: '?? (Aura #195) (Holy, Nature)',
        312321: '?? (Aura #195) (Physical)',
        312749: '?? (Aura #195) (Fire, Nature, Physical, Shadow)',
        316449: '?? (Aura #195) (Physical, Shadow)',
        321395: '?? (Aura #195) (Arcane, Frost, Holy, Physical, Shadow)',
        323427: '?? (Aura #195) (Arcane, Holy, Physical, Shadow)',
        323547: '?? (Aura #195) (Arcane, Frost, Holy, Nature, Physical)',
        324386: '?? (Aura #195) (Holy, Shadow)',
        324547: '?? (Aura #195) (Arcane, Holy, Physical)',
        324559: '?? (Aura #195) (Arcane, Fire, Holy, Nature, Physical)',
        324739: '?? (Aura #195) (Holy, Physical)',
        325013: '?? (Aura #195) (Fire, Frost, Physical)'
    },
    196: {
        1: 'Increase All Cooldowns'
    },
    197: {
        0: 'Mod Chance to be Critically Hit %',
        7: 'Mod Chance to be Critically Hit % (Fire, Holy, Physical)',
        127: 'Mod Chance to be Critically Hit % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    198: {
        1: '?? (Aura #198)'
    },
    199: {
        1: 'Mod Spell Hit Chance %'
    },
    200: {
        1: 'Mod Experience Gained % (mob kills only)'
    },
    201: {
        1: 'Cannot dodge, block or parry'
    },
    202: {},
    203: {
        1: 'Mod Melee Crit Damage Taken by %'
    },
    204: {
        1: 'Mod Ranged Crit Damage Taken by %'
    },
    205: {
        1: 'Mod Spell Crit Damage Taken by % (Physical)'
    },
    206: {
        1: 'Mod Flight Speed % - Stacks'
    },
    207: {
        1: 'Mod Flight Speed %'
    },
    208: {
        1: 'Mod Flight Speed %'
    },
    209: {
        1: 'Mod Mounted Speed %'
    },
    210: {
        1: 'Mod Flight Speed %'
    },
    211: {
        1: 'Mod Mounted Speed % (ground + flying)'
    },
    212: {
        1: 'Mod Ranged Attack Power by % of Stat'
    },
    213: {
        1: 'Mod Rage % Generated From Damage Dealt'
    },
    214: {
        1: 'Tamed Pet Passive'
    },
    215: {
        1: 'Arena Preparation'
    },
    216: {
        1: 'Mod Casting Speed - %'
    },
    217: {
        1: '?? (Aura #217)'
    },
    218: {
        1: 'Aura Unknown - %'
    },
    219: {
        1: 'Mod Mana Regeneration by % of Stat'
    },
    220: {
        1: 'Mod Combat Rating by % of Stat'
    },
    221: {
        1: 'Ignored'
    },
    222: {
        1: '?? (Aura #222)'
    },
    223: {
        1: '?? (Aura #223)'
    },
    224: {
        1: '?? (Aura #224)'
    },
    225: {
        1: '?? (Aura #225)'
    },
    226: {
        0: 'Periodic Dummy'
    },
    227: {
        1: 'Periodically Trigger Spell with Value'
    },
    228: {
        1: 'Stealth Detection (Always)'
    },
    229: {
        0: 'Mod AoE Damage Taken %',
        4: 'Mod AoE Damage Taken % (Fire)',
        32: 'Mod AoE Damage Taken % (Shadow)',
        92: 'Mod AoE Damage Taken % (Arcane, Fire, Frost, Nature)',
        127: 'Mod AoE Damage Taken % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        255: 'Mod AoE Damage Taken % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        34472063: 'Mod AoE Damage Taken % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    230: {
        1: 'Mod Max Health'
    },
    231: {
        1: '?? (Aura #231)'
    },
    232: {
        0: 'Mod Mechanic Duration %',
        1: 'Mod Mechanic Duration % (Charmed)',
        2: 'Mod Mechanic Duration % (Disoriented)',
        5: 'Mod Mechanic Duration % (Fleeing)',
        7: 'Mod Mechanic Duration % (Rooted)',
        9: 'Mod Mechanic Duration % (Silenced)',
        10: 'Mod Mechanic Duration % (Asleep)',
        11: 'Mod Mechanic Duration % (Snared)',
        12: 'Mod Mechanic Duration % (Stunned)',
        13: 'Mod Mechanic Duration % (Frozen)',
        14: 'Mod Mechanic Duration % (Incapacitated)',
        17: 'Mod Mechanic Duration % (Polymorphed)',
        18: 'Mod Mechanic Duration % (Banished)',
        23: 'Mod Mechanic Duration % (Turned)',
        24: 'Mod Mechanic Duration % (Horrified)',
        26: 'Mod Mechanic Duration % (Interrupted)',
        27: 'Mod Mechanic Duration % (Dazed)',
        30: 'Mod Mechanic Duration % (Sapped)',
        1825: 'Mod Mechanic Duration %'
    },
    233: {
        1: 'Change Model of Every Humanoid Seen'
    },
    234: {
        1: 'Mod Mechanic Duration % - Does not Stack (Charmed)',
        2: 'Mod Mechanic Duration % - Does not Stack (Disoriented)',
        3: 'Mod Mechanic Duration % - Does not Stack (Disarmed)',
        5: 'Mod Mechanic Duration % - Does not Stack (Fleeing)',
        7: 'Mod Mechanic Duration % - Does not Stack (Rooted)',
        9: 'Mod Mechanic Duration % - Does not Stack (Silenced)',
        10: 'Mod Mechanic Duration % - Does not Stack (Asleep)',
        11: 'Mod Mechanic Duration % - Does not Stack (Snared)',
        12: 'Mod Mechanic Duration % - Does not Stack (Stunned)',
        13: 'Mod Mechanic Duration % - Does not Stack (Frozen)',
        14: 'Mod Mechanic Duration % - Does not Stack (Incapacitated)',
        17: 'Mod Mechanic Duration % - Does not Stack (Polymorphed)',
        18: 'Mod Mechanic Duration % - Does not Stack (Banished)',
        23: 'Mod Mechanic Duration % - Does not Stack (Turned)',
        24: 'Mod Mechanic Duration % - Does not Stack (Horrified)',
        26: 'Mod Mechanic Duration % - Does not Stack (Silenced)',
        27: 'Mod Mechanic Duration % - Does not Stack (Dazed)',
        30: 'Mod Mechanic Duration % - Does not Stack (Sapped)'
    },
    235: {
        1: 'Mod Dispel Resistance %'
    },
    236: {
        1: 'Control Vehicle'
    },
    237: {
        1: 'Mod Spell Power by % of Attack Power'
    },
    238: {
        1: 'Mod Healing Power by % of Attack Power'
    },
    239: {
        1: "Mod Size % - Doesn't stack"
    },
    240: {
        1: 'Mod Expertise'
    },
    241: {
        1: '?? (Aura #241)'
    },
    242: {},
    243: {
        1: 'Faction Override'
    },
    244: {
        1: 'Comprehend Language (Orcish)',
        2: 'Comprehend Language (Darnassian)',
        3: 'Comprehend Language (Taurahe)',
        6: 'Comprehend Language (Dwarvish)',
        7: 'Comprehend Language (Common)',
        8: 'Comprehend Language (Demonic)',
        9: 'Comprehend Language (Titan)',
        10: 'Comprehend Language (Thalassian)',
        13: 'Comprehend Language (Gnomish)',
        14: 'Comprehend Language (Zandali)',
        33: 'Comprehend Language (Forsaken)',
        35: 'Comprehend Language (Draenei)',
        36: 'Comprehend Language (Zombie)',
        37: 'Comprehend Language (Gnomish Binary)',
        38: 'Comprehend Language (Goblin Binary)',
        40: 'Comprehend Language (Goblin)',
        42: 'Comprehend Language (Pandaren)',
        178: "Comprehend Language (Shath'Yar)",
        180: 'Comprehend Language (Moonkin)',
        181: 'Comprehend Language (Shalassian)'
    },
    245: {
        1: 'Mod Debuffs Duration % (Magic)',
        2: 'Mod Debuffs Duration % (Curse)',
        3: 'Mod Debuffs Duration % (Disease)',
        4: 'Mod Debuffs Duration % (Poison)'
    },
    246: {
        1: 'Mod Debuffs Duration %'
    },
    247: {
        0: 'Clone'
    },
    248: {
        1: 'Mod Chance for Attacks to be Dodged by %'
    },
    249: {
        1: 'Create Death Rune (Blood)'
    },
    250: {
        1: 'Increase Max Health - Stacks'
    },
    251: {
        1: 'Mod Enemy Dodge %'
    },
    252: {
        1: 'Mod Melee, Ranged & Spell Haste by %'
    },
    253: {
        1: 'Critical Block Chance %'
    },
    254: {
        1: 'Remove Shield'
    },
    255: {
        0: 'Mod Mechanic Damage %',
        1: 'Mod Mechanic Damage % (Charmed)',
        3: 'Mod Mechanic Damage % (Disarmed)',
        9: 'Mod Mechanic Damage % (Silenced)',
        13: 'Mod Mechanic Damage % (Frozen)',
        15: 'Mod Mechanic Damage % (Bleeding)',
        18: 'Mod Mechanic Damage % (Banished)',
        20: 'Mod Mechanic Damage % (Shackled)',
        22: 'Mod Mechanic Damage % (Infected)',
        23: 'Mod Mechanic Damage % (Turned)',
        30: 'Mod Mechanic Damage % (Sapped)',
        32: 'Mod Mechanic Damage % (Wounded)',
        33: 'Mod Mechanic Damage %',
        34: 'Mod Mechanic Damage %',
        35: 'Mod Mechanic Damage %'
    },
    256: {},
    257: {
        1: 'Mod Target Resist by Spell Class'
    },
    258: {
        1: '?? (Aura #258)'
    },
    259: {
        1: 'Mod Periodic Healing Taken % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    260: {
        1: 'Screen Effect'
    },
    261: {
        1: 'Phase'
    },
    262: {
        1: '?? (Aura #262)'
    },
    263: {
        1: 'Allows Spells'
    },
    264: {
        1: '?? (Aura #264)'
    },
    265: {
        1: '?? (Aura #265)'
    },
    266: {
        1: '?? (Aura #266)'
    },
    267: {
        1: 'Cancel Aura if Damage Absorbed Reaches X% of Caster Health (All)'
    },
    268: {
        1: '?? (Aura #268)'
    },
    269: {
        1: '?? (Aura #269)'
    },
    270: {
        1: '?? (Aura #270)'
    },
    271: {
        0: 'Mod All Damage Done % by Caster',
        8: 'Mod All Damage Done % by Caster (Nature)',
        12: 'Mod All Damage Done % by Caster (Fire, Nature)'
    },
    272: {
        1: '?? (Aura #272)'
    },
    273: {
        1: '?? (Aura #273)'
    },
    274: {
        1: 'Consume No Ammo'
    },
    275: {
        0: 'Allow Affected Spells to be Used in Any Stance',
        10: "Allow Affected Spells to be Used in Any Stance (Tharon'ja Skeleton)"
    },
    276: {
        4: 'Mod Damage Done % by Mechanic (Distracted)',
        18: 'Mod Damage Done % by Mechanic (Banished)',
        20: 'Mod Damage Done % by Mechanic (Shackled)',
        22: 'Mod Damage Done % by Mechanic (Infected)',
        23: 'Mod Damage Done % by Mechanic (Turned)',
        28: 'Mod Damage Done % by Mechanic (Discovery)',
        32: 'Mod Damage Done % by Mechanic (Wounded)',
        33: 'Mod Damage Done % by Mechanic',
        34: 'Mod Damage Done % by Mechanic',
        35: 'Mod Damage Done % by Mechanic'
    },
    277: {
        1: '?? (Aura #277)'
    },
    278: {
        1: 'Disarm Ranged Weapon'
    },
    279: {
        1: 'Spawn Effect'
    },
    280: {
        1: 'Mod Armor Penetration %'
    },
    281: {
        1: 'Mod All Honor Gain %'
    },
    282: {},
    283: {
        1: 'Mod All Healing Done % by Caster'
    },
    284: {
        1: '?? (Aura #284)'
    },
    285: {
        1: "Mod Attack Power for every 'School' Resistance Point"
    },
    286: {
        1: 'Allow Dot to Crit'
    },
    287: {
        1: '?? (Aura #287)'
    },
    288: {
        1: '?? (Aura #288)'
    },
    289: {
        1: '?? (Aura #289)'
    },
    290: {
        1: 'Mod Crit Chance % - All'
    },
    291: {
        1: 'Mod Experience Gained % (Quests too)'
    },
    292: {},
    293: {
        1: 'Mechanic Abilities'
    },
    294: {
        1: 'Aura of Despair'
    },
    295: {
        1: '?? (Aura #295)'
    },
    296: {
        1: '?? (Aura #296)'
    },
    297: {
        1: '?? (Aura #297)'
    },
    298: {
        1: '?? (Aura #298)'
    },
    299: {
        1: '?? (Aura #299)'
    },
    300: {
        1: '?? (Aura #300)'
    },
    301: {
        0: 'Mod Healing Absorb %',
        127: 'Mod Healing Absorb % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)',
        917631: 'Mod Healing Absorb % (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    302: {},
    303: {
        1: '?? (Aura #303)'
    },
    304: {
        1: '?? (Aura #304)'
    },
    305: {
        1: 'Mod Minimum Speed %'
    },
    306: {
        1: '?? (Aura #306)'
    },
    307: {
        1: '?? (Aura #307)'
    },
    308: {
        1: 'Mod Critical Strike %'
    },
    309: {
        1: '?? (Aura #309)'
    },
    310: {
        4: 'Mod Pet AOE Damage Avoidance (Fire)',
        127: 'Mod Pet AOE Damage Avoidance (Arcane, Fire, Frost, Holy, Nature, Physical, Shadow)'
    },
    311: {
        1: '?? (Aura #311)'
    },
    312: {
        1: 'Animation Replacement'
    },
    313: {
        1: '?? (Aura #313)'
    },
    314: {
        1: '?? (Aura #314)'
    },
    315: {
        1: '?? (Aura #315)'
    },
    316: {
        1: '?? (Aura #316)'
    },
    317: {
        0: '?? (Aura #317)',
        126: '?? (Aura #317)'
    },
    318: {
        1: 'Mod Mastery %'
    },
    319: {
        1: 'Mod Melee Attack Speed'
    },
    320: {
        1: '?? (Aura #320)'
    },
    321: {
        1: '?? (Aura #321)'
    },
    322: {
        1: '?? (Aura #322)'
    },
    323: {
        1: '?? (Aura #323)'
    },
    324: {
        1: '?? (Aura #324)'
    },
    325: {
        1: '?? (Aura #325)'
    },
    326: {
        1: '?? (Aura #326)'
    },
    327: {
        1: '?? (Aura #327)'
    },
    328: {
        1: '?? (Aura #328)'
    },
    329: {
        1: '?? (Aura #329)'
    },
    330: {
        1: 'Allows Cast while Moving'
    },
    331: {
        1: '?? (Aura #331)'
    },
    332: {
        1: 'Overrides Actionbar Spell'
    },
    333: {
        1: 'Overrides Actionbar Spell'
    },
    334: {
        1: '?? (Aura #334)'
    },
    335: {
        1: '?? (Aura #335)'
    },
    336: {
        1: '?? (Aura #336)'
    },
    337: {},
    338: {
        1: '?? (Aura #338)'
    },
    339: {
        1: '?? (Aura #339)'
    },
    340: {
        1: '?? (Aura #340)'
    },
    341: {
        1: '?? (Aura #341)'
    },
    342: {
        0: 'Mod Attack Speed %'
    },
    343: {
        1: '?? (Aura #343)'
    },
    344: {
        1: 'Mod Auto Attack Damage %'
    },
    345: {
        1: 'Ignore Armor %'
    },
    346: {
        1: '?? (Aura #346)'
    },
    347: {
        1: '?? (Aura #347)'
    },
    348: {
        1: '?? (Aura #348)'
    },
    349: {
        1: 'Mod Currency Gain'
    },
    350: {
        1: '?? (Aura #350)'
    },
    351: {
        1: '?? (Aura #351)'
    },
    352: {
        1: '?? (Aura #352)'
    },
    353: {},
    354: {
        1: 'Mod Healing Based on Target Health %'
    },
    355: {
        1: '?? (Aura #355)'
    },
    356: {
        1: 'Mod Spell Damage Done %'
    },
    357: {
        1: '?? (Aura #357)'
    },
    358: {
        1: '?? (Aura #358)'
    },
    359: {
        1: '?? (Aura #359)'
    },
    360: {
        1: '?? (Aura #360)'
    },
    361: {
        1: 'Triggers AoE'
    },
    362: {
        1: '?? (Aura #362)'
    },
    363: {
        1: '?? (Aura #363)'
    },
    364: {},
    365: {
        1: '?? (Aura #365)'
    },
    366: {
        0: 'Override Spell Power By AP %',
        126: 'Override Spell Power By AP % (All)'
    },
    367: {
        1: '?? (Aura #367)'
    },
    368: {
        1: '?? (Aura #368)'
    },
    369: {
        1: '?? (Aura #369)'
    },
    370: {
        1: '?? (Aura #370)'
    },
    371: {
        1: '?? (Aura #371)'
    },
    372: {
        1: '?? (Aura #372)'
    },
    373: {
        1: 'Mod Speed % and Unable to Control Character'
    },
    374: {
        1: '?? (Aura #374)'
    },
    375: {
        1: '?? (Aura #375)'
    },
    376: {
        1: '?? (Aura #376)'
    },
    377: {
        1: 'Allows Movement while Casting'
    },
    378: {},
    379: {
        1: '?? (Aura #379)'
    },
    380: {
        1: '?? (Aura #380)'
    },
    381: {
        1: '?? (Aura #381)'
    },
    382: {
        1: 'Mod Pet Damage %'
    },
    383: {
        1: '?? (Aura #383)'
    },
    384: {}
}