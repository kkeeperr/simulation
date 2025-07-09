import Entity.Coordinates;
import Entity.Entity;

import java.sql.SQLOutput;

public class MapConsoleRenderer {
    private static final String ANSI_RESET = "\033[0m";
    private static final String CLEAR_SCREEN_ANSI = "\033[H\033[2J";

    public void render(GameMap gameMap) {
        System.out.println(CLEAR_SCREEN_ANSI);
        System.out.flush();

        StringBuilder frameBuffer = new StringBuilder();
        for (int x = 0; x < gameMap.getHeight(); x++) {
            String line = "";
            for (int y = 0; y < gameMap.getWidth(); y++) {
                Coordinates currentCoordinates = new Coordinates(x, y);
                Entity entity = gameMap.getEntities().get(currentCoordinates);

                String spriteToDraw;
                if (entity != null) {
                    spriteToDraw = entity.getSymbol();
                } else {
                    spriteToDraw = "\uD83C\uDFFF";
                }
                frameBuffer.append(spriteToDraw).append(ANSI_RESET);
            }
            frameBuffer.append("\n");
        }
        System.out.println(frameBuffer.toString());
        System.out.flush();
    }
}
