package Entity;

public abstract class Creature extends Entity {
    private final int health;
    private final int speed;

    public Creature(Coordinates position, int health, int speed) {
        super(position);
        this.health = health;
        this.speed = speed;
    }

    public abstract void eats();

    public abstract void makeMove();

    public int getHealth() { return health; }
    public int getSpeed() { return speed; }
}
