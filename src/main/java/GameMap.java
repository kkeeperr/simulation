import Entity.Coordinates;
import Entity.Entity;

import java.util.HashMap;
import java.util.Map;

public class GameMap {
    private final int width;
    private final int height;
    private Map<Coordinates, Entity> entities;

    public void setEntity(Coordinates coordinates, Entity entity) {
        entities.put(coordinates, entity);
    }

    public Map<Coordinates, Entity> getEntities() {
        return entities;
    }

    public GameMap(int width, int height) {
        this.width = width;
        this.height = height;
        entities = new HashMap<>();
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }
}
