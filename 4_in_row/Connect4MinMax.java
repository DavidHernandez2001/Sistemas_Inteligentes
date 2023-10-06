import java.util.Random;

public class Connect4MinMax {
    private int[][] board;
    int currentPlayer;

    public Connect4MinMax() {
        board = new int[6][7];
        currentPlayer = 1;
        // Inicializa el tablero con todas las casillas vacías (0)
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 7; j++) {
                board[i][j] = 0;
            }
        }
    }

    public void makeMove(int column) {
        if (column < 0 || column >= 7 || board[0][column] != 0) {
            System.out.println("Movimiento inválido. Inténtalo de nuevo.");
            return;
        }

        // Realiza el movimiento
        for (int row = 5; row >= 0; row--) {
            if (board[row][column] == 0) {
                board[row][column] = currentPlayer;
                break;
            }
        }

        currentPlayer = 3 - currentPlayer; // Cambia al siguiente jugador
    }

    public int minimax(int depth, boolean isMaximizingPlayer) {
        int winner = checkWinner();
        if (winner != 0) {
            if (winner == 1) {
                return -1; // Jugador 1 (humano) gana
            } else if (winner == 2) {
                return 1; // Jugador 2 (computadora) gana
            } else {
                return 0; // Empate
            }
        }

        if (depth == 0) {
            return 0; // Límite de profundidad alcanzado
        }

        if (isMaximizingPlayer) {
            int bestScore = Integer.MIN_VALUE;
            for (int col = 0; col < 7; col++) {
                if (isValidMove(col)) {
                    makeMove(col);
                    int score = minimax(depth - 1, false);
                    undoMove(col);
                    bestScore = Math.max(bestScore, score);
                }
            }
            return bestScore;
        } else {
            int bestScore = Integer.MAX_VALUE;
            for (int col = 0; col < 7; col++) {
                if (isValidMove(col)) {
                    makeMove(col);
                    int score = minimax(depth - 1, true);
                    undoMove(col);
                    bestScore = Math.min(bestScore, score);
                }
            }
            return bestScore;
        }
    }

    public int findBestMove() {
        int bestScore = Integer.MIN_VALUE;
        int bestMove = -1;
        for (int col = 0; col < 7; col++) {
            if (isValidMove(col)) {
                makeMove(col);
                int score = minimax(8, false); // Ajusta la profundidad aquí
                undoMove(col);
                if (score > bestScore) {
                    bestScore = score;
                    bestMove = col;
                }
            }
        }
        return bestMove;
    }

    public boolean isValidMove(int column) {
        return column >= 0 && column < 7 && board[0][column] == 0;
    }

    public void undoMove(int column) {
        for (int row = 0; row < 6; row++) {
            if (board[row][column] != 0) {
                board[row][column] = 0;
                break;
            }
        }
    }

    public int checkWinner() {
        // Comprobar horizontalmente
        for (int row = 0; row < 6; row++) {
            for (int col = 0; col < 4; col++) {
                int player = board[row][col];
                if (player != 0 && player == board[row][col + 1] && player == board[row][col + 2] && player == board[row][col + 3]) {
                    return player;
                }
            }
        }

        // Comprobar verticalmente
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 7; col++) {
                int player = board[row][col];
                if (player != 0 && player == board[row + 1][col] && player == board[row + 2][col] && player == board[row + 3][col]) {
                    return player;
                }
            }
        }

        // Comprobar diagonalmente hacia abajo
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 4; col++) {
                int player = board[row][col];
                if (player != 0 && player == board[row + 1][col + 1] && player == board[row + 2][col + 2] && player == board[row + 3][col + 3]) {
                    return player;
                }
            }
        }

        // Comprobar diagonalmente hacia arriba
        for (int row = 3; row < 6; row++) {
            for (int col = 0; col < 4; col++) {
                int player = board[row][col];
                if (player != 0 && player == board[row - 1][col + 1] && player == board[row - 2][col + 2] && player == board[row - 3][col + 3]) {
                    return player;
                }
            }
        }

        // Si no hay ganador
        return 0;
    }

    public boolean isBoardFull() {
        for (int row = 0; row < 6; row++) {
            for (int col = 0; col < 7; col++) {
                if (board[row][col] == 0) {
                    // Si alguna casilla está vacía, el tablero no está lleno
                    return false;
                }
            }
        }
        // Si no se encontraron casillas vacías, el tablero está lleno
        return true;
    }



    public void printBoard() {
        System.out.println("  0 1 2 3 4 5 6");
        System.out.println("+-+-+-+-+-+-+-+");

        for (int i = 0; i < 6; i++) {
            System.out.print("|");
            for (int j = 0; j < 7; j++) {
                int player = board[i][j];
                String symbol = player == 1 ? "X" : (player == 2 ? "O" : " ");
                System.out.print(symbol + "|");
            }
            System.out.println("\n+-+-+-+-+-+-+-+");
        }
    }

    public void iniciarJuegoAleatoriamente() {
        Random random = new Random();
        currentPlayer = random.nextInt(2) + 1; // 1 o 2 al azar
    }
}

