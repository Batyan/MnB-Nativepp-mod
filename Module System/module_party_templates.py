from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_brigand,0,1),(trp_bandit,0,5),(trp_looter,3,65),(trp_peasant_woman,0,1,pmf_is_prisoner),(trp_farmer,0,2,pmf_is_prisoner)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_slaver_chief,1,3),(trp_slave_crusher,1,9),(trp_slave_hunter,2,15),(trp_slave_driver,4,24),(trp_manhunter,8,36),(trp_bandit,0,4,pmf_is_prisoner)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Steppe Bandits",icon_khergit|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_steppe_rider,0,9),(trp_steppe_bandit,4,47),(trp_peasant_woman,0,1,pmf_is_prisoner),(trp_farmer,0,1,pmf_is_prisoner),(trp_khergit_tribesman,0,2,pmf_is_prisoner)]),
  ("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(6),0,fac_outlaws,bandit_personality,[(trp_tundra_bandit,0,10),(trp_taiga_bandit,4,38),(trp_peasant_woman,0,1,pmf_is_prisoner),(trp_farmer,0,1,pmf_is_prisoner),(trp_vaegir_recruit,0,2,pmf_is_prisoner)]),
  ("desert_bandits","Desert Bandits",icon_khergit|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_desert_rider,1,14),(trp_desert_skirmisher,0,7),(trp_desert_bandit,4,40),(trp_peasant_woman,0,1,pmf_is_prisoner),(trp_farmer,0,1,pmf_is_prisoner),(trp_sarranid_recruit,0,2,pmf_is_prisoner)]),
  ("forest_bandits","Forest Bandits",icon_axeman|carries_goods(6),0,fac_outlaws,bandit_personality,[(trp_forest_warrior,0,11),(trp_forest_hunter,0,7),(trp_forest_bandit,4,38),(trp_peasant_woman,0,1,pmf_is_prisoner),(trp_farmer,0,1,pmf_is_prisoner),(trp_swadian_recruit,0,2,pmf_is_prisoner)]),
  ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(5),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_cavalry,0,7),(trp_mountain_raider,0,10),(trp_mountain_bandit,4,45),(trp_peasant_woman,0,1,pmf_is_prisoner),(trp_farmer,0,1,pmf_is_prisoner),(trp_rhodok_tribesman,0,2,pmf_is_prisoner)]),
  ("sea_raiders","Sea Raiders",icon_axeman|carries_goods(7),0,fac_outlaws,bandit_personality,[(trp_skull_crusher,0,8),(trp_sea_raider,5,48),(trp_peasant_woman,0,1,pmf_is_prisoner),(trp_farmer,0,1,pmf_is_prisoner),(trp_nord_recruit,0,2,pmf_is_prisoner)]),

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(12),0,fac_deserters,bandit_personality,[(trp_peasant_woman,0,1,pmf_is_prisoner),(trp_townsman,0,2,pmf_is_prisoner),(trp_manhunter,0,1,pmf_is_prisoner)]),

  
  
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),


  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(4)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(6)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,9,18),(trp_watchman,4,8),(trp_mercenary_fieldman,2,4)]),
  ("prisoner_train_party","Convoy",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),
  
  ("kingdom_hero_party","War Party",icon_flagbearer_b|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  


# Reinforcements
#  ("default_reinforcements_a","default_reinforcements_a",0,0,fac_commoners,0,[(trp_caravan_guard,1,10),(trp_watchman,3,16),(trp_farmer,9,24)]),
#  ("default_reinforcements_b","default_reinforcements_b",0,0,fac_commoners,0,[(trp_mercenary,1,7),(trp_caravan_guard,3,10),(trp_watchman,3,15)]),
#  ("default_reinforcements_c","default_reinforcements_c",0,0,fac_commoners,0,[(trp_hired_blade,1,7),(trp_mercenary,3,10),(trp_caravan_guard,3,15)]),

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_militia,7,14),(trp_swadian_recruit,5,10)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_noble,1,2),(trp_swadian_militia,6,12),(trp_swadian_skirmisher,3,6),(trp_swadian_footman,1,2),(trp_watchman,0,1)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_noble,2,4),(trp_swadian_cavalryman,4,8),(trp_swadian_footman,2,4)]),
  ("kingdom_1_reinforcements_aa", "{!}kingdom_1_reinforcements_aa", 0, 0, fac_commoners, 0, [(trp_swadian_militia,7,14),(trp_swadian_recruit,5,10)]),
  ("kingdom_1_reinforcements_ab", "{!}kingdom_1_reinforcements_ab", 0, 0, fac_commoners, 0, [(trp_swadian_noble,1,2),(trp_swadian_militia,6,12),(trp_swadian_footman,4,8),(trp_watchman,0,1)]),
  ("kingdom_1_reinforcements_ac", "{!}kingdom_1_reinforcements_ac", 0, 0, fac_commoners, 0, [(trp_swadian_noble,2,4),(trp_swadian_cavalryman,4,8),(trp_swadian_footman,2,4)]),
  ("kingdom_1_reinforcements_ba", "{!}kingdom_1_reinforcements_ba", 0, 0, fac_commoners, 0, [(trp_swadian_militia,6,12),(trp_swadian_recruit,5,10),(trp_watchman,1,2)]),
  ("kingdom_1_reinforcements_bb", "{!}kingdom_1_reinforcements_bb", 0, 0, fac_commoners, 0, [(trp_swadian_noble,1,2),(trp_swadian_militia,4,8),(trp_swadian_skirmisher,1,2),(trp_swadian_footman,3,6),(trp_watchman,2,5)]),
  ("kingdom_1_reinforcements_bc", "{!}kingdom_1_reinforcements_bc", 0, 0, fac_commoners, 0, [(trp_swadian_noble,2,4),(trp_swadian_cavalryman,4,8),(trp_swadian_footman,2,4)]),
  ("kingdom_1_reinforcements_d", "{!}kingdom_1_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_swadian_noble4,1,2),(trp_swadian_noble3,1,4)]),


  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_footman,5,10),(trp_vaegir_recruit,5,10),(trp_vaegir_scout,2,4)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_noble,1,2),(trp_vaegir_footman,2,4),(trp_vaegir_skirmisher,2,4),(trp_vaegir_veteran,2,4),(trp_vaegir_scout,4,8),(trp_watchman,0,1)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_noble,2,4),(trp_vaegir_light_cavalry,4,8),(trp_vaegir_skirmisher,1,2),(trp_vaegir_veteran,1,2)]),
  ("kingdom_2_reinforcements_aa", "{!}kingdom_2_reinforcements_aa", 0, 0, fac_commoners, 0, [(trp_vaegir_footman,7,14),(trp_vaegir_recruit,5,10)]),
  ("kingdom_2_reinforcements_ab", "{!}kingdom_2_reinforcements_ab", 0, 0, fac_commoners, 0, [(trp_vaegir_noble,1,2),(trp_vaegir_footman,4,8),(trp_vaegir_skirmisher,1,2),(trp_vaegir_veteran,3,6),(trp_vaegir_scout,2,4),(trp_watchman,0,1)]),
  ("kingdom_2_reinforcements_ac", "{!}kingdom_2_reinforcements_ac", 0, 0, fac_commoners, 0, [(trp_vaegir_noble,2,4),(trp_vaegir_light_cavalry,4,8),(trp_vaegir_veteran,2,4)]),
  ("kingdom_2_reinforcements_ba", "{!}kingdom_2_reinforcements_ba", 0, 0, fac_commoners, 0, [(trp_vaegir_footman,4,8),(trp_vaegir_recruit,5,10),(trp_watchman,1,2),(trp_vaegir_scout,2,4)]),
  ("kingdom_2_reinforcements_bb", "{!}kingdom_2_reinforcements_bb", 0, 0, fac_commoners, 0, [(trp_vaegir_noble,1,2),(trp_vaegir_footman,2,4),(trp_vaegir_skirmisher,2,4),(trp_vaegir_veteran,2,4),(trp_vaegir_scout,2,4),(trp_watchman,2,5)]),
  ("kingdom_2_reinforcements_bc", "{!}kingdom_2_reinforcements_bc", 0, 0, fac_commoners, 0, [(trp_vaegir_noble,2,4),(trp_vaegir_light_cavalry,4,8),(trp_vaegir_veteran,2,4)]),
  ("kingdom_2_reinforcements_d", "{!}kingdom_2_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_vaegir_noble4,1,2),(trp_vaegir_noble3,1,4)]),


  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_skirmisher,6,12),(trp_khergit_tribesman,5,10),(trp_khergit_steppe_fighter,1,2)]),
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_noble,1,2),(trp_khergit_skirmisher,9,18),(trp_khergit_steppe_fighter,1,2),(trp_watchman,0,1)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_noble,2,4),(trp_khergit_horseman,5,10),(trp_khergit_soldier,1,2)]),
  ("kingdom_3_reinforcements_aa", "{!}kingdom_3_reinforcements_aa", 0, 0, fac_commoners, 0, [(trp_khergit_skirmisher,6,12),(trp_khergit_tribesman,5,10),(trp_khergit_steppe_fighter,1,2)]),
  ("kingdom_3_reinforcements_ab", "{!}kingdom_3_reinforcements_ab", 0, 0, fac_commoners, 0, [(trp_khergit_noble,1,2),(trp_khergit_skirmisher,7,14),(trp_khergit_steppe_fighter,3,6),(trp_watchman,0,1)]),
  ("kingdom_3_reinforcements_ac", "{!}kingdom_3_reinforcements_ac", 0, 0, fac_commoners, 0, [(trp_khergit_noble,2,4),(trp_khergit_horseman,5,10),(trp_khergit_soldier,1,2)]),
  ("kingdom_3_reinforcements_ba", "{!}kingdom_3_reinforcements_ba", 0, 0, fac_commoners, 0, [(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,5,10),(trp_khergit_steppe_fighter,1,2),(trp_watchman,1,2)]),
  ("kingdom_3_reinforcements_bb", "{!}kingdom_3_reinforcements_bb", 0, 0, fac_commoners, 0, [(trp_khergit_noble,1,2),(trp_khergit_skirmisher,7,14),(trp_khergit_steppe_fighter,1,2),(trp_watchman,2,5)]),
  ("kingdom_3_reinforcements_bc", "{!}kingdom_3_reinforcements_bc", 0, 0, fac_commoners, 0, [(trp_khergit_noble,2,4),(trp_khergit_horseman,5,10),(trp_khergit_soldier,1,2)]),
  ("kingdom_3_reinforcements_d", "{!}kingdom_3_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_khergit_noble4,1,2),(trp_khergit_noble3,1,4)]),


  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman,7,14),(trp_nord_recruit,5,10)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_noble,1,2),(trp_nord_huntsman,4,8),(trp_nord_footman,4,8),(trp_nord_trained_footman,2,4),(trp_watchman,0,1)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_noble,2,4),(trp_nord_warrior,1,2),(trp_nord_trained_footman,5,10)]),
  ("kingdom_4_reinforcements_aa", "{!}kingdom_4_reinforcements_aa", 0, 0, fac_commoners, 0, [(trp_nord_footman,7,14),(trp_nord_recruit,5,10)]),
  ("kingdom_4_reinforcements_ab", "{!}kingdom_4_reinforcements_ab", 0, 0, fac_commoners, 0, [(trp_nord_noble,1,2),(trp_nord_huntsman,6,12),(trp_nord_footman,2,4),(trp_nord_trained_footman,2,4),(trp_watchman,0,1)]),
  ("kingdom_4_reinforcements_ac", "{!}kingdom_4_reinforcements_ac", 0, 0, fac_commoners, 0, [(trp_nord_noble,2,4),(trp_nord_warrior,1,2),(trp_nord_trained_footman,4,8),(trp_nord_archer,1,2)]),
  ("kingdom_4_reinforcements_ba", "{!}kingdom_4_reinforcements_ba", 0, 0, fac_commoners, 0, [(trp_nord_footman,6,12),(trp_nord_recruit,5,10),(trp_watchman,1,2)]),
  ("kingdom_4_reinforcements_bb", "{!}kingdom_4_reinforcements_bb", 0, 0, fac_commoners, 0, [(trp_nord_noble,1,2),(trp_nord_huntsman,2,4),(trp_nord_footman,4,8),(trp_nord_trained_footman,2,4),(trp_watchman,2,5)]),
  ("kingdom_4_reinforcements_bc", "{!}kingdom_4_reinforcements_bc", 0, 0, fac_commoners, 0, [(trp_nord_noble,2,4),(trp_nord_warrior,1,2),(trp_nord_trained_footman,5,10)]),
  ("kingdom_4_reinforcements_d", "{!}kingdom_4_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_nord_noble4,1,2),(trp_nord_noble3,1,4)]),


  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,6,12),(trp_rhodok_tribesman,5,10),(trp_rhodok_swordman,1,2)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,1,2),(trp_rhodok_spearman,2,4),(trp_rhodok_crossbowman,6,12),(trp_rhodok_trained_spearman,2,4),(trp_watchman,0,1)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,2,4),(trp_rhodok_trained_spearman,3,6),(trp_rhodok_trained_crossbowman,3,6)]),
  ("kingdom_5_reinforcements_aa", "{!}kingdom_5_reinforcements_aa", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,6,12),(trp_rhodok_tribesman,5,10),(trp_rhodok_swordman,1,2)]),
  ("kingdom_5_reinforcements_ab", "{!}kingdom_5_reinforcements_ab", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,1,2),(trp_rhodok_spearman,2,4),(trp_rhodok_crossbowman,8,16),(trp_watchman,0,1)]),
  ("kingdom_5_reinforcements_ac", "{!}kingdom_5_reinforcements_ac", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,2,4),(trp_rhodok_trained_spearman,2,4),(trp_rhodok_trained_crossbowman,4,8)]),
  ("kingdom_5_reinforcements_ba", "{!}kingdom_5_reinforcements_ba", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,5,10),(trp_rhodok_tribesman,5,10),(trp_rhodok_swordman,1,2),(trp_watchman,1,2)]),
  ("kingdom_5_reinforcements_bb", "{!}kingdom_5_reinforcements_bb", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,1,2),(trp_rhodok_spearman,2,4),(trp_rhodok_crossbowman,6,12),(trp_watchman,2,5)]),
  ("kingdom_5_reinforcements_bc", "{!}kingdom_5_reinforcements_bc", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,2,4),(trp_rhodok_trained_spearman,3,6),(trp_rhodok_trained_crossbowman,3,6)]),
  ("kingdom_5_reinforcements_d", "{!}kingdom_5_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_rhodok_noble4,1,2),(trp_rhodok_noble3,1,4)]),


  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_footman,7,14),(trp_sarranid_recruit,5,10)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_noble,1,2),(trp_sarranid_footman,6,12),(trp_sarranid_skirmisher,1,2),(trp_sarranid_veteran_footman,3,6),(trp_watchman,0,1)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_noble,2,4),(trp_sarranid_cavalry,4,8),(trp_sarranid_veteran_footman,2,4)]),
  ("kingdom_6_reinforcements_aa", "{!}kingdom_6_reinforcements_aa", 0, 0, fac_commoners, 0, [(trp_sarranid_footman,7,14),(trp_sarranid_recruit,5,10)]),
  ("kingdom_6_reinforcements_ab", "{!}kingdom_6_reinforcements_ab", 0, 0, fac_commoners, 0, [(trp_sarranid_noble,1,2),(trp_sarranid_footman,6,12),(trp_sarranid_veteran_footman,4,8),(trp_watchman,0,1)]),
  ("kingdom_6_reinforcements_ac", "{!}kingdom_6_reinforcements_ac", 0, 0, fac_commoners, 0, [(trp_sarranid_noble,2,4),(trp_sarranid_cavalry,4,8),(trp_sarranid_veteran_footman,2,4)]),
  ("kingdom_6_reinforcements_ba", "{!}kingdom_6_reinforcements_ba", 0, 0, fac_commoners, 0, [(trp_sarranid_footman,6,12),(trp_sarranid_recruit,5,10),(trp_watchman,1,2)]),
  ("kingdom_6_reinforcements_bb", "{!}kingdom_6_reinforcements_bb", 0, 0, fac_commoners, 0, [(trp_sarranid_noble,1,2),(trp_sarranid_footman,4,8),(trp_sarranid_skirmisher,3,6),(trp_sarranid_veteran_footman,1,2),(trp_watchman,2,5)]),
  ("kingdom_6_reinforcements_bc", "{!}kingdom_6_reinforcements_bc", 0, 0, fac_commoners, 0, [(trp_sarranid_noble,2,4),(trp_sarranid_cavalry,4,8),(trp_sarranid_veteran_footman,2,4)]),
  ("kingdom_6_reinforcements_d", "{!}kingdom_6_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_sarranid_noble4,1,2),(trp_sarranid_noble3,1,4)]),


  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_watchman,7,14),(trp_farmer,3,6),(trp_townsman,1,2),(trp_peasant_woman,1,2)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_player_noble,1,2),(trp_watchman,6,12),(trp_mercenary_fieldman,2,4),(trp_town_watch,2,4),(trp_hunter_woman,0,1)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_player_noble,2,4),(trp_caravan_guard,3,6),(trp_mercenary_fieldman,1,2),(trp_town_watch,1,2),(trp_mercenary_swordsman,1,2)]),
  ("kingdom_7_reinforcements_aa", "{!}kingdom_7_reinforcements_aa", 0, 0, fac_commoners, 0, [(trp_watchman,7,14),(trp_farmer,3,6),(trp_townsman,1,2),(trp_peasant_woman,1,2)]),
  ("kingdom_7_reinforcements_ab", "{!}kingdom_7_reinforcements_ab", 0, 0, fac_commoners, 0, [(trp_player_noble,1,2),(trp_watchman,6,12),(trp_mercenary_fieldman,3,6),(trp_town_watch,1,2),(trp_hunter_woman,0,1)]),
  ("kingdom_7_reinforcements_ac", "{!}kingdom_7_reinforcements_ac", 0, 0, fac_commoners, 0, [(trp_player_noble,2,4),(trp_caravan_guard,2,4),(trp_mercenary_fieldman,2,4),(trp_town_watch,1,2),(trp_mercenary_swordsman,1,2)]),
  ("kingdom_7_reinforcements_ba", "{!}kingdom_7_reinforcements_ba", 0, 0, fac_commoners, 0, [(trp_watchman,6,12),(trp_farmer,2,4),(trp_townsman,1,2),(trp_peasant_woman,2,4),(trp_hunter_woman,1,2)]),
  ("kingdom_7_reinforcements_bb", "{!}kingdom_7_reinforcements_bb", 0, 0, fac_commoners, 0, [(trp_player_noble,1,2),(trp_watchman,3,6),(trp_mercenary_fieldman,1,2),(trp_town_watch,3,6),(trp_hunter_woman,3,7)]),
  ("kingdom_7_reinforcements_bc", "{!}kingdom_7_reinforcements_bc", 0, 0, fac_commoners, 0, [(trp_player_noble,2,4),(trp_caravan_guard,3,6),(trp_mercenary_fieldman,1,2),(trp_town_watch,1,2),(trp_mercenary_swordsman,1,2)]),
  ("kingdom_7_reinforcements_d", "{!}kingdom_7_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_player_noble4,1,2),(trp_player_noble3,1,4)]),


  ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_footman,6,12),(trp_draftee,5,10),(trp_spotter,1,2)]),
  ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_freerider_noble,1,2),(trp_footman,4,8),(trp_spotter,2,4),(trp_trainee,2,4),(trp_light_infantry,2,4),(trp_watchman,0,1)]),
  ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_freerider_noble,2,4),(trp_light_cavalry,3,6),(trp_trainee,1,2),(trp_light_infantry,2,4)]),
  ("kingdom_8_reinforcements_aa", "{!}kingdom_8_reinforcements_aa", 0, 0, fac_commoners, 0, [(trp_footman,5,10),(trp_draftee,5,10),(trp_spotter,2,4)]),
  ("kingdom_8_reinforcements_ab", "{!}kingdom_8_reinforcements_ab", 0, 0, fac_commoners, 0, [(trp_freerider_noble,1,2),(trp_footman,4,8),(trp_spotter,2,4),(trp_trainee,3,6),(trp_light_infantry,1,2),(trp_watchman,0,1)]),
  ("kingdom_8_reinforcements_ac", "{!}kingdom_8_reinforcements_ac", 0, 0, fac_commoners, 0, [(trp_freerider_noble,2,4),(trp_light_cavalry,3,6),(trp_trainee,2,4),(trp_light_infantry,1,2)]),
  ("kingdom_8_reinforcements_ba", "{!}kingdom_8_reinforcements_ba", 0, 0, fac_commoners, 0, [(trp_footman,5,10),(trp_draftee,5,10),(trp_spotter,1,2),(trp_watchman,1,2)]),
  ("kingdom_8_reinforcements_bb", "{!}kingdom_8_reinforcements_bb", 0, 0, fac_commoners, 0, [(trp_freerider_noble,1,2),(trp_footman,4,8),(trp_trainee,2,4),(trp_light_infantry,2,4),(trp_watchman,2,5)]),
  ("kingdom_8_reinforcements_bc", "{!}kingdom_8_reinforcements_bc", 0, 0, fac_commoners, 0, [(trp_freerider_noble,2,4),(trp_light_cavalry,3,6),(trp_trainee,1,2),(trp_light_infantry,2,4)]),
  ("kingdom_8_reinforcements_d", "{!}kingdom_8_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_freerider_noble4,1,2),(trp_freerider_noble3,1,4)]),


  ("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_skirmisher,2,4),(trp_khergit_tribesman,5,10),(trp_khergit_steppe_fighter,5,10)]),
  ("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_noble,1,2),(trp_khergit_skirmisher,4,8),(trp_khergit_steppe_fighter,6,12),(trp_watchman,0,1)]),
  ("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_noble,2,4),(trp_khergit_horseman,3,6),(trp_khergit_soldier,3,6)]),
  ("kingdom_9_reinforcements_aa", "{!}kingdom_9_reinforcements_aa", 0, 0, fac_commoners, 0, [(trp_khergit_skirmisher,2,4),(trp_khergit_tribesman,5,10),(trp_khergit_steppe_fighter,5,10)]),
  ("kingdom_9_reinforcements_ab", "{!}kingdom_9_reinforcements_ab", 0, 0, fac_commoners, 0, [(trp_khergit_noble,1,2),(trp_khergit_skirmisher,4,8),(trp_khergit_steppe_fighter,6,12),(trp_watchman,0,1)]),
  ("kingdom_9_reinforcements_ac", "{!}kingdom_9_reinforcements_ac", 0, 0, fac_commoners, 0, [(trp_khergit_noble,2,4),(trp_khergit_horseman,3,6),(trp_khergit_soldier,2,4),(trp_khergit_archer,1,2)]),
  ("kingdom_9_reinforcements_ba", "{!}kingdom_9_reinforcements_ba", 0, 0, fac_commoners, 0, [(trp_khergit_skirmisher,2,4),(trp_khergit_tribesman,5,10),(trp_khergit_steppe_fighter,4,8),(trp_watchman,1,2)]),
  ("kingdom_9_reinforcements_bb", "{!}kingdom_9_reinforcements_bb", 0, 0, fac_commoners, 0, [(trp_khergit_noble,1,2),(trp_khergit_skirmisher,4,8),(trp_khergit_steppe_fighter,4,8),(trp_watchman,2,5)]),
  ("kingdom_9_reinforcements_bc", "{!}kingdom_9_reinforcements_bc", 0, 0, fac_commoners, 0, [(trp_khergit_noble,2,4),(trp_khergit_horseman,3,6),(trp_khergit_soldier,3,6)]),
  ("kingdom_9_reinforcements_d", "{!}kingdom_9_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_khergit_noble4,1,2),(trp_khergit_noble3,1,4)]),


  ("kingdom_5a_reinforcements_a", "{!}kingdom_5a_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_swordman,5,10),(trp_rhodok_tribesman,5,10),(trp_rhodok_spearman,2,4)]),
  ("kingdom_5a_reinforcements_b", "{!}kingdom_5a_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,1,2),(trp_rhodok_swordman,5,10),(trp_rhodok_crossbowman,5,10),(trp_watchman,0,1)]),
  ("kingdom_5a_reinforcements_c", "{!}kingdom_5a_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,2,4),(trp_rhodok_trained_swordman,4,8),(trp_rhodok_trained_crossbowman,2,4)]),
  ("kingdom_5a_reinforcements_aa", "{!}kingdom_5a_reinforcements_aa", 0, 0, fac_commoners, 0, [(trp_rhodok_swordman,4,8),(trp_rhodok_tribesman,5,10),(trp_rhodok_spearman,3,6)]),
  ("kingdom_5a_reinforcements_ab", "{!}kingdom_5a_reinforcements_ab", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,1,2),(trp_rhodok_swordman,4,8),(trp_rhodok_crossbowman,6,12),(trp_watchman,0,1)]),
  ("kingdom_5a_reinforcements_ac", "{!}kingdom_5a_reinforcements_ac", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,2,4),(trp_rhodok_trained_swordman,3,6),(trp_rhodok_trained_crossbowman,3,6)]),
  ("kingdom_5a_reinforcements_ba", "{!}kingdom_5a_reinforcements_ba", 0, 0, fac_commoners, 0, [(trp_rhodok_swordman,5,10),(trp_rhodok_tribesman,5,10),(trp_watchman,1,2),(trp_rhodok_spearman,1,2)]),
  ("kingdom_5a_reinforcements_bb", "{!}kingdom_5a_reinforcements_bb", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,1,2),(trp_rhodok_swordman,2,4),(trp_rhodok_crossbowman,4,8),(trp_watchman,2,5)]),
  ("kingdom_5a_reinforcements_bc", "{!}kingdom_5a_reinforcements_bc", 0, 0, fac_commoners, 0, [(trp_rhodok_noble,2,4),(trp_rhodok_trained_swordman,4,8),(trp_rhodok_trained_crossbowman,2,4)]),
  ("kingdom_5a_reinforcements_d", "{!}kingdom_5a_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_rhodok_noble4,1,2),(trp_rhodok_noble3,1,4)]),


##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),
  

  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
  
   ##diplomacy begin
  ("dplmc_spouse","Your spouse",icon_woman|pf_civilian|pf_show_faction,0,fac_neutral,merchant_personality,[]),

  ("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
#recruiter kit begin
   ("dplmc_recruiter","Recruiter",icon_gray_knight|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
   ##diplomacy end
]
