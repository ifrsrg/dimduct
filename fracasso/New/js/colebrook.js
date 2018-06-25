
/**
 * Resolve a equação de Colebrook-White chutando valores para igualar os dois lado dela.
 * 
 * @author Veigaribo
 * 
 * @param {number} rel_roughness - A rugosidade relativa do duto, calculada como a altura média das irregularidades da superfície (rugosidade absoluta) sobre o diâmetro do duto.
 * @param {number} reynold       - O número de Reynolds (Re) é uma constante do fluido em questão definida como Re = ρuL/μ, onde ρ é a densidade do fluido, u é a velocidade do fluido (relativa ao duto), L é a longitude característica do fluxo (diâmetro do duto) e μ é a viscosidade do fluido.
 * @param {number} [x0 = 0.15]   - O valor arbitrário da qual a função irá começar a testar.
 * @param {number} [tol = 1e-10] - Um valor relativo à diferença dos dois lados da equação onde a função parará; isto é, o ponto onde os dois lados serão considerados iguais. A função parará quando um lado dividido pelo o outro for 1+-tol ou mais próximo de 1.
 * 
 * @returns uma aproximação para o valor do fator de atrito de Darcy-Weisbach.
*/
function colebrook(rel_roughness, reynold, x0=.15, tol=1e-10){

    //Dois lados da equação
    left = 1/( Math.sqrt(x0) );
    right = -2 * Math.log10( (rel_roughness / 3.71) + (2.51 / ( reynold*Math.sqrt(x0) )) );

    //O quão diferente os dois foram
    let fator = left/right;

    //Se a diferença for aceitavelmente baixa, o valor de x é retornado
    if( Math.abs(1-fator) <= tol){
        return x0;
    }

    //Se a diferença for muito grande, adiciona um outro multiplicador
    //Não testei pra saber o quão bem isso funciona
    /*var fdof = 1;
    if(left - right > 1){
        fdof = left-right-1;
        fdof /= 2;
        fdof += 1;
    } else if(right - left > 1){
        fdof = right - left - 1;
        fdof /= 2;
        fdof += 1;
        fdof = 1/fdof;
    }*/

    //Multiplica o valor atual de x pelo fator e pelo fdof e repete
    return colebrook(rel_roughness, reynold, x0*fator/**fdof*/, tol);

}

//

function d_e_u(f, larg, theta, recup, vel_i, vazao, d0=0.5, u0=5, tol=1e-10){

    d_novo = (f * larg / d0 + 0.1 * theta / 90.0 + recup) * Math.pow(u0, 2.0) - recup * Math.pow(vel_i, 2.0);
    u_novo = d0 - math.sqrt((4.0 * vazao) / (Math.PI * u0));

    let fator = d_novo+u_novo;

    if( Math.abs(1-fator) <= tol){
        return {d: d_novo, u: u_novo};
    }

    return d_e_u(f, larg, theta, recup, vel_i, vazao, d0, u0, tol);

}
