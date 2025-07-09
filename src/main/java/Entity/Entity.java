package Entity;

public abstract class Entity {
    Coordinates position;

    public Entity(Coordinates position) {
        this.position = position;
    }

    public void setPosition(Coordinates position) {
        this.position = position;
    }

    public Coordinates getPosition() {
        return position;
    }

    public abstract String getSymbol();
}
