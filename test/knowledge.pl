/**parent*/

/**The he 1*/
parent(queenElizabethII,princeCharles).
parent(princePhillip,princeCharles).
parent(queenElizabethII,princessAnne).
parent(princePhillip,princessAnne).
parent(queenElizabethII,princeAndrew).
parent(princePhillip,princeAndrew).
parent(queenElizabethII,princeEdward).
parent(princePhillip,princeEdward).

/**The he 2*/
parent(princessDiana,princeWilliam).
parent(princeCharles,princeWilliam).
parent(camillaParkerBowles,princeWilliam).
parent(princessDiana,princeHarry).
parent(princeCharles,princeHarry).
parent(camillaParkerBowles,princeHarry).

parent(captainMarkPhillips,peterPhillips).
parent(princessAnne,peterPhillips).
parent(timothyLaurence,peterPhillips).
parent(captainMarkPhillips,zaraPhillips).
parent(princessAnne,zaraPhillips).
parent(timothyLaurence,zaraPhillips).

parent(sarahFerguson,princessBeatrice).
parent(princeAndrew,princessBeatrice).
parent(sarahFerguson,princessEugenie).
parent(princeAndrew,princessEugenie).

parent(sophieRhys-jones,jamesViscountSevern).
parent(princeEdward,jamesViscountSevern).
parent(sophieRhys-jones,ladyLouiseMountbatten_Windsor).
parent(princeEdward,ladyLouiseMountbatten_Windsor).

/**The he 3*/
parent(princeWilliam,princeGeorge).
parent(kateMiddleton,princeGeorge).
parent(princeWilliam,princessCharlotte).
parent(kateMiddleton,princessCharlotte).

parent(autumnKelly,savannahPhillips).
parent(peterPhillips,savannahPhillips).
parent(autumnKelly,islaPhillips).
parent(peterPhillips,islaPhillips).

parent(zaraPhillips,miaGraceTindall).
parent(mikeTindall,miaGraceTindall).


/**male*/
male(princePhillip).
male(princeCharles).
male(captainMarkPhillips).
male(timothyLaurence).
male(princeAndrew).
male(princeEdward).
male(princeWilliam).
male(princeHarry).
male(peterPhillips).
male(mikeTindall).
male(jamesViscountSevern).
male(princeGeorge).
male(miaGraceTindall).


/**female*/
female(queenElizabethII).
female(princessDiana).
female(camillaParkerBowles).
female(princessAnne).
female(sarahFerguson).
female(sophieRhys-jones).
female(kateMiddleton).
female(autumnKelly).
female(zaraPhillips).
female(princessBeatrice).
female(princessEugenie).
female(ladyLouiseMountbatten_Windsor).
female(princessCharlotte).
female(savannahPhillips).
female(islaPhillips).


/**married*/
married(queenElizabethII,princePhillips).
married(princePhillips,queenElizabethII).

married(princeCharles,camillaParkerBowles).
married(camillaParkerBowles,princeCharles).

married(princessAnne,timothyLaurence).
married(timothyLaurence,princessAnne).

married(sophieRhys-jones,princeEdward).
married(princeEdward,sophieRhys-jones).

married(princeWilliam,kateMiddleton).
married(kateMiddleton,princeWilliam).

married(autumnKelly,peterPhillips).
married(peterPhillips,autumnKelly).

married(zaraPhillips,mikeTindall).
married(mikeTindall,zaraPhillips).

/**divorced*/
divorced(princessDiana,princeCharles).
divorced(princeCharles,princessDiana).

divorced(captainMarkPhillips,princessAnne).
divorced(princessAnne,captainMarkPhillips).

divorced(sarahFerguson,princeAndrew).
divorced(princeAndrew,sarahFerguson).

/**Dinh nghia cac vi tu*/
husband(Person,Wife):-married(Person,Wife),male(Person).
wife(Person,Husband):-married(Person,Husband),female(Person).
father(Parent,Child):-parent(Parent,Child),male(Parent).
mother(Parent,Child):-parent(Parent,Child),female(Parent).
child(Child,Parent):-parent(Parent,Child).
son(Child,Parent):-parent(Parent,Child),male(Child).
daughter(Child,Parent):-parent(Parent,Child),female(Child).
grandparent(GP,GC):-parent(X,GC),parent(GP,X).
grandmother(GM,GC):-mother(X,GC),mother(GM,X).
grandfather(GF,GC):-father(X,GC),father(GF,X).
grandchild(GC,GP):-grandparent(GP,GC).
grandson(GS,GP):-grandchild(GS,GP),male(GS).
granddaughter(GD,GP):-grandchild(GD,GP),female(GD).
sibling(Person1,Person2):-father(X,Person1),child(Person2,X),Person1\=Person2.
brother(Person,Sibling):-sibling(Person,Sibling),male(Person).
sister(Person,Sibling):-sibling(Person,Sibling),female(Person).
aunt(Person,NieceNephew):-parent(X,NieceNephew),sibling(X,Person),female(Person).
aunt(Person,NieceNephew):-parent(X,NieceNephew),brother(Y,X),wife(Person,Y).
aunt(Person,NieceNephew):-married(NieceNephew,X),parent(Y,X),brother(Z,Y),wife(Person,Z).
uncle(Person,NieceNephew):-parent(X,NieceNephew),sibling(X,Person),male(Person).
uncle(Person,NieceNephew):-parent(X,NieceNephew),sister(Y,X),husband(Person,Y).
uncle(Person,NieceNephew):-married(NieceNephew,X),parent(Y,X),sister(Z,Y),husband(Person,Z).
niece(Person,AuntUncle):-aunt(AuntUncle,Person),female(Person).
niece(Person,AuntUncle):-uncle(AuntUncle,Person),female(Person).
nephew(Person,AuntUncle):-aunt(AuntUncle,Person),male(Person).
nephew(Person,AuntUncle):-uncle(AuntUncle,Person),male(Person).
