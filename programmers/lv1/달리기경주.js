function solution(players, callings) {
  const calledCount = {};
  players.forEach((name, index) => {
    calledCount[name] = index;
  });

  callings.forEach((name, index) => {
    const calledPlayerRank = calledCount[name];
    const switchTarget = players[calledPlayerRank - 1];

    players[calledPlayerRank - 1] = callings[index];
    players[calledPlayerRank] = switchTarget;

    calledCount[name] = calledPlayerRank - 1;
    calledCount[switchTarget] = calledPlayerRank;
  });

  return players;
}
