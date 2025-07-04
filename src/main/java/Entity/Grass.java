package Entity;

import java.util.Random;

public class Grass extends Entity {
    private final int density;

    public Grass(Coordinate coordinate, int density) {
        super(coordinate);
        this.density = set_density();
    }


    private int set_density() {
        Random random = new Random();
        int MAX_DENSITY = 3;
        return random.nextInt(MAX_DENSITY) + 1;
    }

    @Override
    public char getSymbol() {
        return '#';
    }

    public int getDensity() {
        return density;
    }
}
