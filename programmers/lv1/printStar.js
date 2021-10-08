process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    for(let i = 0; i < b; i++){
        for(let j = 0; j < a; j++){
            // 한줄 출력을 위한 process.stdout.write
            process.stdout.write('*');
        }
        console.log()
    }

    // repeat을 이용할 수 있음
    const start = '*'.repeat(a) // 문자를 a만큼 반복
    for(let i = 0; i < b; i++) {
        console.log(star)
    }

});