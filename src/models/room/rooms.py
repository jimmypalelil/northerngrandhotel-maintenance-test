import gc
from src.common.database import Database
from src.models.HK_Models.room.room import room


room_200=room(200,'K')
room_201=room(201,'K')
room_202=room(202,'QQ')
room_203=room(203,'QQ')
room_204=room(204,'QQ')
room_205=room(205,'QQ')
room_206=room(206,'QQ')
room_207=room(207,'QQ')
room_208=room(208,'QQ')
room_210=room(210,'QQ')
room_212=room(212,'K')
room_214=room(214,'QQ')
room_216=room(216,'QQ')
room_218=room(218,'QQ')
room_219=room(219,'QQ')
room_220=room(220,'QQ')
room_221=room(221,'QQ')
room_222=room(222,'QQ')
room_223=room(223,'QQ')
room_224=room(224,'QQ')
room_225=room(225,'QQ')
room_226=room(226,'K')
room_227=room(227,'K')

room_300=room(300,'K')
room_301=room(301,'K')
room_302=room(302,'QQ')
room_303=room(303,'K')
room_304=room(304,'QQ')
room_305=room(305,'K')
room_306=room(306,'QQ')
room_307=room(307,'K')
room_308=room(308,'QQ')
room_309=room(309,'K')
room_310=room(310,'K')
room_311=room(311,'K')
room_312=room(312,'K')
room_314=room(314,'K')
room_316=room(316,'QQ')
room_317=room(317,'QQ')
room_318=room(318,'K')
room_319=room(319,'QQ')
room_320=room(320,'K')
room_321=room(321,'QQ')
room_322=room(322,'K')
room_323=room(323,'QQ')
room_324=room(324,'K')
room_325=room(325,'QQ')
room_326=room(326,'K')
room_327=room(327,'K')

room_400=room(400,'K')
room_401=room(401,'K')
room_402=room(402,'QQ')
room_403=room(403,'K')
room_404=room(404,'K')
room_405=room(405,'K')
room_406=room(406,'QQ')
room_407=room(407,'K')
room_408=room(408,'K')
room_409=room(409,'K')
room_410=room(410,'QQ')
room_411=room(411,'K')
room_412=room(412,'QQ')
room_414=room(414,'K')
room_416=room(416,'K')
room_417=room(417,'K')
room_418=room(418,'K')
room_419=room(419,'K')
room_420=room(420,'K')
room_421=room(421,'K')
room_422=room(422,'QQ')
room_423=room(423,'QQ')
room_424=room(424,'K')
room_425=room(425,'K')
room_426=room(426,'K')
room_427=room(427,'K')

room_500=room(500,'K')
room_501=room(501,'K')
room_502=room(502,'K')
room_503=room(503,'K')
room_504=room(504,'K')
room_505=room(505,'K')
room_506=room(506,'QQ')
room_507=room(507,'K')
room_508=room(508,'K')
room_509=room(509,'K')
room_510=room(510,'K')
room_511=room(511,'K')
room_512=room(512,'K')
room_514=room(514,'QQ')
room_516=room(516,'K')
room_517=room(517,'K')
room_518=room(518,'K')
room_519=room(519,'QQ')
room_520=room(520,'K')
room_521=room(521,'K')
room_522=room(522,'K')
room_523=room(523,'K')
room_524=room(524,'K')
room_525=room(525,'K')
room_526=room(526,'K')
room_527=room(527,'K')

room_600=room(600,'K')
room_601=room(601,'K')
room_602=room(602,'QQ')
room_603=room(603,'K')
room_604=room(604,'K')
room_605=room(605,'K')
room_606=room(606,'K')
room_607=room(607,'K')
room_608=room(608,'K')
room_609=room(609,'K')
room_610=room(610,'QQ')
room_611=room(611,'K')
room_612=room(612,'K')
room_614=room(614,'K')
room_616=room(616,'QQ')
room_617=room(617,'K')
room_618=room(618,'K')
room_619=room(619,'K')
room_620=room(620,'K')
room_621=room(621,'K')
room_622=room(622,'QQ')
room_623=room(623,'K')
room_624=room(624,'K')
room_625=room(625,'QQ')
room_626=room(626,'K')
room_627=room(627,'K')

rooms1 = gc.get_referrers(room)
Database.go()

def run():
    print("hi")
    for rom in rooms1:
        if rom.__class__ is room:
            rom.save_to_mongo()


run()