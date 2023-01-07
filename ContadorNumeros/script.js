function Verificar() {
    let numf = document.getElementById('numf')
    let nump = document.getElementById('nump')
    let num = document.getElementById('num')
    let res = document.getElementById('res')


    if (num.value.length == 0 || numf.value.length == 0 || nump.value.length == 0) {
        res.innerHTML = 'DIGITE UM NÚMERO INICIAL'
    } else {
        let f = Number(numf.value)
        let p = Number(nump.value)
        let i = Number(num.value)
        if (i < f) {
            for (let n = i; n <= f; n += p) {
                res.innerHTML += ` ${n}, `

            }

        } else {
            for (let n = i; n >= f; n -= p) {
                res.innerHTML += `${n}, `
            }
        }
    }
}

