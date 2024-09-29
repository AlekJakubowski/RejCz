import pandas as pd

# Przygotowanie danych do trzech sekcji
data_risk_assessment = {
    'Sekcja': [
        'Karta Praw Podstawowych UE', 'Karta Praw Podstawowych UE', 'Karta Praw Podstawowych UE', 
        'Karta Praw Podstawowych UE', 'Karta Praw Podstawowych UE', 'Karta Praw Podstawowych UE', 
        'Karta Praw Podstawowych UE', 
        'Konstytucja RP', 'Konstytucja RP', 'Konstytucja RP', 'Konstytucja RP', 'Konstytucja RP', 
        'Konstytucja RP', 'Konstytucja RP', 
        'RODO i DODO', 'RODO i DODO', 'RODO i DODO', 'RODO i DODO', 'RODO i DODO', 'RODO i DODO', 
        'RODO i DODO'
    ],
    'Prawo/Wolność': [
        'Prawo do godności', 'Prawo do integralności osoby', 'Prawo do ochrony danych osobowych', 
        'Prawo do wolności słowa', 'Prawo do wolności zgromadzeń', 'Prawo do azylu', 'Prawo do pracy',
        'Prawo do życia', 'Prawo do wolności osobistej', 'Prawo do wolności sumienia', 
        'Prawo do ochrony zdrowia', 'Prawo do własności', 'Prawo do równości wobec prawa', 
        'Prawo do prywatności', 
        'Prawo do ochrony danych osobowych', 'Prawo do dostępu do danych osobowych', 
        'Prawo do poprawiania danych osobowych', 'Prawo do bycia zapomnianym', 
        'Prawo do ograniczenia przetwarzania danych', 'Prawo do przenoszenia danych', 
        'Prawo do sprzeciwu wobec przetwarzania'
    ],
    'Zagrożenie': [
        'Poniżenie, degradacja ludzkiej godności', 'Nadużycie medyczne, przemoc', 
        'Nieuprawnione przetwarzanie danych', 'Ograniczenie dostępu do informacji', 
        'Ograniczenie prawa do demonstracji', 'Brak ochrony dla uchodźców', 'Dyskryminacja w zatrudnieniu',
        'Utrata życia na skutek działań osób trzecich', 'Bezprawne pozbawienie wolności', 
        'Dyskryminacja ze względu na przekonania', 'Ograniczony dostęp do opieki zdrowotnej', 
        'Bezprawna konfiskata majątku', 'Dyskryminacja prawna', 'Naruszenie prywatności osobistej',
        'Kradzież tożsamości, wyciek danych', 'Brak możliwości wglądu w przetwarzane dane', 
        'Uniemożliwienie korekty błędnych danych', 'Ograniczenie prawa do usunięcia danych', 
        'Brak możliwości ograniczenia przetwarzania', 'Ograniczenie w przenoszeniu danych', 
        'Ignorowanie sprzeciwu wobec przetwarzania danych'
    ],
    'Prawdopodobieństwo (1-5)': [3, 3, 4, 3, 2, 2, 3, 4, 3, 3, 2, 4, 3, 3, 4, 3, 3, 2, 2, 3, 2],
    'Skutki (1-5)': [5, 4, 4, 4, 3, 3, 4, 5, 4, 4, 4, 5, 3, 4, 4, 4, 3, 4, 3, 3, 3],
    'Ryzyko': [],
    'Zabezpieczenia techniczne i organizacyjne': [
        'Kodeks etyki, przepisy antydyskryminacyjne', 'Prawo do ochrony zdrowia, monitoring', 
        'Szyfrowanie danych, polityki prywatności', 'Przepisy dotyczące wolności słowa', 
        'Prawo do zgromadzeń, systemy ochrony', 'Prawo do azylu, międzynarodowa ochrona', 
        'Kodeks pracy, audyty HR', 
        'Monitoring, systemy ochrony, policja', 'Prawo do obrony, kodeks karny', 
        'Prawo do wolności sumienia, kampanie edukacyjne', 'Prawo do ochrony zdrowia, rozwój infrastruktury', 
        'Prawo własności, zabezpieczenia prawne', 'Prawo antydyskryminacyjne', 'Ochrona prywatności, audyty', 
        'Szyfrowanie danych, audyty bezpieczeństwa', 'Prawo dostępu, polityki prywatności', 
        'Możliwość zgłaszania poprawek, systemy zgłoszeń', 'Prawo do bycia zapomnianym, procedury usuwania danych', 
        'Ograniczenie przetwarzania, zabezpieczenia IT', 'Przenoszenie danych, interoperacyjność systemów', 
        'Prawo do sprzeciwu, polityki zgodności z przepisami'
    ],
    'Waga zabezpieczenia (1-3)': [2.5, 2, 2.5, 2, 2, 2.5, 2, 3, 2.5, 2, 2.5, 2.5, 2, 2.5, 2.5, 2, 2, 2.5, 2, 2.5, 2],
    'Zredukowane ryzyko': []
}

# Obliczanie ryzyka i zredukowanego ryzyka
for i in range(len(data_risk_assessment['Prawo/Wolność'])):
    ryzyko = data_risk_assessment['Prawdopodobieństwo (1-5)'][i] * data_risk_assessment['Skutki (1-5)'][i]
    zredukowane_ryzyko = ryzyko / data_risk_assessment['Waga zabezpieczenia (1-3)'][i]
    data_risk_assessment['Ryzyko'].append(ryzyko)
    data_risk_assessment['Zredukowane ryzyko'].append(round(zredukowane_ryzyko, 1))

# Tworzenie DataFrame
df_risk_assessment = pd.DataFrame(data_risk_assessment)

# Zapis do pliku Excel
file_path_risk_assessment = '/mnt/data/ocena_ryzyka_prawa_i_wolnosci_trzy_sekcje.xlsx'
df_risk_assessment.to_excel(file_path_risk_assessment, index=False)

file_path_risk_assessment