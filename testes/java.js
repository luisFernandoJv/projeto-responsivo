function ValidaCPF(cpfEnviado){
    Object.defineProperty(this, 'cpfLimpo',{
        enumerable: true,
        get: function(){
            return cpfEnviado.replace(/\D+/g, '');
        }
    });
}

ValidaCPF.prototype.valida = function(){

    if(typeof this.cpfLimpo === 'undefined') return false;
    if(this.cpfLimpo.length !== 11) return false;
    if(this.isSequencia()) false;

    const cpfParcial = this.cpfLimpo.slice(0, -2);
    const digito1 = this.criaDigito(cpfParcial);
    const digito2 = this.criaDigito(cpfParcial + digito1);

    const novoCpf = cpfParcial + digito1 + digito2;

   

    return novoCpf == this.cpfLimpo;
};
ValidaCPF.prototype.criaDigito = function(parcial){
    const cpfArray = Array.from(parcial);
    let regressivo = cpfArray.length + 1;
    const total = cpfArray.reduce((ac, val) => {

        ac += (regressivo * Number(val));
        regressivo--;

        
        return ac;
    }, 0);

    const digito = 11 - (total % 11);
    return digito > 9 ? '0' : String(digito);

};

ValidaCPF.prototype.isSequencia = function(){
    const sequencia =  this.cpfLimpo[0].repeat(this.cpfLimpo.length);
    return sequencia === this.cpfLimpo;


}


const cpf = new ValidaCPF('121.506.014-94');
console.log(cpf.valida());