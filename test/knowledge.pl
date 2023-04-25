male(princePhillip).
male(princeAndrew).
male(princeEdward).
male(princeWilliam).
male(captainMarkPhillips).
male(timothyLaurence).
male(princeCharles).
male(princeHarry).
male(peterPhillips).
male(mikeTindall).
male(jamesviscountSevern).
male(princeGeorge).
male(miaGraceTindall).

female(queenElizabethII).
female(camillaParkerBowles).
female(ladyDianaSpencer).
female(princessAnne).
female(sarahFerguson).
female(sophieRhysJones).
female(kateMiddleton).
female(princessDiana).
female(autumnKelly).
female(zaraPhillips).
female(princessBeatrice).
female(princessCharlotte).
female(savannahPhillips).
female(islaPhillips).
female(princessEugenie).
female(ladyLouiseMountbattenWindsor).

married(queenElizabethII, princePhillip).
married(princePhillip, queenElizabethII).
married(princeCharles, camillaParkerBowles).
married(camillaParkerBowles, princeCharles).
married(princessAnne, timothyLaurence).
married(timothyLaurence, princessAnne).
married(sophieRhysJones, princeEdward).
married(princeEdward, sophieRhysJones).
married(princeWilliam, kateMiddleton).
married(kateMiddleton, princeWilliam).
married(autumnKelly, peterPhillips).
married(peterPhillips, autumnKelly).
married(zaraPhillips, mikeTindall).
married(mikeTindall, zaraPhillips).

divorced(princeCharles, princessDiana).
divorced(princessDiana, princeCharles).
divorced(captainMarkPhillips, princessAnne).
divorced(princessAnne, captainMarkPhillips).
divorced(sarahFerguson, princeAndrew).
divorced(princeAndrew, sarahFerguson).

parent(princeWilliam,princeGeorge).
parent(princeWilliam,princessCharlotte).
parent(kateMiddleton,princeGeorge).
parent(kateMiddleton,princessCharlotte).
parent(autumnKelly,savannahPhillips).
parent(autumnKelly,islaPhillips).
parent(peterPhillips,savannahPhillips).
parent(peterPhillips,islaPhillips).
parent(zaraPhillips,miaGraceTindall).
parent(mikeTindall,miaGraceTindall).
parent(princessDiana,princeWilliam).
parent(princessDiana,princeHarry).
parent(princeCharles,princeWilliam).
parent(princeCharles,princeHarry).
parent(captainMarkPhillips,peterPhillips).
parent(captainMarkPhillips,zaraPhillips).
parent(princessAnne,peterPhillips).
parent(princessAnne,zaraPhillips).
parent(sarahFerguson,princessBeatrice).
parent(princeAndrew,princessBeatrice).
parent(princeAndrew,princessEugenie).
parent(sophieRhysJones,jamesviscountSevern).
parent(sophieRhysJones,ladyLouiseMountbattenWindsor).
parent(princeEdward,jamesviscountSevern).
parent(princeEdward,ladyLouiseMountbattenWindsor).
parent(queenElizabethII,princeCharles).
parent(queenElizabethII,princessAnne).
parent(queenElizabethII,princeAndrew).
parent(queenElizabethII,princeEdward).
parent(princePhillip,princeCharles).
parent(princePhillip,princessAnne).
parent(princePhillip,princeAndrew).
parent(princePhillip,princeEdward).

husband(Person, Wife) :- married(Person, Wife), male(Person).
wife(Person, Husband) :- married(Person, Husband), female(Person).
father(Parent, Child) :- parent(Parent, Child), male(Parent).
mother(Parent, Child) :- parent(Parent, Child), female(Parent).
child(Child, Parent) :- parent(Parent, Child).
son(Child,Parent):-parent(Parent,Child),male(Child).
daughter(Child,Parent):-parent(Parent,Child),female(Child).

grandparent(GP,GC) :- parent(GP,Parent), parent(Parent,GC).
grandmother(GM,GC) :- grandparent(GM,GC), female(GM).
grandfather(GF,GC) :- grandparent(GF,GC), male(GF).
grandchild(GC,GP) :- grandparent(GP,GC).
grandson(GS,GP) :- grandchild(GS,GP),male(GS).
granddaughter(GD,GP) :- grandchild(GD,GP), female(GD).

sibling(Person1, Person2) :- parent(Parent, Person1), parent(Parent, Person2), Person1 \= Person2.
brother(Person, Sibling) :- sibling(Person, Sibling), male(Person).
sister(Person, Sibling) :- sibling(Person, Sibling), female(Person).
aunt(Person, NieceNephew) :- wife(Person, Uncle), brother(Uncle, Parent), parent(Parent, NieceNephew).
aunt(Person, NieceNephew) :- sister(Person, Parent), parent(Parent, NieceNephew).
uncle(Person, NieceNephew) :- husband(Person, Aunt), sister(Aunt, Parent), parent(Parent, NieceNephew).
uncle(Person, NieceNephew) :-brother(Person, Parent),parent(Parent, NieceNephew).
niece(Person, AuntUncle) :- aunt(AuntUncle, Person), male(Person).
niece(Person, AuntUncle) :- uncle(AuntUncle, Person), male(Person).
nephew(Person, AuntUncle) :- aunt(AuntUncle, Person), female(Person).
nephew(Person, AuntUncle) :- uncle(AuntUncle, Person), female(Person).