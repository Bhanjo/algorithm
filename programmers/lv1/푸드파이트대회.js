function solution(food) {
  var answer = [0];
  const player1 = [];
  const player2 = [];

  for (let foodIndex = 1; foodIndex < food.length; foodIndex++) {
    let foodAmount = food[foodIndex];

    // Math.floor로도 구현 가능
    foodAmount % 2 !== 0 && (foodAmount -= 1);

    for (let i = 0; i < foodAmount; i++) {
      i % 2 === 0 ? player1.push(foodIndex) : player2.unshift(foodIndex);
    }
  }

  return player1.join('') + answer.join('') + player2.join('');
}
