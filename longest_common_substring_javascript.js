// Write a JS program that finds the longest common substring between two strings.

let str1 = 'ABABC'
let str2 = 'BABCA'

function lengestSubString(str1,str2) {

    const arr = Array(str2.length + 1).fill(null).map(() =>{
        return Array(str1.length +1).fill(null);
    })


    for (let j =0; j<= str1.length; j +=1){
        arr[0][j] = 0
    }
    for (let i =0; i<= str2.length; i +=1){
        arr[i][0] = 0
    }

    let len = 0
    let col = 0
    let row = 0

    for (let i =1; i<= str2.length; i +=1){
        for (let j =1; j<= str1.length; j +=1){
            if(str1[j-1] === str2[i-1]){
                arr[i][j] = arr[i-1][j-1] + 1
            } else{
                arr[i][j] = 0;
            }
            if (arr[i][j] >len){
                len = arr[i][j];
                col=j;
                row= i;

            }
                
        }
    }
    if (len === 0){
        return ''
    }
    let res = ''

    while(arr[row][col] > 0){
        res = str1[col-1] + res;
        row -= 1;
        col -= 1;
    }
    return res
}


let output = lengestSubString(str1,str2)
console.log(output)