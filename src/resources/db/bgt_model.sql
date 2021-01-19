CREATE TABLE IF NOT EXISTS games (
        game_name TEXT NOT NULL UNIQUE,
        min_players INTEGER NOT NULL,
        max_players INTEGER NOT NULL,
        round_time INTEGER NOT NULL,
        game_time INTEGER NOT NULL,
        game_type TEXT NOT NULL
    );
