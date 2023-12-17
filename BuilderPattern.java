class Car {
    private String color;
    private int numberOfWheels;
    private String name;
    private String model;

    private Car(
            String color, int numberOfWheels, String name, String model) {
        this.color = color;
        this.numberOfWheels = numberOfWheels;
        this.name = name;
        this.model = model;
    }

    public String getColor() { return color; }
    public int getNumberOfWheels() { return numberOfWheels; }
    public String getName() { return name; }
    public String getModel() { return model; }
    
    // I rly like the idea of creating an 'inner builder' from the very
    // beginning, because this closes the constructor of the 'Car' class,
    // so the client's code won't be able to instantiate the 'Car'
    // class directly.

    static class CarBuilder {
        private String color;
        private int numberOfWheels;
        private String name;
        private String model;

        public CarBuilder color(String color) {
            this.color = color;
            return this;
        }

        public CarBuilder numberOfWheels(int numberOfWheels) {
            this.numberOfWheels = numberOfWheels;
            return this;
        }
    
        public CarBuilder name(String name) {
            this.name = name;
            return this;
        }
    
        public CarBuilder model(String model) {
            this.model = model;
            return this;
        }
    
        public Car build() { return new Car(color, numberOfWheels, name, model); }
    }
}

class Director {
    public static void presetRedBMWX6(Car.CarBuilder carBuilderObj) {
        carBuilderObj.color("Red").numberOfWheels(4).name("BMW").model("X6");
    }

    public static void presetBlueBMWX6(Car.CarBuilder carBuilderObj) {
        carBuilderObj.color("Blue").numberOfWheels(4).name("BMW").model("X6");
    }
}

class EntryPoint {
    public static void main(String[] args) {
        Car.CarBuilder carBuilder = new Car.CarBuilder();
        Director.presetRedBMWX6(carBuilder);
        System.out.print(carBuilder.build());
    }
}
