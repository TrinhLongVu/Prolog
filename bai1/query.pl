:- [knowledge].

'who is husband of Prince Harry ?' :- husband(Husband, 'Prince Harry') -> write(Husband).
'who is wife of Mike Tindall ?' :- wife(Wife, 'Mike Tindall') -> write(Wife).
'who is father of Zara Phillips ?' :- father(Father, 'Zara Phillips') -> write(Father).
'Who is mother of Prince Andrews ?' :-mother(Mother, 'Prince George') -> write(Mother).
'who is children of Prince Charles ?' :- findall(Child, child(Child, 'Prince Charles'), Data), write(Data).
'who is son of Queen Elizabeth II ?' :- findall(Son, son(Son ,'Queen Elizabeth II'), Data), write(Data).
'who is daughter of Prince Phillip ?' :- findall(Daughter, daughter(Daughter, 'Prince Phillip'), Data), write(Data).
'Was Prince Charles the son of Prince Phillip ?' :- son('Prince Charles', 'Prince Phillip').
'Was Queen Elizabeth the wife of Mia Grace Tindall ?' :- married('Queen Elizabeth II', 'Mia Grace Tindall').
'who is grandparent of Mia Grace Tindall ?' :- findall(GrandParent, grandparent(GrandParent, 'Mia Grace Tindall'), Data), write(Data).
'Was Princess Anne the grandParent of Mia Grace Tindall ?' :- grandparent('Princess Anne', 'Mia Grace Tindall').
'who is grandmother of Mia Grace Tindall ?' :- grandmother(Grandmother, 'Mia Grace Tindall') -> write(Grandmother).
'who is grandfather of Isla Phillips ?' :- grandfather(Grandfather, 'Isla Phillips') -> write(Grandfather).
'who is sibling of Viscount Severn ?' :- findall(Sibling, sibling(Sibling, 'James, Viscount Severn'), Data), write(Data).
'Was Prince Andrew the sibling of Princess Anne ?' :- sibling('Prince Andrew', 'Princess Anne').
'who is the brother of Princess Anne ?' :- findall(Brother, brother(Brother, 'Princess Anne'), Data), write(Data).
'who is the brother of Prince William ?' :- findall(Brother, brother(Brother, 'Prince William'), Data), write(Data).
'Was Prince Andrew the brother of Princess Anne' :- brother('Prince Andrew', 'Princess Anne').
'who is the sister of Prince Andrew ?' :- findall(Sister, sister(Sister, 'Prince Andrew'), Data), write(Data).
'Was Princess Anne the sister of Prince William ?' :- sister('Princess Anne', 'Prince William').