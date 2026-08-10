# Python Chess

A two-player desktop chess application built with Python and Pygame. The project began as a guided exercise and grew into a larger exploration of chess rules, game-state management, interface design, and data persistence.

## Why this project matters

Chess creates a useful engineering challenge because a legal action depends on more than a piece's movement pattern. The application must coordinate board occupancy, turn ownership, captures, king safety, and special moves while keeping the interface synchronized with the active game state.

This repository demonstrates continued development beyond the original tutorials, including independently added rule handling and gameplay feedback.

## Implemented gameplay

- Legal movement generation for pawns, rooks, knights, bishops, queens, and kings
- Alternating white and black turns
- Friendly-piece blocking and opponent captures
- Valid-move previews for the selected piece
- Check detection and visual feedback
- King-side and queen-side castling
- En passant handling
- Pawn promotion to bishop, knight, rook, or queen
- Captured-piece display
- Move-history display supporting long games
- Forfeit, game-over, and restart flows

## Architecture

The current implementation is divided across three primary modules:

- `main.py` coordinates move generation, rule evaluation, turn flow, and the Pygame event loop.
- `service_functions.py` contains reusable drawing, board-list, move-history, and utility functions.
- `constants.py` initializes Pygame, loads assets, and defines shared board and game state.

The code uses coordinate tuples and parallel piece/location collections to represent the board. Candidate moves are calculated by piece type and filtered against occupied squares and board boundaries before the active turn can apply them.

## Persistence experiment

The repository includes schema and function experiments for recording games, moves, captures, checks, castling, promotions, and completed matches in MySQL. These integrations are currently commented out in the active branch, so the playable application should be treated as an in-memory Pygame game rather than a production-persistent system.

That distinction is intentional in this README: the persistence work documents an architectural direction and prior experiment, not a currently enabled runtime dependency.

## Run locally

### Prerequisites

- Python 3.12 or newer
- Pygame

Install Pygame:

```bash
python -m pip install pygame
```

Start the game from the repository root:

```bash
python main.py
```

The application loads piece and interface images from `assets/images`, so run it with the repository root as the working directory.

## Current limitations

- The game uses module-level mutable state, which makes isolated testing and replay more difficult.
- Rule handling, drawing, and turn coordination still have areas of tight coupling.
- Automated rule tests are not yet included.
- MySQL persistence code is not enabled in the active branch.
- The interface is designed for a fixed desktop window rather than responsive scaling.

## Good next steps

1. Introduce `Board`, `GameState`, `Move`, and piece-domain classes.
2. Separate candidate-move generation from final king-safety validation and state mutation.
3. Add automated tests for castling, en passant, promotion, pins, check, and game-over states.
4. Replace parallel lists with a single authoritative board model.
5. Reintroduce persistence behind a repository or service boundary.
6. Add saved-game loading only after moves can be serialized and replayed deterministically.

## Learning foundation

The project began with these tutorials before moving into additional experimentation and independently developed features:

- [Creating Chess in Python](https://www.youtube.com/watch?v=X-e0jk4I938)
- [Additional Pygame chess development](https://www.youtube.com/watch?v=s2Dd_obh3fM)

## Portfolio context

This project complements the C# and React chess applications in my portfolio. Together, they show how the same rules-heavy domain can be approached through procedural Pygame state, object-oriented .NET architecture, and component-based React/TypeScript design.
