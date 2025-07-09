package Entity;

import java.util.Random;

public class Grass extends Entity {
    private final int density;

    public Grass(Coordinates position) {
        super(position);
        this.density = set_density();
    }


    private int set_density() {
        Random random = new Random();
        int MAX_DENSITY = 3;
        return random.nextInt(MAX_DENSITY) + 1;
    }

    @Override
    public String getSymbol() {
        return "\uD83C\uDF3F";
    }

    public int getDensity() {
        return density;
    }
}
