package Entity;

public class Herbivore extends Creature {


    public Herbivore(Coordinate coordinate, int health, int speed) {
        super(coordinate, health, speed);
    }

    @Override
    public char getSymbol() {
        return 'H';
    }

    @Override
    public void makeMove() {

    }
}
