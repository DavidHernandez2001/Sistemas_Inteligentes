import java.util.Scanner;

public class main {


    public static void main(String[] args) {
        Connect4MinMax game = new Connect4MinMax();
        Scanner scanner = new Scanner(System.in);

        // Iniciar el juego aleatoriamente
        game.iniciarJuegoAleatoriamente();
        System.out.println("Comienza el jugador " + game.currentPlayer);

        while (!game.isBoardFull()) {
            if (game.currentPlayer == 1) {
                // Turno del jugador humano
                System.out.print("Ingresa la columna donde quieres colocar tu ficha (0-6): ");
                int playerMove = scanner.nextInt();
                while (!game.isValidMove(playerMove)) {
                    System.out.println("Movimiento inválido. Inténtalo de nuevo.");
                    playerMove = scanner.nextInt();
                }
                game.makeMove(playerMove);
                game.printBoard();
            } else {
                // Turno de la computadora
                int computerMove = game.findBestMove();
                game.makeMove(computerMove);
                game.printBoard();
            }
        }

        // Verificar el resultado del juego
        int winner = game.checkWinner();
        if (winner == 1) {
            System.out.println("¡Has ganado!");
        } else if (winner == 2) {
            System.out.println("¡La computadora gana!");
        } else {
            System.out.println("¡Empate!");
        }

        scanner.close();
    }
        }
