export class Serializable {

  serialize(): string {
    let result: { [index: string]: string } = {};
    for (let key of Object.getOwnPropertyNames(this)) {
      result[key] = (this as any)[key as any];
    }
    return JSON.stringify(result)
  }

  deserialize(source: string): void {
    let obj = JSON.parse(source);
    console.log(obj)
    let result: { [index: string]: string } = {};
    for (let key of Object.keys(obj)) {
      Object.defineProperty(this, key, {
        value: (obj as any)[key as any],
        writable: true
      })
    }
    console.log(result)
  }
}

class Person implements Serializable {
  constructor(public firstName?: string, public lastName?: string) {}
  // @ts-ignore strictPropertyInitialization
  serialize: () => string;
  // @ts-ignore strictPropertyInitialization
  deserialize: (source: string) => void;
}

function applyMixins(derivedCtor: any, baseCtors: any[]) {
  baseCtors.forEach(baseCtor => {
    Object.getOwnPropertyNames(baseCtor.prototype).forEach(name => {
      derivedCtor.prototype[name] = baseCtor.prototype[name];
    });
  });
}

applyMixins(Person, [Serializable]);

const sourcePerson = new Person('John', 'Galt');
const serializedPerson = sourcePerson.serialize();
const resultPerson = new Person();
resultPerson.deserialize(serializedPerson);

console.log(serializedPerson)
console.log(resultPerson.firstName)
console.log(resultPerson.firstName == 'John')
console.log(resultPerson.deserialize(serializedPerson))
