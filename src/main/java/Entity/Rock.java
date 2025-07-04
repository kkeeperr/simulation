package Entity;

public class Rock extends Entity {


    public Rock(Coordinate coordinate) {
        super(coordinate);
    }

    @Override
    public char getSymbol() {
        return '*';
    }
}
