package Entity;

public class Rock extends Entity {
    public Rock(Coordinates position) {
        super(position);
    }

    @Override
    public String getSymbol() {
        return "🪨";
    }
}
