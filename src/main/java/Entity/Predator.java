package Entity;

public class Predator extends Creature {
    private final int damage;

    public Predator(Coordinate coordinate, int health, int speed, int damage) {
        super(coordinate, health, speed);
        this.damage = damage;
    }


    @Override
    public char getSymbol() {
        return 'P';
    }

    public int getDamage() { return damage; }

    @Override
    public void makeMove() {

    }
}
