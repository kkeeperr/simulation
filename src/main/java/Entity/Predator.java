package Entity;

public class Predator extends Creature {
    private final int damage;

    public Predator(Coordinates position, int health, int speed, int damage) {
        super(position ,health, speed);
        this.damage = damage;
    }


    @Override
    public String getSymbol() {
        return "🐺";
    }

    public int getDamage() { return damage; }

    @Override
    public void eats() {

    }

    @Override
    public void makeMove() {

    }
}
