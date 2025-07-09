package Entity;

public class Herbivore extends Creature {


    public Herbivore(Coordinates position, int health, int speed) {
        super(position, health, speed);
    }

    @Override
    public String getSymbol() {
        return "\uD83D\uDC30";
    }

    @Override
    public void eats() {

    }

    @Override
    public void makeMove() {

    }
}
