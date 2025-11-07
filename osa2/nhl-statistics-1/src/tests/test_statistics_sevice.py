import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_palauttaa_oikean_pelaajan(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_team_palauttaa_oikeat_pelaajat(self):
        team_players = self.stats.team("EDM")
        names = [p.name for p in team_players]
        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_palauttaa_parhaat_pisteiden_mukaan(self):
        top_players = self.stats.top(1)
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_palauttaa_oikean_maaran_pelaajia(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)


if __name__ == "__main__":
    unittest.main()
