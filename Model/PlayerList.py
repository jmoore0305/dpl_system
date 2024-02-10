from DataStore import player_repo

class PlayerList:
    def __init__(self):
        self.players = []


    def load_player_list(self):
        players = [
            ('Justin', 'Moore'),
            ('Michelle', 'Patel'),
            ('Cooper', 'Bond'),
            ('Gabe', 'Mendez-Frances'),
            ('Aisha', 'Khan'),
            ('Ling', 'Wu'),
            ('Olivia', 'Smith'),
            ('Amir', 'Alavi'),
            ('Carlos', 'Garcia'),
            ('Nadia', 'Ivanova')
        ]

        for first_name, last_name in players:
            player_repo.add_player(first_name, last_name)

        self.players = player_repo.get_list()

    def get_player_list(self):
        return self.players

    def add_player(self, first_name, last_name):
        for player in self.players:
            if player['first_name'] == first_name and player['last_name'] == last_name:
                print(f"Player {first_name} {last_name} already exists in the list.")
                return

        player = {'first_name': first_name, 'last_name': last_name}
        self.players.append(player)
        print(f"Added player: {first_name} {last_name}")
        player_repo.add_player(first_name, last_name)

    def remove_player(self, first_name, last_name):
        protected_players = [
            ('Justin', 'Moore'),
            ('Michelle', 'Patel'),
            ('Cooper', 'Bond'),
            ('Gabe', 'Mendez-Frances'),
            ('Aisha', 'Khan'),
            ('Ling', 'Wu'),
            ('Olivia', 'Smith'),
            ('Amir', 'Alavi'),
            ('Carlos', 'Garcia'),
            ('Nadia', 'Ivanova')
        ]

        if (first_name, last_name) in protected_players:
            print(f"Player {first_name} {last_name} cannot be removed.")
            return

        for player in self.players:
            if player['first_name'] == first_name and player['last_name'] == last_name:
                self.players.remove(player)
                print(f"Removed player: {first_name} {last_name}")
                return

        print(f"Player {first_name} {last_name} not found in the list.")


    def print_players(self):
        """Print all players in the list."""
        if self.players:
            print("Player List:")
            for player in self.players:
                print(f"{player['first_name']} {player['last_name']}")
        else:
            print("No players in the list.")

        print("Now printing players in database: ")
        player_repo.print_all_players()