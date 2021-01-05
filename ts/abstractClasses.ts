export abstract class Animal {
  /** @param {number} value The length of the animal in parrots. */
  protected constructor(public value: number) {}

  convertTo (someone: Animal): number {
    return this.value / someone.value
  }
}

export class Boa extends Animal {
  constructor() {
    super(38);
  }
}

export class Parrot extends Animal {
  constructor() {
    super(1);
  }
}

export class Monkey extends Animal {
  constructor() {
    super(38/5);
  }
}

const boa = new Boa();
const monkey = new Monkey();
const parrot = new Parrot();

console.log(boa.convertTo(parrot) == 38);
console.log(boa.convertTo(monkey) == 5);
