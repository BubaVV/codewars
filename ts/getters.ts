export class Cuboid {
  constructor (public length: number, public width: number, public height: number) {}


get surfaceArea(): number {
  return 2 * (this.width * this.length + this.width * this.height + this.length * this.height)
}

get volume(): number {
  return this.height * this.width * this.length
}
}

export class Cube extends Cuboid {
  constructor (public length: number) {
    super(length, length, length)
  }
}
