import Entity.*;

public class Simulation {
    public static void main(String[] args) {
        GameMap gameMap = new GameMap(15, 15);
        gameMap.setEntity(new Coordinates(1, 1), new Grass(new Coordinates(1,1)));
        gameMap.setEntity(new Coordinates(1, 5), new Rock(new Coordinates(1,5)));
        gameMap.setEntity(new Coordinates(2, 3), new Predator(new Coordinates(2,3), 10, 2, 1));
        gameMap.setEntity(new Coordinates(3, 5), new Herbivore(new Coordinates(3,5), 10, 1));

        MapConsoleRenderer renderer = new MapConsoleRenderer();
        renderer.render(gameMap);

        int a = 123;
    }
}
