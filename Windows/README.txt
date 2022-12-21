What are Windows?

A window is usually a screen or a builder of a screen to show visibly. Builders of screens are known as Scripts.
Windows can either be STATIC or NON-STATIC, the latter usually referred to as Slates.

What are Scripts?

Scripts are classes or objects like Quests or Creation that push and build slates. These are intricately tied in with windows.
Scripts never mess with STATIC windows, only Slates.
Scripts use a phase checkpoint system to be able to terminate from tunneling too deep into a process.
Scripts are tightly ingrained into the print queue.

What are Slates?

Slates are object based windows, or non-static windows that are actually completely empty.
Scripts build these slates, and all slates look completely different.
Screens like Combat are not actually slates, because they do not rely on scripts. They instead overwrite themselves.