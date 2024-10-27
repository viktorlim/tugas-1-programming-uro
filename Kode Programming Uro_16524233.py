import random

def start_game():
    while True:
        try:
            bet = int(input("Berapa banyak uang yang ingin dipertaruhkan? "))
            if bet <= 0:
                print("Taruhan harus lebih besar dari 0.")
                continue
            break
        except ValueError:
            print("Tolong masukkan angka.")

    BLACKJACK = 21
    dealer_berhenti = 17
    nilai_kartu = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }
    deck = list(nilai_kartu.keys()) * 4
    random.shuffle(deck)

    def ambil_kartu(deck_kartu):
        return deck_kartu.pop()

    def hitung_nilai(hand):
        nilai = sum(nilai_kartu[card] for card in hand)
        aces = hand.count('A')
        while nilai > BLACKJACK and aces:
            nilai -= 10
            aces -= 1
        return nilai

    def display_kartu(nama, hand):
        print(f"{nama}'s hand: {', '.join(hand)} (value: {hitung_nilai(hand)})")

    def play_blackjack():
        kartu_player = [ambil_kartu(deck), ambil_kartu(deck)]
        kartu_dealer = [ambil_kartu(deck), ambil_kartu(deck)]

        display_kartu("Player", kartu_player)
        print(f"Kartu Dealer: {kartu_dealer[0]}, ?")

        while True:
            pilih = input("Mau tambah atau berhenti? ").strip().lower()
            if pilih == 'tambah':
                kartu_player.append(ambil_kartu(deck))
                display_kartu("Player", kartu_player)
                if hitung_nilai(kartu_player) > BLACKJACK:
                    print(f"Player kalah Rp {bet}!")
                    return
            elif pilih == 'berhenti':
                break
            else:
                print("Invalid. Tolong pilih mau 'tambah' atau 'berhenti'.")

        display_kartu("Dealer", kartu_dealer)
        while hitung_nilai(kartu_dealer) < dealer_berhenti:
            kartu_dealer.append(ambil_kartu(deck))
            display_kartu("Dealer", kartu_dealer)
            if hitung_nilai(kartu_dealer) > BLACKJACK:
                print(f"Player menang Rp {bet*2}")
                return

        player_total = hitung_nilai(kartu_player)
        dealer_total = hitung_nilai(kartu_dealer)

        print("\nFinal Results:")
        display_kartu("Player", kartu_player)
        display_kartu("Dealer", kartu_dealer)

        if player_total > dealer_total:
            print(f"Player menang Rp {bet*2}")
        elif dealer_total > player_total:
            print(f"Player kalah Rp {bet}!")
        else:
            print("Permainan seri!")
    
    play_blackjack()
     
start_game()

mau_main_lagi = input("Apakah anda masih mau main? ").lower()

while mau_main_lagi == "iya":
    start_game()
    mau_main_lagi = input("Apakah anda masih mau main?(iya/tidak) ").lower()

print("terima kasih sudah bermain :)")