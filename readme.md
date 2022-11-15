# Projekt - zadání 2. části
Cílem této části projektu je vyzkoušet si:
provedení explorativní analýzy na zvolené datové sadě.
úpravu datové sady do podoby vhodné pro dolování.
Dostupné datové sady a možné dolovací úlohy:
Datová sada Automobily – dostupná zde: https://archive.ics.uci.edu/ml/datasets/Automobile
Dolovací úloha: predikce ceny automobilu na základě ostatních atributů.
Datová sada Tučňáci – dostupná zde: https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data
Dolovací úlohy: Klasifikace druhů tučňáků na základě ostatních atributů nebo shluková analýza.
Datová sada Platy v IT – dostupná zde: https://www.kaggle.com/parulpandey/2020-it-salary-survey-for-eu-region
Dolovací úloha: Predikce výše platu na základě ostatních atributů.
Způsob odevzdání (požadované výstupy):
Výsledné řešení (jeden zip archiv) odevzdá pouze vedoucí týmu prostřednictvím IS VUT. Řešení bude obsahovat:
Zdrojové kódy pro Vámi provedenou explorativní analýzu a zdrojové kódy pro úpravu datové sady do požadované podoby. Preferovaným programovacím jazykem je Python, ale můžete využít i Javu nebo jazyk R. Řešení je možné odevzdat i formou Jupyter notebooku.
Dokumentaci obsahující výsledky explorativní analýzy a popis provedených úprav datové sady ve formátu pdf. K explorativní analýze bude dokumentace obsahovat odpovídající podkapitolu ke každému požadovanému bodu uvedenému níže. Pro prezentaci zjištěných informací využijte vhodné tabulky a grafy. Dále pro každou požadovanou úpravu datové sady uveďte, jakou metodu (jaké metody) jste použili, a zdůvodněte, proč jste vybrali právě tuto metodu (tyto metody).
Obě výsledné varianty upravené datové sady ve formátu csv. Pro zmenšení velikosti odevzdávaného archivu je možné odevzdat pouze prvních 50 řádků těchto souborů.

Pokyny k řešení:
Z dostupných datových sad si zvolte jednu datovou sadu, kterou se budete dále zabývat. Stáhněte si zvolenou datovou sadu z uvedeného zdroje a prostudujte si dostupné informace k této datové sadě.

TODO:
- [X] 1. Explorativní analýza
- [ ] 2. Úprava dátové sady
- [ ] 3. Dokumentace
- [ ] 4. Odevzdání

DOING:

časť 1 - Exploratívna analýza

prozkoumejte rozložení hodnot jednotlivých atributů pomocí vhodných grafů, zaměřte se i na to, jak hodnota jednoho či dvou atributů ovlivní rozložení hodnot jiného atributu. Do dokumentace vložte alespoň 5 různých grafů, zobrazujících zjištěná rozložení hodnot. Použijte různé typy grafů (např. bodový graf, histogram, krabicový nebo houslový graf, graf složený z více podgrafů apod.).
??? otázka úpravy dátové sady ???

časť 2 - Úprava dátové sady	




Připravte 2 varianty datové sady vhodné pro dolovací algoritmy. Můžete uvažovat dolovací úlohu uvedenou u datové sady nebo navrhnout vlastní dolovací úlohy. V případě vlastní dolovací úlohy ji specifikujte v dokumentaci. V rámci přípravy datové sady proveďte následující kroky:

Pro jednu variantu datové sady proveďte diskretizaci numerických atributů tak, aby výsledná datová sada byla vhodná pro algoritmy, které vyžadují na vstupu kategorické atributy.
Pro druhou variantu datové sady proveďte vhodnou transformaci kategorických atributů na numerické atributy. Dále pak proveďte normalizaci numerických atributů, které má smysl normalizovat. Výsledná datová sada by měla být vhodná pro metody vyžadující numerické vstupy.


Done:

časť 1 - Exploratívna analýza

proveďte korelační analýzu numerických atributů (k analýze využijte i grafy a korelační koeficienty).
prozkoumejte jednotlivé atributy datové sady, jejich typ a hodnoty, kterých nabývají (počet hodnot, nejčastější hodnoty, rozsah hodnot atd.)
zjistěte, zda zvolená datová sada obsahuje nějaké odlehlé hodnoty.
proveďte podrobnou analýzu chybějící hodnot (celkový počet chybějících hodnot, počet objektů s více chybějícími hodnotami atd.).

časť 2 - Úprava dátové sady

Vypořádejte se s odlehlými hodnotami, jsou-li v datové sadě přítomny.
Vypořádejte se s chybějícími hodnotami. Pro odstranění těchto hodnot využijte alespoň dvě různé metody pro odstranění chybějících hodnot. - Určiť korelácie medzi atribútmi a na základe toho vybrať ktoré hodnoty budú použité na odstránenie.

časť 3 - Dokumentace

Určiť korelácie medzi atribútmi a na základe toho vybrať ktoré hodnoty budú použité pri dolovaní vzorov. V dokumentácii je potrebné uviesť korelačné koeficienty a grafy korelácií.
