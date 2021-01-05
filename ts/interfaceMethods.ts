interface IGeometricFigure {
  area: () => number;
  perimeter: () => number;
}

export class Square implements IGeometricFigure {
  side: number;

  constructor (side: number) {this.side = side};

  area(): number {
      return this.side*this.side
  };

  perimeter(): number {
    return 4*this.side
  };
}

export class Circle implements IGeometricFigure {
  radius: number;

  constructor (radius: number) {this.radius = radius};

  area(): number {
    return Math.PI*this.radius*this.radius
  };

  perimeter(): number {
    return 2*Math.PI*this.radius
  };
}
