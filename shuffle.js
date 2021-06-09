const faker = require('faker');

function shuffle(array) {
  let currentIndex = array.length,
    randomIndex;

  while (0 !== currentIndex) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex],
      array[currentIndex],
    ];
  }

  return array;
}

const size = 40;
let array = [];

for (let i = 0; i < size; i++) {
  array.push(i + 1);
}

const users = [];

const shuffleArray = () => {
  shuffle(array);
  array.forEach((el) => console.log(el));
};

const createUsers = () => {
  array.forEach((el) => {
    users.push({ hostname: `machine-00${el}`, name: faker.name.findName() });
  });

  //   console.log(
  //     `{"users": [${[
  //       users.map((u) => ({ name: u.name, hostname: u.hostname })),
  //     ]}}]`
  //   );

  console.log(users);
};

// shuffleArray();
createUsers();
