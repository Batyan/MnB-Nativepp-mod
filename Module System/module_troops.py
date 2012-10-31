import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...

def wp(x):
  n = 0
#  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
#  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  return n

def wp_ranged(x):
  n = 0
#  r = 10 + int(x / 10)
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n
#Skills
knows_common = knows_trade_4|knows_inventory_management_6|knows_prisoner_management_4|knows_leadership_2|knows_tactics_3|knows_weapon_master_5|knows_spotting_1|knows_pathfinding_1|knows_tracking_1
def_attrib = str_8 | agi_7 | int_5 | cha_5
def_attrib_multiplayer = str_14 | agi_14 | int_4 | cha_4



knows_lord_1 = knows_riding_7|knows_ironflesh_7|knows_power_strike_6|knows_athletics_5|knows_inventory_management_2|knows_tactics_8|knows_prisoner_management_5|knows_leadership_10|knows_shield_4

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_22|agi_20|int_20|cha_34|level(30)

knight_attrib_0 = str_12|agi_12|int_9 |cha_8 |level(30)
knight_attrib_1 = str_16|agi_14|int_10|cha_12|level(30)
knight_attrib_2 = str_20|agi_16|int_11|cha_16|level(30)
knight_attrib_3 = str_24|agi_18|int_12|cha_20|level(30)
knight_attrib_4 = str_28|agi_20|int_13|cha_24|level(30)
knight_attrib_5 = str_32|agi_22|int_14|cha_28|level(30)
king_attrib     = str_30|agi_20|int_21|cha_45|level(30)
lesser_king_attrib =str_21|agi_18|int_15|cha_30|level(30)
knight_skills_0 =   knows_riding_3|knows_ironflesh_3 |knows_power_strike_3|knows_athletics_1|knows_shield_1|knows_tactics_1|knows_prisoner_management_1                                                |knows_horse_archery_1|knows_power_throw_1|knows_power_draw_1
knight_skills_1 =   knows_riding_3|knows_ironflesh_4 |knows_power_strike_3|knows_athletics_1|knows_shield_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_1 |knows_trainer_replacement_1|knows_horse_archery_2|knows_power_throw_2|knows_power_draw_2
knight_skills_2 =   knows_riding_4|knows_ironflesh_5 |knows_power_strike_4|knows_athletics_2|knows_shield_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_2 |knows_trainer_replacement_2|knows_horse_archery_3|knows_power_throw_3|knows_power_draw_3
knight_skills_3 =   knows_riding_5|knows_ironflesh_6 |knows_power_strike_5|knows_athletics_3|knows_shield_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_3 |knows_trainer_replacement_3|knows_horse_archery_4|knows_power_throw_4|knows_power_draw_4
knight_skills_4 =   knows_riding_6|knows_ironflesh_7 |knows_power_strike_6|knows_athletics_4|knows_shield_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_4 |knows_trainer_replacement_4|knows_horse_archery_5|knows_power_throw_5|knows_power_draw_5
knight_skills_5 =   knows_riding_7|knows_ironflesh_8 |knows_power_strike_7|knows_athletics_5|knows_shield_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_5 |knows_trainer_replacement_5|knows_horse_archery_6|knows_power_throw_6|knows_power_draw_6
king_skills =       knows_riding_7|knows_ironflesh_10|knows_power_strike_6|knows_athletics_4|knows_shield_5|knows_tactics_8|knows_prisoner_management_5|knows_leadership_10|knows_trainer_replacement_9|knows_horse_archery_5|knows_power_throw_6|knows_power_draw_6
lesser_king_skills =knows_riding_6|knows_ironflesh_8 |knows_power_strike_5|knows_athletics_3|knows_shield_4|knows_tactics_7|knows_prisoner_management_3|knows_leadership_6 |knows_trainer_replacement_8|knows_horse_archery_5|knows_power_throw_5|knows_power_draw_5

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

# 0x000000000000000024db65370a48a4cb00000000001d24d80000000000000000
# 0x000000040000000024db65370a48a4cb00000000001d24d80000000000000000
# 0x000000090000000024db65370a48a4cb00000000001d24d80000000000000000
# 0x0000000d0000000024db65370a48a4cb00000000001d24d80000000000000000
# 0x0000000fc000000024db65370a48a4cb00000000001d24d80000000000000000
nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

# 0x000000002d0015ca4b648aeba46de92400000000001ed92d0000000000000000
# 0x000000046d0015ca4b648aeba46de92400000000001ed92d0000000000000000
# 0x00000008ad0015ca4b648aeba46de92400000000001ed92d0000000000000000
# 0x0000000c6d0015ca4b648aeba46de92400000000001ed92d0000000000000000
# 0x0000000fed0015ca4b648aeba46de92400000000001ed92d0000000000000000
nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

sarranid_face_younger_2 = 0x000000019700758b47de4f58cb8adba1000000000015a2a30000000000000000
sarranid_face_young_1   = 0x000000002f0c7389352b6b4d5e82369a00000000001d275d0000000000000000
sarranid_face_middle_2  = 0x000000072610754638e52a21248e58da00000000001e37620000000000000000
sarranid_face_old_2     = 0x0000000b2e0471c348a34a62d9a642a400000000001cd5990000000000000000
sarranid_face_older_2   = 0x0000000ffd0071c658d28dabd469eb2900000000001fa3250000000000000000

sarranid_face_younger_1 = 0x0000000018046183390d63269c8dcd1d00000000001dca5d0000000000000000
sarranid_face_young_2   = 0x00000002c1006410329d96425645daa000000000001dda4b0000000000000000
sarranid_face_middle_1  = 0x000000072010634f39837342db72367400000000001e28550000000000000000
sarranid_face_old_1     = 0x0000000b1f0865104ae5b28ad084b6ee00000000001d53260000000000000000
sarranid_face_older_1   = 0x0000000fe200624b46e0b12d5a4e34e300000000001e38e30000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield


troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_4|agi_4|int_4|cha_4,wp(5),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_leather_jerkin, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_tribal_warrior_outfit, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots],
   str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_hide_boots],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_leather_vest,itm_hide_boots],
   str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots,itm_ankle_boots,itm_wrapping_boots],
   str_9|agi_7|level(5),wp_melee(60)|wp_ranged(40),knows_common|knows_ironflesh_1|knows_athletics_1|knows_riding_1,mercenary_face_1, mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_leather_boots,itm_nomad_boots],
   str_12|agi_10|level(11),wp_melee(90)|wp_ranged(75),knows_common|knows_ironflesh_2|knows_power_strike_1|knows_athletics_3|knows_riding_2|knows_shield_2|knows_power_draw_1,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [itm_mail_chausses,itm_mail_boots],
   str_15|agi_13|level(17),wp_melee(110)|wp_ranged(90),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_4|knows_riding_4|knows_shield_3|knows_power_draw_2|knows_power_throw_1,mercenary_face_1, mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_iron_greaves],
   str_18|agi_15|level(22),wp_melee(140)|wp_ranged(100),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_5|knows_riding_5|knows_shield_4|knows_power_draw_3|knows_power_throw_2,mercenary_face_1, mercenary_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_wrapping_boots],
   str_9|agi_7|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_8|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_11|agi_9|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_nomad_boots],
   str_12|agi_10|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_leather_boots],
   str_14|agi_10|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_splinted_greaves],
   str_15|agi_11|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_mail_chausses],
   str_16|agi_12|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_splinted_leather_greaves],
   str_18|agi_12|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_mail_boots],
   str_19|agi_13|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_iron_greaves],
   str_20|agi_14|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
  ["farmer","Farmer","Farmers",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,
    itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_straw_hat,itm_hide_boots,itm_wrapping_boots],
   def_attrib|					level(4),	wp_melee(55)|wp_throwing(30),knows_common,man_face_middle_1, man_face_old_2],
  ["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_club,itm_staff,itm_dagger,itm_stones,
    itm_leather_cap,itm_linen_tunic,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
   def_attrib|					level(4),	wp_melee(50)|wp_throwing(35),knows_common,mercenary_face_1, mercenary_face_2],
  ["watchman","Watchman","Watchmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_tab_shield_round_a,itm_tab_shield_kite_a,itm_tab_shield_heater_a,
    itm_padded_cloth,itm_leather_jerkin,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_nomad_boots,itm_wrapping_boots],
   str_11|agi_9|int_5|cha_7|	level(9),	wpex(65,60,60,35,35,45),knows_common|knows_athletics_1|knows_shield_1|knows_power_strike_1,mercenary_face_1, mercenary_face_2],
  ["town_watch","Town Watch","Town Watch",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_fighting_pick,itm_sword_medieval_a,itm_tab_shield_heater_b,itm_tab_shield_kite_b,
    itm_leather_jerkin,itm_leather_vest,itm_gambeson,itm_leather_boots,itm_padded_coif,itm_footman_helmet,itm_leather_gloves],
   str_13|agi_12|int_7|cha_8|	level(14),	wpex(80,75,75,40,40,50),knows_common|knows_athletics_2|knows_ironflesh_1|knows_shield_2|knows_power_strike_2|knows_riding_1,mercenary_face_1, mercenary_face_2],
  ["caravan_guard","Caravan Guard","Caravan Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_fighting_pick,itm_sword_medieval_a_long,itm_sword_medieval_a,itm_tab_shield_heater_cav_a,itm_tab_shield_kite_cav_a,
    itm_leather_jerkin,itm_leather_vest,itm_gambeson,itm_leather_boots,itm_padded_coif,itm_footman_helmet,itm_leather_gloves,itm_saddle_horse],
   str_13|agi_14|int_8|cha_9|	level(16),	wpex(85,80,80,40,40,50),knows_common|knows_athletics_1|knows_riding_2|knows_ironflesh_1|knows_shield_2|knows_power_strike_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_swordsman","Mercenary","Mercenary",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,itm_tab_shield_kite_c,
    itm_mail_hauberk,itm_haubergeon,itm_mail_chausses,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet, itm_helmet_with_neckguard,itm_mail_mittens],
   str_16|agi_14|int_10|cha_10|	level(19),	wpex(100,90,90,45,45,55),knows_common|knows_athletics_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_3|knows_riding_2,mercenary_face_1, mercenary_face_2],
  ["hired_blade","Hired Blade","Hired Blades",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_b,itm_sword_medieval_c,itm_tab_shield_kite_d,itm_tab_shield_heater_d,
    itm_heraldic_mail_with_tunic,itm_heraldic_mail_with_surcoat,itm_mail_boots,itm_guard_helmet,itm_great_helmet,itm_guard_helmet,itm_great_helmet,itm_bascinet,itm_bascinet_b,itm_bascinet_c,itm_mail_mittens],
   str_19|agi_16|int_12|cha_13|	level(24),	wpex(125,120,115,50,50,60),knows_common|knows_athletics_4|knows_shield_4|knows_power_strike_4|knows_ironflesh_3|knows_riding_2,mercenary_face_1, mercenary_face_2],
  ["mercenary_champion","Champion","Champions",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_b,itm_sword_two_handed_a,itm_tab_shield_kite_d,itm_tab_shield_heater_d,
    itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_iron_greaves,itm_guard_helmet,itm_great_helmet,itm_gauntlets],
   str_22|agi_18|int_15|cha_15|	level(29),	wpex(150,145,140,55,55,65),knows_common|knows_athletics_4|knows_shield_4|knows_power_strike_5|knows_ironflesh_4|knows_riding_3,mercenary_face_1, mercenary_face_2],
   
  ["mercenary_fieldman","Fieldman","Fieldmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_arrows_b,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_light_crossbow,itm_hunting_bow,
    itm_gambeson,itm_leather_jerkin,itm_leather_vest,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_nomad_boots,itm_leather_boots,itm_leather_gloves],
   str_11|agi_12|int_6|cha_8|	level(12),	wpex(75,70,70,60,60,35),knows_common|knows_athletics_2|knows_power_draw_2|knows_shield_1|knows_riding_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_crossbowman","Crossbow","Crossbows",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_sword_medieval_b,itm_fighting_pick,itm_crossbow,itm_tab_shield_heater_b,itm_tab_shield_kite_b,
    itm_heraldic_mail_with_tunic_b,itm_padded_leather,itm_mail_coif,itm_padded_coif,itm_footman_helmet,itm_leather_boots,itm_leather_gloves],
   str_13|agi_15|int_9|cha_9|	level(17),	wpex(85,75,75,60,75,40),knows_common|knows_athletics_2|knows_power_strike_1|knows_shield_1|knows_riding_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_trained_crossbowman","Trained Crossbow","Trained Crossbows",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_steel_bolts,itm_sword_medieval_b_small,itm_sword_medieval_b,itm_military_sickle_a,itm_heavy_crossbow,itm_tab_shield_heater_c,itm_tab_shield_kite_c,
    itm_heraldic_mail_with_tunic,itm_kettle_hat,itm_mail_coif,itm_helmet_with_neckguard,itm_mail_chausses,itm_leather_boots,itm_leather_gloves],
   str_15|agi_18|int_11|cha_10|	level(22),	wpex(95,75,75,65,90,40),knows_common|knows_athletics_3|knows_ironflesh_1|knows_power_strike_2|knows_shield_2|knows_riding_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_hunter","Hunter","Hunters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [itm_barbed_arrows,itm_short_bow,itm_sword_medieval_b,itm_sword_khergit_1,itm_fighting_pick,
    itm_padded_coif,itm_heraldic_mail_with_tunic_b,itm_leather_vest,itm_leather_jerkin,itm_leather_boots,itm_leather_gloves],
   str_12|agi_16|int_9|cha_8|	level(17),	wpex(80,70,75,80,60,40),knows_common|knows_athletics_3|knows_power_draw_3|knows_riding_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_ranger","Ranger","Rangers",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_bodkin_arrows,itm_long_bow2,itm_sword_khergit_2,itm_sword_medieval_b_small,itm_sword_medieval_b,itm_military_sickle_a,
    itm_padded_coif,itm_heraldic_mail_with_tunic,itm_mail_coif,itm_leather_boots,itm_leather_gloves],
   str_13|agi_20|int_11|cha_9|	level(22),	wpex(85,70,75,80,65,40),knows_common|knows_athletics_4|knows_power_strike_1|knows_power_draw_4|knows_riding_1,mercenary_face_1, mercenary_face_2],

  ["mercenary_horseman","Horseman","Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_cav_a,itm_tab_shield_kite_cav_a,
    itm_mail_shirt,itm_haubergeon,itm_mail_chausses,itm_norman_helmet,itm_mail_coif,itm_helmet_with_neckguard,itm_leather_gloves,itm_pack_horse,itm_courser,itm_hunter],
   str_15|agi_16|int_10|cha_10|	level(20),	wpex(95,85,85,35,50,45),knows_common|knows_athletics_1|knows_riding_3|knows_ironflesh_2|knows_shield_2|knows_power_strike_2,mercenary_face_1, mercenary_face_2],
  ["mercenary_cavalry","Cavalry","Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_b,itm_sword_medieval_b,itm_tab_shield_heater_cav_b,itm_tab_shield_kite_cav_b,
    itm_mail_hauberk,itm_brigandine_red,itm_mail_boots,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_mail_mittens,itm_courser,itm_hunter],
   str_17|agi_18|int_12|cha_12|	level(24),	wpex(115,105,105,40,60,50),knows_common|knows_athletics_2|knows_riding_4|knows_ironflesh_3|knows_shield_3|knows_power_strike_3,mercenary_face_1, mercenary_face_2],


  ["mercenary_landsknecht","Landsknecht","Landsknechts",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_pike,
    itm_padded_leather,itm_mail_coif,itm_helmet_with_neckguard,itm_leather_gloves,itm_leather_boots],
   str_15|agi_13|int_9|cha_9|	level(18),	wpex(85,80,90,30,40,50),knows_common|knows_ironflesh_4|knows_power_strike_2,swadian_face_old_1, swadian_face_older_2],
  ["mercenary_trained_landsknecht","Trained Landsknecht"," TrainedLandsknechts",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_pike,
    itm_mail_hauberk,itm_kettle_hat,itm_bascinet_2,itm_guard_helmet,itm_mail_mittens,itm_mail_chausses],
   str_17|agi_15|int_11|cha_11|	level(22),	wpex(100,105,110,35,45,55),knows_common|knows_ironflesh_5|knows_power_strike_3|knows_athletics_1,swadian_face_old_1, swadian_face_older_2],
  ["mercenary_veteran_landsknecht","Veteran Landsknecht","Veteran Landsknechts",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_pike,
    itm_scale_armor,itm_bascinet_3,itm_bascinet_2,itm_guard_helmet,itm_gauntlets,itm_iron_greaves],
   str_19|agi_17|int_13|cha_13|	level(26),	wpex(115,120,125,40,50,60),knows_common|knows_ironflesh_6|knows_power_strike_4|knows_athletics_2,swadian_face_old_1, swadian_face_older_2],
  # ["mercenary_landsknecht","Landsknecht","Landsknechts",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   # [itm_pike,
    # itm_scale_armor,itm_bascinet_3,itm_bascinet_2,itm_guard_helmet,itm_gauntlets,itm_iron_greaves],
   # str_19|agi_17|int_13|cha_13|	level(26),	wpex(115,120,125,40,50,60),knows_common|knows_ironflesh_6|knows_power_strike_4|knows_athletics_2,swadian_face_old_1, swadian_face_older_2],
  ["mercenary_zweihander","Zweihander","Zweihanders",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_sword_two_handed_b,
    itm_scale_armor,itm_coat_of_plates,itm_bascinet_3,itm_bascinet_2,itm_guard_helmet,itm_gauntlets,itm_iron_greaves],
   str_18|agi_17|int_13|cha_12|	level(25),	wpex(110,115,100,40,50,60),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_2,swadian_face_old_1, swadian_face_older_2],

  ["mercenary_horse_archer","Mounted Archer","Mounted Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_arabian_sword_a,itm_sword_khergit_1,itm_short_bow,itm_barbed_arrows,
    itm_leather_vest,itm_coarse_tunic,itm_vaegir_fur_cap,itm_nomad_boots,itm_leather_boots,itm_leather_gloves,itm_steppe_horse,itm_arabian_horse_a],
   str_11|agi_15|int_8|cha_8|	level(16),	wpex(75,60,65,80,60,50),knows_common|knows_riding_3|knows_power_draw_3|knows_horse_archery_2,khergit_face_younger_1, khergit_face_young_2],
  ["mercenary_trained_horse_archer","Trained Mounted Archer","Mounted Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_arabian_sword_a,itm_sword_khergit_1,itm_nomad_bow,itm_bodkin_arrows,
    itm_leather_vest,itm_coarse_tunic,itm_vaegir_fur_cap,itm_nomad_boots,itm_leather_boots,itm_leather_gloves,itm_steppe_horse,itm_arabian_horse_a],
   str_13|agi_17|int_10|cha_9|	level(20),	wpex(80,65,70,90,60,50),knows_common|knows_riding_4|knows_power_draw_4|knows_horse_archery_3|knows_athletics_1,khergit_face_young_1, khergit_face_middle_2],
  ["mercenary_veteran_horse_archer","Veteran Mounted Archer","Veteran Mounted Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_arabian_sword_a,itm_sword_khergit_2,itm_bodkin_arrows,itm_war_bow,
    itm_leather_vest,itm_coarse_tunic,itm_vaegir_fur_helmet,itm_leather_boots,itm_leather_gloves,itm_steppe_horse,itm_arabian_horse_a,itm_arabian_horse_b],
   str_15|agi_19|int_12|cha_9|	level(24),	wpex(85,70,75,90,60,50),knows_common|knows_riding_5|knows_power_strike_1|knows_power_draw_5|knows_horse_archery_4|knows_athletics_1,khergit_face_young_1, khergit_face_old_2],

  ["mercenary_ormester","Ormester","Ormesterek",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_nomad_bow,itm_plate_covered_round_shield,itm_scimitar,itm_scimitar_b,itm_scimitar_c,itm_bodkin_arrows,
    itm_vaegir_helmet,itm_vaegir_noble_helmet,itm_vaegir_war_helmet,itm_lamellar_armor,itm_mail_mittens,itm_mail_boots],
   str_18|agi_19|int_14|cha_13|	level(27),	wpex(125,110,100,90,60,70),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_shield_4|knows_athletics_3|knows_power_draw_4,vaegir_face_middle_1, vaegir_face_older_2],

  ["mercenary_viking","Viking","Vikings",tf_mounted|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse,no_scene,reserved,fac_commoners,
   [itm_two_handed_battle_axe_2,itm_two_handed_battle_axe_2,itm_sword_viking_3_long,itm_sword_viking_3,itm_tab_shield_round_d,itm_long_bow,itm_long_bow2,itm_bodkin_arrows,
    itm_mail_mittens,itm_splinted_leather_greaves,itm_mail_shirt,itm_mail_hauberk,itm_nordic_helmet,itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet,itm_hunter],
   str_20|agi_18|int_14|cha_13|	level(28),	wpex(115,130,105,75,50,90),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_shield_4|knows_athletics_3|knows_power_draw_5|knows_riding_5,nord_face_middle_1, nord_face_older_2],

  ["mercenary_master","Master","Master",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_tab_shield_pavise_d,itm_military_pick,itm_military_hammer,
    itm_gauntlets, itm_iron_greaves,itm_bascinet_2,itm_bascinet_3,itm_heraldic_mail_with_surcoat,itm_surcoat_over_mail],
   str_19|agi_16|int_13|cha_11|	level(25),	wpex(110,110,95,50,70,75),knows_common|knows_ironflesh_5|knows_power_strike_3|knows_shield_5|knows_athletics_4,rhodok_face_middle_1, rhodok_face_older_2],


  ["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,
   [],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
   
  ["mercenary_prison_guard","Prison Guard","Prison Guard",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_heraldic_mail_with_surcoat,itm_kettle_hat,itm_mail_coif,itm_mail_mittens,itm_mail_boots,
    itm_sword_two_handed_a],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_castle_guard","Castle Guard","Castle Guard",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_heraldic_mail_with_surcoat,itm_guard_helmet,itm_gauntlets,itm_iron_greaves,
    itm_sword_two_handed_a],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,mercenary_face_1, mercenary_face_2],

#peasant - retainer - footman - man-at-arms -  knight
  ["swadian_recruit","Peasant","Peasants",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_scythe,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_leather_cap,itm_felt_hat,itm_felt_hat,
    itm_red_shirt,itm_coarse_tunic,itm_red_tunic,itm_leather_apron,itm_wrapping_boots],
   def_attrib|					level(4),	wpex(50,45,50,20,20,30),knows_common|knows_athletics_1,swadian_face_younger_1, swadian_face_middle_2],
  ["swadian_militia","Militia","Militias",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_bolts,itm_arrows_b,itm_fighting_pick,itm_sword_medieval_a,itm_hunting_crossbow,itm_hunting_bow2,itm_tab_shield_heater_a,
    itm_padded_cloth,itm_leather_armor,itm_leather_armor,itm_leather_cap,itm_arming_cap,itm_padded_coif,itm_ankle_boots,itm_wrapping_boots],
   str_10|agi_10|int_5|cha_7|	level(9),	wpex(70,60,65,45,40,35),knows_common|knows_shield_1|knows_athletics_1|knows_power_strike_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_footman","Fighter","Fighters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_fighting_pick,itm_sword_medieval_b_small,itm_sword_medieval_b,itm_tab_shield_heater_b,
    itm_padded_leather,itm_red_gambeson,itm_padded_cloth,itm_ankle_boots,itm_leather_boots,itm_padded_coif,itm_mail_coif,itm_footman_helmet,itm_norman_helmet,itm_leather_gloves],
   str_13|agi_12|int_7|cha_9|	level(14),	wpex(90,80,85,45,45,45),knows_common|knows_ironflesh_1|knows_shield_2|knows_athletics_2|knows_power_strike_2|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry","Infantry","Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_awlpike,itm_military_pick,itm_bastard_sword_a,itm_sword_medieval_c,itm_sword_medieval_c_small,itm_tab_shield_heater_c,
    itm_mail_with_surcoat,itm_haubergeon,itm_leather_boots,itm_mail_chausses,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_leather_gloves],
   str_19|agi_12|int_10|cha_11|	level(20),	wpex(110,100,105,50,50,60),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_shield_3|knows_athletics_2|knows_riding_2,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_sergeant","Battle Sergeant","Battle Sergeants",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_awlpike_long,itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c,itm_sword_medieval_c_small,itm_tab_shield_heater_d,
    itm_coat_of_plates_red,itm_mail_with_surcoat,itm_mail_boots,itm_iron_greaves,itm_guard_helmet,itm_guard_helmet,itm_bascinet,itm_bascinet_b,itm_bascinet_c,itm_guard_helmet,itm_gauntlets,itm_mail_mittens],
   str_25|agi_12|int_13|cha_14|	level(26),	wpex(135,120,130,60,60,75),knows_common|knows_shield_4|knows_ironflesh_7|knows_power_strike_4|knows_athletics_2|knows_riding_2,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_skirmisher","Skirmisher","Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_bolts,itm_arrows_b,itm_hunting_crossbow,itm_hunting_bow2,itm_dagger,itm_fighting_pick,itm_sword_medieval_a,itm_tab_shield_heater_a,
    itm_leather_armor,itm_leather_armor,itm_padded_cloth,itm_ankle_boots,itm_padded_coif,itm_arming_cap,itm_footman_helmet,itm_leather_gloves],
   str_12|agi_13|int_7|cha_8|	level(14),	wpex(80,60,65,75,70,40),knows_common|knows_athletics_3|knows_shield_1|knows_ironflesh_1|knows_power_draw_1|knows_riding_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_crossbowman","Sniper","Snipers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_bolts,itm_barbed_arrows,itm_light_crossbow,itm_short_bow2,itm_fighting_pick,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_leather_armor,itm_padded_cloth,itm_red_gambeson,itm_leather_boots,itm_ankle_boots,itm_padded_coif,itm_norman_helmet,itm_footman_helmet,itm_leather_gloves],
   str_14|agi_16|int_10|cha_10|	level(19),	wpex(85,70,70,100,95,45),knows_common|knows_power_draw_2|knows_shield_1|knows_ironflesh_1|knows_athletics_4|knows_power_strike_1|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_sharpshooter","Marksman","Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_steel_bolts,itm_bodkin_arrows,itm_light_crossbow,itm_short_bow2,itm_sword_medieval_b_small,itm_sword_medieval_b,itm_fighting_pick,itm_tab_shield_heater_c,
    itm_haubergeon,itm_padded_leather,itm_padded_leather,itm_leather_boots,itm_helmet_with_neckguard,itm_kettle_hat,itm_mail_coif,itm_leather_gloves],
   str_16|agi_19|int_12|cha_13|	level(24),	wpex(90,75,70,125,120,50),knows_common|knows_power_draw_3|knows_shield_2|knows_ironflesh_2|knows_power_strike_2|knows_athletics_5|knows_riding_2,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_cavalryman","Cavalryman","Cavalrymen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_light_lance,itm_fighting_pick,itm_sword_medieval_b,itm_tab_shield_heater_cav_a,
    itm_padded_leather,itm_red_gambeson,itm_padded_cloth,itm_ankle_boots,itm_leather_boots,itm_padded_coif,itm_mail_coif,itm_footman_helmet,itm_norman_helmet,itm_leather_gloves,itm_saddle_horse,itm_pack_horse],
   str_13|agi_14|int_8|cha_10|	level(16),	wpex(95,85,90,45,45,45),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_2|knows_athletics_2|knows_power_strike_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms","Man at Arms","Men at Arms",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_lance,itm_military_pick,itm_bastard_sword_a,itm_sword_medieval_c,itm_tab_shield_heater_cav_a,
    itm_haubergeon,itm_mail_with_surcoat,itm_leather_boots,itm_mail_chausses,itm_norman_helmet,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_kettle_hat,itm_pack_horse,itm_hunter,itm_leather_gloves],
   str_14|agi_17|int_11|cha_11|	level(22),	wpex(110,100,110,50,50,55),knows_common|knows_riding_4|knows_ironflesh_3|knows_shield_3|knows_power_strike_2|knows_athletics_2,swadian_face_young_1, swadian_face_old_2],
  ["swadian_knight","Sergeant at Arms","Sergeants at Arms",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_heavy_lance,itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c,itm_sword_medieval_c_long,itm_tab_shield_heater_cav_b,
    itm_coat_of_plates_red,itm_mail_with_surcoat,itm_mail_boots,itm_iron_greaves,itm_guard_helmet,itm_great_helmet,itm_guard_helmet,itm_great_helmet,itm_guard_helmet,itm_great_helmet,itm_bascinet,itm_bascinet_b,itm_bascinet_c,itm_hunter,itm_hunter,itm_hunter,itm_hunter,itm_warhorse,itm_mail_mittens,itm_gauntlets],
   str_19|agi_20|int_14|cha_13|	level(28),	wpex(130,120,130,60,60,65),knows_common|knows_riding_5|knows_shield_4|knows_ironflesh_4|knows_power_strike_3|knows_athletics_2,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_messenger","Swadian Messenger","Swadian Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_young_1, swadian_face_old_2],
  ["swadian_deserter","Swadian Deserter","Swadian Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_awlpike,itm_sword_two_handed_a,itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_c,itm_coat_of_plates_red,itm_plate_armor,itm_mail_chausses,itm_iron_greaves,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_mail_mittens],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_awlpike,itm_sword_two_handed_a,itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_c,itm_coat_of_plates_red,itm_plate_armor,itm_mail_chausses,itm_iron_greaves,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_mail_mittens],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

# Vaegir watchman?
  ["vaegir_recruit","Ujonc","Ujoncok",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_hatchet,itm_club,itm_axe,itm_stones,itm_tab_shield_kite_a, itm_tab_shield_kite_a,
    itm_linen_tunic, itm_rawhide_coat,itm_hide_boots],
   def_attrib|					level(4),	wpex(50,50,45,25,15,30),knows_common|knows_athletics_1, vaegir_face_younger_1, vaegir_face_middle_2],
  ["vaegir_footman","Inas","Inas",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spiked_club,itm_sword_khergit_1,itm_two_handed_axe,itm_tab_shield_kite_a,itm_tab_shield_kite_b,
    itm_linen_tunic,itm_vaegir_fur_cap,itm_rawhide_coat,itm_leather_vest,itm_nomad_boots],
   str_11|agi_9|int_5|cha_7|	level(9),	wpex(65,70,60,30,20,40),knows_common|knows_ironflesh_1|knows_athletics_2|knows_power_strike_1, vaegir_face_young_1, vaegir_face_middle_2],
  ["vaegir_scout","Cserkesz","Cserkeszek",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_hatchet,itm_club,itm_knife,itm_arrows,itm_hunting_bow,
    itm_linen_tunic,itm_vaegir_fur_cap,itm_hide_boots],
   str_8|agi_13|int_5|cha_7|	level(10),	wpex(60,55,50,70,40,35),knows_common|knows_power_draw_1|knows_athletics_2,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_skirmisher","Csatar","Csatar",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_sword_khergit_1,itm_short_bow,
    itm_linen_tunic,itm_vaegir_fur_cap,itm_vaegir_fur_helmet,itm_leather_vest,itm_leather_vest,itm_nomad_boots,itm_hide_boots,itm_leather_gloves],
   str_10|agi_16|int_8|cha_9|	level(15),	wpex(65,55,50,85,50,40),knows_common|knows_ironflesh_1|knows_power_draw_2|knows_athletics_3|knows_riding_1,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_archer","Ijasz","Ijaszok",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_bodkin_arrows,itm_scimitar,itm_nomad_bow,
    itm_leather_vest,itm_leather_boots,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_leather_gloves],
   str_12|agi_19|int_10|cha_10|	level(20),	wpex(70,55,50,100,65,45),knows_common|knows_ironflesh_1|knows_power_draw_3|knows_athletics_4|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_marksman","Kivalo Lovesz","Kivalo Loveszok",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_bodkin_arrows,itm_scimitar,itm_strong_bow,
    itm_leather_vest,itm_leather_jerkin,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_fur_helmet,itm_leather_gloves],
   str_14|agi_22|int_13|cha_12|	level(25),	wpex(80,60,55,115,80,50),knows_common|knows_ironflesh_2|knows_power_draw_4|knows_athletics_5|knows_power_strike_1|knows_riding_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_sharpshooter","Mesterlovesz","Mesterloveszok",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_bodkin_arrows,itm_scimitar,itm_war_bow,
    itm_leather_vest,itm_leather_jerkin,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_fur_helmet,itm_leather_gloves],
   str_15|agi_21|int_13|cha_10|	level(25),	wpex(80,60,55,100,80,50),knows_common|knows_ironflesh_2|knows_power_draw_5|knows_athletics_5|knows_power_strike_1|knows_riding_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_veteran","Harcos","Harcosok",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_two_handed_axe,itm_tab_shield_kite_b,itm_scimitar,
    itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_helmet,itm_leather_jerkin,itm_studded_leather_coat,itm_nomad_boots,itm_leather_boots,itm_leather_gloves],
   str_14|agi_11|int_7|cha_8|	level(14),	wpex(80,85,75,30,15,40),knows_common|knows_athletics_3|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_riding_1,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_light_cavalry","Konnyu Lovassag","Konnyu Lovassag",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_two_handed_axe,itm_tab_shield_kite_cav_a,itm_light_lance,itm_scimitar,
    itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_helmet,itm_leather_jerkin,itm_studded_leather_coat,itm_nomad_boots,itm_leather_boots,itm_leather_gloves,itm_saddle_horse,itm_steppe_horse,itm_sumpter_horse,itm_pack_horse],
   str_14|agi_13|int_8|cha_9|	level(16),	wpex(85,90,85,30,15,40),knows_common|knows_riding_3|knows_athletics_3|knows_ironflesh_2|knows_power_strike_1|knows_shield_1,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_infantry","Gyalogsag","Gyalogosok",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_scimitar,itm_tab_shield_kite_c,
    itm_mail_hauberk,itm_lamellar_vest,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_helmet,itm_leather_gloves],
   str_16|agi_14|int_10|cha_11|	level(19),	wpex(100,110,95,50,20,60),knows_common|knows_athletics_4|knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_riding_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_guard","Or","Orok",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_bardiche,itm_long_bardiche,itm_scimitar_b,itm_tab_shield_kite_d,
    itm_banded_armor,itm_lamellar_armor,itm_mail_boots,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_noble_helmet,itm_gauntlets],
   str_18|agi_17|int_12|cha_13|	level(24),	wpex(125,130,120,60,25,80),knows_common|knows_athletics_5|knows_shield_3|knows_ironflesh_4|knows_power_strike_4|knows_riding_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman","Nehezlovassag","Nehezlovassag",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
    itm_studded_leather_coat,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_helmet,itm_steppe_horse,itm_pack_horse,itm_hunter,itm_leather_gloves],
   str_16|agi_16|int_11|cha_11|	level(21),	wpex(95,105,95,50,20,60),knows_common|knows_riding_4|knows_athletics_3|knows_ironflesh_3|knows_shield_2|knows_power_strike_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_knight","Huszar","Huszar",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_bardiche,itm_scimitar_b,itm_lance,itm_tab_shield_kite_cav_b,
    itm_banded_armor,itm_lamellar_armor,itm_mail_boots,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_noble_helmet,itm_hunter,itm_mail_mittens],
   str_18|agi_19|int_13|cha_13|	level(26),	wpex(115,125,115,60,25,80),knows_common|knows_riding_5|knows_shield_3|knows_athletics_3|knows_ironflesh_4|knows_power_strike_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_messenger","Vaegir Messenger","Vaegir Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_scimitar,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_deserter","Vaegir Deserter","Vaegir Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   def_attrib|str_10|level(14),wp(80),knows_common|knows_ironflesh_1|knows_power_draw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_prison_guard","Bortonor","Bortonorok", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_great_bardiche,itm_scimitar_b,itm_tab_shield_kite_b,itm_lamellar_armor,itm_mail_boots,itm_iron_greaves,itm_gauntlets,itm_scale_gauntlets,itm_vaegir_war_helmet,itm_vaegir_noble_helmet],
   def_attrib|level(24),wp(130),knows_common|knows_shield_2|knows_ironflesh_3|knows_power_strike_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_castle_guard","Var Garda","Var Garda", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_great_bardiche,itm_scimitar_b,itm_tab_shield_kite_d,itm_lamellar_armor,itm_mail_boots,itm_iron_greaves,itm_gauntlets,itm_scale_gauntlets,itm_vaegir_war_helmet,itm_vaegir_noble_helmet],
   def_attrib|level(24),wp(130),knows_common|knows_shield_2|knows_ironflesh_3|knows_power_strike_3,vaegir_face_middle_1, vaegir_face_older_2],


  ["khergit_tribesman","Tribesman","Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_arrows_b,itm_club,itm_shortened_spear,itm_hunting_bow,
    itm_steppe_cap,itm_nomad_cap_b,itm_nomad_cap,itm_coarse_tunic,itm_steppe_armor,itm_hide_boots],
   def_attrib|					level(4),	wpex(50,45,50,40,20,35),knows_common|knows_riding_1|knows_power_draw_1|knows_athletics_1,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_skirmisher","Clansman","Clansmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_arrows_b,itm_sword_khergit_1,itm_short_bow,itm_javelin,itm_tab_shield_small_round_a,
    itm_steppe_cap,itm_nomad_cap_b,itm_leather_steppe_cap_c,itm_nomad_cap,itm_leather_steppe_cap_a,itm_coarse_tunic,itm_steppe_armor,itm_leather_vest,itm_nomad_boots,itm_khergit_leather_boots,itm_steppe_horse],
   str_9|agi_11|int_5|cha_7|	level(9),	wpex(65,55,60,60,30,55),knows_common|knows_riding_2|knows_power_draw_1|knows_power_throw_1|knows_horse_archery_1,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_horseman","Steppe Rider","Steppe Riders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_3,
  [itm_barbed_arrows,itm_light_lance,itm_winged_mace,itm_nomad_bow,itm_sword_khergit_2,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_javelin,
   itm_leather_steppe_cap_b,itm_nomad_robe,itm_leather_boots,itm_nomad_boots,itm_khergit_war_helmet,itm_steppe_horse,itm_leather_gloves],
   str_10|agi_15|int_7|cha_8|	level(14),	wpex(80,70,80,80,40,75),knows_common|knows_riding_3|knows_power_draw_2|knows_ironflesh_1|knows_power_throw_1|knows_power_strike_1|knows_horse_archery_2|knows_shield_1|knows_athletics_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_horse_archer","Horse Archer","Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_bodkin_arrows,itm_sword_khergit_2,itm_winged_mace,itm_nomad_bow,itm_tab_shield_small_round_a,
    itm_leather_steppe_cap_b,itm_tribal_warrior_outfit,itm_nomad_robe,itm_leather_boots,itm_steppe_horse,itm_leather_gloves],
   str_11|agi_18|int_9|cha_10|	level(18),	wpex(80,70,80,100,40,75),knows_common|knows_riding_4|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_3|knows_shield_1|knows_athletics_2|knows_power_strike_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer","Veteran Horse Archer","Veteran Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_winged_mace,itm_khergit_bow,itm_khergit_bow2,itm_khergit_arrows,itm_tab_shield_small_round_b,
    itm_leather_steppe_cap_b,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_leather_boots,itm_steppe_horse,itm_courser,itm_leather_gloves],
   str_12|agi_20|int_11|cha_11|	level(22),	wpex(85,70,80,110,50,80),knows_common|knows_riding_5|knows_power_draw_4|knows_ironflesh_1|knows_horse_archery_4|knows_shield_2|knows_power_strike_1|knows_athletics_3,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_dune_rider","Light Lancer","Light Lancers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_winged_mace,itm_light_lance,itm_light_lance,itm_tab_shield_small_round_c,itm_tab_shield_small_round_b,itm_javelin,
    itm_nomad_robe,itm_lamellar_vest_khergit,itm_leather_steppe_cap_b,itm_leather_boots,itm_khergit_war_helmet,itm_leather_gloves,itm_steppe_horse,itm_steppe_horse,itm_hunter],
   str_13|agi_17|int_10|cha_11|	level(19),	wpex(95,85,110,75,40,80),knows_common|knows_riding_5|knows_power_throw_1|knows_power_strike_2|knows_ironflesh_2|knows_athletics_2|knows_shield_2|knows_horse_archery_2,khergit_face_young_1, khergit_face_older_2],
  ["khergit_lancer","Lancer","Lancers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_winged_mace,itm_lance,itm_lance,itm_hafted_blade_b,itm_tab_shield_small_round_c,itm_javelin,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_splinted_greaves,itm_leather_gloves,itm_hunter,itm_courser],
   str_16|agi_19|int_12|cha_14|	level(24),	wpex(110,100,135,80,40,90),knows_common|knows_riding_6|knows_power_throw_2|knows_power_strike_3|knows_ironflesh_3|knows_athletics_3|knows_shield_3|knows_horse_archery_2,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_steppe_fighter","Steppe Fighter","Steppe Fighters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_arrows_b,itm_sword_khergit_1,itm_short_bow,itm_javelin,itm_tab_shield_small_round_a,
    itm_steppe_cap,itm_nomad_cap_b,itm_leather_steppe_cap_c,itm_nomad_cap,itm_leather_steppe_cap_a,itm_coarse_tunic,itm_steppe_armor,itm_leather_vest,itm_nomad_boots,itm_khergit_leather_boots],
   str_9|agi_11|int_5|cha_7|	level(9),	wpex(65,55,60,60,30,50),knows_common|knows_ironflesh_1|knows_power_draw_1|knows_power_throw_1|knows_riding_1|knows_athletics_2|knows_power_strike_1,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_soldier","Soldier","Soldiers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
  [itm_barbed_arrows,itm_nomad_bow,itm_winged_mace,itm_sword_khergit_2,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_javelin,
   itm_leather_steppe_cap_b,itm_nomad_robe,itm_nomad_boots,itm_leather_boots,itm_khergit_war_helmet,itm_leather_gloves],
   str_10|agi_14|int_7|cha_8|	level(13),	wpex(75,65,75,65,40,60),knows_common|knows_power_draw_2|knows_ironflesh_1|knows_power_throw_1|knows_power_strike_2|knows_athletics_3|knows_shield_1|knows_riding_2,khergit_face_young_1, khergit_face_older_2],
  ["khergit_archer","Archer","Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_bodkin_arrows,itm_sword_khergit_2,itm_winged_mace,itm_nomad_bow,itm_tab_shield_small_round_a,
    itm_leather_steppe_cap_b,itm_steppe_armor,itm_tribal_warrior_outfit,itm_leather_boots,itm_leather_gloves],
   str_9|agi_16|int_7|cha_8|	level(14),	wpex(70,60,65,80,40,65),knows_common|knows_power_draw_3|knows_ironflesh_1|knows_athletics_3|knows_shield_1|knows_riding_2|knows_power_strike_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_veteran_archer","Veteran Archer","Veteran Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_winged_mace,itm_khergit_bow,itm_khergit_bow2,itm_khergit_arrows,itm_tab_shield_small_round_b,
    itm_leather_steppe_cap_b,itm_khergit_war_helmet,itm_tribal_warrior_outfit,itm_nomad_robe,itm_leather_boots,itm_leather_gloves],
   str_10|agi_19|int_9|cha_10|	level(18),	wpex(75,60,65,100,50,70),knows_common|knows_power_draw_4|knows_ironflesh_1|knows_athletics_4|knows_shield_2|knows_riding_3|knows_power_strike_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_dune_fighter","Steppe Warrior","Steppe Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_winged_mace,itm_tab_shield_small_round_c,itm_hafted_blade_b,itm_tab_shield_small_round_b,itm_javelin,itm_nomad_bow,itm_bodkin_arrows,
    itm_nomad_robe,itm_tribal_warrior_outfit,itm_leather_boots,itm_leather_steppe_cap_b,itm_khergit_war_helmet,itm_leather_gloves],
    str_12|agi_16|int_9|cha_9|	level(17),	wpex(85,75,90,70,40,70),knows_common|knows_power_strike_3|knows_power_draw_2|knows_ironflesh_2|knows_athletics_4|knows_shield_2|knows_power_throw_1|knows_riding_2,khergit_face_young_1, khergit_face_older_2],
  ["khergit_dismounted_lancer","Dismounted Lancer","Dismounted Lancers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_sword_khergit_3,itm_winged_mace,itm_hafted_blade_b,itm_tab_shield_small_round_c,itm_javelin,itm_nomad_bow,itm_khergit_arrows,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_lamellar_vest_khergit,itm_splinted_greaves,itm_leather_boots,itm_leather_gloves],
   str_14|agi_18|int_11|cha_11|	level(21),	wpex(100,90,110,75,40,80),knows_common|knows_power_strike_4|knows_power_draw_2|knows_ironflesh_3|knows_athletics_5|knows_shield_3|knows_power_throw_2|knows_riding_3,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_messenger","Khergit Messenger","Khergit Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_short_bow,itm_arrows,
    itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,khergit_face_young_1, khergit_face_older_2],
  ["khergit_deserter","Khergit Deserter","Khergit Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,
    itm_steppe_cap,itm_nomad_cap_b,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,
    itm_lamellar_vest_khergit,itm_lamellar_armor,itm_splinted_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_common|knows_shield_2|knows_ironflesh_3|knows_power_strike_3,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,
    itm_lamellar_vest_khergit,itm_lamellar_armor,itm_splinted_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_common|knows_shield_2|knows_ironflesh_3|knows_power_strike_3,khergit_face_middle_1, khergit_face_older_2],


  ["nord_recruit","Pillager","Pillagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_hatchet,itm_tab_shield_round_a,itm_tab_shield_round_a,
    itm_blue_tunic,itm_coarse_tunic,itm_hide_boots],
   str_9|agi_7|int_5|cha_5|		level(5),	wpex(50,50,50,20,20,30),knows_common|knows_power_strike_1,nord_face_younger_1, nord_face_old_2],
  ["nord_footman","Raider","Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_a,itm_tab_shield_round_a,itm_tab_shield_round_b,itm_throwing_knives,
    itm_skullcap,itm_nordic_archer_helmet,itm_nasal_helmet,itm_leather_jerkin,itm_hide_boots],
   str_12|agi_10|int_6|cha_8|	level(11),	wpex(75,70,70,25,20,60),knows_common|knows_ironflesh_1|knows_power_strike_2|knows_athletics_1|knows_shield_1|knows_power_throw_1,nord_face_young_1, nord_face_old_2],
  ["nord_plunderer","Plunderer","Plunderers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_battle_axe_a,itm_tab_shield_round_b,itm_light_throwing_axes,itm_light_throwing_axes,
    itm_nasal_helmet,itm_nordic_footman_helmet,itm_nordic_veteran_archer_helmet,itm_byrnie,itm_leather_boots,itm_leather_gloves],
   str_15|agi_12|int_8|cha_10|	level(16),	wpex(100,95,90,30,25,80),knows_common|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2|knows_shield_2|knows_power_throw_2|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["nord_trained_footman","Trained Raider","Trained Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_battle_axe_a,itm_tab_shield_round_b,itm_light_throwing_axes,itm_light_throwing_axes,
    itm_nasal_helmet,itm_nordic_footman_helmet,itm_nordic_veteran_archer_helmet,itm_byrnie,itm_leather_boots,itm_leather_gloves],
   str_15|agi_12|int_8|cha_10|	level(16),	wpex(100,95,90,30,25,80),knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_2|knows_athletics_2|knows_shield_2|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["nord_warrior","Warrior","Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_one_handed_war_axe_b,itm_tab_shield_round_c,itm_throwing_axes,itm_throwing_axes,
    itm_nordic_footman_helmet,itm_nordic_fighter_helmet,itm_mail_shirt,itm_byrnie,itm_mail_chausses,itm_leather_boots,itm_leather_gloves],
   str_17|agi_14|int_10|cha_12|	level(20),	wpex(120,115,110,35,25,95),knows_common|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_3|knows_athletics_3|knows_shield_3|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["nord_veteran","Veteran","Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_sword_viking_2_small,itm_one_handed_battle_axe_b,itm_one_handed_battle_axe_b,itm_tab_shield_round_d,itm_throwing_axes,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_mail_shirt,itm_mail_chausses,itm_mail_mittens],
   str_19|agi_16|int_12|cha_14|	level(24),	wpex(140,135,130,40,30,110),knows_common|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_3|knows_athletics_4|knows_shield_4|knows_riding_2,nord_face_young_1, nord_face_older_2],
  ["nord_champion","Huscarl","Huscarls",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_sword_viking_3,itm_sword_viking_3_small,itm_one_handed_battle_axe_c,itm_one_handed_battle_axe_c,itm_tab_shield_round_e,itm_heavy_throwing_axes,itm_heavy_throwing_axes,
    itm_nordic_helmet,itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet,itm_banded_armor,itm_mail_boots,itm_splinted_leather_greaves,itm_gauntlets],
   str_21|agi_18|int_14|cha_16|	level(28),	wpex(160,150,145,50,35,130),knows_common|knows_ironflesh_5|knows_power_strike_6|knows_power_throw_4|knows_athletics_5|knows_shield_5|knows_riding_2,nord_face_middle_1, nord_face_older_2],
  ["nord_huntsman","Huntsman","Huntsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_arrows_b,itm_hunting_bow2,itm_one_handed_war_axe_a,
    itm_blue_tunic,itm_hide_boots],
   str_11|agi_10|int_5|cha_6|	level(10),	wpex(60,55,50,60,40,30),knows_common|knows_power_strike_1|knows_power_draw_1,nord_face_young_1, nord_face_old_2],
  ["nord_bowman","Bowman","Bowman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_barbed_arrows,itm_short_bow,itm_two_handed_axe,
    itm_leather_jerkin,itm_leather_boots,itm_nordic_archer_helmet,itm_nordic_veteran_archer_helmet,itm_leather_gloves],
   str_14|agi_13|int_8|cha_9|	level(16),	wpex(70,80,55,85,45,35),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_power_draw_2|knows_athletics_4|knows_riding_1,nord_face_young_1, nord_face_old_2],
  # ["nord_veteran_bowman","Veteran Bowman","Veteran Bowman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_6,
   # [itm_bodkin_arrows,itm_short_bow,itm_two_handed_axe,
    # itm_byrnie,itm_leather_boots,itm_mail_chausses,itm_nordic_archer_helmet,itm_nordic_veteran_archer_helmet,itm_nordic_footman_helmet,itm_leather_gloves],
   # str_15|agi_15|int_10|cha_10|	level(19),	wpex(80,100,60,100,55,40),knows_common|knows_power_strike_3|knows_ironflesh_2|knows_power_draw_3|knows_athletics_5|knows_riding_1,nord_face_middle_1, nord_face_older_2],
  ["nord_archer","Longbowman","Longbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_barbed_arrows,itm_long_bow,itm_one_handed_battle_axe_a,itm_sword_viking_1,
    itm_blue_tunic,itm_leather_jerkin,itm_leather_boots,itm_nordic_archer_helmet,itm_leather_gloves],
   str_14|agi_12|int_8|cha_8|	level(15),	wpex(80,65,55,75,45,35),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_power_draw_4|knows_athletics_1|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_archer","Veteran Longbowman","Veteran Longbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_bodkin_arrows,itm_sword_viking_2_small,itm_sword_viking_2,itm_long_bow,itm_one_handed_battle_axe_a,itm_one_handed_battle_axe_a,
    itm_leather_jerkin,itm_byrnie,itm_leather_boots,itm_nordic_archer_helmet,itm_nordic_veteran_archer_helmet,itm_leather_gloves],
   str_16|agi_14|int_10|cha_10|	level(19),	wpex(100,75,60,90,55,40),knows_common|knows_power_strike_3|knows_ironflesh_2|knows_power_draw_5|knows_athletics_2|knows_riding_1,nord_face_middle_1, nord_face_older_2],
  ["nord_mounted_raider","Mounted Raider","Mounted Raiders",tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_shield|tf_mounted,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_a,itm_tab_shield_round_a,itm_tab_shield_round_b,itm_light_throwing_axes,
    itm_skullcap,itm_nordic_archer_helmet,itm_nasal_helmet,itm_leather_jerkin,itm_hide_boots,itm_sumpter_horse],
   str_13|agi_12|int_7|cha_8|	level(14),	wpex(75,70,70,25,20,70),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_riding_2|knows_power_throw_1|knows_athletics_1|knows_shield_1,nord_face_young_1, nord_face_old_2],
  ["nord_mounted_warrior","Mounted Warrior","Mounted Warriors",tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_mounted|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_one_handed_battle_axe_a,itm_sword_viking_1,itm_tab_shield_round_b,itm_light_throwing_axes,
    itm_nasal_helmet,itm_nordic_footman_helmet,itm_nordic_veteran_archer_helmet,itm_byrnie,itm_leather_boots,itm_leather_gloves,itm_sumpter_horse],
   str_15|agi_14|int_9|cha_10|	level(18),	wpex(100,95,90,30,25,85),knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_3|knows_athletics_2|knows_shield_2,nord_face_young_1, nord_face_old_2],
  ["nord_messenger","Nord Messenger","Nord Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1, nord_face_older_2],
  ["nord_deserter","Nord Deserter","Nord Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   def_attrib|str_10|level(14),wp(80),knows_common|knows_ironflesh_1|knows_power_draw_1,nord_face_young_1, nord_face_older_2],
  ["nord_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_sword_viking_3,itm_one_handed_battle_axe_b,itm_tab_shield_round_d,itm_mail_hauberk,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_mail_mittens],
   def_attrib|level(24),wp(130),knows_common|knows_shield_2|knows_ironflesh_3|knows_power_strike_3,nord_face_middle_1, nord_face_older_2],
  ["nord_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_sword_viking_3,itm_one_handed_battle_axe_b,itm_tab_shield_round_d,itm_tab_shield_round_e,itm_mail_hauberk,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_mail_mittens],
   def_attrib|level(24),wp(130),knows_common|knows_shield_2|knows_ironflesh_3|knows_power_strike_3,nord_face_middle_1, nord_face_older_2],


  ["rhodok_tribesman","Armed Peasant","Armed Peasant",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_pitch_fork,itm_tab_shield_pavise_a,itm_sickle,
    itm_green_tunic,itm_tunic_with_green_cape,itm_wrapping_boots,itm_head_wrappings,itm_straw_hat],
   def_attrib|					level(4),	wpex(50,45,50,15,25,30),knows_common|knows_ironflesh_1|knows_shield_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_spearman","Spearman","Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_spear,itm_tab_shield_pavise_a,
    itm_leather_cap,itm_common_hood,itm_leather_jerkin,itm_leather_armor,itm_aketon_green,itm_wrapping_boots],
   str_11|agi_9|int_5|cha_7|	level(9),	wpex(65,60,70,20,30,40),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_1,rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_trained_spearman","Trained Spearman","Trained Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_pike,itm_war_spear,itm_war_spear,itm_tab_shield_pavise_b,
    itm_footman_helmet,itm_mail_coif,itm_padded_coif,itm_ragged_outfit,itm_aketon_green,itm_leather_boots,itm_leather_gloves],
   str_14|agi_12|int_8|cha_9|	level(15),	wpex(80,70,90,20,40,50),knows_common|knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_athletics_2|knows_riding_1,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman","Veteran Spearman","Veteran Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_war_spear,itm_war_spear,itm_pike,itm_tab_shield_pavise_c,
    itm_mail_coif,itm_kettle_hat,itm_byrnie,itm_leather_boots,itm_mail_chausses,itm_leather_gloves],
   str_17|agi_15|int_11|cha_12|	level(21),	wpex(100,90,115,25,50,60),knows_common|knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_3|knows_riding_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_sergeant","Sergeant","Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_glaive,itm_war_spear,itm_tab_shield_pavise_d,
    itm_guard_helmet,itm_bascinet_3,itm_bascinet_2,itm_surcoat_over_mail,itm_coat_of_plates,itm_mail_boots,itm_mail_mittens],
   str_21|agi_17|int_14|cha_14|	level(27),	wpex(120,105,140,30,60,70),knows_common|knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_4|knows_riding_2,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_swordman","Swordsman","Swordsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_falchion,itm_fighting_pick,itm_club_with_spike_head,itm_tab_shield_pavise_a,
    itm_leather_cap,itm_common_hood,itm_leather_jerkin,itm_leather_armor,itm_wrapping_boots],
   str_11|agi_10|int_5|cha_6|	level(10),	wpex(60,55,60,15,35,45),knows_common|knows_ironflesh_1|knows_shield_1|knows_power_strike_1|knows_athletics_1,rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_trained_swordman","Trained Swordsman","Trained Swordsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_sword_medieval_b_small,itm_club_with_spike_head,itm_fighting_pick,itm_tab_shield_pavise_b,
    itm_footman_helmet,itm_mail_coif,itm_padded_coif,itm_ragged_outfit,itm_aketon_green,itm_leather_boots,itm_leather_gloves],
   str_13|agi_13|int_8|cha_8|	level(15),	wpex(75,65,75,20,40,50),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_2|knows_riding_1,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_swordman","Veteran Swordsman","Veteran Swordsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_sword_medieval_b_small,itm_military_cleaver_b,itm_military_sickle_a,itm_tab_shield_pavise_c,
    itm_mail_coif,itm_kettle_hat,itm_byrnie,itm_ragged_outfit,itm_leather_boots,itm_mail_chausses,itm_leather_gloves],
   str_15|agi_15|int_10|cha_9|	level(19),	wpex(90,75,90,20,45,55),knows_common|knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_athletics_3|knows_riding_1,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_crossbowman","Crossbowman","Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_falchion,itm_fighting_pick,itm_club_with_spike_head,itm_light_crossbow,itm_bolts,
    itm_leather_armor,itm_tunic_with_green_cape,itm_green_tunic,itm_common_hood,itm_wrapping_boots],
   str_11|agi_10|int_5|cha_6|	level(10),	wpex(60,55,55,20,55,30),knows_common|knows_ironflesh_1|knows_shield_1,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_trained_crossbowman","Trained Crossbowman","Trained Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_sword_medieval_a,itm_fighting_pick,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_crossbow,itm_bolts,
    itm_footman_helmet,itm_padded_coif,itm_leather_jerkin,itm_aketon_green,itm_common_hood,itm_wrapping_boots,itm_leather_gloves],
   str_13|agi_13|int_8|cha_7|	level(15),	wpex(70,65,60,30,70,35),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_1|knows_riding_1,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_crossbowman","Veteran Crossbowman","Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_sword_medieval_b_small,itm_military_sickle_a,itm_tab_shield_pavise_b,itm_heavy_crossbow,itm_bolts,
    itm_footman_helmet,itm_kettle_hat,itm_mail_coif,itm_ragged_outfit,itm_aketon_green,itm_leather_boots,itm_leather_gloves],
   str_15|agi_16|int_10|cha_9|	level(20),	wpex(80,75,70,40,85,40),knows_common|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_1|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sharpshooter","Sharpshooter","Sharpshooters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_sword_medieval_b_small,itm_military_cleaver_b,itm_military_pick,itm_tab_shield_pavise_c,itm_sniper_crossbow,itm_steel_bolts,
    itm_kettle_hat,itm_mail_coif,itm_byrnie,itm_leather_boots,itm_mail_chausses,itm_leather_gloves],
   str_18|agi_18|int_13|cha_11|	level(25),	wpex(90,85,80,50,105,45),knows_common|knows_ironflesh_4|knows_shield_3|knows_power_strike_3|knows_athletics_2|knows_riding_2,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_mounted_skirmisher","Mounted Skirmisher","Mounted Skirmishers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_club_with_spike_head,itm_fighting_pick,itm_hunting_crossbow,itm_hunting_crossbow,itm_bolts,
    itm_footman_helmet,itm_common_hood,itm_padded_coif,itm_leather_armor,itm_leather_jerkin,itm_leather_boots,itm_leather_gloves,itm_saddle_horse],
   str_12|agi_12|int_7|cha_8|	level(13),	wpex(75,65,75,20,70,50),knows_common|knows_ironflesh_1|knows_shield_1|knows_riding_2|knows_power_strike_1|knows_athletics_1,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_mounted_trained_skirmisher","Mounted Trained Skirmisher","Mounted Trained Skirmishers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_light_lance,itm_fighting_pick,itm_club_with_spike_head,itm_hunting_crossbow,itm_hunting_crossbow,itm_bolts,
    itm_footman_helmet,itm_padded_coif,itm_aketon_green,itm_ragged_outfit,itm_leather_gloves,itm_leather_boots,itm_saddle_horse],
   str_14|agi_14|int_9|cha_9|	level(17),	wpex(90,85,90,25,85,55),knows_common|knows_ironflesh_1|knows_shield_1|knows_riding_3|knows_power_strike_1|knows_athletics_1|knows_horse_archery_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_mounted_veteran_skirmisher","Mounted Veteran Skirmisher","Mounted Veteran Skirmishers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_military_sickle_a,itm_military_cleaver_b,itm_light_lance,itm_light_crossbow,itm_light_crossbow,itm_steel_bolts,
    itm_mail_coif,itm_kettle_hat,itm_aketon_green,itm_byrnie,itm_leather_boots,itm_leather_gloves,itm_saddle_horse,itm_pack_horse],
   str_16|agi_16|int_11|cha_11|	level(21),	wpex(105,95,105,30,100,60),knows_common|knows_ironflesh_2|knows_shield_2|knows_riding_4|knows_power_strike_2|knows_athletics_2|knows_horse_archery_2,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_messenger","Rhodok Messenger","Rhodok Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_4,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_deserter","Rhodok Deserter","Rhodok Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   def_attrib|str_10|level(14),wp(80),knows_common|knows_ironflesh_1|knows_power_draw_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_military_cleaver_c,itm_military_pick,itm_tab_shield_pavise_b,itm_mail_chausses,itm_byrnie,itm_iron_greaves,itm_guard_helmet,itm_mail_mittens],
   def_attrib|level(24),wp(130),knows_common|knows_shield_2|knows_ironflesh_3|knows_power_strike_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_military_cleaver_c,itm_military_pick,itm_tab_shield_pavise_c,itm_byrnie,itm_mail_chausses,itm_iron_greaves,itm_guard_helmet,itm_mail_mittens],
   def_attrib|level(24),wp(130),knows_common|knows_shield_2|knows_ironflesh_3|knows_power_strike_3,rhodok_face_middle_1, rhodok_face_older_2],
#peasant - retainer - footman - man-at-arms -  knight


  ["sarranid_recruit","Paighan","Paighan",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_knife,itm_falchion,itm_stones,itm_club,
    itm_sarranid_felt_hat,itm_turban,itm_sarranid_boots_a,itm_sarranid_cloth_robe,itm_sarranid_cloth_robe_b],
   def_attrib|					level(4),	wpex(55,45,45,15,15,30),knows_common|knows_athletics_1,sarranid_face_younger_1, sarranid_face_middle_2],
  ["sarranid_footman","Daylami","Daylami",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_mace_2,itm_tab_shield_kite_a,
    itm_skirmisher_armor,itm_desert_turban,itm_turban,itm_sarranid_boots_a,itm_sarranid_boots_b],
   str_9|agi_11|int_5|cha_7|	level(9),	wpex(70,65,65,20,20,45),knows_common|knows_athletics_2|knows_power_strike_1,sarranid_face_young_1, sarranid_face_old_2],
  ["sarranid_veteran_footman","Silihdar","Silihdar",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_bamboo_spear,itm_arabian_sword_a,itm_mace_3,itm_javelin,itm_tab_shield_kite_b,
    itm_sarranid_boots_b,itm_sarranid_warrior_cap,itm_desert_turban,itm_sarranid_leather_armor,itm_leather_gloves],
   str_10|agi_15|int_7|cha_9|	level(14),	wpex(85,80,80,30,30,60),knows_common|knows_ironflesh_1|knows_shield_1|knows_power_strike_2|knows_power_throw_1|knows_athletics_3|knows_riding_1,sarranid_face_young_1, sarranid_face_old_2],
  ["sarranid_infantry","Hajib","Hajib",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
   [itm_arabian_armor_b,itm_sarranid_warrior_cap,itm_sarranid_helmet1,itm_sarranid_mail_coif,itm_sarranid_boots_c,itm_leather_gloves,
    itm_arabian_sword_b,itm_mace_4,itm_bamboo_spear,itm_sarranid_axe_a,itm_javelin,itm_tab_shield_kite_c],
   str_11|agi_19|int_10|cha_11|	level(19),	wpex(105,100,100,35,35,70),knows_common|knows_ironflesh_2|knows_shield_2|knows_athletics_5|knows_power_strike_3|knows_power_throw_2|knows_riding_2,sarranid_face_middle_1, sarranid_face_old_2],
  ["sarranid_guard","Khaskiya","Khaskiya",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
   [itm_arabian_sword_d,itm_bamboo_spear,itm_sarranid_mace_1,itm_sarranid_axe_b,itm_jarid,itm_tab_shield_kite_d,
    itm_sarranid_mail_shirt,itm_sarranid_boots_d,itm_sarranid_veiled_helmet,itm_mail_mittens],
   str_13|agi_21|int_12|cha_13|	level(24),	wpex(125,120,120,40,40,80),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_athletics_6|knows_power_throw_2|knows_riding_2,sarranid_face_middle_1, sarranid_face_older_2],
  ["sarranid_skirmisher","Talaiah","Talaiah",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_turban,itm_desert_turban,itm_skirmisher_armor,itm_sarranid_warrior_cap,itm_sarranid_boots_a,itm_leather_gloves,
    itm_javelin,itm_javelin,itm_javelin,itm_arabian_sword_a,itm_mace_2],
   str_9|agi_16|int_7|cha_9|	level(14),	wpex(80,70,70,30,30,90),knows_common|knows_power_throw_2|knows_power_strike_1|knows_ironflesh_1|knows_athletics_4|knows_riding_1,sarranid_face_young_1, sarranid_face_middle_2],
  ["sarranid_archer","Ramat","Ramat",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,itm_mace_3,itm_tab_shield_small_round_a,
    itm_archers_vest,itm_sarranid_boots_b,itm_sarranid_helmet1,itm_sarranid_warrior_cap,itm_desert_turban,itm_leather_gloves],
   str_10|agi_20|int_10|cha_11|	level(19),	wpex(90,80,80,40,40,110),knows_common|knows_power_throw_3|knows_ironflesh_1|knows_athletics_5|knows_power_strike_2|knows_shield_1|knows_riding_2,sarranid_face_young_1, sarranid_face_old_2],
  ["sarranid_master_archer","Sultaneya Ramat","Sultaneya Ramat",tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
   [itm_arabian_sword_b,itm_mace_4,itm_jarid,itm_jarid,itm_jarid,itm_tab_shield_small_round_b,
    itm_arabian_armor_b,itm_sarranid_boots_c,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_leather_gloves],
   str_12|agi_23|int_12|cha_13|	level(24),	wpex(100,90,90,50,50,130),knows_common|knows_power_throw_4|knows_ironflesh_2|knows_athletics_6|knows_power_strike_3|knows_shield_2|knows_riding_2,sarranid_face_middle_1, sarranid_face_older_2],
  ["sarranid_cavalry","Forsan","Forsan",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
   [itm_javelin,itm_mace_3,itm_arabian_sword_b,itm_tab_shield_small_round_a,
    itm_sarranid_boots_b,itm_sarranid_leather_armor,itm_sarranid_cavalry_robe,itm_sarranid_warrior_cap,itm_desert_turban,itm_leather_gloves,itm_arabian_horse_a],
   str_11|agi_16|int_8|cha_9|	level(16),	wpex(90,85,85,30,30,65),knows_common|knows_ironflesh_1|knows_riding_4|knows_power_throw_1|knows_shield_1|knows_power_strike_1|knows_athletics_2,sarranid_face_young_1, sarranid_face_old_2],
  ["sarranid_horseman","Mamalik Kitabeya","Mamalik Kitabeya",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_6,
   [itm_bamboo_spear,itm_arabian_sword_b,itm_mace_4,itm_javelin,itm_sarranid_axe_a,itm_tab_shield_small_round_b,
    itm_sarranid_cavalry_robe,itm_arabian_armor_b,itm_sarranid_boots_c,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_leather_gloves,itm_arabian_horse_b,itm_arabian_horse_a],
   str_13|agi_19|int_11|cha_10|	level(21),	wpex(100,95,95,35,35,70),knows_common|knows_riding_5|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_power_throw_2|knows_athletics_2,sarranid_face_young_1, sarranid_face_old_2],
  ["sarranid_mamluke","Mamluk","Mamluk",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_bamboo_spear,itm_sarranid_cavalry_sword,itm_sarranid_axe_b,itm_jarid,itm_tab_shield_small_round_c,
    itm_sarranid_mail_shirt,itm_sarranid_boots_d,itm_sarranid_veiled_helmet,itm_arabian_horse_b,itm_mail_mittens],
   str_15|agi_22|int_13|cha_12|	level(26),	wpex(120,110,120,40,40,75),knows_common|knows_riding_6|knows_shield_3|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_athletics_3,sarranid_face_middle_1, sarranid_face_older_2],
  ["sarranid_clibanarii","Clibanarii","Clibanarii",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_sarranid_mace_1,itm_jarid,itm_sarranid_two_handed_mace_1,itm_tab_shield_small_round_c,
    itm_sarranid_mail_shirt,itm_sarranid_boots_d,itm_sarranid_veiled_helmet,itm_arabian_horse_b,itm_mail_mittens],
   str_16|agi_21|int_13|cha_12|	level(26),	wpex(120,115,110,40,40,80),knows_common|knows_power_throw_2|knows_riding_6|knows_shield_2|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3,sarranid_face_middle_1, sarranid_face_older_2],

  ["sarranid_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_bamboo_spear,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_sarranid_helmet1,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,sarranid_face_young_1, sarranid_face_old_2],
  ["sarranid_deserter","Sarranid Deserter","Sarranid Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bamboo_spear,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_desert_turban,itm_arabian_horse_a],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,sarranid_face_young_1, sarranid_face_old_2],
  ["sarranid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_sarranid_cavalry_sword,itm_bamboo_spear,itm_mace_4,itm_sarranid_boots_c,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
   def_attrib|level(24),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,sarranid_face_middle_1, sarranid_face_older_2],
  ["sarranid_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_sarranid_cavalry_sword,itm_bamboo_spear,itm_mace_4,itm_sarranid_boots_c, itm_sarranid_boots_d,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
   def_attrib|level(24),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,sarranid_face_middle_1, sarranid_face_older_2],
   
   
  ["draftee","Draftee","Draftees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_wrapping_boots,itm_coarse_tunic,itm_felt_hat,itm_felt_hat_b,
   itm_club,itm_pickaxe,itm_cleaver,itm_scythe],
   def_attrib|					level(4),	wpex(50,50,50,15,15,30),knows_common|knows_athletics_1,man_face_younger_1, man_face_middle_2],
  ["spotter","Spotter","Spotters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_hide_boots,itm_leather_vest,itm_coarse_tunic,itm_leather_cap,itm_fur_hat,
   itm_falchion,itm_shortened_spear,itm_one_handed_war_axe_a,itm_darts],
   str_10|agi_10|int_5|cha_7|	level(9),	wpex(70,65,65,25,25,70),knows_common|knows_athletics_2|knows_ironflesh_1,man_face_young_1, man_face_old_2],
  ["footman","Footman","Footmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_hide_boots,itm_nomad_boots,itm_leather_vest,itm_gambeson,itm_padded_coif,itm_footman_helmet,
   itm_long_spiked_club,itm_spear],
   str_12|agi_9|int_5|cha_7|	level(10),	wpex(60,60,65,25,25,45),knows_common|knows_athletics_1|knows_ironflesh_1|knows_power_strike_1,man_face_young_1, man_face_old_2],
  ["scout","Scout","Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_8,
   [itm_hide_boots,itm_nomad_boots,itm_leather_vest,itm_gambeson,itm_leather_cap,itm_leather_gloves,
   itm_falchion,itm_light_lance,itm_sword_medieval_a,itm_sword_medieval_a_long,itm_one_handed_war_axe_a,itm_darts,itm_steppe_horse,itm_saddle_horse],
   str_12|agi_13|int_7|cha_9|	level(14),	wpex(85,80,80,35,35,90),knows_common|knows_athletics_3|knows_power_throw_1|knows_riding_2|knows_power_strike_1|knows_horse_archery_1,man_face_young_1, man_face_old_2],
  ["pathfinder","Pathfinder","Pathfinders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_kingdom_8,
   [itm_leather_boots,itm_leather_jerkin,itm_gambeson,itm_footman_helmet,itm_leather_gloves,
   itm_falchion,itm_light_lance,itm_maul,itm_sword_medieval_a,itm_sword_medieval_a_long,itm_one_handed_battle_axe_a,itm_war_darts,itm_steppe_horse,itm_courser],
   str_15|agi_16|int_10|cha_11|	level(20),	wpex(100,95,95,45,45,110),knows_common|knows_athletics_4|knows_power_throw_2|knows_riding_4|knows_ironflesh_1|knows_power_strike_2|knows_horse_archery_2,man_face_middle_1, man_face_old_2],
  ["trainee","Trainee","Trainees",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_leather_boots,itm_gambeson,itm_leather_vest,itm_leather_gloves,
   itm_sword_medieval_a,itm_cartridges,itm_flintlock_pistol,itm_tab_shield_heater_cav_a],
   str_11|agi_16|int_8|cha_9|	level(16),	wpex(90,80,80,35,35,80)|wp_firearm(50),knows_common|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1,man_face_young_1, man_face_old_2],
  ["apprentice","Apprentice","Apprentices",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_leather_boots,itm_gambeson,itm_light_leather,itm_leather_gloves,
   itm_sword_medieval_b,itm_cartridges,itm_flintlock_pistol,itm_tab_shield_heater_cav_a],
   str_13|agi_20|int_11|cha_10|	level(22),	wpex(95,80,80,45,45,85)|wp_firearm(65),knows_common|knows_athletics_3|knows_ironflesh_2|knows_power_strike_2,man_face_middle_1, man_face_old_2],
  ["initiate","Initiate","Initiates",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_mail_boots,itm_mail_hauberk,itm_brigandine_red,itm_mail_and_plate,itm_mail_mittens,
   itm_sword_medieval_d,itm_cartridges,itm_flintlock_pistol,itm_tab_shield_heater_cav_b],
   str_17|agi_22|int_14|cha_12|	level(28),	wpex(120,100,100,60,60,95)|wp_firearm(70),knows_common|knows_athletics_5|knows_ironflesh_3|knows_power_strike_4,man_face_middle_1, man_face_older_2],
  ["adept","Adept","Adepts",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_leather_boots,itm_light_leather,itm_light_mail_and_plate,itm_leather_gloves,
   itm_sword_medieval_d,itm_cartridges,itm_flintlock_pistol,itm_tab_shield_heater_cav_b],
   str_15|agi_24|int_14|cha_10|	level(28),	wpex(100,85,85,60,60,90)|wp_firearm(80),knows_common|knows_athletics_4|knows_ironflesh_3|knows_power_strike_3,man_face_middle_1, man_face_older_2], 
  ["light_infantry","Light Infantry","Light Infantries",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_8, 
   [itm_leather_boots,itm_leather_jerkin,itm_light_mail_and_plate,itm_helmet_with_neckguard,itm_footman_helmet,itm_leather_gloves,
   itm_long_hafted_knobbed_mace,itm_long_hafted_knobbed_mace,itm_war_spear],
   str_15|agi_11|int_8|cha_8|	level(15),	wpex(75,75,80,30,30,60),knows_common|knows_athletics_1|knows_ironflesh_2|knows_power_strike_2|knows_shield_1,man_face_young_2, man_face_old_1],
  ["medium_infantry","Medium Infantry","Medium Infantries",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_mail_chausses,itm_leather_boots,itm_mail_hauberk,itm_mail_and_plate,itm_mail_and_plate,itm_mail_and_plate,itm_kettle_hat,itm_spiked_helmet,itm_leather_gloves,
   itm_long_hafted_knobbed_mace,itm_long_hafted_spiked_mace],
   str_17|agi_14|int_10|cha_10|	level(20),	wpex(95,95,100,35,35,75),knows_common|knows_athletics_1|knows_ironflesh_3|knows_power_strike_3|knows_shield_2,man_face_old_1, man_face_middle_2],
  ["heavy_infantry","Heavy Infantry","Heavy Infantries",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_mail_chausses,itm_mail_hauberk,itm_brigandine_red,itm_kettle_hat,itm_spiked_helmet,itm_bascinet,itm_mail_mittens,
   itm_long_hafted_spiked_mace],
   str_20|agi_16|int_13|cha_12|	level(25),	wpex(115,110,120,40,40,90),knows_common|knows_athletics_1|knows_ironflesh_4|knows_power_strike_4|knows_shield_2,man_face_old_1, man_face_middle_2],
  ["guard","Guard","Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_mail_boots,itm_iron_greaves,itm_scale_armor,itm_coat_of_plates,itm_bascinet,itm_bascinet_b,itm_bascinet_c,itm_guard_helmet,itm_gauntlets,itm_mail_mittens,
   itm_bec_de_corbin_a],
   str_24|agi_17|int_15|cha_14|	level(30),	wpex(135,130,140,50,50,100),knows_common|knows_athletics_2|knows_ironflesh_5|knows_power_strike_5|knows_shield_3,man_face_older_1, man_face_middle_2],
  ["light_cavalry","Light Cavalry","Light Cavalries",tf_mounted|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_leather_boots,itm_leather_jerkin,itm_helmet_with_neckguard,itm_footman_helmet,itm_leather_gloves,
   itm_long_hafted_knobbed_mace,itm_sword_medieval_a_long,itm_fighting_pick,itm_tab_shield_heater_cav_a,itm_saddle_horse,itm_sumpter_horse],
   str_15|agi_12|int_8|cha_9|	level(16),	wpex(85,80,85,30,30,65)|wp_firearm(50),knows_common|knows_ironflesh_2|knows_power_strike_1|knows_riding_2|knows_horse_archery_1|knows_shield_1,man_face_young_2, man_face_old_1],
  ["heavy_cavalry","Heavy Cavalry","Heavy Cavalries",tf_mounted|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_leather_boots,itm_light_mail_and_plate,itm_mail_and_plate,itm_kettle_hat,itm_spiked_helmet,itm_helmet_with_neckguard,itm_leather_gloves,
   itm_sword_medieval_d_long,itm_long_hafted_spiked_mace,itm_military_pick,itm_cartridges,itm_flintlock_pistol,itm_tab_shield_heater_cav_a,itm_pack_horse],
   str_16|agi_15|int_10|cha_10|	level(20),	wpex(100,90,100,35,35,80)|wp_firearm(60),knows_common|knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_riding_3|knows_horse_archery_2|knows_shield_2,man_face_old_1, man_face_middle_2],
  ["paladin","Paladin","Paladins",tf_mounted|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_mail_chausses,itm_mail_boots,itm_mail_hauberk,itm_bascinet,itm_bascinet_b,itm_bascinet_c,itm_kettle_hat,itm_mail_mittens,
   itm_sword_medieval_d_long,itm_long_hafted_spiked_mace,itm_morningstar,itm_cartridges,itm_flintlock_pistol,itm_tab_shield_heater_cav_b,itm_hunter],
   str_17|agi_18|int_12|cha_12|	level(24),	wpex(120,110,120,40,40,90)|wp_firearm(70),knows_common|knows_athletics_2|knows_ironflesh_4|knows_power_strike_3|knows_riding_4|knows_horse_archery_3|knows_shield_3,man_face_older_1, man_face_middle_2],
  ["original_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_brigandine_red,itm_kettle_hat,itm_spiked_helmet,itm_mail_mittens,itm_mail_boots,
    itm_morningstar,itm_sword_medieval_d_long,itm_tab_shield_heater_d],
   def_attrib|level(24),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,man_face_middle_1, man_face_older_2],
  ["original_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_scale_armor,itm_guard_helmet,itm_mail_mittens,itm_mail_boots,
    itm_morningstar,itm_sword_medieval_d_long,itm_tab_shield_heater_d],
   def_attrib|level(24),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,man_face_middle_1, man_face_older_2],
   

  ["looter","Looter","Looters",0,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_club,
    itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_wrapping_boots],
   def_attrib|					level(2),	wpex(20,20,20,10,10,15),knows_common,bandit_face1, bandit_face2],
  ["bandit","Bandit","Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_winged_mace,itm_sword_viking_1,itm_hunting_bow,itm_falchion,itm_throwing_knives,
    itm_rawhide_coat,itm_felt_hat_b,itm_head_wrappings,itm_leather_cap,itm_tabard,itm_coarse_tunic,itm_pelt_coat,itm_nomad_armor,itm_nomad_boots,itm_wrapping_boots],
   str_8|agi_9|int_5|cha_5|		level(6),	wpex(55,55,50,45,45,50),knows_common|knows_power_draw_1|knows_athletics_1|knows_power_strike_1,bandit_face1, bandit_face2],
  ["brigand","Brigand","Brigands",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [itm_arrows,itm_winged_mace,itm_sword_viking_1,itm_falchion,itm_sword_medieval_a,itm_short_bow,itm_throwing_knives,
    itm_leather_cap,itm_felt_hat_b,itm_fur_hat,itm_leather_jerkin,itm_nomad_vest,itm_pelt_coat,itm_nomad_boots],
    str_10|agi_11|int_5|cha_7|	level(10),	wpex(70,70,65,60,60,65),knows_common|knows_power_draw_2|knows_athletics_2|knows_power_strike_2|knows_ironflesh_1,bandit_face1, bandit_face2],
  ["thug","Thug","Thugs",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_barbed_arrows,itm_short_bow,itm_falchion,itm_spiked_mace,itm_sword_viking_2,itm_sword_medieval_b,
    itm_black_hood,itm_common_hood,itm_leather_jerkin,itm_leather_boots,itm_nomad_vest,itm_leather_gloves],
    str_12|agi_13|int_7|cha_9|	level(14),	wpex(85,80,75,75,75,80),knows_common|knows_power_draw_2|knows_athletics_3|knows_power_strike_3|knows_ironflesh_2,bandit_face1, bandit_face2],
  ["murderer","Murderer","Murderers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_bodkin_arrows,itm_spiked_mace,itm_sword_viking_2,itm_sword_medieval_b,itm_short_bow,itm_throwing_daggers,
    itm_pilgrim_hood,itm_common_hood,itm_black_hood,itm_pilgrim_disguise,itm_ragged_outfit,itm_leather_jerkin,itm_leather_boots,itm_leather_gloves],
    str_14|agi_15|int_9|cha_10|	level(18),	wpex(100,95,90,90,90,95),knows_common|knows_power_draw_3|knows_athletics_4|knows_riding_3|knows_power_strike_4|knows_ironflesh_2,bandit_face1, bandit_face2],
  ["assassin","Assassin","Assassins",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_throwing_daggers,itm_scimitar_c,itm_sword_medieval_b_small,itm_sword_viking_2_small,
    itm_pilgrim_hood,itm_pilgrim_disguise,itm_leather_boots,itm_leather_gloves],
    str_12|agi_15|int_8|cha_13|	level(16),	wpex(130,120,115,80,80,100),knows_common|knows_power_throw_2|knows_athletics_6|knows_power_strike_5,bandit_face1, bandit_face2],
  ["mountain_bandit","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows_b,itm_sword_viking_1,itm_winged_mace,itm_maul,itm_falchion,itm_short_bow,itm_javelin,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_felt_hat,itm_head_wrappings,itm_skullcap,itm_ragged_outfit,itm_rawhide_coat,itm_leather_armor,itm_hide_boots,itm_nomad_boots,itm_wooden_shield,itm_nordic_shield],
   str_13|agi_8|int_5|cha_10|	level(10),	wpex(85,95,80,70,50,75),knows_common|knows_power_draw_1|knows_power_strike_1|knows_power_throw_1|knows_ironflesh_2,rhodok_face_young_1, rhodok_face_old_2],
  ["mountain_raider","Mountain Raider","Mountain Raiders",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_barbed_arrows,itm_sword_viking_1,itm_winged_mace,itm_maul,itm_short_bow,itm_javelin,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_head_wrappings,itm_skullcap,itm_studded_leather_coat,itm_ragged_outfit,itm_nomad_vest,itm_nomad_boots,itm_wooden_shield,itm_nordic_shield],
   str_17|agi_10|int_8|cha_13|	level(16),	wpex(115,125,105,90,60,95),knows_common|knows_power_draw_2|knows_power_strike_2|knows_power_throw_2|knows_athletics_1|knows_ironflesh_3,rhodok_face_young_1, rhodok_face_old_2],
  ["mountain_cavalry","Mountain Cavalry","Mountain Cavalries",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arrows_b,itm_sword_viking_1,itm_winged_mace,itm_maul,itm_falchion,itm_short_bow,itm_javelin,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_head_wrappings,itm_skullcap,itm_tribal_warrior_outfit,itm_ragged_outfit,itm_nomad_vest,itm_nomad_boots,itm_wooden_shield,itm_nordic_shield,itm_saddle_horse,itm_sumpter_horse],
   str_15|agi_11|int_8|cha_11|	level(15),	wpex(105,105,95,85,55,90),knows_common|knows_riding_3|knows_power_strike_1|knows_power_draw_2|knows_power_throw_1|knows_ironflesh_2,rhodok_face_young_1, rhodok_face_old_2],
  ["forest_bandit","Forest Bandit","Forest Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_bolts,itm_mace_1,itm_axe,itm_hatchet,itm_quarter_staff,itm_hunting_bow2,itm_hunting_crossbow,
    itm_common_hood,itm_black_hood,itm_shirt,itm_padded_leather,itm_leather_jerkin,itm_ragged_outfit,itm_nomad_boots,itm_leather_boots],
   str_10|agi_12|int_6|cha_9|	level(11),	wpex(80,90,90,75,75,40),knows_common|knows_power_draw_2|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["forest_warrior","Forest Warrior","Forest Warriors",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_bolts,itm_axe,itm_fighting_axe,itm_quarter_staff,itm_long_spiked_club,itm_short_bow2,itm_light_crossbow,
    itm_common_hood,itm_black_hood,itm_padded_leather,itm_leather_jerkin,itm_ragged_outfit,itm_leather_boots,itm_leather_gloves],
   str_13|agi_14|int_8|cha_11|	level(16),	wpex(100,110,110,80,80,55),knows_common|knows_power_draw_2|knows_power_strike_1|knows_athletics_2,swadian_face_young_1, swadian_face_old_2],
  ["forest_hunter","Forest Hunter","Forest Hunters",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_barbed_arrows,itm_bolts,itm_axe,itm_hatchet,itm_quarter_staff,itm_short_bow2,itm_crossbow,
    itm_common_hood,itm_black_hood,itm_padded_leather,itm_leather_jerkin,itm_ragged_outfit,itm_leather_boots,itm_leather_gloves],
   str_12|agi_14|int_8|cha_10|	level(15),	wpex(85,95,95,90,90,45),knows_common|knows_power_draw_3|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["forest_ranger","Forest Ranger","Forest Rangers",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_bodkin_arrows,itm_steel_bolts,itm_axe,itm_quarter_staff,itm_short_bow2,itm_crossbow,
    itm_common_hood,itm_black_hood,itm_padded_leather,itm_leather_jerkin,itm_ragged_outfit,itm_leather_boots,itm_leather_gloves],
   str_13|agi_17|int_10|cha_10|	level(19),	wpex(90,100,100,100,100,50),knows_common|knows_power_draw_4|knows_athletics_2|knows_power_strike_1,swadian_face_young_1, swadian_face_old_2],
  ["sea_raider","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_arrows_b,itm_sword_viking_1,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_wooden_shield_2,itm_kite_shield_a,itm_wooden_shield,itm_short_bow,itm_javelin,itm_light_throwing_axes,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_nasal_helmet,itm_nordic_footman_helmet,itm_nomad_vest,itm_byrnie,itm_leather_boots,itm_nomad_boots,itm_leather_gloves],
   str_15|agi_11|int_8|cha_11|	level(15),	wpex(105,100,100,75,50,75),knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_2|knows_power_throw_2|knows_athletics_2|knows_shield_1,nord_face_young_1, nord_face_old_2],
  ["skull_crusher","Skull Crusher","Skull Crushers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_barbed_arrows,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_war_spear,itm_wooden_shield_2,itm_kite_shield_a,itm_nordic_shield,itm_long_bow2,itm_javelin,itm_throwing_axes,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_huscarl_helmet,itm_nordic_helmet,itm_nordic_warlord_helmet,itm_mail_hauberk,itm_byrnie,itm_mail_chausses,itm_leather_gloves,itm_mail_mittens],
   str_17|agi_14|int_10|cha_14|	level(20),	wpex(135,130,130,75,55,85),knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_draw_4|knows_power_throw_2|knows_athletics_2|knows_shield_2,nord_face_young_1, nord_face_old_2],
  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace, itm_light_lance,itm_hunting_bow,itm_short_bow,itm_javelin,
    itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,itm_nomad_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_leather_vest,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   str_11|agi_12|int_6|cha_9|	level(12),	wpex(90,80,90,70,30,65),knows_common|knows_riding_3|knows_horse_archery_2|knows_power_draw_2|knows_power_throw_1,khergit_face_young_1, khergit_face_old_2],
  ["steppe_rider","Steppe Raider","Steppe Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_barbed_arrows,itm_sword_khergit_1,itm_winged_mace, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_javelin,itm_leather_covered_round_shield,itm_leather_covered_round_shield,
    itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,itm_leather_steppe_cap_c,itm_tribal_warrior_outfit,itm_nomad_vest,itm_leather_vest,itm_leather_boots,itm_nomad_boots,itm_leather_gloves,itm_steppe_horse],
   str_13|agi_15|int_8|cha_12|	level(17),	wpex(115,105,120,85,35,80),knows_common|knows_riding_4|knows_horse_archery_3|knows_power_draw_3|knows_power_strike_1|knows_power_throw_2,khergit_face_young_1, khergit_face_old_2],
  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [itm_arrows_b,itm_sword_khergit_1,itm_winged_mace,itm_nomad_bow,itm_nomad_bow2,itm_javelin,
    itm_vaegir_fur_cap,itm_leather_steppe_cap_c,itm_nomad_armor,itm_leather_jerkin,itm_hide_boots,itm_nomad_boots],
   str_9|agi_14|int_6|cha_9|	level(12),	wpex(90,85,80,75,30,70),knows_common|knows_power_draw_2|knows_athletics_2|knows_power_throw_2,vaegir_face_young_1, vaegir_face_old_2],
  ["tundra_bandit","Tundra Bandit","Tundra Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_barbed_arrows,itm_sword_khergit_1,itm_winged_mace,itm_strong_bow2,itm_strong_bow,itm_jarid,
    itm_vaegir_fur_cap,itm_leather_steppe_cap_b,itm_leather_steppe_cap_c,itm_leather_vest,itm_leather_boots,itm_nomad_boots,itm_leather_gloves],
   str_10|agi_17|int_8|cha_10|	level(16),	wpex(95,90,85,90,35,75),knows_common|knows_power_draw_3|knows_athletics_3|knows_power_throw_3,vaegir_face_young_1, vaegir_face_old_2],
  ["desert_bandit","Desert Bandit","Desert Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arabian_sword_a,itm_javelin,itm_mace_3,itm_leather_covered_round_shield,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe, itm_skirmisher_armor, itm_desert_turban, itm_turban,itm_sarranid_boots_a,itm_sarranid_boots_b,itm_arabian_horse_a],
   str_7|agi_12|int_5|cha_8|	level(8),	wpex(80,75,75,30,30,70),knows_common|knows_riding_4|knows_horse_archery_1|knows_power_throw_1,sarranid_face_young_1, sarranid_face_old_2],
  ["desert_rider","Desert Rider","Desert Riders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arabian_sword_b,itm_mace_4,itm_bamboo_spear,itm_javelin,itm_leather_covered_round_shield,itm_leather_covered_round_shield,
    itm_sarranid_cloth_robe_b,itm_archers_vest,itm_sarranid_boots_a,itm_sarranid_boots_b,itm_desert_turban,itm_turban,itm_arabian_horse_b,itm_leather_gloves],
   str_10|agi_15|int_7|cha_11|	level(15),	wpex(110,100,105,35,40,90),knows_common|knows_riding_5|knows_horse_archery_2|knows_power_strike_1|knows_power_throw_2,sarranid_face_young_1, sarranid_face_old_2],
  ["desert_skirmisher","Desert Skirmisher","Desert Skirmishers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arabian_sword_a,itm_mace_3,itm_jarid,itm_jarid,itm_leather_covered_round_shield,
    itm_sarranid_cloth_robe_b,itm_sarranid_cloth_robe,itm_sarranid_boots_a,itm_skirmisher_armor,itm_desert_turban,itm_turban,itm_arabian_horse_a],
   str_9|agi_15|int_7|cha_12|	level(14),	wpex(95,85,85,40,35,120),knows_common|knows_riding_5|knows_horse_archery_3|knows_power_throw_3,sarranid_face_young_1, sarranid_face_old_2],
  
  ["black_khergit_horseman","Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
   [itm_arrows,itm_sword_khergit_2,itm_scimitar,itm_scimitar,itm_winged_mace,itm_spear,itm_lance,itm_khergit_bow,itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,itm_steppe_cap,itm_nomad_cap,itm_khergit_war_helmet,itm_khergit_war_helmet,itm_mail_hauberk,itm_lamellar_armor,itm_hide_boots,itm_plate_covered_round_shield,itm_plate_covered_round_shield,itm_saddle_horse,itm_steppe_horse],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],

   
   
   #slavers might need helmets to make them more useful and dangerous if against the player
  ["manhunter","Manhunter","Manhunters",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_manhunters,
   [itm_staff,itm_club,itm_nordic_shield,
    itm_rawhide_coat,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
   str_8|agi_8|int_5|cha_5|		level(5),	wpex(50,45,45,30,30,40),knows_common|knows_ironflesh_1|knows_athletics_1|knows_riding_1,bandit_face1, bandit_face2],
##  ["deserter","Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_swadian_deserters,
##   [itm_arrows,itm_spear,itm_fighting_pick,itm_short_bow,itm_sword,itm_voulge,itm_nordic_shield,itm_round_shield,itm_kettle_hat,itm_leather_cap,itm_padded_cloth,itm_leather_armor,itm_scale_armor,itm_saddle_horse],
##   def_attrib|level(12),wp(60),knows_common,bandit_face1, bandit_face2],

#fac_slavers
##  ["slave_keeper","Slave Keeper","Slave Keepers",tf_guarantee_armor,0,0,fac_manhunters,
##   [itm_cudgel,itm_club,itm_woolen_cap,itm_rawhide_coat,itm_coarse_tunic,itm_nomad_armor,itm_nordic_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
##   def_attrib|level(10),wp(60),knows_common,bandit_face1, bandit_face2],
  ["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_manhunters,
   [itm_winged_mace,itm_staff,itm_nordic_shield,
    itm_rawhide_coat,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse,itm_saddle_horse],
   str_11|agi_11|int_6|cha_7|	level(11),	wpex(70,65,65,35,40,50),knows_common|knows_ironflesh_2|knows_power_strike_1|knows_shield_1|knows_athletics_1|knows_riding_2,bandit_face1, bandit_face2],
  # Followings have helmets, starts 2handed weapons too
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_manhunters,
   [itm_maul,itm_winged_mace,itm_quarter_staff,itm_nordic_shield,
    itm_leather_jerkin,itm_ragged_outfit,itm_leather_boots,itm_leather_gloves,itm_footman_helmet,itm_helmet_with_neckguard,itm_saddle_horse],
   str_14|agi_14|int_9|cha_9|	level(17),	wpex(90,85,85,40,50,60),knows_common|knows_ironflesh_3|knows_riding_3|knows_power_strike_2|knows_shield_2|knows_athletics_1,bandit_face1, bandit_face2],
  ["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves,0,0,fac_manhunters,
   [itm_sledgehammer,itm_spiked_mace,itm_quarter_staff,itm_plate_covered_round_shield,
    itm_mail_shirt,itm_leather_boots,itm_leather_gloves,itm_segmented_helmet,itm_nasal_helmet,itm_mail_coif,itm_pack_horse],
   str_17|agi_16|int_12|cha_11|	level(22),	wpex(110,105,105,45,60,70),knows_common|knows_ironflesh_4|knows_riding_4|knows_power_strike_3|knows_shield_3|knows_athletics_2,bandit_face1, bandit_face2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_manhunters,
   [itm_warhammer,itm_spiked_mace,itm_iron_staff,itm_steel_shield,
    itm_mail_hauberk,itm_mail_chausses,itm_mail_mittens,itm_guard_helmet,itm_bascinet_2,itm_bascinet_3,itm_bascinet,itm_bascinet_b,itm_bascinet_c,itm_hunter],
   str_19|agi_18|int_13|cha_13|	level(26),	wpex(130,125,125,50,70,80),knows_common|knows_ironflesh_5|knows_riding_5|knows_power_strike_4|knows_shield_4|knows_athletics_2,bandit_face1, bandit_face2],

#Rhodok tribal, Hunter, warrior, veteran, warchief

#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
#   [], 
#   def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
#  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
#   [], 
#   def_attrib|level(21),wp(100),knows_common|knows_riding_4,khergit_face1, khergit_face2],
#  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,
#   [], 
#   def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],



  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_bolts,itm_arrows_b,itm_hunting_bow,itm_hunting_crossbow,itm_hatchet,itm_club,itm_pickaxe,itm_knife,
    itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_woolen_hose,itm_wrapping_boots],
   str_8|agi_8|int_5|cha_5|		level(5),	wpex(50,45,45,50,50,45),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_bolts,itm_arrows_b,itm_short_bow,itm_light_crossbow,itm_hatchet,itm_fighting_pick,itm_dagger,
    itm_tabard,itm_coarse_tunic,itm_leather_armor,itm_leather_vest,itm_wrapping_boots],
   str_10|agi_12|int_5|cha_7|	level(10),	wpex(65,60,60,65,65,60),knows_common|knows_athletics_1|knows_power_strike_1|knows_power_draw_1,refugee_face1,refugee_face2],
  ["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_bolts,itm_barbed_arrows,itm_short_bow,itm_light_crossbow,itm_fighting_pick,itm_sword_medieval_a,itm_sword_khergit_1,
    itm_leather_jerkin,itm_leather_vest,itm_red_gambeson,itm_leather_boots,itm_leather_gloves],
   str_12|agi_15|int_8|cha_8|	level(15),	wpex(80,75,75,80,80,70),knows_common|knows_power_strike_2|knows_athletics_2|knows_ironflesh_1|knows_power_draw_2,refugee_face1,refugee_face2],
  ["swordwoman","Swordwoman","Swordwomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_commoners,
   [itm_bolts,itm_sword_medieval_b,itm_sword_khergit_2,itm_fighting_pick,itm_darts,itm_barbed_arrows,itm_light_crossbow,itm_short_bow,itm_tab_shield_kite_b,itm_tab_shield_heater_b,
    itm_haubergeon,itm_tribal_warrior_outfit,itm_mail_chausses,itm_leather_boots,itm_leather_gloves],
   str_15|agi_17|int_10|cha_11|	level(20),	wpex(105,95,100,90,90,85),knows_common|knows_athletics_3|knows_ironflesh_2|knows_power_draw_2|knows_shield_2|knows_power_strike_3|knows_power_throw_1,refugee_face1,refugee_face2],
  ["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_commoners,
   [itm_bolts,itm_sword_medieval_b,itm_sword_khergit_3,itm_military_pick,itm_war_darts,itm_bodkin_arrows,itm_light_crossbow,itm_short_bow,itm_tab_shield_kite_c,itm_tab_shield_heater_c,
    itm_brigandine_red,itm_banded_armor,itm_mail_boots,itm_iron_greaves,itm_kettle_hat,itm_helmet_with_neckguard,itm_mail_coif,itm_mail_mittens],
   str_18|agi_19|int_13|cha_13|	level(25),	wpex(130,115,125,100,100,105),knows_common|knows_athletics_4|knows_ironflesh_3|knows_power_draw_2|knows_shield_4|knows_power_strike_4|knows_power_throw_2,refugee_face1,refugee_face2],
  ["lady_knight","Lady Knight","Lady Knights",tf_mounted|tf_female|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_commoners,
   [itm_bolts,itm_sword_medieval_b,itm_sword_khergit_3,itm_war_darts,itm_military_pick,itm_lance,itm_bodkin_arrows,itm_light_crossbow,itm_short_bow,itm_tab_shield_kite_cav_a,itm_tab_shield_heater_cav_a,
    itm_cuir_bouilli,itm_mail_shirt,itm_mail_boots,itm_iron_greaves,itm_spiked_helmet,itm_helmet_with_neckguard,itm_mail_coif,itm_courser,itm_hunter,itm_mail_mittens],
   str_17|agi_21|int_13|cha_13|	level(26),	wpex(120,105,125,95,95,110),knows_common|knows_riding_5|knows_athletics_3|knows_ironflesh_2|knows_power_draw_2|knows_shield_3|knows_power_strike_3|knows_power_throw_2,refugee_face1,refugee_face2],
  ["fieldwoman","Fieldwoman","Fieldwomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_bolts,itm_barbed_arrows,itm_nomad_bow,itm_crossbow,itm_fighting_pick,itm_sword_medieval_b_small,itm_sword_khergit_2,
    itm_ragged_outfit,itm_tribal_warrior_outfit,itm_leather_boots,itm_leather_gloves],
   str_14|agi_18|int_10|cha_10|	level(20),	wpex(90,80,80,95,95,75),knows_common|knows_power_strike_2|knows_athletics_3|knows_ironflesh_1|knows_power_draw_3,refugee_face1,refugee_face2],
  ["woman_archer","Woman Archer","Women Archers",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_gloves,0,0,fac_commoners,
   [itm_bodkin_arrows,itm_long_bow,itm_strong_bow,itm_khergit_bow,itm_military_pick,itm_sword_medieval_b_small,itm_sword_khergit_3,
    itm_tribal_warrior_outfit,itm_leather_boots,itm_leather_gloves],
   str_16|agi_21|int_13|cha_11|	level(25),	wpex(95,80,80,105,95,80),knows_common|knows_athletics_4|knows_power_strike_2|knows_ironflesh_1|knows_power_draw_4,refugee_face1,refugee_face2],
  ["woman_arbalestrier","Woman Sharpshooter","Women Sharpshooters",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_gloves,0,0,fac_commoners,
   [itm_steel_bolts,itm_heavy_crossbow,itm_military_pick,itm_sword_medieval_b,itm_sword_khergit_3,itm_tab_shield_kite_b,itm_tab_shield_heater_b,
    itm_haubergeon,itm_mail_shirt,itm_leather_boots,itm_kettle_hat,itm_helmet_with_neckguard,itm_leather_gloves],
   str_18|agi_20|int_13|cha_11|	level(26),	wpex(100,80,80,95,110,80),knows_common|knows_athletics_3|knows_shield_2|knows_ironflesh_2|knows_power_strike_3,refugee_face1,refugee_face2],

  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(40),knows_common,refugee_face1,refugee_face2],

  # ["swadian_peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_1,
   # [itm_scythe,itm_pickaxe,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,
    # itm_red_shirt,itm_coarse_tunic,itm_red_tunic,itm_leather_apron,itm_wrapping_boots]
   # def_attrib|level(1),wp(40),knows_common|knows_athletics_1,refugee_face1,refugee_face2],
  # ["vaegir_peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_2,
   # [itm_hatchet,itm_club,itm_axe,itm_stones,
    # itm_linen_tunic, itm_rawhide_coat,itm_hide_boots]
   # def_attrib|level(1),wp(40),knows_common|knows_power_strike_1,refugee_face1,refugee_face2],
  # ["khergit_peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_3,
   # [itm_arrows_b,itm_club,itm_shortened_spear,itm_hunting_bow,
    # itm_steppe_cap,itm_nomad_cap_b,itm_nomad_cap,itm_coarse_tunic,itm_steppe_armor,itm_hide_boots]
   # def_attrib|level(1),wp(40),knows_common|knows_riding_1|knows_power_draw_1|knows_athletics_1,refugee_face1,refugee_face2],
  # ["nord_peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_4,
   # [itm_hatchet,
    # itm_blue_tunic,itm_coarse_tunic,itm_hide_boots]
   # def_attrib|level(1),wp(40),knows_common|knows_power_strike_1,refugee_face1,refugee_face2],
  # ["rhodok_peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_5,
   # [itm_pitch_fork,itm_sickle,
    # itm_green_tunic,itm_tunic_with_green_cape,itm_wrapping_boots,itm_head_wrappings,itm_straw_hat]
   # def_attrib|level(1),wp(40),knows_common|knows_ironflesh_1|knows_shield_1,refugee_face1,refugee_face2],
  # ["sarranid_peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_6,
   # [itm_knife,itm_falchion,itm_stones,itm_club,
    # itm_sarranid_felt_hat,itm_turban,itm_sarranid_boots_a,itm_sarranid_cloth_robe,itm_sarranid_cloth_robe_b]
   # def_attrib|level(1),wp(40),knows_common|knows_athletics_1,refugee_face1,refugee_face2],
  # ["freerider_peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_8,
   # [itm_wrapping_boots,itm_coarse_tunic,itm_felt_hat,itm_felt_hat_b,
   # itm_club,itm_pickaxe,itm_cleaver,itm_scythe]
   # def_attrib|level(1),wp(40),knows_common|knows_athletics_1,refugee_face1,refugee_face2],
 
  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_sword_two_handed_a,itm_fur_coat,itm_leather_boots,itm_leather_gloves,
    itm_hunter,itm_courser,itm_hunter,
    itm_leather_jacket, itm_leather_cap],
   str_14|agi_17|int_10|cha_10|	level(20),	wpex(100,100,90,60,80,70),knows_common|knows_riding_4|knows_ironflesh_3|knows_power_strike_3,mercenary_face_1, mercenary_face_2],

  # Special faction troops -- slightly better than common troop (has it's drawbacks though)
  # Should be used by the kings instead of their usual counterpart (or used as an elite side troop)
  # Biggest problem is not enough troops for all faction
  # Frustration for the player, as he can't have these troops
  # Might aswell be some new troops included in the tree
	
  # ["swadian_swordmaster","Swordmaster","Swordmasters",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_helmet, 0, 0, fac_kingdom_1,
   # [itm_sword_two_handed_a,
    # itm_gauntlets,itm_iron_greaves,itm_great_helmet,itm_guard_helmet,itm_mail_with_surcoat],
   # str_23|agi_16|int_14|cha_14|	level(28),	wpex(130,140,130,60,60,80),knows_common|knows_riding_2|knows_shield_2|knows_ironflesh_3|knows_power_strike_4|knows_athletics_5, swadian_face_middle_1, swadian_face_older_2],
  # Two handed sword, less resistant, faster
  # ["vaegir_druzyna","Druzyna","Druzyna",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   # [itm_scimitar_b,itm_tab_shield_kite_cav_b,
    # itm_banded_armor,itm_lamellar_armor,itm_mail_boots,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_mask,itm_hunter,itm_mail_mittens],
   # str_19|agi_19|int_14|cha_13|	level(27),	wpex(130,125,125,60,25,80),knows_common|knows_riding_5|knows_shield_4|knows_athletics_3|knows_ironflesh_4|knows_power_strike_3,vaegir_face_middle_1, vaegir_face_older_2],
  # Always has a shield, but no lance, no two handed
  # ["nord_hirdman","Hirdman","Hirdmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   # [itm_sword_viking_3,itm_sword_viking_3_small,itm_tab_shield_round_e,
    # itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet,itm_cuir_bouilli,itm_iron_greaves,itm_gauntlets],
   # str_21|agi_18|int_14|cha_16|	level(28),	wpex(160,150,145,50,35,130),knows_common|knows_ironflesh_5|knows_power_strike_6|knows_power_throw_4|knows_athletics_5|knows_shield_5|knows_riding_2,nord_face_middle_1, nord_face_older_2],
  # Better armor, no throwing axes, no one handed axes
  # ["sarranid_mamalik_sultaneya","Mamalik Sultaneya","Mamalik Sultaneya",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   # [itm_sarranid_cavalry_sword,itm_sarranid_axe_b,itm_tab_shield_small_round_c,
    # itm_mamluke_mail,itm_sarranid_boots_d,itm_sarranid_veiled_helmet,itm_arabian_horse_b,itm_mail_mittens],
   # str_16|agi_22|int_14|cha_13|	level(27),	wpex(130,120,130,40,40,75),knows_common|knows_riding_6|knows_shield_3|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3,sarranid_face_middle_1, sarranid_face_older_2],
  # Better armor, no lance, no throwing weapons
	
   
  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   [itm_dress,itm_leather_boots],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],
   
   ## recruit noble start ## # Also used for banner's faction storage
  ["noble_begin","noble_begin","noble_begin",0,no_scene,reserved,fac_commoners,
   [],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
   
## swadian nobles   
  ["swadian_noble", "Page", "Pages", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_fighting_pick,itm_sword_medieval_a,itm_sword_medieval_a_long,itm_light_lance,itm_tab_shield_heater_cav_a,
   itm_leather_gloves,itm_leather_boots,itm_ankle_boots,itm_red_gambeson,itm_red_gambeson,itm_gambeson,itm_saddle_horse,itm_pack_horse],
   str_12|agi_10|int_6|cha_9|	level(11),	wpex(90,80,85,70,70,75),knows_common|knows_athletics_1|knows_riding_2|knows_ironflesh_1|knows_shield_1|knows_power_strike_1,swadian_face_younger_1, swadian_face_younger_2],
  ["swadian_noble2", "Squire", "Squires", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_bastard_sword_a,itm_military_pick,itm_sword_medieval_b,itm_sword_medieval_a_long,itm_light_lance,itm_tab_shield_heater_cav_a,
   itm_leather_gloves,itm_mail_chausses,itm_heraldic_mail_with_tunic,itm_heraldic_mail_with_tunic_b,itm_mail_coif,itm_courser,itm_hunter],
   str_16|agi_13|int_9|cha_11|	level(18),	wpex(110,100,105,80,80,90),knows_common|knows_athletics_2|knows_riding_3|knows_ironflesh_2|knows_shield_2|knows_power_strike_2,swadian_face_young_1, swadian_face_young_2],
  ["swadian_noble3", "Knight", "Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sword_two_handed_b,itm_bastard_sword_a,itm_military_pick,itm_sword_medieval_c,itm_sword_medieval_c_long,itm_lance,itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_b,
   itm_mail_mittens,itm_mail_boots,itm_heraldic_mail_with_tunic,itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_helmet_with_neckguard,itm_mail_coif,itm_flat_topped_helmet,itm_courser,itm_hunter,itm_warhorse],
   str_20|agi_16|int_13|cha_13|	level(25),	wpex(130,120,125,90,90,105),knows_common|knows_athletics_3|knows_riding_4|knows_ironflesh_4|knows_shield_2|knows_power_strike_3,swadian_face_middle_1, swadian_face_middle_2],
  ["swadian_noble4", "Master Knight", "Master Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sword_two_handed_b,itm_bastard_sword_b,itm_sword_medieval_c,itm_sword_medieval_c_long,itm_military_pick,itm_lance,itm_tab_shield_heater_cav_b,
   itm_gauntlets,itm_mail_mittens,itm_iron_greaves,itm_mail_boots,itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_great_helmet,itm_guard_helmet,itm_warhorse],
   str_23|agi_20|int_16|cha_15|	level(32),	wpex(150,120,145,100,100,120),knows_common|knows_athletics_4|knows_riding_5|knows_ironflesh_6|knows_shield_3|knows_power_strike_4,swadian_face_old_1, swadian_face_old_2],
  ["swadian_noble5", "Grandmaster Knight", "Grandmaster Knights", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c,itm_sword_medieval_c_long,itm_heavy_lance,itm_tab_shield_heater_cav_b,itm_sword_two_handed_a,
   itm_iron_greaves,itm_gauntlets,itm_plate_armor,itm_heraldic_mail_with_surcoat,itm_great_helmet,itm_warhorse,itm_charger,itm_charger_b],
   str_27|agi_24|int_20|cha_18|	level(40),	wpex(180,170,175,120,120,140),knows_common|knows_athletics_4|knows_riding_6|knows_ironflesh_8|knows_shield_4|knows_power_strike_5,swadian_face_older_1, swadian_face_older_2],
   
## vaegir nobles
  ["vaegir_noble", "Nemesember", "Nemesemberek", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_two_handed_battle_axe_2,itm_light_lance,itm_scimitar,itm_javelin,
   itm_leather_boots,itm_leather_gloves,itm_studded_leather_coat,itm_leather_vest,itm_vaegir_fur_cap,itm_vaegir_fur_helmet,itm_pack_horse,itm_steppe_horse],
   str_11|agi_11|int_6|cha_9|	level(11),	wpex(85,90,80,80,60,80),knows_common|knows_athletics_1|knows_riding_2|knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_horse_archery_1,vaegir_face_younger_1, vaegir_face_younger_2],
  ["vaegir_noble2", "Nemes Lovassag", "Nemes Lovassag", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_scimitar,itm_battle_axe,itm_light_lance,itm_javelin,itm_tab_shield_kite_cav_a,
   itm_leather_gloves,itm_mail_chausses,itm_tribal_warrior_outfit,itm_studded_leather_coat,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_steppe_horse,itm_steppe_horse,itm_hunter],
   str_15|agi_14|int_9|cha_11|	level(18),	wpex(105,110,100,90,70,100),knows_common|knows_athletics_2|knows_riding_3|knows_ironflesh_2|knows_shield_1|knows_power_strike_2|knows_power_throw_1|knows_horse_archery_1,vaegir_face_young_1, vaegir_face_young_2],
  ["vaegir_noble3", "Lovag", "Lovagok", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_scimitar,itm_bardiche,itm_lance,itm_javelin,itm_javelin,itm_tab_shield_kite_cav_a,
   itm_mail_mittens,itm_mail_chausses,itm_lamellar_vest,itm_brigandine_red,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_helmet,itm_hunter],
   str_19|agi_17|int_13|cha_13|	level(25),	wpex(125,130,120,100,80,120),knows_common|knows_athletics_3|knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_3|knows_power_throw_2|knows_horse_archery_2,vaegir_face_middle_1, vaegir_face_middle_2],
  ["vaegir_noble4", "Mester Lovag", "Mester Lovagok", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_bardiche,itm_scimitar_b,itm_lance,itm_tab_shield_kite_cav_b,itm_throwing_spears,itm_throwing_spears,
   itm_mail_boots,itm_mail_mittens,itm_lamellar_armor,itm_banded_armor,itm_vaegir_noble_helmet,itm_vaegir_helmet,itm_vaegir_war_helmet,itm_warhorse_steppe,itm_warhorse],
   str_22|agi_21|int_16|cha_15|	level(32),	wpex(145,150,140,110,90,140),knows_common|knows_athletics_4|knows_riding_5|knows_ironflesh_4|knows_shield_3|knows_power_strike_4|knows_power_throw_3|knows_horse_archery_2,vaegir_face_old_1, vaegir_face_old_2],
  ["vaegir_noble5", "Nagymester Lovag", "Nagymester Lovagok", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_scimitar_b,itm_great_bardiche,itm_heavy_lance,itm_jarid,itm_jarid,itm_tab_shield_kite_cav_b,
   itm_iron_greaves,itm_gauntlets,itm_banded_armor,itm_lamellar_armor,itm_vaegir_elite_armor,itm_vaegir_war_helmet,itm_vaegir_mask,itm_warhorse_steppe,itm_warhorse],
   str_25|agi_26|int_20|cha_18|	level(40),	wpex(175,180,170,130,110,170),knows_common|knows_athletics_4|knows_riding_6|knows_ironflesh_5|knows_shield_3|knows_power_strike_5|knows_power_throw_4|knows_horse_archery_3,vaegir_face_older_1, vaegir_face_older_2],
   
## khergit nobles
  ["khergit_noble", "Soylu", "Soylular", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_winged_mace,itm_light_lance,itm_nomad_bow,itm_barbed_arrows,itm_tab_shield_small_round_a,
   itm_hide_boots,itm_nomad_boots,itm_leather_gloves,itm_nomad_robe,itm_tribal_warrior_outfit,itm_leather_steppe_cap_b,itm_steppe_horse],
   str_11|agi_11|int_6|cha_9|	level(11),	wpex(85,80,90,80,60,75),knows_common|knows_riding_3|knows_power_strike_1|knows_power_draw_2|knows_power_throw_1|knows_horse_archery_1,khergit_face_younger_1, khergit_face_younger_2],
  ["khergit_noble2", "Soylu Suvari", "Soylular Suvari", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_light_lance,itm_bodkin_arrows,itm_nomad_bow,itm_winged_mace,itm_tab_shield_small_round_b,
   itm_leather_boots,itm_leather_gloves,itm_tribal_warrior_outfit,itm_nomad_robe,itm_lamellar_vest_khergit,itm_leather_steppe_cap_b,itm_spiked_helmet,itm_khergit_war_helmet,itm_steppe_horse,itm_courser],
   str_14|agi_15|int_9|cha_11|	level(18),	wpex(105,100,110,100,70,90),knows_common|knows_riding_4|knows_shield_1|knows_athletics_1|knows_ironflesh_1|knows_power_strike_2|knows_horse_archery_2|knows_power_draw_3|knows_power_throw_2,khergit_face_young_1, khergit_face_young_2],
  ["khergit_noble3", "Sef", "Seflerinin", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_lance,itm_bodkin_arrows,itm_nomad_bow,itm_winged_mace,itm_hafted_blade_b,itm_tab_shield_small_round_b,
   itm_leather_boots,itm_leather_gloves,itm_lamellar_vest_khergit,itm_spiked_helmet,itm_khergit_war_helmet,itm_courser,itm_hunter],
   str_17|agi_19|int_13|cha_13|	level(25),	wpex(125,120,130,120,80,105),knows_common|knows_riding_5|knows_shield_2|knows_athletics_2|knows_ironflesh_2|knows_horse_archery_2|knows_power_strike_3|knows_power_draw_4|knows_power_throw_2,khergit_face_middle_1, khergit_face_middle_2],
  ["khergit_noble4", "Diktator", "Diktator", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_sword_khergit_3,itm_lance,itm_khergit_arrows,itm_khergit_bow,itm_hafted_blade_b,itm_tab_shield_small_round_c,
   itm_leather_boots,itm_leather_gloves,itm_scale_gauntlets,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_splinted_greaves,itm_khergit_cavalry_helmet,itm_hunter,itm_courser,itm_warhorse_steppe],
   str_20|agi_23|int_16|cha_15|	level(32),	wpex(145,140,150,140,90,120),knows_common|knows_riding_6|knows_shield_3|knows_athletics_3|knows_ironflesh_3|knows_horse_archery_3|knows_power_strike_4|knows_power_draw_5|knows_power_throw_3,khergit_face_old_1, khergit_face_old_2],
  ["khergit_noble5", "Az Khan", "Az Khan", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_heavy_lance,itm_khergit_arrows,itm_khergit_bow,itm_hafted_blade_a,itm_tab_shield_small_round_c,
   itm_scale_gauntlets,itm_splinted_greaves,itm_lamellar_armor,itm_khergit_elite_armor,itm_khergit_guard_armor,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_warhorse_steppe],
   str_24|agi_27|int_20|cha_18|	level(40),	wpex(175,170,180,160,100,140),knows_common|knows_riding_7|knows_shield_4|knows_athletics_4|knows_ironflesh_4|knows_horse_archery_3|knows_power_strike_5|knows_power_draw_6|knows_power_throw_3,khergit_face_older_1, khergit_face_older_2],
   
## nord nobles   
  ["nord_noble", "Berserker", "Berserkers", tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_long_axe,
   itm_leather_boots,itm_leather_gloves,itm_byrnie,itm_nasal_helmet,itm_nordic_veteran_archer_helmet,itm_nordic_footman_helmet],
   str_14|agi_9|int_6|cha_10|	level(12),	wpex(95,90,100,75,60,80),knows_common|knows_athletics_1|knows_ironflesh_3|knows_power_strike_3,nord_face_younger_1, nord_face_younger_2],
  ["nord_noble2", "Chief", "Chiefs", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_long_axe,
   itm_leather_boots,itm_leather_gloves,itm_mail_shirt,itm_byrnie,itm_nordic_footman_helmet,itm_nordic_fighter_helmet],
   str_17|agi_13|int_10|cha_13|	level(19),	wpex(120,110,125,90,70,100),knows_common|knows_athletics_2|knows_ironflesh_4|knows_power_strike_4,nord_face_young_1, nord_face_young_2],
  ["nord_noble3", "War Chief", "War Chiefs", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_long_axe_b,
   itm_mail_chausses,itm_mail_mittens,itm_mail_hauberk,itm_mail_shirt,itm_nordic_fighter_helmet,itm_nordic_helmet],
   str_22|agi_16|int_14|cha_15|	level(27),	wpex(140,130,150,105,80,120),knows_common|knows_athletics_3|knows_ironflesh_5|knows_power_strike_5,nord_face_middle_1, nord_face_middle_2],
  ["nord_noble4", "War Lord", "War Lords", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_long_axe_b,
   itm_splinted_leather_greaves,itm_mail_mittens,itm_banded_armor,itm_nordic_huscarl_helmet,itm_nordic_helmet,itm_mail_hauberk],
   str_26|agi_19|int_17|cha_18|	level(34),	wpex(160,150,175,120,90,140),knows_common|knows_athletics_4|knows_ironflesh_6|knows_power_strike_6,nord_face_old_1, nord_face_old_2],
  ["nord_noble5", "Lesser Thane", "Lesser Thanes", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_long_axe_c,
   itm_iron_greaves,itm_gauntlets,itm_banded_armor,itm_cuir_bouilli,itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet],
   str_30|agi_23|int_21|cha_21|	level(42),	wpex(180,170,210,135,100,160),knows_common|knows_athletics_5|knows_ironflesh_7|knows_power_strike_7,nord_face_older_1, nord_face_older_2],
   
## rhodok nobles   
  ["rhodok_noble", "Patrician", "Patricians", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_fighting_pick,itm_sword_medieval_a_long,itm_club_with_spike_head,itm_maul,itm_tab_shield_pavise_b,
   itm_leather_boots,itm_leather_gloves,itm_gambeson,itm_ragged_outfit,itm_sumpter_horse],
   str_13|agi_9|int_6|cha_9|	level(11),	wpex(90,85,80,60,80,75),knows_common|knows_athletics_2|knows_riding_2|knows_ironflesh_1|knows_shield_2|knows_power_strike_1,rhodok_face_younger_1, rhodok_face_younger_2],
  ["rhodok_noble2", "Burgher", "Burghers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_fighting_pick,itm_sword_medieval_a_long,itm_club_with_spike_head,itm_sledgehammer,itm_military_cleaver_b,itm_tab_shield_pavise_b,
   itm_leather_boots,itm_mail_chausses,itm_leather_gloves,itm_byrnie,itm_kettle_hat,itm_mail_coif,itm_pack_horse,itm_saddle_horse],
   str_17|agi_12|int_9|cha_11|	level(18),	wpex(110,105,100,70,95,85),knows_common|knows_athletics_3|knows_riding_2|knows_ironflesh_2|knows_shield_3|knows_power_strike_2,rhodok_face_young_1, rhodok_face_young_2],
  ["rhodok_noble3", "Noble Citizen", "Noble Citizens", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_military_sickle_a,itm_club_with_spike_head,itm_military_cleaver_b,itm_sledgehammer,itm_tab_shield_pavise_c,
   itm_mail_chausses,itm_mail_mittens,itm_byrnie,itm_surcoat_over_mail,itm_kettle_hat,itm_bascinet_2,itm_bascinet_2,itm_bascinet,itm_bascinet_b,itm_bascinet_c,itm_hunter],
   str_21|agi_15|int_13|cha_13|	level(25),	wpex(130,125,120,80,110,95),knows_common|knows_athletics_4|knows_riding_3|knows_ironflesh_3|knows_shield_4|knows_power_strike_3,rhodok_face_middle_1, rhodok_face_middle_2],
  ["rhodok_noble4", "Blue Blood", "Blue Bloods", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_military_cleaver_c,itm_military_pick,itm_warhammer,itm_tab_shield_pavise_c,
   itm_mail_boots,itm_mail_mittens,itm_surcoat_over_mail,itm_kettle_hat,itm_bascinet_3,itm_guard_helmet,itm_warhorse_b,itm_hunter],
   str_26|agi_17|int_16|cha_15|	level(32),	wpex(150,145,140,90,125,105),knows_common|knows_athletics_5|knows_riding_4|knows_ironflesh_4|knows_shield_5|knows_power_strike_4,rhodok_face_old_1, rhodok_face_old_2],
  ["rhodok_noble5", "Hero", "Heroes", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_two_handed_cleaver,itm_military_pick,itm_military_cleaver_c,itm_military_hammer,itm_warhammer,itm_tab_shield_pavise_d,
   itm_mail_boots,itm_mail_mittens,itm_iron_greaves,itm_coat_of_plates,itm_surcoat_over_mail,itm_gauntlets,itm_full_helm,itm_guard_helmet,itm_warhorse_b],
   str_30|agi_21|int_20|cha_18|	level(40),	wpex(180,175,170,100,145,120),knows_common|knows_athletics_6|knows_riding_4|knows_ironflesh_5|knows_shield_6|knows_power_strike_5,rhodok_face_older_1, rhodok_face_older_2],
   
## sarranid nobles
  ["sarranid_noble", "Lybla", "Aynlybla", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_mace_2,itm_tab_shield_small_round_a,
   itm_sarranid_boots_a,itm_archers_vest,itm_skirmisher_armor,itm_turban,itm_arabian_horse_a],
   str_11|agi_11|int_6|cha_9|	level(11),	wpex(85,90,80,60,60,80),knows_common|knows_athletics_1|knows_riding_3|knows_power_strike_1,sarranid_face_younger_1, sarranid_face_younger_2],
  ["sarranid_noble2", "Sraf Lybla", "Nasrfla Lybla", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_6,
   [itm_sarranid_two_handed_axe_a,itm_khergit_sword_two_handed_a,
   itm_sarranid_boots_b,itm_sarranid_leather_armor,itm_leather_gloves,itm_sarranid_helmet1,itm_sarranid_warrior_cap,itm_arabian_horse_a,itm_arabian_horse_b],
   str_15|agi_14|int_9|cha_11|	level(18),	wpex(105,110,100,70,70,95),knows_common|knows_athletics_2|knows_riding_4|knows_ironflesh_1|knows_power_strike_2,sarranid_face_young_1, sarranid_face_young_2],
  ["sarranid_noble3", "Sraf", "Nasrfla", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sarranid_two_handed_axe_a,itm_khergit_sword_two_handed_a,itm_sarranid_two_handed_mace_1,
   itm_sarranid_boots_c,itm_leather_gloves,itm_sarranid_cavalry_robe,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_arabian_horse_b],
   str_18|agi_18|int_13|cha_13|	level(25),	wpex(125,130,120,80,80,110),knows_common|knows_athletics_3|knows_riding_5|knows_ironflesh_2|knows_power_strike_3,sarranid_face_middle_1, sarranid_face_middle_2],
  ["sarranid_noble4", "Dys Sraf", "Dys Nasrfla", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sarranid_two_handed_mace_1,itm_sarranid_two_handed_axe_b,itm_khergit_sword_two_handed_b,
   itm_sarranid_boots_d,itm_mail_mittens,itm_sarranid_mail_shirt,itm_sarranid_veiled_helmet,itm_warhorse_sarranid],
   str_22|agi_21|int_16|cha_15|	level(32),	wpex(145,150,140,90,90,125),knows_common|knows_athletics_4|knows_riding_6|knows_ironflesh_3|knows_power_strike_4,sarranid_face_old_1, sarranid_face_old_2],
  ["sarranid_noble5", "Dzarghayn Sraf", "Dzarghayn Nasrfla", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sarranid_two_handed_mace_1,itm_sarranid_two_handed_axe_b,itm_khergit_sword_two_handed_b,
   itm_sarranid_boots_d,itm_scale_gauntlets,itm_sarranid_elite_armor,itm_mamluke_mail,itm_sarranid_veiled_helmet,itm_warhorse_sarranid],
   str_26|agi_25|int_20|cha_18|	level(40),	wpex(175,180,170,100,100,140),knows_common|knows_athletics_5|knows_riding_7|knows_ironflesh_4|knows_power_strike_5,sarranid_face_older_1, sarranid_face_older_2],
   
## player nobles !!! ## merc tree
  ["player_noble", "Bodyguard", "Bodyguards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
   [itm_fighting_pick,itm_sword_medieval_a,itm_war_spear,itm_tab_shield_kite_c,itm_tab_shield_heater_c,
   itm_leather_gloves,itm_leather_boots,itm_heraldic_mail_with_tunic],
   str_13|agi_10|int_6|cha_10|	level(12),	wpex(100,90,100,70,70,60),knows_common|knows_athletics_3|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,man_face_younger_1, man_face_younger_2],
  ["player_noble2", "Guardian", "Guardians", tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
   [itm_sword_medieval_b,itm_fighting_pick,itm_sword_medieval_b_small,itm_war_spear,itm_tab_shield_kite_c,itm_tab_shield_heater_c,
   itm_leather_gloves,itm_leather_boots,itm_mail_chausses,itm_heraldic_mail_with_tunic,itm_mail_coif],
   str_16|agi_14|int_10|cha_13|	level(19),	wpex(125,110,125,85,85,70),knows_common|knows_athletics_4|knows_ironflesh_2|knows_power_strike_3|knows_shield_2,man_face_young_1, man_face_young_2],
  ["player_noble3", "Personal Guard", "Personal Guards", tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_neutral,
   [itm_military_scythe,
   itm_mail_chausses,itm_mail_mittens,itm_heraldic_mail_with_surcoat,itm_kettle_hat,itm_mail_coif],
   str_21|agi_17|int_14|cha_15|	level(27),	wpex(150,130,150,100,100,80),knows_common|knows_athletics_5|knows_ironflesh_3|knows_power_strike_5|knows_shield_2,man_face_middle_1, man_face_middle_2],
  ["player_noble4", "Elite Guard", "Elite Guards", tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_neutral,
   [itm_voulge,itm_voulge,itm_military_scythe,itm_glaive,itm_glaive,
   itm_mail_mittens,itm_mail_boots,itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_kettle_hat,itm_guard_helmet,itm_bascinet,itm_bascinet_b,itm_bascinet_c],
   str_24|agi_21|int_17|cha_18|	level(34),	wpex(175,150,175,115,115,90),knows_common|knows_athletics_6|knows_ironflesh_4|knows_power_strike_6|knows_shield_2,man_face_old_1, man_face_old_2],
  ["player_noble5", "Royal Guard", "Royal Guards", tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_neutral,
   [itm_glaive,itm_voulge,
   itm_gauntlets,itm_iron_greaves,itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_great_helmet,itm_guard_helmet],
   str_28|agi_25|int_21|cha_21|	level(42),	wpex(210,180,210,130,130,100),knows_common|knows_athletics_7|knows_ironflesh_5|knows_power_strike_7|knows_shield_2,man_face_older_1, man_face_older_2],
   
 ## freerider nobles
  ["freerider_noble", "Mounted Infantry", "Mounted Infantries", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_8,
   [itm_fighting_pick,itm_sword_medieval_a,itm_sword_medieval_a_long,itm_tab_shield_heater_cav_a,
   itm_leather_gloves,itm_leather_boots,itm_light_leather,itm_saddle_horse],
   str_10|agi_12|int_6|cha_9|	level(11),	wpex(90,85,80,60,65,75),knows_common|knows_athletics_1|knows_riding_1|knows_ironflesh_1|knows_power_strike_1|knows_shield_1,man_face_younger_1, man_face_younger_2],
  ["freerider_noble2", "Carabinier", "Carabiniers", tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_8,
   [itm_sword_medieval_b,itm_fighting_pick,itm_sword_medieval_b_small,itm_tab_shield_heater_cav_a,itm_fighting_pick,itm_flintlock_pistol,itm_cartridges,
   itm_leather_gloves,itm_leather_boots,itm_mail_chausses,itm_light_mail_and_plate,itm_mail_and_plate,itm_mail_coif,itm_pack_horse],
   str_13|agi_16|int_9|cha_11|	level(18),	wpex(110,105,100,70,75,90)|wp_firearm(60),knows_common|knows_athletics_2|knows_riding_2|knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_horse_archery_1,man_face_young_1, man_face_young_2],
  ["freerider_noble3", "Elite Carabinier", "Elite Carabiniers", tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_tab_shield_heater_cav_a,itm_sword_medieval_d,itm_military_pick,itm_flintlock_pistol,itm_cartridges,
   itm_mail_chausses,itm_mail_mittens,itm_mail_and_plate,itm_kettle_hat,itm_mail_coif,itm_hunter],
   str_16|agi_20|int_13|cha_13|	level(25),	wpex(130,125,120,80,85,105)|wp_firearm(70),knows_common|knows_athletics_2|knows_riding_3|knows_ironflesh_3|knows_power_strike_3|knows_shield_2|knows_horse_archery_1,man_face_middle_1, man_face_middle_2],
  ["freerider_noble4", "Dragoon", "Dragoons", tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_tab_shield_heater_cav_b,itm_sword_medieval_d,itm_shortened_military_scythe,itm_military_pick,itm_flintlock_pistol,itm_cartridges,
   itm_mail_mittens,itm_mail_boots,itm_mail_hauberk,itm_kettle_hat,itm_bascinet,itm_bascinet_b,itm_bascinet_c,itm_hunter],
   str_18|agi_25|int_16|cha_15|	level(32),	wpex(150,145,140,90,95,120)|wp_firearm(80),knows_common|knows_athletics_3|knows_riding_3|knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_horse_archery_2,man_face_old_1, man_face_old_2],
  ["freerider_noble5", "Dragoon Guard", "Dragoon Guards", tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_tab_shield_heater_cav_b,itm_sword_medieval_d,itm_sword_medieval_d_long,itm_shortened_military_scythe,itm_morningstar,itm_flintlock_pistol,itm_cartridges,
   itm_gauntlets,itm_iron_greaves,itm_scale_armor,itm_guard_helmet,itm_warhorse],
   str_22|agi_29|int_20|cha_18|	level(40),	wpex(180,175,170,100,110,135)|wp_firearm(90),knows_common|knows_athletics_4|knows_riding_4|knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_horse_archery_3,man_face_older_1, man_face_older_2],
   
  # Used for banner usage storage
  ["noble_end","noble_end","noble_end",0,no_scene,reserved,fac_commoners,
   [],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
## recruit noble end    ##


#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic,itm_fur_coat, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_arena_tunic_white, itm_leather_apron, itm_shirt, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sarranid_common_dress, itm_sarranid_common_dress_b,itm_woolen_hose, itm_sarranid_felt_head_cloth, itm_sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  
#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_leather_vest, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2],
 ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_robe, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_nomad_armor,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END

  ["Xerina","Xerina","Xerina",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_leather_jerkin,itm_mail_chausses],def_attrib|str_15|agi_15|level(39),wp(240),knows_power_strike_4|knows_ironflesh_4|knows_riding_5|knows_power_draw_3|knows_athletics_5|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton","Dranton","Dranton",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_leather_vest,itm_splinted_greaves],def_attrib|str_15|agi_14|level(42),wp(250),knows_power_strike_5|knows_ironflesh_5|knows_riding_3|knows_power_draw_3|knows_athletics_2|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus","Kradus","Kradus",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_padded_leather,itm_iron_greaves],def_attrib|str_15|agi_14|level(43),wp(220),knows_power_strike_5|knows_ironflesh_5|knows_riding_3|knows_power_draw_3|knows_athletics_3|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],

#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_nomad_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_red_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership, 
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade, 
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],
			   
  ["tavern_weaponsmith_1","Smith","Smith",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_weaponsmith_2","Smith","Smith",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_coarse_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],
			   
  ["tavern_armorsmith_1","Smith","Smith",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_armorsmith_2","Smith","Smith",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_leather_jacket, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_nomad_robe, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_fur_coat, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_short_tunic, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra
  
#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  ["npc1","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_khergit_armor,itm_nomad_boots,itm_knife],
   str_8|agi_7|int_12|cha_7|level(3),wpex(50,60,60,55,40,55),
   knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
   [itm_linen_tunic,itm_wrapping_boots,itm_club],
   str_7|agi_7|int_11|cha_6|level(1),wpex(40,40,40,20,35,30),
   knows_merchant_npc|knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_dress,itm_woolen_hose,itm_knife],
   str_6|agi_9|int_11|cha_6|level(1),wpex(15,10,15,20,20,15),
   knows_merchant_npc|knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_archers_vest,itm_sarranid_boots_b,itm_arabian_sword_a],
   str_10|agi_9|int_13|cha_10|level(10),wpex(110,110,100,90,90,105),
   knows_warrior_npc|knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_3,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_nomad_vest,itm_nomad_boots,itm_sword_khergit_1],
   str_9|agi_9|int_12|cha_7|level(5),wpex(85,70,80,90,70,85),
   knows_warrior_npc|knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_tabard,itm_ankle_boots,itm_sword_medieval_a],
   str_10|agi_12|int_10|cha_5|level(6),wpex(105,105,100,85,85,80),
   knows_warrior_npc|knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_replacement_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_leather_jerkin,itm_hide_boots,itm_hunting_bow,itm_arrows_b,itm_quarter_staff],
   str_8|agi_9|int_10|cha_6|level(2),wpex(65,70,70,80,60,65),
   knows_tracker_npc|knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_tribal_warrior_outfit,itm_nomad_boots, itm_sword_viking_1],
   str_9|agi_10|int_9|cha_10|level(7),wpex(90,90,90,70,65,80),
   knows_warrior_npc|knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_tabard,itm_nomad_boots,itm_sword_medieval_b_small],
   str_11|agi_8|int_7|cha_8|level(2),wpex(100,90,100,80,80,85),
   knows_warrior_npc|knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_2|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_padded_leather,itm_leather_boots,itm_crossbow,itm_bolts,itm_pickaxe],
   str_12|agi_8|int_9|cha_11|level(9),wpex(100,90,85,80,105,85),
   knows_warrior_npc|knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_replacement_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_coarse_tunic,itm_falchion,itm_wrapping_boots],
   str_8|agi_11|int_10|cha_10|level(8),wpex(65,55,70,60,60,65),
   knows_merchant_npc|knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_pilgrim_disguise,itm_nomad_boots,itm_staff],
   str_8|agi_7|int_13|cha_7|level(4),wpex(25,15,30,15,20,20),
   knows_merchant_npc|knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13","Nizar","Nizar",tf_mounted|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_nomad_robe,itm_nomad_boots,itm_light_lance,itm_courser],
   str_9|agi_7|int_12|cha_8|level(5),wpex(75,60,80,60,50,70),
   knows_warrior_npc|knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_leadership_2,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_nobleman_outfit,itm_leather_boots,itm_leather_gloves,itm_sword_medieval_b],
   str_9|agi_8|int_11|cha_8|level(5),wpex(100,100,95,85,85,80),
   knows_warrior_npc|knows_trainer_replacement_4|knows_weapon_master_3|knows_leadership_4|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_rich_outfit,itm_nomad_boots,itm_sword_medieval_b_small],
   str_9|agi_9|int_12|cha_8|level(7),wpex(80,70,75,60,65,60),
   knows_warrior_npc|knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_peasant_dress,itm_nomad_boots,itm_dagger,itm_throwing_knives,itm_throwing_knives],
   str_7|agi_11|int_8|cha_7|level(2),wpex(75,70,70,65,65,85),
   knows_tracker_npc|knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],
  ["npc17","Sverre","Sverre",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_blue_tunic,itm_hide_boots,itm_one_handed_battle_axe_a,itm_tab_shield_round_b],
   str_12|agi_8|int_10|cha_7|level(6),wpex(100,100,90,80,80,95),
   knows_warrior_npc|knows_power_throw_1|knows_power_strike_2|knows_athletics_2|knows_leadership_2|knows_weapon_master_3|knows_trainer_replacement_1,
   0x000000000710134718e569caf46f38e200000000001f36ec0000000000000000],
  ["npc18","Seis","Seis",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_sarranid_cloth_robe,itm_sarranid_boots_b,itm_falchion],
   str_8|agi_9|int_11|cha_7|level(4),wpex(40,30,40,25,25,35),
   knows_merchant_npc|knows_surgery_3|knows_wound_treatment_3|knows_first_aid_2|knows_leadership_1,
   0x000000003f08610048ab4d57646eb75b00000000001f49730000000000000000],
  ["npc19","Aethrod","Aethrod",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_linen_tunic,itm_hide_boots,itm_axe],
   str_12|agi_8|int_7|cha_7|level(3),wpex(70,80,75,60,60,75),
   knows_warrior_npc|knows_ironflesh_1|knows_weapon_master_1|knows_athletics_2|knows_power_strike_3|knows_leadership_1,
   0x000000003f0411086b1ea5b2db7228ad00000000001cc9130000000000000000],
  ["npc20","Saorie","Saorie",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_leather_vest,itm_nomad_boots,itm_hatchet],
   str_7|agi_11|int_8|cha_8|level(3),wpex(80,70,75,65,60,65),
   knows_warrior_npc|knows_weapon_master_2|knows_athletics_2|knows_power_strike_1|knows_leadership_2,
   0x000000019204100339266858dca53b3300000000001eba940000000000000000],
  
  ## 35attrib lvl 4
  ## 51attrib lvl 20
  ## 20skill   lvl 4
  ## 36skill  lvl 20
  ["npc21","Ilya","Ilya",tf_mounted|tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_haubergeon,itm_leather_boots,itm_leather_gloves,itm_mail_coif,
    itm_light_crossbow,itm_steel_bolts,itm_sword_medieval_c,itm_tab_shield_heater_cav_a,itm_hunter],
   str_17|agi_13|int_12|cha_9|level(20),wpex(110,90,95,110,125,95),
   knows_weapon_master_4|knows_riding_5|knows_ironflesh_5 |knows_power_strike_4|knows_athletics_4|knows_shield_3|knows_tactics_4|knows_leadership_3 |knows_trainer_replacement_2|knows_horse_archery_2|knows_power_draw_3,
   0x00000001bf0400041b0a92492cae48b100000000001e475a0000000000000000],
  ["npc22","Ysellian","Ysellian",tf_mounted|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_mail_hauberk,itm_leather_boots,itm_leather_gloves,itm_vaegir_lamellar_helmet,
    itm_strong_bow,itm_bodkin_arrows,itm_bodkin_arrows,itm_scimitar,itm_courser],
   str_15|agi_18|int_9|cha_9|level(20),wpex(90,75,70,130,75,85),
   knows_weapon_master_4|knows_riding_6|knows_ironflesh_2 |knows_power_strike_3|knows_athletics_4|knows_shield_2|knows_tactics_3|knows_leadership_3 |knows_trainer_replacement_3|knows_horse_archery_4|knows_power_draw_5,
   0x00000001b00c11c9461c76470b755aea00000000001f0ae10000000000000000],
  ["npc23","Khutza","Khutza",tf_mounted|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_lamellar_vest_khergit,itm_leather_boots,itm_leather_gloves,itm_khergit_war_helmet,
    itm_lance,itm_sword_khergit_3,itm_javelin,itm_tab_shield_small_round_c,itm_hunter],
   str_12|agi_18|int_12|cha_9|level(20),wpex(100,85,140,80,70,95),
   knows_weapon_master_4|knows_riding_6|knows_ironflesh_3 |knows_power_strike_4|knows_athletics_4|knows_shield_3|knows_tactics_4|knows_leadership_3 |knows_trainer_replacement_4|knows_horse_archery_2|knows_power_throw_2,
   0x00000008651043004adcd158dc37672a00000000001d399d0000000000000000],
  ["npc24","Uhtred","Uhtred",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_mail_shirt,itm_mail_chausses,itm_mail_mittens,itm_nordic_fighter_helmet,
    itm_two_handed_battle_axe_2,itm_tab_shield_round_d,itm_throwing_axes,itm_throwing_axes],
   str_18|agi_18|int_9|cha_6|level(20),wpex(110,130,115,70,65,90),
   knows_weapon_master_3|knows_riding_3|knows_ironflesh_6 |knows_power_strike_6|knows_athletics_6|knows_shield_4|knows_tactics_3|knows_leadership_2 |knows_trainer_replacement_3|knows_power_throw_3,
   0x0000000e4904138625578a372366398400000000001f4d5b0000000000000000],
  ["npc25","Ireth","Ireth",tf_mounted|tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_byrnie,itm_leather_boots,itm_leather_gloves,itm_kettle_hat,
    itm_light_lance,itm_morningstar,itm_courser],
   str_15|agi_15|int_12|cha_9|level(20),wpex(100,105,115,65,75,70),
   knows_weapon_master_5|knows_riding_5|knows_ironflesh_4 |knows_power_strike_5|knows_athletics_5|knows_shield_4|knows_tactics_4|knows_leadership_3 |knows_trainer_replacement_4,
   0x00000001aa10200657214a22ee91670a00000000001d36e30000000000000000],
  ["npc26","Merek","Merek",tf_mounted|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_sarranid_cavalry_robe,itm_sarranid_boots_c,itm_leather_gloves,itm_sarranid_helmet1,
    itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c,itm_arabian_horse_b,itm_javelin,itm_javelin],
   str_11|agi_22|int_9|cha_9|level(20),wpex(125,110,115,65,65,105),
   knows_weapon_master_3|knows_riding_7|knows_ironflesh_2 |knows_power_strike_3|knows_athletics_6|knows_shield_4|knows_tactics_3|knows_leadership_3 |knows_trainer_replacement_3|knows_horse_archery_2|knows_power_throw_3,
   0x00000001831061062b1da5589390ace200000000001cb5b20000000000000000],
  ## New Companions
#NPC system changes end


#governers olgrel rasevas                                                                         Horse                    Bodywear                 Footwear_in                     Footwear_out                       Armor                                Headwear                                              Weapon                                                 Shield                 
  ["kingdom_1_lord",  "King Harlaus",  "Harlaus",  tf_mounted|tf_hero, 0,reserved,  fac_kingdom_1,[itm_charger,            itm_rich_outfit,         itm_blue_hose,                  itm_iron_greaves,                  itm_plate_armor,                     itm_great_helmet,           itm_gauntlets,            itm_sword_two_handed_a,                                itm_tab_shield_heater_cav_b],    king_attrib,wp(220),king_skills, 0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000, swadian_face_older_2],
  ["kingdom_2_lord",  "Kiralyi Yaroglek",  "Yaroglek",  tf_mounted|tf_hero, 0,reserved,  fac_kingdom_2,[itm_warhorse_steppe,itm_courtly_outfit,     itm_leather_boots,              itm_mail_boots,                    itm_heraldic_mail_with_surcoat,      itm_vaegir_mask,            itm_gauntlets,            itm_great_bardiche,                                    itm_tab_shield_kite_cav_b],      king_attrib,wp(220),king_skills, 0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000, vaegir_face_old_2],
  ["kingdom_3_lord",  "Sanjar Khan",  "Sanjar",  tf_mounted|tf_hero, 0,reserved,  fac_kingdom_3,[  itm_warhorse_steppe,    itm_nomad_robe,          itm_leather_boots,              itm_khergit_guard_boots,           itm_khergit_elite_armor,             itm_khergit_guard_helmet,   itm_lamellar_gauntlets,   itm_sword_khergit_4,itm_khergit_bow,itm_khergit_arrows,itm_tab_shield_small_round_c],   king_attrib,wp(220),king_skills, 0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_old_2],
  ["kingdom_4_lord",  "King Ragnar",  "Ragnar",  tf_mounted|tf_hero, 0,reserved,  fac_kingdom_4,[  itm_warhorse,           itm_nobleman_outfit,     itm_leather_boots,              itm_splinted_leather_greaves,      itm_cuir_bouilli,                    itm_nordic_warlord_helmet,  itm_gauntlets,            itm_great_axe,                                         itm_tab_shield_round_e],         king_attrib,wp(220),king_skills, 0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000, nord_face_older_2],
  ["kingdom_5_lord",  "Governor Graveth",  "Graveth",  tf_mounted|tf_hero, 0,reserved,  fac_kingdom_5,[itm_warhorse_b,     itm_tabard,              itm_leather_boots,              itm_mail_boots,                    itm_heraldic_mail_with_tabard,       itm_full_helm,              itm_gauntlets,            itm_two_handed_cleaver,itm_sniper_crossbow,itm_steel_bolts,itm_tab_shield_pavise_d],    king_attrib,wp(220),king_skills, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],
  ["kingdom_6_lord",  "Sultan Hakim",  "Hakim",  tf_mounted|tf_hero, 0,reserved,  fac_kingdom_6,[  itm_warhorse_sarranid,                                                           itm_sarranid_boots_d,              itm_sarranid_elite_armor,            itm_sarranid_veiled_helmet, itm_scale_gauntlets,      itm_sarranid_two_handed_mace_1,itm_jarid,              itm_tab_shield_small_round_c],   king_attrib,wp(220),king_skills, 0x0000000a4b103354189c71d6d386e8ac00000000001e24eb0000000000000000, sarranid_face_old_2],
  ["kingdom_9_lord",  "Yun Khan",  "Yun",  tf_mounted|tf_hero, 0,reserved,  fac_kingdom_9,[  itm_hunter,                   itm_nomad_robe,          itm_leather_boots,                                                 itm_lamellar_vest_khergit,           itm_khergit_war_helmet,     itm_leather_gloves,       itm_sword_khergit_3,itm_khergit_bow,itm_khergit_arrows,itm_tab_shield_small_round_c],   lesser_king_attrib,wp(200),lesser_king_skills, 0x0000000aff0811cb45a594a451b14b2200000000001c48a20000000000000000, khergit_face_old_2],
  ["kingdom_10_lord", "Prince Richter",  "Richter",  tf_mounted|tf_hero, 0,reserved,  fac_kingdom_10,[itm_warhorse,        itm_rich_outfit,         itm_leather_boots,              itm_mail_boots,                    itm_banded_armor,                    itm_kettle_hat,             itm_mail_mittens,         itm_sword_medieval_b,itm_lance,                        itm_tab_shield_heater_cav_b],    lesser_king_attrib,wp(200),lesser_king_skills, 0x0000000d9910434936b5826d2b2c969c00000000001d47140000000000000000, swadian_face_older_2],
  ["kingdom_11_lord", "Governor Guysa",  "Guysa",  tf_mounted|tf_hero, 0,reserved,  fac_kingdom_11,[itm_warhorse_b,        itm_tabard,              itm_leather_boots,              itm_mail_boots,                    itm_surcoat_over_mail,               itm_helmet_with_neckguard,  itm_mail_mittens,         itm_shortened_military_scythe,itm_lance,               itm_tab_shield_heater_cav_b],    lesser_king_attrib,wp(200),lesser_king_skills, 0x000000049c0c30d138ab77da5e499cda00000000001e35140000000000000000, rhodok_face_old_2],


#    Imbrea   Belinda Ruby Qaelmas Rose    Willow
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina
# Dunga        Agatha     Dibus Crahask

#                                                                                       Horse                  Bodywear                 Armor                                  Footwear_in                 Footwear_out                         Headwear                                              Weapon                                                 Shield
  #Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
  #Older knights with higher skills moved to top
  ["knight_1_1", "Lord Klargus", "Klargus", tf_hero, 0, reserved,  fac_kingdom_1, [     itm_warhorse_b,        itm_courtly_outfit,      itm_heraldic_mail_with_surcoat,        itm_nomad_boots,            itm_mail_boots,                      itm_great_helmet,           itm_gauntlets,            itm_sword_medieval_c,itm_heavy_lance,                  itm_tab_shield_heater_cav_b],       knight_attrib_5,wp(240),knight_skills_5, 0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000, swadian_face_older_2],
  ["knight_1_2", "Duke Delinard", "Delinard", tf_hero, 0, reserved,  fac_kingdom_1, [   itm_warhorse_b,        itm_red_gambeson,        itm_heraldic_mail_with_surcoat,        itm_nomad_boots,            itm_iron_greaves,                    itm_guard_helmet,           itm_gauntlets,            itm_bastard_sword_b,                                   itm_tab_shield_heater_cav_b],       knight_attrib_5,wp(240),knight_skills_5, 0x0000000c0f0c320627627238dcd6599400000000001c573d0000000000000000, swadian_face_young_2],
  ["knight_1_3", "Duke Haringoth", "Haringoth", tf_hero, 0, reserved,  fac_kingdom_1, [ itm_warhorse,          itm_nobleman_outfit,     itm_coat_of_plates_red,                itm_leather_boots,          itm_iron_greaves,                    itm_winged_great_helmet,    itm_gauntlets,            itm_morningstar,                                       itm_tab_shield_heater_d],           knight_attrib_5,wp(240),knight_skills_5, 0x0000000cb700210214ce89db276aa2f400000000001d36730000000000000000, swadian_face_young_2],
  ["knight_1_4", "Lord Clais", "Clais", tf_hero, 0, reserved,  fac_kingdom_1, [         itm_warhorse,          itm_short_tunic,         itm_heraldic_mail_with_surcoat,        itm_leather_boots,          itm_iron_greaves,                    itm_great_helmet,           itm_gauntlets,            itm_sword_two_handed_a,                                itm_tab_shield_heater_d],           knight_attrib_5,wp(240),knight_skills_5, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
  ["knight_1_5", "Lord Deglan", "Deglan", tf_hero, 0, reserved,  fac_kingdom_1, [       itm_hunter,            itm_rich_outfit,         itm_brigandine_red,                    itm_woolen_hose,            itm_mail_boots,                      itm_guard_helmet,           itm_mail_mittens,         itm_sword_medieval_c,itm_lance,                        itm_tab_shield_heater_cav_b],       knight_attrib_4,wp(210),knight_skills_4, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
  ["knight_1_6", "Lord Tredian", "Tredian", tf_hero, 0, reserved,  fac_kingdom_1, [     itm_hunter,            itm_tabard,              itm_heraldic_mail_with_tabard,         itm_leather_boots,          itm_mail_boots,                      itm_great_helmet,           itm_mail_mittens,         itm_sword_two_handed_a,                                itm_tab_shield_heater_cav_b],       knight_attrib_4,wp(210),knight_skills_4, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],
  ["knight_1_7", "Lord Grainwad", "Grainwad", tf_hero, 0, reserved,  fac_kingdom_1, [   itm_hunter,            itm_tabard,              itm_heraldic_mail_with_tabard,         itm_leather_boots,          itm_mail_boots,                      itm_flat_topped_helmet,     itm_mail_mittens,         itm_bastard_sword_b,                                   itm_tab_shield_heater_cav_b],       knight_attrib_4,wp(210),knight_skills_4, 0x0000000c1e001500589dae4094aa291c00000000001e37a80000000000000000, swadian_face_young_2],
  ["knight_1_8", "Lord Ryis", "Ryis", tf_hero, 0, reserved,  fac_kingdom_1, [           itm_hunter,            itm_nobleman_outfit,     itm_coat_of_plates_red,                itm_leather_boots,          itm_mail_boots,                      itm_flat_topped_helmet,     itm_gauntlets,            itm_sword_two_handed_a,itm_lance,                      itm_tab_shield_heater_d],           knight_attrib_4,wp(210),knight_skills_4, 0x0000000c330855054aa9aa431a48d74600000000001ed5240000000000000000, swadian_face_older_2],

#Swadian younger knights  
  ["knight_1_9", "Count Plais", "Plais", tf_hero, 0, reserved,  fac_kingdom_1, [        itm_pack_horse,        itm_gambeson,            itm_brigandine_red,                    itm_blue_hose,              itm_mail_boots,                      itm_helmet_with_neckguard,  itm_mail_mittens,         itm_fighting_pick,itm_lance,                           itm_tab_shield_heater_cav_a],       knight_attrib_3,wp(180),knight_skills_3, 0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000, swadian_face_old_2],
  ["knight_1_10", "Count Mirchaud", "Mirchaud", tf_hero, 0, reserved,  fac_kingdom_1, [ itm_courser,           itm_blue_gambeson,       itm_haubergeon,                        itm_woolen_hose,            itm_mail_chausses,                   itm_flat_topped_helmet,     itm_mail_mittens,         itm_sword_two_handed_b,                                itm_tab_shield_heater_c],           knight_attrib_3,wp(180),knight_skills_3, 0x0000000c0610351048e325361d7236cd00000000001d532a0000000000000000, swadian_face_older_2],
  ["knight_1_11", "Count Stamar", "Stamar", tf_hero, 0, reserved,  fac_kingdom_1, [     itm_courser,           itm_red_gambeson,        itm_heraldic_mail_with_surcoat,        itm_nomad_boots,            itm_mail_chausses,                   itm_helmet_with_neckguard,  itm_leather_gloves,       itm_bastard_sword_a,                                   itm_tab_shield_heater_c],           knight_attrib_3,wp(180),knight_skills_3, 0x0000000c03104490280a8cb2a24196ab00000000001eb4dc0000000000000000, swadian_face_older_2],
  ["knight_1_12", "Count Meltor", "Meltor", tf_hero, 0, reserved,  fac_kingdom_1, [     itm_pack_horse,        itm_rich_outfit,         itm_heraldic_mail_with_tabard,         itm_nomad_boots,            itm_mail_chausses,                   itm_helmet_with_neckguard,  itm_leather_gloves,       itm_fighting_pick,itm_lance,                           itm_tab_shield_heater_cav_a],       knight_attrib_3,wp(180),knight_skills_3, 0x0000000c2a0805442b2c6cc98c8dbaac00000000001d389b0000000000000000, swadian_face_older_2],
  ["knight_1_13", "Viscount Beranz", "Beranz", tf_hero, 0, reserved,  fac_kingdom_1, [  itm_pack_horse,        itm_ragged_outfit,       itm_heraldic_mail_with_surcoat,        itm_nomad_boots,            itm_mail_chausses,                   itm_kettle_hat,             itm_leather_gloves,       itm_sword_medieval_c,itm_sword_two_handed_a,           itm_tab_shield_heater_c],           knight_attrib_2,wp(150),knight_skills_2, 0x0000000c380c30c2392a8e5322a5392c00000000001e5c620000000000000000, swadian_face_older_2],
  ["knight_1_14", "Viscount Rafard", "Rafard", tf_hero, 0, reserved,  fac_kingdom_1, [  itm_saddle_horse,      itm_short_tunic,         itm_heraldic_mail_with_tunic_b,        itm_leather_boots,          itm_mail_chausses,                   itm_kettle_hat,             itm_leather_gloves,       itm_bastard_sword_a,itm_lance,                         itm_tab_shield_heater_cav_a],       knight_attrib_2,wp(150),knight_skills_2, 0x0000000c3f10000532d45203954e192200000000001e47630000000000000000, swadian_face_older_2],
  ["knight_1_15", "Viscount Regas", "Regas", tf_hero, 0, reserved,  fac_kingdom_1, [    itm_saddle_horse,      itm_rich_outfit,         itm_haubergeon,                        itm_woolen_hose,            itm_mail_chausses,                   itm_kettle_hat,             itm_mail_mittens,         itm_sword_medieval_b,itm_light_lance,                  itm_tab_shield_heater_c],           knight_attrib_2,wp(150),knight_skills_2, 0x0000000c5c0840034895654c9b660c5d00000000001e34530000000000000000, swadian_face_young_2],
  ["knight_1_16", "Viscount Devlian", "Devlian", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_courtly_outfit,      itm_heraldic_mail_with_tunic,          itm_nomad_boots,            itm_mail_chausses,                   itm_helmet_with_neckguard,  itm_leather_gloves,       itm_sword_medieval_b,                                  itm_tab_shield_heater_b],           knight_attrib_2,wp(150),knight_skills_2, 0x000000095108144657a1ba3ad456e8cb00000000001e325a0000000000000000, swadian_face_young_2],
  ["knight_1_17", "Baron Rafarch", "Rafarch", tf_hero, 0, reserved,  fac_kingdom_1, [   itm_saddle_horse,      itm_gambeson,            itm_heraldic_mail_with_tunic_b,        itm_leather_boots,          itm_leather_boots,                   itm_mail_coif,              itm_leather_gloves,       itm_fighting_pick,itm_light_lance,                     itm_tab_shield_heater_b],           knight_attrib_1,wp(120),knight_skills_1, 0x0000000c010c42c14d9d6918bdb336e200000000001dd6a30000000000000000, swadian_face_young_2],
  ["knight_1_18", "Baron Rochabarth", "Rochabarth", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,        itm_blue_gambeson,       itm_haubergeon,                        itm_leather_boots,          itm_leather_boots,                   itm_mail_coif,              itm_leather_gloves,       itm_sword_two_handed_b,                                itm_tab_shield_heater_b],           knight_attrib_1,wp(120),knight_skills_1, 0x0000000c150045c6365d8565932a8d6400000000001ec6940000000000000000, swadian_face_young_2],
  ["knight_1_19", "Baron Despin", "Despin", tf_hero, 0, reserved,  fac_kingdom_1, [     itm_saddle_horse,      itm_rich_outfit,         itm_heraldic_mail_with_tunic,          itm_leather_boots,          itm_leather_boots,                   itm_footman_helmet,         itm_leather_gloves,       itm_sword_two_handed_b,                                itm_tab_shield_heater_b],           knight_attrib_1,wp(120),knight_skills_1, 0x00000008200012033d9b6d4a92ada53500000000001cc1180000000000000000, swadian_face_young_2],
  ["knight_1_20", "Baron Montewar", "Montewar", tf_hero, 0, reserved,  fac_kingdom_1, [ itm_saddle_horse,      itm_ragged_outfit,       itm_heraldic_mail_with_tunic,          itm_leather_boots,          itm_leather_boots,                   itm_footman_helmet,         itm_leather_gloves,       itm_sword_medieval_a,                                  itm_tab_shield_heater_b],           knight_attrib_1,wp(120),knight_skills_1, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],
  #new lords
  ["knight_1_21", "Juta", "Juta", tf_hero, 0, reserved,  fac_kingdom_1, [],       knight_attrib_0,wp(90),knight_skills_0, 0x000000019610145156e1ca6b857a96a5000000000000a4db0000000000000000, swadian_face_older_2],
  ["knight_1_22", "Euvino", "Euvino", tf_hero, 0, reserved,  fac_kingdom_1, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000001a31022904865366616f6b51a00000000000cb6e10000000000000000, swadian_face_young_2],
  ["knight_1_23", "Tearney", "Tearney", tf_hero, 0, reserved,  fac_kingdom_1, [],           knight_attrib_0,wp(90),knight_skills_0, 0x0000000b3f101213468d55a51a891c6b00000000001d54d20000000000000000, swadian_face_young_2],
  ["knight_1_24", "Pechnack", "Pechnack", tf_hero, 0, reserved,  fac_kingdom_1, [],           knight_attrib_0,wp(90),knight_skills_0, 0x000000047f1005804b6b661faa8897a300000000001e38ca0000000000000000, swadian_face_older_2],
  ["knight_1_25", "Roland", "Roland", tf_hero, 0, reserved,  fac_kingdom_1, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000002ff1013895d5eae1b3788ca9100000000001e445a0000000000000000, swadian_face_older_2],
  ["knight_1_26", "Baldur", "Baldur", tf_hero, 0, reserved,  fac_kingdom_1, [],       knight_attrib_0,wp(90),knight_skills_0, 0x0000000c3f0011042d64aa46d48e25a600000000001f3b220000000000000000, swadian_face_older_2],
  ["knight_1_27", "Mondery", "Mondery", tf_hero, 0, reserved,  fac_kingdom_1, [],       knight_attrib_0,wp(90),knight_skills_0, 0x000000039704215356dc6096f569c25200000000001e46ab0000000000000000, swadian_face_young_2],
  ["knight_1_28", "Copart", "Copart", tf_hero, 0, reserved,  fac_kingdom_1, [],           knight_attrib_0,wp(90),knight_skills_0, 0x000000063c0014d15689923adb6e535d00000000001e18d40000000000000000, swadian_face_older_2],
  ["knight_1_29", "Delan", "Delan", tf_hero, 0, reserved,  fac_kingdom_1, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000009c00831944aa58928536f252100000000001f368a0000000000000000, swadian_face_old_2],
  ["knight_1_30", "Sally", "Sally", tf_hero, 0, reserved,  fac_kingdom_1, [],           knight_attrib_0,wp(90),knight_skills_0, 0x00000002cf08219148ac325cac854aa300000000001e392a0000000000000000, swadian_face_older_2],
  ["knight_1_31", "Galimade", "Galimade", tf_hero, 0, reserved,  fac_kingdom_1, [],           knight_attrib_0,wp(90),knight_skills_0, 0x00000001fa08119064d570cacc253d1b00000000001da6d40000000000000000, swadian_face_older_2],
  ["knight_1_32", "Fouckard", "Fouckard", tf_hero, 0, reserved,  fac_kingdom_1, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000006b91004c62ce4d948a89754e400000000001d92e30000000000000000, swadian_face_older_2],
  ["knight_1_33", "Turias", "Turias", tf_hero, 0, reserved,  fac_kingdom_1, [],           knight_attrib_0,wp(90),knight_skills_0, 0x00000006a10415c452a451372c6868f400000000001dc0a40000000000000000, swadian_face_young_2],
  ["knight_1_34", "Helmut", "Helmut", tf_hero, 0, reserved,  fac_kingdom_1, [],           knight_attrib_0,wp(90),knight_skills_0, 0x00000009360c04113b144d25196e2b0e00000000001dc4dc0000000000000000, swadian_face_young_2],
  ["knight_1_35", "Verrier", "Verrier", tf_hero, 0, reserved,  fac_kingdom_1, [],           knight_attrib_0,wp(90),knight_skills_0, 0x000000047f0803c5265c6ce8dc5233a600000000001de59d0000000000000000, swadian_face_young_2],
  # ["knight_1_38", "Downward", "Downward", tf_hero, 0, reserved,  fac_kingdom_1, [],           knight_attrib_0,wp(90),knight_skills_0, 0x00000006bd10220416f2d3472b89571e00000000001cb71c0000000000000000, swadian_face_young_2],


  
#  ["knight_1_21", "Lord Swadian 21", "knight_1_7", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_ragged_outfit,      itm_heraldic_mail_with_surcoat,           itm_nomad_boots,            itm_splinted_greaves,                itm_great_helmet, itm_gauntlets,           itm_sword_medieval_c,   itm_sword_two_handed_a,   itm_tab_shield_heater_cav_a],   knight_attrib_2,wp(150),knight_skills_2, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],
 # ["knight_1_22", "Lord Swadian 22", "knight_1_8", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_short_tunic,       itm_heraldic_mail_with_surcoat,           itm_leather_boots,          itm_mail_chausses,                   itm_winged_great_helmet, itm_gauntlets,       itm_bastard_sword_a,  itm_sword_two_handed_a,  itm_tab_shield_heater_d],    knight_attrib_3,wp(180),knight_skills_3|knows_trainer_replacement_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
#  ["knight_1_23", "Lord Swadian 23", "knight_1_9", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_rich_outfit,        itm_mail_hauberk,                   itm_woolen_hose,            itm_mail_chausses,                   itm_guard_helmet, itm_gauntlets,         itm_sword_medieval_c,    itm_tab_shield_heater_d],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_replacement_6, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
#  ["knight_1_24", "Lord Swadian 24", "knight_1_0", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_tabard,      itm_heraldic_mail_with_surcoat,               itm_leather_boots,          itm_mail_boots,                      itm_winged_great_helmet, itm_gauntlets, itm_bastard_sword_b, itm_sword_two_handed_b,  itm_tab_shield_heater_cav_b], knight_attrib_5,wp(240),knight_skills_5|knows_trainer_replacement_5, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],

  
  ## Vaegir
  ["knight_2_1", "Baro Vuldrat", "Vuldrat", tf_hero, 0, reserved,  fac_kingdom_2, [     itm_saddle_horse,      itm_tribal_warrior_outfit,                                      itm_nomad_boots,                                                 itm_vaegir_spiked_helmet,   itm_leather_gloves,       itm_sword_viking_1,itm_javelin,                        itm_tab_shield_kite_b],             knight_attrib_1,wp(120),knight_skills_1, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
  ["knight_2_2", "Vargrof Naldera", "Naldera", tf_hero, 0, reserved,  fac_kingdom_2, [  itm_saddle_horse,      itm_rich_outfit,         itm_lamellar_vest,                     itm_woolen_hose,            itm_leather_boots,                   itm_vaegir_spiked_helmet,   itm_leather_gloves,       itm_sword_viking_2,itm_light_lance,                    itm_tab_shield_kite_c],             knight_attrib_2,wp(150),knight_skills_2, 0x0000000c2a0015d249b68b46a98e176400000000001d95a40000000000000000, vaegir_face_old_2],
  ["knight_2_3", "Grof Meriga", "Meriga", tf_hero, 0, reserved,  fac_kingdom_2, [       itm_pack_horse,        itm_short_tunic,         itm_mail_hauberk,                      itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_lamellar_helmet, itm_mail_mittens,         itm_sword_khergit_2,itm_lance,                         itm_tab_shield_kite_c],             knight_attrib_3,wp(180),knight_skills_3, 0x0000000c131031c546a38a2765b4c86000000000001e58d30000000000000000, vaegir_face_older_2],
  ["knight_2_4", "Ur Khavel", "Khavel", tf_hero, 0, reserved,  fac_kingdom_2, [         itm_hunter,            itm_courtly_outfit,      itm_lamellar_vest,                     itm_leather_boots,          itm_mail_chausses,                   itm_vaegir_noble_helmet,    itm_scale_gauntlets,      itm_great_axe,                                         itm_tab_shield_kite_cav_a],         knight_attrib_4,wp(210),knight_skills_4, 0x0000000c2f0832c748f272540d8ab65900000000001d34e60000000000000000, vaegir_face_older_2],
  ["knight_2_5", "Herceg Doru", "Doru", tf_hero, 0, reserved,  fac_kingdom_2, [         itm_warhorse_steppe,   itm_rich_outfit,         itm_banded_armor,                      itm_leather_boots,          itm_mail_boots,                      itm_vaegir_war_helmet,      itm_lamellar_gauntlets,   itm_bastard_sword_b,                                   itm_tab_shield_kite_cav_b],         knight_attrib_5,wp(250),knight_skills_5, 0x0000000e310061435d76bb5f55bad9ad00000000001ed8ec0000000000000000, vaegir_face_older_2],
  ["knight_2_6", "Baro Belgaru", "Belgaru", tf_hero, 0, reserved,  fac_kingdom_2, [     itm_pack_horse,        itm_nomad_vest,          itm_studded_leather_coat,              itm_woolen_hose,            itm_leather_boots,                   itm_vaegir_spiked_helmet,   itm_leather_gloves,       itm_sword_viking_1,                                    itm_tab_shield_kite_b],             knight_attrib_1,wp(120),knight_skills_1, 0x0000000a0100421038da7157aa4e430a00000000001da8bc0000000000000000, vaegir_face_middle_2],
  ["knight_2_7", "Vargrof Ralcha", "Ralcha", tf_hero, 0, reserved,  fac_kingdom_2, [    itm_steppe_horse,      itm_leather_jacket,      itm_mail_hauberk,                      itm_leather_boots,          itm_leather_boots,                   itm_vaegir_lamellar_helmet, itm_mail_mittens,         itm_two_handed_battle_axe_2,itm_lance,                 itm_tab_shield_kite_c],             knight_attrib_2,wp(150),knight_skills_2, 0x0000000c04100153335ba9390b2d277500000000001d89120000000000000000, vaegir_face_old_2],
  ["knight_2_8", "Grof Vlan", "Vlan", tf_hero, 0, reserved,  fac_kingdom_2, [           itm_pack_horse,        itm_nomad_robe,          itm_studded_leather_coat,              itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_noble_helmet,    itm_scale_gauntlets,      itm_bardiche,                                          itm_tab_shield_kite_c],             knight_attrib_3,wp(180),knight_skills_3, 0x0000000c00046581234e8da2cdd248db00000000001f569c0000000000000000, vaegir_face_older_2],
  ["knight_2_9", "Ur Mleza", "Mleza", tf_hero, 0, reserved,  fac_kingdom_2, [           itm_hunter,            itm_rich_outfit,         itm_lamellar_armor,                    itm_leather_boots,          itm_mail_chausses,                   itm_vaegir_war_helmet,      itm_lamellar_gauntlets,   itm_great_axe,                                         itm_tab_shield_kite_d],             knight_attrib_4,wp(210),knight_skills_4, 0x0000000c160451d2136469c4d9b159ad00000000001e28f10000000000000000, vaegir_face_older_2],
  ["knight_2_10", "Herceg Nelag", "Nelag", tf_hero, 0, reserved,  fac_kingdom_2, [      itm_warhorse,          itm_fur_coat,            itm_vaegir_elite_armor,                itm_woolen_hose,            itm_mail_boots,                      itm_vaegir_war_helmet,      itm_lamellar_gauntlets,   itm_fighting_axe,itm_jarid,                            itm_tab_shield_kite_cav_b],         knight_attrib_5,wp(250),knight_skills_5, 0x0000000f7c00520e66b76edd5cd5eb6e00000000001f691e0000000000000000, vaegir_face_older_2],
  ["knight_2_11", "Baro Crahask", "Crahask", tf_hero, 0, reserved,  fac_kingdom_2, [    itm_steppe_horse,      itm_leather_jacket,      itm_studded_leather_coat,              itm_nomad_boots,                                                 itm_vaegir_spiked_helmet,   itm_leather_gloves,       itm_sword_viking_1,itm_light_lance,                    itm_tab_shield_kite_b],             knight_attrib_1,wp(120),knight_skills_1, 0x0000000c1d0821d236acd6991b74d69d00000000001e476c0000000000000000, vaegir_face_middle_2],
  ["knight_2_12", "Vargrof Bracha", "Bracha", tf_hero, 0, reserved,  fac_kingdom_2, [   itm_steppe_horse,      itm_rich_outfit,         itm_studded_leather_coat,              itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_lamellar_helmet, itm_mail_mittens,         itm_bardiche,                                          itm_tab_shield_kite_c],             knight_attrib_2,wp(150),knight_skills_2, 0x0000000c0f04024b2509d5d53944c6a300000000001d5b320000000000000000, vaegir_face_old_2],
  ["knight_2_13", "Ur Druli", "Druli", tf_hero, 0, reserved,  fac_kingdom_2, [          itm_hunter,            itm_short_tunic,         itm_mail_hauberk,                      itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_noble_helmet,    itm_scale_gauntlets,      itm_great_bardiche,                                    itm_tab_shield_kite_cav_a],         knight_attrib_3,wp(180),knight_skills_3, 0x0000000c680432d3392230cb926d56ca00000000001da69b0000000000000000, vaegir_face_older_2],
  ["knight_2_14", "Ur Marmun", "Marmun", tf_hero, 0, reserved,  fac_kingdom_2, [        itm_hunter,            itm_courtly_outfit,      itm_lamellar_vest,                     itm_leather_boots,          itm_leather_boots,                   itm_vaegir_noble_helmet,    itm_scale_gauntlets,      itm_sword_khergit_3,itm_jarid,                         itm_tab_shield_kite_cav_a],         knight_attrib_4,wp(210),knight_skills_4, 0x0000000c27046000471bd2e93375b52c00000000001dd5220000000000000000, vaegir_face_older_2],
  ["knight_2_15", "Herceg Gastya", "Gastya", tf_hero, 0, reserved,  fac_kingdom_2, [    itm_warhorse_steppe,   itm_rich_outfit,         itm_banded_armor,                      itm_leather_boots,          itm_mail_boots,                      itm_vaegir_war_helmet,      itm_lamellar_gauntlets,   itm_sword_khergit_3,                                   itm_tab_shield_kite_cav_b],         knight_attrib_5,wp(250),knight_skills_5, 0x0000000de50052123b6bb36de5d6eb7400000000001dd72c0000000000000000, vaegir_face_older_2],
  ["knight_2_16", "Baro Harish", "Harish", tf_hero, 0, reserved,  fac_kingdom_2, [      itm_saddle_horse,      itm_nomad_vest,          itm_lamellar_vest,                     itm_woolen_hose,            itm_leather_boots,                   itm_vaegir_spiked_helmet,   itm_leather_gloves,       itm_two_handed_battle_axe_2,                           itm_tab_shield_kite_b],             knight_attrib_1,wp(120),knight_skills_1, 0x000000085f00000539233512e287391d00000000001db7200000000000000000, vaegir_face_middle_2],
  ["knight_2_17", "Vargrof Taisa", "Taisa", tf_hero, 0, reserved,  fac_kingdom_2, [     itm_steppe_horse,      itm_leather_jacket,      itm_mail_hauberk,                      itm_leather_boots,          itm_leather_boots,                   itm_vaegir_lamellar_helmet, itm_mail_mittens,         itm_bardiche,                                          itm_tab_shield_kite_c],             knight_attrib_2,wp(150),knight_skills_2, 0x0000000a070c4387374bd19addd2a4ab00000000001e32cc0000000000000000, vaegir_face_old_2],
  ["knight_2_18", "Grof Valishin", "Valishin", tf_hero, 0, reserved,  fac_kingdom_2, [  itm_pack_horse,        itm_nomad_robe,          itm_brigandine_red,                    itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_noble_helmet,    itm_scale_gauntlets,      itm_great_bardiche,                                    itm_tab_shield_kite_d],             knight_attrib_3,wp(180),knight_skills_3, 0x0000000b670012c23d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_older_2],
  ["knight_2_19", "Ur Rudin", "Rudin", tf_hero, 0, reserved,  fac_kingdom_2, [          itm_pack_horse,        itm_rich_outfit,         itm_lamellar_armor,                    itm_leather_boots,          itm_mail_chausses,                   itm_vaegir_noble_helmet,    itm_scale_gauntlets,      itm_sword_viking_3,itm_lance,                          itm_tab_shield_kite_d],             knight_attrib_4,wp(210),knight_skills_4, 0x0000000e070050853b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],
  ["knight_2_20", "Herceg Kumipa", "Kumipa", tf_hero, 0, reserved,  fac_kingdom_2, [    itm_warhorse,          itm_fur_coat,            itm_vaegir_elite_armor,                itm_woolen_hose,            itm_mail_boots,                      itm_vaegir_war_helmet,      itm_lamellar_gauntlets,   itm_great_bardiche,                                    itm_tab_shield_kite_cav_b],         knight_attrib_5,wp(250),knight_skills_5, 0x0000000f800021c63b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],
  #new lords
  ["knight_2_21", "Xernt", "Xernt", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x00000001a8082549311d4a44d1aab49b0000000000175ad30000000000000000, vaegir_face_middle_2],
  ["knight_2_22", "Hylgnod", "Hylgnod", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x00000001860c23c1468ea9c29bb24714000000000011b6e10000000000000000, vaegir_face_old_2],
  ["knight_2_23", "Ralchad", "Rachad", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x00000001bd100390199aa0dd2555e70b00000000000825960000000000000000, vaegir_face_older_2],
  ["knight_2_24", "Khelm", "Khelm", tf_hero, 0, reserved,  fac_kingdom_2, [],         knight_attrib_0,wp(90),knight_skills_0, 0x000000018a1024cc46e429ba9b6e22dd00000000000e329c0000000000000000, vaegir_face_older_2],
  ["knight_2_25", "Guro", "Guro", tf_hero, 0, reserved,  fac_kingdom_2, [],         knight_attrib_0,wp(90),knight_skills_0, 0x0000000bea04134a16736eeb4c8a372c00000000001e44660000000000000000, vaegir_face_older_2],
  ["knight_2_26", "Weln", "Weln", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x00000006e50c0192348d724253b1b8b300000000001d2b1a0000000000000000, vaegir_face_middle_2],
  ["knight_2_27", "Bjalfi", "Bjalfi", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x00000006f004150b5929ad18b3a9dce400000000001f47230000000000000000, vaegir_face_old_2],
  ["knight_2_28", "Vuloi", "Vuloi", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x000000073f0403c9174b4db8f38a277200000000001da4a10000000000000000, vaegir_face_older_2],
  ["knight_2_29", "Opnik", "Opnik", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x000000050d0811c8356472d9936ebfcd00000000001d5b240000000000000000, vaegir_face_older_2],
  ["knight_2_30", "Tulao", "Tulao", tf_hero, 0, reserved,  fac_kingdom_2, [],         knight_attrib_0,wp(90),knight_skills_0, 0x00000006090810c7669acd4a93aa25a100000000001cc9a40000000000000000, vaegir_face_older_2],
  ["knight_2_31", "Waldn", "Waldn", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x00000004e20015cd3b0cb5359b4524f400000000001dc69a0000000000000000, vaegir_face_middle_2],
  ["knight_2_32", "Kobyla", "Kobyla", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x0000000d2e100287178b75c7f2eea97500000000001d55430000000000000000, vaegir_face_old_2],
  ["knight_2_33", "Gottorp", "Gottorp", tf_hero, 0, reserved,  fac_kingdom_2, [],         knight_attrib_0,wp(90),knight_skills_0, 0x00000002590022813edb8d38dda63a5b00000000001edb240000000000000000, vaegir_face_older_2],
  ["knight_2_34", "Hunyadi", "Hunyadi", tf_hero, 0, reserved,  fac_kingdom_2, [],         knight_attrib_0,wp(90),knight_skills_0, 0x00000005010024c95da38eb66cb126f600000000001f28a30000000000000000, vaegir_face_older_2],
  ["knight_2_35", "Hanak", "Hanak", tf_hero, 0, reserved,  fac_kingdom_2, [],         knight_attrib_0,wp(90),knight_skills_0, 0x000000079e0402d34c1b8d475d49b4a200000000001d56d10000000000000000, vaegir_face_older_2],
  # ["knight_2_36", "Arpad", "Arpad", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x0000000c910c255239e5aab72692bcda00000000001de76d0000000000000000, vaegir_face_middle_2],
  # ["knight_2_37", "Hoknil", "Hoknil", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x0000000a3d0c030e57626c9acd8d8d7400000000001e511c0000000000000000, vaegir_face_old_2],
  # ["knight_2_38", "Shuldok", "Shuldok", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x0000000dca0421d33b6889c5136ec71400000000001cb5890000000000000000, vaegir_face_older_2],
  # ["knight_2_39", "Serw", "Serw", tf_hero, 0, reserved,  fac_kingdom_2, [],             knight_attrib_0,wp(90),knight_skills_0, 0x000000067e08110a2751ba9664d1c954000000000016b7630000000000000000, vaegir_face_older_2],
  # ["knight_2_40", "Pasch", "Pasch", tf_hero, 0, reserved,  fac_kingdom_2, [],         knight_attrib_0,wp(90),knight_skills_0, 0x00000006da0011cc448b46bb5329ab2d00000000001e9ad20000000000000000, vaegir_face_older_2],

  
  ## Khergit
  ["knight_3_1", "Sef Alagur", "Alagur", tf_hero, 0, reserved,  fac_kingdom_3, [        itm_steppe_horse,      itm_leather_vest,        itm_leather_vest,                      itm_nomad_boots,            itm_nomad_boots,                     itm_khergit_war_helmet,     itm_leather_gloves,       itm_sword_khergit_2,itm_nomad_bow,itm_arrows,          itm_tab_shield_small_round_a],      knight_attrib_1,wp(120),knight_skills_1, 0x000000043000318b54b246b7094dc39c00000000001d31270000000000000000, khergit_face_middle_2],
  ["knight_3_2", "Sef Tonju",  "Tonju", tf_hero, 0, reserved,  fac_kingdom_3, [         itm_steppe_horse,      itm_nomad_robe,          itm_nomad_robe,                        itm_nomad_boots,            itm_nomad_boots,                     itm_khergit_cavalry_helmet, itm_leather_gloves,       itm_winged_mace,itm_nomad_bow,itm_barbed_arrows,       itm_tab_shield_small_round_b],      knight_attrib_2,wp(150),knight_skills_2, 0x0000000c280461004929b334ad632aa200000000001e05120000000000000000, khergit_face_old_2],
  ["knight_3_3", "Diktator Belir",  "Belir", tf_hero, 0, reserved,  fac_kingdom_3, [    itm_hunter,            itm_nomad_robe,          itm_lamellar_vest_khergit,             itm_leather_boots,          itm_leather_boots,                   itm_khergit_guard_helmet,   itm_leather_gloves,       itm_winged_mace,itm_khergit_bow,itm_bodkin_arrows,     itm_tab_shield_small_round_b],      knight_attrib_3,wp(180),knight_skills_3, 0x0000000e880062c53b0a6e4994ae272a00000000001db4e10000000000000000, khergit_face_older_2],
  ["knight_3_4", "Diktator Asugan", "Asugan", tf_hero, 0, reserved,  fac_kingdom_3, [   itm_courser,           itm_lamellar_vest_khergit,itm_lamellar_vest_khergit,            itm_hide_boots,             itm_splinted_greaves,                itm_khergit_cavalry_helmet, itm_leather_gloves,       itm_scimitar,itm_lance,                                itm_tab_shield_small_round_b],      knight_attrib_4,wp(210),knight_skills_4, 0x0000000c23085386391b5ac72a96d95c00000000001e37230000000000000000, khergit_face_older_2],
  ["knight_3_5", "Az Khan Brula",  "Brula", tf_hero, 0, reserved,  fac_kingdom_3, [     itm_hunter,            itm_ragged_outfit,       itm_khergit_elite_armor,               itm_hide_boots,             itm_splinted_greaves,                itm_khergit_guard_helmet,   itm_lamellar_gauntlets,   itm_sword_khergit_4, itm_lance,                        itm_tab_shield_small_round_c],      knight_attrib_5,wp(250),knight_skills_5, 0x0000000efe0051ca4b377b4964b6eb6500000000001f696c0000000000000000, khergit_face_older_2],
  ["knight_3_6", "Sef Imirza", "Imirza", tf_hero, 0, reserved,  fac_kingdom_3, [        itm_saddle_horse,      itm_leather_vest,                                               itm_hide_boots,             itm_hide_boots,                      itm_khergit_cavalry_helmet, itm_leather_gloves,       itm_sword_khergit_2,itm_lance,                         itm_tab_shield_small_round_a],      knight_attrib_1,wp(120),knight_skills_1, 0x00000006f600418b54b246b7094dc31a00000000001d37270000000000000000, khergit_face_middle_2],
  ["knight_3_7", "Diktator Urumuda","Urumuda", tf_hero, 0, reserved,  fac_kingdom_3, [  itm_steppe_horse,      itm_tribal_warrior_outfit,                                      itm_leather_boots,          itm_leather_boots,                   itm_khergit_guard_helmet,   itm_leather_gloves,       itm_sword_khergit_3,                                   itm_tab_shield_small_round_b],      knight_attrib_2,wp(150),knight_skills_2, 0x0000000bdd00510a44be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_old_2],
  ["knight_3_8", "Diktator Kramuk", "Kramuk", tf_hero, 0, reserved,  fac_kingdom_3, [   itm_courser,           itm_nomad_vest,          itm_lamellar_vest_khergit,             itm_woolen_hose,            itm_splinted_greaves,                itm_khergit_cavalry_helmet, itm_leather_gloves,       itm_winged_mace,                                       itm_tab_shield_small_round_b],      knight_attrib_3,wp(180),knight_skills_3, 0x0000000abc00518b5af4ab4b9c8e596400000000001dc76d0000000000000000, khergit_face_older_2],
  ["knight_3_9", "Az Khan Chaurka","Chaurka", tf_hero, 0, reserved,  fac_kingdom_3, [   itm_hunter,            itm_nomad_robe,          itm_lamellar_armor,                    itm_leather_boots,          itm_leather_boots,                   itm_khergit_guard_helmet,   itm_leather_gloves,       itm_khergit_sword_two_handed_b,                        itm_tab_shield_small_round_b],      knight_attrib_4,wp(210),knight_skills_4, 0x0000000a180441c921a30ea68b54971500000000001e54db0000000000000000, khergit_face_older_2],
  ["knight_3_10", "Az Khan Sebula","Sebula", tf_hero, 0, reserved,  fac_kingdom_3, [    itm_warhorse_steppe,   itm_lamellar_vest_khergit,itm_lamellar_armor,                   itm_hide_boots,             itm_splinted_greaves,                itm_khergit_guard_helmet,   itm_lamellar_gauntlets,   itm_sword_khergit_4,                                   itm_tab_shield_small_round_c],      knight_attrib_5,wp(250),knight_skills_5, 0x0000000a3b00418c5b36c686d920a76100000000001c436f0000000000000000, khergit_face_older_2],
  ["knight_3_11", "Sef Tulug", "Tulug", tf_hero, 0, reserved,  fac_kingdom_3, [         itm_steppe_horse,      itm_nomad_robe,          itm_nomad_robe,                        itm_nomad_boots,            itm_nomad_boots,                     itm_khergit_war_helmet,     itm_leather_gloves,       itm_sword_khergit_2,itm_javelin,                       itm_tab_shield_small_round_a],      knight_attrib_1,wp(120),knight_skills_1, 0x00000007d100534b44962d14d370c65c00000000001ed6df0000000000000000, khergit_face_middle_2],
  ["knight_3_12", "Diktator Nasugei", "Nasugei", tf_hero, 0, reserved,  fac_kingdom_3, [itm_steppe_horse,      itm_nomad_vest,          itm_lamellar_vest_khergit,             itm_nomad_boots,            itm_nomad_boots,                     itm_khergit_guard_helmet,   itm_leather_gloves,       itm_sword_khergit_3,                                   itm_tab_shield_small_round_b],      knight_attrib_2,wp(150),knight_skills_2, 0x0000000bf400610c5b33d3c9258edb6c00000000001eb96d0000000000000000, khergit_face_old_2],
  ["knight_3_13", "Diktator Urubay","Urubay", tf_hero, 0, reserved,  fac_kingdom_3, [   itm_courser,           itm_nomad_robe,          itm_lamellar_vest_khergit,             itm_leather_boots,          itm_leather_boots,                   itm_khergit_cavalry_helmet, itm_leather_gloves,       itm_sword_khergit_3,itm_khergit_bow,itm_bodkin_arrows, itm_tab_shield_small_round_b],      knight_attrib_3,wp(180),knight_skills_3, 0x0000000bfd0061c65b6eb33b25d2591d00000000001f58eb0000000000000000, khergit_face_older_2],
  ["knight_3_14", "Az Khan Hugu",  "Hugu", tf_hero, 0, reserved,  fac_kingdom_3, [      itm_courser,           itm_lamellar_vest_khergit,                                      itm_hide_boots,             itm_splinted_greaves,                itm_khergit_guard_helmet,   itm_leather_gloves,       itm_winged_mace,itm_jarid,                             itm_tab_shield_small_round_b],      knight_attrib_4,wp(210),knight_skills_4, 0x0000000b6900514144be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_older_2],
  ["knight_3_15", "Az Khan Tansugai", "Tansugai", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe,  itm_ragged_outfit,       itm_khergit_elite_armor,               itm_hide_boots,             itm_splinted_greaves,                itm_khergit_cavalry_helmet, itm_lamellar_gauntlets,   itm_sword_khergit_4,                                   itm_tab_shield_small_round_c],      knight_attrib_5,wp(250),knight_skills_5, 0x0000000c360c524b6454465b59b9d93500000000001ea4860000000000000000, khergit_face_older_2],
  ["knight_3_16", "Sef Tirida","Tirida", tf_hero, 0, reserved,  fac_kingdom_3, [        itm_steppe_horse,      itm_tribal_warrior_outfit,                                      itm_nomad_boots,            itm_nomad_boots,                     itm_khergit_guard_helmet,   itm_leather_gloves,       itm_sword_khergit_2,itm_nomad_bow,itm_arrows,          itm_tab_shield_small_round_a],      knight_attrib_1,wp(120),knight_skills_1, 0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000, khergit_face_middle_2],
  ["knight_3_17", "Diktator Ulusamai", "Ulusamai", tf_hero, 0, reserved,  fac_kingdom_3, [itm_steppe_horse,    itm_nomad_robe,          itm_nomad_robe,                        itm_leather_boots,          itm_leather_boots,                   itm_khergit_guard_helmet,   itm_leather_gloves,       itm_winged_mace,itm_nomad_bow,itm_barbed_arrows,       itm_tab_shield_small_round_a],      knight_attrib_2,wp(150),knight_skills_2, 0x0000000c3c0821c647264ab6e68dc4d500000000001e42590000000000000000, khergit_face_old_2],
  ["knight_3_18", "Diktator Karaban", "Karaban", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,           itm_nomad_vest,          itm_lamellar_vest_khergit,             itm_hide_boots,             itm_splinted_greaves,                itm_khergit_guard_helmet,   itm_leather_gloves,       itm_scimitar,itm_khergit_bow,itm_bodkin_arrows,        itm_tab_shield_small_round_b],      knight_attrib_3,wp(180),knight_skills_3, 0x0000000c0810500347ae7acd0d3ad74a00000000001e289a0000000000000000, khergit_face_older_2],
  ["knight_3_19", "Az Khan Akadan","Akadan", tf_hero, 0, reserved,  fac_kingdom_3, [    itm_hunter,            itm_nomad_robe,          itm_lamellar_armor,                    itm_leather_boots,          itm_splinted_greaves,                itm_khergit_cavalry_helmet, itm_leather_gloves,       itm_sword_khergit_3,itm_lance,                         itm_tab_shield_small_round_c],      knight_attrib_4,wp(210),knight_skills_4, 0x0000000c1500510528f50d52d20b152300000000001d66db0000000000000000, khergit_face_older_2],
  ["knight_3_20", "Dundush Khan","Dundush", tf_hero, 0, reserved,  fac_kingdom_3, [     itm_warhorse_steppe,   itm_lamellar_vest,       itm_khergit_elite_armor,               itm_hide_boots,             itm_splinted_greaves,                itm_khergit_guard_helmet,   itm_lamellar_gauntlets,   itm_sword_khergit_4,itm_khergit_bow,itm_khergit_arrows,itm_tab_shield_small_round_c],      knight_attrib_5,wp(250),knight_skills_5, 0x0000000f7800620d66b76edd5cd5eb6e00000000001f691e0000000000000000, khergit_face_older_2],
  #new lords
  ["knight_3_21", "Khun", "Khun", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x000000018204454b564b9292e374b4ac00000000000929180000000000000000, khergit_face_middle_2],
  ["knight_3_22", "Nis",  "Nis", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x000000019a0030896732ef1b3271c6e000000000000c93130000000000000000, khergit_face_old_2],
  ["knight_3_23", "Gharn",  "Gharn", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000007d400400944cb699c8e4aa76400000000001ed52c0000000000000000, khergit_face_older_2],
  ["knight_3_24", "Azlei", "Azlei", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x000000020008458735ab8db88a52632400000000001dc4dc0000000000000000, khergit_face_older_2],
  ["knight_3_25", "Liraz",  "Liraz", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000001f004210b30eb71eeddc6358200000000001ca6f30000000000000000, khergit_face_older_2],
  ["knight_3_26", "Hyun", "Hyun", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x0000000c7b04400b6aeb2edad3b2996400000000001d389b0000000000000000, khergit_face_middle_2],
  ["knight_3_27", "Uklaz","Uklaz", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000006c01045c932add25a923236e300000000001d48960000000000000000, khergit_face_old_2],
  ["knight_3_28", "Deslin", "Deslin", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000001ff0c20cb4ce38d481d9636d100000000001dc7740000000000000000, khergit_face_older_2],
  ["knight_3_29", "Jound","Jound", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000008ff0041cf39636d581c6e534100000000001fc6920000000000000000, khergit_face_older_2],
  ["knight_3_30", "Sulen","Sulen", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000008190862c9454c95b4558d491d00000000001d629c0000000000000000, khergit_face_older_2],
  ["knight_3_31", "Faren","Faren", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x000000045908648c151e51f31c9a129400000000001ed2ec0000000000000000, khergit_face_older_2],
  ["knight_3_32", "Woun",  "Woun", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000009b804534a565a4e46c770ece200000000001cc7920000000000000000, khergit_face_older_2],
  ["knight_3_33", "Delnai", "Delnai", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x000000027008504912d392e7546d416500000000001d34dc0000000000000000, khergit_face_older_2],
  ["knight_3_34", "Zay","Zay", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x000000084e0c538d371caa44e4b756e400000000001d45690000000000000000, khergit_face_middle_2],
  ["knight_3_35", "Kilnaz", "Kilnaz", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x0000000a5c00238946ed0a2d644a38ea00000000001cd91b0000000000000000, khergit_face_old_2],
  # ["knight_3_38", "Roldan", "Roldan", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000008d404238a2a9b4b2d59a5b2e300000000001ec3530000000000000000, khergit_face_older_2],
  # ["knight_3_39", "Daman","Daman", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000006b208324c16d972288497415c00000000001dc45b0000000000000000, khergit_face_older_2],
  # ["knight_3_40", "Solm","Solm", tf_hero, 0, reserved,  fac_kingdom_3, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000006f31043015994ae2963a9f8d900000000001e31510000000000000000, khergit_face_older_2],

  ## Nord
  ["knight_4_1", "War Lord Aedin", "Aedin", tf_hero, 0, reserved,  fac_kingdom_4, [                            itm_rich_outfit,         itm_studded_leather_coat,              itm_leather_boots,          itm_leather_boots,                   itm_nasal_helmet,           itm_leather_gloves,       itm_battle_axe,itm_light_throwing_axes,                itm_tab_shield_round_b],       	 knight_attrib_1,wp(120),knight_skills_1, 0x0000000c13002254340eb1d91159392d00000000001eb75a0000000000000000, nord_face_middle_2],
  ["knight_4_2", "Lesser Thane Irya", "Irya", tf_hero, 0, reserved,  fac_kingdom_4, [                          itm_short_tunic,         itm_byrnie,                            itm_blue_hose,              itm_mail_chausses,                   itm_nordic_footman_helmet,  itm_mail_mittens,         itm_one_handed_battle_axe_a,itm_throwing_axes,         itm_tab_shield_round_c],       	 knight_attrib_2,wp(150),knight_skills_2, 0x0000000c1610218368e29744e9a5985b00000000001db2a10000000000000000, nord_face_old_2],
  ["knight_4_3", "Lesser Thane Olaf", "Olaf", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_hunter,            itm_rich_outfit,         itm_mail_shirt,                        itm_nomad_boots,            itm_mail_chausses,                   itm_nordic_fighter_helmet,  itm_mail_mittens,         itm_war_axe,itm_throwing_axes,                         itm_tab_shield_round_c],      	     knight_attrib_3,wp(180),knight_skills_3, 0x0000000c03040289245a314b744b30a400000000001eb2a90000000000000000, nord_face_older_2],
  ["knight_4_4", "Thane Reamald", "Reamald", tf_hero, 0, reserved,  fac_kingdom_4, [    itm_hunter,            itm_leather_vest,        itm_banded_armor,                      itm_woolen_hose,            itm_mail_boots,                      itm_nordic_huscarl_helmet,  itm_mail_mittens,         itm_spiked_mace,itm_throwing_axes,                     itm_tab_shield_round_d],      	     knight_attrib_4,wp(210),knight_skills_4, 0x0000000c3f1001ca3d6955b26a8939a300000000001e39b60000000000000000, nord_face_older_2],
  ["knight_4_5", "Jarl Turya", "Turya", tf_hero, 0, reserved,  fac_kingdom_4, [                                itm_fur_coat,            itm_cuir_bouilli,                      itm_leather_boots,          itm_splinted_leather_greaves,        itm_nordic_warlord_helmet,  itm_gauntlets,            itm_one_handed_battle_axe_c,itm_heavy_throwing_axes,   itm_tab_shield_round_e],      	     knight_attrib_5,wp(250),knight_skills_5, 0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000, nord_face_older_2],
  ["knight_4_6", "War Lord Gundur", "Gundur", tf_hero, 0, reserved,  fac_kingdom_4, [                          itm_nomad_robe,          itm_byrnie,                            itm_nomad_boots,            itm_nomad_boots,                     itm_nasal_helmet,           itm_leather_gloves,       itm_battle_axe,                                        itm_tab_shield_round_b],       	 knight_attrib_1,wp(120),knight_skills_1, 0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_middle_2],
  ["knight_4_7", "Lesser Thane Harald", "Harald", tf_hero, 0, reserved,  fac_kingdom_4, [                      itm_fur_coat,            itm_mail_shirt,                        itm_leather_boots,          itm_leather_boots,                   itm_nordic_footman_helmet,  itm_mail_mittens,         itm_sword_viking_2,                                    itm_tab_shield_round_c],       	 knight_attrib_2,wp(150),knight_skills_2, 0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_old_2],
  ["knight_4_8", "Lesser Thane Knudarr", "Knudarr", tf_hero, 0, reserved,  fac_kingdom_4, [                    itm_rich_outfit,         itm_mail_hauberk,                      itm_woolen_hose,            itm_mail_chausses,                   itm_nordic_fighter_helmet,  itm_mail_mittens,         itm_long_axe_b,itm_throwing_axes,                      itm_tab_shield_round_c],       	 knight_attrib_3,wp(180),knight_skills_3, 0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000, nord_face_older_2],
  ["knight_4_9", "Thane Haeda", "Haeda", tf_hero, 0, reserved,  fac_kingdom_4, [        itm_hunter,            itm_nomad_robe,          itm_mail_hauberk,                      itm_blue_hose,              itm_mail_chausses,                   itm_nordic_huscarl_helmet,  itm_gauntlets,            itm_one_handed_battle_axe_b,itm_short_bow,itm_bodkin_arrows,itm_tab_shield_round_d],  	 knight_attrib_4,wp(210),knight_skills_4, 0x00000000080c54c1345bd21349b1b67300000000001c90c80000000000000000, nord_face_older_2],
  ["knight_4_10", "Thane Turegor", "Turegor", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_hunter,            itm_courtly_outfit,      itm_banded_armor,                      itm_nomad_boots,            itm_splinted_leather_greaves,        itm_nordic_warlord_helmet,  itm_gauntlets,            itm_great_axe,                                         itm_tab_shield_round_d],       	 knight_attrib_5,wp(250),knight_skills_5, 0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_older_2],
  ["knight_4_11", "War Lord Logarson", "Logarson", tf_hero, 0, reserved,  fac_kingdom_4, [                     itm_rich_outfit,         itm_studded_leather_coat,              itm_leather_boots,                                               itm_nordic_footman_helmet,  itm_mail_mittens,         itm_battle_axe,                                        itm_tab_shield_round_b],      	     knight_attrib_1,wp(120),knight_skills_1, 0x000000002d100005471d4ae69ccacb1d00000000001dca550000000000000000, nord_face_middle_2],
  ["knight_4_12", "Lesser Thane Aeric", "Aeric", tf_hero, 0, reserved,  fac_kingdom_4, [                       itm_short_tunic,         itm_byrnie,                            itm_leather_boots,                                               itm_nasal_helmet,           itm_leather_gloves,       itm_one_handed_battle_axe_a,                           itm_tab_shield_round_c],       	 knight_attrib_2,wp(150),knight_skills_2, 0x0000000b9500020824936cc51cb5bb2500000000001dd4d80000000000000000, nord_face_old_2],
  ["knight_4_13", "Lesser Thane Faarn", "Faarn", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,            itm_rich_outfit,         itm_mail_hauberk,                      itm_nomad_boots,            itm_mail_chausses,                   itm_nordic_fighter_helmet,  itm_mail_mittens,         itm_war_axe,                                           itm_tab_shield_round_c],       	 knight_attrib_3,wp(180),knight_skills_3, 0x0000000a300012c439233512e287391d00000000001db7200000000000000000, nord_face_older_2],
  ["knight_4_14", "Thane Bulba", "Bulba", tf_hero, 0, reserved,  fac_kingdom_4, [                              itm_leather_vest,        itm_banded_armor,                      itm_woolen_hose,            itm_splinted_leather_greaves,        itm_nordic_huscarl_helmet,  itm_gauntlets,            itm_sword_viking_3_small,itm_throwing_axes,            itm_tab_shield_round_c],       	 knight_attrib_4,wp(210),knight_skills_4, 0x0000000c0700414f2cb6aa36ea50a69d00000000001dc55c0000000000000000, nord_face_older_2],
  ["knight_4_15", "Jarl Rayeck", "Rayeck", tf_hero, 0, reserved,  fac_kingdom_4, [      itm_warhorse,          itm_leather_jacket,      itm_cuir_bouilli,                      itm_leather_boots,          itm_mail_boots,                      itm_nordic_warlord_helmet,  itm_gauntlets,            itm_spiked_mace,                                       itm_tab_shield_round_e],       	 knight_attrib_5,wp(250),knight_skills_5, 0x0000000d920801831715d1aa9221372300000000001ec6630000000000000000, nord_face_older_2],
  ["knight_4_16", "War Lord Dirigun", "Dirigun", tf_hero, 0, reserved,  fac_kingdom_4, [                       itm_nomad_robe,          itm_byrnie,                            itm_nomad_boots,            itm_nomad_boots,                     itm_nasal_helmet,           itm_leather_gloves,       itm_battle_axe,itm_light_throwing_axes,                itm_tab_shield_round_b],       	 knight_attrib_1,wp(120),knight_skills_1, 0x000000099700124239233512e287391d00000000001db7200000000000000000, nord_face_middle_2],
  ["knight_4_17", "Lesser Thane Marayirr", "Marayirr", tf_hero, 0, reserved,  fac_kingdom_4, [                 itm_fur_coat,            itm_mail_shirt,                        itm_leather_boots,          itm_leather_boots,                   itm_nordic_footman_helmet,  itm_mail_mittens,         itm_sword_viking_2,itm_light_throwing_axes,            itm_tab_shield_round_c],       	 knight_attrib_2,wp(150),knight_skills_2, 0x0000000c2f0442036d232a2324b5b81400000000001e55630000000000000000, nord_face_old_2],
  ["knight_4_18", "Lesser Thane Gearth", "Gearth", tf_hero, 0, reserved,  fac_kingdom_4, [                     itm_rich_outfit,         itm_mail_hauberk,                      itm_woolen_hose,            itm_mail_chausses,                   itm_nordic_fighter_helmet,  itm_mail_mittens,         itm_sword_viking_2,                                    itm_tab_shield_round_d],       	 knight_attrib_3,wp(180),knight_skills_3, 0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000, nord_face_older_2],
  ["knight_4_19", "Thane Surdun", "Surdun", tf_hero, 0, reserved,  fac_kingdom_4, [     itm_hunter,            itm_nomad_robe,          itm_mail_hauberk,                      itm_blue_hose,              itm_mail_chausses,                   itm_nordic_huscarl_helmet,  itm_gauntlets,            itm_one_handed_battle_axe_c,itm_heavy_throwing_axes,   itm_tab_shield_round_d],       	 knight_attrib_4,wp(210),knight_skills_4, 0x0000000c0308225124e26d4a6295965a00000000001d23e40000000000000000, nord_face_older_2],
  ["knight_4_20", "Thane Gerlad", "Gerlad", tf_hero, 0, reserved,  fac_kingdom_4, [     itm_hunter,            itm_courtly_outfit,      itm_banded_armor,                      itm_nomad_boots,            itm_mail_boots,                      itm_nordic_warlord_helmet,  itm_gauntlets,            itm_great_axe,itm_heavy_throwing_axes,                 itm_tab_shield_round_d],       	 knight_attrib_5,wp(250),knight_skills_5, 0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000, nord_face_older_2],
  #new lords
  ["knight_4_21", "Godfred", "Godfred", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x000000018604004f26c37f385429c54500000000000d35690000000000000000, nord_face_middle_2],
  ["knight_4_22", "Thorir", "Thorir", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x0000000b87101053549c4fa86591341d00000000001e55200000000000000000, nord_face_old_2],
  ["knight_4_23", "Herp", "Herp", tf_hero, 0, reserved,  fac_kingdom_4, [],      	     knight_attrib_0,wp(90),knight_skills_0, 0x00000003000811494cf36ebc5b8ec91500000000001dd9660000000000000000, nord_face_older_2],
  ["knight_4_24", "Hagar", "Hagar", tf_hero, 0, reserved,  fac_kingdom_4, [],      	     knight_attrib_0,wp(90),knight_skills_0, 0x0000000e470c15061c344ed772d64a9400000000001eab230000000000000000, nord_face_older_2],
  ["knight_4_25", "Ingmar", "Ingmar", tf_hero, 0, reserved,  fac_kingdom_4, [],      	     knight_attrib_0,wp(90),knight_skills_0, 0x000000008a0801c156ab7346de974c9500000000001dab690000000000000000, nord_face_older_2],
  ["knight_4_26", "Reilo", "Reilo", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x00000009400c0145286685b32b6648da00000000001e37a40000000000000000, nord_face_middle_2],
  ["knight_4_27", "Fafnir", "Fafnir", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x00000005400401cd471d4d5813c5d86300000000001d125c0000000000000000, nord_face_old_2],
  ["knight_4_28", "Jimalar", "Jimalar", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x000000042d081241464a6ea4949ad49300000000001e59150000000000000000, nord_face_older_2],
  ["knight_4_29", "Ydnor", "Ydnor", tf_hero, 0, reserved,  fac_kingdom_4, [],  	 knight_attrib_0,wp(90),knight_skills_0, 0x00000008c30c12c22b2d4de093d1929100000000001ee8e30000000000000000, nord_face_older_2],
  ["knight_4_30", "Lafir", "Lafir", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x000000039b0c024176dd963a5d8e199400000000001f42a60000000000000000, nord_face_older_2],
  ["knight_4_31", "Gutenhar", "Gutenhar", tf_hero, 0, reserved,  fac_kingdom_4, [],      	     knight_attrib_0,wp(90),knight_skills_0, 0x00000008c100018335aa6d992cb2332400000000000da69c0000000000000000, nord_face_middle_2],
  ["knight_4_32", "Laum", "Laum", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x00000008c404054948dc92b3a3954c9500000000001e56e20000000000000000, nord_face_old_2],
  ["knight_4_33", "Solinar", "Solinar", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x000000088300028b46e0694d6291345a00000000001d2ce60000000000000000, nord_face_older_2],
  ["knight_4_34", "Barn", "Barn", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x0000000416000345495456b4d178b2d600000000001d99510000000000000000, nord_face_older_2],
  ["knight_4_35", "Rolnack", "Rolnack", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x000000070000120e14e9b19b6c5ac4e400000000001cd8e50000000000000000, nord_face_older_2],
  # ["knight_4_36", "Tundar", "Tundar", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x000000027f0002ca3d1e75a75567575d00000000001ed91b0000000000000000, nord_face_middle_2],
  # ["knight_4_37", "Moln", "Moln", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x00000007c108151057aaccc664af162e00000000000d46cc0000000000000000, nord_face_old_2],
  # ["knight_4_38", "Cundol", "Cundol", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x0000000a420411d014e3a6b71c2de31b00000000001217a40000000000000000, nord_face_older_2],
  # ["knight_4_39", "Jorund", "Jorund", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x00000004a80c054d52db4d346c88a78b00000000001ea51e0000000000000000, nord_face_older_2],
  # ["knight_4_40", "Lorn", "Lorn", tf_hero, 0, reserved,  fac_kingdom_4, [],       	 knight_attrib_0,wp(90),knight_skills_0, 0x0000000d00040545695341eabc8d896300000000001d579a0000000000000000, nord_face_older_2],

  ## Rhodok
  ["knight_5_1", "Burgher Matheas", "Matheas", tf_hero, 0, reserved,  fac_kingdom_5, [  itm_saddle_horse,      itm_tabard,              itm_aketon_green,                      itm_leather_boots,          itm_leather_boots,                   itm_footman_helmet,         itm_leather_gloves,       itm_fighting_pick,                                     itm_tab_shield_heater_b],       knight_attrib_1,wp(120),knight_skills_1, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_5_2", "Elder Gutlans", "Gutlans", tf_hero, 0, reserved,  fac_kingdom_5, [    itm_saddle_horse,      itm_red_gambeson,        itm_ragged_outfit,                     itm_leather_boots,          itm_leather_boots,                   itm_kettle_hat,             itm_leather_gloves,       itm_military_cleaver_b,                                itm_tab_shield_heater_c],       knight_attrib_2,wp(150),knight_skills_2, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_5_3", "Leader Laruqen", "Laruqen", tf_hero, 0, reserved,  fac_kingdom_5, [                          itm_short_tunic,         itm_heraldic_mail_with_tunic,          itm_nomad_boots,            itm_mail_chausses,                   itm_kettle_hat,             itm_mail_mittens,         itm_military_cleaver_c,                                itm_tab_shield_pavise_c],       knight_attrib_3,wp(180),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_4", "Gaffer Raichs", "Raichs", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_hunter,            itm_leather_jacket,      itm_brigandine_red,                    itm_woolen_hose,            itm_mail_chausses,                   itm_flat_topped_helmet,     itm_mail_mittens,         itm_military_cleaver_c,                                itm_tab_shield_heater_cav_a],   knight_attrib_4,wp(210),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_5", "Warden Reland", "Reland", tf_hero, 0, reserved,  fac_kingdom_5, [                            itm_rich_outfit,         itm_scale_armor,                       itm_leather_boots,          itm_mail_boots,                      itm_guard_helmet,           itm_gauntlets,            itm_glaive,                                            itm_tab_shield_pavise_d],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_5_6", "Burgher Tarchias", "Tarchias", tf_hero, 0, reserved,  fac_kingdom_5, [                       itm_ragged_outfit,       itm_ragged_outfit,                     itm_leather_boots,          itm_leather_boots,                   itm_kettle_hat,             itm_leather_gloves,       itm_military_cleaver_b,                                itm_tab_shield_pavise_a],       knight_attrib_1,wp(120),knight_skills_1, 0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000, rhodok_face_middle_2],
  ["knight_5_7", "Elder Gharmall", "Gharmall", tf_hero, 0, reserved,  fac_kingdom_5, [  itm_pack_horse,        itm_coarse_tunic,        itm_aketon_green,                      itm_leather_boots,          itm_leather_boots,                   itm_kettle_hat,             itm_leather_gloves,       itm_military_sickle_a,                                 itm_tab_shield_heater_c],       knight_attrib_2,wp(150),knight_skills_2, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, rhodok_face_old_2],
  ["knight_5_8", "Leader Talbar", "Talbar", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_pack_horse,        itm_courtly_outfit,      itm_byrnie,                            itm_woolen_hose,            itm_mail_chausses,                   itm_bascinet,               itm_mail_mittens,         itm_military_pick,                                     itm_tab_shield_heater_cav_a],   knight_attrib_3,wp(180),knight_skills_3, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, rhodok_face_older_2],
  ["knight_5_9", "Leader Rimusk", "Rimusk", tf_hero, 0, reserved,  fac_kingdom_5, [                            itm_leather_jacket,      itm_surcoat_over_mail,                 itm_leather_boots,          itm_mail_boots,                      itm_kettle_hat,             itm_gauntlets,            itm_two_handed_cleaver                                                        ],       knight_attrib_4,wp(210),knight_skills_4, 0x00000000420430c32331b5551c4724a100000000001e39a40000000000000000, rhodok_face_older_2],
  ["knight_5_10", "Gaffer Falsevor", "Falsevor", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_b,        itm_rich_outfit,         itm_coat_of_plates,                    itm_blue_hose,              itm_iron_greaves,                    itm_bascinet,               itm_gauntlets,            itm_bastard_sword_b,                                   itm_tab_shield_heater_cav_a],   knight_attrib_5,wp(250),knight_skills_5, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],
  ["knight_5_11", "Elder Etrosq", "Falsevor", tf_hero, 0, reserved,  fac_kingdom_5, [                          itm_tabard,              itm_aketon_green,                      itm_leather_boots,          itm_leather_boots,                   itm_kettle_hat,             itm_leather_gloves,       itm_fighting_pick,itm_pike,                            itm_tab_shield_pavise_a],       knight_attrib_1,wp(120),knight_skills_1, 0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000, rhodok_face_middle_2],
  ["knight_5_12", "Elder Kurnias", "Kurnias", tf_hero, 0, reserved,  fac_kingdom_5, [                          itm_red_gambeson,        itm_byrnie,                            itm_leather_boots,          itm_leather_boots,                   itm_kettle_hat,             itm_leather_gloves,       itm_long_hafted_knobbed_mace,                          itm_tab_shield_pavise_b],       knight_attrib_2,wp(150),knight_skills_2, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, rhodok_face_old_2],
  ["knight_5_13", "Leader Tellrog", "Tellrog", tf_hero, 0, reserved,  fac_kingdom_5, [  itm_saddle_horse,      itm_short_tunic,         itm_haubergeon,                        itm_nomad_boots,            itm_mail_chausses,                   itm_bascinet,               itm_mail_mittens,         itm_shortened_military_scythe                                                 ],       knight_attrib_3,wp(180),knight_skills_3, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2],
  ["knight_5_14", "Gaffer Tribidan", "Tribidan", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,            itm_leather_jacket,      itm_brigandine_red,                    itm_woolen_hose,            itm_mail_chausses,                   itm_bascinet,               itm_mail_mittens,         itm_morningstar,itm_light_crossbow,itm_bolts                                  ],       knight_attrib_4,wp(210),knight_skills_4, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
  ["knight_5_15", "Warden Gerluchs", "Gerluchs", tf_hero, 0, reserved,  fac_kingdom_5, [                       itm_rich_outfit,         itm_heraldic_mail_with_tabard,         itm_leather_boots,          itm_mail_boots,                      itm_kettle_hat,             itm_gauntlets,            itm_ashwood_pike,itm_sword_medieval_b_small,           itm_tab_shield_pavise_d],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],
  ["knight_5_16", "Burgher Fudreim", "Fudreim", tf_hero, 0, reserved,  fac_kingdom_5, [ itm_sumpter_horse,     itm_ragged_outfit,       itm_ragged_outfit,                     itm_leather_boots,          itm_leather_boots,                   itm_footman_helmet,         itm_leather_gloves,       itm_sword_medieval_a,                                  itm_tab_shield_heater_a],       knight_attrib_1,wp(120),knight_skills_1, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, rhodok_face_middle_2],
  ["knight_5_17", "Elder Nealcha", "Nealcha", tf_hero, 0, reserved,  fac_kingdom_5, [                          itm_coarse_tunic,        itm_byrnie,                            itm_leather_boots,          itm_mail_chausses,                   itm_spiked_helmet,          itm_leather_gloves,       itm_sword_medieval_b,                                  itm_tab_shield_pavise_b],       knight_attrib_2,wp(150),knight_skills_2, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
  ["knight_5_18", "Leader Fraichin", "Fraichin", tf_hero, 0, reserved,  fac_kingdom_5, [itm_pack_horse,        itm_courtly_outfit,      itm_byrnie,                            itm_woolen_hose,            itm_mail_chausses,                   itm_flat_topped_helmet,     itm_mail_mittens,         itm_sword_medieval_b,                                  itm_tab_shield_heater_d],       knight_attrib_3,wp(180),knight_skills_3, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2],
  ["knight_5_19", "Gaffer Trimbau", "Trimbau", tf_hero, 0, reserved,  fac_kingdom_5, [                         itm_leather_jacket,      itm_heraldic_mail_with_surcoat,        itm_leather_boots,          itm_mail_boots,                      itm_bascinet_2,             itm_gauntlets,            itm_military_pick,                                     itm_tab_shield_pavise_d],       knight_attrib_4,wp(210),knight_skills_4, 0x0000000038043194092ab4b2d9adb44c00000000001e072c0000000000000000, rhodok_face_older_2],
  ["knight_5_20", "Warden Reichsin", "Reichsin", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse,          itm_rich_outfit,         itm_scale_armor,                       itm_blue_hose,              itm_iron_greaves,                    itm_full_helm,              itm_gauntlets,            itm_military_pick,itm_heavy_lance,                     itm_tab_shield_heater_cav_b],   knight_attrib_5,wp(250),knight_skills_5, 0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000, rhodok_face_older_2],
  #new lords
  ["knight_5_21", "Elios", "Elios", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000001a20850c417264518422e596b00000000001d35630000000000000000, rhodok_face_middle_2],
  ["knight_5_22", "Solis", "Solis", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000001b90c3045171429d8a4492d1a00000000000a675a0000000000000000, rhodok_face_old_2],
  ["knight_5_23", "Renald", "Renald", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000001ba0c6540475b312773ad5d2c00000000001eb5620000000000000000, rhodok_face_older_2],
  ["knight_5_24", "Durin", "Durin", tf_hero, 0, reserved,  fac_kingdom_5, [],   knight_attrib_0,wp(90),knight_skills_0, 0x00000009210c634e37b3734a55775ce500000000001ea7650000000000000000, rhodok_face_older_2],
  ["knight_5_25", "Holmar", "Holmar", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x0000000abf0441d05e50a898da8dc26500000000001dc2e30000000000000000, rhodok_face_older_2],
  ["knight_5_26", "Dismis", "Dismis", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000002ee085282136c6cc69b8a692200000000001d5a5d0000000000000000, rhodok_face_middle_2],
  ["knight_5_27", "Sard", "Sard", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x0000000ad61052874aad76956bd2676c00000000001ebd1c0000000000000000, rhodok_face_old_2],
  ["knight_5_28", "Jemun", "Jemun", tf_hero, 0, reserved,  fac_kingdom_5, [],   knight_attrib_0,wp(90),knight_skills_0, 0x00000002b21045443d1d9a52ed8a68e500000000001dc4e20000000000000000, rhodok_face_older_2],
  ["knight_5_29", "Kird", "Kird", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000004170031012f348d458d72e79a00000000001ca7a10000000000000000, rhodok_face_older_2],
  ["knight_5_30", "Cirec", "Cirec", tf_hero, 0, reserved,  fac_kingdom_5, [],   knight_attrib_0,wp(90),knight_skills_0, 0x000000043f0412c63054ceda5b6d32e400000000001ca71b0000000000000000, rhodok_face_older_2],
  ["knight_5_31", "Tumis", "Tumis", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000001ee1042062aea4ca52251a6aa00000000001d47210000000000000000, rhodok_face_middle_2],
  ["knight_5_32", "Bargas", "Bargas", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000008e60c424132f30e3725f214b300000000001cb79a0000000000000000, rhodok_face_old_2],
  ["knight_5_33", "Moder", "Moder", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000003f200431156a365c69c38971900000000001e12eb0000000000000000, rhodok_face_older_2],
  ["knight_5_34", "Ormed", "Ormed", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000004410c35c448a330c2927166de00000000001d232d0000000000000000, rhodok_face_older_2],
  ["knight_5_35", "Shuls", "Shuls", tf_hero, 0, reserved,  fac_kingdom_5, [],       knight_attrib_0,wp(90),knight_skills_0, 0x000000053c1065c4366c75a5a4862a9c00000000001db5160000000000000000, rhodok_face_older_2],

  ## Sarranid
  ["knight_6_1", "Naib Uqais", "Uqais", tf_hero, 0, reserved,  fac_kingdom_6, [         itm_arabian_horse_a,   itm_archers_vest,                                               itm_sarranid_boots_b,                                            itm_sarranid_warrior_cap,   itm_leather_gloves,       itm_bamboo_spear,itm_arabian_sword_a,                  itm_tab_shield_small_round_a],  knight_attrib_1,wp(120),knight_skills_1, 0x00000000600c2084486195383349eae500000000001d16a30000000000000000, sarranid_face_middle_2],
  ["knight_6_2", "Naib Hamezan", "Hamezan", tf_hero, 0, reserved,  fac_kingdom_6, [     itm_arabian_horse_a,   itm_sarranid_leather_armor,                                     itm_sarranid_boots_b,                                            itm_sarranid_horseman_helmet,itm_leather_gloves,      itm_sarranid_two_handed_mace_1                                                ],       knight_attrib_2,wp(150),knight_skills_2, 0x00000001380825d444cb68b92b8d3b1d00000000001dd71e0000000000000000, sarranid_face_old_2],
  ["knight_6_3", "Emir Atis", "Atis", tf_hero, 0, reserved,  fac_kingdom_6, [           itm_arabian_horse_b,   itm_sarranid_cavalry_robe,                                      itm_sarranid_boots_c,                                            itm_sarranid_helmet1,       itm_leather_gloves,       itm_sarranid_two_handed_axe_a                                                 ],       knight_attrib_3,wp(180),knight_skills_3, 0x000000002208428579723147247ad4e500000000001f14d40000000000000000, sarranid_face_older_2],
  ["knight_6_4", "Emir Nuwas", "Nuwas", tf_hero, 0, reserved,  fac_kingdom_6, [         itm_arabian_horse_b,   itm_arabian_armor_b,                                            itm_sarranid_boots_c,                                            itm_sarranid_mail_coif,     itm_mail_mittens,         itm_sarranid_cavalry_sword,itm_bamboo_spear,           itm_tab_shield_small_round_c],  knight_attrib_4,wp(210),knight_skills_4, 0x00000009bf084285050caa7d285be51a00000000001d11010000000000000000, sarranid_face_older_2],
  ["knight_6_5", "Shah Mundhalir", "Mundhalir", tf_hero, 0, reserved,  fac_kingdom_6, [ itm_arabian_horse_b,   itm_mamluke_mail,                                               itm_sarranid_boots_d,                                            itm_sarranid_veiled_helmet, itm_mail_mittens,         itm_khergit_sword_two_handed_b                                                ],       knight_attrib_5,wp(250),knight_skills_5, 0x000000002a084003330175aae175da9c00000000001e02150000000000000000, sarranid_face_older_2],
  ["knight_6_6", "Naib Ghanawa", "Ghanawa", tf_hero, 0, reserved,  fac_kingdom_6, [     itm_arabian_horse_a,   itm_sarranid_leather_armor,                                     itm_sarranid_boots_b,                                            itm_sarranid_warrior_cap,   itm_leather_gloves,       itm_bamboo_spear,itm_arabian_sword_a,                  itm_tab_shield_small_round_a],  knight_attrib_1,wp(120),knight_skills_1, 0x00000001830043834733294c89b128e200000000001259510000000000000000, sarranid_face_middle_2],
  ["knight_6_7", "Emir Nuam", "Nuam", tf_hero, 0, reserved,  fac_kingdom_6, [           itm_arabian_horse_a,   itm_sarranid_cavalry_robe,                                      itm_sarranid_boots_b,                                            itm_sarranid_horseman_helmet,itm_leather_gloves,      itm_arabian_sword_b,                                   itm_tab_shield_small_round_b],  knight_attrib_2,wp(150),knight_skills_2, 0x0000000cbf10434020504bbbda9135d500000000001f62380000000000000000, sarranid_face_old_2],
  ["knight_6_8", "Emir Dhiyul", "Dhiyul", tf_hero, 0, reserved,  fac_kingdom_6, [       itm_arabian_horse_b,   itm_sarranid_cavalry_robe,                                      itm_sarranid_boots_c,                                            itm_sarranid_helmet1,       itm_leather_gloves,       itm_sarranid_axe_a,itm_bamboo_spear,                   itm_tab_shield_small_round_b],  knight_attrib_3,wp(180),knight_skills_3, 0x0000000190044003336dcd3ca2cacae300000000001f47640000000000000000, sarranid_face_older_2],
  ["knight_6_9", "Emir Lakhem", "Lakhem", tf_hero, 0, reserved,  fac_kingdom_6, [       itm_arabian_horse_b,   itm_sarranid_mail_shirt,                                        itm_sarranid_boots_c,                                            itm_sarranid_mail_coif,     itm_mail_mittens,         itm_sarranid_two_handed_mace_1                                                ],       knight_attrib_4,wp(210),knight_skills_4, 0x0000000dde0040c4549dd5ca6f4dd56500000000001e291b0000000000000000, sarranid_face_older_2],
  ["knight_6_10", "Shah Ghulassen", "Ghulassen", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid, itm_sarranid_elite_armor,                                       itm_sarranid_boots_d,                                            itm_sarranid_veiled_helmet, itm_mail_mittens,         itm_bamboo_spear,itm_sarranid_axe_b,                   itm_tab_shield_small_round_c],  knight_attrib_5,wp(250),knight_skills_5, 0x00000001a60441c66ce99256b4ad4b3300000000001d392c0000000000000000, sarranid_face_older_2],
  ["knight_6_11", "Naib Azadun", "Azadun", tf_hero, 0, reserved,  fac_kingdom_6, [      itm_arabian_horse_a,   itm_archers_vest,                                               itm_sarranid_boots_b,                                            itm_sarranid_warrior_cap,   itm_leather_gloves,       itm_sarranid_mace_1,                                   itm_tab_shield_small_round_a],  knight_attrib_1,wp(120),knight_skills_1, 0x0000000fff08134726c28af8dc96e4da00000000001e541d0000000000000000, sarranid_face_middle_2],
  ["knight_6_12", "Naib Quryas", "Quryas", tf_hero, 0, reserved,  fac_kingdom_6, [      itm_arabian_horse_a,   itm_sarranid_cavalry_robe,                                      itm_sarranid_boots_b,                                            itm_sarranid_horseman_helmet,itm_leather_gloves,      itm_bamboo_spear,itm_arabian_sword_b,                  itm_tab_shield_small_round_b],  knight_attrib_2,wp(150),knight_skills_2, 0x0000000035104084635b74ba5491a7a400000000001e46d60000000000000000, sarranid_face_old_2],
  ["knight_6_13", "Emir Amdar", "Amdar", tf_hero, 0, reserved,  fac_kingdom_6, [        itm_arabian_horse_b,   itm_sarranid_cavalry_robe,                                      itm_sarranid_boots_c,                                            itm_sarranid_helmet1,       itm_leather_gloves,       itm_khergit_sword_two_handed_a                                                ],       knight_attrib_3,wp(180),knight_skills_3, 0x00000000001021435b734d4ad94eba9400000000001eb8eb0000000000000000, sarranid_face_older_2],
  ["knight_6_14", "Emir Hiwan", "Hiwan", tf_hero, 0, reserved,  fac_kingdom_6, [        itm_arabian_horse_b,   itm_arabian_armor_b,                                            itm_sarranid_boots_c,                                            itm_sarranid_mail_coif,     itm_mail_mittens,         itm_bamboo_spear,itm_sarranid_cavalry_sword,           itm_tab_shield_small_round_c],  knight_attrib_4,wp(210),knight_skills_4, 0x000000000c0c45c63a5b921ac22db8e200000000001cca530000000000000000, sarranid_face_older_2],
  ["knight_6_15", "Shah Muhnir", "Muhnir", tf_hero, 0, reserved,  fac_kingdom_6, [      itm_arabian_horse_b,   itm_sarranid_elite_armor,                                       itm_sarranid_boots_d,                                            itm_sarranid_veiled_helmet, itm_mail_mittens,         itm_sarranid_two_handed_mace_1                                                ],       knight_attrib_5,wp(250),knight_skills_5, 0x000000001b0c4185369a6938cecde95600000000001f25210000000000000000, sarranid_face_older_2],
  ["knight_6_16", "Naib Ayyam", "Ayyam", tf_hero, 0, reserved,  fac_kingdom_6, [        itm_arabian_horse_a,   itm_sarranid_leather_armor,                                     itm_sarranid_boots_b,                                            itm_sarranid_warrior_cap,   itm_leather_gloves,       itm_bamboo_spear,itm_arabian_sword_a,                  itm_tab_shield_small_round_a],  knight_attrib_1,wp(120),knight_skills_1, 0x00000007770841c80a01e1c5eb51ffff00000000001f12d80000000000000000, sarranid_face_middle_2],
  ["knight_6_17", "Emir Raddoun", "Raddoun", tf_hero, 0, reserved,  fac_kingdom_6, [    itm_arabian_horse_a,   itm_sarranid_leather_armor,                                     itm_sarranid_boots_b,                                            itm_sarranid_horseman_helmet,itm_leather_gloves,      itm_arabian_sword_b,                                   itm_tab_shield_small_round_b],  knight_attrib_2,wp(150),knight_skills_2, 0x000000007f0462c32419f47a1aba8bcf00000000001e7e090000000000000000, sarranid_face_old_2],
  ["knight_6_18", "Emir Tilimsan", "Tilimsan", tf_hero, 0, reserved,  fac_kingdom_6, [  itm_arabian_horse_b,   itm_sarranid_cavalry_robe,                                      itm_sarranid_boots_c,                                            itm_sarranid_helmet1,       itm_leather_gloves,       itm_bamboo_spear,itm_sarranid_axe_a,                   itm_tab_shield_small_round_b],  knight_attrib_3,wp(180),knight_skills_3, 0x000000003410410070d975caac91aca500000000001c27530000000000000000, sarranid_face_older_2],
  ["knight_6_19", "Emir Dhashwal", "Dhashwal", tf_hero, 0, reserved,  fac_kingdom_6, [  itm_arabian_horse_b,   itm_sarranid_mail_shirt,                                        itm_sarranid_boots_c,                                            itm_sarranid_mail_coif,     itm_mail_mittens,         itm_sarranid_two_handed_axe_a                                                 ],       knight_attrib_4,wp(210),knight_skills_4, 0x000000018a08618016ac36bc8b6e4a9900000000001dd45d0000000000000000, sarranid_face_older_2],
  ["knight_6_20", "Shah Biliya", "Biliya", tf_hero, 0, reserved,  fac_kingdom_6, [      itm_warhorse_sarranid, itm_mamluke_mail,                                               itm_sarranid_boots_d,                                            itm_sarranid_veiled_helmet, itm_mail_mittens,         itm_sarranid_two_handed_axe_b                                                 ],       knight_attrib_5,wp(250),knight_skills_5, 0x00000001bd0040c0281a899ac956b94b00000000001ec8910000000000000000, sarranid_face_older_2],
  #new lords
  ["knight_6_21", "Shabn", "Shabn", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x000000019908425348ce70b4e192bd1a000000000009dcf30000000000000000, sarranid_face_middle_2],
  ["knight_6_22", "Olisam", "Olisam", tf_hero, 0, reserved,  fac_kingdom_6, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000001ab08730716a5edaae385849300000000001d37650000000000000000, sarranid_face_old_2],
  ["knight_6_23", "Dusis", "Dusis", tf_hero, 0, reserved,  fac_kingdom_6, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000001ae0c638e5a7575b34ad1cb2d000000000016b7840000000000000000, sarranid_face_older_2],
  ["knight_6_24", "Ashrob", "Ashrob", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x000000019b0071545a6381352291c32200000000001533110000000000000000, sarranid_face_older_2],
  ["knight_6_25", "Hildalir", "Hildalir", tf_hero, 0, reserved,  fac_kingdom_6, [],       knight_attrib_0,wp(90),knight_skills_0, 0x00000001800c6089592ca9ab1386287100000000000595120000000000000000, sarranid_face_older_2],
  ["knight_6_26", "Furnish", "Furnish", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x0000000ca60464125a6b4e577b7ad6db00000000001e571d0000000000000000, sarranid_face_middle_2],
  ["knight_6_27", "Yuli", "Yuli", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x0000000ae60c71c44a6bcec499925cd500000000001dd29b0000000000000000, sarranid_face_old_2],
  ["knight_6_28", "Sanshub", "Sanshub", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x00000009790c63074749736b6c86d45300000000001eb6a30000000000000000, sarranid_face_older_2],
  ["knight_6_29", "Ughaln", "Ughaln", tf_hero, 0, reserved,  fac_kingdom_6, [],       knight_attrib_0,wp(90),knight_skills_0, 0x0000000d3f08711354e455b4938e3f2300000000001e256b0000000000000000, sarranid_face_older_2],
  ["knight_6_30", "Kelvi", "Kelvi", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x0000000cef08619318536f394c519d1c00000000001ee6b30000000000000000, sarranid_face_older_2],
  ["knight_6_31", "Zalib", "Zalib", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x00000006b800720d5ad4adab306eb6da00000000001d286b0000000000000000, sarranid_face_middle_2],
  ["knight_6_32", "Zefir", "Zefir", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x00000009240c41cc6889a9a2b2ca4cb400000000001de95b0000000000000000, sarranid_face_old_2],
  ["knight_6_33", "Radem", "Radem", tf_hero, 0, reserved,  fac_kingdom_6, [],       knight_attrib_0,wp(90),knight_skills_0, 0x000000042c0c61853be330c69cc0a32300000000001ce9190000000000000000, sarranid_face_older_2],
  ["knight_6_34", "Waldin", "Waldin", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x0000000bc30462922724adb8ab92b11200000000001c97140000000000000000, sarranid_face_older_2],
  ["knight_6_35", "Bolfir", "Bolfir", tf_hero, 0, reserved,  fac_kingdom_6, [],       knight_attrib_0,wp(90),knight_skills_0, 0x0000000cca0444d126d64d1b1e915ce400000000001cbb630000000000000000, sarranid_face_older_2],
  # ["knight_6_36", "Nehelez", "Nehelez", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x000000056b0072d314e35ab91771995500000000001ec7220000000000000000, sarranid_face_middle_2],
  # ["knight_6_37", "Ohedin", "Ohedin", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x0000000bce0441cd4d5386bb723555a300000000001e32650000000000000000, sarranid_face_old_2],
  # ["knight_6_38", "Joslin", "Joslin", tf_hero, 0, reserved,  fac_kingdom_6, [],  knight_attrib_0,wp(90),knight_skills_0, 0x000000073a00751012e3d11ce5123ad300000000001d3cca0000000000000000, sarranid_face_older_2],
  # ["knight_6_39", "Shakmi", "Shakmi", tf_hero, 0, reserved,  fac_kingdom_6, [],       knight_attrib_0,wp(90),knight_skills_0, 0x000000026400404d43a3c6591d665cf600000000001eb7950000000000000000, sarranid_face_older_2],
  # ["knight_6_40", "Dulya", "Dulya", tf_hero, 0, reserved,  fac_kingdom_6, [],       knight_attrib_0,wp(90),knight_skills_0, 0x0000000d6810750b5372c138dcd1472200000000001cc5120000000000000000, sarranid_face_older_2],

  ["knight_9_1", "Saliz", "Saliz", tf_hero, 0, reserved, fac_kingdom_9,     [itm_steppe_horse, itm_leather_boots, itm_leather_gloves, itm_tribal_warrior_outfit, itm_nomad_bow, itm_khergit_arrows, itm_khergit_arrows, itm_sword_khergit_2], knight_attrib_1,wp(120),knight_skills_1, 0x00000001a30c31cf5d736b4ca251a46200000000001439720000000000000000, man_face_middle_1],
  ["knight_9_2", "Pshidal", "Pshidal", tf_hero, 0, reserved, fac_kingdom_9, [itm_steppe_horse, itm_leather_boots, itm_leather_gloves, itm_nomad_robe, itm_spiked_helmet, itm_nomad_bow, itm_khergit_arrows, itm_sword_khergit_2, itm_tab_shield_small_round_a], knight_attrib_1,wp(120),knight_skills_1, 0x000000080b106009239c5162dc953af300000000001dd89b0000000000000000, man_face_middle_1],
  ["knight_9_3", "Nayoz", "Nayoz", tf_hero, 0, reserved, fac_kingdom_9,     [], knight_attrib_0,wp(90),knight_skills_0, 0x000000019d0440483395c1c9486dd70c000000000012396e0000000000000000, man_face_middle_1],
  ["knight_9_4", "Lubnia", "Lubnia", tf_hero, 0, reserved, fac_kingdom_9,   [], knight_attrib_0,wp(90),knight_skills_0, 0x00000001b20421cb334c9576567328f300000000000c9b6a0000000000000000, man_face_middle_1],
  ["knight_9_5", "Olz", "Olz", tf_hero, 0, reserved, fac_kingdom_9,         [], knight_attrib_0,wp(90),knight_skills_0, 0x00000001b40c43536b8b4a64ed69529a00000000001da88d0000000000000000, man_face_middle_1],
  ["knight_9_6", "Papriol", "Papriol", tf_hero, 0, reserved, fac_kingdom_9, [], knight_attrib_0,wp(90),knight_skills_0, 0x00000001ae0442ca295d6ea765c5255c00000000001e22dc0000000000000000, man_face_middle_1],
  ["knight_9_7", "Golag", "Golag", tf_hero, 0, reserved,  fac_kingdom_9,    [],    knight_attrib_0,wp(90),knight_skills_0, 0x00000005d60c620c2d2369c7d271d72e00000000001e28da0000000000000000, man_face_middle_1],
  ["knight_9_8", "Herei", "Herei", tf_hero, 0, reserved,  fac_kingdom_9,    [],    knight_attrib_0,wp(90),knight_skills_0, 0x000000049410414b36d98c47154a576500000000001dbcdd0000000000000000, man_face_middle_1],
  
  ["knight_10_1", "Quip", "Quip", tf_hero, 0, reserved, fac_kingdom_10,           [itm_pack_horse, itm_leather_boots, itm_leather_gloves, itm_mail_hauberk, itm_linen_tunic, itm_mail_coif,  itm_military_pick, itm_tab_shield_heater_cav_a], knight_attrib_1,wp(120),knight_skills_1, 0x000000096a00224d371e1198a38cc449000000000009392e0000000000000000, man_face_middle_1],
  ["knight_10_2", "Falmender", "Falmender", tf_hero, 0, reserved, fac_kingdom_10, [itm_hunter,     itm_leather_boots, itm_mail_chausses, itm_leather_gloves, itm_mail_hauberk, itm_fur_coat,    itm_kettle_hat, itm_lance,   itm_sword_medieval_b, itm_tab_shield_heater_cav_a], knight_attrib_3,wp(180),knight_skills_3, 0x00000002031022d2368a6eab1354d8d500000000001d15140000000000000000, man_face_middle_1],
  ["knight_10_3", "Thern", "Thern", tf_hero, 0, reserved, fac_kingdom_10,     [itm_mail_chausses, itm_leather_boots, itm_leather_gloves, itm_mail_and_plate, itm_kettle_hat, itm_long_hafted_knobbed_mace, itm_tabard], knight_attrib_1,wp(120),knight_skills_1, 0x00000001b41021ce37b471d71b5aa2db0000000000113b2c0000000000000000, man_face_middle_1],
  ["knight_10_4", "Jalaman", "Jalaman", tf_hero, 0, reserved, fac_kingdom_10, [], knight_attrib_0,wp(90),knight_skills_0, 0x00000001bc08020329344a5ae58cb79500000000001248d50000000000000000, man_face_middle_1],
  ["knight_10_5", "Karn", "Karn", tf_hero, 0, reserved, fac_kingdom_10,       [], knight_attrib_0,wp(90),knight_skills_0, 0x000000018408040c298953369389e6f300000000001522ca0000000000000000, man_face_middle_1],
  ["knight_10_6", "Holmun", "Holmun", tf_hero, 0, reserved, fac_kingdom_10,   [], knight_attrib_0,wp(90),knight_skills_0, 0x0000000970103484164b4d78dd5942cd00000000000e44e10000000000000000, man_face_middle_1],
  ["knight_10_7", "Reint", "Reint", tf_hero, 0, reserved,  fac_kingdom_10, [],    knight_attrib_0,wp(90),knight_skills_0, 0x00000009ba0813d0495aa32aad791b1c00000000001d29130000000000000000, man_face_middle_1],
  ["knight_10_8", "Ivon", "Ivon", tf_hero, 0, reserved,  fac_kingdom_10, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000001480430c41899c93591adb94b00000000001e36a40000000000000000, man_face_middle_1],
  ["knight_10_9", "Adot", "Adot", tf_hero, 0, reserved,  fac_kingdom_10, [],      knight_attrib_0,wp(90),knight_skills_0, 0x00000003dd0c04044cda6db515ae286400000000001cbced0000000000000000, swadian_face_young_2],

 
  ["knight_11_1", "Tont", "Tont", tf_hero, 0, reserved,  fac_kingdom_11, [itm_pack_horse, itm_leather_boots, itm_leather_gloves, itm_byrnie, itm_linen_tunic, itm_kettle_hat, itm_sword_medieval_b, itm_tab_shield_heater_cav_a, itm_steel_bolts, itm_light_crossbow],       knight_attrib_1,wp(120),knight_skills_1, 0x00000008560c32934e63713b1d51549400000000001e469a0000000000000000, rhodok_face_middle_2],
  ["knight_11_2", "Soxi", "Soxi", tf_hero, 0, reserved,  fac_kingdom_11, [itm_mail_chausses, itm_wrapping_boots, itm_leather_gloves, itm_byrnie, itm_green_tunic, itm_mail_coif, itm_sledgehammer, itm_heavy_crossbow, itm_bolts],       knight_attrib_1,wp(120),knight_skills_1, 0x000000074704628d5c8cae4aa6aeb4a400000000001746e10000000000000000, rhodok_face_old_2],
  ["knight_11_3", "Mandavir", "Mandavir", tf_hero, 0, reserved,  fac_kingdom_11, [],       knight_attrib_0,wp(90),knight_skills_0, 0x0000000c71002146071a6cd6da6cb8a600000000001d46c10000000000000000, rhodok_face_older_2],
  ["knight_11_4", "Chalbau", "Chalbau", tf_hero, 0, reserved,  fac_kingdom_11, [],       knight_attrib_0,wp(90),knight_skills_0, 0x0000000d2000404e23229134536609e300000000000dd6930000000000000000, rhodok_face_older_2],
  ["knight_11_5", "Tillman", "Tillman", tf_hero, 0, reserved,  fac_kingdom_11, [],   knight_attrib_0,wp(90),knight_skills_0, 0x00000008f90445442ae051489d6bb8a200000000000dd90c0000000000000000, rhodok_face_older_2],
  ["knight_11_6", "Caenlin", "Caenlin", tf_hero, 0, reserved,  fac_kingdom_11, [],       knight_attrib_0,wp(90),knight_skills_0, 0x0000000b6608354736f273671a76277300000000001d48ca0000000000000000, rhodok_face_older_2],
  ["knight_11_7", "Lisd", "Lisd", tf_hero, 0, reserved,  fac_kingdom_11, [],       knight_attrib_0,wp(90),knight_skills_0, 0x0000000380044490664475d86276a99400000000001db75a0000000000000000, rhodok_face_older_2],
  ["knight_11_8", "Hondmall", "Hondmall", tf_hero, 0, reserved,  fac_kingdom_11, [],   knight_attrib_0,wp(90),knight_skills_0, 0x000000060a083446369d6a3b2b6ee32200000000001f14dc0000000000000000, rhodok_face_older_2],

  ["knight_7_1", "Knight Cill", "Cill", tf_hero, 0, reserved, fac_neutral, [], knight_attrib_0,wp(90),knight_skills_0, 0x00000001ae0012ce1a0db6c2e389b8da0000000000054a730000000000000000, man_face_middle_1],
  ["knight_7_2", "Knight Dullbert", "Dullbert", tf_hero, 0, reserved, fac_neutral, [], knight_attrib_0,wp(90),knight_skills_0, 0x000000019e1040c866db3598918b546000000000000e275d0000000000000000, man_face_middle_1],
  ["knight_7_3", "Knight Chool", "Chool", tf_hero, 0, reserved, fac_neutral, [], knight_attrib_0,wp(90),knight_skills_0, 0x000000019e04718b18ddba6ba10dc78b000000000019d95a0000000000000000, man_face_middle_1],
  ["knight_7_4", "Knight Tyra", "Tyra", tf_hero, 0, reserved, fac_neutral, [], knight_attrib_0,wp(90),knight_skills_0, 0x00000007f00c02d2569c892c9e8d595500000000001e92d20000000000000000, man_face_middle_1],
  ["knight_7_5", "Grace", "Grace", tf_hero|tf_female, 0, reserved, fac_neutral, [], knight_attrib_0,wp(90),knight_skills_0, 0x00000000bb0c10054ac98d64ec71299a00000000001db8d40000000000000000, woman_face_1],
  
  
  ["adventurer_01", "Adventurer_01", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x000000045a0c2203352c7a99d4911b5400000000001d4b540000000000000000],
  ["adventurer_02", "Adventurer_02", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x00000001bc00504622e1cad36c4646f500000000000dc7560000000000000000],
  ["adventurer_03", "Adventurer_03", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x000000018108400b16cbb145a27237a200000000001a571c0000000000000000],
  ["adventurer_04", "Adventurer_04", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x000000018c08008a1a655644e46de66300000000000aa3940000000000000000],
  ["adventurer_05", "Adventurer_05", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x000000099d1050cd04db6e391493653200000000001d56da0000000000000000],
  ["adventurer_06", "Adventurer_06", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x000000055f0463ca59629e47756a606e00000000001d96910000000000000000],
  ["adventurer_07", "Adventurer_07", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x00000005750861934a9c9b44c30b5aec000000000005cc5f0000000000000000],
  ["adventurer_08", "Adventurer_08", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x0000000bde0805c4275a423bc995f7f200000000001d35610000000000000000],
  ["adventurer_09", "Adventurer_09", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x00000002d008534d4924710b1b6d59240000000000164cb20000000000000000],
  ["adventurer_10", "Adventurer_10", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x00000002d20c4409792356256e893961000000000011b8e20000000000000000],
  ["adventurer_11", "Adventurer_11", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x000000047c041290172eaa7469c54ae500000000001d230c0000000000000000],
  ["adventurer_12", "Adventurer_12", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x0000000bc00431cc32952ae6dab5696300000000001e48a60000000000000000],
  ["adventurer_13", "Adventurer_13", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x00000008cb1061c136ddcdb774ed595c00000000001de4cc0000000000000000],
  ["adventurer_14", "Adventurer_14", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x0000000b8a00124364e46e1a9290b9a400000000001db8640000000000000000],
  ["adventurer_15", "Adventurer_15", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x0000000a1f04638426e381ab1c713b1c00000000001dc8da0000000000000000],
  ["adventurer_16", "Adventurer_16", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [],
   def_attrib|level(30), wp(10),knows_common, 0x00000005620862d2489dd8b75c96e78d00000000001db71d0000000000000000],
  ["adventurer_17", "Adventurer_17", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x00000004760443033b5472b753b5dadb0000000000132ca90000000000000000],
  ["adventurer_18", "Adventurer_18", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x000000022e00251446636d83648ecae600000000001f4b5b0000000000000000],
  ["adventurer_19", "Adventurer_19", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x000000020d00144a37aa712564573b1200000000001749630000000000000000],
  ["adventurer_20", "Adventurer_20", "Adventurer_01", tf_hero, 0, reserved, fac_neutral_4, [], 
   def_attrib|level(30), wp(10),knows_common, 0x000000083810454d3a6cf2292539cceb00000000001f64950000000000000000],
  
  ["kingdom_1_pretender", "Lady Isolla of Suno",		"Isolla", tf_hero|tf_female|tf_unmoveable_in_party_window|tf_mounted, 	0,reserved,  fac_kingdom_1,[itm_charger,			itm_rich_outfit,	itm_blue_hose,		itm_coat_of_plates_red,	itm_iron_greaves,		itm_gauntlets,			itm_great_helmet,			itm_sword_medieval_c_long,itm_light_crossbow,itm_steel_bolts,	itm_tab_shield_heater_cav_b],		king_attrib,wp(220),king_skills, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent

  ["kingdom_2_pretender", "Prince Valdym the Bastard",	"Valdym", tf_hero|tf_unmoveable_in_party_window|tf_mounted, 			0,reserved,  fac_kingdom_2,[itm_warhorse,			itm_courtly_outfit,	itm_leather_boots,	itm_lamellar_armor,		itm_iron_greaves,		itm_scale_gauntlets,	itm_vaegir_war_helmet,		itm_scimitar_b,itm_war_bow,itm_bodkin_arrows,					itm_tab_shield_kite_cav_b],			king_attrib,wp(220),king_skills, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
#had his patrimony falsified

  ["kingdom_3_pretender", "Dustum Khan",				"Dustum", tf_hero|tf_unmoveable_in_party_window|tf_mounted, 			0,reserved,  fac_kingdom_3,[itm_warhorse_steppe,	itm_nomad_robe,		itm_leather_boots,	itm_khergit_guard_armor,itm_splinted_greaves,	itm_lamellar_gauntlets,	itm_khergit_guard_helmet,	itm_hafted_blade_a,itm_jarid,itm_jarid,							itm_tab_shield_small_round_c],		king_attrib,wp(220),king_skills, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],
#of the family

  ["kingdom_4_pretender", "Lethwin Far-Seeker",			"Lethwin",tf_hero|tf_unmoveable_in_party_window, 						0,reserved,  fac_kingdom_4,[						itm_tabard,			itm_leather_boots,	itm_banded_armor,		itm_iron_greaves,		itm_gauntlets,			itm_nordic_warlord_helmet,	itm_long_axe_c,itm_long_bow,itm_bodkin_arrows,					itm_tab_shield_round_e],			king_attrib,wp(220),king_skills, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#dispossessed and wronged

  ["kingdom_5_pretender", "Lord Kastor of Veluca",		"Kastor", tf_hero|tf_unmoveable_in_party_window|tf_mounted, 			0,reserved,  fac_kingdom_5,[itm_warhorse,			itm_nobleman_outfit,itm_leather_boots,	itm_coat_of_plates,		itm_iron_greaves,		itm_gauntlets,			itm_bascinet_3,				itm_warhammer,itm_heavy_lance,									itm_tab_shield_heater_cav_b],		king_attrib,wp(220),king_skills, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
#republican

  ["kingdom_6_pretender", "Arwa the Pearled One",		"Arwa",   tf_hero|tf_female|tf_unmoveable_in_party_window|tf_mounted, 	0,reserved,  fac_kingdom_6,[itm_warhorse_sarranid, 											itm_mamluke_mail,		itm_sarranid_boots_d,	itm_scale_gauntlets,	itm_sarranid_veiled_helmet,	itm_sarranid_cavalry_sword,										itm_tab_shield_small_round_c],		king_attrib,wp(220),king_skills, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],

##  ["kingdom_1_lord_a", "Kingdom 1 Lord A", "Kingdom 1 Lord A", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_b", "Kingdom 1 Lord B", "Kingdom 1 Lord B", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_c", "Kingdom 1 Lord C", "Kingdom 1 Lord C", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_d", "Kingdom 1 Lord D", "Kingdom 1 Lord D", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_e", "Kingdom 1 Lord E", "Kingdom 1 Lord E", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_f", "Kingdom 1 Lord F", "Kingdom 1 Lord F", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_g", "Kingdom 1 Lord G", "Kingdom 1 Lord G", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_h", "Kingdom 1 Lord H", "Kingdom 1 Lord H", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_i", "Kingdom 1 Lord I", "Kingdom 1 Lord I", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_j", "Kingdom 1 Lord J", "Kingdom 1 Lord J", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_k", "Kingdom 1 Lord K", "Kingdom 1 Lord K", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_l", "Kingdom 1 Lord L", "Kingdom 1 Lord L", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_m", "Kingdom 1 Lord M", "Kingdom 1 Lord M", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_n", "Kingdom 1 Lord N", "Kingdom 1 Lord N", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],



#  ["town_1_ruler_a", "King Harlaus",  "King Harlaus",  tf_hero, scn_town_1_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010908101e36db44b75b6dd],
#  ["town_2_ruler_a", "Duke Taugard",  "Duke Taugard",  tf_hero, scn_town_2_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000310401e06db86375f6da],
#  ["town_3_ruler_a", "Count Grimar",  "Count Grimar",  tf_hero, scn_town_3_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004430301e46136eb75bc0a],
#  ["town_4_ruler_a", "Count Haxalye", "Count Haxalye", tf_hero, scn_town_4_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010918701e77136e905bc0e
#  ["town_5_ruler_a", "Count Belicha", "Count Belicha", tf_hero, scn_town_5_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000421c801e7713729c5b8ce],
#  ["town_6_ruler_a", "Count Nourbis", "Count Nourbis", tf_hero, scn_town_6_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c640501e371b72bcdb724],
#  ["town_7_ruler_a", "Count Rhudolg", "Count Rhudolg", tf_hero, scn_town_7_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c710201fa51b7286db721],
 
#  ["town_8_ruler_b", "King Yaroglek", "King_yaroglek", tf_hero, scn_town_8_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000128801f294ca6d66d555],
#  ["town_9_ruler_b", "Count Aolbrug", "Count_Aolbrug", tf_hero, scn_town_9_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004234401f26a271c8d38ea],
#  ["town_10_ruler_b","Count Rasevas", "Count_Rasevas", tf_hero, scn_town_10_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000001032c201f38e269372471c],
#  ["town_11_ruler_b","Count Leomir",  "Count_Leomir",  tf_hero, scn_town_11_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c538001f55148936d3895],
#  ["town_12_ruler_b","Count Haelbrad","Count_Haelbrad",tf_hero, scn_town_12_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000410c701f38598ac8aaaab],
#  ["town_13_ruler_b","Count Mira",    "Count_Mira",    tf_hero, scn_town_13_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004204401f390c515555594],
#  ["town_14_ruler_b","Count Camechaw","Count_Camechaw",tf_hero, scn_town_14_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

##  ["kingdom_2_lord_a", "Kingdom 2 Lord A", "Kingdom 2 Lord A", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_b", "Kingdom 2 Lord B", "Kingdom 2 Lord B", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_c", "Kingdom 2 Lord C", "Kingdom 2 Lord C", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_d", "Kingdom 2 Lord D", "Kingdom 2 Lord D", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_e", "Kingdom 2 Lord E", "Kingdom 2 Lord E", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_f", "Kingdom 2 Lord F", "Kingdom 2 Lord F", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_g", "Kingdom 2 Lord G", "Kingdom 2 Lord G", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_h", "Kingdom 2 Lord H", "Kingdom 2 Lord H", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_i", "Kingdom 2 Lord I", "Kingdom 2 Lord I", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_j", "Kingdom 2 Lord J", "Kingdom 2 Lord J", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_k", "Kingdom 2 Lord K", "Kingdom 2 Lord K", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_l", "Kingdom 2 Lord L", "Kingdom 2 Lord L", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_m", "Kingdom 2 Lord M", "Kingdom 2 Lord M", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_n", "Kingdom 2 Lord N", "Kingdom 2 Lord N", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],



#Royal family members

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Swadian ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_lady_1","Lady Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [          itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_2","Lady Nelda","Nelda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["knight_1_lady_3","Lady Bela","Bela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["knight_1_lady_4","Lady Elina","Elina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_l_lady_5","Lady Constanis","Constanis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_6","Lady Vera","Vera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_1_lady_7","Lady Auberina","Auberina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_8","Lady Tibal","Tibal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_1_lady_9","Lady Magar","Magar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_10","Lady Thedosa","Thedosa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_11","Lady Melisar","Melisar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_12","Lady Irena","Irena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_l_lady_13","Lady Philenna","Philenna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_14","Lady Sonadel","Sonadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_1_lady_15","Lady Boadila","Boadila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_16","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_1_lady_17","Lady Johana","Johana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_1_lady_18","Lady Bernatys","Bernatys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_1_lady_19","Lady Enricata","Enricata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_1_lady_20","Lady Gaeta","Gaeta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  
  #Vaegir ladies
  ["kingdom_2_lady_1","Lady Junitha","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_2","Lady Katia","Katia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_3","Lady Seomis","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_4","Lady Drina","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_5","Lady Nesha","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_6","Lady Tabath","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_7","Lady Pelaeka","Pelaeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_8","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_9","Lady Vayen","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_10","Lady Joaka","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_11","Lady Tejina","Tejina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_12","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_13","Lady Myntha","Myntha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_14","Lady Akilina","Akilina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_15","Lady Sepana","Sepana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_16","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


  ["kingdom_3_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_2","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_6","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_8","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_3_lady_10","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_11","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_3_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_14","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_16","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  
  
  
  ["kingdom_4_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_1","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_1","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2c_daughter_2","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["knight_4_1b_wife_2","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1b_daughter","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1c_daughter","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],


  ["kingdom_5_lady_1","Lady Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_2","Lady Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_4","Lady Reada","Reada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_5_wife","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_5_2b_wife_1","Lady Baotheia","Baotheia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
  ["kingdom_5_1c_daughter_1","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_1","Lady Meraced","Meraced",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_1","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_1","Lady Calantina","Calantina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_2","Lady Forbesa","Forbesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_2","Lady Claudora","Claudora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1b_wife","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2b_wife_2","Lady Miraeia","Miraeia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_3","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_2","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_2","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_4","Lady Ellian","Ellian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  
#Sarranid ladies
  ["kingdom_6_lady_1","Lady Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_6_lady_2","Lady Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_6_lady_3","Lady Sulaha","Sulaha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_6_lady_4","Lady Shatha","Shatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_6_lady_5","Lady Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_6","Lady Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_6_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_6_lady_9","Lady Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_10","Lady Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_6_lady_11","Lady Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_12","Lady Ruwa","Ruwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_6_lady_13","Lady Luqa","Luqa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_14","Lady Zandina","Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_6_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_16","Lady Zahara","Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_6_lady_17","Lady Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_6_lady_18","Lady Khalisa","Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_6_lady_19","Lady Janab","Janab",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_6_lady_20","Lady Sur","Sur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],



  
#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],


#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,         itm_leather_boots,          itm_straw_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,       itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,          itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_leather,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,       itm_light_leather,          itm_leather_boots,          itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_leather,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_leather,         itm_woolen_hose,            itm_fur_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],

  
#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],

  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_49_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_50_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_51_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_52_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

#Arena Masters
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_nomad_armor,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_nomad_armor,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],



# Underground 

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_hide_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_red_gambeson,       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_woolen_dress,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##  
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jacket,     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_blue_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_blue_gambeson,     itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_woolen_dress,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_leather,       itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,     itm_nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,   itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,     itm_wrapping_boots,itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_sarranid_dress_a,        itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe,       itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,        itm_sarranid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe_b,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],

#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_nomad_armor,   itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woolen_dress,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_sarranid_common_dress_b,  itm_sarranid_boots_a, itm_sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron, itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],

# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nomad_armor,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_woolen_hose,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_woolen_hose],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_sarranid_boots_a],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe,      itm_sarranid_boots_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe_b,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_blue_hose,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],


#Town Mayors    #itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_gambeson,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_fur_coat,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_rich_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_red_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_fur_coat,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,     itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,       itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,    itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],


#Village stores
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_111_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_112_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_113_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_114_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
  
  
  
# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_armor,itm_strange_short_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_boots,itm_strange_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_helmet,itm_strange_great_sword],def_attrib|level(18),wp(60),knows_common, 0],

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],  
  
# These are used as arrays in the scripts.
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point  

  ["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_medieval_b, itm_throwing_daggers],
   def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2],
   
  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_8|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,    bandit_face1, bandit_face2],

  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

   
   
  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_viking_1,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],
   
  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],

  ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_robe, itm_black_hood, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],   
  ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_rich_outfit, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],   
   
   
##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_leather_jacket,itm_hide_boots, itm_saddle_horse, itm_leather_jacket, itm_leather_cap],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_dagger,itm_hunting_crossbow,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],


  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_nomad_boots, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],
  
  
#Multiplayer ai troops
  ["swadian_crossbowman_multiplayer_ai","Skirmisher","Skirmishers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_bolts,itm_steel_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_hunting_bow,itm_short_bow,itm_arrows_b,itm_barbed_arrows,itm_bodkin_arrows,itm_sword_medieval_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_fighting_pick,itm_tab_shield_heater_a,itm_tab_shield_heater_b,itm_tab_shield_heater_c,
    itm_red_shirt,itm_padded_cloth,itm_leather_armor,itm_red_gambeson,itm_ankle_boots,itm_leather_boots,itm_arming_cap,itm_norman_helmet,itm_helmet_with_neckguard,itm_kettle_hat,itm_leather_gloves],
   str_11|agi_14|int_4|cha_4|level(14),wpex(85,80,75,105,100,20),knows_common|knows_ironflesh_2|knows_athletics_4|knows_shield_2|knows_power_strike_1|knows_power_draw_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer_ai","Infantry","Infantry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_awlpike,itm_awlpike_long,itm_bastard_sword_a,itm_bastard_sword_b,itm_sword_two_handed_a,itm_sword_medieval_c,itm_sword_medieval_c_small,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_tab_shield_heater_c,itm_tab_shield_heater_b,itm_tab_shield_heater_a,itm_tab_shield_heater_d,
    itm_red_tunic,itm_red_gambeson,itm_leather_armor,itm_padded_cloth,itm_haubergeon,itm_ankle_boots,itm_leather_gloves,itm_mail_chausses,itm_leather_boots,itm_arming_cap,itm_norman_helmet,itm_helmet_with_neckguard,itm_flat_topped_helmet,itm_mail_coif,itm_leather_gloves],
   str_16|agi_12|int_4|cha_4|level(17),wpex(115,120,110,20,20,90),knows_common|knows_ironflesh_3|knows_athletics_1|knows_power_strike_2|knows_shield_3|knows_power_throw_1|knows_riding_5,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai","Man at Arms","Men at Arms",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_light_lance,itm_lance,itm_sword_medieval_a,itm_sword_medieval_b,itm_sword_medieval_c,itm_bastard_sword_a,itm_bastard_sword_b,itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_b,
    itm_red_tunic,itm_padded_cloth,itm_red_gambeson,itm_leather_armor,itm_haubergeon,itm_mail_with_surcoat,itm_ankle_boots,itm_leather_boots,itm_mail_chausses,itm_arming_cap,itm_norman_helmet,itm_helmet_with_neckguard,itm_flat_topped_helmet,itm_leather_gloves,itm_saddle_horse,itm_courser,itm_hunter,itm_pack_horse],
   str_15|agi_12|int_4|cha_4|level(16),wpex(110,100,115,20,20,85),knows_common|knows_riding_4|knows_ironflesh_4|knows_shield_3|knows_power_strike_3|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer_ai","Ijasz","Ijaszok",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_bodkin_arrows,itm_barbed_arrows,itm_scimitar,itm_mace_2,itm_mace_1,itm_strong_bow,itm_nomad_bow,itm_short_bow,
    itm_leather_vest,itm_linen_tunic,itm_leather_boots,itm_nomad_boots,itm_hide_boots,itm_vaegir_fur_helmet,itm_vaegir_fur_helmet,itm_leather_gloves],
   str_9|agi_15|int_4|cha_4|level(13),wpex(75,75,70,100,20,40),knows_common|knows_ironflesh_1|knows_athletics_5|knows_shield_1|knows_power_draw_5,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer_ai","Harcos","Harcosok",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_studded_leather_coat,itm_leather_jerkin,itm_leather_vest,itm_linen_tunic,itm_leather_boots,itm_nomad_boots,itm_hide_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_leather_gloves,
    itm_war_spear,itm_spear, itm_tab_shield_kite_c,itm_tab_shield_kite_b,itm_tab_shield_kite_a, itm_scimitar,itm_battle_axe],
   str_15|agi_14|int_4|cha_4|level(18),wpex(110,115,105,20,10,100),knows_common|knows_ironflesh_3|knows_athletics_5|knows_power_strike_4|knows_shield_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai","Nehezlovassag","Nehezlovassag",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_scimitar,itm_lance,itm_light_lance,itm_tab_shield_kite_cav_a,
    itm_lamellar_vest,itm_studded_leather_coat,itm_leather_jerkin,itm_leather_vest,itm_linen_tunic,itm_leather_boots,itm_nomad_boots,itm_hide_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_leather_gloves,itm_steppe_horse,itm_hunter,itm_pack_horse,itm_courser,itm_saddle_horse],
   str_14|agi_14|int_4|cha_4|level(17),wpex(100,105,105,20,10,100),knows_common|knows_ironflesh_2|knows_athletics_2|knows_power_strike_2|knows_shield_3|knows_power_throw_2|knows_riding_5,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_ai","Dismounted Lancer","Dismounted Lancer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_sword_khergit_1,itm_winged_mace,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,
    itm_spiked_helmet,itm_khergit_war_helmet,itm_steppe_cap,itm_leather_steppe_cap_b,itm_leather_steppe_cap_a,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_steppe_armor,itm_coarse_tunic,itm_leather_boots,itm_nomad_boots,itm_hide_boots,itm_leather_gloves],
   str_15|agi_15|int_4|cha_4|level(19),wpex(100,100,120,20,10,120),knows_common|knows_ironflesh_2|knows_athletics_4|knows_power_strike_3|knows_shield_3|knows_power_throw_3,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer_ai","Horse Archer","Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_khergit_bow,itm_nomad_bow,itm_short_bow,itm_hunting_bow,itm_khergit_arrows,itm_bodkin_arrows,itm_barbed_arrows,itm_tab_shield_small_round_a,
    itm_tribal_warrior_outfit,itm_steppe_armor,itm_coarse_tunic,itm_leather_boots,itm_nomad_boots,itm_hide_boots,itm_leather_gloves,itm_steppe_horse],
   str_10|agi_16|int_4|cha_4|level(15),wpex(75,70,70,95,20,70),knows_common|knows_athletics_2|knows_shield_2|knows_power_draw_4|knows_power_throw_1|knows_riding_5|knows_horse_archery_4,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai","Lancer","Lancers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_sword_khergit_3,itm_sword_khergit_2,itm_sword_khergit_1,itm_lance,itm_light_lance,itm_hafted_blade_b,itm_tab_shield_small_round_c,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_steppe_cap,itm_leather_steppe_cap_b,itm_leather_steppe_cap_a,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_steppe_armor,itm_coarse_tunic,itm_splinted_greaves,itm_leather_boots,itm_nomad_boots,itm_hide_boots,itm_leather_gloves,itm_hunter,itm_courser,itm_steppe_horse],
   str_15|agi_15|int_4|cha_4|level(19),wpex(100,100,120,20,10,120),knows_common|knows_ironflesh_2|knows_athletics_4|knows_power_strike_2|knows_shield_3|knows_power_throw_3|knows_riding_6|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["nord_veteran_multiplayer_ai","Warrior","Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_one_handed_battle_axe_b,itm_one_handed_battle_axe_a,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_tab_shield_round_d,itm_tab_shield_round_c,itm_tab_shield_round_b,itm_tab_shield_round_a,itm_throwing_axes,itm_light_throwing_axes,itm_sword_viking_2,itm_sword_viking_2_small,itm_sword_viking_1,itm_long_axe,itm_two_handed_battle_axe_2,itm_two_handed_axe,
    itm_nordic_huscarl_helmet,itm_nordic_fighter_helmet,itm_nordic_footman_helmet,itm_nordic_veteran_archer_helmet,itm_mail_shirt,itm_byrnie,itm_leather_jerkin,itm_blue_tunic,itm_splinted_leather_greaves,itm_leather_boots,itm_hide_boots,itm_leather_gloves],
   str_16|agi_15|int_4|cha_4|level(20),wpex(120,120,105,20,10,130),knows_common|knows_ironflesh_4|knows_athletics_6|knows_power_strike_5|knows_shield_5|knows_power_throw_4,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai","Mounted Warrior","Mounted Warriors",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_light_throwing_axes,itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_sword_viking_2,itm_sword_viking_1,itm_two_handed_axe,itm_tab_shield_round_b,itm_tab_shield_round_a,
    itm_nordic_footman_helmet,itm_nordic_veteran_archer_helmet,itm_nordic_archer_helmet,itm_leather_jerkin,itm_blue_tunic,itm_leather_boots,itm_hide_boots,itm_leather_gloves,itm_sumpter_horse,itm_saddle_horse],
   str_11|agi_12|int_4|cha_4|level(12),wpex(95,100,85,20,10,105),knows_common|knows_ironflesh_3|knows_athletics_3|knows_power_strike_3|knows_shield_3|knows_power_throw_3|knows_riding_3|knows_horse_archery_2,nord_face_young_1, nord_face_older_2],
  ["nord_archer_multiplayer_ai","Longbowman","Longbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_4,
   [itm_barbed_arrows,itm_arrows_b,itm_sword_viking_1,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_a,itm_long_bow,itm_short_bow,
    itm_leather_jerkin,itm_blue_tunic,itm_leather_boots,itm_hide_boots,itm_nordic_archer_helmet,itm_leather_gloves],
   str_12|agi_12|int_4|cha_4|level(13),wpex(90,90,80,95,20,20),knows_common|knows_ironflesh_2|knows_athletics_3|knows_power_strike_2|knows_shield_1|knows_power_draw_6,nord_face_young_1, nord_face_old_2],
  ["rhodok_veteran_crossbowman_multiplayer_ai","Crossbowman","Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_military_sickle_a,itm_fighting_pick,itm_club_with_spike_head,itm_sword_medieval_a,itm_tab_shield_pavise_b,itm_tab_shield_pavise_a,itm_heavy_crossbow,itm_crossbow,itm_steel_bolts,itm_bolts,
    itm_kettle_hat,itm_mail_coif,itm_footman_helmet,itm_padded_coif,itm_leather_cap,itm_aketon_green,itm_leather_armor,itm_tunic_with_green_cape,itm_green_tunic,itm_leather_boots,itm_ankle_boots,itm_wrapping_boots,itm_leather_gloves],
   str_14|agi_10|int_4|cha_4|level(13),wpex(95,85,80,10,100,20),knows_common|knows_ironflesh_3|knows_athletics_2|knows_power_strike_2|knows_shield_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai","Spearman","Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_pike,itm_war_spear,itm_spear,itm_ashwood_pike,itm_military_cleaver_b,itm_military_pick,itm_military_sickle_a,itm_fighting_pick,itm_sword_medieval_b,itm_tab_shield_pavise_c,itm_tab_shield_pavise_b,itm_tab_shield_pavise_a,
    itm_kettle_hat,itm_mail_coif,itm_footman_helmet,itm_padded_coif,itm_leather_cap,itm_byrnie,itm_aketon_green,itm_ragged_outfit,itm_leather_armor,itm_green_tunic,itm_leather_boots,itm_ankle_boots,itm_wrapping_boots,itm_leather_gloves],
   str_16|agi_14|int_4|cha_4|level(19),wpex(110,105,130,10,20,95),knows_common|knows_ironflesh_4|knows_athletics_5|knows_power_strike_4|knows_shield_5|knows_power_throw_1,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Mounted Skirmisher","Mounted Skirmishers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_light_lance,itm_light_crossbow,itm_hunting_crossbow,itm_bolts,itm_sword_medieval_b,itm_sword_medieval_a,itm_fighting_pick,itm_military_sickle_a,itm_club_with_spike_head,
    itm_kettle_hat,itm_mail_coif,itm_footman_helmet,itm_padded_coif,itm_ragged_outfit,itm_aketon_green,itm_leather_armor,itm_green_tunic,itm_leather_boots,itm_ankle_boots,itm_wrapping_boots,itm_leather_gloves,itm_saddle_horse,itm_pack_horse],
   str_12|agi_12|int_4|cha_4|level(13),wpex(100,95,110,10,60,60),knows_common|knows_ironflesh_2|knows_athletics_3|knows_power_strike_2|knows_shield_2|knows_riding_4|knows_horse_archery_3,rhodok_face_young_1, rhodok_face_older_2],
  ["sarranid_infantry_multiplayer_ai","Hajib","Hajib",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
   [itm_arabian_armor_b,itm_sarranid_leather_armor,itm_archers_vest,itm_skirmisher_armor,itm_sarranid_cloth_robe,itm_sarranid_warrior_cap,itm_desert_turban,itm_turban,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_leather_gloves,
    itm_arabian_sword_b,itm_arabian_sword_a,itm_mace_4,itm_mace_3,itm_mace_2,itm_bamboo_spear,itm_tab_shield_kite_c,itm_tab_shield_kite_b,itm_tab_shield_kite_a],
   str_14|agi_16|int_4|cha_4|level(19),wpex(110,100,110,15,10,120),knows_common|knows_ironflesh_2|knows_athletics_7|knows_power_strike_4|knows_shield_3|knows_power_throw_3,sarranid_face_middle_1, sarranid_face_old_2],
  ["sarranid_archer_multiplayer_ai","Ramat","Ramat",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_mace_2,itm_mace_3,itm_jarid,itm_jarid,itm_throwing_spears,itm_javelin,itm_tab_shield_small_round_a,
    itm_archers_vest,itm_skirmisher_armor,itm_sarranid_cloth_robe,itm_sarranid_boots_b,itm_desert_turban,itm_turban,itm_leather_gloves],
   str_11|agi_16|int_4|cha_4|level(16),wpex(90,80,80,15,10,140),knows_common|knows_ironflesh_2|knows_athletics_5|knows_power_strike_2|knows_shield_2|knows_power_throw_5,sarranid_face_young_1, sarranid_face_old_2],
  ["sarranid_horseman_multiplayer_ai","Forsan","Forsan",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_6,
   [itm_bamboo_spear,itm_arabian_sword_b,itm_arabian_sword_a,itm_mace_4,itm_mace_3,itm_mace_2,itm_sarranid_axe_a,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_javelin,
    itm_sarranid_cavalry_robe,itm_sarranid_leather_armor,itm_archers_vest,itm_skirmisher_armor,itm_sarranid_cloth_robe,itm_sarranid_boots_b,itm_sarranid_mail_coif,itm_desert_turban,itm_turban,itm_leather_gloves,itm_arabian_horse_a,itm_arabian_horse_b],
   str_13|agi_15|int_4|cha_4|level(17),wpex(105,95,110,15,10,110),knows_common|knows_ironflesh_1|knows_athletics_4|knows_power_strike_2|knows_shield_3|knows_power_throw_2|knows_riding_6|knows_horse_archery_1,sarranid_face_young_1, sarranid_face_old_2],
  ["freerider_infantry_multiplayer_ai","Heavy Infantry","Heavy Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_10,
   [itm_mail_chausses,itm_leather_boots,itm_mail_hauberk,itm_mail_and_plate,itm_kettle_hat,itm_spiked_helmet,itm_leather_gloves,
    itm_long_hafted_knobbed_mace,itm_long_hafted_spiked_mace],
   str_14|agi_10|int_4|cha_4|level(13),wpex(110,100,130,10,15,100),knows_common|knows_ironflesh_7|knows_athletics_2|knows_power_strike_4|knows_shield_3,man_face_middle_1, man_face_old_2],
  ["freerider_archer_multiplayer_ai","Apprentice","Apprentices",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_10,
   [itm_leather_boots,itm_light_mail_and_plate,itm_leather_gloves,
    itm_sword_medieval_b,itm_cartridges,itm_flintlock_pistol,itm_tab_shield_heater_cav_a],
   str_10|agi_12|int_4|cha_4|level(11),wpex(80,70,70,10,15,20)|wp_firearm(80),knows_common|knows_ironflesh_2|knows_athletics_4|knows_power_strike_1|knows_shield_2,man_face_young_1, man_face_old_2],
  ["freerider_horseman_multiplayer_ai","Heavy Cavalry","Heavy Cavalries",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_10,
   [itm_mail_chausses,itm_leather_boots,itm_mail_and_plate,itm_mail_hauberk,itm_kettle_hat,itm_spiked_helmet,itm_helmet_with_neckguard,itm_leather_gloves,
    itm_lance,itm_sword_medieval_c_long,itm_long_hafted_spiked_mace,itm_cartridges,itm_flintlock_pistol,itm_tab_shield_heater_cav_a,itm_pack_horse,itm_hunter],
   str_13|agi_11|int_4|cha_4|level(13),wpex(100,90,110,10,15,100)|wp_firearm(40),knows_common|knows_ironflesh_3|knows_athletics_1|knows_power_strike_2|knows_shield_3|knows_riding_4|knows_horse_archery_2,man_face_young_1, man_face_old_2],
  ["khergit_t_dismounted_lancer_multiplayer_ai","Dismounted Lancer","Dismounted Lancer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_9,
   [itm_sword_khergit_2,itm_sword_khergit_1,itm_sword_khergit_3,itm_sword_khergit_4,itm_winged_mace,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_tab_shield_small_round_c,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_steppe_cap,itm_leather_steppe_cap_b,itm_leather_steppe_cap_a,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_steppe_armor,itm_coarse_tunic,itm_splinted_greaves,itm_leather_boots,itm_nomad_boots,itm_hide_boots,itm_leather_gloves],
   str_15|agi_15|int_4|cha_4|level(19),	wpex(105,100,115,20,10,115),knows_common|knows_ironflesh_2|	knows_athletics_5|	knows_power_strike_3|	knows_shield_3|	knows_power_throw_3|knows_riding_3,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_t_archer_multiplayer_ai","Archer","Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_9,
   [itm_sword_khergit_1,itm_khergit_bow,itm_nomad_bow,itm_short_bow,itm_hunting_bow,itm_khergit_arrows,itm_bodkin_arrows,itm_barbed_arrows,itm_tab_shield_small_round_a,
    itm_tribal_warrior_outfit,itm_steppe_armor,itm_coarse_tunic,itm_leather_boots,itm_nomad_boots,itm_hide_boots,itm_leather_gloves],
   str_10|agi_16|int_4|cha_4|level(15),wpex(75,70,70,95,20,70),knows_common|knows_athletics_4|knows_shield_2|knows_power_draw_4|knows_riding_3|knows_horse_archery_1|knows_power_throw_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_t_horseman_multiplayer_ai","Horseman","Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_9,
   [itm_hunting_bow,itm_short_bow,itm_barbed_arrows,itm_sword_khergit_2,itm_sword_khergit_1,itm_light_lance,itm_hafted_blade_b,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,
    itm_khergit_war_helmet,itm_steppe_cap,itm_leather_steppe_cap_b,itm_leather_steppe_cap_a,itm_tribal_warrior_outfit,itm_steppe_armor,itm_coarse_tunic,itm_leather_boots,itm_nomad_boots,itm_hide_boots,itm_leather_gloves,itm_courser,itm_steppe_horse],
   str_12|agi_15|int_4|cha_4|level(16),wpex(100,100,120,70,15,90),knows_common|knows_ironflesh_1|knows_athletics_3|knows_power_strike_1|knows_shield_3|knows_power_draw_2|knows_power_throw_2|knows_horse_archery_2|knows_riding_6,khergit_face_middle_1, khergit_face_older_2],

   
   
#Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayer","Skirmisher","Skirmishers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_padded_cloth, itm_leather_boots,
    itm_fighting_pick, itm_short_bow2, itm_barbed_arrows, itm_tab_shield_heater_b],
   str_11|agi_14|int_4|cha_4|level(14),	wpex(85,80,75,130,120,20),	knows_common|knows_ironflesh_2|	knows_athletics_5|	knows_power_strike_1|	knows_shield_2|	knows_power_draw_3,															swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer","Infantry","Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_padded_cloth, itm_leather_boots, itm_mail_coif,
    itm_sword_medieval_b, itm_tab_shield_heater_c],
   str_16|agi_12|int_4|cha_4|level(17),	wpex(115,120,110,20,20,90),	knows_common|knows_ironflesh_6|	knows_athletics_3|	knows_power_strike_4|	knows_shield_4|	knows_power_throw_1,														swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer","Man at Arms","Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_red_tunic, itm_leather_boots,
    itm_sword_medieval_a_long, itm_light_lance, itm_tab_shield_heater_cav_a, itm_saddle_horse],
   str_15|agi_12|int_4|cha_4|level(16),	wpex(110,100,115,20,20,85),	knows_common|knows_ironflesh_3|	knows_athletics_1|	knows_power_strike_2|	knows_shield_3|	knows_power_throw_1|knows_riding_5,											swadian_face_young_1, swadian_face_old_2],

  ["vaegir_archer_multiplayer","Ijasz","Ijaszok",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_leather_vest, itm_hide_boots, itm_vaegir_fur_cap,
    itm_scimitar, itm_nomad_bow, itm_arrows, itm_arrows],
   str_9|agi_15|int_4|cha_4|level(13),	wpex(75,75,70,120,20,40),	knows_common|knows_ironflesh_1|	knows_athletics_5|							knows_shield_1|	knows_power_draw_5,															vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer","Gyalogsag","Gyalogsag",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_leather_jerkin, itm_leather_boots, itm_vaegir_fur_helmet,
    itm_scimitar, itm_tab_shield_kite_c],
   str_15|agi_14|int_4|cha_4|level(18),	wpex(110,115,105,20,10,100),knows_common|knows_ironflesh_3|	knows_athletics_5|	knows_power_strike_4|	knows_shield_3|	knows_power_throw_2,														vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer","Huszar","Huszar",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_linen_tunic, itm_hide_boots,
    itm_scimitar, itm_light_lance, itm_tab_shield_kite_cav_a, itm_saddle_horse],
   str_14|agi_14|int_4|cha_4|level(17),	wpex(100,105,105,20,10,100),knows_common|knows_ironflesh_2|	knows_athletics_2|	knows_power_strike_2|	knows_shield_2|	knows_power_throw_2|knows_riding_5,											vaegir_face_young_1, vaegir_face_older_2],

  ["khergit_veteran_horse_archer_multiplayer","Horse Archer","Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_coarse_tunic, itm_hide_boots, itm_steppe_cap,
    itm_sword_khergit_1, itm_short_bow, itm_arrows_b, itm_arrows_b, itm_steppe_horse],
   str_10|agi_16|int_4|cha_4|level(15),	wpex(75,70,70,115,20,70),	knows_common|					knows_athletics_2|							knows_shield_2|	knows_power_draw_4|knows_power_throw_1|knows_riding_5|knows_horse_archery_4,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer","Lancer","Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_coarse_tunic, itm_hide_boots, itm_leather_steppe_cap_b,
    itm_sword_khergit_1, itm_light_lance, itm_tab_shield_small_round_a, itm_steppe_horse],
   str_15|agi_15|int_4|cha_4|level(19),	wpex(100,100,120,20,10,120),knows_common|knows_ironflesh_2|	knows_athletics_4|	knows_power_strike_2|	knows_shield_3|	knows_power_throw_3|knows_riding_6|knows_horse_archery_1,					khergit_face_middle_1, khergit_face_older_2],

  ["nord_archer_multiplayer","Longbowman","Longbowmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_blue_tunic, itm_hide_boots, itm_nordic_archer_helmet,
    itm_one_handed_war_axe_a, itm_long_bow, itm_arrows_b, itm_arrows_b],
   str_12|agi_12|int_4|cha_4|level(13),	wpex(90,90,80,110,20,20),	knows_common|knows_ironflesh_2|	knows_athletics_2|	knows_power_strike_2|	knows_shield_1|	knows_power_draw_6,															nord_face_young_1, nord_face_old_2],
  ["nord_veteran_multiplayer","Huscarl","Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_leather_jerkin, itm_leather_boots, itm_nordic_footman_helmet,
    itm_one_handed_war_axe_b, itm_tab_shield_round_c],
   str_16|agi_15|int_4|cha_4|level(20),	wpex(120,120,105,20,10,130),knows_common|knows_ironflesh_4|	knows_athletics_6|	knows_power_strike_5|	knows_shield_5|	knows_power_throw_4,														nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer","Mounted Warrior","Mounted Warrior",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_leather_jerkin, itm_leather_boots, itm_nordic_archer_helmet,
    itm_two_handed_axe, itm_one_handed_war_axe_a, itm_tab_shield_round_a, itm_saddle_horse],
   str_11|agi_12|int_4|cha_4|level(12),	wpex(95,100,85,20,10,105),	knows_common|knows_ironflesh_3|	knows_athletics_3|	knows_power_strike_3|	knows_shield_3|	knows_power_throw_3|knows_riding_3|knows_horse_archery_2,					nord_face_young_1, nord_face_older_2],

  ["rhodok_veteran_crossbowman_multiplayer","Crossbowman","Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tunic_with_green_cape, itm_leather_boots, itm_padded_coif, itm_leather_gloves,
    itm_fighting_pick, itm_crossbow, itm_bolts, itm_tab_shield_pavise_b],
   str_14|agi_10|int_4|cha_4|level(13),	wpex(95,85,80,10,120,20),	knows_common|knows_ironflesh_3|	knows_athletics_2|	knows_power_strike_2|	knows_shield_3,																				rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayer","Sergeant","Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_aketon_green, itm_leather_boots, itm_mail_coif,
    itm_sword_medieval_a, itm_war_spear, itm_tab_shield_pavise_b],
   str_16|agi_14|int_4|cha_4|level(19),	wpex(110,105,130,10,20,95),	knows_common|knows_ironflesh_4|	knows_athletics_5|	knows_power_strike_4|	knows_shield_5|	knows_power_throw_1,														rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer","Mounted Skirmisher","Mounted Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_green_tunic, itm_leather_boots, itm_padded_coif,
    itm_fighting_pick, itm_light_lance, itm_tab_shield_pavise_a, itm_pack_horse],
   str_12|agi_12|int_4|cha_4|level(13),	wpex(100,95,110,10,60,60),	knows_common|knows_ironflesh_2|	knows_athletics_3|	knows_power_strike_2|	knows_shield_2|	knows_riding_4|knows_horse_archery_3,										rhodok_face_middle_1, rhodok_face_older_2],

  ["sarranid_archer_multiplayer","Ramat","Ramat",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_skirmisher_armor, itm_sarranid_boots_a, itm_sarranid_warrior_cap, 
    itm_mace_4, itm_javelin, itm_javelin, itm_tab_shield_small_round_a],
   str_11|agi_16|int_4|cha_4|level(16),	wpex(90,80,80,15,10,140),	knows_common|knows_ironflesh_2|	knows_athletics_5|	knows_power_strike_2|	knows_shield_2|	knows_power_throw_5,														sarranid_face_young_1, sarranid_face_older_2],
  ["sarranid_merc_multiplayer","Paighan","Paighan",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_sarranid_cloth_robe_b, itm_sarranid_boots_b, itm_leather_gloves,
    itm_mace_4, itm_short_bow2, itm_barbed_arrows, itm_barbed_arrows],
   str_9|agi_15|int_4|cha_4|level(13),	wpex(70,65,65,80,10,50),	knows_common|knows_ironflesh_1|	knows_athletics_4|							knows_shield_1|	knows_power_draw_3|knows_power_throw_1,										sarranid_face_young_1, sarranid_face_older_2],
  ["sarranid_footman_multiplayer","Hajib","Hajib",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_archers_vest, itm_sarranid_boots_b, itm_sarranid_warrior_cap, itm_leather_gloves,
    itm_arabian_sword_b, itm_tab_shield_kite_c],
   str_14|agi_16|int_4|cha_4|level(19),	wpex(110,100,110,15,10,120),knows_common|knows_ironflesh_2|	knows_athletics_7|	knows_power_strike_4|	knows_shield_3|	knows_power_throw_3,														sarranid_face_young_1, sarranid_face_older_2],
  ["sarranid_mamluke_multiplayer","Mamluk","Mamluk",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_sarranid_cloth_robe, itm_sarranid_boots_b, itm_leather_gloves,
    itm_sarranid_cavalry_sword, itm_tab_shield_small_round_a, itm_arabian_horse_a],
   str_13|agi_15|int_4|cha_4|level(17),	wpex(105,95,110,15,10,110),	knows_common|knows_ironflesh_1|	knows_athletics_4|	knows_power_strike_2|	knows_shield_2|	knows_power_throw_2|knows_riding_6|knows_horse_archery_1,					sarranid_face_young_1, sarranid_face_older_2],

  ["freerider_adept_multiplayer","Adept","Adepts",tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_leather_jerkin, itm_leather_boots, itm_footman_helmet,
    itm_sword_medieval_d, itm_tab_shield_heater_b],
   str_10|agi_12|int_4|cha_4|level(11),	wpex(80,70,70,10,15,20)|wp_firearm(80),knows_common|knows_ironflesh_2|knows_athletics_4|knows_power_strike_1|knows_shield_2,																				man_face_young_1, man_face_older_2],
  ["freerider_guard_multiplayer","Guard","Guards",tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_leather_jerkin, itm_leather_boots, itm_footman_helmet,
    itm_fighting_pick, itm_long_hafted_knobbed_mace, itm_tab_shield_heater_a],
   str_14|agi_10|int_4|cha_4|level(13),	wpex(110,100,130,10,15,100),knows_common|knows_ironflesh_7|knows_athletics_2|	knows_power_strike_4|	knows_shield_3,																				man_face_young_1, man_face_older_2],
  ["freerider_paladin_multiplayer","Paladin","Paladins",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_coarse_tunic, itm_wrapping_boots,
    itm_sword_medieval_a_long, itm_long_hafted_knobbed_mace, itm_tab_shield_heater_cav_a, itm_saddle_horse],
   str_13|agi_11|int_4|cha_4|level(13),	wpex(100,90,110,10,15,100)|wp_firearm(40),knows_common|knows_ironflesh_3|knows_athletics_1|knows_power_strike_2|knows_shield_3|knows_riding_4|knows_horse_archery_2,								man_face_young_1, man_face_older_2],

  ["khergit_t_archer_multiplayer","Archer","Archers",tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_steppe_armor, itm_hide_boots,
    itm_winged_mace, itm_short_bow, itm_barbed_arrows, itm_barbed_arrows],
   str_10|agi_16|int_4|cha_4|level(15),	wpex(75,70,70,115,20,70),	knows_common|					knows_athletics_4|							knows_shield_2|knows_power_draw_4|knows_riding_3|knows_horse_archery_1|knows_power_throw_1,	khergit_face_middle_1, khergit_face_older_2],
  ["khergit_t_dismounted_lancer_multiplayer","Dismounted Lancer","Dismounted Lancers",tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_steppe_armor, itm_leather_boots, itm_steppe_cap,
    itm_sword_khergit_2, itm_tab_shield_small_round_b, itm_javelin],
   str_15|agi_15|int_4|cha_4|level(19),	wpex(105,100,115,20,10,115),knows_common|knows_ironflesh_2|	knows_athletics_5|	knows_power_strike_3|	knows_shield_3|	knows_power_throw_3|knows_riding_3,											khergit_face_middle_1, khergit_face_older_2],
  ["khergit_t_horseman_multiplayer","Horseman","Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_steppe_armor, itm_hide_boots,
    itm_sword_khergit_1, itm_light_lance, itm_hunting_bow, itm_arrows_b, itm_steppe_horse],
   str_12|agi_15|int_4|cha_4|level(16),	wpex(100,100,120,70,15,90),	knows_common|knows_ironflesh_1|	knows_athletics_3|	knows_power_strike_1|	knows_shield_3|	knows_power_draw_2|knows_power_throw_2|knows_horse_archery_2|knows_riding_6,khergit_face_middle_1, khergit_face_older_2],

  ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
  

  #replacable troop, not used
  ["nurse","Nurse","{!}nurse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  #erase later added to avoid errors

#Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["quick_battle_troop_1","Rodrigo de Braganca","Rodrigo de Braganca", tf_hero,0,0,fac_kingdom_1,
   [itm_long_hafted_knobbed_mace, itm_wooden_shield, itm_iron_staff, itm_throwing_daggers,
    itm_felt_hat, itm_fur_coat, itm_light_leather_boots, itm_leather_gloves],
   str_9|agi_15|int_12|cha_12|level(15),wpex(110,50,130,15,30,100),knows_riding_3|knows_athletics_5|knows_shield_3|knows_weapon_master_3|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_3,0x0000000e240070cd598bb02b9556428c00000000001eabce0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_2","Usiatra","Usiatra", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_nomad_bow, itm_barbed_arrows, itm_scimitar, itm_tab_shield_small_round_c, itm_sumpter_horse,
    itm_leather_armor, itm_splinted_greaves, itm_leather_gloves],
   str_12|agi_14|int_11|cha_18|level(22),wpex(110,100,100,150,80,115),knows_horse_archery_2|knows_riding_3|knows_athletics_4|knows_shield_2|knows_weapon_master_4|knows_power_draw_3|knows_power_throw_1|knows_power_strike_3|knows_ironflesh_4,0x000000007f004000719b69422165b71300000000001d5d1d0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_3","Hegen","Hegen", tf_hero,0,0,fac_kingdom_1,
   [itm_heavy_lance, itm_sword_two_handed_b, itm_sword_medieval_c, itm_tab_shield_heater_c, itm_warhorse,
    itm_guard_helmet, itm_coat_of_plates, itm_mail_mittens, itm_mail_boots],
   str_18|agi_16|int_12|cha_11|level(24),wpex(120,150,130,50,50,50),knows_riding_5|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_strike_6|knows_ironflesh_6,0x000000018000324428db8a431491472400000000001e44a90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_4","Konrad","Konrad", tf_hero,0,0,fac_kingdom_1,
   [itm_sword_two_handed_a, itm_mace_4, itm_tab_shield_kite_d,
    itm_bascinet_3, itm_scale_armor, itm_mail_mittens, itm_mail_boots],
   str_18|agi_15|int_12|cha_12|level(24),wpex(130,150,110,30,50,90),knows_riding_2|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_throw_3|knows_power_strike_6|knows_ironflesh_6,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000, swadian_face_old_2],
  ["quick_battle_troop_5","Sverre","Sverre", tf_hero,0,0,fac_kingdom_1,
   [itm_long_axe, itm_sword_viking_1, itm_light_throwing_axes, itm_tab_shield_round_d,
    itm_nordic_fighter_helmet, itm_byrnie, itm_leather_gloves, itm_leather_boots],
   str_15|agi_15|int_12|cha_12|level(21),wpex(140,115,125,80,15,110),knows_riding_1|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_draw_2|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_5,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_6","Borislav","Borislav", tf_hero,0,0,fac_kingdom_1,
   [itm_strong_bow, itm_barbed_arrows, itm_barbed_arrows, itm_shortened_spear,
    itm_leather_warrior_cap, itm_leather_jerkin, itm_leather_gloves, itm_ankle_boots],
   str_12|agi_15|int_15|cha_9|level(18),wpex(70,70,100,140,15,100),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_weapon_master_3|knows_power_draw_4|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_2,0x000000089e00444415136e36e34dc8e400000000001d46d90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_7","Stavros","Stavros", tf_hero,0,0,fac_kingdom_1,
   [itm_heavy_crossbow, itm_bolts, itm_sword_medieval_b_small, itm_tab_shield_pavise_c,
    itm_nasal_helmet, itm_padded_leather, itm_leather_gloves, itm_leather_boots],
   str_12|agi_15|int_15|cha_12|level(21),wpex(100,70,70,30,140,80),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_throw_2|knows_power_strike_4|knows_ironflesh_4,0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_8","Gamara","Gamara", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_throwing_spears, itm_throwing_spears, itm_scimitar, itm_leather_covered_round_shield,
    itm_desert_turban, itm_skirmisher_armor, itm_leather_gloves, itm_sarranid_boots_b],
   str_12|agi_15|int_12|cha_12|level(18),wpex(100,40,100,85,15,130),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_2,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_9","Aethrod","Aethrod", tf_hero,0,0,fac_kingdom_1,
   [itm_nomad_bow, itm_barbed_arrows, itm_barbed_arrows, itm_scimitar_b,
    itm_splinted_greaves, itm_lamellar_vest, itm_leather_gloves],
   str_16|agi_21|int_12|cha_14|level(26),wpex(95,90,80,160,70,115),knows_horse_archery_2|knows_riding_2|knows_athletics_7|knows_shield_2|knows_weapon_master_4|knows_power_draw_7|knows_power_throw_3|knows_power_strike_3|knows_ironflesh_4,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_10","Zaira","Zaira", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_sarranid_cavalry_sword, itm_strong_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_arabian_horse_b,
    itm_sarranid_felt_head_cloth_b, itm_sarranid_cloth_robe, itm_sarranid_boots_b, itm_leather_gloves],
   str_13|agi_18|int_15|cha_9|level(18),wpex(105,50,75,145,50,30),knows_horse_archery_6|knows_riding_6|knows_weapon_master_2|knows_power_draw_4|knows_power_throw_1|knows_power_strike_4|knows_ironflesh_1,0x0000000502003001471a6a24dc6594cb00000000001da4840000000000000000, swadian_face_old_2],
  ["quick_battle_troop_11","Argo Sendnar","Argo Sendnar", tf_hero,0,0,fac_kingdom_1,
   [itm_morningstar, itm_tab_shield_round_d, itm_war_spear, itm_courser,
    itm_leather_gloves, itm_fur_hat, itm_leather_boots, itm_leather_jacket],
   str_15|agi_12|int_14|cha_20|level(28),wpex(100,90,135,20,20,20),knows_riding_4|knows_athletics_2|knows_shield_4|knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_5,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000, swadian_face_old_2],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_tribal_warrior_outfit,itm_nomad_robe,itm_hide_boots,itm_tab_shield_small_round_a,itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_leather_vest,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],
   
  ["swadian_merchant", "Merchant of Praven", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, 
   [itm_sword_medieval_c_small, itm_red_gambeson, itm_leather_boots], 
   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["vaegir_merchant", "Merchant of Reyvadin", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, 
   [itm_scimitar, itm_leather_vest, itm_leather_boots], 
   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, 
   [itm_sword_khergit_3, itm_steppe_armor, itm_nomad_boots], 
   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, 
   [itm_sword_viking_3_small, itm_leather_jerkin, itm_leather_boots], 
   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, 
   [itm_military_cleaver_b, itm_tabard, itm_leather_boots], 
   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, 
   [itm_arabian_sword_b, itm_archers_vest, itm_sarranid_boots_b], 
   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],       
  ["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],
 
  ["sea_raider_leader","Sea Raider Captain","Sea Raiders",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_arrows_b,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_war_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_leather_jerkin,itm_byrnie,itm_leather_jerkin,itm_leather_boots, itm_nomad_boots],
   def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],

  ["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,
   [itm_butchering_knife,itm_falchion,itm_stones,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots],
   def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],
   
  ["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],   
  
  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],   
   
  ["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],     
  ##diplomacy begin
  ["dplmc_chamberlain","Chamberlain Aubrey de Vere", "Chamberlains",tf_hero|tf_male,0,0,fac_commoners,[itm_tabard, itm_leather_boots], def_attrib|level(10), wp(40),knows_inventory_management_10,0x0000000dfc0c238838e571c8d469c91b00000000001e39230000000000000000],

  ["dplmc_constable","Constable Miles de Gloucester","Constables",tf_hero|tf_male,0,0,fac_commoners,[itm_dplmc_coat_of_plates_red_constable, itm_leather_boots],
   knight_attrib_4,wp_melee(200),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_athletics_4,0x0000000b4b1015054b1b4d591cba28d300000000001e472b0000000000000000],

  ["dplmc_chancellor","Chancellor Herfast","Chancellors",tf_hero|tf_male,0,0,fac_commoners,[itm_nobleman_outfit, itm_leather_boots],def_attrib|level(10), wp(40),knows_inventory_management_10, 0x00000009a20c21cf491bad28a28628d400000000001e371a0000000000000000],

  ["dplmc_messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],

  ["dplmc_scout","Scout","Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],

   
# recruiter kit begin 
  ["dplmc_recruiter","Recruiter","Recruiter",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,swadian_face_young_1, swadian_face_old_2],
# recruiter kit end
  ##diplomacy end
]


#Troop upgrade declarations

# Mercenary tree
upgrade(troops,"farmer", "watchman")
upgrade(troops,"townsman","watchman")
upgrade2(troops,"watchman","town_watch","mercenary_fieldman")
upgrade2(troops,"town_watch","mercenary_swordsman","caravan_guard")
upgrade(troops,"mercenary_swordsman","hired_blade")
upgrade(troops,"hired_blade","mercenary_champion")
upgrade(troops,"caravan_guard","mercenary_horseman")
upgrade(troops,"mercenary_horseman","mercenary_cavalry")
upgrade2(troops,"mercenary_fieldman","mercenary_crossbowman","mercenary_hunter")
upgrade(troops,"mercenary_crossbowman","mercenary_trained_crossbowman")
upgrade(troops,"mercenary_hunter","mercenary_ranger")

# Special mercenaries
upgrade(troops,"mercenary_landsknecht","mercenary_trained_landsknecht")
upgrade(troops,"mercenary_trained_landsknecht","mercenary_veteran_landsknecht")

# upgrade(troops,"mercenary_horse_archer","mercenary_veteran_horse_archer")
upgrade(troops,"mercenary_horse_archer","mercenary_trained_horse_archer")
upgrade(troops,"mercenary_trained_horse_archer","mercenary_veteran_horse_archer")

# Swadian tree
upgrade(troops,"swadian_recruit","swadian_militia")
upgrade2(troops,"swadian_militia","swadian_footman","swadian_skirmisher")
upgrade2(troops,"swadian_footman","swadian_cavalryman","swadian_infantry")
upgrade(troops,"swadian_infantry","swadian_sergeant")
upgrade(troops,"swadian_skirmisher","swadian_crossbowman")
upgrade(troops,"swadian_crossbowman","swadian_sharpshooter")
upgrade(troops,"swadian_cavalryman","swadian_man_at_arms")
upgrade(troops,"swadian_man_at_arms","swadian_knight")

# Vaegir tree
upgrade2(troops,"vaegir_recruit","vaegir_footman","vaegir_scout")
upgrade(troops,"vaegir_footman","vaegir_veteran")
upgrade(troops,"vaegir_scout","vaegir_skirmisher")
upgrade(troops,"vaegir_skirmisher","vaegir_archer")
upgrade2(troops,"vaegir_archer","vaegir_marksman","vaegir_sharpshooter")
upgrade2(troops,"vaegir_veteran","vaegir_light_cavalry","vaegir_infantry")
upgrade(troops,"vaegir_light_cavalry","vaegir_horseman")
upgrade(troops,"vaegir_infantry","vaegir_guard")
upgrade(troops,"vaegir_horseman","vaegir_knight")

# Khergit tree
upgrade2(troops,"khergit_tribesman","khergit_skirmisher","khergit_steppe_fighter")
upgrade(troops,"khergit_skirmisher","khergit_horseman")
upgrade2(troops,"khergit_horseman","khergit_dune_rider","khergit_horse_archer")
upgrade(troops,"khergit_horse_archer","khergit_veteran_horse_archer")
upgrade(troops,"khergit_dune_rider","khergit_lancer")
upgrade2(troops,"khergit_steppe_fighter","khergit_soldier","khergit_archer")
upgrade(troops,"khergit_soldier","khergit_dune_fighter")
upgrade(troops,"khergit_archer","khergit_veteran_archer")
upgrade(troops,"khergit_dune_fighter","khergit_dismounted_lancer")

# Nord tree
upgrade2(troops,"nord_recruit","nord_footman","nord_huntsman")
upgrade2(troops,"nord_footman","nord_trained_footman","nord_plunderer")
upgrade(troops,"nord_trained_footman","nord_warrior")
upgrade(troops,"nord_warrior","nord_veteran")
upgrade(troops,"nord_veteran","nord_champion")
upgrade2(troops,"nord_plunderer","nord_warrior","nord_mounted_raider")
upgrade(troops,"nord_mounted_raider","nord_mounted_warrior")
# upgrade(troops,"nord_huntsman","nord_archer")
upgrade2(troops,"nord_huntsman","nord_archer","nord_bowman")
upgrade(troops,"nord_archer","nord_veteran_archer")
# upgrade(troops,"nord_bowman","nord_veteran_bowman")

# Rhodok tree
upgrade2(troops,"rhodok_tribesman","rhodok_spearman","rhodok_crossbowman")
upgrade2(troops,"rhodok_swordman","rhodok_trained_swordman","rhodok_mounted_skirmisher")
upgrade2(troops,"rhodok_spearman","rhodok_trained_spearman","rhodok_swordman")
upgrade(troops,"rhodok_trained_spearman","rhodok_veteran_spearman")
upgrade(troops,"rhodok_veteran_spearman","rhodok_sergeant")
upgrade(troops,"rhodok_trained_swordman","rhodok_veteran_swordman")
upgrade(troops,"rhodok_mounted_skirmisher","rhodok_mounted_trained_skirmisher")
upgrade(troops,"rhodok_mounted_trained_skirmisher","rhodok_mounted_veteran_skirmisher")
upgrade(troops,"rhodok_crossbowman","rhodok_trained_crossbowman")
upgrade(troops,"rhodok_trained_crossbowman","rhodok_veteran_crossbowman")
upgrade(troops,"rhodok_veteran_crossbowman","rhodok_sharpshooter")

# Sarranid tree
upgrade(troops,"sarranid_recruit","sarranid_footman")
upgrade2(troops,"sarranid_footman","sarranid_veteran_footman","sarranid_skirmisher")
upgrade2(troops,"sarranid_veteran_footman","sarranid_cavalry","sarranid_infantry")
upgrade(troops,"sarranid_infantry","sarranid_guard")
upgrade(troops,"sarranid_skirmisher","sarranid_archer")
upgrade(troops,"sarranid_archer","sarranid_master_archer")
upgrade(troops,"sarranid_cavalry","sarranid_horseman")
upgrade2(troops,"sarranid_horseman","sarranid_mamluke","sarranid_clibanarii")

# Freerider tree
upgrade2(troops,"draftee","spotter","footman")
upgrade2(troops,"spotter","scout","trainee")
upgrade(troops,"scout","pathfinder")
upgrade(troops,"trainee","apprentice")
upgrade2(troops,"apprentice","initiate","adept")
upgrade(troops,"footman","light_infantry")
upgrade2(troops,"light_infantry","medium_infantry","light_cavalry")
upgrade(troops,"medium_infantry","heavy_infantry")
upgrade(troops,"heavy_infantry","guard")
upgrade(troops,"light_cavalry","heavy_cavalry")
upgrade(troops,"heavy_cavalry","paladin")

#bandit trees
upgrade(troops,"looter","bandit")
upgrade(troops,"bandit","brigand")
upgrade2(troops,"brigand","thug","assassin")
upgrade(troops,"thug","murderer")

upgrade2(troops,"mountain_bandit","mountain_raider","mountain_cavalry")
upgrade2(troops,"forest_bandit","forest_warrior","forest_hunter")
upgrade(troops,"forest_hunter","forest_ranger"),
upgrade(troops,"steppe_bandit","steppe_rider")
upgrade(troops,"taiga_bandit","tundra_bandit")
upgrade(troops,"sea_raider","skull_crusher")
upgrade2(troops,"desert_bandit","desert_rider","desert_skirmisher")
#bandit trees ended

# Manhunters
upgrade(troops,"manhunter","slave_driver")
upgrade(troops,"slave_driver","slave_hunter")
upgrade(troops,"slave_hunter","slave_crusher")
upgrade(troops,"slave_crusher","slaver_chief")

# Women tree
upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")
upgrade2(troops,"fighter_woman","swordwoman","fieldwoman")
upgrade2(troops,"swordwoman","sword_sister","lady_knight")
upgrade2(troops,"fieldwoman","woman_archer","woman_arbalestrier")
upgrade(troops,"refugee","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")

# Nobles
# Swadian
upgrade(troops,"swadian_noble", "swadian_noble2")
upgrade(troops,"swadian_noble2", "swadian_noble3")
upgrade(troops,"swadian_noble3", "swadian_noble4")
upgrade(troops,"swadian_noble4", "swadian_noble5")
# Vaegir
upgrade(troops,"vaegir_noble", "vaegir_noble2")
upgrade(troops,"vaegir_noble2", "vaegir_noble3")
upgrade(troops,"vaegir_noble3", "vaegir_noble4")
upgrade(troops,"vaegir_noble4", "vaegir_noble5")
# Khergit
upgrade(troops,"khergit_noble", "khergit_noble2")
upgrade(troops,"khergit_noble2", "khergit_noble3")
upgrade(troops,"khergit_noble3", "khergit_noble4")
upgrade(troops,"khergit_noble4", "khergit_noble5")
# Nord
upgrade(troops,"nord_noble", "nord_noble2")
upgrade(troops,"nord_noble2", "nord_noble3")
upgrade(troops,"nord_noble3", "nord_noble4")
upgrade(troops,"nord_noble4", "nord_noble5")
# Rhodok
upgrade(troops,"rhodok_noble", "rhodok_noble2")
upgrade(troops,"rhodok_noble2", "rhodok_noble3")
upgrade(troops,"rhodok_noble3", "rhodok_noble4")
upgrade(troops,"rhodok_noble4", "rhodok_noble5")
# Player/Mercenary
upgrade(troops,"player_noble", "player_noble2")
upgrade(troops,"player_noble2", "player_noble3")
upgrade(troops,"player_noble3", "player_noble4")
upgrade(troops,"player_noble4", "player_noble5")
# Sarranid
upgrade(troops,"sarranid_noble", "sarranid_noble2")
upgrade(troops,"sarranid_noble2", "sarranid_noble3")
upgrade(troops,"sarranid_noble3", "sarranid_noble4")
upgrade(troops,"sarranid_noble4", "sarranid_noble5")
# Freerider
upgrade(troops,"freerider_noble", "freerider_noble2")
upgrade(troops,"freerider_noble2", "freerider_noble3")
upgrade(troops,"freerider_noble3", "freerider_noble4")
upgrade(troops,"freerider_noble4", "freerider_noble5")
