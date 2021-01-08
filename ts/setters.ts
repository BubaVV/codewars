declare var ICuboid: {
  new (length: number): ICuboid;
}

interface ICuboid {
  /** Length of the cube */
  length: number;
  /** Surface area of the cube */
  surfaceArea: number;
  /** Volume of the cube */
  volume: number;
}

export class Cube implements ICuboid {
  constructor(public length: number) {}

  get surfaceArea() {
    return 6 * this.length * this.length
  }

  set surfaceArea(area: number) {
    this.length = Math.sqrt(area / 6)
  }

  get volume() {
    return Math.pow(this.length, 3)
  }

  set volume(area: number) {
    this.length = Math.pow(area, 1/3)
  }
}
