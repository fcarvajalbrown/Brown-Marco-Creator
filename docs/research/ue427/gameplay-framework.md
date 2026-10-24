# Gameplay framework

Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-quick-reference-in-unreal-engine?application_version=4.27 and https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine?application_version=4.27

- All framework classes are Actors, placed in a level or spawned when needed. [docs]
- Pawn: an Actor that can be an agent in the world, possessed by a Controller, set up to accept input; not assumed humanoid. [docs]
- Character: a humanoid Pawn with a CapsuleComponent for collision and a CharacterMovementComponent by default; moves, replicates movement and has animation functionality. [docs]
- Controller: an Actor that directs a Pawn by possessing it; PlayerController stands for the human player, AIController for a simulated one. [docs]
- HUD: the 2D on-screen display, typically one per PlayerController. PlayerCameraManager: the player's view, also typically one per PlayerController. [docs]
- GameMode: the game's rules and win conditions; exists only on the server and should hold little changing data. [docs]
- GameState: the state of the game (connected players, score, mission progress); exists on server and all clients and replicates. [docs]
- PlayerState: per participant (human or bot simulating a player), on all machines, replicates; non-player AI has none. [docs]
- A game is a GameMode plus a GameState; joining players get PlayerControllers, which possess Pawns and own the HUD and PlayerCameraManager. [docs]
- Movement and game logic can live either in the Pawn or in its Controller. [docs]

## For Brown Marco Creator

Phase F builds this class set. Open: whether to keep the server-only GameMode / replicated GameState split before networking is in scope.
